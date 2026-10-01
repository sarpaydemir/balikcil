# Review 4 — criteria written before ruling

Mateo · data engineer, reviewing posture · written 2026-10-01T21:56Z (system
clock), before any figure in the fourth run's juror files was re-checked and
before any row was ruled on. By this time I had read: `RULES.md`,
`TACTICS.md`, `exam-prep/README.md`, `exam-prep/JUROR-QUESTIONS.md`,
`exam-prep/REVIEW-3.md`, `exam-prep/fourth-fix/FOURTH-FIX.md`, the four
fourth-fix juror files, `exam-prep/third-fix/juror-questions/JQ-R04-GATE.md`,
`decisions/2026-10-01-jq-r04-gate/verdict.md`, the fourth-fix sections of
`VERDICT.md` and `HANDED-FORWARD.md`, and two passages of
`canteen/2026-09-19-sofia.md` (lines 180–215, 900–945). So these criteria
are not blind to the files; they are written before any number is checked.

## Fitness

A row is **fit** when it passes REVIEW-2's five tests as REVIEW-3 applied them
(i–v, quoted in REVIEW-3 §5) **and** test (vi), the one the instruction adds:

> (vi) a juror file carries no figure, passage or precedent that leans toward
> one of the options it offers. A figure belongs in a juror file only where
> the question cannot be answered without it, and then it must be correct.

## How I apply (vi) — fixed here, applied the same way to every row

A file item (figure, passage or precedent) **fails (vi)** when both hold:

1. **It leans.** It gives a juror a reason to prefer one offered option over
   another that is not a reading of the rule text the question is about.
   Three kinds, named so the test is applied the same way everywhere:
   - **L1 · effect of an option.** It shows what choosing an option does to
     a measured outcome the laboratory acts on — whether material passes a
     gate, whether a coin signature remains, how strict a chance line is —
     where the question and its options do not themselves refer to that
     outcome. (The laboratory's own precedent for this test is
     `JQ-R04-GATE.md` lines 154–157: the result of each reading is withheld
     "so that the choice is made on the wording and not on its result
     (RULES 6)".)
   - **L2 · precedent.** It reports what an earlier run, script or person
     chose or did on the open point itself, beyond describing what a card
     currently prints.
   - **L3 · one-sided argument.** An argument outside the options list that
     supports one option and has no counterpart for the others.
2. **It is not needed.** A juror could answer the question without it: it is
   not the premise of the question or of an option (the fact the question or
   an option text itself refers to), and not a description of what an
   option does mechanically.

An item that is needed passes (vi) if it is correct (test v). An item that
is not needed but does not lean is not a failure of (vi); I may note it.

A row fails (vi) if any item in the part the row names, or in a shared
section of the file that the row's jurors read, fails. Where one item is
read by several rows (a shared table, or a figure in one part that the file
points another part to), I name every row it affects.

## Correctness (test v)

Every figure a row shows must be recomputed or traced to a run I re-ran, and
must be what the file says it is. A figure equal to the source but labelled
as something it is not fails (v), as in REVIEW-3 §9 item 7.

## Couplings

A coupling stands when the rows answered together share a rule text or an
outcome that changes another's meaning, and when no row in a coupled group
can be answered by choosing by the combined effect on whether material
passes (REVIEW-3 §5's test for GATE).

## Contradiction with the ratified JQ-R04-GATE verdict

A contradiction exists when the verdict (as ratified, read with the GATE
file it answered) and a to-be-commissioned juror file give the same rule
text readings that cannot both be applied to the same exam cards. A gap
(one says nothing where the other speaks) is named as a gap, not a
contradiction.

## Reproduction

A script output reproduces when re-running it under the stated run number
gives the same run number and byte-identical output files, apart from lines
that record the clock, free disk or output path. Any other difference is a
failure to reproduce and is reported as such.

## Rulings on the problems

Solved / not solved / solved only under stated conditions, with the
conditions named. No new threshold is introduced anywhere; every constant
in my probes is imported from the instruments or from RULES 12 / TACTICS 1.
