# Identity audit — card set `raw-observation`

Written by `scripts/16_identity_audit.py`. It attacks the cards with what an exam candidate can see and measures the result against a permutation chance line. It applies no rule and proposes no fix.

| field | value |
|---|---|
| run number (RULES 29) | `13d935bb5cf78346` |
| full input fingerprint | `13d935bb5cf78346e698d1614f2485a4348c59ed1814ed145eca79ef7e79c018` |
| written at (system clock, UTC, RULES 23) | 2026-10-01T19:11:12Z |
| free disk space at start (bytes) | 12509528064 |
| card folder | `cards` |
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
| `repeat-close` | 2 | 0.075163 | 0.166667 | no | 0.563626 | 0.513268 | YES |
| `repeat-chg` | 2 | 0.062092 | 0.160131 | no | 0.523074 | 0.51347 | YES |
| `repeat-volume` | 2 | 0.042484 | 0.150327 | no | 0.506038 | 0.512154 | no |
| `repeat-trades` | 2 | 0.215686 | 0.176471 | YES | 0.58522 | 0.513129 | YES |
| `repeat-takerbuy` | 2 | 0.058824 | 0.163399 | no | 0.502733 | 0.511336 | no |
| `repeat-openint` | 2 | 0.101307 | 0.173203 | no | 0.621051 | 0.513538 | YES |
| `repeat-ratio` | 6 | 0.186275 | 0.176471 | YES | 0.563942 | 0.512059 | YES |
| `repeat-depth` | 4 | 0.153595 | 0.163399 | no | 0.535063 | 0.513994 | YES |
| `repeat-btceth` | 4 | 0.078431 | 0.173203 | no | 0.497586 | 0.512573 | no |
| `ALL` | 67 | 0.660131 | 0.179739 | YES | 0.717861 | 0.512798 | YES |
| `ALL-except-frozen-volatility` | 64 | 0.669935 | 0.176471 | YES | 0.720524 | 0.512569 | YES |
| `ALL-removable` | 55 | 0.627451 | 0.176471 | YES | 0.709277 | 0.512746 | YES |

## The gate rows — `ALL-removable`, both attacks

`ALL-removable` is every family except the forced ones (`volatility-frozen`, `funding-line`, `p7-shape`, `repeat-chg`). Both attacks are printed. **This report does not say which of them decides the acceptance gate**; that is open question JQ-R04-GATE (`exam-prep/second-fix/juror-questions/JQ-R04-GATE.md`).

| attack | observed | chance line (best 1%) | beats it |
|---|---|---|---|
| nearest-neighbour same-coin | 0.627451 | 0.176471 | YES |
| pair AUC | 0.709277 | 0.512746 | YES |

## T3 — does the card say which clock hours it covers?

Two cards are "detected" as covering the same hours when they print 3 consecutive rows that are identical in the named column(s). The truth is the start hours: two cards share a clock hour when their 48-hour spans intersect (the relation `14_overlap_map.py` measured).

| columns used | pairs | truly sharing an hour | detected | detection rate | false positives | false-positive rate | note |
|---|---|---|---|---|---|---|---|
| `BTC+ETH` | 46665 | 495 | 243 | 0.490909 | 0 | 0.0 | 3 consecutive identical rows |
| `chg%` | 46665 | 495 | 10 | 0.020202 | 1 | 2.2e-05 | 3 consecutive identical rows |
| `close` | 46665 | 495 | 10 | 0.020202 | 0 | 0.0 | 3 consecutive identical rows |
| `quote vol` | 46665 | 495 | 10 | 0.020202 | 0 | 0.0 | 3 consecutive identical rows |
| `bullet:US releases` | 46665 | 495 | 8 | 0.016162 | 0 | 0.0 | the whole bullet text identical, the default 'none' text excluded |

## T4 — release names that sit on one calendar day of this set

A count, not an attack: a release that a reader can date from public knowledge dates the card that prints it (REVIEW §3.4). Computed against the truth file.

| quantity | count |
|---|---|
| cards printing at least one release name | 100 of 306 |
| distinct release names | 87 |
| names that occur on exactly one calendar day of this set | 68 |
| cards carrying such a name | 68 |

## Fingerprints

| file | SHA-256 |
|---|---|
| `exam-prep/second-fix/identity/run-13d935bb5cf78346/identity-audit-raw-observation.csv` | `2bfa60be6993836d39405feb89e56abed3b05cfca9fb02ea76f3d8b75c67f6e7` |
| `exam-prep/second-fix/identity/run-13d935bb5cf78346/hour-linkage-raw-observation.csv` | `d591bebacbb18592695509c08d2da0861d9ec1a2ff2a3d6020aad31e6484facd` |

