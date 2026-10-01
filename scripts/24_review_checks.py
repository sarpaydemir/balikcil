#!/usr/bin/env python3
"""
24_review_checks.py -- re-measure, independently, every number the review
(`exam-prep/REVIEW.md`) uses to state an action item, against the instruments
exactly as the review saw them.

What it does
------------
The review of `exam-prep/` names defects and backs each with a number. Before
acting on a review item this run re-measures the number the item rests on, so
that nothing is fixed (or disputed) on the reviewer's word alone. The reviewed
instruments are loaded from the git commit that holds them as reviewed
(REVIEWED_COMMIT), not from the working tree, so this script keeps measuring
the reviewed code even after the instruments are changed by this run.

  C-1  REVIEW §3.1  which level-carrying families beat their chance line on
                    the `strict-flags` audit (read from the committed CSV)
  C-2  REVIEW §3.2  the `close` repeat-structure probe (the review's Probe 1),
                    re-run with the reviewed audit's own machinery
  C-3  REVIEW §3.3  the `ALL-removable` gate rows, both attacks, all four
                    blinded variants (read from the committed CSVs)
  C-4  REVIEW §3.4  the release-name date channel (the review's Probe 2)
  C-5  REVIEW §3.5a the B-4 depth-run cards, before window vs after window
  C-6  REVIEW §3.5b the "two-fifths" figure, from run record ca8b0bc394468298
  C-7  REVIEW §4.2  the reviewed block_shuffle_indices on the review's
                    three-event example (the review's Probe 3, part 1)
  C-8  REVIEW §4.4  same-coin events per configuration, from events.csv
                    (the review's Probe 4)
  C-9  REVIEW §2.3  the combined blinded-card fingerprint recipe
  C-10 REVIEW §4.3  the identity partition reproduces the card-level line

Input   : git object REVIEWED_COMMIT:scripts/{15_event_collapse,
          16_identity_audit}.py ; cards/ ; exam-prep/blind-proof/*/ ;
          exam-prep/identity/*.csv ; exam-prep/identity/runs/ca8b0bc394468298.json ;
          exam-prep/collapse/events.csv
Output  : exam-prep/second-fix/checks/review-checks-<run16>.md
          exam-prep/second-fix/checks/runs/<run16>.json   (append-only)

Rules implemented
-----------------
RULES 12 : 1,000 shuffles and the best-1% boundary, imported from the
           reviewed audit, not restated.
RULES 19 : every number written here is counted by this script.
RULES 23 : the clock is read from the system.
RULES 29 : run number = SHA-256 of this script, the reviewed sources and
           every input file.
RULES 30 : a run already recorded is never rewritten; a record that would
           differ stops the script.

Constants -- where each came from
---------------------------------
REVIEWED_COMMIT  the commit holding the instruments with the SHA-256 values
                 the review's §8 lists (verified at run time; the script stops
                 if they differ).
REVIEWED_SHA     copied from REVIEW.md §8.
SEED             20260913, TACTICS 1's draw number, imported from the reviewed
                 audit. Used for C-7's draws, which the review does not state a
                 seed for.
C7_DRAWS_*       200 and 1,000 -- the draw counts the review's §4.2 states.
No threshold, score or trading rule is defined anywhere in this file.
"""

import csv
import datetime as dt
import hashlib
import json
import os
import random
import re
import shutil
import subprocess
import sys
import types
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import lab_cards  # noqa: E402

REVIEWED_COMMIT = "7735d08f106f609b78f44fa652515e4330db9420"
REVIEWED_SHA = {
    "scripts/15_event_collapse.py":
        "f3de235883aac8b364aa5391c8371d50a9ecca288007f8d0bfaadadafe0ffb12",
    "scripts/16_identity_audit.py":
        "4c4928b84ff9b484995058c2dd4e5b043af1491b60f314e1a0f418dd90e4a371",
}
C7_DRAWS_CROSS = 200
C7_DRAWS_CONST = 1000

OUT_DIR = os.path.join(REPO, "exam-prep", "second-fix", "checks")
VARIANTS = ("ratio", "rank", "strict", "strict-flags")


