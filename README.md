# Balıkçıl — observation laboratory

**Code name:** Balıkçıl (Turkish for heron) · **Folder:** `/home/user/balikcil`

A heron stands motionless in the water for hours. It does nothing, it only
watches. When it understands the water, it strikes once.

This laboratory works the same way. It does not trade; first it watches: what
happens while a coin is quiet, what happens before a sharp move, what the
exchange is doing meanwhile, what is happening in the world.

**The goal is a scoring system.** If the score is above one line, buy; at
another line, sell (short); in between, do nothing. Where the score comes from
is found by watching, not by guessing.

## Why there is a wall

We worked for months in the old laboratory and accumulated a pile of opinions.
So that those opinions do not colour the new watchers' eyes, Balıkçıl stands
behind a wall:

- the old rule file is not loaded
- the old experiment folders and status files cannot be read
- Balıkçıl has its own memory
- data is downloaded from scratch

The wall lives in `.claude/settings.json` and **only works when Balıkçıl is
opened from this folder.** Details in `RULES.md`.

## The flow — seven steps

1. **The draw.** Coins are picked by lot: 10 coins for observation, 20 for the
   exam, the rest for the money test.
2. **Preparation.** Data is downloaded. Each coin's large-movement moments and
   calm moments are found. A one-page card is written for each moment. A script
   does this, not an AI.
3. **Free observation.** Four watchers read the cards of the 10 coins. They see
   both before and after the movement, and take notes.
4. **The canteen.** The watchers read each other's notes and argue. The skeptic
   attacks every idea. The canteen chair turns the surviving ideas into rules.
5. **The blind exam.** Cards from the exam coins are shown, but only the part
   before the movement. The coin name and date are hidden. The rules predict
   "what will happen". Somebody who never watched, and a simple rule, sit the
   same exam.
6. **The money test.** A rule that passes the exam is tried, with its costs, on
   hundreds of coins never seen before.
7. **The report.** Plain first, technical after.

**Free observation produces ideas, not evidence.** Evidence comes only from
steps 5 and 6.

## Language

The laboratory runs in **English**: agent definitions, instructions, notes, the
canteen, rules, scripts, exam papers, technical reports.

**One role speaks Turkish:** Derya, the reporter, who writes the plain account
for the user. Technical terms are never translated. See `TEAM.md`.

## Files

- `TEAM.md` — who is who, what they do, what they cannot do
- `RULES.md` — the rules that do not change
- `TACTICS.md` — how it is done, step by step
- `LEDGER.md` — what happened when; append-only, no line is ever deleted
- `CLAUDE.md` — the first thing a session opened in this folder reads
- `.claude/settings.json` — the wall settings
- `.claude/agents/` — the six agent definitions
- `.claude/skills/` — skills, and `SOURCES.md` saying where each came from

Folders: `data/` · `cards/` · `notes/` · `canteen/` · `exam/` ·
`instructions/` · `scripts/` · `reports/`

## Status

Founded `2026-09-13`, moved and walled `2026-09-14`, agents and skills set up
`2026-09-18`, switched to English `2026-09-18`. First run `2026-09-18`: the
universe was built from the archive and the draw was made (795 contracts; 10
observation · 20 exam · 765 money test). No card has been written and no
watcher has run yet.

**To be added later:** the observation screen. Cards, notes, votes and
objections on a single page.
