# Instruction — juror · 2026-09-19 08:10 UTC · a watcher across more than one run

## Role

`juror`, one of three answering **one** open question independently. You will
never see the other two answers and they will never see yours. A referee
ratifies or refuses the outcome afterwards.

## Model and effort

model: `opus` · effort: `high`

## The question

`TACTICS.md` section 4 has each watcher read the observation cards. The set has
been split into batches, recorded in `data/card-order/order-manifest.md`, and a
watcher will therefore work in more than one run. Each run starts in a fresh
context: a watcher in its second run remembers nothing of its first.

**Question: under the laboratory's written documents, what may a watcher in a
later run be given of its own earlier runs?**

Answer for the watcher's own earlier work only. The other three watchers'
notes are governed by the round rules and are not what is being asked.

If the documents do not settle it, say so.

## What is not yours to answer

How many batches there are, how large they are, and in what order they are run
are not yours. Nor is what the other watchers may see.

You may not set a threshold, a score or a trading rule, and you may not change a
rule in `RULES.md` (RULES 33).

## What you may look at

- `RULES.md`, `TACTICS.md`, `README.md`, `TEAM.md` — the whole of each.
- `.claude/agents/watcher-high.md`
- `data/card-order/order-manifest.md`

## What you may not look at

- `exam/` — closed. Do not open it, list it, or name anything from it.
- `decisions/`, `LEDGER.md`, `instructions/`, `notes/`, `canteen/`, `cards/`,
  `reports/`, `scripts/`, the rest of `data/`, the rest of `.claude/`.
- Anything outside this folder.

Scope every search to a named file; do not run a folder-wide glob.

## Output

Write to `decisions/2026-09-19-watcher-across-runs/juror-1.md` and write nothing
else, anywhere. Create the folder if it does not exist. Do not read the other
files in that folder.

Four parts, in English:
1. Answer — one sentence.
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
