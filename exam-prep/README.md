# `exam-prep/` — the ground prepared before any exam card exists

Mateo · data engineer · 2026-09-19 (system clock, RULES 23)

This folder holds the working behind two problems the canteen measured and
stopped at: **R-04**, whether the exam is blind at all, and **N-1**, collapsing
cards that share a clock hour into one event before anything is counted.

Nothing here is a trading rule, a threshold in a score, or an interpretation of
a card. It is instruments and measurements.

## Read in this order

| file | what it is |
|---|---|
| `VERDICT.md` | solved or not solved, for each problem. Says nothing about how. |
| `R-04-blindness.md` | the blindness standard, what the raw card leaks, what the blinding closes, what it cannot close and why, and the acceptance gate the exam-building run must run |
| `N-1-collapse.md` | the collapse standard, the readings of RULES 13 that the rules allow, what each counts, what collapsing does to a chance line, and the open question left for three jurors |
| `decisions-and-open-questions.md` | ten decisions I took that the instruction did not cover, five questions I refused to answer, and the steer check on my own instruction |
| `FINGERPRINTS.md` | SHA-256 of every file in this folder except the card files, and of the five scripts |

## The measured output

| folder | what is in it |
|---|---|
| `collapse/` | `events.csv` (every card's event under every configuration), `collapse-summary.csv`, `shuffle-calibration.csv`, `collapse-manifest.md`, `runs/` |
| `identity/` | one audit per card set — raw and four blinded configurations — plus the hour-linkage tables, the residual diagnostic, and `runs/` |
| `blind-proof/<variant>/` | 306 blinded cards, the truth file that lets the audit attack them, the blinding manifest and `runs/` |

The blinded cards in `blind-proof/` are blinded copies of the **observation**
cards. They are a proof that the instrument works and a fixture the reviewer
can attack. **They are not exam cards** and no exam card exists yet.

## The instruments

| script | what it does |
|---|---|
| `scripts/lab_cards.py` | reads a card — raw or blinded — into a plain dict |
| `scripts/15_event_collapse.py` | the collapse engine, the cluster-level shuffle, the chance line that refuses to run without an event map |
| `scripts/16_identity_audit.py` | three de-anonymisation attacks with permutation chance lines |
| `scripts/17_blind_cards.py` | the blinding transform, configurable, with its own guards |
| `scripts/18_residual_diagnostic.py` | where the leftover coin signal on a blinded set comes from |

Every one of them writes an append-only run record (RULES 29, 30), reads the
system clock rather than guessing it (RULES 23), and records free disk space.
Every constant is defined at the top of its file with the rule or the document
it came from.

## What this run did not touch

`exam/` — not read, not written. `decisions/`, `instructions/`, `LEDGER.md`,
`reports/` — not read. Nothing outside the Balıkçıl folder was read, with any
tool or from the command line.
