# Identity audit — card set `blinded-ratio`

Written by `scripts/16_identity_audit.py`. It attacks the cards with what an exam candidate can see and measures the result against a permutation chance line. It applies no rule and proposes no fix.

| field | value |
|---|---|
| run number (RULES 29) | `12b07f79e74f0be7` |
| full input fingerprint | `12b07f79e74f0be7f69e4e9724cf010ed9beccafe5d4129f19f63eb8402676af` |
| written at (system clock, UTC, RULES 23) | 2026-10-01T20:28:56Z |
| free disk space at start (bytes) | 12419985408 |
| card folder | `exam-prep/blind-proof/ratio/cards` |
| cards | 306 |
| distinct coins | 10 |
| shuffles (RULES 12) | 1000 |
| boundary (RULES 12) | best 1.0% |
| seed (TACTICS 1 draw number) | `20260913` |
| `scripts/16_identity_audit.py` SHA-256 | `4a248f78c78376c3b58ce7b02bc20af2c035e8089529449d303c70061164f4da` |

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
| `granularity-close` | 1 | 0.143791 | 0.169935 | no | 0.596809 | 0.513207 | YES |
| `ALL` | 51 | 0.428105 | 0.173203 | YES | 0.619958 | 0.512216 | YES |
| `ALL-except-frozen-volatility` | 48 | 0.415033 | 0.173203 | YES | 0.619374 | 0.511842 | YES |
| `ALL-removable` | 40 | 0.405229 | 0.173203 | YES | 0.615496 | 0.5126 | YES |

### Nearest neighbour and tied distances (third-fix run)

The nearest-neighbour score above breaks a distance tie by the lowest card index, so where features tie it depends on how the cards are numbered (REVIEW-2 §4.1). `tie range` is the lowest and highest value that score can take over every tie-break; `tie-free` is its exact mean over every tie-break, which does not depend on card order, with its own chance line from the same 1000 shuffles. Where no card has a tied nearest neighbour the three agree.

| feature family | cards with a tied nearest neighbour | nearest-neighbour (index tie-break) | tie range | tie-free | chance line | beats chance |
|---|---|---|---|---|---|---|
| `price-level` | 20 | 0.153595 | 0.137255 – 0.156863 | 0.147059 | 0.179739 | no |
| `volatility-frozen` | 0 | 0.160131 | 0.160131 – 0.160131 | 0.160131 | 0.176471 | no |
| `volume-level` | 11 | 0.186275 | 0.183007 – 0.186275 | 0.184641 | 0.179739 | YES |
| `trades-level` | 153 | 0.212418 | 0.117647 – 0.415033 | 0.194979 | 0.166511 | YES |
| `openint-level` | 305 | 0.127451 | 0.0 – 0.996732 | 0.120354 | 0.122747 | no |
| `depth-level` | | | | | | no features left after blinding |
| `ratio-level` | | | | | | no features left after blinding |
| `taker-buy` | 0 | 0.166667 | 0.166667 – 0.166667 | 0.166667 | 0.179739 | no |
| `funding-line` | 184 | 0.153595 | 0.091503 – 0.53268 | 0.183139 | 0.162366 | YES |
| `wikipedia-presence` | | | | | | no features left after blinding |
| `p7-shape` | 0 | 0.150327 | 0.150327 – 0.150327 | 0.150327 | 0.179739 | no |
| `btc-eth` | | | | | | no features left after blinding |
| `shape-scale-free` | 0 | 0.196078 | 0.196078 – 0.196078 | 0.196078 | 0.173203 | YES |
| `repeat-close` | 293 | 0.160131 | 0.009804 – 0.885621 | 0.140828 | 0.138747 | YES |
| `repeat-chg` | 301 | 0.101307 | 0.006536 – 0.928105 | 0.142932 | 0.134485 | YES |
| `repeat-volume` | 304 | 0.071895 | 0.0 – 0.98366 | 0.124515 | 0.129736 | no |
| `repeat-trades` | 231 | 0.232026 | 0.091503 – 0.454248 | 0.22216 | 0.16227 | YES |
| `repeat-takerbuy` | 300 | 0.130719 | 0.006536 – 0.934641 | 0.128017 | 0.134658 | no |
| `repeat-openint` | 283 | 0.111111 | 0.0 – 0.584967 | 0.11507 | 0.148615 | no |
| `repeat-ratio` | 3 | 0.186275 | 0.186275 – 0.186275 | 0.186275 | 0.176471 | YES |
| `repeat-depth` | 266 | 0.199346 | 0.058824 – 0.846405 | 0.18171 | 0.149343 | YES |
| `repeat-btceth` | | | | | | no features left after blinding |
| `granularity-close` | 304 | 0.143791 | 0.006536 – 0.95098 | 0.194551 | 0.133443 | YES |
| `ALL` | 0 | 0.428105 | 0.428105 – 0.428105 | 0.428105 | 0.173203 | YES |
| `ALL-except-frozen-volatility` | 0 | 0.415033 | 0.415033 – 0.415033 | 0.415033 | 0.173203 | YES |
| `ALL-removable` | 0 | 0.405229 | 0.405229 – 0.405229 | 0.405229 | 0.173203 | YES |

