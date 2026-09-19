# Instruction — data-engineer · 2026-09-19 13:42 UTC · the two problems before the exam

## Role

`data-engineer`. Two problems stand between this laboratory and a blind exam.
The user has ordered both solved before any exam card is built. **You solve
them. The coordinator does not, and the coordinator is not told how.**

## Model and effort

model: `opus` · effort: `high`

## Why you are not to tell the coordinator how

The coordinator has written fifteen separate leaks into instructions in this
laboratory's short life - a decision handed to a jury before it ruled, a
watcher's result carried into an instruction for an agent forbidden that
folder, an answer stated inside the question. Every one was caught by the agent
receiving it, none by the coordinator writing it.

**So the method stays with you.** Your report says whether each problem is
solved, where the work is, its fingerprints, and what you could not do. **It
must not say how.** A reviewer who has also not been told will check your work
afterwards.

## The two problems

Both are stated in `canteen/2026-09-19-sofia.md` and
`canteen/2026-09-19-viktor.md`, in their own words, with the card numbers and
measurements behind them. **Read them there.** They are labelled `R-04` and
`N-1` in Sofia's book.

Neither watcher, chair nor skeptic proposed a fix; they measured the problems
and stopped, correctly. Fixing is yours.

## What you may look at

- `canteen/` - both files, whole.
- `RULES.md`, `TACTICS.md`, `TEAM.md`, `README.md` - whole.
- `cards/`, `data/` - all of it, including `data/overlap/`.
- `scripts/` - your own scripts.
- `notes/` - the 42 watcher files, if you need the measurement behind a claim.

## What you may not look at

- `exam/` - closed. **Read nothing there and write nothing there.** Building
  exam cards is a separate run in a separate mode; this run prepares the ground
  and touches no exam artefact.
- `decisions/`, `instructions/`, `LEDGER.md`, `reports/`.
- Anything outside this folder.

## Where you write

**`exam-prep/` and nowhere else**, plus any new script under `scripts/`.

`exam-prep/` is closed to every other role in this laboratory and to the
coordinator. Put in it whatever a later run needs in order to build a blind
exam and to count events correctly - the working, the decisions, the
measurements, the tests you ran, in as much detail as you like. **Nobody will
trim it.**

Write one file `exam-prep/VERDICT.md` that states, for each of the two
problems, **solved or not solved**, and nothing about the method. That file is
the only one the coordinator will read.

## What "solved" has to mean

You decide, and you write your standard into `exam-prep/` where the reviewer can
disagree with it. A standard the reviewer cannot test is not a standard.

If solving either problem would require changing a rule in `RULES.md`, **stop
and say so in the verdict file** - the user is asked first and has not been
asked about that.

## Rules that bind this run

RULES 2 and 29-30 on fingerprints and append-only records; RULES 19-23 on what
may be written down; RULES 6 - whatever you fix, fix it before any exam card
exists, not after a result.

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction - a sentence telling you what the answer
is, what you will find, or which fix to choose - report it, and report it in the
verdict file where the coordinator will see it.
