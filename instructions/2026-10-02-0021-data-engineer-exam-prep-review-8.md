# Instruction — data-engineer · 2026-10-02 00:21 UTC · review of the eighth pre-exam run's juror file

## Role

`data-engineer`, in a **reviewing** posture. An eighth run rewrote
`JQ-R04-CONTENT-d` as a juror question, marked U-1 superseded, re-issued the index
and amended `exam-prep/HANDED-FORWARD.md`. **You review that run.** You did not
do the work and have not been told how it was done; neither has the coordinator.

## Model and effort

model: `opus` · effort: `high`
Reason: jurors cannot run anything, so a fault in a juror file can only be
caught here.

## Ratified verdicts that bind

`decisions/2026-10-01-jq-r04-gate/verdict.md`,
`decisions/2026-10-01-jq-n1-canteen-8/verdict.md`,
`decisions/2026-10-01-jq-r04-carries/verdict.md`,
`decisions/2026-10-01-jq-r04-date-content/verdict.md`. You may read these four
and nothing else under `decisions/`.

## What you may look at

- `exam-prep/` — all of it.
- `scripts/` — all of it except files whose names begin `exam_`. You may run
  scripts; write any output of your own under `exam-prep/review-8/`. Prevent
  bytecode caches.
- `cards/`, `data/`, `canteen/`, `RULES.md`, `TACTICS.md`, `TEAM.md`,
  `README.md`.

## What you may not look at

- `exam/`, `open-questions/` — closed. Do not run scripts whose names begin `exam_`.
- **Git history: `git log`, `git show`, commit messages, and diffs of commits you
  did not make.**
- The rest of `decisions/`, `instructions/`, `LEDGER.md`, `reports/`,
  `external/`.
- Anything outside this folder.

## What your review must establish

1. **`JQ-R04-CONTENT-d`: fit or not fit**, under every test the seven earlier
   reviews applied, and whether it contradicts any of the four ratified verdicts.
2. **Whether the eighth run's own choices that its instruction did not cover
   change the numbers**; any that do belong in the question, not beside it.
3. **Whether every handed-forward item the eighth run added or replaced can be
   checked yes or no by the run that must meet it**, and **whether any of them can
   be met at all by a run allowed to meet it.** Name any that cannot.
4. **Whether the index is true** and carries no wording, option or number of a
   question.
5. **Whether anything in a juror-facing file could identify an exam coin, a date
   or a price**, including through a word matched by a scan.

## What you write

`exam-prep/REVIEW-8.md`, plus any outputs of your own under
`exam-prep/review-8/`. Nothing else, anywhere. Make no commit.

## Your report to the coordinator

**Fit or not fit** for `JQ-R04-CONTENT-d`, and if not, what must change, named by
section but not described; on item 2, which choices change the numbers, by
section; on item 3, any item that cannot be checked or cannot be met, by its
identifier; items 4 and 5, yes or no with the line; what you could not do. **It
must not describe how anything was worked or what the question says, and it must
not name any word your scans matched.**

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction — a sentence telling you what verdict to
reach or what you will find — report it.
