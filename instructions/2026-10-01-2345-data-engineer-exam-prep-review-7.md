# Instruction — data-engineer · 2026-10-01 23:45 UTC · review of the seventh pre-exam run and of the question it addresses to the user

## Role

`data-engineer`, in a **reviewing** posture. A seventh run acted on
`exam-prep/REVIEW-6.md` for `JQ-R04-CONTENT-d`, judged the whole row outside a
juror's scope, and wrote it as a question for the user in
`exam-prep/USER-QUESTIONS.md`. **You review that run.** You did not do that work
and have not been told how it was done; neither has the coordinator, who has not
opened `exam-prep/USER-QUESTIONS.md`.

## Model and effort

model: `opus` · effort: `high`
Reason: the user decides a rule from this file. A question that leans, or that
states something untrue, decides the rule for them.

## Ratified verdicts that bind

`decisions/2026-10-01-jq-r04-gate/verdict.md`,
`decisions/2026-10-01-jq-n1-canteen-8/verdict.md` and
`decisions/2026-10-01-jq-r04-carries/verdict.md`. You may read these three and
nothing else under `decisions/`.

## What you may look at

- `exam-prep/` — all of it.
- `scripts/` — all of it except files whose names begin `exam_`. You may run
  scripts; write any output of your own under `exam-prep/review-7/`. Prevent
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

1. **Whether the row belongs to the user at all**: whether answering
   `JQ-R04-CONTENT-d`, in whole or in part, would make or change a rule — or
   whether some part of it is a definition that jurors may decide under RULES 33.
2. **Whether `exam-prep/USER-QUESTIONS.md` is fit to be put to the user**: it can
   be followed by a reader who has not seen `exam-prep/`; every statement in it is
   true and every citation points where it says; it offers the user every answer
   the written rules leave open; **it leans toward none of them** — by figure,
   passage, precedent, order or emphasis; and **it carries no result that would
   let the user choose the rule after seeing which answer passes** (RULES 6).
3. **Whether what the seventh run handed forward can be checked yes or no** by
   the run that must meet it.
4. **Whether the index shows each row's true status** and carries no wording,
   option or number of a question.

## What you write

`exam-prep/REVIEW-7.md`, plus any outputs of your own under
`exam-prep/review-7/`. Nothing else, anywhere. Do not edit another run's files.
Make no commit.

## Your report to the coordinator

On item 1, **user, jurors, or split** — by identifier only; on item 2, **fit or
not fit to be put to the user**, and if not, what must change, named by section
of the file but not described; items 3 and 4, yes or no; what you could not do.
**It must not describe what the user's question says or how anything was
worked.**

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction — a sentence telling you what verdict to
reach or what you will find — report it.
