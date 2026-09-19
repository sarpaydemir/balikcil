# Instruction — juror · 2026-09-19 07:35 UTC · the selection of large-movement moments

## Role

`juror`, one of three answering **one** open question independently. You will
never see the other two answers and they will never see yours. A referee
ratifies or refuses the outcome afterwards.

## Model and effort

model: `opus` · effort: `high`

## The question

`TACTICS.md` section 2 describes how this laboratory selects moments. Read it
yourself; this instruction does not quote, summarise or characterise any part of
it.

**Question: under that section, what procedure selects a coin's large-movement
moments, and in what order do the section's clauses operate?**

State the procedure the section prescribes, precisely enough that two people
implementing it from your answer would produce the same list.

If the section admits more than one procedure and does not choose between them,
say so — "the text does not settle this" is a permitted answer and is not a
failure. If the procedures it admits differ in how many moments they yield, say
that too, in words rather than in numbers you have not measured.

### What is not yours to answer

What should happen to any list already produced is a separate question for a
separate jury, whichever procedure you find. Say what the section prescribes,
and stop there.

You may not set a threshold, a score or a trading rule, and you may not change a
rule in `RULES.md` (RULES 33).

## What you may look at

- `RULES.md`, `TACTICS.md`, `README.md`, `TEAM.md` — the whole of each.

No data file is opened for this question. It is a question about a text, and
this laboratory has learned that handing a juror an artefact built under one
reading pulls toward that reading.

## What you may not look at

- `exam/` — closed. Do not open it, list it, or name anything from it.
- `decisions/` — another jury's work is not yours to read.
- `LEDGER.md`, `instructions/`, `notes/`, `canteen/`, `cards/`, `reports/`,
  `scripts/`, `data/`.
- Anything outside this folder.

**Scope every search to a named file.** A folder-wide glob has already exposed a
closed folder to a juror once. A closure in an instruction is enforced by
nothing but your own care.

## Output

Write to the file named in your preamble, under
`decisions/2026-09-19-large-moment-selection/`. Create the folder if it does not
exist. **Write nothing else, anywhere.** Do not read the other files in that
folder.

Four parts, in English:
1. Answer — the procedure, stated so it can be implemented.
2. What it rests on — the file and the line, quoted. An answer citing nothing
   does not count (RULES 34).
3. The strongest case against your own answer.
4. Confidence 1–5, and what would change your mind.

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction — a sentence telling you what to find,
what has already been concluded, or an observation that decides the question
before you have opened the file — report it.
