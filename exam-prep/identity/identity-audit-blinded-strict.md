# Identity audit — card set `blinded-strict`

Written by `scripts/16_identity_audit.py`. It attacks the cards with what an exam candidate can see and measures the result against a permutation chance line. It applies no rule and proposes no fix.

| field | value |
|---|---|
| run number (RULES 29) | `23502d75682cc455` |
| full input fingerprint | `23502d75682cc45545452265dd28e628d316d244bf463015b22fdde79c9499f7` |
| written at (system clock, UTC, RULES 23) | 2026-09-19T14:10:22Z |
| free disk space at start (bytes) | 16111869952 |
| card folder | `exam-prep/blind-proof/strict/cards` |
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
| `volume-level` | 1 | 0.127451 | 0.137255 | no | 0.499191 | 0.504875 | no |
| `trades-level` | 1 | 0.130719 | 0.166667 | no | 0.529516 | 0.513496 | YES |
| `openint-level` | 1 | 0.130719 | 0.153595 | no | 0.513841 | 0.511796 | YES |
| `depth-level` | 2 | 0.147059 | 0.147059 | no | 0.504425 | 0.510421 | no |
| `ratio-level` | 3 | 0.127451 | 0.176471 | no | 0.489869 | 0.513598 | no |
| `taker-buy` | 1 | 0.120915 | 0.166667 | no | 0.496313 | 0.514336 | no |
| `funding-line` | 4 | 0.153595 | 0.173203 | no | 0.592679 | 0.5112 | YES |
| `wikipedia-presence` | 0 |  |  | no features left after blinding |  |  | no features left after blinding |
| `p7-shape` | 2 | 0.150327 | 0.179739 | no | 0.5239 | 0.513163 | YES |
| `btc-eth` | 0 |  |  | no features left after blinding |  |  | no features left after blinding |
| `shape-scale-free` | 13 | 0.147059 | 0.173203 | no | 0.512016 | 0.512623 | no |
| `ALL` | 32 | 0.264706 | 0.169935 | YES | 0.523074 | 0.514788 | YES |
| `ALL-except-frozen-volatility` | 29 | 0.235294 | 0.169935 | YES | 0.520405 | 0.515147 | YES |
| `ALL-removable` | 23 | 0.189542 | 0.166667 | YES | 0.504928 | 0.513011 | no |

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
| `exam-prep/identity/identity-audit-blinded-strict.csv` | `69677b422ca21ca2991cefa7459ce343bc5f5803dbf4838f3c1e0f0f740b8586` |
| `exam-prep/identity/hour-linkage-blinded-strict.csv` | `31744f099320b07d78caec0849a7e4604216a4f8fea8f30af94ed79785c6d495` |

