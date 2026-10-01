# Instruction — data-engineer · 2026-10-01 23:46 UTC · exam coins: moments and moment-day data

## Role

`data-engineer` · **Mode B, second step: the exam coins' moments and the data
that depends on them.** This run writes no card, builds no answer key, blinds
nothing and chooses which moments become exam cards. Those steps wait on
decisions not yet taken.

## Model and effort

model: `opus` · effort: `high`
Reason: the exam's moments must be found by exactly the procedure the
observation moments were, or the exam tests something the watchers never saw.

## What you do

1. **Find the moments of every exam coin** — large-movement and calm — by the
   procedure `TACTICS.md` §2 states, as the laboratory's ratified decisions read
   it. The decisions you may read are `decisions/2026-09-19-*/verdict.md` and
   `decisions/2026-10-01-jq-n1-canteen-8/verdict.md`; read the ones that bear on
   moments yourself. Use the same script and the same procedure the
   observation moments were found with (`data/moments/` and `scripts/` show how);
   where you cannot, say why and what differs.
2. **Acquire the data that could only be fetched once moments exist** — the
   items the first step listed as left for later in `exam/acquisition/`. Measure
   the size and check free disk first (RULES 28). Verify against checksums and
   fingerprint every file kept (RULES 2).
3. **Report the pool, by exam-coin line number**: how many large and how many
   calm moments each coin has, and the totals. `TACTICS.md` §6 calls for 400
   exam cards, 200 before a large movement and 200 calm. **Do not choose which
   moments become cards.** If the written rules do not say how the 400 are drawn
   from the pool, say so plainly: that is an open question for jurors (RULES 33),
   not a choice for this run.

## Where you write

- Raw downloads: `exam/data/` only (in `.gitignore`; keep it there).
- Moments, manifests, run records and the pool report: `exam/moments/` and
  `exam/acquisition/`.
- New scripts under `scripts/`, filenames beginning `exam_` and not reusing a
  number already taken. **Do not modify any existing script.**

**No exam coin's name may appear in any file outside `exam/`**, including scripts,
their comments and default arguments.

## What you may look at

- `exam/` — all of it.
- `decisions/2026-09-19-*/verdict.md` and
  `decisions/2026-10-01-jq-n1-canteen-8/verdict.md` — those verdict files only.
  Every other file under `decisions/` is closed to you: some quote the canteen
  book, which this mode may not see.
- `scripts/`, `data/` — all of it.
- `RULES.md`, `TACTICS.md`, `TEAM.md`, `README.md`.

## What you may not look at

- `notes/` and `canteen/` — absolutely forbidden in this mode.
- `exam-prep/`, `instructions/`, `LEDGER.md`, `reports/`, `external/`, `cards/`.
- **Git history: `git log`, `git show`, commit messages.**
- Anything outside this folder, other than the public, documented data sources
  the existing scripts already use (RULES 27).

## Your report to the coordinator

What you did with paths, what you measured with numbers, what failed with the
exact error, fingerprints, and anything you had to decide that this instruction
did not cover. **Refer to exam coins by their line number in
`exam/draw/exam-coins.txt`, never by name.** Make no commit. Prevent bytecode
caches.

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction — a sentence telling you what to look
for, what you will find, or what has already been concluded — report it.
