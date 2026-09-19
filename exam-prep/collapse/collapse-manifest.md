# Collapse manifest — the event map RULES 13 needs

Written by `scripts/15_event_collapse.py`. It builds every candidate reading of RULES 13's "the same hour" and measures each. **It chooses none of them.** The choice is an open question under RULES 33 and is stated in `exam-prep/N-1-collapse.md`.

## Run

| field | value |
|---|---|
| run number (SHA-256 of the inputs, RULES 29) | `386d234b85269a21` |
| full input fingerprint | `386d234b85269a214440e46a155781ad31ce2de0109a3a73b8bc93501d207a08` |
| written at (system clock, UTC, RULES 23) | 2026-09-19T14:18:31Z |
| free disk space at start (bytes) | 16111312896 |
| moments read | 306 |
| input | the 306 cards in `cards/` |
| shuffles (RULES 12) | 1000 |
| boundary (RULES 12) | best 1.0% |
| seed (TACTICS 1 draw number) | `20260913` |
| `scripts/15_event_collapse.py` SHA-256 | `f3de235883aac8b364aa5391c8371d50a9ecca288007f8d0bfaadadafe0ffb12` |

Run records live in `runs/`, one JSON per run number, append-only (RULES 30). Records present when this manifest was written: `386d234b85269a21`, `4af3b344a4898af0`, `5ba9140fe3c467fa`.

## The candidate readings

