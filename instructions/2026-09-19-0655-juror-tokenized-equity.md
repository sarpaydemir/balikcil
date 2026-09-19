# Instruction — juror · 2026-09-19 06:55 UTC · tokenized equities in the universe

## Role

`juror`, one of three answering **one** open question independently. You will
never see the other two answers and they will never see yours. A referee
ratifies or refuses the outcome afterwards.

## Model and effort

model: `opus` · effort: `high`

## The question

`TACTICS.md` section 0 defines this laboratory's universe. The definition is
written in terms of contracts.

**Question: does that definition admit a contract whose underlying is a
tokenized equity — a share in a listed company — rather than a
cryptocurrency?**

`data/observation/external/coin-names.json` holds a name lookup for each of the
ten observation contracts, taken from the public CoinGecko search endpoint and
recorded with its source URL, its result and its error where there was one.
Read it and decide for yourself what it shows.

**Nothing has been decided on this question.** No answer exists to agree or
disagree with, and no work has been done either way.

### What is not yours to answer

If your answer is that such contracts do not belong, **the remedy is a separate
question for a separate jury** — what to do about a contract already drawn is
not yours, and you should not propose it. Say what the definition admits, and
stop there.

You also may not set a threshold, a score or a trading rule, and you may not
change a rule in `RULES.md` (RULES 33).

## What you may look at

- `RULES.md`, `TACTICS.md`, `README.md`, `TEAM.md` — the whole of each.
- `data/observation/external/coin-names.json`
- `data/draw/observation-coins.txt`
- `data/universe/universe.csv`

## What you may not look at

- `exam/` — closed. Do not open it, list it, or name anything from it.
- `decisions/` — another jury's work is not yours to read.
- `LEDGER.md`, `instructions/`, `notes/`, `canteen/`, `cards/`, `reports/`,
  `scripts/`.
- Anything outside this folder.

## Output

Write to the file named in your preamble, under
`decisions/2026-09-19-tokenized-equity/`. Create the folder if it does not
exist. **Write nothing else, anywhere.** Do not read the other files in that
folder.

Four parts, in English:
1. Answer — one sentence.
2. What it rests on — the file and the line, quoted. An answer citing nothing
   does not count (RULES 34).
3. The strongest case against your own answer.
4. Confidence 1–5, and what would change your mind.

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction — a sentence telling you what to find, or
what has already been concluded — report it. Three such leaks were found in the
laboratory's previous jury question and the correction is being tested here.
