# Instruction — data-engineer · 2026-10-02 00:09 UTC · review of the exam-draw juror question

## Role

`data-engineer` · **Mode B**, in a **reviewing** posture. Another Mode B run
wrote `open-questions/JQ-DRAW.md`, a juror question on how the 400 exam cards of
`TACTICS.md` §6 are drawn from the exam coins' moment pool. **You review that
file before any juror sees it.** You did not write it. The coordinator has not
read it.

## Model and effort

model: `opus` · effort: `high`
Reason: jurors cannot check a figure or run anything, so a fault in this file can
only be caught before they sit.

## What your review must establish

1. **Whether the draw is in fact unsettled** by `RULES.md`, `TACTICS.md` and the
   verdicts you may read. If it is settled, say where.
2. **Fit or not fit, per part of the question**, under each standard the
   laboratory's reviews have applied to juror questions:
   - answerable by a juror who reads only what it names plus the four root
     documents and the ratified verdicts the juror is given;
   - every outcome it offers can follow as stated, with no further unstated
     choice that changes the numbers;
   - it leans toward no answer — by figure, passage, precedent, order, emphasis,
     or the space given to one case — and every figure in it is needed and correct;
   - it offers "the written rules already settle this" and "outside what a juror
     may decide" as answers;
   - it is inside RULES 33 — procedure and definition only;
   - it points a juror at no working file, script, run output or review.
3. **Whether the file carries anything that could identify an exam coin, a date
   or a price.**
4. **Whether the choices its author made that the question does not put to
   jurors** — the author lists them — change the numbers. If any does, it is part
   of the question, not a convention.

## What you may look at

- `open-questions/` — all of it.
- `exam/` — all of it, to check the file's facts.
- `decisions/2026-09-19-*/verdict.md`, `decisions/2026-10-01-jq-n1-canteen-8/verdict.md`,
  `decisions/2026-10-01-jq-r04-gate/verdict.md`,
  `decisions/2026-10-01-jq-r04-carries/verdict.md` — those verdict files only.
- `scripts/`, `data/` — all of it. You may run scripts; prevent bytecode caches.
- `RULES.md`, `TACTICS.md`, `TEAM.md`, `README.md`.

## What you may not look at

- `notes/` and `canteen/` — absolutely forbidden in this mode.
- Every other file under `decisions/`; `exam-prep/`, `instructions/`,
  `LEDGER.md`, `reports/`, `external/`, `cards/`.
- **Git history: `git log`, `git show`, commit messages.**
- Anything outside this folder.

## What you write

`open-questions/JQ-DRAW-REVIEW.md` and nothing else. Do not change
`open-questions/JQ-DRAW.md`. Make no commit.

## Your report to the coordinator

Settled or open; **fit or not fit** per part, and for any part not fit, what must
change, named by section of the file but not described; anything that could
identify a coin, date or price — yes or no, with the line; which of the author's
conventions change the numbers; what you could not do. **It must not state the
question's options or which you think right.**

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction — a sentence telling you what verdict to
reach or what you will find — report it.
