#!/usr/bin/env python3
"""
exam_36_draw_question_v2_check.py -- checks the second version of the juror
                                     question JQ-DRAW against the exam moment
                                     pool, against its own claims, and against
                                     the wall.

What it does
------------
1. Re-measures every fact that open-questions/JQ-DRAW.md section 1 states:
     F1  each kind holds more than the TACTICS 6 card count (200 / 200);
     F2  every exam coin has exactly as many calm as large-movement moments;
     F3  no two moments share both start hour and coin;
     F4  the pool's stored 24-hour change of every moment equals
         close(t0+23h) / close(t0-1h) - 1, recomputed from the exam hourly
         klines with scripts/06_find_moments.py's own loader; and the 200
         largest large-movement moments by |simple change| are not the same
         200 as by |log change| (count of differing moments recorded);
     F5  the draw number at TACTICS.md line 22 equals the seed recorded in
         exam/moments/pool-report.json and the SEED constant of
         scripts/04_draw.py, and both scripts feed it to random.Random
         (static text check of the two scripts).
   Also records, for the reviewer only: whether any two large-movement moments
   share a size (the tie rule of part a), and per-coin feasibility of
   Coin-matched.
2. Measures whether each choice in section 4 of the question (list order,
   generator use, order of the two draws, coin order) changes which moments are
   drawn. Uses seeds 1..1000 ONLY; the draw number is excluded, so no part of
   the real exam draw is computed. Only counts of differing moments are kept.
   Also checks that sample(list, 0) leaves the generator state unchanged.
3. Scans open-questions/JQ-DRAW.md, in ANY case and as whole words, for: every
   exam coin's symbol and base name; every name, base ticker, search-hit id and
   search-hit name in exam/data/external/coin-names.json, and every word of 4 or
   more letters inside those; date and clock patterns; eight-digit runs; month
   and weekday names; decimal numbers. EVERY match fails the check
   (open-questions/README.md: no exam coin's name, "not even as a word matched
   by a scan"). Lists every digit run with its line numbers.
4. Writes one record under exam/draw-question/ (matched words are written ONLY
   there, never elsewhere) and appends one line with clock readings to
   exam/draw-question/v2-check-runs.jsonl.

It chooses no moment and runs no exam draw.

Input   : open-questions/JQ-DRAW.md, TACTICS.md, exam/draw/exam-coins.txt,
          exam/moments/moments.csv, exam/moments/pool-report.json,
          exam/data/external/coin-names.json, exam/data/klines_1h/<SYM>/*.zip,
          scripts/06_find_moments.py (imported, unchanged; main() not called),
          scripts/04_draw.py, scripts/exam_27_find_moments.py (read as text)
Output  : exam/draw-question/JQ-DRAW-v2-check-<run16>.json
          exam/draw-question/v2-check-runs.jsonl   (append-only)
          console; exit status 1 if any fact fails or the scan matches anything
Rules   : RULES 9 and TACTICS 6 (names and dates hidden), RULES 19 (only
          measured numbers), RULES 23 (clock read from the system),
          RULES 29/30 (run number = SHA-256 of the inputs; an existing record
          with different content stops the script).
Constants (where each comes from):
  CARDS_LARGE = CARDS_CALM = 200   TACTICS.md §6 lines 99-100
  MECH_SEEDS = 1..1000             the seed range of the JQ-DRAW-v1 review §4,
                                   chosen there to avoid the draw number
  NAME_WORD_MIN = 4                the word length of the JQ-DRAW-v1 review §3
Randomness: random.Random(s) for s in MECH_SEEDS only.
Usage   : python3 -B scripts/exam_36_draw_question_v2_check.py
"""

import collections
import csv
import hashlib
import importlib.util
import json
import math
import os
import random
import re
import statistics
import sys
from datetime import datetime, timezone

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
QUESTION = os.path.join(ROOT, "open-questions", "JQ-DRAW.md")
TACTICS = os.path.join(ROOT, "TACTICS.md")
COINS = os.path.join(ROOT, "exam", "draw", "exam-coins.txt")
MOMENTS = os.path.join(ROOT, "exam", "moments", "moments.csv")
POOL_REPORT = os.path.join(ROOT, "exam", "moments", "pool-report.json")
COIN_NAMES = os.path.join(ROOT, "exam", "data", "external", "coin-names.json")
EXAM_KLINES = os.path.join(ROOT, "exam", "data", "klines_1h")
SCRIPT_06 = os.path.join(HERE, "06_find_moments.py")
SCRIPT_04 = os.path.join(HERE, "04_draw.py")
SCRIPT_27 = os.path.join(HERE, "exam_27_find_moments.py")
OUT_DIR = os.path.join(ROOT, "exam", "draw-question")
RUNS_LOG = os.path.join(OUT_DIR, "v2-check-runs.jsonl")

