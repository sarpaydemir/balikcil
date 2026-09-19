# Identity audit — card set `blinded-rank`

Written by `scripts/16_identity_audit.py`. It attacks the cards with what an exam candidate can see and measures the result against a permutation chance line. It applies no rule and proposes no fix.

| field | value |
|---|---|
| run number (RULES 29) | `3b1cb7d540d11283` |
| full input fingerprint | `3b1cb7d540d11283b964516268113596ecc15f7933e17df7bf0aec85c2ea6af2` |
| written at (system clock, UTC, RULES 23) | 2026-09-19T14:09:55Z |
| free disk space at start (bytes) | 16111878144 |
| card folder | `exam-prep/blind-proof/rank/cards` |
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
| `price-level` | 1 | 0.153595 | 0.179739 | no | 0.503476 | 0.512978 | no |
| `volatility-frozen` | 3 | 0.160131 | 0.176471 | no | 0.542629 | 0.513267 | YES |
| `volume-level` | 2 | 0.183007 | 0.179739 | YES | 0.527862 | 0.512206 | YES |
| `trades-level` | 2 | 0.196078 | 0.179739 | YES | 0.529441 | 0.513128 | YES |
| `openint-level` | 1 | 0.130719 | 0.153595 | no | 0.513841 | 0.511796 | YES |
| `depth-level` | 2 | 0.147059 | 0.147059 | no | 0.504425 | 0.510421 | no |
| `ratio-level` | 3 | 0.127451 | 0.176471 | no | 0.489869 | 0.513598 | no |
| `taker-buy` | 2 | 0.166667 | 0.179739 | no | 0.563111 | 0.513622 | YES |
| `funding-line` | 4 | 0.153595 | 0.173203 | no | 0.592679 | 0.5112 | YES |
| `wikipedia-presence` | 0 |  |  | no features left after blinding |  |  | no features left after blinding |
| `p7-shape` | 2 | 0.150327 | 0.179739 | no | 0.5239 | 0.513163 | YES |
| `btc-eth` | 0 |  |  | no features left after blinding |  |  | no features left after blinding |
| `shape-scale-free` | 13 | 0.147059 | 0.173203 | no | 0.512016 | 0.512623 | no |
| `ALL` | 35 | 0.29085 | 0.169935 | YES | 0.536044 | 0.51469 | YES |
| `ALL-except-frozen-volatility` | 32 | 0.287582 | 0.169935 | YES | 0.532986 | 0.514298 | YES |
| `ALL-removable` | 26 | 0.232026 | 0.169935 | YES | 0.520307 | 0.513273 | YES |

## T3 — does the card say which clock hours it covers?

Two cards are "detected" as covering the same hours when they print 3 consecutive rows that are identical in the named column(s). The truth is the start hours: two cards share a clock hour when their 48-hour spans intersect (the relation `14_overlap_map.py` measured).

| columns used | pairs | truly sharing an hour | detected | detection rate | false positives | false-positive rate | note |
|---|---|---|---|---|---|---|---|
| `BTC+ETH` | 0 | 0 | 0 |  | 0 |  | column(s) not printed on this card set |
| `chg%` | 46665 | 495 | 10 | 0.020202 | 1 | 2.2e-05 | 3 consecutive identical rows |
| `close` | 46665 | 495 | 0 | 0.0 | 2 | 4.3e-05 | 3 consecutive identical rows |
| `quote vol` | 0 | 0 | 0 |  | 0 |  | column(s) not printed on this card set |

## Fingerprints

| file | SHA-256 |
|---|---|
| `exam-prep/identity/identity-audit-blinded-rank.csv` | `4b24272ad07cfa0bde6d23925d4f10aa3947642a475d9c35a49482b89fca2c5c` |
| `exam-prep/identity/hour-linkage-blinded-rank.csv` | `4ebba376b70d226d47bae572feff87a5dc4be658b3f5e0381b22ef7a75c4fa01` |

