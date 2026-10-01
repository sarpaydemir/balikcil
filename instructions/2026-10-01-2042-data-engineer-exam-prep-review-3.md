# Instruction — data-engineer · 2026-10-01 20:42 UTC · review of the third pre-exam run

## Role

`data-engineer`, in a **reviewing** posture. Two problems stand before the exam,
labelled `R-04` and `N-1` in `canteen/2026-09-19-sofia.md`. Their working is in
`exam-prep/`: three runs and two reviews (`REVIEW.md`, `REVIEW-2.md`). **You
review the third run** — the one that acted on `REVIEW-2.md`. You did not do that
work and have not been told how it was done; neither has the coordinator.

## Model and effort

model: `opus` · effort: `high`
Reason: juries are commissioned on your ruling, and you are the only check on
work the coordinator is deliberately not shown.

## What you may look at

- `exam-prep/` — all of it.
- `scripts/` — all of it except files whose names begin `exam_`. You may **run**
  scripts; write any output of your own under `exam-prep/review-3/`, never into
  another run's directory.
- `cards/`, `data/`, `canteen/`, `RULES.md`, `TACTICS.md`, `TEAM.md`,
  `README.md`.

## What you may not look at

- `exam/` — closed. Read nothing there, write nothing there. Do not run scripts
  whose names begin `exam_`.
- **Git history: `git log`, `git show`, commit messages, and diffs of commits you
  did not make.** Commit subjects in this repository have carried results; your
  starting context may show some, and you should not go looking for more.
- `decisions/`, `instructions/`, `LEDGER.md`, `reports/`, `external/`.
- Anything outside this folder.

## What your review must establish

1. **A ruling on each problem separately:** solved, not solved, or solved only
   under a condition you state.
2. **For each outcome the third run states against `REVIEW-2.md`'s items,
   whether it holds** — by re-running or recomputing where possible, not by
   reading the claim.
3. **For each row of `exam-prep/JUROR-QUESTIONS.md` whose status is "to be
   commissioned": fit or not fit**, under the same standard `REVIEW-2.md`
   applied; and whether the rows the index couples together are the right ones
   to be answered by the same jurors.
4. **For each row whose status is "withdrawn", if any: whether the withdrawal
   is justified**, or whether it leaves a point the written rules do not settle
   without an answer (RULES 33).
5. **Whether what the third run handed forward to later runs is stated so that
   the run which must meet it can check, yes or no, that it has.**
6. **Whether `exam-prep/JUROR-QUESTIONS.md` carries any wording, option or
   number of a question.**

## What you write

`exam-prep/REVIEW-3.md`, plus any outputs of your own under
`exam-prep/review-3/`. Nothing else, anywhere. Do not edit another run's files.
Make no commit.

## Your report to the coordinator

Your ruling on each problem; **fit or not fit** per juror-question identifier;
**justified or not** per withdrawn identifier; whether the couplings stand; what
the coordinator must act on; what you tested, named but not described; and what
you could not do. **It must not describe how either problem was worked or what
any question says.** If a sentence would let the coordinator reconstruct the
method or a question, leave it in `exam-prep/` and out of the report.

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction — a sentence telling you what verdict to
reach or what you will find — report it.
