# Instruction — data-engineer · 2026-09-19 06:15 UTC · moments and cards

## Role

`data-engineer` · **Mode A (data and cards)**. The universe and the draw are
done (run number `e458f643863ed84e`). This run finds the moments for the **10
observation coins** and writes their cards. No watcher has run yet and no card
exists.

## Model and effort

model: `opus` · effort: `high`

Reason: the card is the only thing every watcher will ever see. A field that is
silently empty, a unit that is silently wrong, or an "after" section that
leaks into the "before" section cannot be caught downstream — the watchers will
simply believe the card.

## What you may look at

- `TACTICS.md` — section **2 (moments)** and section **3 (the card)** are the
  specification for this run. Section 4 onward is later work.
- `RULES.md` — the whole file. RULES 16 and 19–21 and 28 bear on this run.
- `data/draw/observation-coins.txt` — the 10 coins this run is about.
- `data/universe/` — what the previous run downloaded and its manifest.
- `scripts/` — your own scripts from the previous run; reuse
  `lab_archive.py` rather than writing a second downloader.
- `README.md`, `TEAM.md`, `LEDGER.md`.
- The public Binance data archive and the other public, documented sources
  TACTICS 3 names. Use documented addresses; never guess a URL.

## What you may not look at

- `exam/` — **closed, read nothing.** This run writes nothing there either.
- `notes/`, `canteen/`, `reports/`, `instructions/` — not part of this run.
- Anything outside this folder. See Wall below.

## The task

### 1 · Disk first

TACTICS 3 says order book files are large and only the moment days are
downloaded. Measure free space before you start, estimate what you are about to
fetch, and write both down (RULES 28). **If it will not fit, stop and say so.**
Do not fill the disk and do not quietly drop a data source to make room — if
something has to be left out, that is a decision you report, not one you take.

### 2 · Moments

Implement TACTICS 2 exactly as written, for the 10 observation coins only:
large-movement moments, the 48-hour rule between them, the per-lifetime scaling
for a coin that did not trade all year, and the same number of calm moments at
least 72 hours away from any large movement. Randomness is seeded and the seed
is written down.

TACTICS 2 uses hourly closing prices, which this laboratory has not downloaded
yet. Fetch them the same way as before: from the archive, verified against the
`.CHECKSUM` companion, recorded in a manifest with source URL, download time
and SHA-256.

Write the moment list to `data/moments/` with, per moment: coin, start hour,
kind (large or calm), and the measured 24-hour move. This file is an input to
the cards, so fingerprint it.

### 3 · Cards

Implement TACTICS 3. One card per moment, two sections, **before** and
**after**. Every field TACTICS 3 lists, where the data exists.

Three things that decide whether these cards are usable at all:

- **Nothing from the "after" section may appear in the "before" section** — not
  a total, not an average, not a summary line computed over hours that had not
  happened yet. Check this in code and report the check.
- **An empty field and a missing field are different.** "This coin has no
  funding data for these hours" and "this field was never fetched" must read
  differently on the card (RULES 20). A card never implies a measurement that
  was not made.
- **Numbers are rounded and the card is short** (TACTICS 3). The card is read by
  a watcher, not by a machine.

For every source in TACTICS 3 that you could not reach: name it, name the error
you got, and name which cards are affected. A source that failed is reported as
failed, never as "no data" (RULES 20, 21).

Card numbers must be stable: the same input must always produce the same card
number. Write the numbering scheme down.

## Output

All output in English.

- `scripts/` — new scripts, standalone, resumable, header comment block, seeds
  fixed and written down.
- `data/moments/` — the moment list and its manifest.
- `data/` — whatever you downloaded, with the same per-file manifest discipline
  as the previous run.
- `cards/` — the cards for the 10 observation coins, plus a `cards/INDEX.md`
  giving the numbering scheme, the count of large and calm cards per coin, the
  fingerprint of each card file, and **a list, by name, of every field that is
  missing or empty and why**.

Then your five-part report: what you did with paths, what you measured with
numbers, what failed and the exact error, fingerprints, and anything you had to
decide that this instruction did not cover.

## Time and interruption

This is the longest run so far. Checkpoint it and start the long part so that it
survives the session closing (RULES 26). A partial result with an honest account
of where it stopped is worth more than a guess.

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

The instruction tells you what you may look at, never what to look for. If you
see a steer, a result, or a "pay attention to X" sentence in this instruction,
report it — that is a leak.
