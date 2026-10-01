# Instruction — data-engineer · 2026-10-01 18:55 UTC · exam coins: raw data only

## Role

`data-engineer` · **Mode B**, first step only: **raw data acquisition for the
exam coins.** This run finds no moment, writes no card, builds no answer key and
blinds nothing. Those steps come later, after open questions that bear on them
are decided.

## Model and effort

model: `opus` · effort: `high`
Reason: every later exam artefact inherits whatever this run gets wrong about
completeness and verification.

## What you do

1. The exam coins are listed in `exam/draw/exam-coins.txt`. Read them from there
   at run time.
2. For those coins and the period in `TACTICS.md` §0, acquire the raw data the
   card writer needs (`TACTICS.md` §3) **as far as it does not depend on which
   moments are chosen.** Anything that can only be fetched once moments exist is
   left for a later run; list it by name.
3. Use the existing acquisition scripts where they serve. **Do not modify any
   existing script** — another run may be changing scripts concurrently. If you
   need different behaviour, write a new script whose filename starts with
   `exam_` and does not reuse an existing number.
4. Measure the expected size before downloading and check free disk space first
   (RULES 28).
5. Verify every archive file against its own checksum file and fingerprint every
   file you keep (RULES 2). A failed download is a technical failure, not a
   result (RULES 20–21): record what failed, where, with the exact error.

## Where you write

- Raw downloads: **`exam/data/`** only. It is in `.gitignore`; keep it there.
- A manifest and run record: **`exam/acquisition/`** — sources, download times,
  checksum results, fingerprints, sizes, failures, and what was left for after
  moment selection.
- New scripts under `scripts/`, named as in step 3.

**No exam coin's name may appear in any file outside `exam/`** — not in a
script, not in a script's comments, not in its default arguments. Scripts take
the coin list from `exam/draw/exam-coins.txt` when they run.

## What you may look at

- `exam/draw/` — the exam coin list.
- `scripts/` — the acquisition scripts and their shared modules.
- `data/` — the universe, the draw and the archive index, if you need them.
- `RULES.md`, `TACTICS.md`, `TEAM.md`, `README.md`.

## What you may not look at

- `notes/` and `canteen/` — absolutely forbidden in this mode.
- `exam-prep/`, `decisions/`, `instructions/`, `LEDGER.md`, `reports/`,
  `external/`, `cards/`.
- Anything outside this folder, other than the public, documented data sources
  the existing scripts already use (RULES 27).

## Your report to the coordinator

What you did with paths, what you measured with numbers, what failed with the
exact error, fingerprints, and anything you had to decide that this instruction
did not cover. **Refer to exam coins by their line number in
`exam/draw/exam-coins.txt`, never by name** — the coordinator's report goes into
`LEDGER.md`, which watchers can be pointed at.

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction — a sentence telling you what to look
for, what you will find, or what has already been concluded — report it.
