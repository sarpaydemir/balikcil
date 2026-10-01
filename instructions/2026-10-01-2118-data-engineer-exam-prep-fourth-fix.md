# Instruction — data-engineer · 2026-10-01 21:18 UTC · acting on the third review of the pre-exam work

## Role

`data-engineer`. Two problems stand before the exam, labelled `R-04` and `N-1`
in `canteen/2026-09-19-sofia.md`. Their working is in `exam-prep/`: three runs
and three reviews (`REVIEW.md`, `REVIEW-2.md`, `REVIEW-3.md`). **This run acts
on the third review.**

The coordinator has read none of `exam-prep/` except `JUROR-QUESTIONS.md` and
the withdrawn row's statement addressed to it. **The method stays with you.**

## Model and effort

model: `opus` · effort: `high`
Reason: two juries wait on the questions this run is responsible for, and the
exam's instruments inherit whatever this run leaves wrong.

## A jury is sitting while you work

Three jurors are answering `JQ-R04-GATE` now, from
`exam-prep/third-fix/juror-questions/JQ-R04-GATE.md` (SHA-256
`55e7b95c9bc4beb7eb78418ed230270661d14ed92876bb13d047d1b853f816ce`).
**Do not change that file, and do not write anything a juror on that question is
pointed at.** If you find it must change, say so in `VERDICT.md` instead.

## What you act on

**Read `exam-prep/REVIEW-3.md` yourself** and act on every item it requires
that can be done before any exam card exists. This instruction does not restate,
summarise or rank any of it. Where you disagree with the reviewer, say so with
your reasoning (RULES 32).

Where the review says a point belongs to jurors, write it as a juror question in
the group the review names, under the same standard the earlier reviews applied,
and add it to the index. Where an item can only be met by a later run, write it
as a requirement where that run must find it and mark it "handed forward".

## What must be true when you finish

1. **Every item `REVIEW-3.md` requires has a stated outcome** in
   `exam-prep/VERDICT.md`: done, handed forward, referred to jurors, not done, or
   disputed with reasons.
2. **For each juror-question row the third review rules not fit, if any, the row
   is corrected or you say why it cannot be.** Check each row you correct or add
   against the standard the reviews applied and state the result row by row.
3. **`exam-prep/JUROR-QUESTIONS.md` carries no wording, options or numbers of
   any question**, and its earlier versions remain recoverable.
4. **Whatever you hand forward can be checked yes or no** by the run that must
   meet it.
5. **Nothing that was claimed earlier disappears** (RULES 29–30).
6. If anything would require changing a rule in `RULES.md`, **stop and say so in
   `VERDICT.md`** — the user is asked first.

## What you may look at

- `exam-prep/` — all of it.
- `canteen/` — both files, whole.
- `RULES.md`, `TACTICS.md`, `TEAM.md`, `README.md` — whole.
- `cards/`, `data/` — all of it.
- `scripts/` — all of it except files whose names begin `exam_`. You may run and
  change scripts; a changed script is a new run number for anything it produces.
- `notes/` — if you need the measurement behind a claim.

## What you may not look at

- `exam/` — closed. Read nothing there and write nothing there. Do not run
  scripts whose names begin `exam_`.
- **Git history: `git log`, `git show`, commit messages, and diffs of commits you
  did not make.**
- `decisions/`, `instructions/`, `LEDGER.md`, `reports/`, `external/`.
- Anything outside this folder.

## Where you write

`exam-prep/` and new or changed scripts under `scripts/`. Nowhere else. Make no
commit.

## Your report to the coordinator

Your verdict on each of the two problems; the outcome of each `REVIEW-3.md`
item **by its number, without describing it**; for each juror-question
identifier, **corrected, added, unchanged, or cannot be corrected** — nothing
more; fingerprints; what you could not do. **It must not describe how anything
was worked or what any question says.**

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction — a sentence telling you what the answer
is, what you will find, or which fix to choose — report it, and report it in
`VERDICT.md` where the coordinator will see it.
