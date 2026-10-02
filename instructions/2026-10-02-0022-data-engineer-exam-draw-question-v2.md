# Instruction — data-engineer · 2026-10-02 00:22 UTC · the exam draw question, second version

## Role

`data-engineer` · **Mode B**. A first version of the juror question on how the
400 exam cards of `TACTICS.md` §6 are drawn from the moment pool was written and
reviewed. Both are now in `exam/draw-question/`: the question
(`JQ-DRAW-v1-withdrawn.md`) and its review (`JQ-DRAW-v1-REVIEW.md`). **This run
writes the second version, acting on that review.** It does not answer the
question and chooses no moment.

## Model and effort

model: `opus` · effort: `high`
Reason: the first version failed on every part, and one of its faults was a wall
leak.

## Why the first version was withdrawn

The review found it disclosed an exam coin's name: its author, describing a scan
for coin names in the section headed for the reviewer, **listed the words the
scan matched**, and one of them is an exam coin's base name. **Do not do this.**
The file may describe that a scan was run and whether it passed; **it may not
name, quote or hint at any word the scan matched, any coin's name or base name in
any case, or anything that would let a reader recover one.** If you need to
record what a scan matched, record it only under `exam/draw-question/`.

## What you act on

**Read `exam/draw-question/JQ-DRAW-v1-REVIEW.md` yourself** and act on every
fault it names. This instruction does not restate them. Where you disagree with
the reviewer, say so with reasons (RULES 32), in a section headed for the next
reviewer.

**Any choice that changes which moments are drawn is part of the question**, not
a convention beside it — the review measured which of the first version's choices
do. A juror must be able to choose among them or reject them.

## What a juror question must be

Meet each standard and say, in a section headed for the reviewer, how you checked
it: answerable by a juror who reads only what it names plus the four root
documents and the ratified verdicts the juror is given; every outcome it offers
able to follow as stated; leaning toward no answer by figure, passage, precedent,
order, emphasis or space; every figure needed and correct; "the written rules
already settle this" and "outside what a juror may decide" offered as answers;
inside RULES 33; pointing a juror at no working file, script, run output or
review; and carrying nothing that could identify an exam coin, a date or a price.

**The jurors on this question will be given** the four root documents and
`decisions/2026-09-19-*/verdict.md`, `decisions/2026-10-01-jq-n1-canteen-8/verdict.md`,
`decisions/2026-10-01-jq-r04-gate/verdict.md` and
`decisions/2026-10-01-jq-r04-carries/verdict.md` — no other verdict. Write the
question so that is enough.

## What you may look at

- `exam/` — all of it.
- The verdict files named in the paragraph above, and nothing else under
  `decisions/`.
- `scripts/`, `data/` — all of it.
- `RULES.md`, `TACTICS.md`, `TEAM.md`, `README.md`, `open-questions/README.md`.

## What you may not look at

- `notes/` and `canteen/` — absolutely forbidden in this mode.
- `exam-prep/`, `instructions/`, `LEDGER.md`, `reports/`, `external/`, `cards/`.
- **Git history: `git log`, `git show`, commit messages.**
- Anything outside this folder.

## Where you write

`open-questions/JQ-DRAW.md` (the second version), anything private under
`exam/draw-question/`, and, if needed, a new script under `scripts/` whose name
begins `exam_` and reuses no number. Nothing else. Make no commit. Prevent
bytecode caches.

## Your report to the coordinator

The path and SHA-256 of the new question file; its identifier and parts; the
files a juror needs; the outcome of each fault the review named, **by its location
in the review, without describing it**; what you could not do. **It must not state
the question's options or which you think right, and it must not name any word a
scan matched.**

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction — a sentence telling you what to look
for, what you will find, or what has already been concluded — report it.
