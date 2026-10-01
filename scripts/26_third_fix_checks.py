#!/usr/bin/env python3
"""
26_third_fix_checks.py -- the numbers the third-fix run needs that no other
numbered script produces, and the guard test of the changed collapse engine.

What it does
------------
  G-1  The guards of scripts/15_event_collapse.py as changed by the third-fix
       run: chance_line() with the required `key_moments_sha256`. REVIEW-2
       §4.3's forged-moment attempts are repeated against the key fingerprint
       of the true moments; plus the attempt that shows the limit (a caller
       who passes the forged map's OWN fingerprint is not stopped by code).
  G-2  Criterion K-9: the representative column of the shuffle calibration,
       computed EXACTLY (hypergeometric null, no simulation), for every
       configuration, with the same synthetic answers and representatives as
       15_event_collapse.py; the exact distribution of the statistic the
       instrument reports (the 10th largest of 1,000 draws) and its 2.5% /
       97.5% points; and, for the un-collapsed card-level line, how far apart
       two independent reported lines fall by chance.
  G-3  Criterion K-8: overlapping card pairs from data/overlap/pairs.csv by
       the two kinds and by same / different coin, for card spans sharing an
       hour (the manifest's definition) and for before windows sharing an hour
       (start gap <= 23 h), and the same-coin calm pairs listed.
  G-4  The facts JQ-B1 rests on: B-1's frozen trigger text, whether the two
       contracts it names are observation coins, and whether the draw manifest
       records the observation and exam lists as disjoint. Nothing under
       exam/ is read.
  G-5  JQ-N1 part 2: what greedy-clique does under cross-coin when two
       moments of one coin cover the chosen hour (the engine keeps the
       earliest), and how many events change if the latest is kept instead
       -- the engine's own loop, with only that one choice reversed.

Input   : cards/ ; data/overlap/pairs.csv ; data/draw/observation-coins.txt ;
          data/draw/draw-manifest.md ; data/moments/moment-manifest.md ;
          canteen/2026-09-19-sofia.md (lines 186-187, read for G-4) ;
          exam-prep/collapse/run-756cf4ea156d92c3/shuffle-calibration.csv ;
          scripts/15_event_collapse.py (imported)
Output  : exam-prep/third-fix/checks/third-fix-checks-<run16>.md
          exam-prep/third-fix/checks/runs/<run16>.json   (append-only)

Rules implemented
-----------------
RULES 12 : 1,000 shuffles and the best 1%, imported from the engine.
RULES 19 : every number written here is counted by this script.
RULES 23 : the clock is read from the system.
RULES 29 / 30 : run number = SHA-256 of this script, the engine and every
           input; a recorded run is never rewritten.

Constants: none of its own. SHUFFLES, TOP_FRACTION and SEED are imported from
15_event_collapse.py (RULES 12, TACTICS 1). The 2.5% / 97.5% points in G-2
describe spread; they are not a test threshold. No threshold, score or
trading rule is defined anywhere in this file.
"""

import csv
import datetime as dt
import hashlib
import importlib.util
import json
import os
import random
import re
import shutil
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from math import comb

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import lab_cards  # noqa: E402

