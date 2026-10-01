# Instruction — data-engineer · 2026-10-01 23:57 UTC · `JQ-R04-CONTENT-d` back to jurors, and the index made true

## Role

`data-engineer`. **This run acts on `exam-prep/REVIEW-7.md`**, and on the items
of `exam-prep/REVIEW-6.md` that concern `JQ-R04-CONTENT-d` and were left open
when the seventh run withdrew that row.

The coordinator has read none of `exam-prep/` except `JUROR-QUESTIONS.md`, the
withdrawn row's statement, and the sections of `VERDICT.md` addressed to it. It
has not opened `exam-prep/USER-QUESTIONS.md`. **The method stays with you.**

## Model and effort

model: `opus` · effort: `high`
Reason: `R-04` cannot close until this row is settled.

## Where the row goes, and who decides that

Review 6 found the row's scope contested; the seventh run judged the whole row
outside a juror's scope and wrote it for the user; review 7 rules it a juror
question. **The coordinator does not settle this.** RULES 35 gives the scope
check to the referee: a referee who judges an outcome outside what a juror may
decide refuses it, and a question refused on scope goes to the user.

So the row goes to jurors. Write `JQ-R04-CONTENT-d` as a juror question that
meets every test the seven reviews applied, in which **"this is outside what a
juror may decide" is an answer a juror can give**. Mark U-1 in
`exam-prep/USER-QUESTIONS.md` as superseded by that route, keeping its text
(RULES 30), so that it can be returned to if the referee refuses on scope.

## Ratified verdicts that bind

`decisions/2026-10-01-jq-r04-gate/verdict.md`,
`decisions/2026-10-01-jq-n1-canteen-8/verdict.md`,
`decisions/2026-10-01-jq-r04-carries/verdict.md` and
`decisions/2026-10-01-jq-r04-date-content/verdict.md`. Read them yourself. A
juror file you write may point a juror at a ratified verdict's outcome; it must
not hand a juror any verdict's reasoning that quotes material the juror is not
otherwise allowed.

## What must be true when you finish

1. **Every item `REVIEW-7.md` requires, and every `REVIEW-6.md` item on this row
   left open, has a stated outcome** in `exam-prep/VERDICT.md`.
2. **`JQ-R04-CONTENT-d` meets every test the seven reviews applied**, stated test
   by test, and does not contradict any of the four ratified verdicts.
3. **The index shows each row's true status** — the four ratified groups as
   ratified, naming their verdict files — carries no wording, options or numbers
   of any question, and keeps its earlier versions recoverable.
4. **Whatever is handed forward can be checked yes or no** by the run that must
   meet it.
5. **Nothing claimed earlier disappears** (RULES 29–30).
6. If anything would require changing a rule in `RULES.md`, **stop and say so in
   `VERDICT.md`**.

## What you may look at

- `exam-prep/` — all of it.
- The four ratified `verdict.md` files above, and nothing else under
  `decisions/`.
- `canteen/` — both files, whole.
- `RULES.md`, `TACTICS.md`, `TEAM.md`, `README.md` — whole.
- `cards/`, `data/` — all of it.
- `scripts/` — all of it except files whose names begin `exam_`.

## What you may not look at

- `exam/` — closed. Do not run scripts whose names begin `exam_`.
- **Git history: `git log`, `git show`, commit messages, and diffs of commits you
  did not make.**
- The rest of `decisions/`, `instructions/`, `LEDGER.md`, `reports/`,
  `external/`, `notes/`.
- Anything outside this folder.

## Where you write

`exam-prep/` and new scripts under `scripts/`. Nowhere else. Make no commit.
Prevent bytecode caches.

## Your report to the coordinator

The outcome of each review item you acted on, **by its number, without
describing it**; the status of `JQ-R04-CONTENT-d` and of U-1; whether the index
is now true; fingerprints; what you could not do. **It must not describe how
anything was worked or what any question says.**

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction — a sentence telling you what the answer
is, what you will find, or which fix to choose — report it, and report it in
`VERDICT.md` where the coordinator will see it.
