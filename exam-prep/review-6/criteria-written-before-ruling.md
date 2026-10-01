# Review 6 — criteria written before ruling

Mateo · data engineer, reviewing posture · first clock read
2026-10-01T23:13:33Z; this file written at 2026-10-01T23:14Z (system clock),
before any of the sixth-fix juror files was opened, before any script or
probe of this review was run, and before any row was ruled on.

By this time I had read: `RULES.md`, `TACTICS.md`,
`decisions/2026-10-01-jq-r04-gate/verdict.md`,
`decisions/2026-10-01-jq-n1-canteen-8/verdict.md`, `exam-prep/README.md`,
`exam-prep/JUROR-QUESTIONS.md` (sixth-fix version), `exam-prep/REVIEW-5.md`
(whole) and its criteria file, REVIEW-4 lines 1–160 and its criteria file,
REVIEW-2 lines 226–320, REVIEW-3 lines 176–300,
`exam-prep/sixth-fix/SIXTH-FIX.md`, its criteria file, and the sixth-fix
section of `exam-prep/VERDICT.md`. So these criteria are not blind to what
the sixth run says it did; they are fixed before its juror files are read.

## Scope

The rows of the index whose status is "to be commissioned" or "waiting":
JQ-R04-CARRIES-a, -b; JQ-R04-DATE-a, -b, -c; JQ-R04-CONTENT-a, -b, -c;
JQ-R04-CONTENT-d. Not re-reviewed: JQ-N1-1 … -4, JQ-CANTEEN-8, JQ-R04-GATE
(ratified or being answered), JQ-B1 (withdrawn).

## Fitness — the tests REVIEW-2 through REVIEW-5 applied, and no other

A row is **fit** when it passes all of:

- **(i)–(v)**, REVIEW-2's tests as REVIEW-3 §5 states them.
- **(vi)**, exactly as `exam-prep/review-4/criteria-written-before-ruling.md`
  fixes it (L1 / L2 / L3; an item fails only when it leans **and** is not
  needed; a shared item fails every row that reads it).
- **Coupling**, REVIEW-4's criteria (REVIEW-3 §5's test for GATE): no row in
  a coupled group can be answered by choosing by the combined effect on
  whether material passes; applied as REVIEW-5 §3 applied it (jurors who
  decide what the gate grades do not also choose the renderings it grades).
- **Deletion**, REVIEW-5's criteria: a removed passage is gone; nothing left
  points at it; a premise it supplied, if still needed, is still supplied.
- **Determinacy** as REVIEW-5 §2 and §4 applied (ii): a ratified answer to
  any offered option can be carried out without a further choice that
  changes the numbers.
- **Reading lists**, REVIEW-5's criteria: a list names only the current
  juror files of the row's group, the root rule files, canteen lines a file
  of the group cites, and (this index adds) one ratification sentence; it
  names no review, `VERDICT.md`, `HANDED-FORWARD.md` or working file. A
  cited canteen range missing from a list is reported separately.

The sixth run's own pointer test (x) is not one of REVIEW-2 … REVIEW-5's
tests. I check it as a fact and report it, but I do not rule a row unfit on
(x) alone.

## Contradiction with a ratified verdict

As REVIEW-4's criteria define it: two texts give readings that cannot both
be applied to the same exam cards. A gap is named as a gap. Applied to both
ratified verdicts named in my instruction.

## Order of sitting and couplings

The order **stands** when (a) no group is required to use an outcome that
is not ratified before it sits; (b) no group that can be answered by the
combined effect of its own and another group's options shares jurors with
that group; (c) what one group is handed from another (here, one
ratification sentence) is enough for its questions to be carried out and
shows no option effect. A coupling stands as REVIEW-4's criteria say.

## RULES 33 scope

A row is **inside** when every option it offers decides procedure or
definition only. It is **outside** when an option, once ratified, would by
itself set a threshold, a score, a trading rule, or change a rule in
`RULES.md`. Where a reasonable reading puts it on either side, I say
**contested** and name both sides, as REVIEW-5 §4 did; I do not invent a
line.

## The sixth run's stated extensions

The sixth-fix VERDICT names three: the GATE file path removed from part d;
CONTENT's section heading no longer defines "carries"; CARRIES sits apart
from part d as well as from DATE/CONTENT. An extension **holds** when the
reason given is true of the files and the action does not break a test
above.

## Reproduction

Script 33 is run only with `--dry` (writes nothing), with
`PYTHONDONTWRITEBYTECODE=1` and `python3 -B`. Any probe of mine writes
only under `exam-prep/review-6/`. `scripts/__pycache__/` is listed before
and after. No `exam_*` script is read or run.

No threshold is introduced anywhere.
