# Instruction — juror · 2026-09-19 09:05 UTC · the order in which cards reach a watcher

## Role

`juror`, one of three answering **one** open question independently. You will
never see the other two answers and they will never see yours. A referee
ratifies or refuses the outcome afterwards.

## Model and effort

model: `opus` · effort: `high`

## The question

**Question: what does `TACTICS.md` section 4 require of the order in which the
cards reach a watcher?**

State the requirement precisely enough that someone could check a given order
against it and say yes or no.

If the section admits more than one requirement and does not choose between
them, say so.

## What is not yours to answer

Whether any order already built meets your answer is not yours — you are not
shown one, and what to do about one is a separate question for a separate jury.
Nor is the batch size, the batch count or the run order.

You may not set a threshold, a score or a trading rule, and you may not change a
rule in `RULES.md` (RULES 33).

## What you may look at

- `RULES.md`, `TACTICS.md`, `README.md`, `TEAM.md` — the whole of each.
- `.claude/agents/watcher-high.md`

## What you may not look at

- `exam/` — closed. Do not open it, list it, or name anything from it.
- `decisions/`, `LEDGER.md`, `instructions/`, `notes/`, `canteen/`, `cards/`,
  `reports/`, `scripts/`, `data/`, the rest of `.claude/`.
- Anything outside this folder.

Scope every search to a named file; do not run a folder-wide glob.

## Output

Write to `decisions/2026-09-19-card-order-requirement/juror-1.md` and write
nothing else, anywhere. Create the folder if it does not exist. Do not read the
other files in that folder.

Four parts, in English:
1. Answer — the requirement, stated so an order can be checked against it.
2. What it rests on — the file and the line, quoted. An answer citing nothing
   does not count (RULES 34).
3. The strongest case against your own answer.
4. Confidence 1-5, and what would change your mind.

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction, report it.
