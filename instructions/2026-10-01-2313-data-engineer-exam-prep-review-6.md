# Instruction — data-engineer · 2026-10-01 23:13 UTC · review of the sixth pre-exam run's juror files

## Role

`data-engineer`, in a **reviewing** posture. A sixth run has acted on
`exam-prep/REVIEW-5.md` for the `JQ-R04-DATE` and `JQ-R04-CONTENT` rows, added
`JQ-R04-CARRIES-a` and `-b`, moved `JQ-R04-CONTENT-d` into a file of its own, and
re-issued `exam-prep/JUROR-QUESTIONS.md`. **You review only the R-04 rows still
to be commissioned.** You did not do that work and have not been told how it was
done; neither has the coordinator.

## Model and effort

model: `opus` · effort: `high`
Reason: jurors cannot run anything, so a fault in a juror file can only be
caught here.

## Ratified verdicts that bind

- `decisions/2026-10-01-jq-r04-gate/verdict.md`
- `decisions/2026-10-01-jq-n1-canteen-8/verdict.md`

You may read both. Nothing else under `decisions/`.

## What you may look at

- `exam-prep/` — all of it.
- `scripts/` — all of it except files whose names begin `exam_`. You may run
  scripts; write any output of your own under `exam-prep/review-6/`. Prevent
  bytecode caches.
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

1. **For each row of the index whose status is "to be commissioned" or
   "waiting": fit or not fit**, under every test `REVIEW-2.md` through
   `REVIEW-5.md` applied.
2. **Whether any of those rows contradicts either ratified verdict above.**
3. **Whether the order of sitting in the index, and its couplings, stand.**
4. **Whether each of those rows is inside what a juror may decide under RULES
   33**, or would decide a threshold, a score, a trading rule or a change to a
   rule in `RULES.md`. Name any row that is outside, by identifier.
5. **Whether the sixth run's stated extensions of `REVIEW-5.md` hold.**

Do not re-review the `JQ-N1` group, `JQ-CANTEEN-8` or `JQ-R04-GATE`: they are
ratified.

## What you write

`exam-prep/REVIEW-6.md`, plus any outputs of your own under
`exam-prep/review-6/`. Nothing else, anywhere. Make no commit.

## Your report to the coordinator

**Fit or not fit** per identifier; **inside or outside a juror's scope** per
identifier; any contradiction with a ratified verdict, by file and section only;
whether the order and couplings stand; whether the extensions hold; what you
could not do. **It must not describe how either problem was worked or what any
question says.**

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction — a sentence telling you what verdict to
reach or what you will find — report it.