## The gate rows — `ALL-removable`, both attacks

`ALL-removable` is every family except the forced ones (`volatility-frozen`, `funding-line`, `p7-shape`, `repeat-chg`). Both attacks are printed. **This report does not say which of them decides the acceptance gate**; that is open question JQ-R04-GATE (`exam-prep/third-fix/juror-questions/JQ-R04-GATE.md`).

| attack | observed | chance line (best 1%) | beats it |
|---|---|---|---|
| nearest-neighbour same-coin | 0.405229 | 0.173203 | YES |
| nearest-neighbour same-coin, tie-free (0 cards with a tied nearest neighbour) | 0.405229 | 0.173203 | YES |
| pair AUC | 0.615496 | 0.5126 | YES |

## T3 — does the card say which clock hours it covers?

Two cards are "detected" as covering the same hours when they print 3 consecutive rows that are identical in the named column(s). The truth is the start hours: two cards share a clock hour when their 48-hour spans intersect (the relation `14_overlap_map.py` measured).

| columns used | pairs | truly sharing an hour | detected | detection rate | false positives | false-positive rate | note |
|---|---|---|---|---|---|---|---|
| `BTC+ETH` | 0 | 0 | 0 |  | 0 |  | column(s) not printed on this card set |
| `chg%` | 46665 | 495 | 10 | 0.020202 | 1 | 2.2e-05 | 3 consecutive identical rows |
| `close` | 46665 | 495 | 0 | 0.0 | 2 | 4.3e-05 | 3 consecutive identical rows |
| `quote vol` | 46665 | 495 | 0 | 0.0 | 0 | 0.0 | 3 consecutive identical rows |
| `bullet:US releases` | 46665 | 495 | 8 | 0.016162 | 15 | 0.000325 | the whole bullet text identical, the default 'none' text excluded |

## T4 — release names that sit on one calendar day of this set

A count, not an attack: a release that a reader can date from public knowledge dates the card that prints it (REVIEW §3.4). Computed against the truth file.

| quantity | count |
|---|---|
| cards printing at least one release name | 100 of 306 |
| distinct release names | 30 |
| names that occur on exactly one calendar day of this set | 11 |
| cards carrying such a name | 13 |
| names that fall on exactly one release day of this set (card start hour + printed offset; a name printed without an offset is keyed by the card's start day) | 13 |
| cards carrying such a name | 18 |

The first two rows of counts above are by the day the card starts (the second-fix definition); the last two by the day the release falls (third-fix). Both measure uniqueness **within this card set**, not how often a release is published.

## Fingerprints

| file | SHA-256 |
|---|---|
| `exam-prep/third-fix/identity/run-12b07f79e74f0be7/identity-audit-blinded-ratio.csv` | `c65820915a0324ff5b452223fea9ed1b4b4c3e6f33c02b35d7a744ad65c6c528` |
| `exam-prep/third-fix/identity/run-12b07f79e74f0be7/hour-linkage-blinded-ratio.csv` | `a240267eaf15370330de90357275ab111b21d8a096352d4bd8a753da7162b2a1` |

