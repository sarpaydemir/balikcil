#!/usr/bin/env python3
"""
15_event_collapse.py -- the event-collapse engine RULES 13 / TACTICS 7 need.

What it does
------------
Turns a list of moments (id, coin, kind, start hour) into a PARTITION into
events, under every candidate reading of "the same hour" that the written
rules allow, and measures each reading. It then calibrates what collapsing
does to a shuffle: the 1% boundary of the null distribution under a card-level
shuffle (what TACTICS 7 says today, uncollapsed) against a cluster-level
(block) shuffle over the events.

It also exposes `collapse()` and `block_shuffle_indices()` so the later judge
script imports the same code instead of writing the rule a second time.

Input   : cards/C###.md  (default)  -- or --moments CSV with columns
          id,coin,kind,start_hour_utc  (ISO, e.g. 2026-05-07T20:00Z)
Output  : exam-prep/collapse/events.csv
          exam-prep/collapse/collapse-summary.csv
          exam-prep/collapse/shuffle-calibration.csv
          exam-prep/collapse/collapse-manifest.md
          exam-prep/collapse/runs/<run16>.json   (append-only)

Rules implemented
-----------------
RULES 13  : "Moments occurring in several coins in the same hour count as a
            single event."  This script does not CHOOSE which reading of that
            sentence is right -- it builds all of them and measures them. The
            choice is an open question under RULES 33 and is named in
            exam-prep/N-1-collapse.md.
TACTICS 7 : "A moment appearing in several cards in the same hour counts as a
            single event."  Same sentence, same treatment.
RULES 12  : the shuffle count (1000) and the 1% boundary come from this rule,
            not from here.
RULES 19  : every number written is counted; nothing is estimated.
RULES 23  : the clock is read from the system.
RULES 28  : free disk space is read and recorded (no download happens).
RULES 29  : the run number is the SHA-256 of the inputs, including this file.
RULES 30  : the run record is append-only; differing content stops the script.

Constants -- where each came from
---------------------------------
SHUFFLES = 1000        RULES 12: "the answers are shuffled 1,000 times".
TOP_FRACTION = 0.01    RULES 12: "the real result must fall inside the best 1%".
SEED = 20260913        TACTICS 1's draw number, "written before the draw; it
                       does not change". Not a number chosen here.
MOVE_WINDOW_HOURS = 24 TACTICS 2: a moment is a 24-hour movement.
CARD_SPAN_HOURS  = 48  TACTICS 3 / the card text: before 24 h + after 24 h.

No threshold, score or trading rule is defined anywhere in this file.
"""

import argparse
import csv
import datetime as dt
import hashlib
import json
import os
import random
import shutil
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lab_cards  # noqa: E402

SHUFFLES = 1000
TOP_FRACTION = 0.01
SEED = 20260913
MOVE_WINDOW_HOURS = 24
CARD_SPAN_HOURS = 48

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS_DIR = os.path.join(REPO, "cards")
OUT_DIR = os.path.join(REPO, "exam-prep", "collapse")
RUNS_DIR = os.path.join(OUT_DIR, "runs")

# The candidate readings of "in the same hour".  Each is a (name, rule) pair.
#   start-hour  : the moments begin in the same clock hour.
#                 (TACTICS 2: "A moment's start is the hour at which the
#                  24-hour movement began.")
#   move-window : the 24-hour movements themselves share a clock hour,
#                 i.e. |start gap| <= 23 h.
#   card-span   : the 48-hour card spans share a clock hour, i.e.
#                 |start gap| <= 47 h.  This is the relation measured by
#                 14_overlap_map.py.
DEFINITIONS = {
    "start-hour": 0,
    "move-window": MOVE_WINDOW_HOURS - 1,
    "card-span": CARD_SPAN_HOURS - 1,
}

# How an overlap relation that is not transitive is turned into a partition.
#   component    : transitive closure -- anything chained together is one event.
#   greedy-clique: repeatedly take the clock hour covered by the most
#                  still-unassigned moments (ties: earliest hour, then lowest
#                  id), make those moments one event, remove them, repeat.
#                  A stated convention, not an observation: some rule is needed
#                  because a set of overlapping intervals has no unique
#                  partition into "groups sharing an hour".
RESOLUTIONS = ("component", "greedy-clique")

# Whether two moments of the SAME coin may be merged.
#   any        : yes.
#   cross-coin : no -- RULES 13 says "in several coins", and same-coin spacing
#                is the separate open question Sofia refuses to answer (her §8).
SCOPES = ("any", "cross-coin")


