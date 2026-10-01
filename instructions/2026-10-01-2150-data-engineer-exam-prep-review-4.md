# Instruction — data-engineer · 2026-10-01 21:50 UTC · review of the fourth pre-exam run

## Role

`data-engineer`, in a **reviewing** posture. Two problems stand before the exam,
labelled `R-04` and `N-1` in `canteen/2026-09-19-sofia.md`. Their working is in
`exam-prep/`: four runs and three reviews. **You review the fourth run** — the
one that acted on `REVIEW-3.md`. You did not do that work and have not been told
how it was done; neither has the coordinator.

This review is **narrower** than the ones before it. Two juries wait on it.

## Model and effort

model: `opus` · effort: `high`
Reason: two juries are commissioned on your ruling, and jurors cannot check a
figure; they have no tools to run anything.

## What you may look at

- `exam-prep/` — all of it.
- `scripts/` — all of it except files whose names begin `exam_`. You may **run**
  scripts; write any output of your own under `exam-prep/review-4/`.
- `cards/`, `data/`, `canteen/`, `RULES.md`, `TACTICS.md`, `TEAM.md`,
  `README.md`.
- `decisions/2026-10-01-jq-r04-gate/verdict.md` — a ratified verdict on a
  neighbouring question; you may read this file and nothing else under
  `decisions/`.

## What you may not look at

- `exam/` — closed. Read nothing there, write nothing there. Do not run scripts
  whose names begin `exam_`.
- **Git history: `git log`, `git show`, commit messages, and diffs of commits you
  did not make.**
- The rest of `decisions/`, `instructions/`, `LEDGER.md`, `reports/`,
  `external/`.
- Anything outside this folder.

## What your review must establish

1. **For each row of `exam-prep/JUROR-QUESTIONS.md` whose status is "to be
   commissioned": fit or not fit.** Apply the standard `REVIEW-2.md` and
   `REVIEW-3.md` applied, and one more test those reviews did not state:
   **a juror file carries no figure, passage or precedent that leans toward one
   of the options it offers.** A figure belongs in a juror file only where the
   question cannot be answered without it, and then it must be correct. Name, in
   `REVIEW-4.md`, anything that fails this test.
2. **Whether the couplings in the index stand.**
3. **Whether the ratified verdict on `JQ-R04-GATE` and any juror file still to be
   commissioned read the same rule in contradictory ways**, and if so, where.
4. **For the scripts the fourth run changed or added, whether their outputs
   reproduce** under the run numbers it states.
5. **A ruling on each problem**: solved, not solved, or solved only under a
   condition you state.

You need not re-review what `REVIEW-3.md` already ruled on and the fourth run
did not change.

## What you write

`exam-prep/REVIEW-4.md`, plus any outputs of your own under
`exam-prep/review-4/`. Nothing else, anywhere. Do not edit another run's files.
Make no commit.

## Your report to the coordinator

**Fit or not fit** per juror-question identifier; whether the couplings stand;
whether any contradiction with the ratified verdict exists, located by file and
section only; your ruling on each problem; what the coordinator must act on;
what you tested, named but not described; what you could not do. **It must not
describe how either problem was worked or what any question says.**

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction — a sentence telling you what verdict to
reach or what you will find — report it.
