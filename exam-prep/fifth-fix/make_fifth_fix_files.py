#!/usr/bin/env python3
"""
make_fifth_fix_files.py -- builds the fifth-fix juror files from the
fourth-fix juror files, by exact, asserted text edits.

What it does : reads the four files in exam-prep/fourth-fix/juror-questions/,
               applies the edits listed below (each one asserts that the old
               text occurs exactly once), and writes the result to
               exam-prep/fifth-fix/juror-questions/ -- or, with --out DIR, to
               DIR, so that a reviewer can rebuild and compare.
Input        : exam-prep/fourth-fix/juror-questions/{JQ-N1,JQ-CANTEEN-8,
               JQ-R04-DATE,JQ-R04-CONTENT}.md  (never modified)
Output       : the same four names under the output folder.
Rule         : acts on exam-prep/REVIEW-4.md §2 and §4 (RULES 32-33); every
               edit not listed by REVIEW-4 is named in FIFTH-FIX.md §2.
               No number is introduced except the line numbers of passages
               quoted for the first time (checked by
               scripts/32_juror_file_check_fifth.py).
No randomness, no threshold, no clock. Run with PYTHONDONTWRITEBYTECODE=1.
"""
import argparse
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, "exam-prep", "fourth-fix", "juror-questions")
DST = os.path.join(ROOT, "exam-prep", "fifth-fix", "juror-questions")
F4 = "exam-prep/fourth-fix/juror-questions/"
F5 = "exam-prep/fifth-fix/juror-questions/"
DATE_LINE = "2026-10-01"   # the run's date, read from the system clock


class Doc:
    def __init__(self, text):
        self.s = text

    def rep(self, old, new):
        n = self.s.count(old)
        if n != 1:
            sys.exit("STOP: expected exactly one occurrence, found %d of:\n%s"
                     % (n, old[:200]))
        self.s = self.s.replace(old, new)

    def path(self, old, new, expect):
        n = self.s.count(old)
        if n != expect:
            sys.exit("STOP: path %s occurs %d times, expected %d"
                     % (old, n, expect))
        self.s = self.s.replace(old, new)


def jq_n1(d):
    lines = d.s.split("\n")
    a = lines.index("What the two ways do to the 1% boundary, measured with "
                    "synthetic coin-flip")
    b = lines.index("  measurement was made.")
    if not (b > a and lines[b + 1] == "" and lines[b + 2] == "---"):
        sys.exit("STOP: JQ-N1 part 4 block boundaries not as expected")
    del lines[a:b + 2]
    d.s = "\n".join(lines)
    d.rep("    start hour, ties by card number — that is the convention the "
          "calibration\n    below used; it is not a ruling).",
          "    start hour, ties by card number).")
    d.rep("That RULES 13 is clear and needs no juror. The measured spread (289 "
          "events\nagainst 58 from the same 306 cards; across the "
          "configurations, answer types\nand the two ways of part 4, the 1% "
          "boundary ranges from 0.5458 to 0.6613 in\nthe full table of the "
          "source file named above) is the reason it was referred: RULES 33 "
          "calls \"a choice that changes the\nnumbers\" an open question.",
          "That RULES 13 is clear and needs no juror. The measured spread (289 "
          "events\nagainst 58 from the same 306 cards) is the reason it was "
          "referred: RULES 33\ncalls \"a choice that changes the numbers\" an "
          "open question.")
    d.path(F4 + "JQ-CANTEEN-8.md", F5 + "JQ-CANTEEN-8.md", 2)
    d.rep("unchanged.\nThis file re-issues, and replaces for juror use,",
          "unchanged.\n"
          "Corrected by: Mateo · fifth-fix run · %s (system clock) — part 4's\n"
          "table of 1%% boundaries and the block on random variation are "
          "removed, with\n"
          "4a's reference to the convention they used; they are not needed to "
          "answer\n"
          "part 4 (fourth review). The closing paragraph no longer quotes\n"
          "figures from that table. No question, option or count was changed.\n"
          "This file re-issues, and replaces for juror use," % DATE_LINE)


def jq_canteen8(d):
    d.rep("  but says **nothing** about calm-to-calm.\"\n"
          "- The script that drew the moments, `scripts/06_find_moments.py` "
          "lines\n"
          "  63–65: \"TACTICS 2 puts no minimum distance between two *calm* "
          "moments. None\n"
          "  is imposed here.\"\n",
          "  but says **nothing** about calm-to-calm.\"\n")
    d.path(F4 + "JQ-N1.md", F5 + "JQ-N1.md", 2)
    old = ("the options, the counts and the stakes are unchanged; JQ-N1 has a "
           "new place.\n")
    d.rep(old, old +
          "Corrected by: Mateo · fifth-fix run · %s (system clock) — one\n"
          "quotation of a script comment is removed from the rule texts; it is "
          "not\n"
          "needed to answer (fourth review). Nothing else changed; JQ-N1\n"
          "has a new place.\n" % DATE_LINE)


