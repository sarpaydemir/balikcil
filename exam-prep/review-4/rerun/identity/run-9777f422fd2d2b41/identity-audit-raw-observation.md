# Identity audit — card set `raw-observation`

Written by `scripts/29_identity_audit_exact.py` (the audit of `scripts/16_identity_audit.py` with distances compared exactly, fourth-fix run). It attacks the cards with what an exam candidate can see and measures the result against a permutation chance line. It applies no rule and proposes no fix.

| field | value |
|---|---|
| run number (RULES 29) | `9777f422fd2d2b41` |
| full input fingerprint | `9777f422fd2d2b410b1fa8471e78404deffbd86423ef18e9b25d1692331c5c16` |
| written at (system clock, UTC, RULES 23) | 2026-10-01T21:58:10Z |
| free disk space at start (bytes) | 12395479040 |
| card folder | `cards` |
| cards | 306 |
| distinct coins | 10 |
| shuffles (RULES 12) | 1000 |
| boundary (RULES 12) | best 1.0% |
| seed (TACTICS 1 draw number) | `20260913` |
| `scripts/29_identity_audit_exact.py` SHA-256 | `cfc4bdcb6f1ee65430ac08fad0d085ff6e83510ac4d741145aa32cde3487d03f` |

## T1 and T2 — does the card say which coin it is?

`nearest-neighbour` = leave one card out, find the closest other card in this family's features, ask whether it is the same coin. `pair AUC` = over all 46665 pairs, how well the distance separates a same-coin pair from a different-coin pair; 0.5 is no information. Both chance lines are the boundary of the best 1% of 1000 coin-label shuffles.

| feature family | features | nearest-neighbour same-coin | chance line | beats chance | pair AUC | chance line | beats chance |
|---|---|---|---|---|---|---|---|
| `price-level` | 1 | 0.637255 | 0.179739 | YES | 0.909321 | 0.512881 | YES |
| `volatility-frozen` | 3 | 0.160131 | 0.176471 | no | 0.542629 | 0.513458 | YES |
| `volume-level` | 2 | 0.366013 | 0.176471 | YES | 0.727393 | 0.512781 | YES |
| `trades-level` | 2 | 0.277778 | 0.173203 | YES | 0.712365 | 0.512173 | YES |
| `openint-level` | 1 | 0.751634 | 0.179739 | YES | 0.925362 | 0.513152 | YES |
| `depth-level` | 2 | 0.441176 | 0.179739 | YES | 0.838113 | 0.513689 | YES |
| `ratio-level` | 3 | 0.464052 | 0.179739 | YES | 0.649369 | 0.513486 | YES |
| `taker-buy` | 2 | 0.186275 | 0.173203 | YES | 0.571071 | 0.511815 | YES |
| `funding-line` | 5 | 0.428105 | 0.173203 | YES | 0.719538 | 0.513795 | YES |
| `wikipedia-presence` | 1 | 0.176471 | 0.150327 | YES | 0.629541 | 0.510776 | YES |
| `p7-shape` | 2 | 0.150327 | 0.183007 | no | 0.5239 | 0.514334 | YES |
| `btc-eth` | 4 | 0.078431 | 0.173203 | no | 0.488021 | 0.514125 | no |
| `shape-scale-free` | 13 | 0.189542 | 0.176471 | YES | 0.566219 | 0.512203 | YES |
| `repeat-close` | 2 | 0.075163 | 0.166667 | no | 0.563862 | 0.513194 | YES |
| `repeat-chg` | 2 | 0.062092 | 0.160131 | no | 0.523354 | 0.513649 | YES |
| `repeat-volume` | 2 | 0.042484 | 0.150327 | no | 0.505981 | 0.512135 | no |
| `repeat-trades` | 2 | 0.205882 | 0.176471 | YES | 0.585348 | 0.513105 | YES |
| `repeat-takerbuy` | 2 | 0.058824 | 0.163399 | no | 0.50287 | 0.511422 | no |
| `repeat-openint` | 2 | 0.101307 | 0.173203 | no | 0.621996 | 0.51359 | YES |
| `repeat-ratio` | 6 | 0.186275 | 0.176471 | YES | 0.563942 | 0.512058 | YES |
| `repeat-depth` | 4 | 0.153595 | 0.163399 | no | 0.535053 | 0.513996 | YES |
| `repeat-btceth` | 4 | 0.078431 | 0.173203 | no | 0.497578 | 0.512524 | no |
| `granularity-close` | 1 | 0.424837 | 0.166667 | YES | 0.716709 | 0.513759 | YES |
| `ALL` | 68 | 0.660131 | 0.179739 | YES | 0.71456 | 0.513 | YES |
| `ALL-except-frozen-volatility` | 65 | 0.669935 | 0.176471 | YES | 0.717212 | 0.51287 | YES |
| `ALL-removable` | 56 | 0.624183 | 0.173203 | YES | 0.706435 | 0.512713 | YES |

### Nearest neighbour and tied distances (third-fix run)

The nearest-neighbour score above breaks a distance tie by the lowest card index, so where features tie it depends on how the cards are numbered (REVIEW-2 §4.1). `tie range` is the lowest and highest value that score can take over every tie-break; `tie-free` is its exact mean over every tie-break, which does not depend on card order, with its own chance line from the same 1000 shuffles. Where no card has a tied nearest neighbour the three agree. Distances are compared in exact arithmetic (fourth-fix run, REVIEW-3 §4.1), so a tie here is an exact tie.