| name | what counts as "the same hour" | largest start gap that still merges |
|---|---|---|
| `start-hour` | the two moments begin in the same clock hour (TACTICS 2: a moment's start is the hour the 24-hour movement began) | 0 h |
| `move-window` | the two 24-hour movements share a clock hour | 23 h |
| `card-span` | the two 48-hour card spans share a clock hour — the relation `14_overlap_map.py` measured | 47 h |

`component` = anything chained together is one event. `greedy-clique` = repeatedly take the clock hour covered by the most still-unassigned moments (ties: earliest hour, then lowest id). `greedy-clique` is a **stated convention**, not an observation: overlapping intervals have no unique partition into "groups sharing an hour", so some deterministic rule is needed and this one is written down so it can be disagreed with.

`any` = two moments of the same coin may merge. `cross-coin` = they may not, because RULES 13 says "in several coins" and same-coin spacing is a separate open question.

## What each reading counts

| configuration | events | cards per event | events of size 1 | largest event | events holding both kinds | events holding more than one coin |
|---|---|---|---|---|---|---|
| `none/none/none` | 306 | 1.00 | 306 | 1 | 0 | 0 |
| `start-hour/component/any` | 289 | 1.06 | 274 | 3 | 2 | 15 |
| `start-hour/component/cross-coin` | 289 | 1.06 | 274 | 3 | 2 | 15 |
| `move-window/component/any` | 131 | 2.34 | 49 | 8 | 52 | 80 |
| `move-window/component/cross-coin` | 136 | 2.25 | 56 | 8 | 52 | 80 |
| `move-window/greedy-clique/any` | 161 | 1.90 | 68 | 6 | 49 | 88 |
| `move-window/greedy-clique/cross-coin` | 168 | 1.82 | 78 | 6 | 50 | 90 |
| `card-span/component/any` | 58 | 5.28 | 10 | 20 | 37 | 47 |
| `card-span/component/cross-coin` | 62 | 4.94 | 13 | 20 | 39 | 49 |
| `card-span/greedy-clique/any` | 116 | 2.64 | 32 | 7 | 56 | 83 |
| `card-span/greedy-clique/cross-coin` | 125 | 2.45 | 41 | 7 | 60 | 84 |

"Events holding both kinds" is the count that matters for a judge: an event holding a `large` card and a `calm` card has no single label, so a scheme that replaces an event by one answer cannot be used on it. The column is measured, not argued.

## What collapsing does to a shuffle

RULES 12 fixes the shuffle at 1,000 draws and the line at the best 1%. The two answer vectors below are **synthetic**, drawn from seed `20260913`: `synthetic-iid` is one independent coin flip per card, `synthetic-event-constant` is one coin flip per event of the same configuration, repeated on every card in it. No rule from the canteen book is evaluated here and no result about any rule is produced. The point of the table is the **width of the null**, which is a property of the shuffle scheme and the labels, not of any signal.

| configuration | predictor | n cards | card-level shuffle · 1% boundary | cluster-level (block) shuffle · 1% boundary | n events | representative-collapse shuffle · 1% boundary |
|---|---|---|---|---|---|---|
| `none/none/none` | synthetic-iid | 306 | 0.5719 | 0.5588 | 306 | 0.5654 |
| `none/none/none` | synthetic-event-constant | 306 | 0.5719 | 0.5588 | 306 | 0.5654 |
| `start-hour/component/any` | synthetic-iid | 306 | 0.5719 | 0.5719 | 289 | 0.5744 |
| `start-hour/component/any` | synthetic-event-constant | 306 | 0.5654 | 0.5654 | 289 | 0.5744 |
| `start-hour/component/cross-coin` | synthetic-iid | 306 | 0.5719 | 0.5719 | 289 | 0.5744 |
| `start-hour/component/cross-coin` | synthetic-event-constant | 306 | 0.5654 | 0.5654 | 289 | 0.5744 |
| `move-window/component/any` | synthetic-iid | 306 | 0.5719 | 0.5654 | 131 | 0.6031 |
| `move-window/component/any` | synthetic-event-constant | 306 | 0.5621 | 0.5817 | 131 | 0.6031 |
| `move-window/component/cross-coin` | synthetic-iid | 306 | 0.5719 | 0.5654 | 136 | 0.5882 |
| `move-window/component/cross-coin` | synthetic-event-constant | 306 | 0.5654 | 0.5784 | 136 | 0.5882 |
| `move-window/greedy-clique/any` | synthetic-iid | 306 | 0.5719 | 0.5654 | 161 | 0.5901 |
| `move-window/greedy-clique/any` | synthetic-event-constant | 306 | 0.5588 | 0.5719 | 161 | 0.5901 |
| `move-window/greedy-clique/cross-coin` | synthetic-iid | 306 | 0.5719 | 0.5588 | 168 | 0.5893 |
| `move-window/greedy-clique/cross-coin` | synthetic-event-constant | 306 | 0.5621 | 0.5752 | 168 | 0.5893 |
| `card-span/component/any` | synthetic-iid | 306 | 0.5719 | 0.5654 | 58 | 0.6552 |
| `card-span/component/any` | synthetic-event-constant | 306 | 0.5686 | 0.5817 | 58 | 0.6552 |
| `card-span/component/cross-coin` | synthetic-iid | 306 | 0.5719 | 0.5654 | 62 | 0.6613 |
| `card-span/component/cross-coin` | synthetic-event-constant | 306 | 0.5654 | 0.5784 | 62 | 0.6613 |
| `card-span/greedy-clique/any` | synthetic-iid | 306 | 0.5719 | 0.5588 | 116 | 0.6121 |
| `card-span/greedy-clique/any` | synthetic-event-constant | 306 | 0.5621 | 0.5817 | 116 | 0.6121 |
| `card-span/greedy-clique/cross-coin` | synthetic-iid | 306 | 0.5719 | 0.5654 | 125 | 0.6000 |
| `card-span/greedy-clique/cross-coin` | synthetic-event-constant | 306 | 0.5654 | 0.5719 | 125 | 0.6000 |

The last column is the one that moves. Keeping every card and only permuting whole events (the middle column) barely widens the null, because the overlapping cards do not carry the same label — see the "events holding both kinds" column above. Replacing each event by one card (the last column) widens it a great deal, because the null is then drawn over n = events.

## Fingerprints

| file | rows | SHA-256 |
|---|---|---|
| `exam-prep/collapse/events.csv` | 3366 | `7d887b831847b8838735ec0db334238cda51d9709ec6d7c97a1aa12f1faba727` |
| `exam-prep/collapse/collapse-summary.csv` | 11 | `6f3f5ce5748fc5e9d95086d07bbd6f7db9b00539b1df4445463a2df01f1400f5` |
| `exam-prep/collapse/shuffle-calibration.csv` | 22 | `145069adbb97faae4533c98bd009e7163200588942a5f57956a7eaf1981a6a66` |

