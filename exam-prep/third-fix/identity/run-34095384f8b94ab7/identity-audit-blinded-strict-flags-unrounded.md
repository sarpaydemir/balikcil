# Identity audit — card set `blinded-strict-flags-unrounded`

Written by `scripts/16_identity_audit.py`. It attacks the cards with what an exam candidate can see and measures the result against a permutation chance line. It applies no rule and proposes no fix.

| field | value |
|---|---|
| run number (RULES 29) | `34095384f8b94ab7` |
| full input fingerprint | `34095384f8b94ab764ac0c1ee0f2ce8125566e046becb0b3362235a5d33681ea` |
| written at (system clock, UTC, RULES 23) | 2026-10-01T20:34:55Z |
| free disk space at start (bytes) | 12419416064 |
| card folder | `exam-prep/third-fix/blind-proof/strict-flags-unrounded/cards` |
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
| `volume-level` | 0 |  |  | no features left after blinding |  |  | no features left after blinding |
| `trades-level` | 1 | 0.133987 | 0.137255 | no | 0.499688 | 0.503342 | no |
| `openint-level` | 0 |  |  | no features left after blinding |  |  | no features left after blinding |
| `depth-level` | 0 |  |  | no features left after blinding |  |  | no features left after blinding |
| `ratio-level` | 1 | 0.127451 | 0.137255 | no | 0.508182 | 0.505214 | YES |
| `taker-buy` | 0 |  |  | no features left after blinding |  |  | no features left after blinding |
| `funding-line` | 3 | 0.094771 | 0.160131 | no | 0.57274 | 0.510926 | YES |
| `wikipedia-presence` | 0 |  |  | no features left after blinding |  |  | no features left after blinding |
| `p7-shape` | 2 | 0.150327 | 0.179739 | no | 0.5239 | 0.513163 | YES |
| `btc-eth` | 0 |  |  | no features left after blinding |  |  | no features left after blinding |
| `shape-scale-free` | 10 | 0.137255 | 0.176471 | no | 0.514428 | 0.512536 | YES |
| `repeat-close` | 2 | 0.160131 | 0.166667 | no | 0.542144 | 0.510666 | YES |
| `repeat-chg` | 2 | 0.101307 | 0.166667 | no | 0.523074 | 0.512879 | YES |
| `repeat-volume` | 0 |  |  | no features left after blinding |  |  | no features left after blinding |
| `repeat-trades` | 2 | 0.127451 | 0.143791 | no | 0.50116 | 0.508092 | no |
| `repeat-takerbuy` | 0 |  |  | no features left after blinding |  |  | no features left after blinding |
| `repeat-openint` | 2 | 0.130719 | 0.137255 | no | 0.50805 | 0.504862 | YES |
| `repeat-ratio` | 2 | 0.117647 | 0.147059 | no | 0.515022 | 0.509836 | YES |
| `repeat-depth` | 4 | 0.127451 | 0.140523 | no | 0.498739 | 0.507118 | no |
| `repeat-btceth` | 0 |  |  | no features left after blinding |  |  | no features left after blinding |
| `granularity-close` | 1 | 0.143791 | 0.169935 | no | 0.596809 | 0.513207 | YES |
| `ALL` | 36 | 0.267974 | 0.169935 | YES | 0.55979 | 0.514776 | YES |
| `ALL-except-frozen-volatility` | 33 | 0.25817 | 0.176471 | YES | 0.556628 | 0.514574 | YES |
| `ALL-removable` | 26 | 0.238562 | 0.176471 | YES | 0.545585 | 0.51371 | YES |

### Nearest neighbour and tied distances (third-fix run)

The nearest-neighbour score above breaks a distance tie by the lowest card index, so where features tie it depends on how the cards are numbered (REVIEW-2 §4.1). `tie range` is the lowest and highest value that score can take over every tie-break; `tie-free` is its exact mean over every tie-break, which does not depend on card order, with its own chance line from the same 1000 shuffles. Where no card has a tied nearest neighbour the three agree.

