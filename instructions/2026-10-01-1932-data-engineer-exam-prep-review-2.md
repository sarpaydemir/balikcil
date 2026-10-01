# Instruction — data-engineer · 2026-10-01 19:32 UTC · review of the second pre-exam fix

## Role

`data-engineer`, in a **reviewing** posture. Two problems stand before the exam,
labelled `R-04` and `N-1` in `canteen/2026-09-19-sofia.md`. A first run worked
them, a first review (`exam-prep/REVIEW.md`) ruled on that work, and a second run
acted on the review. **You review the second run.** You did not do that work and
have not been told how it was done; neither has the coordinator, who has read
none of `exam-prep/` except the juror-question index.

## Model and effort

model: `opus` · effort: `high`
Reason: you are the only check on work the coordinator is deliberately not shown.

## What you may look at

- `exam-prep/` — all of it.
- `scripts/` — all of it. You may **run** scripts; write any output of your own
  under `exam-prep/review-2/`, never into another run's directory.
- `cards/`, `data/`, `canteen/`, `RULES.md`, `TACTICS.md`, `TEAM.md`,
  `README.md`.

## What you may not look at

- `exam/` — closed. Read nothing there, write nothing there. Scripts under
  `scripts/` whose names begin `exam_` belong to a separate run that is working
  now; do not run them.
- `decisions/`, `instructions/`, `LEDGER.md`, `reports/`, `external/`.
- Anything outside this folder.

## What your review must establish

1. **A ruling on each problem separately:** solved, not solved, or solved only
   under a condition you state.
2. **For each outcome the second run states against the first review's items,
   whether it holds** — established by re-running or recomputing where that is
   possible, not by reading the claim. Where the second run disputes the first
   review, say which side the material supports.
3. **For each row of `exam-prep/JUROR-QUESTIONS.md`, whether it is fit to be put
   to jurors as written.** A question is fit when a juror reading only the files
   its row names can answer it; when every outcome it offers can actually follow
   from the instrument or rule it is about; when its wording does not lean toward
   one answer; and when it is inside what a juror may decide under RULES 33.
   For each row that is not fit, say what must change — in `exam-prep/`, not in
   your report.
4. **Whether `exam-prep/JUROR-QUESTIONS.md` itself carries any content of a
   question** — wording, options or numbers. The coordinator commissions jurors
   from it and must not learn a question's content from it.

## What you write

`exam-prep/REVIEW-2.md`, plus any outputs of your own under
`exam-prep/review-2/`. Nothing else, anywhere. Do not edit another run's files.

## Your report to the coordinator

Your ruling on each problem; for each juror-question identifier, **fit or not
fit**, nothing more; what you tested, named but not described; what the
coordinator must act on; and what you could not do. **It must not describe how
either problem was worked or what any juror question says.** If a sentence would
let the coordinator reconstruct the method or a question, leave it in
`exam-prep/` and out of the report.

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction — a sentence telling you what verdict to
reach or what you will find — report it.
