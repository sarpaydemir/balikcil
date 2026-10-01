# Review 5 — criteria written before ruling

Mateo · data engineer, reviewing posture · first clock read
2026-10-01T22:43:49Z (system clock); written before any script or probe of
this review was run and before any row was ruled on.

By this time I had read: `RULES.md`, `TACTICS.md`, `exam-prep/REVIEW-4.md`,
`exam-prep/review-4/criteria-written-before-ruling.md`, REVIEW-2 §5 and
REVIEW-3 §5 (tests and couplings), `exam-prep/JUROR-QUESTIONS.md`,
`exam-prep/fifth-fix/FIFTH-FIX.md`, its criteria file, the four fifth-fix
juror files and their `diff` against the fourth-fix files, the fifth-fix
sections of `VERDICT.md` and `HANDED-FORWARD.md`,
`exam-prep/third-fix/juror-questions/JQ-R04-GATE.md` lines 1–161,
`decisions/2026-10-01-jq-r04-gate/verdict.md`, `R-04-blindness.md`
lines 175–200 and 285–320, and `scripts/29_identity_audit_exact.py`
(header lines 55–115, `card_features()`, `REPEAT_GROUP`, `FAMILIES`,
`FORCED_FAMILIES`, the `ALL-removable` construction). So these criteria are
not blind to the files; they are fixed before any check is run.

## Scope

Only what the fifth run changed or added: the deletions and additions in the
four juror files, the new part d, the index, and the three disagreements the
fifth run states (VERDICT fifth-fix section, "Where I disagree"). A part
whose text is unchanged is checked only for what the change around it does
to it (a shared section it is read with, a pointer, the group it sits in).

## Fitness — the same tests, applied as before

A row is **fit** when it passes REVIEW-2's (i)–(v) as REVIEW-3 §5 states
them, REVIEW-4's (vi) exactly as its criteria file fixes it (L1 / L2 / L3,
failing only when it leans **and** is not needed), and the coupling test of
REVIEW-4's criteria ("no row in a coupled group can be answered by choosing
by the combined effect on whether material passes", REVIEW-3 §5's test for
GATE). I add no test of my own.

For a deletion: (a) the passage REVIEW-4 named is gone; (b) nothing left
points at what is gone; (c) the premise the deleted passage supplied, if the
question still needs it, is still supplied.

For the new part d: all of (i)–(vi), the coupling test, and the
contradiction test below; every quoted passage checked against its source
lines by a probe of mine; its premise sentence checked against the audit's
code by a probe of mine.

## Contradiction with the ratified verdict

As REVIEW-4's criteria define it: two texts give readings that cannot both
be applied to the same exam cards. A gap is named as a gap.

## The gap REVIEW-4 named (one attack enough for "carries a signature"?)

It **must be answered before the group** if, as the fifth-run files now
stand, a juror's answer to some part cannot be carried out, or would mean
different things, depending on it (test (i) or (ii)). Otherwise it is a gap
that can follow.

## Reading lists

A list complies when it names only the current juror files of the row's
group, the root rule files, and canteen lines a file of the group cites; and
names no review, no `VERDICT.md`, no `HANDED-FORWARD.md`, no working file.
A cited canteen range missing from a list is reported separately (it is not
"beyond what the question needs").

## Disagreements

A disagreement holds when the reason given is true of the files and the
action taken does not break a test above.

## Reproduction

The fifth run's builder and check script are run with
`PYTHONDONTWRITEBYTECODE=1` and `python3 -B`, writing only under
`exam-prep/review-5/` (the builder with `--out`; the check with `--dry`,
which writes nothing). `scripts/__pycache__/` is listed before and after.

No threshold is introduced anywhere.
