# Instruction — data-engineer · 2026-09-19 09:40 UTC · rebuilding the card order

## Role

`data-engineer` · **Mode A**. The card order built at 07:55 UTC was built under
a reading of TACTICS 4 that a jury has since ruled on. This run builds the order
again under the ratified requirement. It writes no card and changes none.

## Model and effort

model: `opus` · effort: `high`

## The ratified requirement

**Read it yourself** in `decisions/2026-09-19-card-order-requirement/verdict.md`
and in the three juror answers beside it. This instruction does not restate,
summarise or paraphrase the requirement, and you should not take my word for any
part of it.

The measured conformance of the existing order is in
`data/card-order/order-conformance-check.md`. It is a measurement and draws no
conclusion; drawing the conclusion against the ratified requirement is part of
your work.

## What you may look at

- `decisions/2026-09-19-card-order-requirement/` — the verdict and the three
  juror answers.
- `RULES.md`, `TACTICS.md` — the whole of each.
- `cards/INDEX.md` and the card files.
- `data/moments/moments.csv`
- `data/card-order/` — what the previous run produced, including its manifest
  and its conformance check.
- `scripts/` — your own scripts, including `11_card_order.py`.

## What you may not look at

- `exam/` — closed. Read nothing, write nothing there.
- `notes/`, `canteen/`, `reports/`, `instructions/`, `LEDGER.md`, the other
  folders under `decisions/`.
- Anything outside this folder.

## The task

1. **Check the existing order against the ratified requirement** and say plainly
   whether it conforms. If you find it does, say so and stop — do not rebuild
   something that does not need rebuilding.
2. If it does not conform, **build an order that does**, over the same 306
   cards, and split it into batches as before.
3. The seed must be fixed and recorded, and must be derived rather than
   invented, as the previous run's was. Say what you derived it from and why it
   differs from the previous seed — an order rebuilt with the same seed and the
   same procedure would be the same order.
4. **Nothing under `data/card-order/` that the previous run wrote may be
   overwritten or deleted** (RULES 30). The old order stays where it is, as the
   record of what was built and why it was replaced. Put the new artefacts
   somewhere that makes the succession obvious, and say in the manifest which
   order supersedes which.
5. Run the same checks as before — permutation, every card in exactly one batch,
   batches concatenating back to the order, reproducibility across runs — and
   add a check of the new order against the ratified requirement, expressed so
   that someone reading it can answer yes or no without trusting you.

## Output

All output in English. The new order, its batch files and a manifest carrying
the seed and its derivation, the batch table, every check with its result, the
fingerprints, and a statement of what it supersedes.

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
