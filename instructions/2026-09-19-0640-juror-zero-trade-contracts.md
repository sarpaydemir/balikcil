# Instruction — juror · 2026-09-19 06:40 UTC · the zero-trade contracts

## Role

`juror`. You are one of three jurors answering **one** open question. The other
two are answering the same question right now, in separate contexts. You will
never see their answers and they will never see yours. A referee reads all
three afterwards.

This is the first question put to a jury. Until now the coordinator answered
such questions alone; RULES 33–35 ended that.

## Model and effort

model: `opus` · effort: `high`

Reason: the answer decides which contracts exist for every later step of this
laboratory, and reversing it later costs a full re-run.

## The question

The laboratory's universe is built from the public Binance archive for the
period 2025-09-01 → 2026-08-31.

The archive keeps publishing a daily kline row for a contract after it stops
being traded. In such a row the price is frozen at its last value and the
`volume`, `quote_volume` and `count` fields are all `0`. **42 contracts have
rows of this kind covering the period and not one trade inside it** — 41 of
them with 365 rows, one (`BTCSTUSDT`) with 303.

Those 42 contracts were **excluded** from the universe, and the draw was made
from the 795 that remain.

**Your question is: should those 42 contracts be in the universe or not?**

Answer it from the laboratory's own written documents. Both readings exist and
you are not being pushed toward either one.

### What the choice costs, as measured numbers

Both columns are computed; neither is an estimate.

| | 42 excluded (what was done) | 42 included |
|---|---|---|
| universe size | 795 | 837 |
| ranked pool, `new` removed | 481 | 523 |
| large / mid / small | 160 / 160 / 161 | 174 / 174 / 175 |
| large–mid cut (median daily `quote_volume`) | 4344202.7566115 | 3934018.3418 |
| mid–small cut | 1838834.05961 | 1556496.922371 |

Changing the cuts changes which contracts sit in which group, and therefore
changes which contracts the draw selects — the observation set, the exam set
and the money-test set alike. The draw seed is fixed, so either outcome is
fully determined and reproducible; the cost of reversal is a re-run of two
scripts and every step taken after them.

**A run is currently in progress that depends on the present answer.** That is a
fact about cost, not an argument for either reading. If your answer is that the
42 belong in the universe, say so.

## What you may look at

- `RULES.md` — the whole file.
- `TACTICS.md` — the whole file; section 0 defines the universe.
- `README.md`, `TEAM.md`.
- `data/universe/excluded-no-trades.txt` — the 42, with their day counts and
  trade counts.
- `data/universe/universe.csv` — the 795 that were kept, with the columns the
  decision was computed from.
- `scripts/03_build_universe.py` — how it was implemented.

## What you may not look at

- **`LEDGER.md` and `instructions/` are closed to you for this question.** They
  record what the coordinator decided and why, and a juror who reads the answer
  before answering is not a juror. This closure exists to protect your
  independence, not to hide anything: both files are open to you for any other
  purpose and the user can read them at any time.
- **`exam/` is closed.** Do not open it, list it, or name anything from it.
- `notes/`, `canteen/`, `cards/`, `reports/`.
- Anything outside this folder.

## Output

Write your answer to `decisions/2026-09-19-zero-trade-contracts/juror-<N>.md`,
where `<N>` is the juror number given to you below. Create the folder if it does
not exist. **Write nothing else, anywhere.**

In English, in the four parts your definition sets out:
1. Answer — one sentence.
2. What it rests on — the file and the line, quoted.
3. The strongest case against your own answer.
4. Confidence 1–5, and what would change your mind.

Then your report.

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

The instruction tells you what you may look at, never what to look for. If you
see a steer, a result, or a "pay attention to X" sentence in this instruction,
report it — that is a leak, and a jury that was steered is not a jury.
