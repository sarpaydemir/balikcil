# Identity audit — card set `blinded-ratio`

Written by `scripts/16_identity_audit.py`. It attacks the cards with what an exam candidate can see and measures the result against a permutation chance line. It applies no rule and proposes no fix.

| field | value |
|---|---|
| run number (RULES 29) | `d91cfc33459a0270` |
| full input fingerprint | `d91cfc33459a0270289fd7a8d939601fd3c230533273f726ad2d172bde0e8bc6` |
| written at (system clock, UTC, RULES 23) | 2026-10-01T19:12:03Z |
| free disk space at start (bytes) | 12502163456 |
| card folder | `exam-prep/blind-proof/ratio/cards` |
| cards | 306 |
| distinct coins | 10 |
| shuffles (RULES 12) | 1000 |
| boundary (RULES 12) | best 1.0% |
| seed (TACTICS 1 draw number) | `20260913` |
| `scripts/16_identity_audit.py` SHA-256 | `4dfd9fd12de458e499ceeea88d9f445d10f853fd21ccb22dc407185a5b767a91` |

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
| `repeat-close` | 2 | 0.160131 | 0.166667 | no | 0.542144 | 0.510666 | YES |
| `repeat-chg` | 2 | 0.101307 | 0.166667 | no | 0.523074 | 0.512879 | YES |
| `repeat-volume` | 2 | 0.071895 | 0.160131 | no | 0.502178 | 0.511858 | no |
| `repeat-trades` | 2 | 0.232026 | 0.173203 | YES | 0.58522 | 0.512746 | YES |
| `repeat-takerbuy` | 2 | 0.130719 | 0.169935 | no | 0.505484 | 0.513182 | no |
| `repeat-openint` | 2 | 0.111111 | 0.169935 | no | 0.53459 | 0.512409 | YES |
| `repeat-ratio` | 6 | 0.186275 | 0.176471 | YES | 0.563859 | 0.51252 | YES |
| `repeat-depth` | 4 | 0.199346 | 0.176471 | YES | 0.538332 | 0.512939 | YES |
| `repeat-btceth` | 0 |  |  | no features left after blinding |  |  | no features left after blinding |
| `ALL` | 50 | 0.421569 | 0.176471 | YES | 0.615864 | 0.512144 | YES |
| `ALL-except-frozen-volatility` | 47 | 0.411765 | 0.173203 | YES | 0.615208 | 0.512029 | YES |
| `ALL-removable` | 39 | 0.382353 | 0.176471 | YES | 0.61048 | 0.511921 | YES |

## The gate rows — `ALL-removable`, both attacks

`ALL-removable` is every family except the forced ones (`volatility-frozen`, `funding-line`, `p7-shape`, `repeat-chg`). Both attacks are printed. **This report does not say which of them decides the acceptance gate**; that is open question JQ-R04-GATE (`exam-prep/second-fix/juror-questions/JQ-R04-GATE.md`).

| attack | observed | chance line (best 1%) | beats it |
|---|---|---|---|
| nearest-neighbour same-coin | 0.382353 | 0.176471 | YES |
| pair AUC | 0.61048 | 0.511921 | YES |

## T3 — does the card say which clock hours it covers?

Two cards are "detected" as covering the same hours when they print 3 consecutive rows that are identical in the named column(s). The truth is the start hours: two cards share a clock hour when their 48-hour spans intersect (the relation `14_overlap_map.py` measured).

| columns used | pairs | truly sharing an hour | detected | detection rate | false positives | false-positive rate | note |
|---|---|---|---|---|---|---|---|
| `BTC+ETH` | 0 | 0 | 0 |  | 0 |  | column(s) not printed on this card set |
| `chg%` | 46665 | 495 | 10 | 0.020202 | 1 | 2.2e-05 | 3 consecutive identical rows |
| `close` | 46665 | 495 | 0 | 0.0 | 2 | 4.3e-05 | 3 consecutive identical rows |
| `quote vol` | 0 | 0 | 0 |  | 0 |  | column(s) not printed on this card set |
| `bullet:US releases` | 46665 | 495 | 8 | 0.016162 | 15 | 0.000325 | the whole bullet text identical, the default 'none' text excluded |

## T4 — release names that sit on one calendar day of this set

A count, not an attack: a release that a reader can date from public knowledge dates the card that prints it (REVIEW §3.4). Computed against the truth file.

| quantity | count |
|---|---|
| cards printing at least one release name | 100 of 306 |
| distinct release names | 30 |
| names that occur on exactly one calendar day of this set | 11 |
| cards carrying such a name | 13 |

## Fingerprints

| file | SHA-256 |
|---|---|
| `exam-prep/second-fix/identity/run-d91cfc33459a0270/identity-audit-blinded-ratio.csv` | `bb8249b6ba2b1704cdf37d804b6b988e82b7d16feead102a0f79b40c31e0c7ed` |
| `exam-prep/second-fix/identity/run-d91cfc33459a0270/hour-linkage-blinded-ratio.csv` | `c0f739f843f0dedd636328d5febaa9adc0a81ffd1f410da9e75ac8e73eddbe33` |