| feature family | cards with a tied nearest neighbour | nearest-neighbour (index tie-break) | tie range | tie-free | chance line | beats chance |
|---|---|---|---|---|---|---|
| `price-level` | 20 | 0.153595 | 0.137255 – 0.156863 | 0.147059 | 0.179739 | no |
| `volatility-frozen` | 0 | 0.160131 | 0.160131 – 0.160131 | 0.160131 | 0.176471 | no |
| `volume-level` | | | | | | no features left after blinding |
| `trades-level` | 304 | 0.133987 | 0.006536 – 1.0 | 0.125607 | 0.125607 | no |
| `openint-level` | | | | | | no features left after blinding |
| `depth-level` | | | | | | no features left after blinding |
| `ratio-level` | 306 | 0.127451 | 0.0 – 0.98366 | 0.120162 | 0.125 | no |
| `taker-buy` | | | | | | no features left after blinding |
| `funding-line` | 305 | 0.094771 | 0.0 – 0.996732 | 0.151876 | 0.124803 | YES |
| `wikipedia-presence` | | | | | | no features left after blinding |
| `p7-shape` | 0 | 0.150327 | 0.150327 – 0.150327 | 0.150327 | 0.179739 | no |
| `btc-eth` | | | | | | no features left after blinding |
| `shape-scale-free` | 0 | 0.137255 | 0.137255 – 0.137255 | 0.137255 | 0.176471 | no |
| `repeat-close` | 293 | 0.160131 | 0.009804 – 0.885621 | 0.140828 | 0.138747 | YES |
| `repeat-chg` | 301 | 0.101307 | 0.006536 – 0.928105 | 0.142932 | 0.134485 | YES |
| `repeat-volume` | | | | | | no features left after blinding |
| `repeat-trades` | 306 | 0.127451 | 0.0 – 0.98366 | 0.121018 | 0.124768 | no |
| `repeat-takerbuy` | | | | | | no features left after blinding |
| `repeat-openint` | 304 | 0.130719 | 0.0 – 0.993464 | 0.122116 | 0.128468 | no |
| `repeat-ratio` | 306 | 0.117647 | 0.0 – 0.977124 | 0.122049 | 0.128202 | no |
| `repeat-depth` | 302 | 0.127451 | 0.0 – 0.986928 | 0.119378 | 0.129149 | no |
| `repeat-btceth` | | | | | | no features left after blinding |
| `granularity-close` | 304 | 0.143791 | 0.006536 – 0.95098 | 0.194551 | 0.133443 | YES |
| `ALL` | 0 | 0.267974 | 0.267974 – 0.267974 | 0.267974 | 0.169935 | YES |
| `ALL-except-frozen-volatility` | 0 | 0.25817 | 0.25817 – 0.25817 | 0.25817 | 0.176471 | YES |
| `ALL-removable` | 0 | 0.238562 | 0.238562 – 0.238562 | 0.238562 | 0.176471 | YES |

## The gate rows — `ALL-removable`, both attacks

`ALL-removable` is every family except the forced ones (`volatility-frozen`, `funding-line`, `p7-shape`, `repeat-chg`). Both attacks are printed. **This report does not say which of them decides the acceptance gate**; that is open question JQ-R04-GATE (`exam-prep/third-fix/juror-questions/JQ-R04-GATE.md`).

| attack | observed | chance line (best 1%) | beats it |
|---|---|---|---|
| nearest-neighbour same-coin | 0.238562 | 0.176471 | YES |
| nearest-neighbour same-coin, tie-free (0 cards with a tied nearest neighbour) | 0.238562 | 0.176471 | YES |
| pair AUC | 0.545585 | 0.51371 | YES |

## T3 — does the card say which clock hours it covers?

Two cards are "detected" as covering the same hours when they print 3 consecutive rows that are identical in the named column(s). The truth is the start hours: two cards share a clock hour when their 48-hour spans intersect (the relation `14_overlap_map.py` measured).

| columns used | pairs | truly sharing an hour | detected | detection rate | false positives | false-positive rate | note |
|---|---|---|---|---|---|---|---|
| `BTC+ETH` | 0 | 0 | 0 |  | 0 |  | column(s) not printed on this card set |
| `chg%` | 46665 | 495 | 10 | 0.020202 | 1 | 2.2e-05 | 3 consecutive identical rows |
| `close` | 46665 | 495 | 0 | 0.0 | 2 | 4.3e-05 | 3 consecutive identical rows |
| `quote vol` | 46665 | 495 | 35 | 0.070707 | 2910 | 0.063028 | 3 consecutive identical rows |
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
| `exam-prep/third-fix/identity/run-34095384f8b94ab7/identity-audit-blinded-strict-flags-unrounded.csv` | `405d07d8d055270f9bd1c767e6f75a1ac42be10f96351b81fc0ec3c2fccf4553` |
| `exam-prep/third-fix/identity/run-34095384f8b94ab7/hour-linkage-blinded-strict-flags-unrounded.csv` | `0b80b6d6460c1eb65284e490173e000cb05e5b21b3f4220e39faeb8a54f8ed4f` |

