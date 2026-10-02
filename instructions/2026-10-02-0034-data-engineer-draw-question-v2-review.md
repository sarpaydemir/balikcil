# Instruction — data-engineer · 2026-10-02 00:34 UTC · review of the exam-draw juror question, second version

## Role

`data-engineer` · **Mode B**, in a **reviewing** posture. The second version of
`open-questions/JQ-DRAW.md` has been written, acting on the review of the first
(`exam/draw-question/JQ-DRAW-v1-REVIEW.md`). Its author's notes for the reviewer
are in `exam/draw-question/`. **You review the second version before any juror
sees it.** You did not write it or the first review. The coordinator has not read
either version.

## Model and effort

model: `opus` · effort: `high`
Reason: jurors cannot check a figure or run anything, and the first version
leaked a coin's name.

## What your review must establish

1. **Fit or not fit, per part**, under each standard the laboratory's reviews have
   applied to juror questions: answerable by a juror who reads only what it names
   plus the four root documents and the verdicts the jurors will be given; every
   outcome able to follow as stated, with no unstated choice that changes the
   numbers; leaning toward no answer by figure, passage, precedent, order, emphasis
   or space; every figure needed and correct; "already settled" and "outside what a
   juror may decide" offered as answers; inside RULES 33; pointing at no working
   file, script, run output or review.
2. **Whether the file carries anything that could identify an exam coin, a date or
   a price** — including through ordinary words that are also a coin's base name,
   used in a way that links them to a coin.
3. **Whether each fault the first review named is resolved**, and whether the
   author's stated departures from the first review hold.
4. **Whether anything the author chose that the question does not put to jurors
   changes which moments are drawn.**

**The jurors will be given** the four root documents and
`decisions/2026-09-19-*/verdict.md`, `decisions/2026-10-01-jq-n1-canteen-8/verdict.md`,
`decisions/2026-10-01-jq-r04-gate/verdict.md` and
`decisions/2026-10-01-jq-r04-carries/verdict.md`, and nothing else beyond the
question file.

## What you may look at

- `open-questions/` and `exam/` — all of it.
- The verdict files named in the paragraph above, and nothing else under
  `decisions/`.
- `scripts/`, `data/` — all of it. You may run scripts; prevent bytecode caches.
  Never compute a draw with the number on `TACTICS.md` line 22.
- `RULES.md`, `TACTICS.md`, `TEAM.md`, `README.md`.

## What you may not look at

- `notes/` and `canteen/` — absolutely forbidden in this mode.
- Every other file under `decisions/`; `exam-prep/`, `instructions/`,
  `LEDGER.md`, `reports/`, `external/`, `cards/`.
- **Git history: `git log`, `git show`, commit messages.**
- Anything outside this folder.

## What you write

`exam/draw-question/JQ-DRAW-v2-REVIEW.md` and nothing else. Do not change the
question file. Make no commit.

## Your report to the coordinator

**Fit or not fit** per part, and for any not fit, what must change, named by
section but not described; on item 2, yes or no, with the line only; on items 3
and 4, by the first review's line references or the question's sections; what you
could not do. **It must not state the question's options or which you think
right, and it must not name any word a scan matched.**

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction — a sentence telling you what verdict to
reach or what you will find — report it.
