#!/usr/bin/env python3
"""
p2_quotes.py -- review 6 probe. Checks that every passage the four
sixth-fix juror files (JQ-R04-CARRIES, JQ-R04-CONTENT-d, JQ-R04-DATE,
JQ-R04-CONTENT) quote from RULES.md, TACTICS.md, the canteen book, the
ratified GATE verdict, the GATE juror file and the audit script is found in
the lines they cite. Each quote is also checked to occur in the juror file
that quotes it. A quote containing an ellipsis is split at it and each piece
is checked. Comparison is on whitespace-collapsed text with '**' removed.

Input : RULES.md, TACTICS.md, canteen/2026-09-19-sofia.md,
        decisions/2026-10-01-jq-r04-gate/verdict.md,
        exam-prep/third-fix/juror-questions/JQ-R04-GATE.md,
        scripts/29_identity_audit_exact.py (read as text only),
        exam-prep/sixth-fix/juror-questions/*.md
Output: stdout only (captured by the reviewer into p2_quotes.out).
Rules : RULES 34 (citations), RULES 19. No threshold, no randomness.
Run   : PYTHONDONTWRITEBYTECODE=1 python3 -B exam-prep/review-6/probes/p2_quotes.py
"""
import os
import re
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
J = "exam-prep/sixth-fix/juror-questions/"
CAR, D, DATE, CONT = (J + "JQ-R04-CARRIES.md", J + "JQ-R04-CONTENT-d.md",
                      J + "JQ-R04-DATE.md", J + "JQ-R04-CONTENT.md")
R, T, C = "RULES.md", "TACTICS.md", "canteen/2026-09-19-sofia.md"
V = "decisions/2026-10-01-jq-r04-gate/verdict.md"
G = "exam-prep/third-fix/juror-questions/JQ-R04-GATE.md"
A = "scripts/29_identity_audit_exact.py"

