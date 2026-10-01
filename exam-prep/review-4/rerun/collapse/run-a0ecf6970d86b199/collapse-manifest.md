# Collapse manifest — the event map RULES 13 needs

Written by `scripts/15_event_collapse.py`. It builds every candidate reading of RULES 13's "the same hour" and measures each. **It chooses none of them.** The choice is an open question under RULES 33; see `exam-prep/second-fix/juror-questions/JQ-N1.md`.

## Run

| field | value |
|---|---|
| run number (SHA-256 of the inputs, RULES 29) | `a0ecf6970d86b199` |
| full input fingerprint | `a0ecf6970d86b199d33190817debe83c03c197bd81c9651f2ef3c48ee1b71144` |
| written at (system clock, UTC, RULES 23) | 2026-10-01T21:57:10Z |
| free disk space at start (bytes) | 12396142592 |
| moments read | 306 |
| input | the 306 cards in `cards/` |
| shuffles (RULES 12) | 1000 |
| boundary (RULES 12) | best 1.0% |
| seed (TACTICS 1 draw number) | `20260913` |
| `scripts/15_event_collapse.py` SHA-256 | `002bb40639dee684fd4b7c653d2db45ec2c4527ade38d565e765619a9eebf4e6` |

Run records live in `runs/`, one JSON per run number, append-only (RULES 30). Records present when this manifest was written: `a0ecf6970d86b199`. The outputs of run `386d234b85269a21` (the version reviewed in `exam-prep/REVIEW.md`) are the files directly in `exam-prep/collapse/` and are not touched by later runs; every later run writes into its own `run-<number>/` directory.

## The block-shuffle self-test

Before anything is measured the script checks, on 1000 draws per event map (seed `20260913`), that every block draw is a permutation, that every event reads all its answers from one source event of its own size, and that an event-constant answer vector stays event-constant. It stops on the first failure. It passed on the review's three-event example and on all 11 configurations.

## The candidate readings