OUT_DIR = os.path.join(REPO, "exam-prep", "third-fix", "checks")
CALIB_RUN = "756cf4ea156d92c3"


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name,
                                                  os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def sha256_file(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def die(msg):
    sys.stderr.write("STOP: %s\n" % msg)
    sys.exit(1)


# ---- exact nulls (G-2) ------------------------------------------------------

def null_pmf(n, a, l):
    """Exact null of accuracy when n answers holding `a` ones are shuffled
    against labels holding `l` ones: matches = n - a - l + 2x, x
    hypergeometric."""
    tot = comb(n, a)
    pmf = {}
    for x in range(max(0, a + l - n), min(a, l) + 1):
        acc = Fraction(n - a - l + 2 * x, n)
        pmf[acc] = pmf.get(acc, 0) + Fraction(comb(l, x) * comb(n - l, a - x),
                                              tot)
    return dict(sorted(pmf.items()))


def exact_top(pmf, fraction):
    run = Fraction(0)
    for v in reversed(list(pmf)):
        run += pmf[v]
        if run >= Fraction(fraction).limit_denominator(10 ** 6):
            return v
    return list(pmf)[0]


def reported_stat_dist(pmf, draws, k):
    """Distribution of the k-th largest of `draws` independent null draws --
    the statistic quantile_top() returns with fraction k / draws."""
    vals = list(pmf)
    sf, run = {}, Fraction(0)
    for v in reversed(vals):
        run += pmf[v]
        sf[v] = run

    def at_least_k(p):
        p = float(p)
        q = 1.0 - p
        s = 0.0
        for j in range(k):
            s += comb(draws, j) * (p ** j) * (q ** (draws - j))
        return 1.0 - s
    g = {v: at_least_k(sf[v]) for v in vals}
    out = {}
    for i, v in enumerate(vals):
        out[v] = g[v] - (g[vals[i + 1]] if i + 1 < len(vals) else 0.0)
    return out


def spread(d):
    c, res = 0.0, {}
    for v, p in d.items():
        c += p
        for q in (0.025, 0.975):
            if q not in res and c >= q - 1e-12:
                res[q] = float(v)
    return res[0.025], res[0.975]


def p_apart(d, delta):
    it = [(float(v), p) for v, p in d.items() if p > 0]
    return sum(p1 * p2 for v1, p1 in it for v2, p2 in it
               if abs(v1 - v2) >= delta - 1e-12)


# ---- G-5: the engine's greedy loop with one choice reversed ---------------

def greedy_cross_coin(moments, gap, keep):
    """A copy of 15_event_collapse._collapse_lists()'s greedy-clique branch
    under cross-coin; `keep` is "earliest" (the engine's choice) or "latest"
    (the alternative), applied when two moments of one coin are in the
    chosen window."""
    items = sorted(moments, key=lambda m: (m["start_dt"], m["id"]))
    left = list(items)
    events = []
    while left:
        best = None
        for anchor in left:
            lo = anchor["start_dt"]
            members = [m for m in left
                       if 0 <= (m["start_dt"] - lo).total_seconds() / 3600.0
                       <= gap]
            seen, kept = set(), []
            seq = members if keep == "earliest" else list(reversed(members))
            for m in seq:
                if m["coin"] in seen:
                    continue
                seen.add(m["coin"])
                kept.append(m)
            kept.sort(key=lambda m: (m["start_dt"], m["id"]))
            key = (-len(kept), lo, kept[0]["id"])
            if best is None or key < best[0]:
                best = (key, kept)
        ids = {m["id"] for m in best[1]}
        events.append(sorted(ids))
        left = [m for m in left if m["id"] not in ids]
    events.sort(key=lambda g: g[0])
    return events


def main():
    started = dt.datetime.now(dt.timezone.utc)
    free_bytes = shutil.disk_usage(REPO).free
    ec = load("ec", "15_event_collapse.py")
    inputs = []

    def use(p):
        inputs.append((os.path.relpath(p, REPO), sha256_file(p)))
        return p

    raw = lab_cards.load_all(os.path.join(REPO, "cards"))
    moments = [{"id": c["card"], "coin": c["coin"], "kind": c["kind"],
                "start_dt": ec.parse_hour(c["start_hour_utc"])} for c in raw]
    by = {m["id"]: m for m in moments}
    ids = sorted(by)
    labels = [1 if by[i]["kind"] == "large" else 0 for i in ids]
    R = {}

    # ---- G-1 ---------------------------------------------------------------
    key = ec.moments_fingerprint(moments)
    r0 = random.Random(ec.SEED)
    answers = [r0.randint(0, 1) for _ in ids]
    g1 = []

    def attempt(name, fn):
        try:
            rec = fn()
            g1.append({"attempt": name, "result": "accepted",
                       "config": rec["config"], "events": rec["events"],
                       "boundary": round(rec["boundary"], 6),
                       "key_check": rec.get("key_check")})
        except Exception as e:      # the point is to record what is raised
            g1.append({"attempt": name, "result": type(e).__name__,
                       "detail": str(e)[:150]})

    true_cs = ec.collapse(moments, "card-span", "component", "any")
    shifted = [dict(m, start_dt=m["start_dt"] + dt.timedelta(
        hours=1000 * k)) for k, m in enumerate(moments)]
    forged = ec.collapse(shifted, "card-span", "component", "any")
    one = [dict(m) for m in moments]
    one[0]["start_dt"] = one[0]["start_dt"] + dt.timedelta(hours=1000)
    forged1 = ec.collapse(one, "card-span", "component", "any")
    attempt("true moments, card-span/component/any, key of the true moments",
            lambda: ec.chance_line(answers, labels, true_cs, ids, "block",
                                   key_moments_sha256=key))
    attempt("identity_map() of the true moments, key of the true moments",
            lambda: ec.chance_line(answers, labels, ec.identity_map(moments),
                                   ids, "block", key_moments_sha256=key))
    attempt("REVIEW-2 p4 attempt 1: start hours moved 1,000 h apart, "
            "key of the true moments",
            lambda: ec.chance_line(answers, labels, forged, ids, "block",
                                   key_moments_sha256=key))
    attempt("REVIEW-2 p4 attempt 1b: one card's start hour moved, key of the "
            "true moments",
            lambda: ec.chance_line(answers, labels, forged1, ids, "block",
                                   key_moments_sha256=key))
    attempt("key omitted",
            lambda: ec.chance_line(answers, labels, true_cs, ids, "block"))
    attempt("key given as None",
            lambda: ec.chance_line(answers, labels, true_cs, ids, "block",
                                   key_moments_sha256=None))
    attempt("LIMIT: forged map passed with its OWN moments fingerprint "
            "(what a judge who does not read the key could do)",
            lambda: ec.chance_line(answers, labels, forged, ids, "block",
                                   key_moments_sha256=forged
                                   .moments_sha256()))
    R["G-1"] = {"key_moments_sha256_true": key, "attempts": g1}

    # ---- G-2 ---------------------------------------------------------------
    draws = ec.SHUFFLES
    k = int(round(ec.TOP_FRACTION * draws))
    cal_path = use(os.path.join(REPO, "exam-prep", "collapse",
                                "run-" + CALIB_RUN, "shuffle-calibration.csv"))
    cal = list(csv.DictReader(open(cal_path, encoding="utf-8")))
    configs = []
    for r in cal:
        if r["config"] not in configs:
            configs.append(r["config"])
    g2 = []
    for cfg in configs:
        if cfg == "none/none/none":
            events = ec.identity_map(moments)
        else:
            d, rs, s = cfg.split("/")
            events = ec.collapse(moments, d, rs, s)
        reps = [sorted(ev, key=lambda c: (by[c]["start_dt"], c))[0]
                for ev in events]
        rl = [1 if by[c]["kind"] == "large" else 0 for c in reps]
        rr = random.Random(ec.SEED)
        ra = [rr.randint(0, 1) for _ in reps]
        pmf = null_pmf(len(reps), sum(ra), sum(rl))
        dist = reported_stat_dist(pmf, draws, k)
        lo, hi = spread(dist)
        rows = [x for x in cal if x["config"] == cfg]
        g2.append({"config": cfg, "n": len(reps),
                   "representative_reported": float(
                       rows[0]["representative_shuffle_1pct_boundary"]),
                   "representative_exact_1pct": round(float(
                       exact_top(pmf, ec.TOP_FRACTION)), 6),
                   "reported_stat_2_5pct": round(lo, 6),
                   "reported_stat_97_5pct": round(hi, 6),
                   "card_level": {x["predictor"]: float(
                       x["card_shuffle_1pct_boundary"]) for x in rows},
                   "block": {x["predictor"]: float(
                       x["block_shuffle_1pct_boundary"]) for x in rows}})
    # card-level, un-collapsed: two independent reported lines
    pmf = null_pmf(len(ids), sum(answers), sum(labels))
    dist = reported_stat_dist(pmf, draws, k)
    step = 2.0 / len(ids)
    apart = {j: round(p_apart(dist, j * step), 4) for j in (1, 2, 3, 4)}
    R["G-2"] = {"rows": g2, "card_level_n": len(ids),
                "card_level_exact_1pct": round(float(exact_top(
                    pmf, ec.TOP_FRACTION)), 6),
                "card_level_reported_2_5pct": round(spread(dist)[0], 6),
                "card_level_reported_97_5pct": round(spread(dist)[1], 6),
                "support_step": round(step, 6),
                "p_two_lines_apart_by_steps": apart}

    # ---- G-3 ---------------------------------------------------------------
    pairs_path = use(os.path.join(REPO, "data", "overlap", "pairs.csv"))
    pairs = list(csv.DictReader(open(pairs_path, encoding="utf-8")))
    span = Counter()
    before = Counter()
    same_calm = []
    for p in pairs:
        kinds = "+".join(sorted((p["kind_a"], p["kind_b"])))
        sc = "same coin" if p["same_coin"] == "yes" else "different coins"
        span[(kinds, sc)] += 1
        gap = int(p["start_gap_hours"])
        if gap <= 23:
            before[(kinds, sc)] += 1
        if p["same_coin"] == "yes":
            same_calm.append({"pair": "%s/%s" % (p["card_a"], p["card_b"]),
                              "kinds": kinds, "start_gap_hours": gap,
                              "shared_hours": int(p["shared_hours"]),
                              "before_windows_share_an_hour": gap <= 23})
    mm = open(use(os.path.join(REPO, "data", "moments",
                               "moment-manifest.md")),
              encoding="utf-8").read()
    m = re.search(r"calm pairs inside one coin closer than 48 h[^|]*\| (\d+) "
                  r"\|", mm)
    R["G-3"] = {"pairs": len(pairs),
                "card_span": {"%s · %s" % k2: v
                              for k2, v in sorted(span.items())},
                "before_window": {"%s · %s" % k2: v
                                  for k2, v in sorted(before.items())},
                "same_coin_pairs": same_calm,
                "moment_manifest_consecutive_calm_pairs_under_48h":
                    int(m.group(1)) if m else None}

    # ---- G-4 ---------------------------------------------------------------
    obs = [x.strip() for x in open(use(os.path.join(
        REPO, "data", "draw", "observation-coins.txt")),
        encoding="utf-8") if x.strip()]
    man = open(use(os.path.join(REPO, "data", "draw", "draw-manifest.md")),
               encoding="utf-8").read()
    book = open(use(os.path.join(REPO, "canteen", "2026-09-19-sofia.md")),
                encoding="utf-8").read().split("\n")
    trig = book[186].strip()          # line 187 of the frozen book
    named = re.findall(r"\b([A-Z0-9]+USDT)\b", trig)
    R["G-4"] = {"book_line_187": trig,
                "contracts_named_by_trigger": named,
                "observation_coins": obs,
                "named_contracts_in_observation_list":
                    {c: c in obs for c in named},
                "draw_manifest_disjoint_true":
                    bool(re.search(r'"disjoint": true', man)),
                "draw_manifest_observation_x_exam_overlap_empty":
                    bool(re.search(r'"observation_x_exam_overlap": \[\]',
                                   man))}

    # ---- G-5 ---------------------------------------------------------------
    g5 = []
    for d in ("move-window", "card-span"):
        gap = ec.DEFINITIONS[d]
        eng = ec.collapse(moments, d, "greedy-clique", "cross-coin")
        a = greedy_cross_coin(moments, gap, "earliest")
        b = greedy_cross_coin(moments, gap, "latest")
        sa = {tuple(e) for e in a}
        sb = {tuple(e) for e in b}
        both = lambda ev: sum(1 for e in ev  # noqa: E731
                              if len({by[c]["kind"] for c in e}) > 1)
        g5.append({"definition": d,
                   "copy_equals_engine": sorted(map(list, eng)) == sorted(a),
                   "events_keep_earliest": len(a),
                   "events_keep_latest": len(b),
                   "events_in_one_partition_only": len(sa ^ sb),
                   "events_holding_both_kinds_earliest": both(a),
                   "events_holding_both_kinds_latest": both(b)})
    R["G-5"] = g5

    # ---- run number, write once ---------------------------------------------
    script_sha = sha256_file(os.path.abspath(__file__))
    h = hashlib.sha256()
    h.update(("script:%s\n" % script_sha).encode())
    for f in ("15_event_collapse.py", "lab_cards.py"):
        h.update(("%s:%s\n" % (f, sha256_file(os.path.join(HERE, f))))
                 .encode())
    for name, sha in sorted(set(inputs)):
        h.update(("%s:%s\n" % (name, sha)).encode())
    for c in raw:
        h.update(("%s:%s\n" % (c["card"], c["sha256"])).encode())
    run_full = h.hexdigest()
    run16 = run_full[:16]
    core = json.loads(json.dumps({"run": run16, "input_fingerprint": run_full,
                                  "script_sha256": script_sha,
                                  "inputs": sorted(set(inputs)),
                                  "results": R}, default=str))
    runs_dir = os.path.join(OUT_DIR, "runs")
    os.makedirs(runs_dir, exist_ok=True)
    rec_path = os.path.join(runs_dir, run16 + ".json")
    if os.path.exists(rec_path):
        if json.load(open(rec_path, encoding="utf-8")) != core:
            die("run record %s exists with different content (RULES 30)"
                % rec_path)
        sys.stderr.write("run %s already recorded; nothing written\n" % run16)
        return

    A = ["# Third-fix checks — run `%s`" % run16, "",
         "Written by `scripts/26_third_fix_checks.py`. Every number below is "
         "counted by that script.", "",
         "| field | value |", "|---|---|",
         "| run number (RULES 29) | `%s` |" % run16,
         "| full input fingerprint | `%s` |" % run_full,
         "| written at (system clock, UTC, RULES 23) | %s |"
         % started.strftime("%Y-%m-%dT%H:%M:%SZ"),
         "| free disk space at start (bytes) | %d |" % free_bytes,
         "| `scripts/26_third_fix_checks.py` SHA-256 | `%s` |" % script_sha,
         "| `scripts/15_event_collapse.py` SHA-256 | `%s` |"
         % sha256_file(os.path.join(HERE, "15_event_collapse.py")),
         "", "## G-1 · what `chance_line()` accepts and refuses (third-fix "
         "engine)", "",
         "Fingerprint of the true moments (`moments_fingerprint()`): `%s`."
         % key, "", "| attempt | result | detail |", "|---|---|---|"]
    for r in g1:
        det = ("config %s, %d events, boundary %.6f, key_check %s"
               % (r["config"], r["events"], r["boundary"], r["key_check"])
               if r["result"] == "accepted" else r["detail"])
        A.append("| %s | %s | %s |" % (r["attempt"], r["result"],
                                       det.replace("|", "/")))
    x = R["G-2"]
    A += ["", "## G-2 · K-9, the representative column computed exactly", "",
          "Exact null (hypergeometric), the same synthetic answers and "
          "representatives as `15_event_collapse.py`. `reported` is the "
          "simulated value in `exam-prep/collapse/run-%s/"
          "shuffle-calibration.csv`; `2.5%% – 97.5%%` is the spread of the "
          "statistic the instrument reports (the 10th largest of %d draws), "
          "a description, not a threshold." % (CALIB_RUN, draws), "",
          "| configuration | n | representative, reported | exact 1% point "
          "| spread of the reported statistic, 2.5% – 97.5% | card-level "
          "(iid / event-constant) | block (iid / event-constant) |",
          "|---|---|---|---|---|---|---|"]
    for r in x["rows"]:
        A.append("| `%s` | %d | %.4f | %.4f | %.4f – %.4f | %.4f / %.4f | "
                 "%.4f / %.4f |"
                 % (r["config"], r["n"], r["representative_reported"],
                    r["representative_exact_1pct"],
                    r["reported_stat_2_5pct"], r["reported_stat_97_5pct"],
                    r["card_level"]["synthetic-iid"],
                    r["card_level"]["synthetic-event-constant"],
                    r["block"]["synthetic-iid"],
                    r["block"]["synthetic-event-constant"]))
    A += ["", "Un-collapsed card-level line (n = %d): exact 1%% point %.4f; "
          "the reported statistic falls between %.4f and %.4f (2.5%% – "
          "97.5%%). The support moves in steps of %.6f; the probability that "
          "two independent reported lines differ by at least 1, 2, 3, 4 steps "
          "is %s." % (x["card_level_n"], x["card_level_exact_1pct"],
                      x["card_level_reported_2_5pct"],
                      x["card_level_reported_97_5pct"], x["support_step"],
                      ", ".join("%s" % x["p_two_lines_apart_by_steps"][j]
                                for j in (1, 2, 3, 4)))]
    y = R["G-3"]
    A += ["", "## G-3 · K-8, overlapping card pairs", "",
          "Source `data/overlap/pairs.csv` (run `12ce59e2902a0034`), %d "
          "pairs whose 48-hour card spans share at least one clock hour (the "
          "manifest's definition). `before windows` = the subset whose 24-hour "
          "before windows share an hour (start gap <= 23 h)." % y["pairs"],
          "", "| kinds · coins | card spans share an hour | before windows "
          "share an hour |", "|---|---|---|"]
    for k2 in y["card_span"]:
        A.append("| %s | %d | %d |" % (k2, y["card_span"][k2],
                                       y["before_window"].get(k2, 0)))
    A += ["", "Same-coin pairs:", "",
          "| pair | kinds | start gap (h) | shared hours | before windows "
          "share an hour |", "|---|---|---|---|---|"]
    for r in y["same_coin_pairs"]:
        A.append("| %s | %s | %d | %d | %s |"
                 % (r["pair"], r["kinds"], r["start_gap_hours"],
                    r["shared_hours"],
                    "yes" if r["before_windows_share_an_hour"] else "no"))
    A += ["", "`data/moments/moment-manifest.md` records %s consecutive "
          "same-coin calm pairs closer than 48 h (it counts neighbours in time "
          "only, so a run of three close calm moments counts 2 there and 3 "
          "pairs here)." % y["moment_manifest_consecutive_calm_pairs_under_48h"]]
    z = R["G-4"]
    A += ["", "## G-4 · the facts JQ-B1 rests on", "",
          "| fact | value |", "|---|---|",
          "| `canteen/2026-09-19-sofia.md` line 187 | `%s` |"
          % z["book_line_187"].replace("|", "/"),
          "| contracts the frozen trigger names | %s |"
          % ", ".join(z["contracts_named_by_trigger"]),
          "| each named contract is in `data/draw/observation-coins.txt` | "
          "%s |" % z["named_contracts_in_observation_list"],
          "| `data/draw/draw-manifest.md` records `\"disjoint\": true` | %s |"
          % z["draw_manifest_disjoint_true"],
          "| `data/draw/draw-manifest.md` records "
          "`\"observation_x_exam_overlap\": []` | %s |"
          % z["draw_manifest_observation_x_exam_overlap_empty"], "",
          "Nothing under `exam/` was read. Whether the exam cards are in fact "
          "built from the drawn exam list is for the exam-building run to "
          "confirm (`exam-prep/HANDED-FORWARD.md`)."]
    A += ["", "## G-5 · greedy-clique under cross-coin: which moment of a "
          "coin is kept", "",
          "The engine keeps, in the chosen window, the earliest moment of "
          "each coin (by start hour, then card number). The same loop with "
          "only that choice reversed (keep the latest):", "",
          "| definition | copy equals engine | events, keep earliest | "
          "events, keep latest | events in one partition only | events "
          "holding both kinds, earliest / latest |", "|---|---|---|---|---|---|"]
    for r in g5:
        A.append("| `%s` | %s | %d | %d | %d | %d / %d |"
                 % (r["definition"], r["copy_equals_engine"],
                    r["events_keep_earliest"], r["events_keep_latest"],
                    r["events_in_one_partition_only"],
                    r["events_holding_both_kinds_earliest"],
                    r["events_holding_both_kinds_latest"]))
    A += ["", "## Inputs", "", "| file | SHA-256 |", "|---|---|"]
    for name, sha in sorted(set(inputs)):
        A.append("| `%s` | `%s` |" % (name, sha))
    A.append("")
    md_path = os.path.join(OUT_DIR, "third-fix-checks-%s.md" % run16)
    if os.path.exists(md_path):
        die("%s exists without a run record" % md_path)
    with open(md_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(A) + "\n")
    with open(rec_path, "w", encoding="utf-8") as fh:
        json.dump(core, fh, indent=1, sort_keys=True)
        fh.write("\n")
    sys.stderr.write("run %s written\n" % run16)


if __name__ == "__main__":
    main()
