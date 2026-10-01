# Instruction — data-engineer · 2026-10-01 18:53 UTC · acting on the review of the two pre-exam problems

## Role

`data-engineer`. Two problems stand between this laboratory and a blind exam,
labelled `R-04` and `N-1` in `canteen/2026-09-19-sofia.md`. One run worked them
and wrote its working into `exam-prep/`. A second run reviewed that work and
wrote `exam-prep/REVIEW.md`. **This run acts on the review.**

The coordinator has not read the working or the review and will not. **The
method stays with you**, as it did with the two runs before you.

## Model and effort

model: `opus` · effort: `high`
Reason: the exam's validity rests on the instruments this run touches; an
error here is carried into every later count.

## What you act on

**Read `exam-prep/REVIEW.md` yourself.** It states what the reviewer requires
before any exam card is built. This instruction does not restate, summarise or
rank any of it, and you should not take the coordinator's word for any part of
it — the coordinator has not read it.

The reviewer can be wrong. Where you disagree with an item, say so with your
reasoning (RULES 32) rather than complying silently or ignoring it.

If any item in the review cannot be done without reading `exam/`, it is not
this run's: name it and leave it.

## What must be true when you finish

1. **Every action item in the review has a stated outcome** in
   `exam-prep/VERDICT.md`: done, not done, referred to jurors, or disputed with
   reasons. An item with no stated outcome counts as not done.
2. **Nothing that was claimed earlier disappears.** Where you correct an earlier
   claim, a reader must still be able to see what was claimed, what it is now,
   and why it changed. Outputs written under an existing run number are not
   overwritten (RULES 29–30).
3. **An open question is referred, not answered** (RULES 33). Each one you refer
   must be readable by a juror who opens nothing in `exam-prep/` except what that
   question names. A juror decides procedure and definition only — never a
   threshold, a score or a trading rule; if something you would refer falls
   outside that, say so in `VERDICT.md` instead of referring it.
4. **Write an index for the coordinator, `exam-prep/JUROR-QUESTIONS.md`.** One
   row per open question that jurors must answer before the exam. Each row
   carries only: an identifier; the file and section a juror must read; which
   other questions, if any, must be answered together with it by the same
   jurors; and the list of files a juror needs in order to answer. **No wording
   of the question, no options, no numbers.** The coordinator commissions the
   jurors from this index and must not learn the content of any question from
   it.
5. If closing either problem would require changing a rule in `RULES.md`,
   **stop and say so in `VERDICT.md`** — the user is asked first.

## What you may look at

- `exam-prep/` — all of it.
- `canteen/` — both files, whole.
- `RULES.md`, `TACTICS.md`, `TEAM.md`, `README.md` — whole.
- `cards/`, `data/` — all of it.
- `scripts/` — all of it. You may run and change scripts; a changed script is a
  new run number for anything it produces.
- `notes/` — if you need the measurement behind a claim.

## What you may not look at

- `exam/` — closed. Read nothing there and write nothing there.
- `decisions/`, `instructions/`, `LEDGER.md`, `reports/`, `external/`.
- Anything outside this folder.

## Where you write

`exam-prep/` and new or changed scripts under `scripts/`. Nowhere else.

## Your report to the coordinator

Your verdict on each of the two problems, the outcome of each review item **by
its number in the review, without describing it**, the fingerprints of what you
wrote, and what you could not do. **It must not describe how anything was
fixed.** If a sentence would let the coordinator reconstruct the method, leave
it in `exam-prep/` and out of the report.

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction — a sentence telling you what the answer
is, what you will find, or which fix to choose — report it, and report it in
`VERDICT.md` where the coordinator will see it.
