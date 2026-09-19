# Instruction — juror · 2026-09-19 07:15 UTC · TACTICS 2 and the separation of calm moments

## Role

`juror`, one of three answering **one** open question independently. You will
never see the other two answers and they will never see yours. A referee
ratifies or refuses the outcome afterwards.

## Model and effort

model: `opus` · effort: `high`

## The question

`TACTICS.md` section 2 describes how this laboratory selects moments. Read it
yourself; it is short, and this instruction deliberately does not quote or
summarise any part of it.

**Question: under that section, is there a minimum distance required between
two calm moments belonging to the same coin?**

Answer only what the section requires. Neither answer has been taken, neither
has been implemented in preference to the other in anything you may read, and
no answer is expected.

### The question is live, and here is why, measured

In the moment list produced for the ten observation coins
(`data/moments/moments.csv`, 153 calm moments), the coordinator measured:

- **20** pairs of calm moments that are adjacent in time within their own coin
  and less than 48 hours apart;
- **21** pairs in total within a coin and less than 48 hours apart — the extra
  one arising where three calm moments of one coin fall inside a single
  48-hour window.

Both numbers are measured from that file, not estimated. They are given so that
you know the question is not hypothetical. They bear on neither answer: if the
section requires no separation, those pairs are correct; if it requires one,
they are not.

### What is not yours to answer

**Whichever way you answer**, what should happen to moments already selected is
a separate question for a separate jury, and you should not propose it. The
same applies whichever way you answer — say what the section requires, and stop
there.

You may not set a threshold, a score or a trading rule, and you may not change a
rule in `RULES.md` (RULES 33). If you find that the section is silent, say it is
silent; "the text does not settle this" is a permitted answer and is not a
failure.

## What you may look at

- `RULES.md`, `TACTICS.md`, `README.md`, `TEAM.md` — the whole of each.
- `data/moments/moments.csv`

## What you may not look at

- `exam/` — closed. Do not open it, list it, or name anything from it.
- `decisions/` — another jury's work is not yours to read.
- `LEDGER.md`, `instructions/`, `notes/`, `canteen/`, `cards/`, `reports/`,
  `scripts/`, and everything under `data/` except the one file named above.
- Anything outside this folder.

**Scope every search to a named file.** In an earlier question a folder-wide
`*.md` glob matched a closed folder and exposed three lines of it before the
juror stopped. A closure in an instruction is not enforced by anything but your
own care.

## Output

Write to the file named in your preamble, under
`decisions/2026-09-19-calm-separation/`. Create the folder if it does not exist.
**Write nothing else, anywhere.** Do not read the other files in that folder.

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

If you see a steer in this instruction — a sentence telling you what to find,
what has already been concluded, or an observation that decides the question
before you have opened the file — report it. Six such faults have been found in
this laboratory's instructions so far, every one by the agent receiving them.
