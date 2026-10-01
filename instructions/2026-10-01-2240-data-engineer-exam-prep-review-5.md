# Instruction — data-engineer · 2026-10-01 22:40 UTC · review of the fifth pre-exam run's juror files

## Role

`data-engineer`, in a **reviewing** posture. A fifth run has acted on
`exam-prep/REVIEW-4.md` and re-issued the juror files and
`exam-prep/JUROR-QUESTIONS.md`. **You review only what that run changed or
added.** You did not do that work and have not been told how it was done;
neither has the coordinator.

## Model and effort

model: `opus` · effort: `high`
Reason: jurors cannot run anything, so a fault in a juror file can only be
caught here.

## What you may look at

- `exam-prep/` — all of it.
- `decisions/2026-10-01-jq-r04-gate/verdict.md` — a ratified verdict; nothing
  else under `decisions/`.
- `scripts/` — all of it except files whose names begin `exam_`. You may run
  scripts; write any output of your own under `exam-prep/review-5/`. If running
  a script would write a bytecode cache, prevent it.
- `cards/`, `data/`, `canteen/`, `RULES.md`, `TACTICS.md`, `TEAM.md`,
  `README.md`.

## What you may not look at

- `exam/` — closed. Do not run scripts whose names begin `exam_`.
- **Git history: `git log`, `git show`, commit messages, and diffs of commits you
  did not make.**
- The rest of `decisions/`, `instructions/`, `LEDGER.md`, `reports/`,
  `external/`.
- Anything outside this folder.

## What your review must establish

1. **For each juror-question row whose status is "to be commissioned": fit or
   not fit**, under every test `REVIEW-2.md`, `REVIEW-3.md` and `REVIEW-4.md`
   applied. Where the fifth run left a part's text unchanged, you need only
   check what it did change in that file.
2. **Whether any row to be commissioned contradicts the ratified gate verdict.**
3. **Whether the point `REVIEW-4.md` names as a gap rather than a contradiction
   must be answered before the group it sits in can be.** If it must, say which
   row is not fit until it is.
4. **Whether the index's reading lists give a juror nothing beyond what each
   question needs**, and name no review, `VERDICT.md` or working file.
5. **Whether the fifth run's stated disagreements with `REVIEW-4.md` hold.**

Do not re-review what `REVIEW-4.md` ruled on and the fifth run did not change.

## What you write

`exam-prep/REVIEW-5.md`, plus any outputs of your own under
`exam-prep/review-5/`. Nothing else, anywhere. Make no commit.

## Your report to the coordinator

**Fit or not fit** per juror-question identifier; whether any contradiction
with the ratified verdict exists, by file and section only; your answer on the
gap, by row identifier only; whether the reading lists comply; whether the
disagreements hold; what you could not do. **It must not describe how either
problem was worked or what any question says.**

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction — a sentence telling you what verdict to
reach or what you will find — report it.
