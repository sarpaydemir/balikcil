# Instruction — data-engineer · 2026-10-01 22:51 UTC · acting on the fifth review, DATE and CONTENT rows only

## Role

`data-engineer`. Two problems stand before the exam, labelled `R-04` and `N-1`
in `canteen/2026-09-19-sofia.md`. Their working is in `exam-prep/`: five runs
and five reviews. **This run acts on `exam-prep/REVIEW-5.md` as it concerns the
`JQ-R04-DATE` and `JQ-R04-CONTENT` rows**, and on nothing else.

The coordinator has read none of `exam-prep/` except `JUROR-QUESTIONS.md`, the
withdrawn row's statement, and the section of `VERDICT.md` addressed to it.
**The method stays with you.**

## Model and effort

model: `opus` · effort: `high`
Reason: one jury waits on the files this run corrects.

## A jury is sitting while you work, and one verdict is ratified

- Three jurors are answering the `JQ-N1` group with `JQ-CANTEEN-8` now, from
  `exam-prep/fifth-fix/juror-questions/JQ-N1.md` (SHA-256
  `071bf434f05cfc7e83b87b7698274f609a5bf28334b956fec95e64b50709497e`) and
  `exam-prep/fifth-fix/juror-questions/JQ-CANTEEN-8.md` (SHA-256
  `944c5d85ee547e93ae55ac8d5f10dab05bc5ebe593b3de03d9b092b40aa8d396`). **Do not
  change either file or anything those jurors are pointed at.**
- `JQ-R04-GATE` is ratified: `decisions/2026-10-01-jq-r04-gate/verdict.md`. It
  binds this run. Its question file is not to be changed.

## A sentence of the coordinator's withdrawn

The fifth run's instruction said: *"Write it as a juror question in the group
it bears on."* Where that sentence conflicts with a review's ruling on which rows
are answered together, **the coordinator withdraws it: the reviews' rulings on
couplings govern.** It was a default of the coordinator's, written without
reading any juror file, and it has no standing against a reviewer's reasoned
ruling.

## What you act on

**Read `exam-prep/REVIEW-5.md` yourself** and act on what it requires of the
DATE and CONTENT rows. This instruction does not restate any of it. Where you
disagree, say so with reasons (RULES 32).

If a point must be answered before a group can be, and it is a choice that
changes the numbers which no written rule settles, **it is an open question
(RULES 33)**: write it as a juror question that is answered **before** that group
sits, and make the order plain in the index.

## What must be true when you finish

1. **Every item `REVIEW-5.md` requires of the DATE and CONTENT rows has a stated
   outcome** in `exam-prep/VERDICT.md`.
2. **Every DATE or CONTENT row still to be commissioned meets every test the five
   reviews applied.** State the result row by row.
3. **No juror file or reading list points a juror at a review, `VERDICT.md`,
   `HANDED-FORWARD.md` or any working file**, including in headers, and no list
   gives more of a file than the question needs.
4. **The index carries no wording, options or numbers of any question**, shows
   each row's true status and the order in which groups must sit, and its earlier
   versions remain recoverable.
5. **Nothing claimed earlier disappears** (RULES 29–30).
6. If anything would require changing a rule in `RULES.md`, **stop and say so in
   `VERDICT.md`**.

## What you may look at

- `exam-prep/` — all of it.
- `decisions/2026-10-01-jq-r04-gate/verdict.md` — and nothing else under
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

The outcome of each `REVIEW-5.md` item you acted on, **by its number, without
describing it**; for each juror-question identifier, **corrected, added,
unchanged, or cannot be corrected**; the order in which the remaining groups must
sit, by identifier; fingerprints; what you could not do. **It must not describe
how anything was worked or what any question says.**

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction — a sentence telling you what the answer
is, what you will find, or which fix to choose — report it, and report it in
`VERDICT.md` where the coordinator will see it.
