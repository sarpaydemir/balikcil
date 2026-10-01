#!/usr/bin/env python3
"""p2_quotes.py — review-7 probe: is every passage that
`exam-prep/USER-QUESTIONS.md` quotes found (a) in the cited lines of the cited
file and (b) in USER-QUESTIONS.md itself?

Input   RULES.md, TACTICS.md, decisions/2026-10-01-jq-r04-gate/verdict.md,
        exam-prep/third-fix/juror-questions/JQ-R04-GATE.md,
        exam-prep/USER-QUESTIONS.md. Nothing else is opened.
Output  stdout only (redirected by the reviewer to p2_quotes.out).
Rule    RULES 34 discipline (a citation must point where it says). No
        randomness, no threshold.
Run     PYTHONDONTWRITEBYTECODE=1 python3 -B exam-prep/review-7/probes/p2_quotes.py
"""
import os
import re
import sys

sys.dont_write_bytecode = True
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
UQ = "exam-prep/USER-QUESTIONS.md"

# (cited file, first line, last line, passage) — transcribed from U-1 by the
# reviewer; each passage is what U-1 puts inside quotation marks.
QUOTES = [
    ("RULES.md", 41, 41, "In the exam the coin name and the date are hidden."),
    ("TACTICS.md", 101, 107, "the coin name"),
    ("TACTICS.md", 101, 107, "the date and time"),
    ("TACTICS.md", 101, 107,
     "the price itself (converted to a number starting from 100)"),
    ("TACTICS.md", 101, 107, "the coin name inside announcements"),
    ("TACTICS.md", 101, 107,
     "the Wikipedia number itself (given as a ratio to the coin's own average)"),
    ("TACTICS.md", 101, 107, "the date in the release calendar"),
    ("TACTICS.md", 55, 62,
     "price, volume, trade count, taker buy/sell pressure"),
    ("TACTICS.md", 55, 62, "bitcoin and ethereum, over the same hours"),
    ("RULES.md", 51, 52,
     "The chance line is not invented. The answers are shuffled 1,000 times, "
     "and the real result must fall inside the best 1%."),
    ("decisions/2026-10-01-jq-r04-gate/verdict.md", 72, 72,
     "The gate fails if either the nearest-neighbour attack or the pair AUC "
     "attack beats its own RULES 12 chance line on the exam cards."),
    ("exam-prep/third-fix/juror-questions/JQ-R04-GATE.md", 64, 66,
     "every feature in the audit's current list, minus the families that "
     "must stay on the card because a frozen canteen rule or TACTICS "
     "requires them"),
    ("TACTICS.md", 94, 94, "Then the canteen book freezes"),
    ("RULES.md", 3, 4,
     "These rules do not change. If one must change, the user is asked "
     "first, and then it is written into `LEDGER.md`."),
    ("RULES.md", 119, 121,
     "A juror decides procedure and definition only: never a trading rule, "
     "never a threshold or score, and never a change to a rule in this file."),
    ("RULES.md", 34, 35,
     "The rule is written first, the result is opened second. A rule is not "
     "changed after looking at a result."),
]

# Section pointers U-1 makes without quoting (file, first, last, a heading or
# phrase that must be inside those lines for the pointer to be right).
POINTERS = [
    ("TACTICS.md", 55, 62, "What is on the card"),
    ("TACTICS.md", 101, 107, "the coin name"),
]


def norm(s):
    s = s.replace("**", "").replace("`", "")
    s = re.sub(r"^\s*[-*]\s+", " ", s, flags=re.M)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def read(rel):
    if os.path.basename(rel).startswith("exam_"):
        sys.exit("refusing to open " + rel)
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def main():
    uq = norm(read(UQ))
    n = bad = 0
    for rel, a, b, q in QUOTES + POINTERS:
        lines = read(rel).split("\n")[a - 1:b]
        src = norm("\n".join(lines))
        in_src = norm(q) in src
        in_uq = norm(q) in uq or (rel, a, b, q) in POINTERS
        n += 1
        ok = in_src and in_uq
        bad += 0 if ok else 1
        print("%s %s:%d-%d in-source=%s in-U-1=%s :: %s" % (
            "ok  " if ok else "FAIL", rel, a, b, in_src, in_uq, q[:70]))
    print("%d checks, %d failed" % (n, bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
