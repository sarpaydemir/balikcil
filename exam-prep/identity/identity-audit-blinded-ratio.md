# Identity audit — card set `blinded-ratio`

Written by `scripts/16_identity_audit.py`. It attacks the cards with what an exam candidate can see and measures the result against a permutation chance line. It applies no rule and proposes no fix.

| field | value |
|---|---|
| run number (RULES 29) | `b8230e324e0c03e6` |
| full input fingerprint | `b8230e324e0c03e6e89b9630a0a9735b46945ae65d2d675d2ffe8a4cc953d4b9` |
| written at (system clock, UTC, RULES 23) | 2026-09-19T14:09:32Z |
| free disk space at start (bytes) | 16111882240 |
| card folder | `exam-prep/blind-proof/ratio/cards` |
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
| `volume-level` | 1 | 0.186275 | 0.179739 | YES | 0.528896 | 0.512822 | YES |
| `trades-level` | 1 | 0.212418 | 0.176471 | YES | 0.52623 | 0.513451 | YES |
| `openint-level` | 1 | 0.127451 | 0.133987 | no | 0.505179 | 0.503379 | YES |
| `depth-level` | 0 |  |  | no features left after blinding |  |  | no features left after blinding |
| `ratio-level` | 0 |  |  | no features left after blinding |  |  | no features left after blinding |
| `taker-buy` | 2 | 0.166667 | 0.179739 | no | 0.563111 | 0.513622 | YES |
| `funding-line` | 4 | 0.153595 | 0.173203 | no | 0.592679 | 0.5112 | YES |
| `wikipedia-presence` | 0 |  |  | no features left after blinding |  |  | no features left after blinding |
| `p7-shape` | 2 | 0.150327 | 0.179739 | no | 0.5239 | 0.513163 | YES |
| `btc-eth` | 0 |  |  | no features left after blinding |  |  | no features left after blinding |
| `shape-scale-free` | 13 | 0.196078 | 0.173203 | YES | 0.566272 | 0.514272 | YES |
| `ALL` | 28 | 0.310458 | 0.169935 | YES | 0.588218 | 0.513431 | YES |
| `ALL-except-frozen-volatility` | 25 | 0.294118 | 0.173203 | YES | 0.586293 | 0.513674 | YES |
| `ALL-removable` | 19 | 0.212418 | 0.169935 | YES | 0.572619 | 0.513541 | YES |

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
| `exam-prep/identity/identity-audit-blinded-ratio.csv` | `693442d4f6cf69b293797ee904adf302654e2b4b426048d9762e0aaf5f7610e2` |
| `exam-prep/identity/hour-linkage-blinded-ratio.csv` | `6cc5dd02ac6a7f824addd22290b69414715c74757d9d9fbcc4f96c812f56302b` |