def jq_date(d):
    d.rep("card in time; that has not been measured.\n\n"
          "The first run removed these columns from its blinded cards and said "
          "it was\n"
          "acting on a reading it could not settle alone.\n\n",
          "card in time; that has not been measured.\n\n")
    d.path(F4 + "JQ-R04-CONTENT.md", F5 + "JQ-R04-CONTENT.md", 2)
    old = "c). The three parts below are word for word the third-fix run's.\n"
    d.rep(old, old +
          "Corrected by: Mateo · fifth-fix run · %s (system clock) — part a:\n"
          "one sentence about an earlier run is removed; it is not needed to "
          "answer\n"
          "(fourth review). The closing paragraph now says where it is decided\n"
          "whether the acceptance gate grades a field that stays "
          "(JQ-R04-CONTENT,\n"
          "which gained a part d). The three questions and their options are\n"
          "unchanged.\n" % DATE_LINE)
    d.rep("JQ-R04-CONTENT, all three of its parts",
          "JQ-R04-CONTENT, all four of its parts")
    d.rep("the field stays and is named in the exam manifest as a known "
          "channel. Neither\nanswer changes `RULES.md`.",
          "the field stays and is named in the exam manifest as a known "
          "channel;\n"
          "whether the acceptance gate grades what the audit computes from a "
          "field that\n"
          "stays is JQ-R04-CONTENT part d, which you answer too. Neither answer "
          "changes\n`RULES.md`.")


PART_D = '''## Part d · A field your answers keep on the card, and the acceptance gate

Before the answer key is sealed, the exam cards pass an acceptance gate. The
step it applies reads (`exam-prep/third-fix/juror-questions/JQ-R04-GATE.md`
lines 55–57, quoting the step as first written): "If `ALL-removable` beats
its chance line on the exam cards, the cards are not blind and the gate has
failed." Which of the two attacks decides was put to jurors and ratified
(`decisions/2026-10-01-jq-r04-gate/verdict.md` line 72): "The gate fails if
either the nearest-neighbour attack or the pair AUC attack beats its own
RULES 12 chance line on the exam cards." That ruling stands; this part does
not reopen it. The passages quoted in this part are all it needs; you need
not open either file.

What the row `ALL-removable` is (`JQ-R04-GATE.md` lines 64–66):
"`ALL-removable` is **every feature in the audit's current list**, minus the
families that must stay on the card because a frozen canteen rule or TACTICS
requires them." A **feature** is a number the audit computes from what a card
prints (for example the typical level of a column, or how many of its values
repeat); features are grouped into **families**. What is left out of the row
is still measured on the exam cards and named in the exam manifest with its
size; the gate does not grade it.

In the audit as it stands, everything it computes from the bitcoin and
ethereum columns, the trade-count column, the price column and the other
ranked columns is inside the row.

**Question d.** When the ratified answers to JQ-R04-DATE and to parts a–c
here keep a field on the exam card, do the features the audit computes from
that field count as families "that must stay on the card because … TACTICS
requires them", and so leave `ALL-removable`?

- **yes** — a field the ratified answers keep on the card stays because
  TACTICS, as they read it, requires it there; its features leave the row
  and are measured and named, not graded.
- **only where no permitted rendering leaves it out** — its features leave
  the row only when the ratified answers permit no exam card without that
  field; where a permitted rendering without it exists, the field stays in
  the row if it is used.
- **no** — only what a frozen canteen rule or TACTICS requires by its own
  words leaves the row; a field that stays because of a juror reading stays
  in the row, and the gate grades it.
- **Other**, with reasons.

Which features are computed from a field is read from the audit's code, not
chosen; the run that composes the row records it, and that run is reviewed.
If you think this cannot be answered as a definition — because one of the
options would accept or refuse a measured coin signature on exam cards under
RULES 9 as a rule, rather than read the gate's definition — say so: a
question about a rule is the user's, not a juror's (RULES 33).

---

## What follows from the answers — not to steer
'''


