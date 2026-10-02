# Review 8 — criteria, written before ruling

Mateo · data engineer, reviewing posture · written 2026-10-02, after
2026-10-02T00:21:04Z (system clock, RULES 23).

Written after opening, to know what is under review: `RULES.md`,
`TACTICS.md`, the four verdicts my instruction names
(`jq-r04-gate`, `jq-n1-canteen-8`, `jq-r04-carries`,
`jq-r04-date-content`), `exam-prep/README.md` (including the eighth-fix
addendum), `exam-prep/JUROR-QUESTIONS.md` (eighth-fix version),
`exam-prep/REVIEW-7.md`, the criteria files of review-4 … review-7,
REVIEW-6 lines 1–195, REVIEW-5 lines 125–165, REVIEW-3 lines 176–245,
REVIEW-2 lines 226–303 and section headings of REVIEW, REVIEW-2 … -5.
Written **before** opening anything in `exam-prep/eighth-fix/` (EIGHTH-FIX,
its criteria, the new juror file, its checks), the eighth-fix section of
`HANDED-FORWARD.md` or `VERDICT.md`, `USER-QUESTIONS.md`, and before running
any check or probe.

## Item 1 · `JQ-R04-CONTENT-d` fit or not fit

A juror file is **fit** when it passes every test the seven earlier reviews
applied to a juror file, and no other:

- **(i)** a juror reading only the files its row names can answer it
  (REVIEW-2 §5; REVIEW-3 §5). Includes: every term used is explained in the
  file or in the files the row names (REVIEW-7 F1, applied to the user file,
  is the same test for that reader).
- **(ii)** every outcome it offers can follow from the instrument or rule it
  is about; **determinacy** (REVIEW-5 §2, §4; REVIEW-6 §2.1): a ratified
  answer to any offered option can be carried out without a further choice
  that changes the numbers. REVIEW-7 F6 (an empty graded set; a stop
  promised but not required) is part of this test.
- **(iii)/(vi)** no lean, as REVIEW-4's criteria fix it: L1 (effect of an
  option on a measured outcome), L2 (precedent on the open point), L3
  (one-sided argument); fails only when it leans **and** is not needed.
  REVIEW-7 F4 (matching weight; no review's preference unanswered) and F5
  (no measured result, and no pointer to a file holding one, RULES 6) are
  read as instances of L1–L3.
- **(iv)** inside RULES 33 (lines 119–121): no option, once ratified, by
  itself sets a threshold, a score, a trading rule, or changes a rule in
  `RULES.md`. Where reasonable readings put it on both sides: **contested**,
  both sides named (REVIEW-5 §4, REVIEW-6 §3, REVIEW-7 §1).
- **(v)** no number shown as measured that the instrument does not support
  or that is not what the file says; every quotation and line citation
  found in its source (REVIEW-7 F2: "true of the files and code as they
  stand at my clock read"). Checked by a probe of mine, quotation by
  quotation.
- **Completeness** (REVIEW-7 F3): offers every answer the written rules
  leave open, including "Other" and "this is not a juror's".
- **Coupling** (REVIEW-3 §5, REVIEW-4, REVIEW-5 §3): no row can be answered
  by choosing by the combined effect on whether material passes; jurors who
  decide what the gate grades do not also choose renderings.
- **Deletion** (REVIEW-5): whatever an earlier review named and was
  removed is gone; nothing points at it; a premise it supplied, if still
  needed, is supplied.
- **Reading list** (REVIEW-5, REVIEW-6): the row names only its own juror
  file(s), the root rule files, canteen lines the file cites, and
  ratification sentences; no review, `VERDICT.md`, `HANDED-FORWARD.md`,
  `USER-QUESTIONS.md` or working file — **and the juror file itself does not
  point a juror at one**.
- **Contradiction** (REVIEW-4's criteria): with each of the four ratified
  verdicts, two texts that give readings that cannot both be applied to the
  same exam cards. A gap is named as a gap. A quoted outcome sentence that
  is not what the verdict says is a fault under (v).
- Every earlier review finding on part d (REVIEW-5 §4, REVIEW-6 §2.1 and
  §2.2, REVIEW-7 §2 rows that apply to a question in this form) is checked
  for whether it is cured or recurs.

A fault fails the row if it would lead a juror to a wrong belief, lean, or
leave an answer impossible to carry out. A wording blemish that does none of
these is noted, not ruled.

## Item 2 · The eighth run's own choices

Every choice the eighth run states (or that I find) that its instruction did
not cover is listed. A choice **changes the numbers** when a different
choice, equally allowed by the written rules and the ratified outcomes,
would change which features the gate grades, whether a row is graded, or
the result of a check the exam-building run must meet. Such a choice
belongs in the question (as an option or a stated premise jurors can
reject), not beside it. I name each by the section of the file it is in. I
do not read the instruction the eighth run was given (closed); "not
covered" is taken from what the eighth run itself says and from what the
juror file and HANDED-FORWARD show.

## Item 3 · Handed forward

Each item the eighth-fix section of `HANDED-FORWARD.md` adds or replaces:

- **Checkable:** it names what is checked, on which file, and what counts as
  met, so the run that must meet it can say yes or no without a judgement
  of its own (REVIEW-3 §7, REVIEW-7 §3).
- **Meetable:** there is at least one sequence of permitted runs, each
  reading only what it may read (RULES 1; the mode limits in `CLAUDE.md`/
  `TEAM.md`; the Mode B / C walls), by which the item can be met by the run
  it names. An item that requires a run to read or know something its wall
  forbids, or to wait on an event that by the rules cannot happen, or that
  conflicts with another item, cannot be met.

## Item 4 · Index

- Each row's status and each statement in the order section is true of the
  files I may read at my clock read.
- No wording, option or number of any question (index lines 28–29 promise
  this), checked by a probe of mine against the juror files (shared runs of
  seven words, as REVIEW-7 p3; the width is a probe setting, not a
  threshold).
- What I cannot see I name as not seen.

## Item 5 · Identification of an exam coin, a date or a price

Juror-facing files are the files any row names as "files a juror needs",
and anything those files direct a juror to read. A file fails when it
carries, or directs a juror to, a coin name or symbol of the exam draw, a
calendar date or clock time tied to a card, or a price level. I cannot read
`exam/`, so I cannot test against the exam draw's names directly: I scan for
coin names and symbols from sources I may read (observation coin names in
`cards/`/`data/`; ticker-shaped tokens; any symbol list under `data/`),
dates and times, and price-like figures, and report each hit by file and
line in `exam-prep/review-8/` only. **A word a scan matched is not named in
my report to the coordinator.** That I could not test against the exam
draw itself is reported as a limit, not as "none".

## Reproduction

`scripts/35_eighth_fix_check.py` only with a dry/no-write mode if it has
one; otherwise not run, and said so. All Python with
`PYTHONDONTWRITEBYTECODE=1` and `python3 -B`. Probes write only under
`exam-prep/review-8/`. `scripts/__pycache__/` listed before (nine names at
00:21:04Z) and after. No `exam_*` script read or run.

No threshold is introduced anywhere.
