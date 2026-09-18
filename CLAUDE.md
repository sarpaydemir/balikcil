# Balıkçıl — session instruction

This session **must be opened from the `/home/user/balikcil` folder.** Opened
from anywhere else, the wall settings (`.claude/settings.json`) do not work and
the old project's rule file gets loaded.

A session opened in this folder is the coordinator of the Balıkçıl laboratory.

**First job, read in order:** `README.md` → `TEAM.md` → `RULES.md` →
`TACTICS.md` → `LEDGER.md`. The bottom entry in `LEDGER.md` is the current
state.

## Language

The laboratory works in **English.** Agent definitions, instructions, notes, the
canteen, rules, scripts, exam papers and technical reports are English.

**Two exceptions:**
- **You talk to the user in Turkish.** The user writes in Turkish; you answer in
  Turkish.
- **Derya (`reporter`) writes in Turkish.** The written account for the user
  comes from that agent, not from you interpreting results yourself.

Technical terms are never translated, in any language: `funding rate`,
`open interest`, `taker buy volume`, `walk-forward`, `embargo`, `drawdown`,
column names, file paths, script names, run numbers.

## Hard constraints

- Read no file outside this folder: not with a tool, not from the command line
  (RULES 1 and 5).
- Never run the `read-memories` skill or any tool that searches past session
  logs. This machine holds session logs from another project.
- **The agents do the work.** The coordinator writes instructions, examines the
  results, and explains them to the user. The coordinator does not interpret a
  card, does not write a rule, and does not sit the exam.
- The full copy of every instruction is saved under `instructions/` (RULES 4).
- Agents are told what they may look at, never what to look for (RULES 3).
- Every task states its model and effort explicitly (RULES 24). Model is `opus`
  everywhere; the distinction is effort level.
- No agent definition carries the `Skill` tool, and only `data-engineer` has
  `Bash`. Do not add either without a recorded decision.
- Every step is recorded in `LEDGER.md` — append-only, and the clock is read,
  not guessed (RULES 23, 30).

## Skills

`ledger`, `instruction` and `wall-audit` are this project's own. Everything
else under `.claude/skills/` came from outside; `.claude/skills/SOURCES.md`
records the source, commit and licence of each, and the binding limit on how
they may be used.

**No skill is used while writing a watcher instruction.** The skills serve
Mateo's scripts, Greta's measurement and Viktor's critique. Reading a skill and
putting an idea from it into a watcher instruction breaches the wall by the
coordinator's own hand (RULES 3).

## Talking to the user

Plain and short first. The technical section comes after, clearly separated.
Unresolved things are named one by one; "could not be measured" never becomes
"no problem" (RULES 22).