def die(msg):
    sys.stderr.write("STOP: %s\n" % msg)
    sys.exit(1)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_hour(s):
    s = s.strip().replace("Z", "")
    if len(s) == 16:                       # 2026-05-07T20:00
        s += ":00"
    return dt.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S").replace(
        tzinfo=dt.timezone.utc)


def fmt_hour(t):
    return t.strftime("%Y-%m-%dT%H:00Z")


# ---------------------------------------------------------------------------
# The engine.  These two functions are the ones a later script imports.
# ---------------------------------------------------------------------------

def collapse(moments, definition="start-hour", resolution="component",
             scope="any"):
    """moments: list of dicts with id, coin, start_dt (datetime).

    Returns a list of events; each event is a list of moment ids, and the
    events partition the input exactly once. Deterministic: no randomness.
    """
    if definition not in DEFINITIONS:
        raise ValueError("unknown definition %r" % definition)
    if resolution not in RESOLUTIONS:
        raise ValueError("unknown resolution %r" % resolution)
    if scope not in SCOPES:
        raise ValueError("unknown scope %r" % scope)

    gap = DEFINITIONS[definition]
    items = sorted(moments, key=lambda m: (m["start_dt"], m["id"]))

    def joinable(a, b):
        if scope == "cross-coin" and a["coin"] == b["coin"]:
            return False
        d = abs((a["start_dt"] - b["start_dt"]).total_seconds()) / 3600.0
        return d <= gap

    if resolution == "component" or definition == "start-hour":
        # union-find over the joinable relation
        parent = {m["id"]: m["id"] for m in items}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[max(rx, ry)] = min(rx, ry)

        for i, a in enumerate(items):
            for b in items[i + 1:]:
                d = (b["start_dt"] - a["start_dt"]).total_seconds() / 3600.0
                if d > gap:
                    break
                if joinable(a, b):
                    union(a["id"], b["id"])
        groups = defaultdict(list)
        for m in items:
            groups[find(m["id"])].append(m["id"])
        events = [sorted(v) for v in groups.values()]
        events.sort(key=lambda g: g[0])
        return events

    # greedy-clique
    left = list(items)
    events = []
    while left:
        # candidate clock hours: every moment's start hour, and every hour a
        # moment's window reaches back to. A covering window of width `gap`
        # only needs to be tried with its left edge at some moment's start.
        best = None
        for anchor in left:
            lo = anchor["start_dt"]
            members = [m for m in left
                       if 0 <= (m["start_dt"] - lo).total_seconds() / 3600.0
                       <= gap]
            if scope == "cross-coin":
                seen, keep = set(), []
                for m in members:            # at most one card per coin
                    if m["coin"] in seen:
                        continue
                    seen.add(m["coin"])
                    keep.append(m)
                members = keep
            key = (-len(members), lo, members[0]["id"])
            if best is None or key < best[0]:
                best = (key, members)
        members = best[1]
        events.append(sorted(m["id"] for m in members))
        ids = {m["id"] for m in members}
        left = [m for m in left if m["id"] not in ids]
    events.sort(key=lambda g: g[0])
    return events


def block_shuffle_indices(events, id_order, rng):
    """One cluster-level (block) permutation.

    Returns a list of positions: position i of the returned list says which
    card's answer is read for card i. Whole events keep their internal
    pattern; only whole events are moved. This is what a shuffle must do when
    the cards inside an event are not independent observations (RULES 13).
    """
    pos = {cid: i for i, cid in enumerate(id_order)}
    blocks = [[pos[c] for c in ev] for ev in events]
    order = list(range(len(blocks)))
    rng.shuffle(order)
    slots = [p for b in blocks for p in b]          # target positions
    donors = [p for i in order for p in blocks[i]]  # source positions
    out = [None] * len(id_order)
    for s, d in zip(slots, donors):
        out[s] = d
    return out


def quantile_top(values, fraction):
    """The boundary of the best `fraction` of a null distribution: the value
    such that only `fraction` of draws are >= it. RULES 12's "best 1%"."""
    s = sorted(values, reverse=True)
    idx = max(0, int(round(fraction * len(s))) - 1)
    return s[idx]


