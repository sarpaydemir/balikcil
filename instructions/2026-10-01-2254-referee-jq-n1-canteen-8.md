# Instruction — referee · 2026-10-01 22:54 UTC · open question JQ-N1-1 to JQ-N1-4 with JQ-CANTEEN-8

## Role

`referee`. Three jurors have answered one open question independently. You
ratify the outcome or refuse it, under RULES 35.

## Model and effort

model: `haiku` · effort: medium
Reason: RULES 35 and your own definition. You are small on purpose.

## What you may look at

- `decisions/2026-10-01-jq-n1-canteen-8/juror-1.md`
- `decisions/2026-10-01-jq-n1-canteen-8/juror-2.md`
- `decisions/2026-10-01-jq-n1-canteen-8/juror-3.md`
- `instructions/2026-10-01-2249-juror-jq-n1-canteen-8-1.md` — the instruction the jurors were given; all three received the
  same text but for the juror number and the output file.
- `exam-prep/fifth-fix/juror-questions/JQ-N1.md`
- `exam-prep/fifth-fix/juror-questions/JQ-CANTEEN-8.md`
  — where the question is written, for the independence and scope checks.
- `RULES.md`, `TACTICS.md`, `TEAM.md`.
- `decisions/2026-09-19-*/verdict.md` and `decisions/2026-10-01-jq-r04-gate/verdict.md`
  — ratified verdicts on other questions.

## What you may not look at

- `exam/` — closed.
- `LEDGER.md`, `notes/`, `cards/`, `reports/`, `data/`, `scripts/`, `external/`,
  and anything in `exam-prep/` or `decisions/` not named above. You are judging
  the answers, not re-answering the question.
- Anything outside this folder.

## Your job

The six checks your definition sets out, in order, each with its result written
down: count · independence · grounding · the outcome and its split in numbers ·
the reasoned objection (RULES 32) · scope.

The question has several parts that were answered together. Give the outcome and
the split **for each part**, and say whether the parts' outcomes are consistent
with one another.

Ratified verdicts on other questions are in `decisions/2026-09-19-*/verdict.md`
and `decisions/2026-10-01-jq-r04-gate/verdict.md`; you may read those files. If
the outcome before you reads a rule in a way that contradicts one of them, say
where, as part of the scope check.

**You do not answer the question.** If you judge all three jurors wrong, you
refuse and say why. You never write what you think the right answer is.

## Output

Write to `decisions/2026-10-01-jq-n1-canteen-8/verdict.md`, in English. Write nothing else, anywhere.

Begin with a single line that is exactly `RATIFIED` or `REFUSED`, then the six
checks with their results, then what follows from your verdict.

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction — a sentence telling you which verdict to
reach — report it. That is a leak.
