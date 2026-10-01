# Identity audit — card set `blinded-rank`

Written by `scripts/16_identity_audit.py`. It attacks the cards with what an exam candidate can see and measures the result against a permutation chance line. It applies no rule and proposes no fix.

| field | value |
|---|---|
| run number (RULES 29) | `5fce3f6fbe815bae` |
| full input fingerprint | `5fce3f6fbe815baee9ed7d075fa14a0b631e2facdb278fa701c7969e166c37b8` |
| written at (system clock, UTC, RULES 23) | 2026-10-01T19:41:12Z |
| free disk space at start (bytes) | 12427255808 |
| card folder | `exam-prep/blind-proof/rank/cards` |
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
| `repeat-close` | 2 | 0.160131 | 0.166667 | no | 0.542144 | 0.510666 | YES |
| `repeat-chg` | 2 | 0.101307 | 0.166667 | no | 0.523074 | 0.512879 | YES |
| `repeat-volume` | 2 | 0.163399 | 0.153595 | YES | 0.506038 | 0.511512 | no |
| `repeat-trades` | 2 | 0.232026 | 0.173203 | YES | 0.58522 | 0.512746 | YES |
| `repeat-takerbuy` | 2 | 0.130719 | 0.169935 | no | 0.505484 | 0.513182 | no |
| `repeat-openint` | 2 | 0.143791 | 0.173203 | no | 0.621051 | 0.513329 | YES |
| `repeat-ratio` | 6 | 0.186275 | 0.176471 | YES | 0.563942 | 0.51247 | YES |
| `repeat-depth` | 4 | 0.222222 | 0.169935 | YES | 0.535063 | 0.51332 | YES |
| `repeat-btceth` | 0 |  |  | no features left after blinding |  |  | no features left after blinding |
| `ALL` | 57 | 0.408497 | 0.169935 | YES | 0.584749 | 0.513403 | YES |
| `ALL-except-frozen-volatility` | 54 | 0.415033 | 0.173203 | YES | 0.583953 | 0.513282 | YES |
| `ALL-removable` | 46 | 0.434641 | 0.169935 | YES | 0.577283 | 0.513169 | YES |

## The gate rows — `ALL-removable`, both attacks

`ALL-removable` is every family except the forced ones (`volatility-frozen`, `funding-line`, `p7-shape`, `repeat-chg`). Both attacks are printed. **This report does not say which of them decides the acceptance gate**; that is open question JQ-R04-GATE (`exam-prep/second-fix/juror-questions/JQ-R04-GATE.md`).

| attack | observed | chance line (best 1%) | beats it |
|---|---|---|---|
| nearest-neighbour same-coin | 0.434641 | 0.169935 | YES |
| pair AUC | 0.577283 | 0.513169 | YES |

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
| `exam-prep/review-2/rerun/identity/run-5fce3f6fbe815bae/identity-audit-blinded-rank.csv` | `a90d32ebf5fc26018ac1f827df50efe82df3d66fe0197acd397356c7f5f4156e` |
| `exam-prep/review-2/rerun/identity/run-5fce3f6fbe815bae/hour-linkage-blinded-rank.csv` | `11f07aa54741e567e5235796b761959e8b662ae2570ac79f36c2b69088386b50` |

