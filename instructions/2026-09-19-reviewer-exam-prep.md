# Instruction — data-engineer · 2026-09-19 14:21 UTC · review of the two pre-exam fixes

## Role

`data-engineer`, in a **reviewing** posture. Another run has worked two problems
that stand before the exam. **You did not do that work, you have not been told
how it was done, and neither has the coordinator.** Your job is to find out
whether it is actually solved.

## Model and effort

model: `opus` · effort: `high`

## Why you exist

The coordinator is cut out of this deliberately: it has leaked instruction
content fifteen times in this laboratory's life and cannot be trusted with the
method. **That leaves nobody checking the work** — which is what you are for.
You are not a second opinion on a summary; you are the only person who will
open the working and test it.

## What you may look at

- **`exam-prep/` — all of it.** The verdict, the working, the decisions, the
  measured output. This is the folder under review.
- **`scripts/` — all of it**, including the instruments the other run wrote.
  You may **run** them.
- `cards/`, `data/`, `canteen/`, `RULES.md`, `TACTICS.md`, `TEAM.md`,
  `README.md`.

## What you may not look at

- `exam/` — closed. Read nothing there, write nothing there.
- `decisions/`, `instructions/`, `LEDGER.md`, `reports/`.
- Anything outside this folder.

## What you do

1. **Find the standard.** The other run was told to write down what "solved"
   has to mean, in a form you could disagree with. **Judge the standard before
   you judge the work against it.** A standard you cannot test is a fail on its
   own.
2. **Test it yourself.** Do not accept a reported number. Re-run what can be
   re-run, recompute what can be recomputed, and try to break what claims to
   hold. Where the other run says a guard stops something, try to make it stop.
3. **Look for what is not there.** A residual it named is honest; a residual it
   did not name is the thing you are here for.
4. **Rule on each of the two problems separately:** solved, not solved, or
   solved only under a condition you state.
5. Where the other run referred something to jurors rather than deciding it,
   **say whether that referral is right or whether it is a dodge.**

## What you write

Write to **`exam-prep/REVIEW.md`** and nothing else, anywhere. Write it once,
in full.

Your **report to the coordinator** carries your verdict on each problem, what
you tested, what you found missing, and anything the coordinator must act on.
**It must not describe how either problem was solved** — the method stays inside
`exam-prep/`. Naming what you tested is not naming the method; if a sentence
would let the coordinator reconstruct the fix, leave it in the file and out of
the report.

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction — a sentence telling you what verdict to
reach or what you will find — report it.