def chance_line(answers, labels, events, id_order, mode, shuffles=SHUFFLES,
                fraction=TOP_FRACTION, seed=SEED):
    """The RULES 12 chance line, computed so that it CANNOT be computed
    without an event map.

    answers / labels : one entry per id, in `id_order`.
    events           : the partition returned by collapse().
    mode             : "block"          -- keep every card, permute whole
                                           events (cluster-level permutation);
                       "representative" -- keep one card per event (earliest
                                           start hour is chosen by the caller,
                                           so the caller passes the reduced
                                           lists and events of size 1).
    There is deliberately no card-level mode and no default mode: TACTICS 7
    says a moment appearing in several cards in the same hour counts as a
    single event, and a judge who wants the un-collapsed line has to write it
    himself rather than pick it off a default.

    Returns (observed, boundary, null_distribution).
    """
    if mode not in ("block", "representative"):
        raise ValueError("mode must be 'block' or 'representative'")
    if not (len(answers) == len(labels) == len(id_order)):
        raise ValueError("answers, labels and id_order must be the same length")
    flat = sorted(c for ev in events for c in ev)
    if flat != sorted(id_order):
        raise ValueError("the events do not partition id_order exactly")
    observed = sum(1 for a, l in zip(answers, labels) if a == l) / len(labels)
    rng = random.Random(seed)
    null = []
    if mode == "block":
        for _ in range(shuffles):
            idx = block_shuffle_indices(events, id_order, rng)
            null.append(sum(1 for i, l in zip(idx, labels)
                            if answers[i] == l) / len(labels))
    else:
        if any(len(ev) != 1 for ev in events):
            raise ValueError("representative mode needs one card per event; "
                             "reduce the inputs before calling")
        perm = list(answers)
        for _ in range(shuffles):
            rng.shuffle(perm)
            null.append(sum(1 for a, l in zip(perm, labels)
                            if a == l) / len(labels))
    return observed, quantile_top(null, fraction), null


