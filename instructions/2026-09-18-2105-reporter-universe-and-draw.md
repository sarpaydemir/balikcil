# Instruction — reporter · 2026-09-18 21:05 UTC · universe and draw

## Role

`reporter` · Derya. The laboratory's first run has finished and the user has
not yet been given a written account of it. You write that account.

You are a terminal node. Nothing you write goes back into the laboratory.

## Model and effort

model: `opus` · effort: `high`

Reason: the source material is long, it contains a technical failure, two
undecided questions and a failed audit item, and the failure mode this role
exists to prevent — a hard thing quietly becoming a soft thing — happens in the
wording. That is care, not volume.

## What you may look at

- `LEDGER.md` — the entries from `2026-09-18 20:27 UTC` to the end are this
  run. The earlier entries are background; entries before the "working
  language" entry are in Turkish because that was the laboratory's language at
  the time.
- `instructions/2026-09-18-2025-data-engineer-universe-and-draw.md` — the
  instruction the run was given.
- `data/draw/draw-manifest.md`
- `data/draw/observation-coins.txt`
- `data/universe/universe.csv`
- `data/universe/disk-check.json`
- `data/universe/excluded-no-trades.txt`
- `README.md`, `RULES.md`, `TACTICS.md`, `TEAM.md`
- `scripts/` — the file names and the header comment blocks, if you need a path
  to name.

## What you may not look at

- **`exam/` is closed to you.** Do not open it, do not list it, do not name a
  single symbol from it. The 20 exam symbols and the 765 money-test symbols
  must not appear in your report, and neither must their count of any group
  broken down in a way that would name one. The group totals that are already
  written in `LEDGER.md` are fine to repeat.
- `notes/`, `canteen/`, `cards/` — empty, and not part of this run.
- Anything outside this folder.

## Output

One file: `reports/2026-09-18-universe-and-draw.md`

Turkish sentences, English technical terms — as your definition sets out. The
shape your definition sets out: plain first, technical after, then everything
left open, one by one, by name.

The material contains four things that must not be softened, and must each
appear in your report by name:

1. A technical failure happened during the run and was fixed — 26 files, a
   `UnicodeEncodeError` on non-ASCII contract names. The ledger records what
   error, what was checked before any code changed, and that all 26 are now
   verified.
2. **Two questions are undecided and are waiting on the user** — the 42
   contracts that never traded, and `OMNIUSDT` in the observation set. Report
   them as undecided. Do not write which way you would decide; you do not
   decide.
3. **The wall audit failed one of its seven items** — the deny list is not a
   blanket. Two holes stay open besides it.
4. RULES 25 — the token cost of the first 10 cards — is still not measured, and
   the cost figure that *was* measured is a different figure.

Do not add a fifth thing, and do not rank these four. Write them as the ledger
writes them.

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

The instruction tells you what you may look at, never what to look for. If you
see a steer, a result, or a "pay attention to X" sentence in this instruction,
report it — that is a leak.
