# Instruction — data-engineer · 2026-09-19 07:55 UTC · the card order and its batches

## Role

`data-engineer` · **Mode A**. The 306 observation cards exist. This run produces
the order in which they are given to a watcher, and the batches a watcher reads
them in. It writes no card and changes none.

## Model and effort

model: `opus` · effort: `high`

## What you may look at

- `TACTICS.md` — section 4 states how cards are given to a watcher.
- `RULES.md` — the whole file.
- `cards/INDEX.md` and the card files, for their numbers and their sizes.
- `data/moments/moments.csv`
- `scripts/` — your own scripts.

## What you may not look at

- `exam/` — closed. Read nothing, write nothing there.
- `notes/`, `canteen/`, `decisions/`, `reports/`, `instructions/`, `LEDGER.md`.
- Anything outside this folder.

## The task

### 1 · The order

Produce one order over all 306 cards, satisfying what TACTICS 4 requires of the
order in which cards reach a watcher. Read that requirement from TACTICS 4
itself; this instruction does not restate it.

The order must be reproducible: the same input must always produce the same
order. Fix the seed, write it down, and say where the seed came from rather than
inventing a number.

### 2 · The batches

A watcher reads the cards in batches, because the 306 cards do not fit in one
agent's context. Split the order into batches.

**Measure before choosing the size:** the bytes of the cards, and what a batch
therefore costs to read. State the batch size you chose, the measurement it
rests on, and what you assumed about how much room a reader needs beyond the
cards themselves. If you cannot measure something the choice depends on, say so
rather than estimating silently (RULES 19).

Every card appears in exactly one batch. Verify that in code and report the
check. The batch a card falls into must not be decided by its coin, its kind or
its date — only by its position in the order from step 1.

### 3 · What a watcher is given

For each batch, produce the list of card numbers in that batch, in order, in a
form an instruction can name directly.

## Output

All output in English.

- `scripts/` — the script, standalone, re-runnable, header comment block, seed
  fixed and written down.
- `data/card-order/order.csv` — one row per card, in order: position, card
  number. Nothing else on the row.
- `data/card-order/batches/` — one file per batch, listing that batch's card
  numbers in order.
- `data/card-order/order-manifest.md` — the seed and where it came from, the
  number of batches, the size of each, the measurement the size rests on, the
  every-card-exactly-once check, and the SHA-256 of `order.csv` and of each
  batch file.

Then your five-part report: what you did with paths, what you measured with
numbers, what failed and the exact error, fingerprints, and anything you had to
decide that this instruction did not cover.

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction — a sentence telling you what to look
for, what you will find, or what has already been concluded — report it.