# ---------------------------------------------------------------------------
# Measurement
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--moments", default=None,
                    help="CSV with id,coin,kind,start_hour_utc; "
                         "default: read the 306 observation cards")
    ap.add_argument("--out", default=OUT_DIR)
    args = ap.parse_args()

    started = dt.datetime.now(dt.timezone.utc)
    free_bytes = shutil.disk_usage(REPO).free

    # ---- input -------------------------------------------------------------
    input_desc = []
    moments = []
    if args.moments:
        with open(args.moments, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                moments.append({"id": row["id"], "coin": row["coin"],
                                "kind": row["kind"],
                                "start_dt": parse_hour(row["start_hour_utc"])})
        input_desc.append((os.path.relpath(args.moments, REPO),
                           sha256_file(args.moments)))
    else:
        cards = lab_cards.load_all(CARDS_DIR)
        for c in cards:
            moments.append({"id": c["card"], "coin": c["coin"],
                            "kind": c["kind"],
                            "start_dt": parse_hour(c["start_hour_utc"])})
            input_desc.append(("cards/%s.md" % c["card"], c["sha256"]))
    if not moments:
        die("no moments read")
    ids = [m["id"] for m in moments]
    if len(set(ids)) != len(ids):
        die("duplicate moment ids in the input")
    by_id = {m["id"]: m for m in moments}
    id_order = sorted(ids)

    # ---- run number (RULES 29) --------------------------------------------
    script_sha = sha256_file(os.path.abspath(__file__))
    h = hashlib.sha256()
    h.update(("script:" + script_sha + "\n").encode())
    h.update(("module:" + sha256_file(
        os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "lab_cards.py")) + "\n").encode())
    h.update(("shuffles:%d;top:%s;seed:%d\n"
              % (SHUFFLES, TOP_FRACTION, SEED)).encode())
    for name, sha in sorted(input_desc):
        h.update(("%s:%s\n" % (name, sha)).encode())
    run_full = h.hexdigest()
    run16 = run_full[:16]

    # ---- every configuration ----------------------------------------------
    configs = [("none", "none", "none")]
    for d in ("start-hour", "move-window", "card-span"):
        for r in (["component"] if d == "start-hour" else list(RESOLUTIONS)):
            for s in SCOPES:
                configs.append((d, r, s))

    event_rows = []
    summary_rows = []
    partitions = {}
    for (d, r, s) in configs:
        cfg = "%s/%s/%s" % (d, r, s)
        if d == "none":
            events = [[i] for i in id_order]
        else:
            events = collapse(moments, d, r, s)
        # the partition must be exact -- check it, do not assume it
        flat = [c for ev in events for c in ev]
        if sorted(flat) != id_order:
            die("configuration %s did not partition the moments exactly" % cfg)
        partitions[cfg] = events

        sizes = Counter(len(ev) for ev in events)
        mixed_kind = sum(1 for ev in events
                         if len({by_id[c]["kind"] for c in ev}) > 1)
        mixed_coin = sum(1 for ev in events
                         if len({by_id[c]["coin"] for c in ev}) > 1)
        singletons = sizes.get(1, 0)
        largest = max(len(ev) for ev in events)
        # design effect: how many cards one event holds on average
        summary_rows.append({
            "config": cfg,
            "definition": d, "resolution": r, "scope": s,
            "cards": len(id_order),
            "events": len(events),
            "cards_per_event_mean": round(len(id_order) / len(events), 4),
            "events_of_size_1": singletons,
            "largest_event": largest,
            "events_holding_both_kinds": mixed_kind,
            "events_holding_more_than_one_coin": mixed_coin,
            "cards_in_events_of_size_1": singletons,
            "size_histogram": " ".join("%d:%d" % (k, sizes[k])
                                       for k in sorted(sizes)),
        })
        for i, ev in enumerate(sorted(events, key=lambda g: (
                min(by_id[c]["start_dt"] for c in g), g[0])), 1):
            eid = "E%04d" % i
            kinds = sorted({by_id[c]["kind"] for c in ev})
            for c in ev:
                event_rows.append({
                    "config": cfg, "event_id": eid, "event_size": len(ev),
                    "card": c, "coin": by_id[c]["coin"],
                    "kind": by_id[c]["kind"],
                    "start_hour_utc": fmt_hour(by_id[c]["start_dt"]),
                    "event_kinds": "+".join(kinds),
                    "event_first_hour_utc": fmt_hour(
                        min(by_id[c2]["start_dt"] for c2 in ev)),
                    "event_last_hour_utc": fmt_hour(
                        max(by_id[c2]["start_dt"] for c2 in ev)),
                })

    # ---- shuffle calibration ----------------------------------------------
    # Two SYNTHETIC answer vectors, drawn from the fixed seed and labelled
    # synthetic. They are calibration input for the instrument, not a result
    # about any rule: no rule from the canteen book is evaluated here.
    labels = [1 if by_id[c]["kind"] == "large" else 0 for c in id_order]
    calib_rows = []
    for cfg, events in partitions.items():
        for predictor in ("synthetic-iid", "synthetic-event-constant"):
            rng = random.Random(SEED)
            if predictor == "synthetic-iid":
                answers = [rng.randint(0, 1) for _ in id_order]
            else:
                # one draw per event of THIS configuration, repeated inside it
                answers = [None] * len(id_order)
                pos = {c: i for i, c in enumerate(id_order)}
                for ev in events:
                    v = rng.randint(0, 1)
                    for c in ev:
                        answers[pos[c]] = v
            observed = sum(1 for a, l in zip(answers, labels)
                           if a == l) / len(labels)

            rng_card = random.Random(SEED)
            null_card = []
            perm = list(answers)
            for _ in range(SHUFFLES):
                rng_card.shuffle(perm)
                null_card.append(sum(1 for a, l in zip(perm, labels)
                                     if a == l) / len(labels))

            rng_block = random.Random(SEED)
            null_block = []
            for _ in range(SHUFFLES):
                idx = block_shuffle_indices(events, id_order, rng_block)
                null_block.append(sum(1 for i, l in zip(idx, labels)
                                      if answers[i] == l) / len(labels))

            # Mode A -- representative collapse: keep ONE card per event
            # (the earliest start hour, ties by lowest id) and shuffle over
            # that reduced set. This is the reading of RULES 13 that literally
            # replaces an event by a single observation, and it is the one
            # that changes the width of the null the most, because the null
            # is then drawn over n = events, not n = cards.
            reps = [sorted(ev, key=lambda c: (by_id[c]["start_dt"], c))[0]
                    for ev in events]
            rep_labels = [1 if by_id[c]["kind"] == "large" else 0
                          for c in reps]
            rng_rep = random.Random(SEED)
            rep_answers = [rng_rep.randint(0, 1) for _ in reps]
            null_rep = []
            for _ in range(SHUFFLES):
                rng_rep.shuffle(rep_answers)
                null_rep.append(sum(1 for a, l in zip(rep_answers, rep_labels)
                                    if a == l) / len(rep_labels))

            calib_rows.append({
                "config": cfg,
                "predictor": predictor,
                "representative_n": len(reps),
                "representative_shuffle_1pct_boundary": round(
                    quantile_top(null_rep, TOP_FRACTION), 6),
                "shuffles": SHUFFLES,
                "seed": SEED,
                "observed_accuracy": round(observed, 6),
                "card_shuffle_1pct_boundary": round(
                    quantile_top(null_card, TOP_FRACTION), 6),
                "card_shuffle_max": round(max(null_card), 6),
                "block_shuffle_1pct_boundary": round(
                    quantile_top(null_block, TOP_FRACTION), 6),
                "block_shuffle_max": round(max(null_block), 6),
            })

    # ---- write -------------------------------------------------------------
    os.makedirs(args.out, exist_ok=True)
    runs_dir = os.path.join(args.out, "runs")
    os.makedirs(runs_dir, exist_ok=True)

    core = {
        "run": run16, "input_fingerprint": run_full,
        "moments": len(id_order), "configurations": len(configs),
        "shuffles": SHUFFLES, "seed": SEED, "top_fraction": TOP_FRACTION,
        "events_by_config": {r["config"]: r["events"] for r in summary_rows},
        "script_sha256": script_sha,
    }
    rec_path = os.path.join(runs_dir, run16 + ".json")
    if os.path.exists(rec_path):
        with open(rec_path, encoding="utf-8") as fh:
            old = json.load(fh)
        differ = [k for k, v in core.items() if old.get(k) != v]
        if differ:
            die("run record %s exists and disagrees on %s (RULES 30: records "
                "are append-only); no output file was touched"
                % (rec_path, ", ".join(sorted(differ))))
    prior = sorted(f[:-5] for f in os.listdir(runs_dir) if f.endswith(".json"))
    if run16 not in prior:
        prior.append(run16)

    def write_csv(path, rows, fields):
        with open(path, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
            w.writeheader()
            w.writerows(rows)

    ev_path = os.path.join(args.out, "events.csv")
    write_csv(ev_path, event_rows, list(event_rows[0].keys()))
    sm_path = os.path.join(args.out, "collapse-summary.csv")
    write_csv(sm_path, summary_rows, list(summary_rows[0].keys()))
    cb_path = os.path.join(args.out, "shuffle-calibration.csv")
    write_csv(cb_path, calib_rows, list(calib_rows[0].keys()))

    # ---- manifest ----------------------------------------------------------
    A = []
    A.append("# Collapse manifest — the event map RULES 13 needs")
    A.append("")
    A.append("Written by `scripts/15_event_collapse.py`. It builds every "
             "candidate reading of RULES 13's \"the same hour\" and measures "
             "each. **It chooses none of them.** The choice is an open "
             "question under RULES 33 and is stated in "
             "`exam-prep/N-1-collapse.md`.")
    A.append("")
    A.append("## Run")
    A.append("")
    A.append("| field | value |")
    A.append("|---|---|")
    A.append("| run number (SHA-256 of the inputs, RULES 29) | `%s` |" % run16)
    A.append("| full input fingerprint | `%s` |" % run_full)
    A.append("| written at (system clock, UTC, RULES 23) | %s |"
             % started.strftime("%Y-%m-%dT%H:%M:%SZ"))
    A.append("| free disk space at start (bytes) | %d |" % free_bytes)
    A.append("| moments read | %d |" % len(id_order))
    A.append("| input | %s |" % ("`%s`" % os.path.relpath(args.moments, REPO)
                                 if args.moments
                                 else "the %d cards in `cards/`"
                                      % len(id_order)))
    A.append("| shuffles (RULES 12) | %d |" % SHUFFLES)
    A.append("| boundary (RULES 12) | best %s%% |" % (TOP_FRACTION * 100))
    A.append("| seed (TACTICS 1 draw number) | `%d` |" % SEED)
    A.append("| `scripts/15_event_collapse.py` SHA-256 | `%s` |" % script_sha)
    A.append("")
    A.append("Run records live in `runs/`, one JSON per run number, "
             "append-only (RULES 30). Records present when this manifest was "
             "written: %s." % ", ".join("`%s`" % p for p in prior))
    A.append("")
    A.append("## The candidate readings")
    A.append("")
    A.append("| name | what counts as \"the same hour\" | largest start gap "
             "that still merges |")
    A.append("|---|---|---|")
    A.append("| `start-hour` | the two moments begin in the same clock hour "
             "(TACTICS 2: a moment's start is the hour the 24-hour movement "
             "began) | 0 h |")
    A.append("| `move-window` | the two 24-hour movements share a clock hour "
             "| 23 h |")
    A.append("| `card-span` | the two 48-hour card spans share a clock hour "
             "— the relation `14_overlap_map.py` measured | 47 h |")
    A.append("")
    A.append("`component` = anything chained together is one event. "
             "`greedy-clique` = repeatedly take the clock hour covered by the "
             "most still-unassigned moments (ties: earliest hour, then lowest "
             "id). `greedy-clique` is a **stated convention**, not an "
             "observation: overlapping intervals have no unique partition into "
             "\"groups sharing an hour\", so some deterministic rule is needed "
             "and this one is written down so it can be disagreed with.")
    A.append("")
    A.append("`any` = two moments of the same coin may merge. `cross-coin` = "
             "they may not, because RULES 13 says \"in several coins\" and "
             "same-coin spacing is a separate open question.")
    A.append("")
    A.append("## What each reading counts")
    A.append("")
    A.append("| configuration | events | cards per event | events of size 1 | "
             "largest event | events holding both kinds | events holding more "
             "than one coin |")
    A.append("|---|---|---|---|---|---|---|")
    for r in summary_rows:
        A.append("| `%s` | %d | %.2f | %d | %d | %d | %d |"
                 % (r["config"], r["events"], r["cards_per_event_mean"],
                    r["events_of_size_1"], r["largest_event"],
                    r["events_holding_both_kinds"],
                    r["events_holding_more_than_one_coin"]))
    A.append("")
    A.append("\"Events holding both kinds\" is the count that matters for a "
             "judge: an event holding a `large` card and a `calm` card has no "
             "single label, so a scheme that replaces an event by one answer "
             "cannot be used on it. The column is measured, not argued.")
    A.append("")
    A.append("## What collapsing does to a shuffle")
    A.append("")
    A.append("RULES 12 fixes the shuffle at 1,000 draws and the line at the "
             "best 1%%. The two answer vectors below are **synthetic**, drawn "
             "from seed `%d`: `synthetic-iid` is one independent coin flip per "
             "card, `synthetic-event-constant` is one coin flip per event of "
             "the same configuration, repeated on every card in it. No rule "
             "from the canteen book is evaluated here and no result about any "
             "rule is produced. The point of the table is the **width of the "
             "null**, which is a property of the shuffle scheme and the "
             "labels, not of any signal." % SEED)
    A.append("")
    A.append("| configuration | predictor | n cards | card-level shuffle · "
             "1% boundary | cluster-level (block) shuffle · 1% boundary | "
             "n events | representative-collapse shuffle · 1% boundary |")
    A.append("|---|---|---|---|---|---|---|")
    for r in calib_rows:
        A.append("| `%s` | %s | %d | %.4f | %.4f | %d | %.4f |"
                 % (r["config"], r["predictor"], len(id_order),
                    r["card_shuffle_1pct_boundary"],
                    r["block_shuffle_1pct_boundary"],
                    r["representative_n"],
                    r["representative_shuffle_1pct_boundary"]))
    A.append("")
    A.append("The last column is the one that moves. Keeping every card and "
             "only permuting whole events (the middle column) barely widens "
             "the null, because the overlapping cards do not carry the same "
             "label — see the \"events holding both kinds\" column above. "
             "Replacing each event by one card (the last column) widens it a "
             "great deal, because the null is then drawn over n = events.")
    A.append("")
    A.append("## Fingerprints")
    A.append("")
    A.append("| file | rows | SHA-256 |")
    A.append("|---|---|---|")
    for p, n in ((ev_path, len(event_rows)), (sm_path, len(summary_rows)),
                 (cb_path, len(calib_rows))):
        A.append("| `%s` | %d | `%s` |"
                 % (os.path.relpath(p, REPO), n, sha256_file(p)))
    A.append("")
    man_path = os.path.join(args.out, "collapse-manifest.md")
    with open(man_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(A) + "\n")
    with open(man_path + ".sha256", "w", encoding="utf-8") as fh:
        fh.write(sha256_file(man_path) + "  collapse-manifest.md\n")

    with open(rec_path, "w", encoding="utf-8") as fh:
        json.dump(core, fh, indent=1, sort_keys=True)
        fh.write("\n")
    sys.stderr.write("run %s: %d moments, %d configurations\n"
                     % (run16, len(id_order), len(configs)))


if __name__ == "__main__":
    main()
