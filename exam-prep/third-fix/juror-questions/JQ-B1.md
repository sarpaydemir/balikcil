# JQ-B1 · withdrawn as a juror question — a statement

Written by: Mateo · data engineer · third-fix run · 2026-10-01 (system clock).
This file replaces, for the coordinator, the juror file
`exam-prep/second-fix/juror-questions/JQ-B1.md`, which is kept unchanged.
**It is not a juror file and is not to be commissioned as one.** The reason is
below; the second review of the pre-exam work required that it be
established first whether any exam card can satisfy blocker B-1's frozen
trigger, and that the row be withdrawn or reduced to a statement if none can
(`exam-prep/REVIEW-2.md` §5).

## What was asked

The canteen chair recorded, and did not answer, "whether B-1's
instrument-class exclusion may be applied at all in a blind exam"
(`canteen/2026-09-19-sofia.md` lines 935–939). The second-fix run wrote it out
for jurors with three options: not in the exam; by the candidate from what
the card shows; by the judge's script from the sealed answer key.

## What is established, and from where

1. B-1's trigger, frozen: "the contract is AVGOUSDT or NOKUSDT"
   (`canteen/2026-09-19-sofia.md` line 187).
2. Both contracts are observation coins: both are in
   `data/draw/observation-coins.txt`.
3. TACTICS 1 draws the exam from "a different 20 coins" (`TACTICS.md` line
   24), and the draw script draws the exam symbols from what remains after
   the observation draw (`scripts/04_draw.py` lines 120–124). The draw
   manifest records the check: `"observation_x_exam_overlap": []` and
   `"disjoint": true` (`data/draw/draw-manifest.md`, "Disjointness check").

Counted, not asserted: `scripts/26_third_fix_checks.py`, run
`212dd7ecffc51263`, G-4. Nothing under `exam/` was read.

## What follows

Under the frozen trigger, **B-1 cannot fire on any exam card**, whichever of
the three means were chosen: the candidate, the judge's script and nobody at
all would all block the same set of exam cards — none. The question
therefore has no outcome that changes anything in the exam, and three jurors
would be asked to choose between options that cannot differ. In the money
test B-1 is a plain symbol exclusion (lines 205–212), which no option
disputes.

The second-fix file also asked jurors, if they chose a means, to say "what
the trigger … means for an exam set that does not contain those two
contracts". That asks for B-1's trigger to be read as an instrument class
rather than as the two contracts it names, which would be a changed trigger
— a new rule under RULES 6 (`RULES.md` lines 34–36), not a juror's
definition (RULES 33). That sentence is not carried forward.

## What would make it a question again — by name

- **The exam cards contain AVGOUSDT or NOKUSDT.** That would contradict the
  draw manifest; the exam-building run must check it before sealing the key
  (`exam-prep/HANDED-FORWARD.md`). If it happens, this statement is void and
  the question returns to jurors.
- **The laboratory wants B-1 to cover tokenised-equity contracts generally.**
  That is a new rule under RULES 6, for the user, with the "afterwards" label;
  it is not a juror question and is not raised here.

## Whether the withdrawal is mine to make

Withdrawing a question is not answering it: nothing above says whether B-1
*may* be applied in a blind exam, only that, as frozen, it never fires on an
exam card. Withdrawing is still a decision the instruction to this run did
not name, and it is listed as such in `exam-prep/VERDICT.md`. The coordinator
can reverse it; the second-fix juror file is unchanged and its closing
sentence would then have to be removed first.