CARDS_LARGE = 200          # TACTICS.md §6 line 99
CARDS_CALM = 200           # TACTICS.md §6 line 100
MECH_SEEDS = range(1, 1001)  # JQ-DRAW-v1 review §4
NAME_WORD_MIN = 4          # JQ-DRAW-v1 review §3
QUOTE_SUFFIX = "USDT"
HOUR_MS = 3600 * 1000

MONTHS = ("january february march april may june july august september "
          "october november december jan feb mar apr jun jul aug sep sept oct "
          "nov dec").split()
WEEKDAYS = ("monday tuesday wednesday thursday friday saturday sunday "
            "mon tue tues wed thu thur thurs fri sat sun").split()
PATTERNS = [r"\d{4}-\d{2}-\d{2}", r"\d{4}-\d{2}", r"\d{8}", r"\b\d{1,2}:\d{2}\b",
            r"\b\d+\.\d+\b", r"\b\d+,\d{3}\b"]


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_06():
    spec = importlib.util.spec_from_file_location("find_moments_06", SCRIPT_06)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def ordered(rows, key):
    return sorted(rows, key=key)


def by_hour_then_symbol(r):
    return (int(r["start_ms"]), r["symbol"])


def by_symbol_then_hour(r):
    return (r["symbol"], int(r["start_ms"]))


def ids(rows):
    return [r["moment_id"] for r in rows]


def draw_section4(rng, large_list, calm_by_coin, calm_list, a_random, b_mode,
                  a_fixed=None, coin_order=None, b_first=False, method="sample"):
    """Section 4 of the question, with switches that vary one choice at a time."""
    def pick(lst, k):
        if method == "sample":
            return rng.sample(lst, k)
        c = list(lst)
        rng.shuffle(c)
        return c[:k]

    def do_a():
        return pick(large_list, CARDS_LARGE) if a_random else list(a_fixed)

    def do_b(a_sel):
        if b_mode == "even":
            return pick(calm_list, CARDS_CALM)
        k = collections.Counter(m.split("-")[0] for m in a_sel)
        out = []
        for coin in coin_order:
            out.extend(pick(calm_by_coin[coin], k.get(coin, 0)))
        return out

    if b_first and b_mode == "even":
        b = do_b(None)
        a = do_a()
    else:
        a = do_a()
        b = do_b(a)
    return set(a), set(b)


def summary(diffs):
    return {"min": min(diffs), "median": statistics.median(diffs), "max": max(diffs),
            "seeds_identical": sum(1 for d in diffs if d == 0), "seeds": len(diffs)}


