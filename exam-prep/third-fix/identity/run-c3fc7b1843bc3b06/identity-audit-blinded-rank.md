# Identity audit — card set `blinded-rank`

Written by `scripts/16_identity_audit.py`. It attacks the cards with what an exam candidate can see and measures the result against a permutation chance line. It applies no rule and proposes no fix.

| field | value |
|---|---|
| run number (RULES 29) | `c3fc7b1843bc3b06` |
| full input fingerprint | `c3fc7b1843bc3b06b9d2a86e095a11dd1431d3478171a79daf3393731c1b1fc6` |
| written at (system clock, UTC, RULES 23) | 2026-10-01T20:18:58Z |
| free disk space at start (bytes) | 12422418432 |
| card folder | `exam-prep/blind-proof/rank/cards` |
| cards | 306 |
| distinct coins | 10 |
| shuffles (RULES 12) | 1000 |
| boundary (RULES 12) | best 1.0% |
| seed (TACTICS 1 draw number) | `20260913` |
| `scripts/16_identity_audit.py` SHA-256 | `6437fcffad722bcac4c2be17aa755e3349f06f92ed2a5f0b7d090b41dec084ec` |

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
| `granularity-close` | 1 | 0.143791 | 0.169935 | no | 0.596809 | 0.513207 | YES |
| `ALL` | 58 | 0.421569 | 0.176471 | YES | 0.588238 | 0.513261 | YES |
| `ALL-except-frozen-volatility` | 55 | 0.424837 | 0.176471 | YES | 0.587519 | 0.513157 | YES |
| `ALL-removable` | 47 | 0.447712 | 0.169935 | YES | 0.581433 | 0.513237 | YES |

### Nearest neighbour and tied distances (third-fix run)

The nearest-neighbour score above breaks a distance tie by the lowest card index, so where features tie it depends on how the cards are numbered (REVIEW-2 §4.1). `tie range` is the lowest and highest value that score can take over every tie-break; `tie-free` is its exact mean over every tie-break, which does not depend on card order, with its own chance line from the same 1000 shuffles. Where no card has a tied nearest neighbour the three agree.

| feature family | cards with a tied nearest neighbour | nearest-neighbour (index tie-break) | tie range | tie-free | chance line | beats chance |
|---|---|---|---|---|---|---|
| `price-level` | 20 | 0.153595 | 0.137255 – 0.156863 | 0.147059 | 0.179739 | no |
| `volatility-frozen` | 0 | 0.160131 | 0.160131 – 0.160131 | 0.160131 | 0.176471 | no |
| `volume-level` | 11 | 0.183007 | 0.179739 – 0.183007 | 0.181373 | 0.176471 | YES |
| `trades-level` | 61 | 0.196078 | 0.189542 – 0.24183 | 0.210434 | 0.175957 | YES |
| `openint-level` | 303 | 0.130719 | 0.003268 – 0.96732 | 0.141978 | 0.131035 | YES |
| `depth-level` | 305 | 0.147059 | 0.022876 – 0.977124 | 0.147147 | 0.131292 | YES |
| `ratio-level` | 167 | 0.127451 | 0.081699 – 0.326797 | 0.134483 | 0.164822 | no |
| `taker-buy` | 0 | 0.166667 | 0.166667 – 0.166667 | 0.166667 | 0.179739 | no |
| `funding-line` | 184 | 0.153595 | 0.091503 – 0.53268 | 0.183139 | 0.162366 | YES |
| `wikipedia-presence` | | | | | | no features left after blinding |
| `p7-shape` | 0 | 0.150327 | 0.150327 – 0.150327 | 0.150327 | 0.179739 | no |
| `btc-eth` | | | | | | no features left after blinding |
| `shape-scale-free` | 0 | 0.147059 | 0.147059 – 0.147059 | 0.147059 | 0.173203 | no |
| `repeat-close` | 293 | 0.160131 | 0.009804 – 0.885621 | 0.140828 | 0.138747 | YES |
| `repeat-chg` | 301 | 0.101307 | 0.006536 – 0.928105 | 0.142932 | 0.134485 | YES |
| `repeat-volume` | 304 | 0.163399 | 0.0 – 0.977124 | 0.129737 | 0.129843 | no |
| `repeat-trades` | 231 | 0.232026 | 0.091503 – 0.454248 | 0.22216 | 0.16227 | YES |
| `repeat-takerbuy` | 300 | 0.130719 | 0.006536 – 0.934641 | 0.128017 | 0.134658 | no |
| `repeat-openint` | 289 | 0.143791 | 0.045752 – 0.862745 | 0.202839 | 0.141941 | YES |
| `repeat-ratio` | 4 | 0.186275 | 0.186275 – 0.186275 | 0.186275 | 0.176471 | YES |
| `repeat-depth` | 273 | 0.222222 | 0.088235 – 0.957516 | 0.214744 | 0.14232 | YES |
| `repeat-btceth` | | | | | | no features left after blinding |
| `granularity-close` | 304 | 0.143791 | 0.006536 – 0.95098 | 0.194551 | 0.133443 | YES |
| `ALL` | 0 | 0.421569 | 0.421569 – 0.421569 | 0.421569 | 0.176471 | YES |
| `ALL-except-frozen-volatility` | 0 | 0.424837 | 0.424837 – 0.424837 | 0.424837 | 0.176471 | YES |
| `ALL-removable` | 0 | 0.447712 | 0.447712 – 0.447712 | 0.447712 | 0.169935 | YES |

## The gate rows — `ALL-removable`, both attacks

`ALL-removable` is every family except the forced ones (`volatility-frozen`, `funding-line`, `p7-shape`, `repeat-chg`). Both attacks are printed. **This report does not say which of them decides the acceptance gate**; that is open question JQ-R04-GATE (`exam-prep/third-fix/juror-questions/JQ-R04-GATE.md`).

| attack | observed | chance line (best 1%) | beats it |
|---|---|---|---|
| nearest-neighbour same-coin | 0.447712 | 0.169935 | YES |
| nearest-neighbour same-coin, tie-free (0 cards with a tied nearest neighbour) | 0.447712 | 0.169935 | YES |
| pair AUC | 0.581433 | 0.513237 | YES |

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
| names that fall on exactly one release day of this set (card start hour + printed offset; a name printed without an offset is keyed by the card's start day) | 13 |
| cards carrying such a name | 18 |

The first two rows of counts above are by the day the card starts (the second-fix definition); the last two by the day the release falls (third-fix). Both measure uniqueness **within this card set**, not how often a release is published.

## Fingerprints

| file | SHA-256 |
|---|---|
| `exam-prep/third-fix/identity/run-c3fc7b1843bc3b06/identity-audit-blinded-rank.csv` | `7f46d759c891db057cb54b9b6ba01544d7880595b86b45043154224d204ea357` |
| `exam-prep/third-fix/identity/run-c3fc7b1843bc3b06/hour-linkage-blinded-rank.csv` | `11f07aa54741e567e5235796b761959e8b662ae2570ac79f36c2b69088386b50` |

