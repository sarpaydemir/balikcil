#!/usr/bin/env python3
"""
30_fourth_fix_checks.py -- the checks the fourth-fix run's criteria fix
(exam-prep/fourth-fix/criteria-written-before-measuring.md, K-13 ... K-16).

What it does
------------
  H-1 (K-14) The engine's key check. Every attempt REVIEW-3 q4 made, the
      third-fix G-1 attempts, and attempts on what the fourth-fix run added
      (a subclass, a patched method, a tampered configuration label, a
      "latest" map). Each is reported as accepted or refused.
  H-2 (K-15) "Keep the latest". The engine's new option against two literal
      implementations written by the reviewers: REVIEW-3 q1's `literal()` and
      REVIEW-2 p1b's `greedy_latest()` (each function is read out of its
      probe file and executed by itself; the probes' own top-level code is not
      run). On the observation moments and on q1's 200 random moment sets.
      The engine's literal path with "earliest" against its existing path.
      Then the counts JQ-N1 part 2 shows, and the JQ-N1 table row of each
      "+latest" configuration.
  H-3 (K-13) The exact audit (scripts/29_identity_audit_exact.py) against
      REVIEW-3 q2's exact figures on the three sets q2 ran, and, cell by
      cell, against the third-fix audit (scripts/16_identity_audit.py) on all
      seven card sets.
  H-4 (K-16) What the unrounded-rank rendering changes, per ranked column.
  H-5 Observation moments: coins with two moments at one start hour (the
      card-number tie-break of "latest" can only matter there).

Input   : cards/; scripts/15_event_collapse.py; scripts/29_identity_audit_exact.py;
          exam-prep/review-3/probes/q1_greedy_latest.py, q2_tiefree_*.out;
          exam-prep/review-2/probes/p1_collapse_independent.py,
          p1b_greedy_convention.py; the audit runs in exam-prep/fourth-fix/
          identity/ and exam-prep/third-fix/identity/; the strict-flags and
          unrounded-rank card sets and their truth files.
Output  : exam-prep/fourth-fix/checks/fourth-fix-checks-<run16>.md
          exam-prep/fourth-fix/checks/runs/<run16>.json   (append-only)

Rules implemented
-----------------
RULES 12 : shuffles, line and seed are the instruments' own (imported).
RULES 19 : every number written here is counted by this script.
RULES 23 : the clock is read from the system.
RULES 29 / 30 : run number = SHA-256 of this script, the scripts it imports
           and every input file; a recorded run is never rewritten.

Constants: Q1_SETS = 200 and the seed 20260913 are REVIEW-3 q1's own (its
random sets are regenerated exactly as q1 drew them). No threshold, score or
trading rule is defined anywhere in this file.
"""

import ast
import csv
import datetime as dt
import glob
import hashlib
import importlib.util
import json
import os
import random
import shutil
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import lab_cards  # noqa: E402

OUT_DIR = os.path.join(REPO, "exam-prep", "fourth-fix", "checks")
Q1 = os.path.join(REPO, "exam-prep", "review-3", "probes",
                  "q1_greedy_latest.py")
P1 = os.path.join(REPO, "exam-prep", "review-2", "probes",
                  "p1_collapse_independent.py")
P1B = os.path.join(REPO, "exam-prep", "review-2", "probes",
                   "p1b_greedy_convention.py")
Q2_OUT = {
    "blinded-strict-flags": "q2_tiefree_strict-flags.out",
    "blinded-strict-flags-k1": "q2_tiefree_strict-flags-k1.out",
    "blinded-strict-flags-unrounded": "q2_tiefree_strict-flags-unrounded.out",
}
Q1_SETS = 200
Q1_SEED = 20260913
# the third-fix audit runs (THIRD-FIX §4.1), one per card set
THIRD = {"raw-observation": "4858581e2eb08704",
         "blinded-ratio": "12b07f79e74f0be7",
         "blinded-rank": "96f1d17e27b8afaf",
         "blinded-strict": "1f2ae3cf3a5b2044",
         "blinded-strict-flags": "e05144718b909704",
         "blinded-strict-flags-k1": "ded6a9caaf77d910",
         "blinded-strict-flags-unrounded": "34095384f8b94ab7"}
SF = os.path.join(REPO, "exam-prep", "blind-proof", "strict-flags")
UR = os.path.join(REPO, "exam-prep", "third-fix", "blind-proof",
                  "strict-flags-unrounded")