| name | what counts as "the same hour" | largest start gap that still merges |
|---|---|---|
| `start-hour` | the two moments begin in the same clock hour (TACTICS 2: a moment's start is the hour the 24-hour movement began) | 0 h |
| `move-window` | the two 24-hour movements share a clock hour | 23 h |
| `card-span` | the two 48-hour card spans share a clock hour — the relation `14_overlap_map.py` measured | 47 h |

`component` = anything chained together is one event. `greedy-clique` = repeatedly take the clock hour covered by the most still-unassigned moments (ties: earliest hour, then lowest id). `greedy-clique` is a **stated convention**, not an observation: overlapping intervals have no unique partition into "groups sharing an hour", so some deterministic rule is needed and this one is written down so it can be disagreed with.

`any` = two moments of the same coin may be joined directly. `cross-coin` = two moments of the same coin are never joined **directly**. Under `greedy-clique` that means no event holds two moments of one coin. Under `component` it does **not**: a component is a chain, and two moments of one coin still land in one event when both are joined to a moment of another coin. The column "events holding 2+ cards of one coin" below counts it.

## What each reading counts

| configuration | events | cards per event | events of size 1 | largest event | events holding both kinds | events holding more than one coin | events holding 2+ cards of one coin | largest same-coin count | block: events that cannot move | block: cards in them |
|---|---|---|---|---|---|---|---|---|---|---|
| `none/none/none` | 306 | 1.00 | 306 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| `start-hour/component/any` | 289 | 1.06 | 274 | 3 | 2 | 15 | 0 | 1 | 0 | 0 |
| `start-hour/component/cross-coin` | 289 | 1.06 | 274 | 3 | 2 | 15 | 0 | 1 | 0 | 0 |
| `move-window/component/any` | 131 | 2.34 | 49 | 8 | 52 | 80 | 15 | 2 | 1 | 8 |
| `move-window/component/cross-coin` | 136 | 2.25 | 56 | 8 | 52 | 80 | 10 | 2 | 1 | 8 |
| `move-window/greedy-clique/any` | 161 | 1.90 | 68 | 6 | 49 | 88 | 10 | 2 | 1 | 5 |
| `move-window/greedy-clique/cross-coin` | 168 | 1.82 | 78 | 6 | 50 | 90 | 0 | 1 | 1 | 5 |
| `card-span/component/any` | 58 | 5.28 | 10 | 20 | 37 | 47 | 25 | 5 | 2 | 23 |
| `card-span/component/cross-coin` | 62 | 4.94 | 13 | 20 | 39 | 49 | 26 | 4 | 3 | 44 |
| `card-span/greedy-clique/any` | 116 | 2.64 | 32 | 7 | 56 | 83 | 13 | 3 | 0 | 0 |
| `card-span/greedy-clique/cross-coin` | 125 | 2.45 | 41 | 7 | 60 | 84 | 0 | 1 | 0 | 0 |

"Events holding both kinds": an event holding a `large` card and a `calm` card has no single label. "Block: events that cannot move": an event whose size no other event shares is mapped onto itself in every block draw.

## What collapsing does to a shuffle

RULES 12 fixes the shuffle at 1,000 draws and the line at the best 1%. The two answer vectors below are **synthetic**, drawn from seed `20260913`: `synthetic-iid` is one independent coin flip per card, `synthetic-event-constant` is one coin flip per event of the same configuration, repeated on every card in it. No rule from the canteen book is evaluated here and no result about any rule is produced. The block column is computed through `chance_line()`. The representative column keeps, for this calibration only, the earliest card of each event (ties: lowest id); that is not a ruling on which card represents an event.

| configuration | predictor | n cards | card-level shuffle · 1% boundary | cluster-level (block) shuffle · 1% boundary | n events | representative-collapse shuffle · 1% boundary |
|---|---|---|---|---|---|---|
| `none/none/none` | synthetic-iid | 306 | 0.5719 | 0.5588 | 306 | 0.5654 |
| `none/none/none` | synthetic-event-constant | 306 | 0.5719 | 0.5588 | 306 | 0.5654 |
| `start-hour/component/any` | synthetic-iid | 306 | 0.5719 | 0.5523 | 289 | 0.5744 |
| `start-hour/component/any` | synthetic-event-constant | 306 | 0.5654 | 0.5588 | 289 | 0.5744 |
| `start-hour/component/cross-coin` | synthetic-iid | 306 | 0.5719 | 0.5523 | 289 | 0.5744 |
| `start-hour/component/cross-coin` | synthetic-event-constant | 306 | 0.5654 | 0.5588 | 289 | 0.5744 |
| `move-window/component/any` | synthetic-iid | 306 | 0.5719 | 0.5654 | 131 | 0.6031 |
| `move-window/component/any` | synthetic-event-constant | 306 | 0.5621 | 0.5948 | 131 | 0.6031 |
| `move-window/component/cross-coin` | synthetic-iid | 306 | 0.5719 | 0.5654 | 136 | 0.5882 |
| `move-window/component/cross-coin` | synthetic-event-constant | 306 | 0.5654 | 0.5980 | 136 | 0.5882 |
| `move-window/greedy-clique/any` | synthetic-iid | 306 | 0.5719 | 0.5654 | 161 | 0.5901 |
| `move-window/greedy-clique/any` | synthetic-event-constant | 306 | 0.5588 | 0.5980 | 161 | 0.5901 |
| `move-window/greedy-clique/cross-coin` | synthetic-iid | 306 | 0.5719 | 0.5588 | 168 | 0.5893 |
| `move-window/greedy-clique/cross-coin` | synthetic-event-constant | 306 | 0.5621 | 0.5752 | 168 | 0.5893 |
| `card-span/component/any` | synthetic-iid | 306 | 0.5719 | 0.5588 | 58 | 0.6552 |
| `card-span/component/any` | synthetic-event-constant | 306 | 0.5686 | 0.5621 | 58 | 0.6552 |
| `card-span/component/cross-coin` | synthetic-iid | 306 | 0.5719 | 0.5588 | 62 | 0.6613 |
| `card-span/component/cross-coin` | synthetic-event-constant | 306 | 0.5654 | 0.5523 | 62 | 0.6613 |
| `card-span/greedy-clique/any` | synthetic-iid | 306 | 0.5719 | 0.5523 | 116 | 0.6121 |
| `card-span/greedy-clique/any` | synthetic-event-constant | 306 | 0.5621 | 0.6013 | 116 | 0.6121 |
| `card-span/greedy-clique/cross-coin` | synthetic-iid | 306 | 0.5719 | 0.5458 | 125 | 0.6000 |
| `card-span/greedy-clique/cross-coin` | synthetic-event-constant | 306 | 0.5654 | 0.5719 | 125 | 0.6000 |

## Fingerprints

| file | rows | SHA-256 |
|---|---|---|
| `exam-prep/review-4/rerun/collapse/run-a0ecf6970d86b199/events.csv` | 3366 | `7d887b831847b8838735ec0db334238cda51d9709ec6d7c97a1aa12f1faba727` |
| `exam-prep/review-4/rerun/collapse/run-a0ecf6970d86b199/collapse-summary.csv` | 11 | `94d9205c77918551b4fbe0df9806abdf14d0599ae96ed911553e446652676bcd` |
| `exam-prep/review-4/rerun/collapse/run-a0ecf6970d86b199/shuffle-calibration.csv` | 22 | `0c4b27f9556086644ff5ad9137322a06854f64b78daf9bf1babebd73115b5cd7` |

