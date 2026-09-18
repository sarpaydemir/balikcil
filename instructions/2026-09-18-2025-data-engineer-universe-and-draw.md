# Instruction — data-engineer · 2026-09-18 20:25 UTC · universe and draw

## Role

`data-engineer` · **Mode A (data and cards)**. This is the laboratory's first
run: nothing has been downloaded and no agent has run before you. You build the
universe list for the period and you run the draw. You write no card in this
run.

## Model and effort

model: `opus` · effort: `high`

Reason: every number this laboratory later produces rests on this run's symbol
list and group assignment. An error here is silent and propagates to every
later step, and the archive's layout has to be read from its own documentation
rather than assumed.

## What you may look at

- `TACTICS.md` — sections **0 (period and universe)** and **1 (the draw)** are
  the specification for this run. Sections 2 onward describe later runs.
- `RULES.md` — the whole file.
- `README.md`, `TEAM.md`, `LEDGER.md` at the root.
- `data/`, `scripts/` — your working folders, currently empty.
- The public Binance data archive, `https://data.binance.vision`, and its
  documented listing interface. Use the documented address; never guess a URL.

## What you may not look at

- `notes/`, `canteen/`, `cards/` — empty, and not part of this run.
- `exam/` — you **read nothing** there. This run is the one exception to the
  folder being untouched: you **write** two files into `exam/draw/` (named
  under Output below) and nothing else. Do not create, read or list anything
  else under `exam/`.
- Anything outside this folder. See Wall below.

## The task

### 1 · Disk

Measure free disk space before downloading anything and record the measured
figure (RULES 28). If there is not enough room for what you are about to fetch,
stop and say so rather than filling the disk.

### 2 · Universe

Build the list of Binance USDT perpetual futures contracts (`futures/um`) that
traded at any point inside the period **2025-09-01 → 2026-08-31**, inclusive,
UTC.

- The list is built **from the archive**, not from the exchange's live symbol
  endpoint, so that contracts which stopped trading during the period are in it
  (TACTICS 0).
- For every file you download, record where it came from, when you downloaded
  it, and its SHA-256 (RULES 2).
- The archive publishes a `.CHECKSUM` companion for its files. **Verify each
  downloaded file against its own checksum file** and record the result. A file
  that fails verification is not silently dropped: it is recorded as a failure,
  by name.
- You need daily (`1d`) klines per symbol over the period for step 3. Download
  nothing else in this run — no order book, no funding, no 5-minute data. Those
  belong to later runs.

### 3 · Groups

Assign every symbol in the universe to exactly one of four groups
(TACTICS 1):

- **new** — the symbol's first trade in the archive falls inside the period.
- **large · mid · small** — everything else, by median daily trading volume
  over the period.

Two points of TACTICS 1 wording that the coordinator resolves here, so that you
do not have to decide them yourself:

1. **`new` is assigned first and is exclusive.** A symbol whose first trade
   falls inside the period is `new`, and is not also ranked into
   large/mid/small.
2. TACTICS 1 says the remaining symbols are "split into three by the median of
   daily trading volume". Implement that as: rank the remaining symbols by
   their median daily volume over the period and cut the ranked list into
   **three groups of equal size** (tertiles); where the count does not divide
   by three, the remainder goes to the lower-volume groups. Write down which
   volume column you used and the two cut values you computed.

State the cut values as measured numbers. Do not round them away.

### 4 · The draw

- **Draw number: `20260913`.** It is written in TACTICS 1, it was fixed before
  the draw, and it does not change. Use it as the random seed and write the
  seed into the output.
- Draw, without replacement and in this order:
  - **observation:** 10 symbols — 3 large · 3 mid · 2 small · 2 new
  - **exam:** 20 symbols from what remains — 6 large · 6 mid · 4 small · 4 new
  - **money test:** every symbol not drawn into the two groups above.
- The three sets must be disjoint. Verify that in code and report the check.
- If a group does not hold enough symbols to fill its quota, **stop and report
  it.** Do not substitute from another group on your own judgement.
- The draw must be reproducible: running your script again on the same universe
  file must produce the same three lists. Show that you ran it twice and got
  the same result.

## Output

All output in English.

- `scripts/` — the scripts you wrote, standalone and re-runnable, each with the
  header comment block your definition describes. Downloading must be
  **resumable**: a re-run picks up where an interrupted run stopped, and does
  not re-download what it already has and verified (RULES 26).
- `data/universe/` — the downloaded archive files and a manifest recording, per
  file: source URL, download time (read from the system clock, RULES 23),
  SHA-256, and the checksum-verification result.
- `data/universe/universe.csv` — one row per symbol: symbol, first trading day
  and last trading day seen in the archive, number of days with data, median
  daily volume, assigned group.
- `data/draw/observation-coins.txt` — the 10 observation symbols, one per line.
- `data/draw/draw-manifest.md` — the seed, the method, the size of each group,
  the two cut values, the SHA-256 of each of the four list files, and the
  disjointness check. **This file names the 10 observation symbols and does not
  name the exam or money-test symbols** — it is readable by roles that must not
  see those names.
- `exam/draw/exam-coins.txt` — the 20 exam symbols, one per line.
- `exam/draw/money-test-coins.txt` — the remaining symbols, one per line.

Then write your report in the five-part shape your definition sets out: what
you did with paths, what you measured with numbers, what you could not do and
the exact error, fingerprints, and anything you had to decide that this
instruction did not cover — by name.

## Time and interruption

This run may take longer than ten minutes. Write checkpoints and start the long
part so that it survives the session closing (RULES 26). If you run out of time
or hit a wall, a partial result with an honest account of where it stopped is
worth more than a guess. A technical failure is reported as a technical
failure, never as a result (RULES 21).

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

The instruction tells you what you may look at, never what to look for. If you
see a steer, a result, or a "pay attention to X" sentence in this instruction,
report it — that is a leak.