def main():
    started = now()
    ok = True
    out = {"facts": {}, "mechanics": {}, "scan": {}, "reviewer_only": {}}

    coins = [l.strip() for l in open(COINS, encoding="utf-8") if l.strip()]
    rows = list(csv.DictReader(open(MOMENTS, encoding="utf-8")))
    large = [r for r in rows if r["kind"] == "large"]
    calm = [r for r in rows if r["kind"] == "calm"]

    # ---- F1 ---------------------------------------------------------------
    f1 = len(large) > CARDS_LARGE and len(calm) > CARDS_CALM
    out["facts"]["F1_more_than_200_each"] = {"pass": f1, "large": len(large), "calm": len(calm)}
    print("F1 more than 200 large and 200 calm: %s (%d, %d)" % (f1, len(large), len(calm)))

    # ---- F2 ---------------------------------------------------------------
    per = collections.defaultdict(collections.Counter)
    for r in rows:
        per[r["symbol"]][r["kind"]] += 1
    f2 = all(per[c]["large"] == per[c]["calm"] for c in coins)
    zero = sum(1 for c in coins if per[c]["large"] == 0)
    out["facts"]["F2_calm_equals_large_per_coin"] = {"pass": f2, "coins": len(coins),
                                                     "coins_with_zero_moments": zero}
    print("F2 every coin calm == large: %s (coins %d, with zero moments %d)" % (f2, len(coins), zero))

    # ---- F3 ---------------------------------------------------------------
    keys = [(r["start_ms"], r["symbol"]) for r in rows]
    f3 = len(set(keys)) == len(keys)
    out["facts"]["F3_no_shared_hour_and_coin"] = {"pass": f3}
    print("F3 no two moments share start hour and coin: %s" % f3)

    # ---- F4 ---------------------------------------------------------------
    m06 = load_06()
    m06.KLINES_DIR = EXAM_KLINES
    mismatches = 0
    exact = {}
    for sym in sorted({r["symbol"] for r in rows}):
        bars = m06.load_hourly(sym)
        for r in rows:
            if r["symbol"] != sym:
                continue
            t0 = int(r["start_ms"])
            base = bars[t0 - HOUR_MS]["close"]
            end = bars[t0 + 23 * HOUR_MS]["close"]
            mv = end / base - 1.0
            if "%.4f" % (mv * 100.0) != r["move_24h_pct"]:
                mismatches += 1
            exact[r["moment_id"]] = (mv, math.log(end / base))
    f4a = mismatches == 0 and len(exact) == len(rows)
    simple_top = set(ids(sorted(large, key=lambda r: (-abs(exact[r["moment_id"]][0]),
                                                      int(r["start_ms"]), r["symbol"]))[:CARDS_LARGE]))
    log_top = set(ids(sorted(large, key=lambda r: (-abs(exact[r["moment_id"]][1]),
                                                   int(r["start_ms"]), r["symbol"]))[:CARDS_LARGE]))
    differ = len(simple_top - log_top)
    f4b = differ > 0
    out["facts"]["F4_measure"] = {"pass": f4a and f4b, "moments_recomputed": len(exact),
                                  "stored_value_mismatches": mismatches,
                                  "top200_simple_vs_log_differ": differ}
    print("F4 stored change == close(t0+23h)/close(t0-1h)-1 for every moment: %s (%d recomputed, %d mismatches)"
          % (f4a, len(exact), mismatches))
    print("F4 top-200 by |simple| vs |log| differ in %d of 200" % differ)

    sizes_full = [abs(exact[r["moment_id"]][0]) for r in large]
    out["reviewer_only"]["large_sizes_distinct"] = {"distinct": len(set(sizes_full)),
                                                    "of": len(sizes_full)}

    # ---- F5 ---------------------------------------------------------------
    tl = open(TACTICS, encoding="utf-8").read().split("\n")[21]
    m = re.search(r"Draw number:\*\*\s*`(\d+)`", tl)
    draw_no = int(m.group(1)) if m else None
    pool_seed = json.load(open(POOL_REPORT, encoding="utf-8")).get("seed")
    t04 = open(SCRIPT_04, encoding="utf-8").read()
    t06 = open(SCRIPT_06, encoding="utf-8").read()
    t27 = open(SCRIPT_27, encoding="utf-8").read()
    s04 = re.search(r"^SEED = (\d+)", t04, re.M)
    s06 = re.search(r"^SEED = (\d+)", t06, re.M)
    f5 = (draw_no is not None and pool_seed == draw_no
          and s04 and int(s04.group(1)) == draw_no and "rng = random.Random(SEED)" in t04
          and s06 and int(s06.group(1)) == draw_no
          and "rng = random.Random(m06.SEED)" in t27)
    out["facts"]["F5_draw_number_already_seeded"] = {
        "pass": bool(f5), "tactics_line_22_has_number": draw_no is not None,
        "pool_report_seed_equals_it": pool_seed == draw_no,
        "04_draw_seed_equals_it_and_seeds_random": bool(s04 and int(s04.group(1)) == draw_no
                                                        and "rng = random.Random(SEED)" in t04),
        "exam_27_seeds_random_with_06_seed_equal_to_it": bool(s06 and int(s06.group(1)) == draw_no
                                                              and "rng = random.Random(m06.SEED)" in t27)}
    print("F5 draw number already seeded the coin draw and the pool's calm choice: %s" % bool(f5))
    ok = ok and f1 and f2 and f3 and f4a and f4b and bool(f5)

    # ---- mechanics (seeds 1..1000, draw number excluded) --------------------
    assert draw_no not in MECH_SEEDS
    L_hs = ids(ordered(large, by_hour_then_symbol))
    L_sh = ids(ordered(large, by_symbol_then_hour))
    C_hs = ids(ordered(calm, by_hour_then_symbol))
    C_sh = ids(ordered(calm, by_symbol_then_hour))
    calm_by_coin = {c: ids(ordered([r for r in calm if r["symbol"] == c], by_hour_then_symbol))
                    for c in coins}
    asc = sorted(coins)
    desc = list(reversed(asc))
    largest = sorted(simple_top)
    cm_feasible = True
    d_order, d_method, d_ab, d_coin_even_a, d_coin_largest = [], [], [], [], []
    d_order_calm, d_method_calm = [], []
    k0_ok = True
    for s in MECH_SEEDS:
        base_a, base_b_even = draw_section4(random.Random(s), L_hs, calm_by_coin, C_hs, True, "even")
        alt_a, _ = draw_section4(random.Random(s), L_sh, calm_by_coin, C_hs, True, "even")
        d_order.append(len(base_a - alt_a))
        _, alt_b = draw_section4(random.Random(s), L_hs, calm_by_coin, C_sh, False, "even",
                                 a_fixed=largest)
        _, base_b_after_largest = draw_section4(random.Random(s), L_hs, calm_by_coin, C_hs, False,
                                                "even", a_fixed=largest)
        d_order_calm.append(len(base_b_after_largest - alt_b))
        sh_a, _ = draw_section4(random.Random(s), L_hs, calm_by_coin, C_hs, True, "even", method="shuffle")
        d_method.append(len(base_a - sh_a))
        _, sh_b = draw_section4(random.Random(s), L_hs, calm_by_coin, C_hs, False, "even",
                                a_fixed=largest, method="shuffle")
        d_method_calm.append(len(base_b_after_largest - sh_b))
        bf_a, _ = draw_section4(random.Random(s), L_hs, calm_by_coin, C_hs, True, "even", b_first=True)
        d_ab.append(len(base_a - bf_a))
        a1, b_asc = draw_section4(random.Random(s), L_hs, calm_by_coin, C_hs, True, "coin", coin_order=asc)
        _, b_desc = draw_section4(random.Random(s), L_hs, calm_by_coin, C_hs, True, "coin", coin_order=desc)
        d_coin_even_a.append(len(b_asc - b_desc))
        k = collections.Counter(x.split("-")[0] for x in a1)
        if any(k[c] > len(calm_by_coin[c]) for c in coins) or len(b_asc) != CARDS_CALM:
            cm_feasible = False
        _, bl_asc = draw_section4(random.Random(s), L_hs, calm_by_coin, C_hs, False, "coin",
                                  a_fixed=largest, coin_order=asc)
        _, bl_desc = draw_section4(random.Random(s), L_hs, calm_by_coin, C_hs, False, "coin",
                                   a_fixed=largest, coin_order=desc)
        d_coin_largest.append(len(bl_asc - bl_desc))
        r = random.Random(s)
        st = r.getstate()
        r.sample(C_hs, 0)
        if r.getstate() != st:
            k0_ok = False
    kl = collections.Counter(x.split("-")[0] for x in largest)
    cm_largest_ok = all(kl[c] <= len(calm_by_coin[c]) for c in coins)
    out["mechanics"] = {
        "list_order_hour_symbol_vs_symbol_hour_part_a": summary(d_order),
        "sample_vs_shuffle_take_first_part_a": summary(d_method),
        "list_order_hour_symbol_vs_symbol_hour_part_b_even_after_largest": summary(d_order_calm),
        "sample_vs_shuffle_take_first_part_b_even_after_largest": summary(d_method_calm),
        "a_first_vs_b_first_part_a": summary(d_ab),
        "coin_order_asc_vs_desc_coin_matched_after_even_chance": summary(d_coin_even_a),
        "coin_order_asc_vs_desc_coin_matched_after_largest": summary(d_coin_largest),
        "sample_k0_leaves_state_unchanged": k0_ok,
        "coin_matched_feasible_every_seed_after_even_chance": cm_feasible,
        "coin_matched_feasible_after_largest": cm_largest_ok,
    }
    for k_, v in out["mechanics"].items():
        print("M %s: %s" % (k_, v))
    mech_ok = (all(out["mechanics"][k_]["seeds_identical"] == 0 for k_ in out["mechanics"]
                   if isinstance(out["mechanics"][k_], dict))
               and k0_ok and cm_feasible and cm_largest_ok)
    print("M every section-4 choice changes the drawn moments in every seed: %s" % mech_ok)
    ok = ok and mech_ok

    # ---- scan ---------------------------------------------------------------
    names = json.load(open(COIN_NAMES, encoding="utf-8"))
    tokens = set()
    for sym in coins:
        tokens.add(sym)
        tokens.add(sym[:-len(QUOTE_SUFFIX)] if sym.endswith(QUOTE_SUFFIX) else sym)
    for v in names.values():
        for f in ("base_ticker", "name", "symbol"):
            if isinstance(v.get(f), str) and v.get(f):
                tokens.add(v[f])
        for h in v.get("exact_symbol_hits") or []:
            for f in ("id", "name"):
                if isinstance(h.get(f), str) and h.get(f):
                    tokens.add(h[f])
    words = set()
    for t in tokens:
        for w in re.split(r"[^A-Za-z0-9]+", t):
            if len(w) >= NAME_WORD_MIN:
                words.add(w)
    all_tokens = sorted(tokens | words, key=lambda s: s.lower())
    text = open(QUESTION, encoding="utf-8").read()
    lines = text.split("\n")
    matches = []
    for tok in all_tokens:
        rx = re.compile(r"(?<![A-Za-z0-9])%s(?![A-Za-z0-9])" % re.escape(tok), re.IGNORECASE)
        for n, ln in enumerate(lines, 1):
            for mm in rx.finditer(ln):
                matches.append({"line": n, "kind": "coin-name-token", "matched": mm.group(0)})
    for n, ln in enumerate(lines, 1):
        for p in PATTERNS:
            for mm in re.finditer(p, ln):
                matches.append({"line": n, "kind": "pattern " + p, "matched": mm.group(0)})
        for w in re.findall(r"[A-Za-z]+", ln):
            if w.lower() in MONTHS or w.lower() in WEEKDAYS:
                matches.append({"line": n, "kind": "month-or-weekday", "matched": w})
    digits = collections.defaultdict(list)
    for n, ln in enumerate(lines, 1):
        for mm in re.finditer(r"\d+", ln):
            digits[mm.group(0)].append(n)
    out["scan"] = {"tokens_checked": len(all_tokens), "matches": matches,
                   "digit_runs": {k_: digits[k_] for k_ in sorted(digits, key=lambda s: (len(s), s))}}
    print("scan: %d tokens checked, %d matches" % (len(all_tokens), len(matches)))
    for mm in matches:
        print("  MATCH line %d %s: %s" % (mm["line"], mm["kind"], mm["matched"]))
    print("digit runs:", json.dumps(out["scan"]["digit_runs"]))
    ok = ok and not matches

    # ---- record (RULES 29/30) ----------------------------------------------
    inputs = {os.path.relpath(p, ROOT): sha(p) for p in
              (QUESTION, TACTICS, COINS, MOMENTS, POOL_REPORT, COIN_NAMES,
               SCRIPT_06, SCRIPT_04, SCRIPT_27, os.path.abspath(__file__))}
    run = hashlib.sha256(json.dumps(inputs, sort_keys=True).encode()).hexdigest()
    out["inputs_sha256"] = inputs
    out["run_number"] = run
    out["result"] = "PASS" if ok else "FAIL"
    body = json.dumps(out, indent=1, sort_keys=True) + "\n"
    rec = os.path.join(OUT_DIR, "JQ-DRAW-v2-check-%s.json" % run[:16])
    if os.path.exists(rec):
        if open(rec, encoding="utf-8").read() != body:
            print("STOP: %s exists with different content; nothing overwritten" % rec)
            return 2
    else:
        with open(rec, "w", encoding="utf-8") as fh:
            fh.write(body)
    with open(RUNS_LOG, "a", encoding="utf-8") as fh:
        fh.write(json.dumps({"run_number": run, "started_utc": started, "finished_utc": now(),
                             "result": out["result"],
                             "question_sha256": inputs["open-questions/JQ-DRAW.md"]},
                            sort_keys=True) + "\n")
    print("record %s" % os.path.relpath(rec, ROOT))
    print("sha256 %s  open-questions/JQ-DRAW.md" % inputs["open-questions/JQ-DRAW.md"])
    print("RESULT: %s" % out["result"])
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
