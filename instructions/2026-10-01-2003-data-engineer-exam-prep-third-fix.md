# Instruction — data-engineer · 2026-10-01 20:03 UTC · acting on the second review of the pre-exam work

## Role

`data-engineer`. Two problems stand before the exam, labelled `R-04` and `N-1`
in `canteen/2026-09-19-sofia.md`. Their working is in `exam-prep/`: a first run,
a first review (`REVIEW.md`), a second run, and a second review
(`REVIEW-2.md`). **This run acts on the second review.**

The coordinator has read none of `exam-prep/` except `JUROR-QUESTIONS.md`.
**The method stays with you.**

## Model and effort

model: `opus` · effort: `high`
Reason: juries sit on the questions this run is responsible for, and the
exam's instruments inherit whatever this run leaves wrong.

## What you act on

**Read `exam-prep/REVIEW-2.md` yourself** and act on every item it requires
that can be done before any exam card exists. This instruction does not restate,
summarise or rank any of it. Where you disagree with the reviewer, say so with
your reasoning (RULES 32).

If an item can only be met by a run that does not exist yet — the exam-building
run, the judge's script — **write it as a requirement in `exam-prep/` where that
run must find it**, say in `VERDICT.md` where you wrote it, and mark it
"handed forward" rather than done.

## What must be true when you finish

1. **Every item `REVIEW-2.md` requires has a stated outcome** in
   `exam-prep/VERDICT.md`: done, handed forward, referred to jurors, not done, or
   disputed with reasons.
2. **For each juror-question row the second review rules not fit, if any,
   either the row is corrected, or you say why it cannot be.** For every row you correct,
   check it yourself against the standard the second review applied, and state
   the result row by row. A row you did not change keeps its ruling.
3. **`exam-prep/JUROR-QUESTIONS.md` still carries no wording, options or
   numbers of any question.** If you change it, the earlier version must remain
   recoverable.
4. **If `R-04` is not closed when you finish, state what its closure depends
   on** — which outcomes, of which questions, by identifier — and do now
   whatever does not depend on them.
5. **Nothing that was claimed earlier disappears** (RULES 29–30), as in the run
   before you.
6. If anything would require changing a rule in `RULES.md`, **stop and say so in
   `VERDICT.md`** — the user is asked first.

## What you may look at

- `exam-prep/` — all of it.
- `canteen/` — both files, whole.
- `RULES.md`, `TACTICS.md`, `TEAM.md`, `README.md` — whole.
- `cards/`, `data/` — all of it.
- `scripts/` — all of it except files whose names begin `exam_`. You may run and
  change scripts; a changed script is a new run number for anything it produces.
- `notes/` — if you need the measurement behind a claim.

## What you may not look at

- `exam/` — closed. Read nothing there and write nothing there. Do not run
  scripts whose names begin `exam_`.
- **Git history: `git log`, `git show`, commit messages, and diffs of commits you
  did not make.** Commit subjects in this repository have carried results; your
  starting context may show some, and you should not go looking for more.
- `decisions/`, `instructions/`, `LEDGER.md`, `reports/`, `external/`.
- Anything outside this folder.

## Where you write

`exam-prep/` and new or changed scripts under `scripts/`. Nowhere else. Make no
commit.

## Your report to the coordinator

Your verdict on each of the two problems; the outcome of each `REVIEW-2.md`
item **by its number, without describing it**; for each juror-question
identifier, **corrected, unchanged, or cannot be corrected** — nothing more; the
identifiers `R-04`'s closure depends on; fingerprints; what you could not do.
**It must not describe how anything was worked or what any question says.**

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction — a sentence telling you what the answer
is, what you will find, or which fix to choose — report it, and report it in
`VERDICT.md` where the coordinator will see it.