def jq_content(d):
    d.rep("TACTICS 3 puts on the card? — three parts\n",
          "TACTICS 3 puts on the card? — four parts\n")
    d.rep("third-fix run (`exam-prep/REVIEW-3.md` §5). **You do not need to "
          "open\n",
          "third-fix run (`exam-prep/REVIEW-3.md` §5).\n"
          "Corrected by: Mateo · fifth-fix run · %s (system clock) — part a\n"
          "states its premise without figures; one pointer in part c is "
          "removed;\n"
          "option b1 no longer says what happens after the channel is named; "
          "part d\n"
          "is new: it asks how a field your answers keep on the card stands "
          "with the\n"
          "acceptance gate, which the closing paragraph of this file and of\n"
          "JQ-R04-DATE now point to. The questions of parts a, b and c and the\n"
          "remaining options are unchanged.\n"
          "Part d arises from the fourth review. **You do not need to open\n"
          % DATE_LINE)
    d.path(F4 + "JQ-R04-DATE.md", F5 + "JQ-R04-DATE.md", 2)
    d.rep("RULES 9. You do **not** decide a threshold, a score or a trading "
          "rule; you do\n",
          "RULES 9; and, in part d, what the acceptance gate's definition of\n"
          "`ALL-removable` covers. You do **not** decide a threshold, a score "
          "or a\ntrading rule; you do\n")
    d.rep("contradict each other. Parts a and c of this file bear on each other "
          "(see\npart a).\n",
          "contradict each other. Parts a and c of this file bear on each other "
          "(see\npart a), and part d bears on every part of both files.\n")
    d.rep("  same rank (the configuration called `strict-flags`, audit run\n"
          "  `9ff0ffec3fe21ebe`);\n",
          "  same rank (the configuration called `strict-flags`);\n")
    d.rep("  writer had before it rounded (otherwise the same configuration, "
          "audit run\n  `d6557e91f9f97f7b`).\n",
          "  writer had before it rounded (otherwise the same configuration).\n")
    a = d.s.index("| rendering | feature | pair AUC (line) | nearest neighbour "
                  "(line) |\n")
    b = d.s.index("What the frozen canteen book does with the trade count:")
    old = d.s[a:b]
    if not (old.count("\n|") == 5 and old.endswith(
            "it is ranked from the values before rounding.\n\n")):
        sys.exit("STOP: JQ-R04-CONTENT part a table not as expected")
    d.s = d.s[:a] + (
        "Whether the column carries a measured coin signature on exam cards "
        "is\nmeasured by the audit before any exam card is used. Question a "
        "asks about\nthe case where it does.\n\n") + d.s[b:]
    d.rep("If your answer to part c permits ranking from the values before "
          "rounding and\nthat rendering is used, the condition of this "
          "question is not met for the\ntrade-count column on today's "
          "measurements; your answer to part a then\ngoverns any other column, "
          "or exam material, on which the condition is met.\n\n", "")
    d.rep("- **b1** — the actual price rebased to 100, at a fixed number of "
          "decimals,\n  with its measured signature named in the exam "
          "manifest.\n",
          "- **b1** — the actual price rebased to 100, at a fixed number of "
          "decimals.\n")
    d.rep("`516027c6c9f215d6`, H-4.) What the second way does to the "
          "trade-count\ncolumn's measured coin signature is in part a. Whether "
          "an exam candidate can\nuse the finer order is not measured.\n",
          "`516027c6c9f215d6`, H-4.) Whether an exam candidate can use the "
          "finer order\nis not measured.\n")
    d.rep("---\n\n## What follows from the answers — not to steer\n", PART_D)
    d.rep("used. Neither answer changes `RULES.md`; if no permitted rendering "
          "removes a\nchannel, the channel is named in the exam manifest with "
          "its number.",
          "used. Every channel the audit measures on the exam cards is named "
          "in the\nexam manifest with its number. Whether the acceptance gate "
          "grades a channel\nthat stays on the card is part d: where it does, "
          "the exam cards fail the\ngate if either attack beats its line on "
          "the row; where it does not, the\nchannel is measured and named but "
          "not graded. Neither answer changes\n`RULES.md`.")


EDITS = {"JQ-N1.md": jq_n1, "JQ-CANTEEN-8.md": jq_canteen8,
         "JQ-R04-DATE.md": jq_date, "JQ-R04-CONTENT.md": jq_content}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=DST)
    out = ap.parse_args().out
    os.makedirs(out, exist_ok=True)
    for name, fn in EDITS.items():
        with open(os.path.join(SRC, name), encoding="utf-8") as fh:
            d = Doc(fh.read())
        fn(d)
        dest = os.path.join(out, name)
        if os.path.exists(dest):
            with open(dest, encoding="utf-8") as fh:
                if fh.read() == d.s:
                    print("%s: already written, identical" % name)
                    continue
            if os.path.abspath(out) == os.path.abspath(DST):
                sys.exit("STOP: %s exists with different content; "
                         "not overwritten (RULES 30)" % dest)
        with open(dest, "w", encoding="utf-8") as fh:
            fh.write(d.s)
        print("%s: written" % name)


if __name__ == "__main__":
    main()
