#!/usr/bin/env python3
"""Review 8, probe p2 -- every quotation in the eighth-fix
JQ-R04-CONTENT-d juror file, checked (a) present in the juror file and
(b) present in the cited source within the cited lines.

Normalisation (both sides alike): markdown bold `**` removed, runs of
whitespace collapsed to one space, an ellipsis "…" splits a quotation into
parts that must each be found, in order. Nothing else is altered.
Input: the juror file, RULES.md, TACTICS.md, the GATE juror file, three
verdict files. Output: stdout (caller redirects to p2_quotes.out).
No randomness; no constants of judgement.
"""
import os
import re
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = HERE.rsplit(os.sep + "exam-prep" + os.sep, 1)[0]
assert os.path.isfile(os.path.join(REPO, "RULES.md"))

D = "exam-prep/eighth-fix/juror-questions/JQ-R04-CONTENT-d.md"
GATE = "exam-prep/third-fix/juror-questions/JQ-R04-GATE.md"
VG = "decisions/2026-10-01-jq-r04-gate/verdict.md"
VDC = "decisions/2026-10-01-jq-r04-date-content/verdict.md"
VC = "decisions/2026-10-01-jq-r04-carries/verdict.md"

# (quotation, source, first line, last line) -- transcribed from the d file
Q = [
    ("In the exam the coin name and the date are hidden.", "RULES.md", 41, 41),
    ("The chance line is not invented. The answers are shuffled 1,000 times, "
     "and the real result must fall inside the best 1%.", "RULES.md", 51, 52),
    ("A juror decides procedure and definition only: never a trading rule, "
     "never a threshold or score, and never a change to a rule in this file.",
     "RULES.md", 119, 121),
    ("the 24 hours before the start, hour by hour; plus a one-line summary of "
     "the previous 7 days.", "TACTICS.md", 50, 51),
    ("price, volume, trade count, taker buy/sell pressure", "TACTICS.md", 55, 64),
    ("open interest, long/short ratios (5-minute archive)", "TACTICS.md", 55, 64),
    ("funding rate, payment interval and its changes", "TACTICS.md", 55, 64),
    ("bitcoin and ethereum, over the same hours", "TACTICS.md", 55, 64),
    ("number of people viewing the page on Wikipedia (daily)", "TACTICS.md",
     55, 64),
    ("the coin name", "TACTICS.md", 101, 107),
    ("the date and time", "TACTICS.md", 101, 107),
    ("the price itself (converted to a number starting from 100)",
     "TACTICS.md", 101, 107),
    ("the coin name inside announcements", "TACTICS.md", 101, 107),
    ("the Wikipedia number itself (given as a ratio to the coin's own "
     "average)", "TACTICS.md", 101, 107),
    ("the date in the release calendar", "TACTICS.md", 101, 107),
    ("Then the canteen book freezes", "TACTICS.md", 94, 94),
    ("If `ALL-removable` beats its chance line on the exam cards, the cards "
     "are not blind and the gate has failed.", GATE, 1, 10 ** 6),
    ("The gate fails if either the nearest-neighbour attack or the pair AUC "
     "attack beats its own RULES 12 chance line on the exam cards.", VG, 72, 72),
    ("every feature in the audit's current list, minus the families that "
     "must stay on the card because a frozen canteen rule or TACTICS requires "
     "them", GATE, 1, 10 ** 6),
    ("Do RULES 9 and TACTICS 6 require removing columns that identify clock "
     "hours? No.", VDC, 39, 47),
    ('Does hiding "the date in the release calendar" cover release *names* '
     'that identify the day? No.', VDC, 39, 47),
    ('Does hiding "the date and time" cover clock hour revealed by an offset '
     'plus outside knowledge of release times? No.', VDC, 39, 47),
    ("May the blinding remove a TACTICS 3 field when nothing frozen reads it "
     "and it carries a measured coin signature? Yes — when both conditions "
     "hold: nothing the frozen canteen book reads it, and in the rendering the "
     "exam card would otherwise carry, it carries a measured coin signature as "
     "JQ-R04-CARRIES defines one.", VDC, 39, 47),
    ("b1 (actual price rebased to 100, fixed decimals): Permitted.", VDC, 39, 47),
    ("b2 (computed from printed chg%, starting from 100): Permitted.", VDC,
     39, 47),
    ("b3 (no price column; chg% stays): Permitted only if and as far as "
     "CONTENT-a yes.", VDC, 39, 47),
    ("May a ranked column come from pre-rounding values, ordering hours the "
     "raw card prints as equal? No.", VDC, 39, 47),
    ("When the test in part b identifies a column's feature sets, the column "
     "carries a measured coin signature when either the pair AUC attack or "
     "the nearest-neighbour attack beats its own RULES 12 chance line on that "
     "set.", VC, 107, 107),
    ("The test reads every feature computed from the column's own printed "
     "values and from nothing else, tested together as one set.", VC, 109, 109),
    ("that must stay on the card because … TACTICS requires them", GATE, 1,
     10 ** 6),
]


def norm(s):
    return re.sub(r"\s+", " ", s.replace("**", "")).strip()


def found(q, text):
    pos = 0
    for part in [p.strip() for p in norm(q).split("…")]:
        i = text.find(part, pos)
        if i < 0:
            return False
        pos = i + len(part)
    return True


dtext = norm(open(os.path.join(REPO, D), encoding="utf-8").read())
fails = 0
for q, src, lo, hi in Q:
    lines = open(os.path.join(REPO, src), encoding="utf-8").read().split("\n")
    # a block-quote marker at the start of a source line is not text
    seg = norm("\n".join(re.sub(r"^> ?", "", x) for x in lines[lo - 1:hi]))
    a = found(q, dtext)
    b = found(q, seg)
    ok = a and b
    fails += 0 if ok else 1
    print("%s  in-d-file=%s in-source=%s  %s %s  %s"
          % ("ok  " if ok else "FAIL", a, b, src,
             ("%d-%d" % (lo, hi)) if hi < 10 ** 6 else "(whole file)",
             q[:60]))
print("\n%d quotations, %d failed" % (len(Q), fails))
