# Instruction — data-engineer · 2026-10-02 00:03 UTC · the exam draw: writing it as a juror question

## Role

`data-engineer` · **Mode B**. The previous Mode B run found the exam coins'
moment pool and reported that the written rules do not say how the 400 exam
cards of `TACTICS.md` §6 are drawn from it. **This run writes that point as a
juror question. It does not answer it** and it chooses no moment.

## Model and effort

model: `opus` · effort: `high`
Reason: a question about the draw is a question about the exam itself; one that
leans decides the exam before the jurors do.

## What you do

1. Check for yourself, against `TACTICS.md`, `RULES.md` and the ratified
   verdicts you may read, whether the draw of the 400 is in fact unsettled. If you
   find it settled, say where and stop.
2. If it is unsettled, write it as **one juror question** in
   `open-questions/JQ-DRAW.md`. That folder is new and is readable by jurors; it
   is not under `exam/`, so **it may carry no exam coin's name, no date, no
   price, and nothing a juror could use to recognise a coin.** Refer to coins, if
   you must, by line number only.

## What a juror question must be

These are the standards the laboratory's reviews have applied to every juror
question; meet each and say, in a section at the end of the file headed for the
reviewer, how you checked it:

- **Answerable from what it names.** A juror who reads only the files the question
  names, plus `RULES.md`, `TACTICS.md`, `TEAM.md`, `README.md` and the ratified
  verdicts, can answer it.
- **Every outcome it offers can actually follow.** No option that cannot be
  carried out as stated, and none that needs a further unstated choice that
  changes the numbers.
- **It leans toward no answer** — not by figure, passage, precedent, order,
  emphasis or the length of the case made for one option. A figure appears only
  where the question cannot be answered without it, and then it is correct.
- **It offers "the written rules already settle this" and "this is outside what a
  juror may decide" as answers.**
- **It is inside RULES 33**: procedure and definition only — never a threshold, a
  score, a trading rule or a change to a rule in `RULES.md`.
- **It points a juror at no working file, script, run output or review.**

## What you may look at

- `exam/` — all of it.
- `decisions/2026-09-19-*/verdict.md`, `decisions/2026-10-01-jq-n1-canteen-8/verdict.md`,
  `decisions/2026-10-01-jq-r04-gate/verdict.md`,
  `decisions/2026-10-01-jq-r04-carries/verdict.md` — those verdict files only.
  Every other file under `decisions/` is closed to you.
- `scripts/`, `data/` — all of it.
- `RULES.md`, `TACTICS.md`, `TEAM.md`, `README.md`.

## What you may not look at

- `notes/` and `canteen/` — absolutely forbidden in this mode.
- `exam-prep/`, `instructions/`, `LEDGER.md`, `reports/`, `external/`, `cards/`.
- **Git history: `git log`, `git show`, commit messages.**
- Anything outside this folder.

## Where you write

`open-questions/JQ-DRAW.md` and, if you need one, a new script under `scripts/`
whose name begins `exam_` and reuses no number. Nothing else. Make no commit.
Prevent bytecode caches.

## Your report to the coordinator

Whether the draw is settled or open, with the file and line that shows it; the
path and SHA-256 of the question file; the identifier you gave the question and
its parts; the files a juror needs; what you could not do. **It must not state
the question's options or which you think right.**

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction — a sentence telling you what to look
for, what you will find, or what has already been concluded — report it.