# (juror files that quote it, source, first line, last line, quote)
Q = [
    ((CAR, D, DATE, CONT), R, 41, 41,
     "In the exam the coin name and the date are hidden."),
    ((CAR, D), R, 51, 52, "The chance line is not invented. The answers are "
     "shuffled 1,000 times, and the real result must fall inside the best 1%."),
    ((CAR,), R, 119, 121, "A juror decides procedure and definition only: "
     "never a trading rule, never a threshold or score, and never a change to "
     "a rule in this file."),
    ((D,), R, 34, 35, "The rule is written first, the result is opened "
     "second. A rule is not changed after looking at a result."),
    ((CONT,), R, 34, 35, "A rule is not changed after looking at a result."),
    ((DATE,), R, 43, 44, "An agent sitting the exam cannot use tools and "
     "cannot read files."),
    ((CAR, D), T, 50, 51, "the 24 hours before the start, hour by hour; plus "
     "a one-line summary of the previous 7 days."),
    ((CAR, CONT), T, 56, 56, "price, volume, trade count, taker buy/sell "
     "pressure"),
    ((D, DATE), T, 55, 62, "price, volume, trade count, taker buy/sell "
     "pressure"),
    ((D,), T, 55, 62, "open interest, long/short ratios (5-minute archive)"),
    ((D,), T, 55, 62, "funding rate, payment interval and its changes"),
    ((D,), T, 55, 62, "order book depth"),
    ((D, DATE), T, 55, 62, "bitcoin and ethereum, over the same hours"),
    ((D, DATE), T, 55, 62, "US release calendar (inflation, employment, rate "
     "decision)"),
    ((CONT,), T, 57, 57, "open interest, long/short ratios (5-minute archive)"),
    ((CONT,), T, 59, 59, "order book depth"),
    ((CONT,), T, 71, 71, "Numbers are rounded and the card is kept short."),
    ((CAR,), T, 101, 103, "the coin name"),
    ((CAR,), T, 101, 103, "the date and time"),
    ((CONT,), T, 101, 104, "the price itself (converted to a number starting "
     "from 100)"),
    ((D, DATE), T, 101, 107, "the coin name inside announcements"),
    ((D, DATE), T, 101, 107, "the Wikipedia number itself (given as a ratio "
     "to the coin's own average)"),
    ((D, DATE), T, 101, 107, "the date in the release calendar"),
    ((DATE,), T, 107, 107, "the date in the release calendar"),
    ((DATE,), T, 103, 103, "the date and time"),
    ((D,), V, 72, 72, "The gate fails if either the nearest-neighbour attack "
     "or the pair AUC attack beats its own RULES 12 chance line on the exam "
     "cards."),
    ((D,), G, 55, 57, "If `ALL-removable` beats its chance line on the exam "
     "cards, the cards are not blind and the gate has failed."),
    ((D,), G, 64, 66, "`ALL-removable` is every feature in the audit's "
     "current list, minus the families that must stay on the card because a "
     "frozen canteen rule or TACTICS requires them."),
    ((D,), A, 431, 431, "the frozen book's S-1 reads `chg%` at 5.00% absolute"),
    ((D,), A, 432, 432, "B-5, U-2 and U-3 are answered from it"),
    ((D,), A, 433, 433, "TACTICS 3 puts a previous-7-day summary on the card"),
    ((D,), A, 434, 434, "it reads the same unchanged `chg%` column"),
    ((CONT,), C, 114, 120, "at least one row whose hourly close-to-close "
     "change is |5.00%| or more. Read it from the `chg%` column. If an exam "
     "card does not print `chg%`, compute it from the `close` column as "
     "close(h)/close(h-1) - 1"),
    ((CONT,), C, 221, 225, "Rule no: B-2 · the `taker L/S` column may not be "
     "read / Trigger : always — the column is excluded from every score. … "
     "Exit : n/a. It lifts only when somebody checks the column against the "
     "5-minute taker archive and states a trade-count floor."),
    ((CONT,), C, 245, 246, "any hour of the card prints `open int` = 0 "
     "between live neighbours. On such a card no open-interest statistic may "
     "be computed."),
    ((CONT,), C, 268, 270, "the `depth -1%` or `depth +1%` column repeats one "
     "identical value for three or more consecutive hours. On such a card and "
     "such hours no depth statistic may be computed."),
    ((CONT,), C, 667, 671, "The trade-count floor under `taker L/S`. No "
     "watcher names a number. … How determined: by Mateo/Nadia against the "
     "5-minute taker archive, as a data-cleaning decision, not a trading "
     "decision. Until then B-2 excludes the column outright, which needs no "
     "number."),
]


def norm(s):
    return re.sub(r"\s+", " ", s.replace("**", "")).strip()


def lines(rel, a, b):
    with open(os.path.join(REPO, rel), encoding="utf-8") as fh:
        ls = fh.read().split("\n")
    # a markdown block-quote marker at the start of a line is not text
    return norm(" ".join(re.sub(r"^>\s?", "", x) for x in ls[a - 1:b]))


def whole(rel):
    with open(os.path.join(REPO, rel), encoding="utf-8") as fh:
        return norm(fh.read())


bad = 0
n = 0
for files, src, a, b, q in Q:
    pieces = [norm(x) for x in re.split(r"…", q) if norm(x)]
    # a "/" in the canteen B-2 quote stands for a line break in the book
    src_txt = lines(src, a, b)
    for piece in pieces:
        alts = [piece] + ([piece.replace(" / ", " ")] if " / " in piece else [])
        n += 1
        ok_src = any(x in src_txt for x in alts)
        print("%-4s src %s %d-%d: %s" % ("ok" if ok_src else "FAIL", src, a, b,
                                         piece[:70]))
        bad += not ok_src
        for f in files:
            n += 1
            ok_f = piece in whole(f)
            print("%-4s  in %s" % ("ok" if ok_f else "FAIL", f.split("/")[-1]))
            bad += not ok_f
print("checks %d, failed %d" % (n, bad))
sys.exit(1 if bad else 0)