RANKED = ["quote vol", "trades", "taker buy%", "open int", "L/S acct",
          "top L/S pos", "taker L/S", "depth -1%", "depth +1%"]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def sha256_file(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def die(msg):
    sys.stderr.write("STOP: %s\n" % msg)
    sys.exit(1)


def function_from(path, name, env):
    """Read one top-level function out of a probe file and execute only its
    definition, in `env`. The probe's other top-level code is not run."""
    tree = ast.parse(open(path, encoding="utf-8").read())
    fn = [n for n in tree.body
          if isinstance(n, ast.FunctionDef) and n.name == name]
    if len(fn) != 1:
        die("%s: function %s not found exactly once" % (path, name))
    mod = ast.Module(body=fn, type_ignores=[])
    exec(compile(mod, path, "exec"), env)
    return env[name]


def raw_tokens(path, colname):
    """The printed tokens of one column of a card's before table (strings)."""
    lines = open(path, encoding="utf-8").read().split("\n")
    i0 = lines.index("## Before")
    for i in range(i0, len(lines)):
        if lines[i].startswith("| h |"):
            head = [x.strip() for x in lines[i].strip().strip("|").split("|")]
            k = head.index(colname)
            out = []
            j = i + 2
            while j < len(lines) and lines[j].startswith("|"):
                out.append([x.strip() for x in
                            lines[j].strip().strip("|").split("|")][k])
                j += 1
            if len(out) != 24:
                die("%s: before table has %d rows" % (path, len(out)))
            return out
    die("%s: no before table" % path)


def main():
    started = dt.datetime.now(dt.timezone.utc)
    free_bytes = shutil.disk_usage(REPO).free
    inputs = []

    def use(p):
        inputs.append((os.path.relpath(p, REPO), sha256_file(p)))
        return p

    ec = load("ec", use(os.path.join(HERE, "15_event_collapse.py")))
    ia_path = use(os.path.join(HERE, "29_identity_audit_exact.py"))
    use(os.path.join(HERE, "lab_cards.py"))
    use(Q1)
    use(P1)
    use(P1B)
    for f in Q2_OUT.values():
        use(os.path.join(REPO, "exam-prep", "review-3", "probes", f))
    cards = lab_cards.load_all(os.path.join(REPO, "cards"))
    for c in cards:
        inputs.append(("cards/%s.md" % c["card"], c["sha256"]))
    ms = [{"id": c["card"], "coin": c["coin"], "kind": c["kind"],
           "start_dt": ec.parse_hour(c["start_hour_utc"])} for c in cards]
    by_id = {m["id"]: m for m in ms}
    ids = sorted(by_id)
    out = {}
    L = []

    # ================= H-1 · the key check ==================================
    labels = [by_id[i]["kind"] for i in ids]
    answers = ["large"] * len(ids)
    key = ec.moments_fingerprint(ms)
    CFG = ("card-span", "component", "any")
    h1 = []

    def attempt(name, fn, expect):
        try:
            r = fn()
            res = "accepted"
            info = "events %d, key_check %s, record event_map_sha256 %s…" % (
                r["events"], r["key_check"], r["event_map_sha256"][:12])
        except Exception as e:  # noqa: BLE001 -- the refusal is the result
            res = "refused"
            info = "%s: %s" % (type(e).__name__, str(e)[:80])
        h1.append({"attempt": name, "result": res, "expected": expect,
                   "as_expected": res == expect, "detail": info})

    true_map = ec.collapse(ms, *CFG)
    attempt("q4-0 true map, true key",
            lambda: ec.chance_line(answers, labels, ec.collapse(ms, *CFG),
                                   ids, "block", key_moments_sha256=key),
            "accepted")
    m1 = [dict(m) for m in ms]
    m1[0]["coin"] = "XUSDT"
    attempt("q4-1 one coin changed, true key",
            lambda: ec.chance_line(answers, labels, ec.collapse(m1, *CFG),
                                   ids, "block", key_moments_sha256=key),
            "refused")
    m2 = [dict(m) for m in ms] + [{"id": "C999", "coin": "XUSDT",
                                   "kind": "calm",
                                   "start_dt": ms[0]["start_dt"]}]
    attempt("q4-2 extra moment, true key",
            lambda: ec.chance_line(answers, labels, ec.collapse(m2, *CFG),
                                   ids, "block", key_moments_sha256=key),
            "refused")
    m3 = [dict(m) for m in ms]
    m3[5]["start_dt"] = m3[5]["start_dt"] + dt.timedelta(hours=2000)
    em3 = ec.collapse(m3, *CFG)
    em3.moments_sha256 = lambda: key
    attempt("q4-3 forged hour, instance method patched to return the key",
            lambda: ec.chance_line(answers, labels, em3, ids, "block",
                                   key_moments_sha256=key), "refused")

    class EM(ec.EventMap):
        def moments_sha256(self):
            return key
    src = ec.collapse(m3, *CFG)
    em4 = EM(list(src), src.definition, src.resolution, src.scope, m3)
    attempt("q4-4 forged hour, subclass overriding moments_sha256()",
            lambda: ec.chance_line(answers, labels, em4, ids, "block",
                                   key_moments_sha256=key), "refused")
    em5 = ec.collapse(m3, *CFG)
    em5.moments = ec.collapse(ms, *CFG).moments
    attempt("q4-5 forged hour, .moments overwritten with the true tuple",
            lambda: ec.chance_line(answers, labels, em5, ids, "block",
                                   key_moments_sha256=key), "refused")
    em4b = EM(list(true_map), true_map.definition, true_map.resolution,
              true_map.scope, ms)
    attempt("H1-6 TRUE map wrapped in a subclass, true key",
            lambda: ec.chance_line(answers, labels, em4b, ids, "block",
                                   key_moments_sha256=key), "refused")
    m7 = [dict(m) for m in ms]
    for m in m7:
        m["start_dt"] = m["start_dt"] + dt.timedelta(hours=1000) \
            if m["id"] < "C150" else m["start_dt"]
    attempt("G1 forged hours (half the moments moved 1,000 h), true key",
            lambda: ec.chance_line(answers, labels, ec.collapse(m7, *CFG),
                                   ids, "block", key_moments_sha256=key),
            "refused")
    attempt("G1 key omitted",
            lambda: ec.chance_line(answers, labels, ec.collapse(ms, *CFG),
                                   ids, "block"), "refused")
    attempt("G1 key None",
            lambda: ec.chance_line(answers, labels, ec.collapse(ms, *CFG),
                                   ids, "block", key_moments_sha256=None),
            "refused")
    em8 = ec.collapse(ms, *CFG)
    em8.config = "card-span/greedy-clique/cross-coin"
    attempt("H1-8 configuration label changed after construction",
            lambda: ec.chance_line(answers, labels, em8, ids, "block",
                                   key_moments_sha256=key), "refused")
    em9 = ec.collapse(ms, "card-span", "greedy-clique", "cross-coin")
    em9.same_coin_keep = "latest"
    attempt("H1-9 same_coin_keep changed after construction",
            lambda: ec.chance_line(answers, labels, em9, ids, "block",
                                   key_moments_sha256=key), "refused")
    attempt("H1-10 a plain list of events",
            lambda: ec.chance_line(answers, labels, [list(e) for e in
                                                     true_map], ids, "block",
                                   key_moments_sha256=key), "refused")
    em11 = ec.collapse(ms, *CFG)
    em11.sha256 = lambda: "0" * 64
    rec11 = {}

    def a11():
        r = ec.chance_line(answers, labels, em11, ids, "block",
                           key_moments_sha256=key)
        rec11.update(r)
        return r
    attempt("H1-11 true map, instance sha256() patched to a constant",
            a11, "accepted")
    attempt("H1-12 'latest' card-span map, true key",
            lambda: ec.chance_line(answers, labels, ec.collapse(
                ms, "card-span", "greedy-clique", "cross-coin",
                same_coin_keep="latest"), ids, "block",
                key_moments_sha256=key), "accepted")
    attempt("H1-13 'latest' requested with component",
            lambda: ec.collapse(ms, "card-span", "component", "cross-coin",
                                same_coin_keep="latest"), "refused")
    rec_true = ec.chance_line(answers, labels, ec.collapse(ms, *CFG), ids,
                              "block", key_moments_sha256=key)
    out["H-1"] = {"attempts": h1,
                  "all_as_expected": all(x["as_expected"] for x in h1),
                  "record_event_map_sha256_equals_method": rec_true[
                      "event_map_sha256"] == true_map.sha256(),
                  "patched_sha256_not_in_record":
                      rec11.get("event_map_sha256") == true_map.sha256()}
    if not out["H-1"]["all_as_expected"]:
        die("H-1: an attempt did not behave as K-14 requires: %s"
            % [x["attempt"] for x in h1 if not x["as_expected"]])

    # ================= H-2 · keep the latest ================================
    q1_literal = function_from(Q1, "literal", {})
    p1 = load("p1", P1)
    p1b_latest = function_from(P1B, "greedy_latest", {"p": p1})
    t0 = min(m["start_dt"] for m in ms)
    obs = [{"id": m["id"], "coin": m["coin"],
            "h": int((m["start_dt"] - t0).total_seconds() // 3600)}
           for m in ms]
    p1ms = p1.read_cards()
    if sorted((m["id"], m["coin"]) for m in p1ms) != \
            sorted((m["id"], m["coin"]) for m in ms):
        die("H-2: p1's card reader and the engine's disagree on id/coin")
    T0 = dt.datetime(2025, 1, 1, tzinfo=dt.timezone.utc)

    def to_engine(xs):
        return [{"id": x["id"], "coin": x["coin"],
                 "start_dt": T0 + dt.timedelta(hours=x["h"])} for x in xs]

    def S(evs):
        return sorted(tuple(sorted(e)) for e in evs)

    h2 = {"observation": {}, "random": {}}
    for d in ("move-window", "card-span"):
        gap = ec.DEFINITIONS[d]
        eng_l = S(ec.collapse(ms, d, "greedy-clique", "cross-coin",
                              same_coin_keep="latest"))
        eng_e = S(ec.collapse(ms, d, "greedy-clique", "cross-coin"))
        lit_e = S(ec._greedy_literal(ms, gap, "earliest"))
        q1_l = S(q1_literal(obs, gap, True, "latest"))
        p1b_l = S(p1b_latest(p1ms, d))
        row = {"engine_latest_events": len(eng_l),
               "engine_earliest_events": len(eng_e),
               "latest_equals_q1_literal": eng_l == q1_l,
               "latest_equals_p1b": eng_l == p1b_l,
               "literal_earliest_equals_engine_earliest": lit_e == eng_e,
               "events_in_one_partition_only_latest_vs_earliest":
                   len(set(eng_l) ^ set(eng_e))}
        # the JQ-N1 table row of the "+latest" configuration
        sizes = Counter(len(e) for e in eng_l)
        same = [max(Counter(by_id[c]["coin"] for c in e).values())
                for e in eng_l]
        row["table_row"] = {
            "events": len(eng_l), "events_of_1_card": sizes.get(1, 0),
            "largest_event": max(len(e) for e in eng_l),
            "events_holding_both_kinds": sum(
                1 for e in eng_l if len({by_id[c]["kind"] for c in e}) > 1),
            "events_holding_2plus_cards_of_one_coin": sum(
                1 for x in same if x >= 2),
            "largest_same_coin_count": max(same),
            "block_immovable_events": sum(1 for e in eng_l
                                          if sizes[len(e)] == 1),
            "block_cards_in_immovable_events": sum(
                len(e) for e in eng_l if sizes[len(e)] == 1)}
        h2["observation"][d] = row
    rng = random.Random(Q1_SEED)
    diff = Counter()
    for _ in range(Q1_SETS):
        n = rng.randint(5, 25)
        coins = ["X", "Y", "Z", "W"][:rng.randint(2, 4)]
        xs = [{"id": "C%03d" % i, "coin": rng.choice(coins),
               "h": rng.randint(0, 150)} for i in range(n)]
        em = to_engine(xs)
        for d in ("move-window", "card-span"):
            gap = ec.DEFINITIONS[d]
            if S(ec.collapse(em, d, "greedy-clique", "cross-coin",
                             same_coin_keep="latest")) != \
                    S(q1_literal(xs, gap, True, "latest")):
                diff[(d, "latest vs q1 literal")] += 1
            if S(ec._greedy_literal(em, gap, "earliest")) != \
                    S(ec.collapse(em, d, "greedy-clique", "cross-coin")):
                diff[(d, "literal earliest vs engine earliest")] += 1
    for d in ("move-window", "card-span"):
        for what in ("latest vs q1 literal",
                     "literal earliest vs engine earliest"):
            h2["random"]["%s: %s" % (d, what)] = diff[(d, what)]
    ok2 = all(r["latest_equals_q1_literal"] and r["latest_equals_p1b"]
              and r["literal_earliest_equals_engine_earliest"]
              for r in h2["observation"].values()) and not sum(diff.values())
    h2["accepted"] = ok2
    out["H-2"] = h2
    if not ok2:
        die("H-2: the 'latest' option does not match the literal references "
            "(K-15); nothing from it may be used")

    # ================= H-5 · same coin, same start hour =====================
    cnt = Counter((m["coin"], m["start_dt"]) for m in ms)
    out["H-5"] = {"coin_start_hours_with_2plus_moments":
                  sum(1 for v in cnt.values() if v > 1)}

    # ================= H-3 · the exact audit ================================
    ia_sha = sha256_file(ia_path)
    new_runs = {}
    for rec in sorted(glob.glob(os.path.join(
            REPO, "exam-prep", "fourth-fix", "identity", "runs", "*.json"))):
        r = json.load(open(rec, encoding="utf-8"))
        if r.get("script_sha256") == ia_sha and "card_set" in r:
            new_runs[r["card_set"]] = r
    missing = sorted(set(THIRD) - set(new_runs))
    if missing:
        die("H-3: no exact-audit run for %s; run "
            "exam-prep/fourth-fix/run-instruments.sh first" % missing)
    h3 = {"sets": {}, "q2": {}}
    for lab, run3 in THIRD.items():
        rn = new_runs[lab]
        nd = os.path.join(REPO, rn["output_dir"])
        od = os.path.join(REPO, "exam-prep", "third-fix", "identity",
                          "run-" + run3)
        r3 = json.load(open(os.path.join(REPO, "exam-prep", "third-fix",
                                         "identity", "runs", run3 + ".json"),
                            encoding="utf-8"))
        a_new = use(os.path.join(nd, "identity-audit-%s.csv" % lab))
        a_old = use(os.path.join(od, "identity-audit-%s.csv" % lab))
        t_new = use(os.path.join(nd, "hour-linkage-%s.csv" % lab))
        t_old = use(os.path.join(od, "hour-linkage-%s.csv" % lab))
        rows_n = {x["family"]: x for x in csv.DictReader(open(a_new))}
        rows_o = {x["family"]: x for x in csv.DictReader(open(a_old))}
        cells = []
        for fam in rows_o:
            for col in rows_o[fam]:
                if rows_o[fam][col] != rows_n[fam][col]:
                    cells.append({"family": fam, "column": col,
                                  "third_fix": rows_o[fam][col],
                                  "exact": rows_n[fam][col]})
        h3["sets"][lab] = {
            "exact_run": rn["run"], "third_fix_run": run3,
            "hour_linkage_identical": sha256_file(t_new) == sha256_file(t_old),
            "t4_identical": rn["t4_release_names"] == r3["t4_release_names"],
            "features_used_identical": all(
                rows_o[f]["features_used"] == rows_n[f]["features_used"]
                for f in rows_o),
            "cells_differing": cells,
            "gate_row": {k: rows_n["ALL-removable"][k] for k in (
                "features_used", "nn_same_coin_accuracy", "nn_chance_1pct",
                "nn_beats_chance", "cards_with_tied_nn", "nn_tie_free",
                "nn_tie_free_chance_1pct", "nn_tie_free_beats_chance",
                "pair_auc", "auc_chance_1pct", "auc_beats_chance")}}
        if lab in Q2_OUT:
            q2p = os.path.join(REPO, "exam-prep", "review-3", "probes",
                               Q2_OUT[lab])
            res = []
            for line in open(q2p, encoding="utf-8"):
                p = [x.strip() for x in line.split("|")]
                if len(p) < 9 or p[0] == "family":
                    continue
                fam = p[0]
                x = rows_n[fam]
                ok = (x["features_used"] == p[1]
                      and x["cards_with_tied_nn"] == p[3]
                      and "%.4f" % float(x["nn_tie_free"]) == p[5]
                      and "%.4f" % float(x["nn_tie_free_chance_1pct"]) == p[6]
                      and (x["nn_tie_free_beats_chance"] == "YES")
                      == (p[7] == "YES"))
                res.append({"family": fam, "q2_tied_exact": p[3],
                            "audit_tied": x["cards_with_tied_nn"],
                            "q2_tie_free": p[5],
                            "audit_tie_free": "%.4f" % float(x["nn_tie_free"]),
                            "q2_line": p[6],
                            "audit_line": "%.4f" % float(
                                x["nn_tie_free_chance_1pct"]),
                            "equal": ok})
            h3["q2"][lab] = res
    ok3 = all(all(r["equal"] for r in v) for v in h3["q2"].values()) and all(
        s["hour_linkage_identical"] and s["t4_identical"]
        and s["features_used_identical"] for s in h3["sets"].values())
    h3["accepted"] = ok3
    out["H-3"] = h3
    if not ok3:
        die("H-3: the exact audit fails K-13's acceptance check; nothing "
            "from it may be used")

    # ================= H-4 · what the unrounded rank changes ================
    tsf = {r["id"]: r for r in csv.DictReader(open(use(os.path.join(
        SF, "truth-strict-flags.csv")), encoding="utf-8"))}
    tur = {r["id"]: r for r in csv.DictReader(open(use(os.path.join(
        UR, "truth-strict-flags-unrounded.csv")), encoding="utf-8"))}
    if {k: v["source_card"] for k, v in tsf.items()} != \
            {k: v["source_card"] for k, v in tur.items()}:
        die("H-4: the two sets do not number their cards alike")
    h4 = {}
    for col in RANKED:
        h4[col] = {"cards_where_renderings_differ": 0,
                   "cards_with_a_printed_tie": 0,
                   "hours_tied_on_raw_card": 0,
                   "hours_tied_on_raw_card_ranked_apart": 0,
                   "cards_with_an_hour_ranked_apart": 0}
    for bid in sorted(tsf):
        pa = use(os.path.join(SF, "cards", bid + ".md"))
        pb = use(os.path.join(UR, "cards", bid + ".md"))
        ca = lab_cards.parse_any_card(pa)
        cb = lab_cards.parse_any_card(pb)
        raw = os.path.join(REPO, "cards", tsf[bid]["source_card"] + ".md")
        for col in RANKED:
            name = col + " r"
            if name not in ca["cols"] or name not in cb["cols"]:
                die("H-4: %s has no column %r" % (bid, name))
            r = h4[col]
            if ca["cols"][name] != cb["cols"][name]:
                r["cards_where_renderings_differ"] += 1
            toks = raw_tokens(raw, col)
            ranks = cb["cols"][name]
            tied = [i for i in range(24)
                    if any(toks[j] == toks[i] for j in range(24) if j != i)]
            apart = [i for i in tied
                     if any(toks[j] == toks[i] and ranks[j] != ranks[i]
                            for j in range(24) if j != i)]
            r["hours_tied_on_raw_card"] += len(tied)
            r["hours_tied_on_raw_card_ranked_apart"] += len(apart)
            r["cards_with_a_printed_tie"] += 1 if tied else 0
            r["cards_with_an_hour_ranked_apart"] += 1 if apart else 0
    tot = {"hours_tied_on_raw_card_ranked_apart": sum(
        v["hours_tied_on_raw_card_ranked_apart"] for v in h4.values())}
    cards_any = set()
    for bid in sorted(tsf):
        cb = lab_cards.parse_any_card(os.path.join(UR, "cards", bid + ".md"))
        raw = os.path.join(REPO, "cards", tsf[bid]["source_card"] + ".md")
        for col in RANKED:
            toks = raw_tokens(raw, col)
            ranks = cb["cols"][col + " r"]
            if any(toks[i] == toks[j] and ranks[i] != ranks[j]
                   for i in range(24) for j in range(24) if i != j):
                cards_any.add(bid)
                break
    tot["cards_with_any_hour_ranked_apart"] = len(cards_any)
    out["H-4"] = {"by_column": h4, "total": tot, "cards": len(tsf)}

    # ================= run number and record ================================
    h = hashlib.sha256()
    h.update(("script:" + sha256_file(os.path.abspath(__file__)) + "\n")
             .encode())
    for name, s in sorted(set(inputs)):
        h.update(("%s:%s\n" % (name, s)).encode())
    run_full = h.hexdigest()
    run16 = run_full[:16]
    core = {"run": run16, "input_fingerprint": run_full,
            "script_sha256": sha256_file(os.path.abspath(__file__)),
            "results": out}
    runs_dir = os.path.join(OUT_DIR, "runs")
    os.makedirs(runs_dir, exist_ok=True)
    rec_path = os.path.join(runs_dir, run16 + ".json")
    if os.path.exists(rec_path):
        old = json.load(open(rec_path, encoding="utf-8"))
        if json.loads(json.dumps(core)) != {k: old.get(k) for k in core}:
            die("run record %s exists with different content (RULES 30)"
                % rec_path)
        sys.stderr.write("run %s already recorded with identical results; "
                         "nothing written\n" % run16)
        return

    # ================= report ===============================================
    L.append("# Fourth-fix checks — run `%s`" % run16)
    L.append("")
    L.append("Written by `scripts/30_fourth_fix_checks.py` at %s (system "
             "clock, RULES 23); free disk at start %d bytes. Criteria: "
             "`exam-prep/fourth-fix/criteria-written-before-measuring.md`."
             % (started.strftime("%Y-%m-%dT%H:%M:%SZ"), free_bytes))
    L.append("")
    L.append("## H-1 · the engine's key check (K-14)")
    L.append("")
    L.append("| attempt | result | K-14 expects | detail |")
    L.append("|---|---|---|---|")
    for x in h1:
        L.append("| %s | **%s** | %s | %s |" % (x["attempt"], x["result"],
                                               x["expected"],
                                               x["detail"].replace("|", "/")))
    L.append("")
    L.append("Every attempt as K-14 requires: **%s**. The record's "
             "`event_map_sha256` equals `EventMap.sha256()` of the true map "
             "(formula unchanged): %s. With `sha256()` patched on the "
             "instance, the record still carries the true fingerprint: %s."
             % (out["H-1"]["all_as_expected"],
                out["H-1"]["record_event_map_sha256_equals_method"],
                out["H-1"]["patched_sha256_not_in_record"]))
    L.append("")
    L.append("## H-2 · keep the latest (K-15)")
    L.append("")
    L.append("| definition | events, earliest | events, latest | latest = "
             "q1 literal | latest = p1b | literal path with earliest = "
             "engine | events in one partition only |")
    L.append("|---|---|---|---|---|---|---|")
    for d, r in h2["observation"].items():
        L.append("| %s | %d | %d | %s | %s | %s | %d |" % (
            d, r["engine_earliest_events"], r["engine_latest_events"],
            r["latest_equals_q1_literal"], r["latest_equals_p1b"],
            r["literal_earliest_equals_engine_earliest"],
            r["events_in_one_partition_only_latest_vs_earliest"]))
    L.append("")
    L.append("Random moment sets (q1's generator, seed %d, %d sets), sets "
             "that differ:" % (Q1_SEED, Q1_SETS))
    L.append("")
    for k, v in h2["random"].items():
        L.append("- %s: %d of %d" % (k, v, Q1_SETS))
    L.append("")
    L.append("Table row of each `+latest` configuration, in JQ-N1's columns:")
    L.append("")
    L.append("| configuration | events | events of 1 card | largest event | "
             "events holding a large and a calm card | events holding 2+ "
             "cards of one coin | largest same-coin count | block: events "
             "that cannot move | block: cards in them |")
    L.append("|---|---|---|---|---|---|---|---|---|")
    for d, r in h2["observation"].items():
        t = r["table_row"]
        L.append("| %s / greedy-clique / cross-coin + latest | %d | %d | %d "
                 "| %d | %d | %d | %d | %d |" % (
                     d, t["events"], t["events_of_1_card"],
                     t["largest_event"], t["events_holding_both_kinds"],
                     t["events_holding_2plus_cards_of_one_coin"],
                     t["largest_same_coin_count"],
                     t["block_immovable_events"],
                     t["block_cards_in_immovable_events"]))
    L.append("")
    L.append("Accepted (K-15): **%s**." % h2["accepted"])
    L.append("")
    L.append("## H-3 · the exact audit (K-13)")
    L.append("")
    L.append("Against REVIEW-3 q2 (tied cards exact, tie-free score, its "
             "line, its verdict, at 4 decimals):")
    L.append("")
    L.append("| card set | family | q2 tied (exact) | audit tied | q2 "
             "tie-free (line) | audit tie-free (line) | equal |")
    L.append("|---|---|---|---|---|---|---|")
    for lab, res in h3["q2"].items():
        for r in res:
            L.append("| %s | `%s` | %s | %s | %s (%s) | %s (%s) | %s |" % (
                lab, r["family"], r["q2_tied_exact"], r["audit_tied"],
                r["q2_tie_free"], r["q2_line"], r["audit_tie_free"],
                r["audit_line"], r["equal"]))
    L.append("")
    L.append("Against the third-fix audit, every set:")
    L.append("")
    L.append("| card set | exact run | third-fix run | T3 CSV identical | "
             "T4 identical | features identical | cells that differ |")
    L.append("|---|---|---|---|---|---|---|")
    for lab, s in h3["sets"].items():
        L.append("| %s | `%s` | `%s` | %s | %s | %s | %d |" % (
            lab, s["exact_run"], s["third_fix_run"],
            s["hour_linkage_identical"], s["t4_identical"],
            s["features_used_identical"], len(s["cells_differing"])))
    L.append("")
    L.append("Every cell that differs (third-fix → exact):")
    L.append("")
    L.append("| card set | family | column | third-fix | exact |")
    L.append("|---|---|---|---|---|")
    for lab, s in h3["sets"].items():
        for c in s["cells_differing"]:
            L.append("| %s | `%s` | %s | %s | %s |" % (
                lab, c["family"], c["column"], c["third_fix"], c["exact"]))
    L.append("")
    L.append("Gate row (`ALL-removable`) in the exact audit:")
    L.append("")
    L.append("| card set | features | NN (line) | tied cards | tie-free "
             "(line) | pair AUC (line) |")
    L.append("|---|---|---|---|---|---|")
    for lab, s in h3["sets"].items():
        g = s["gate_row"]
        L.append("| %s | %s | %s (%s) %s | %s | %s (%s) %s | %s (%s) %s |" % (
            lab, g["features_used"], g["nn_same_coin_accuracy"],
            g["nn_chance_1pct"], g["nn_beats_chance"],
            g["cards_with_tied_nn"], g["nn_tie_free"],
            g["nn_tie_free_chance_1pct"], g["nn_tie_free_beats_chance"],
            g["pair_auc"], g["auc_chance_1pct"], g["auc_beats_chance"]))
    L.append("")
    L.append("Accepted (K-13): **%s**." % h3["accepted"])
    L.append("")
    L.append("## H-4 · what the unrounded-rank rendering changes (K-16)")
    L.append("")
    L.append("On the %d observation cards; `strict-flags` against the "
             "unrounded-rank set, paired by `source_card`. \"Tied on the raw "
             "card\": the hour prints the same token as another hour of the "
             "same column on the raw card's before table. \"Ranked apart\": "
             "such an hour gets a different rank from an hour it ties with, "
             "on the unrounded-rank card." % len(tsf))
    L.append("")
    L.append("| column | cards where the two renderings differ | cards with "
             "a printed tie | hours tied on the raw card | of those, ranked "
             "apart | cards with an hour ranked apart |")
    L.append("|---|---|---|---|---|---|")
    for col, r in h4.items():
        L.append("| `%s` | %d | %d | %d | %d | %d |" % (
            col, r["cards_where_renderings_differ"],
            r["cards_with_a_printed_tie"], r["hours_tied_on_raw_card"],
            r["hours_tied_on_raw_card_ranked_apart"],
            r["cards_with_an_hour_ranked_apart"]))
    L.append("")
    L.append("Cards with at least one hour ranked apart in any ranked "
             "column: **%d of %d**." % (tot["cards_with_any_hour_ranked_apart"],
                                        len(tsf)))
    L.append("")
    L.append("## H-5 · same coin, same start hour")
    L.append("")
    L.append("Coin-and-start-hour combinations carrying two or more "
             "observation moments: **%d**."
             % out["H-5"]["coin_start_hours_with_2plus_moments"])
    L.append("")
    L.append("## Inputs")
    L.append("")
    L.append("Run number `%s` = SHA-256 over this script and %d input files "
             "(the 306 cards, the probes and audit outputs named above, the "
             "two card sets of H-4)." % (run16, len(set(inputs))))
    L.append("")
    md = os.path.join(OUT_DIR, "fourth-fix-checks-%s.md" % run16)
    with open(md, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    with open(rec_path, "w", encoding="utf-8") as fh:
        json.dump(core, fh, indent=1, sort_keys=True)
        fh.write("\n")
    sys.stderr.write("run %s written: %s\n" % (run16,
                                               os.path.relpath(md, REPO)))


if __name__ == "__main__":
    main()