| feature family | cards with a tied nearest neighbour | nearest-neighbour (index tie-break) | tie range | tie-free | chance line | beats chance |
|---|---|---|---|---|---|---|
| `price-level` | 1 | 0.637255 | 0.633987 – 0.637255 | 0.635621 | 0.179739 | YES |
| `volatility-frozen` | 0 | 0.160131 | 0.160131 – 0.160131 | 0.160131 | 0.176471 | no |
| `volume-level` | 0 | 0.366013 | 0.366013 – 0.366013 | 0.366013 | 0.176471 | YES |
| `trades-level` | 102 | 0.277778 | 0.22549 – 0.460784 | 0.316471 | 0.169658 | YES |
| `openint-level` | 0 | 0.751634 | 0.751634 – 0.751634 | 0.751634 | 0.179739 | YES |
| `depth-level` | 0 | 0.441176 | 0.441176 – 0.441176 | 0.441176 | 0.179739 | YES |
| `ratio-level` | 0 | 0.464052 | 0.464052 – 0.464052 | 0.464052 | 0.179739 | YES |
| `taker-buy` | 0 | 0.186275 | 0.186275 – 0.186275 | 0.186275 | 0.173203 | YES |
| `funding-line` | 120 | 0.428105 | 0.316993 – 0.689542 | 0.406918 | 0.165551 | YES |
| `wikipedia-presence` | 306 | 0.176471 | 0.130719 – 1.0 | 0.249525 | 0.124498 | YES |
| `p7-shape` | 0 | 0.150327 | 0.150327 – 0.150327 | 0.150327 | 0.183007 | no |
| `btc-eth` | 19 | 0.078431 | 0.071895 – 0.078431 | 0.075163 | 0.173203 | no |
| `shape-scale-free` | 0 | 0.189542 | 0.189542 – 0.189542 | 0.189542 | 0.176471 | YES |
| `repeat-close` | 293 | 0.075163 | 0.009804 – 0.885621 | 0.151031 | 0.137442 | YES |
| `repeat-chg` | 301 | 0.062092 | 0.006536 – 0.928105 | 0.142932 | 0.132629 | YES |
| `repeat-volume` | 304 | 0.042484 | 0.0 – 0.977124 | 0.129737 | 0.129863 | no |
| `repeat-trades` | 236 | 0.205882 | 0.078431 – 0.454248 | 0.213445 | 0.162172 | YES |
| `repeat-takerbuy` | 304 | 0.058824 | 0.006536 – 0.931373 | 0.121157 | 0.133929 | no |
| `repeat-openint` | 289 | 0.101307 | 0.045752 – 0.862745 | 0.202839 | 0.144287 | YES |
| `repeat-ratio` | 5 | 0.186275 | 0.186275 – 0.186275 | 0.186275 | 0.176471 | YES |
| `repeat-depth` | 273 | 0.153595 | 0.088235 – 0.957516 | 0.214744 | 0.142978 | YES |
| `repeat-btceth` | 271 | 0.078431 | 0.009804 – 0.607843 | 0.114688 | 0.149097 | no |
| `granularity-close` | 295 | 0.424837 | 0.140523 – 0.973856 | 0.419882 | 0.140266 | YES |
| `ALL` | 0 | 0.660131 | 0.660131 – 0.660131 | 0.660131 | 0.179739 | YES |
| `ALL-except-frozen-volatility` | 0 | 0.669935 | 0.669935 – 0.669935 | 0.669935 | 0.176471 | YES |
| `ALL-removable` | 0 | 0.624183 | 0.624183 – 0.624183 | 0.624183 | 0.173203 | YES |

## The gate rows — `ALL-removable`, both attacks

`ALL-removable` is every family except the forced ones (`volatility-frozen`, `funding-line`, `p7-shape`, `repeat-chg`). Both attacks are printed. **This report does not say which of them decides the acceptance gate**; that is open question JQ-R04-GATE (`exam-prep/third-fix/juror-questions/JQ-R04-GATE.md`).

| attack | observed | chance line (best 1%) | beats it |
|---|---|---|---|
| nearest-neighbour same-coin | 0.624183 | 0.173203 | YES |
| nearest-neighbour same-coin, tie-free (0 cards with a tied nearest neighbour) | 0.624183 | 0.173203 | YES |
| pair AUC | 0.706435 | 0.512713 | YES |

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
| names that fall on exactly one release day of this set (card start hour + printed offset; a name printed without an offset is keyed by the card's start day) | 85 |
| cards carrying such a name | 99 |

The first two rows of counts above are by the day the card starts (the second-fix definition); the last two by the day the release falls (third-fix). Both measure uniqueness **within this card set**, not how often a release is published.

## Fingerprints

| file | SHA-256 |
|---|---|
| `exam-prep/review-4/rerun/identity/run-9777f422fd2d2b41/identity-audit-raw-observation.csv` | `7623e3052d391ff5dda7af45488d46b97b0bab6a3b7ca11187caac84dd323af9` |
| `exam-prep/review-4/rerun/identity/run-9777f422fd2d2b41/hour-linkage-raw-observation.csv` | `d591bebacbb18592695509c08d2da0861d9ec1a2ff2a3d6020aad31e6484facd` |

