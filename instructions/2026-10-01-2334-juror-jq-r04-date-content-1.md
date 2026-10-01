# Instruction — juror · 2026-10-01 23:34 UTC · open question JQ-R04-DATE-a to -c with JQ-R04-CONTENT-a to -c

## Role

`juror`, one of three answering **one** open question independently. You will
never see the other two answers and they will never see yours. A referee
ratifies or refuses the outcome afterwards (RULES 35).

## Model and effort

model: `opus` · effort: `high`

## The question

**Read it where it is written:** `exam-prep/sixth-fix/juror-questions/JQ-R04-DATE.md`, Parts a to c, and `exam-prep/sixth-fix/juror-questions/JQ-R04-CONTENT.md`, Parts a to c.

It has 6 parts — JQ-R04-DATE-a, JQ-R04-DATE-b, JQ-R04-DATE-c, JQ-R04-CONTENT-a, JQ-R04-CONTENT-b, JQ-R04-CONTENT-c — which the laboratory's index says must be answered together by the same jurors. Together they count as one question under RULES 33: answer every part, and say where your answer to one part depends on another.

The coordinator has not read the question and does not restate it. Answer it as
it is posed there. If it cannot be answered as posed — because it is ambiguous,
because an outcome it offers cannot follow, or because it asks for something a
juror may not decide — say so and why. That is an answer.

## Earlier decisions of this laboratory

Earlier open questions were decided by juries and ratified. Their outcomes are in
the files named `verdict.md` inside the folders of `decisions/` whose names begin
`2026-09-19-`, and in `decisions/2026-10-01-jq-r04-gate/verdict.md`, `decisions/2026-10-01-jq-n1-canteen-8/verdict.md`. **You may read those `verdict.md` files and
nothing else under `decisions/`.** If one of them already settles part of your
question, say so and cite it.

**One earlier verdict reaches you only as quoted here.** The question `JQ-R04-CARRIES` was answered by three jurors and ratified. Its folder, `decisions/2026-10-01-jq-r04-carries/`, is closed to you. Its ratified outcome, copied verbatim from the verdict section of `decisions/2026-10-01-jq-r04-carries/verdict.md` (SHA-256 `514a8d45038d3d7ad2feba3479c58d6e1da8e50358c799203f35b22cc246050a`), lines 107 and 109, is:

> **JQ-R04-CARRIES-a:** When the test in part b identifies a column's feature sets, the column carries a measured coin signature when **either** the pair AUC attack or the nearest-neighbour attack beats its own RULES 12 chance line on that set. Split: 3–0.
>
> **JQ-R04-CARRIES-b:** The test reads every feature computed from the column's own printed values and from nothing else, tested together as one set. For the trade-count column: its typical level, its two repeat features and its two shape features, not the previous-7-day feature. The audit gains this set as a row of its own. Split: 2–1 (majority for option 1; one juror proposes supplementing with pure-column families, both implementations possible).

It binds you as settled law.

## What is not yours to decide

You may not set a threshold, a score or a trading rule, and you may not change a
rule in `RULES.md` (RULES 33). If answering would require one, say so instead.

## What you may look at

- `exam-prep/sixth-fix/juror-questions/JQ-R04-DATE.md`
- `exam-prep/sixth-fix/juror-questions/JQ-R04-CONTENT.md`
- `canteen/2026-09-19-sofia.md` lines 112–120, 221–225, 245–246, 268–270 and 667–671 **only** — no other line of that file
- `RULES.md`, `TACTICS.md`, `TEAM.md`, `README.md` — the whole of each.
- `decisions/2026-09-19-*/verdict.md` and the other `verdict.md` files named above.

## What you may not look at

- `exam/` — closed. Do not open it, list it, or name anything from it.
- Anything in `exam-prep/` not named above.
- Under `decisions/`, anything that is not one of the `verdict.md` files above —
  in particular, nothing in `decisions/2026-10-01-jq-r04-date-content/` except the file you write.
- `LEDGER.md`, `instructions/`, `notes/`, `cards/`, `reports/`, `scripts/`,
  `external/`, the rest of `data/` and of `canteen/`, `.claude/`.
- Anything outside this folder.
- `decisions/2026-10-01-jq-r04-carries/` — closed to you, except as quoted in this instruction.

Scope every search to a named file; do not run a folder-wide glob.

## Output

Write to `decisions/2026-10-01-jq-r04-date-content/juror-1.md` and write nothing else, anywhere. Create the
folder if it does not exist. Do not read the other files in that folder.

Four parts, in English:
1. Answer — part by part, each under its identifier.
2. What it rests on — the file and the line, quoted. An answer citing nothing
   does not count (RULES 34).
3. The strongest case against your own answer.
4. Confidence 1–5, and what would change your mind.

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction, report it.