def die(msg):
    sys.stderr.write("STOP: %s\n" % msg)
    sys.exit(1)


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(path):
    with open(path, "rb") as fh:
        return sha256_bytes(fh.read())


def git_source(relpath):
    out = subprocess.run(["git", "-C", REPO, "show",
                          "%s:%s" % (REVIEWED_COMMIT, relpath)],
                         capture_output=True, check=True).stdout
    if sha256_bytes(out) != REVIEWED_SHA[relpath]:
        die("%s at %s does not have the SHA-256 the review lists"
            % (relpath, REVIEWED_COMMIT))
    return out


def load_reviewed(relpath, name):
    src = git_source(relpath)
    mod = types.ModuleType(name)
    # the module only uses __file__ to locate the repository and lab_cards.py
    mod.__file__ = os.path.join(REPO, relpath)
    exec(compile(src, "%s@%s" % (relpath, REVIEWED_COMMIT[:7]), "exec"),
         mod.__dict__)
    return mod, sha256_bytes(src)


def read_csv(path):
    with open(path, encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def attack(ia, feats, coins, prefixes):
    """The reviewed audit's own T1/T2 loop, unchanged in substance."""
    allkeys = sorted({k for f in feats for k in f})
    keys = ia.select({k: 1 for k in allkeys}, prefixes)
    vecs, used = ia.standardise(feats, keys)
    dists = ia.pair_distances(vecs)
    nn_idx = ia.nearest_neighbours(dists)
    rank, total = ia.pair_ranks(dists)
    obs_nn = ia.nn_accuracy(nn_idx, coins)
    obs_auc = ia.pair_auc(rank, total, coins)
    rng = random.Random(ia.SEED)
    perm = list(coins)
    null_nn, null_auc = [], []
    for _ in range(ia.SHUFFLES):
        rng.shuffle(perm)
        null_nn.append(ia.nn_accuracy(nn_idx, perm))
        null_auc.append(ia.pair_auc(rank, total, perm))
    return {"features": len(used),
            "nn": round(obs_nn, 6),
            "nn_line": round(ia.quantile_top(null_nn, ia.TOP_FRACTION), 6),
            "auc": round(obs_auc, 6),
            "auc_line": round(ia.quantile_top(null_auc, ia.TOP_FRACTION), 6)}


def main():
    started = dt.datetime.now(dt.timezone.utc)
    free_bytes = shutil.disk_usage(REPO).free
    ia, ia_sha = load_reviewed("scripts/16_identity_audit.py", "ia_reviewed")
    ec, ec_sha = load_reviewed("scripts/15_event_collapse.py", "ec_reviewed")

    inputs = []

    def use(path):
        inputs.append((os.path.relpath(path, REPO), sha256_file(path)))
        return path

    R = {}   # results, all JSON-serialisable

    # ---- C-1 / C-3 : the committed audit CSVs --------------------------------
    level_families = ("price-level", "openint-level", "depth-level",
                      "ratio-level", "volume-level", "trades-level",
                      "wikipedia-presence", "btc-eth", "taker-buy")
    c1, c3 = [], []
    for v in VARIANTS:
        rows = read_csv(use(os.path.join(
            REPO, "exam-prep", "identity",
            "identity-audit-blinded-%s.csv" % v)))
        for r in rows:
            if r["family"] in level_families and (
                    r["nn_beats_chance"] == "YES"
                    or r["auc_beats_chance"] == "YES"):
                c1.append({"variant": v, "family": r["family"],
                           "nn": r["nn_same_coin_accuracy"],
                           "nn_line": r["nn_chance_1pct"],
                           "nn_beats": r["nn_beats_chance"],
                           "auc": r["pair_auc"], "auc_line": r["auc_chance_1pct"],
                           "auc_beats": r["auc_beats_chance"]})
            if r["family"] == "ALL-removable":
                c3.append({"variant": v,
                           "nn": r["nn_same_coin_accuracy"],
                           "nn_line": r["nn_chance_1pct"],
                           "nn_beats": r["nn_beats_chance"],
                           "auc": r["pair_auc"], "auc_line": r["auc_chance_1pct"],
                           "auc_beats": r["auc_beats_chance"]})
    R["C-1"] = c1
    R["C-3"] = c3

    # ---- C-2 : the close repeat-structure probe (review Probe 1) -------------
    removable = sorted({p for k, v in ia.FAMILIES.items()
                        if k not in ("volatility-frozen", "funding-line",
                                     "p7-shape") for p in v})
    probe_sets = [("volatility-frozen", ["volatility:"]),
                  ("closeset", ["closeset:"]),
                  ("volatility-frozen+closeset", ["volatility:", "closeset:"]),
                  ("ALL-removable", removable),
                  ("ALL-removable+closeset", removable + ["closeset:"])]
    c2 = []
    for v in VARIANTS:
        d = os.path.join(REPO, "exam-prep", "blind-proof", v)
        truth = {r["id"]: r for r in read_csv(use(os.path.join(
            d, "truth-%s.csv" % v)))}
        names = sorted(f for f in os.listdir(os.path.join(d, "cards"))
                       if f.endswith(".md"))
        cards = [lab_cards.parse_any_card(use(os.path.join(d, "cards", n)))
                 for n in names]
        coins = [truth[c["card"]]["coin"] for c in cards]
        feats = []
        for c in cards:
            f = ia.card_features(c)
            col = c["cols"]["close"]
            f["closeset:distinct"] = float(len(set(col)))
            f["closeset:maxrepeat"] = float(max(sum(1 for x in col if x == u)
                                                for u in set(col)))
            feats.append(f)
        for name, prefixes in probe_sets:
            res = attack(ia, feats, coins, prefixes)
            res.update({"variant": v, "feature_set": name})
            c2.append(res)
        sys.stderr.write("C-2 %s done\n" % v)
    R["C-2"] = c2

    # ---- C-4 : release names (review Probe 2), strict-flags set --------------
    d = os.path.join(REPO, "exam-prep", "blind-proof", "strict-flags")
    truth = {r["id"]: r for r in read_csv(os.path.join(
        d, "truth-strict-flags.csv"))}
    names = sorted(f for f in os.listdir(os.path.join(d, "cards"))
                   if f.endswith(".md"))
    rel = {}
    for n in names:
        c = lab_cards.parse_any_card(os.path.join(d, "cards", n))
        rel[c["card"]] = c["bullets"].get("US releases", "")
    NONE = "none in these hours."
    card_names = {}
    for cid, txt in rel.items():
        if txt == NONE or not txt:
            card_names[cid] = []
            continue
        parts = [p.strip() for p in txt.split(";")]
        nm = []
        for p in parts:
            p = re.sub(r"\s*\((?:[-+]\d+ h|the calendar publishes no clock "
                       r"time)\)$", "", p)
            nm.append(p)
        card_names[cid] = nm
    name_days = defaultdict(set)
    for cid, nm in card_names.items():
        day = truth[cid]["start_hour_utc"][:10]
        for x in nm:
            name_days[x].add(day)
    single_day = sorted(x for x, s in name_days.items() if len(s) == 1)
    cards_with_single = sorted(cid for cid, nm in card_names.items()
                               if any(x in single_day for x in nm))
    # linkage: exact match of the bullet text, |gap| <= 47 h is the truth
    ids = sorted(rel)

    def t0(cid):
        s = truth[cid]["start_hour_utc"].replace("Z", "")
        s = s + ":00" if len(s) == 16 else s
        return dt.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S")
    ts = {cid: t0(cid) for cid in ids}
    true_pairs = det = fp = 0
    for i, a in enumerate(ids):
        for b in ids[i + 1:]:
            share = abs((ts[a] - ts[b]).total_seconds()) / 3600.0 <= 47
            hit = rel[a] == rel[b] and rel[a] not in (NONE, "")
            if share:
                true_pairs += 1
                det += hit
            else:
                fp += hit
    R["C-4"] = {"cards": len(ids),
                "cards_printing_a_release_name":
                    sum(1 for nm in card_names.values() if nm),
                "distinct_release_names": len(name_days),
                "names_on_exactly_one_calendar_day": single_day,
                "count_names_on_exactly_one_calendar_day": len(single_day),
                "cards_carrying_such_a_name": len(cards_with_single),
                "linkage_truly_overlapping_pairs": true_pairs,
                "linkage_detected": det, "linkage_false_positives": fp}

    # ---- C-5 : B-4 depth runs, before vs after window ------------------------
    raw = lab_cards.load_all(os.path.join(REPO, "cards"))

    def longest(vals):
        best = cur = 1
        for i in range(1, len(vals)):
            cur = cur + 1 if vals[i] == vals[i - 1] else 1
            best = max(best, cur)
        return best
    before3, after_only, detail = [], [], {}
    for c in raw:
        b = max(longest(c["before"]["depth -1%"]),
                longest(c["before"]["depth +1%"]))
        a = max(longest(c["after"]["depth -1%"]),
                longest(c["after"]["depth +1%"]))
        if b >= 3:
            before3.append(c["card"])
        if a >= 3 and b < 3:
            after_only.append(c["card"])
        if c["card"] in ("C017", "C018", "C019", "C041", "C058", "C059"):
            detail[c["card"]] = {
                "before_bid": longest(c["before"]["depth -1%"]),
                "before_ask": longest(c["before"]["depth +1%"]),
                "after_bid": longest(c["after"]["depth -1%"]),
                "after_ask": longest(c["after"]["depth +1%"])}
    oi_before = [c["card"] for c in raw
                 if any(v == 0 for v in c["before"]["open int"])]
    R["C-5"] = {"cards_with_before_window_depth_run_ge_3": before3,
                "cards_with_depth_run_ge_3_only_after": after_only,
                "detail": detail,
                "cards_with_before_window_openint_zero": oi_before}

    # ---- C-6 : two-fifths ----------------------------------------------------
    rec = json.load(open(use(os.path.join(
        REPO, "exam-prep", "identity", "runs", "ca8b0bc394468298.json")),
        encoding="utf-8"))
    rows = {r["time_overlapping_neighbours_forbidden"]: r for r in rec["rows"]}
    no, yes = rows["no"], rows["yes"]
    ex_mean0 = no["nn_same_coin_accuracy"] - no["null_mean"]
    ex_mean1 = yes["nn_same_coin_accuracy"] - yes["null_mean"]
    ex_line0 = no["nn_same_coin_accuracy"] - no["chance_1pct"]
    ex_line1 = yes["nn_same_coin_accuracy"] - yes["chance_1pct"]
    R["C-6"] = {"excess_over_null_mean": [round(ex_mean0, 6),
                                          round(ex_mean1, 6)],
                "reduction_over_null_mean_pct":
                    round(100 * (ex_mean0 - ex_mean1) / ex_mean0, 1),
                "excess_over_line": [round(ex_line0, 6), round(ex_line1, 6)],
                "reduction_over_line_pct":
                    round(100 * (ex_line0 - ex_line1) / ex_line0, 1)}

    # ---- C-7 : the reviewed block shuffle on the review's example -----------
    ev = [["c0", "c1", "c2"], ["c3"], ["c4", "c5"]]
    order = ["c0", "c1", "c2", "c3", "c4", "c5"]
    pos = {c: i for i, c in enumerate(order)}
    src_event = {}
    for k, e in enumerate(ev):
        for c in e:
            src_event[pos[c]] = k
    rng = random.Random(ia.SEED)
    crossed = 0
    for _ in range(C7_DRAWS_CROSS):
        idx = ec.block_shuffle_indices(ev, order, rng)
        if any(len({src_event[idx[pos[c]]] for c in e}) > 1 for e in ev):
            crossed += 1
    rng = random.Random(ia.SEED)
    const = [0, 0, 0, 1, 2, 2]          # constant inside each event
    still = 0
    for _ in range(C7_DRAWS_CONST):
        idx = ec.block_shuffle_indices(ev, order, rng)
        permd = [const[i] for i in idx]
        if all(len({permd[pos[c]] for c in e}) == 1 for e in ev):
            still += 1
    R["C-7"] = {"seed": ia.SEED,
                "draws_with_an_event_reading_from_two_sources":
                    "%d of %d" % (crossed, C7_DRAWS_CROSS),
                "event_constant_vectors_still_event_constant":
                    "%d of %d" % (still, C7_DRAWS_CONST)}

    # ---- C-8 : same-coin events per configuration ----------------------------
    evrows = read_csv(use(os.path.join(REPO, "exam-prep", "collapse",
                                       "events.csv")))
    by = defaultdict(lambda: defaultdict(list))
    for r in evrows:
        by[r["config"]][r["event_id"]].append(r["coin"])
    c8 = []
    for cfg in sorted(by):
        evs = by[cfg]
        same = [max(list(coins).count(x) for x in set(coins))
                for coins in evs.values()]
        c8.append({"config": cfg, "events": len(evs),
                   "events_holding_2plus_same_coin":
                       sum(1 for s in same if s >= 2),
                   "largest_same_coin_count": max(same)})
    R["C-8"] = c8

    # ---- C-9 : the combined fingerprint recipe -------------------------------
    c9 = []
    for v in VARIANTS:
        d = os.path.join(REPO, "exam-prep", "blind-proof", v)
        truth_rows = read_csv(os.path.join(d, "truth-%s.csv" % v))
        h = hashlib.sha256()
        for r in sorted(truth_rows, key=lambda r: r["id"]):
            h.update((r["id"] + ":" + sha256_file(os.path.join(
                d, "cards", r["id"] + ".md")) + "\n").encode())
        c9.append({"variant": v, "combined": h.hexdigest()})
    R["C-9"] = c9

    # ---- C-10 : the identity partition bypass --------------------------------
    labels = [1 if c["kind"] == "large" else 0 for c in raw]
    idord = [c["card"] for c in raw]
    rng = random.Random(ia.SEED)
    answers = [rng.randint(0, 1) for _ in idord]
    obs, line_block, _ = ec.chance_line(answers, labels,
                                        [[c] for c in idord], idord, "block")
    obs2, line_rep, _ = ec.chance_line(answers, labels,
                                       [[c] for c in idord], idord,
                                       "representative")
    rng_card = random.Random(ia.SEED)
    perm = list(answers)
    null = []
    for _ in range(ia.SHUFFLES):
        rng_card.shuffle(perm)
        null.append(sum(1 for a, l in zip(perm, labels) if a == l)
                    / len(labels))
    R["C-10"] = {"identity_partition_accepted_block": True,
                 "identity_partition_accepted_representative": True,
                 "block_boundary": round(line_block, 6),
                 "representative_boundary": round(line_rep, 6),
                 "card_level_boundary_same_seed": round(
                     ia.quantile_top(null, ia.TOP_FRACTION), 6)}

    # ---- run number and write-once -------------------------------------------
    script_sha = sha256_file(os.path.abspath(__file__))
    h = hashlib.sha256()
    h.update(("script:%s\nreviewed16:%s\nreviewed15:%s\nlab_cards:%s\n"
              % (script_sha, ia_sha, ec_sha,
                 sha256_file(os.path.join(HERE, "lab_cards.py")))).encode())
    for name, sha in sorted(set(inputs)):
        h.update(("%s:%s\n" % (name, sha)).encode())
    for c in raw:
        h.update(("%s:%s\n" % (c["card"], c["sha256"])).encode())
    run_full = h.hexdigest()
    run16 = run_full[:16]
    core = {"run": run16, "input_fingerprint": run_full,
            "reviewed_commit": REVIEWED_COMMIT, "script_sha256": script_sha,
            "results": R}
    runs_dir = os.path.join(OUT_DIR, "runs")
    os.makedirs(runs_dir, exist_ok=True)
    rec_path = os.path.join(runs_dir, run16 + ".json")
    if os.path.exists(rec_path):
        old = json.load(open(rec_path, encoding="utf-8"))
        if old != json.loads(json.dumps(core)):
            die("run record %s exists with different content (RULES 30)"
                % rec_path)
        sys.stderr.write("run %s already recorded with identical results; "
                         "nothing written\n" % run16)
        return

    A = ["# Review checks — run `%s`" % run16, "",
         "Written by `scripts/24_review_checks.py` against the instruments as "
         "reviewed (commit `%s`). Every number below is counted by that "
         "script; the review's own figure is quoted next to it where the "
         "review gives one." % REVIEWED_COMMIT[:7], "",
         "| field | value |", "|---|---|",
         "| run number (RULES 29) | `%s` |" % run16,
         "| full input fingerprint | `%s` |" % run_full,
         "| written at (system clock, UTC, RULES 23) | %s |"
         % started.strftime("%Y-%m-%dT%H:%M:%SZ"),
         "| free disk space at start (bytes) | %d |" % free_bytes,
         "| `scripts/24_review_checks.py` SHA-256 | `%s` |" % script_sha, ""]

    A += ["## C-1 · REVIEW §3.1 — level-carrying families that beat a chance "
          "line", "",
          "| variant | family | nn | line | beats | pair AUC | line | beats |",
          "|---|---|---|---|---|---|---|---|"]
    for r in c1:
        A.append("| `%s` | `%s` | %s | %s | %s | %s | %s | %s |"
                 % (r["variant"], r["family"], r["nn"], r["nn_line"],
                    r["nn_beats"], r["auc"], r["auc_line"], r["auc_beats"]))
    A += ["", "## C-2 · REVIEW §3.2 — the `close` repeat-structure probe", "",
          "Review figures (`strict-flags`): `closeset` nn 0.1601 / line 0.1667,"
          " AUC 0.5421 / line 0.5107; `volatility-frozen`+`closeset` nn "
          "0.1830 / 0.1732, AUC 0.5569 / 0.5136; `ALL-removable`+`closeset` "
          "nn 0.2451 / 0.1732, AUC 0.5172 / 0.5141.", "",
          "| variant | feature set | features | nn | line | pair AUC | line |",
          "|---|---|---|---|---|---|---|"]
    for r in c2:
        A.append("| `%s` | `%s` | %d | %.6f | %.6f | %.6f | %.6f |"
                 % (r["variant"], r["feature_set"], r["features"], r["nn"],
                    r["nn_line"], r["auc"], r["auc_line"]))
    A += ["", "## C-3 · REVIEW §3.3 — the `ALL-removable` gate rows", "",
          "| variant | nn | line | beats | pair AUC | line | beats |",
          "|---|---|---|---|---|---|---|"]
    for r in c3:
        A.append("| `%s` | %s | %s | %s | %s | %s | %s |"
                 % (r["variant"], r["nn"], r["nn_line"], r["nn_beats"],
                    r["auc"], r["auc_line"], r["auc_beats"]))
    c4 = R["C-4"]
    A += ["", "## C-4 · REVIEW §3.4 — release names (`strict-flags`)", "",
          "| quantity | this script | review |", "|---|---|---|",
          "| cards printing at least one release name | %d of %d | 100 of 306 |"
          % (c4["cards_printing_a_release_name"], c4["cards"]),
          "| distinct release names | %d | 30 |"
          % c4["distinct_release_names"],
          "| names on exactly one calendar day | %d | 11 |"
          % c4["count_names_on_exactly_one_calendar_day"],
          "| cards carrying such a name | %d | 13 |"
          % c4["cards_carrying_such_a_name"],
          "| exact-match linkage: truly overlapping pairs detected | %d of %d "
          "| 8 of 495 |" % (c4["linkage_detected"],
                            c4["linkage_truly_overlapping_pairs"]),
          "| exact-match linkage: false positives | %d | 15 |"
          % c4["linkage_false_positives"], "",
          "Names on exactly one calendar day: %s."
          % "; ".join("*%s*" % x
                      for x in c4["names_on_exactly_one_calendar_day"])]
    c5 = R["C-5"]
    A += ["", "## C-5 · REVIEW §3.5(a) — B-4 depth runs by window", "",
          "Cards with a run of 3+ identical values in a depth column inside "
          "the before window: %s (%d)."
          % (" ".join(c5["cards_with_before_window_depth_run_ge_3"]),
             len(c5["cards_with_before_window_depth_run_ge_3"])),
          "", "Cards whose only such run is in the after window: %s."
          % (" ".join(c5["cards_with_depth_run_ge_3_only_after"]) or "none"),
          "", "| card | before bid | before ask | after bid | after ask |",
          "|---|---|---|---|---|"]
    for k in sorted(c5["detail"]):
        x = c5["detail"][k]
        A.append("| %s | %d | %d | %d | %d |" % (k, x["before_bid"],
                                                 x["before_ask"],
                                                 x["after_bid"],
                                                 x["after_ask"]))
    A += ["", "Cards with an `open int` zero inside the before window: %s."
          % " ".join(c5["cards_with_before_window_openint_zero"])]
    c6 = R["C-6"]
    A += ["", "## C-6 · REVIEW §3.5(b) — the \"two-fifths\" figure", "",
          "Excess over the null mean: %.6f → %.6f, a reduction of %.1f%%. "
          "Excess over the 1%% line: %.6f → %.6f, a reduction of %.1f%%. "
          "Review: 23.7%% and 85.7%%."
          % (c6["excess_over_null_mean"][0], c6["excess_over_null_mean"][1],
             c6["reduction_over_null_mean_pct"], c6["excess_over_line"][0],
             c6["excess_over_line"][1], c6["reduction_over_line_pct"])]
    c7 = R["C-7"]
    A += ["", "## C-7 · REVIEW §4.2 — the reviewed block shuffle", "",
          "Events `[[c0,c1,c2],[c3],[c4,c5]]`, seed `%d`. Draws in which at "
          "least one event read its answers from more than one source event: "
          "**%s** (review: 175 of 200, seed not stated). Event-constant "
          "vectors still event-constant after permutation: **%s** (review: "
          "138 of 1,000; a true block permutation gives all)."
          % (c7["seed"], c7["draws_with_an_event_reading_from_two_sources"],
             c7["event_constant_vectors_still_event_constant"])]
    A += ["", "## C-8 · REVIEW §4.4 — same-coin events per configuration", "",
          "| configuration | events | events holding 2+ cards of one coin | "
          "largest same-coin count |", "|---|---|---|---|"]
    for r in c8:
        A.append("| `%s` | %d | %d | %d |" % (r["config"], r["events"],
                                            r["events_holding_2plus_same_coin"],
                                            r["largest_same_coin_count"]))
    A += ["", "## C-9 · REVIEW §2.3 — combined blinded-card fingerprints", "",
          "Recipe: SHA-256 over the concatenation, in card-id order, of "
          "`<id>:<SHA-256 of the card file>\\n`.", "",
          "| variant | combined SHA-256 |", "|---|---|"]
    for r in c9:
        A.append("| `%s` | `%s` |" % (r["variant"], r["combined"]))
    c10 = R["C-10"]
    A += ["", "## C-10 · REVIEW §4.3 — the identity partition", "",
          "The reviewed `chance_line()` accepted `events=[[c] for c in "
          "id_order]` in both modes. Boundaries on a synthetic coin-flip "
          "answer vector (seed `%d`): block %.6f, representative %.6f; a "
          "plain card-level shuffle with the same seed: %.6f."
          % (ia.SEED, c10["block_boundary"], c10["representative_boundary"],
             c10["card_level_boundary_same_seed"]), ""]
    md_path = os.path.join(OUT_DIR, "review-checks-%s.md" % run16)
    if os.path.exists(md_path):
        die("%s exists without a run record; refusing to overwrite" % md_path)
    with open(md_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(A) + "\n")
    with open(rec_path, "w", encoding="utf-8") as fh:
        json.dump(core, fh, indent=1, sort_keys=True)
        fh.write("\n")
    sys.stderr.write("run %s written\n" % run16)


if __name__ == "__main__":
    main()
