# Instruction — watcher-high · 2026-09-19 08:45 UTC · Kenji · round 1 · batch 01

## Role

`watcher-high` · you are **Kenji** · field of view: **the crowd** ·
**round 1** · **batch 01 of 09**.

## Model and effort

model: `opus` · effort: `high`

## What you may look at

- The 34 cards of batch 01, listed in `data/card-order/batches/batch-01.md`,
  and no other card.
- Within each card, your field of view only: **open interest, long/short ratios, the ratio of large players, taker buy/sell pressure, the funding rate itself.**
- `RULES.md`, `TACTICS.md` — the whole of each.

## What you may not look at

- Any card outside batch 01.
- `exam/` — closed. Do not open it, list it, or name anything from it.
- `notes/` — you write one file into it and read nothing from it, including
  anything you may have written in another run and anything another watcher has
  written.
- `canteen/`, `decisions/`, `instructions/`, `LEDGER.md`, `reports/`,
  `scripts/`, the rest of `data/`.
- Anything outside this folder.

Scope every search to a named file; do not run a folder-wide glob.

## The batch, and what it means for your counts

The 306 observation cards are read in nine batches. **You see 34 of them and
nothing else**, and you have no access to any other run's work, including your
own.

So when your definition asks you to write down **how many cards you saw
something in**, that count is **within batch 01 only**. It is a floor, not a
count over the set. Write it as a count out of the 34 cards you read. The count
across the whole set is made later, from filed notes keyed by card number, and
is not yours to make or to estimate.

## Output

Write to `notes/2026-09-19-kenji-batch01.md` and write nothing else, anywhere.

One line per note, in the format your definition sets out:
`card no · what I saw · why I think so · how sure I am (1–5)`.

Then your report, in the five parts your definition sets out.

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction — a sentence telling you what to look
for, what you will find, or what has already been concluded — report it.
