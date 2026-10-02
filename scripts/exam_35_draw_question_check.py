#!/usr/bin/env python3
"""
exam_35_draw_question_check.py -- checks the juror question JQ-DRAW against the
                                  exam moment pool and against the wall.

What it does
------------
1. Re-measures, from the exam moment pool, the two facts JQ-DRAW section 1
   states, plus the two facts its reviewer section and section 4 rely on:
     F1  each kind holds more than the TACTICS 6 card count (200 / 200);
     F2  every exam coin has exactly as many calm as large-movement moments;
     F3  no two large-movement moments have the same absolute 24-hour size
         (checked on the 4-decimal values in moments.csv; distinct at 4
         decimals implies distinct at full precision);
     F4  no two moments share both start hour and coin.
2. Scans open-questions/JQ-DRAW.md for every exam coin's symbol and base
   name (whole word), for date and clock patterns, for month names, and for
   decimal numbers. A name in its listed (upper) case, a capitalised month
   name, a date/clock pattern or a decimal fails the check. A name matched only
   in another case, or a lower-case month word, is listed as REVIEW for a human
   reader and does not fail it (some base names and month names are ordinary
   English words). Lists every digit run with its line number.
3. Prints SHA-256 of the question file and of the inputs.

It chooses no moment and runs no draw. It writes no file. Coin names are read
at run time and never printed: hits are reported by coin line number.

Input   : exam/draw/exam-coins.txt, exam/moments/moments.csv,
          open-questions/JQ-DRAW.md
Output  : console only; exit status 1 if any fact fails or any name / date /
          decimal is found in the question file.
Rules   : RULES 9 and TACTICS 6 (names and dates hidden), RULES 19 (only
          measured numbers), RULES 33 standards given in the instruction of
          2026-10-02 00:03 UTC.
Constants: CARDS_LARGE = CARDS_CALM = 200 are TACTICS.md §6 lines 99-100.
Randomness: none.
Usage   : python3 -B scripts/exam_35_draw_question_check.py
"""

import collections
import csv
import hashlib
import os
import re
import sys

sys.dont_write_bytecode = True

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COINS = os.path.join(ROOT, "exam", "draw", "exam-coins.txt")
MOMENTS = os.path.join(ROOT, "exam", "moments", "moments.csv")
QUESTION = os.path.join(ROOT, "open-questions", "JQ-DRAW.md")

CARDS_LARGE = 200   # TACTICS.md §6 line 99
CARDS_CALM = 200    # TACTICS.md §6 line 100
QUOTE_SUFFIX = "USDT"

MONTHS = ("january february march april may june july august september "
          "october november december jan feb mar apr jun jul aug sep sept oct "
          "nov dec").split()


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    ok = True
    coins = [l.strip() for l in open(COINS, encoding="utf-8") if l.strip()]
    line_of = {c: i + 1 for i, c in enumerate(coins)}
    rows = list(csv.DictReader(open(MOMENTS, encoding="utf-8")))

    kinds = collections.Counter(r["kind"] for r in rows)
    f1 = kinds["large"] > CARDS_LARGE and kinds["calm"] > CARDS_CALM
    print("F1 more than %d large and more than %d calm: %s (large %d, calm %d)"
          % (CARDS_LARGE, CARDS_CALM, f1, kinds["large"], kinds["calm"]))

    per = collections.defaultdict(collections.Counter)
    for r in rows:
        per[line_of[r["symbol"]]][r["kind"]] += 1
    f2 = all(c["large"] == c["calm"] for c in per.values())
    print("F2 every coin calm == large: %s (coins with moments: %d of %d)"
          % (f2, len(per), len(coins)))

    sizes = [abs(float(r["move_24h_pct"])) for r in rows if r["kind"] == "large"]
    f3 = len(set(sizes)) == len(sizes)
    print("F3 no two large moments share a size: %s (%d distinct of %d)"
          % (f3, len(set(sizes)), len(sizes)))

    keys = [(r["start_hour_utc"], line_of[r["symbol"]]) for r in rows]
    f4 = len(set(keys)) == len(keys)
    print("F4 no two moments share start hour and coin: %s" % f4)
    ok = ok and f1 and f2 and f3 and f4

    text = open(QUESTION, encoding="utf-8").read()
    lines = text.split("\n")
    hits = []      # fail the check
    review = []    # listed for a human reader; do not fail the check
    for sym in coins:
        base = sym[:-len(QUOTE_SUFFIX)] if sym.endswith(QUOTE_SUFFIX) else sym
        for token in {sym, base}:
            form = "symbol" if token == sym else "base"
            exact = re.compile(r"(?<![A-Za-z0-9])%s(?![A-Za-z0-9])" % re.escape(token))
            loose = re.compile(r"(?<![A-Za-z0-9])%s(?![A-Za-z0-9])" % re.escape(token),
                               re.IGNORECASE)
            for n, ln in enumerate(lines, 1):
                if exact.search(ln):
                    hits.append("coin line %d (%s form, exact case) at file line %d"
                                % (line_of[sym], form, n))
                elif loose.search(ln):
                    words = sorted(set(m.group(0) for m in loose.finditer(ln)))
                    review.append("coin line %d (%s form, other case: %s) at file line %d"
                                  % (line_of[sym], form, "/".join(words), n))
    date_pats = [r"\d{4}-\d{2}-\d{2}", r"\d{8}", r"\b\d{1,2}:\d{2}\b",
                 r"\d{4}-\d{2}", r"\b\d+\.\d+\b"]
    for n, ln in enumerate(lines, 1):
        for p in date_pats:
            for m in re.finditer(p, ln):
                hits.append("pattern %s '%s' at file line %d" % (p, m.group(0), n))
        for w in re.findall(r"[A-Za-z]+", ln):
            if w.lower() in MONTHS:
                if w[0].isupper():
                    hits.append("month word '%s' at file line %d" % (w, n))
                else:
                    review.append("lower-case month word '%s' at file line %d" % (w, n))
    print("name / date / decimal hits in question file: %d" % len(hits))
    for h in hits:
        print("  HIT", h)
    print("other-case / lower-case matches for a human reader (do not fail): %d"
          % len(review))
    for r in review:
        print("  REVIEW", r)
    ok = ok and not hits

    digits = collections.defaultdict(list)
    for n, ln in enumerate(lines, 1):
        for m in re.finditer(r"\d+", ln):
            digits[m.group(0)].append(n)
    print("every digit run in the question file (value: file lines):")
    for v in sorted(digits, key=lambda s: (len(s), s)):
        print("  %s: %s" % (v, ",".join(str(x) for x in digits[v])))

    print("sha256 %s  open-questions/JQ-DRAW.md" % sha(QUESTION))
    print("sha256 %s  exam/moments/moments.csv" % sha(MOMENTS))
    print("sha256 %s  exam/draw/exam-coins.txt" % sha(COINS))
    print("RESULT: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
