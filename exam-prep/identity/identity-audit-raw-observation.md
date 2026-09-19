# Identity audit — card set `raw-observation`

Written by `scripts/16_identity_audit.py`. It attacks the cards with what an exam candidate can see and measures the result against a permutation chance line. It applies no rule and proposes no fix.

| field | value |
|---|---|
| run number (RULES 29) | `3c090e41041104e0` |
| full input fingerprint | `3c090e41041104e07dc76d71d5332040fb7c79622ab14ecb2e6171a88d4ab856` |
| written at (system clock, UTC, RULES 23) | 2026-09-19T14:09:00Z |
| free disk space at start (bytes) | 16111890432 |
| card folder | `cards` |
| cards | 306 |
| distinct coins | 10 |
| shuffles (RULES 12) | 1000 |
| boundary (RULES 12) | best 1.0% |
| seed (TACTICS 1 draw number) | `20260913` |
| `scripts/16_identity_audit.py` SHA-256 | `4c4928b84ff9b484995058c2dd4e5b043af1491b60f314e1a0f418dd90e4a371` |

## T1 and T2 — does the card say which coin it is?

`nearest-neighbour` = leave one card out, find the closest other card in this family's features, ask whether it is the same coin. `pair AUC` = over all 46665 pairs, how well the distance separates a same-coin pair from a different-coin pair; 0.5 is no information. Both chance lines are the boundary of the best 1% of 1000 coin-label shuffles.

| feature family | features | nearest-neighbour same-coin | chance line | beats chance | pair AUC | chance line | beats chance |
|---|---|---|---|---|---|---|---|
| `price-level` | 1 | 0.637255 | 0.179739 | YES | 0.909321 | 0.512881 | YES |
| `volatility-frozen` | 3 | 0.160131 | 0.176471 | no | 0.542629 | 0.513458 | YES |
| `volume-level` | 2 | 0.366013 | 0.176471 | YES | 0.727393 | 0.512781 | YES |
| `trades-level` | 2 | 0.277778 | 0.173203 | YES | 0.71236 | 0.51217 | YES |
| `openint-level` | 1 | 0.751634 | 0.179739 | YES | 0.925362 | 0.513152 | YES |
| `depth-level` | 2 | 0.441176 | 0.179739 | YES | 0.838113 | 0.513689 | YES |
| `ratio-level` | 3 | 0.464052 | 0.179739 | YES | 0.649369 | 0.513486 | YES |
| `taker-buy` | 2 | 0.186275 | 0.173203 | YES | 0.571071 | 0.511815 | YES |
| `funding-line` | 5 | 0.428105 | 0.173203 | YES | 0.719539 | 0.513795 | YES |
| `wikipedia-presence` | 1 | 0.176471 | 0.150327 | YES | 0.629541 | 0.510776 | YES |
| `p7-shape` | 2 | 0.150327 | 0.183007 | no | 0.5239 | 0.514334 | YES |
| `btc-eth` | 4 | 0.078431 | 0.173203 | no | 0.488021 | 0.514125 | no |
| `shape-scale-free` | 13 | 0.189542 | 0.176471 | YES | 0.566219 | 0.512203 | YES |
| `ALL` | 41 | 0.637255 | 0.173203 | YES | 0.728644 | 0.513204 | YES |
| `ALL-except-frozen-volatility` | 38 | 0.637255 | 0.169935 | YES | 0.732029 | 0.512654 | YES |
| `ALL-removable` | 31 | 0.601307 | 0.173203 | YES | 0.716461 | 0.513732 | YES |

## T3 — does the card say which clock hours it covers?

Two cards are "detected" as covering the same hours when they print 3 consecutive rows that are identical in the named column(s). The truth is the start hours: two cards share a clock hour when their 48-hour spans intersect (the relation `14_overlap_map.py` measured).

| columns used | pairs | truly sharing an hour | detected | detection rate | false positives | false-positive rate | note |
|---|---|---|---|---|---|---|---|
| `BTC+ETH` | 46665 | 495 | 243 | 0.490909 | 0 | 0.0 | 3 consecutive identical rows |
| `chg%` | 46665 | 495 | 10 | 0.020202 | 1 | 2.2e-05 | 3 consecutive identical rows |
| `close` | 46665 | 495 | 10 | 0.020202 | 0 | 0.0 | 3 consecutive identical rows |
| `quote vol` | 46665 | 495 | 10 | 0.020202 | 0 | 0.0 | 3 consecutive identical rows |

## Fingerprints

| file | SHA-256 |
|---|---|
| `exam-prep/identity/identity-audit-raw-observation.csv` | `904b51057baf1cde00ea0ecab5d2627f4da5c2ed0c507ec294169782f828ad7c` |
| `exam-prep/identity/hour-linkage-raw-observation.csv` | `967458ff6a1b390bd2c8bdc2d338f179095e255776432092bdd033456d13ea59` |

