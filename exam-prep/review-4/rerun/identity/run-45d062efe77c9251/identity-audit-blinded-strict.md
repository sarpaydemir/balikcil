# Identity audit — card set `blinded-strict`

Written by `scripts/29_identity_audit_exact.py` (the audit of `scripts/16_identity_audit.py` with distances compared exactly, fourth-fix run). It attacks the cards with what an exam candidate can see and measures the result against a permutation chance line. It applies no rule and proposes no fix.

| field | value |
|---|---|
| run number (RULES 29) | `45d062efe77c9251` |
| full input fingerprint | `45d062efe77c9251a1a8181eb5d1c46104a830f1913983bee6da6a4ee3991821` |
| written at (system clock, UTC, RULES 23) | 2026-10-01T22:05:57Z |
| free disk space at start (bytes) | 12394881024 |
| card folder | `exam-prep/blind-proof/strict/cards` |
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
| `price-level` | 1 | 0.153595 | 0.179739 | no | 0.503476 | 0.512978 | no |
| `volatility-frozen` | 3 | 0.160131 | 0.176471 | no | 0.542629 | 0.513267 | YES |
| `volume-level` | 1 | 0.127451 | 0.137255 | no | 0.499191 | 0.504875 | no |
| `trades-level` | 1 | 0.130719 | 0.166667 | no | 0.52952 | 0.513493 | YES |
| `openint-level` | 1 | 0.130719 | 0.153595 | no | 0.513841 | 0.511796 | YES |
| `depth-level` | 2 | 0.147059 | 0.147059 | no | 0.504425 | 0.510421 | no |
| `ratio-level` | 3 | 0.127451 | 0.176471 | no | 0.489869 | 0.513598 | no |
| `taker-buy` | 1 | 0.120915 | 0.166667 | no | 0.496313 | 0.514336 | no |
| `funding-line` | 4 | 0.150327 | 0.173203 | no | 0.592675 | 0.511202 | YES |
| `wikipedia-presence` | 0 |  |  | no features left after blinding |  |  | no features left after blinding |
| `p7-shape` | 2 | 0.150327 | 0.179739 | no | 0.5239 | 0.513163 | YES |
| `btc-eth` | 0 |  |  | no features left after blinding |  |  | no features left after blinding |
| `shape-scale-free` | 13 | 0.147059 | 0.173203 | no | 0.512016 | 0.512623 | no |
| `repeat-close` | 2 | 0.160131 | 0.166667 | no | 0.541608 | 0.510755 | YES |
| `repeat-chg` | 2 | 0.101307 | 0.166667 | no | 0.523354 | 0.512968 | YES |
| `repeat-volume` | 2 | 0.163399 | 0.153595 | YES | 0.505981 | 0.511495 | no |
| `repeat-trades` | 2 | 0.22549 | 0.173203 | YES | 0.585348 | 0.512775 | YES |
| `repeat-takerbuy` | 2 | 0.124183 | 0.169935 | no | 0.50287 | 0.513118 | no |
| `repeat-openint` | 2 | 0.143791 | 0.173203 | no | 0.621996 | 0.513399 | YES |
| `repeat-ratio` | 6 | 0.186275 | 0.176471 | YES | 0.563942 | 0.51247 | YES |
| `repeat-depth` | 4 | 0.222222 | 0.169935 | YES | 0.535053 | 0.513322 | YES |
| `repeat-btceth` | 0 |  |  | no features left after blinding |  |  | no features left after blinding |
| `granularity-close` | 1 | 0.143791 | 0.169935 | no | 0.599532 | 0.512967 | YES |
| `ALL` | 55 | 0.437908 | 0.169935 | YES | 0.581825 | 0.51362 | YES |
| `ALL-except-frozen-volatility` | 52 | 0.421569 | 0.173203 | YES | 0.581506 | 0.513658 | YES |
| `ALL-removable` | 44 | 0.408497 | 0.169935 | YES | 0.574149 | 0.513603 | YES |

### Nearest neighbour and tied distances (third-fix run)

The nearest-neighbour score above breaks a distance tie by the lowest card index, so where features tie it depends on how the cards are numbered (REVIEW-2 §4.1). `tie range` is the lowest and highest value that score can take over every tie-break; `tie-free` is its exact mean over every tie-break, which does not depend on card order, with its own chance line from the same 1000 shuffles. Where no card has a tied nearest neighbour the three agree. Distances are compared in exact arithmetic (fourth-fix run, REVIEW-3 §4.1), so a tie here is an exact tie.

| feature family | cards with a tied nearest neighbour | nearest-neighbour (index tie-break) | tie range | tie-free | chance line | beats chance |
|---|---|---|---|---|---|---|
| `price-level` | 20 | 0.153595 | 0.137255 – 0.156863 | 0.147059 | 0.179739 | no |
| `volatility-frozen` | 0 | 0.160131 | 0.160131 – 0.160131 | 0.160131 | 0.176471 | no |
| `volume-level` | 306 | 0.127451 | 0.0 – 0.990196 | 0.118599 | 0.128468 | no |
| `trades-level` | 300 | 0.130719 | 0.006536 – 0.875817 | 0.154136 | 0.140329 | YES |
| `openint-level` | 303 | 0.130719 | 0.003268 – 0.96732 | 0.141978 | 0.131035 | YES |
| `depth-level` | 305 | 0.147059 | 0.022876 – 0.977124 | 0.147147 | 0.131292 | YES |
| `ratio-level` | 167 | 0.127451 | 0.081699 – 0.326797 | 0.134483 | 0.164822 | no |
| `taker-buy` | 304 | 0.120915 | 0.003268 – 0.957516 | 0.11978 | 0.131061 | no |
| `funding-line` | 186 | 0.150327 | 0.088235 – 0.535948 | 0.182594 | 0.162494 | YES |
| `wikipedia-presence` | | | | | | no features left after blinding |
| `p7-shape` | 0 | 0.150327 | 0.150327 – 0.150327 | 0.150327 | 0.179739 | no |
| `btc-eth` | | | | | | no features left after blinding |
| `shape-scale-free` | 0 | 0.147059 | 0.147059 – 0.147059 | 0.147059 | 0.173203 | no |
| `repeat-close` | 293 | 0.160131 | 0.009804 – 0.885621 | 0.140828 | 0.138747 | YES |
| `repeat-chg` | 301 | 0.101307 | 0.006536 – 0.928105 | 0.142932 | 0.134485 | YES |
| `repeat-volume` | 304 | 0.163399 | 0.0 – 0.977124 | 0.129737 | 0.129843 | no |
| `repeat-trades` | 236 | 0.22549 | 0.078431 – 0.454248 | 0.213445 | 0.161858 | YES |
| `repeat-takerbuy` | 304 | 0.124183 | 0.006536 – 0.931373 | 0.121157 | 0.132718 | no |
| `repeat-openint` | 289 | 0.143791 | 0.045752 – 0.862745 | 0.202839 | 0.142742 | YES |
| `repeat-ratio` | 5 | 0.186275 | 0.186275 – 0.186275 | 0.186275 | 0.176471 | YES |
| `repeat-depth` | 273 | 0.222222 | 0.088235 – 0.957516 | 0.214744 | 0.14232 | YES |
| `repeat-btceth` | | | | | | no features left after blinding |
| `granularity-close` | 304 | 0.143791 | 0.006536 – 0.95098 | 0.194823 | 0.133656 | YES |
| `ALL` | 0 | 0.437908 | 0.437908 – 0.437908 | 0.437908 | 0.169935 | YES |
| `ALL-except-frozen-volatility` | 0 | 0.421569 | 0.421569 – 0.421569 | 0.421569 | 0.173203 | YES |
| `ALL-removable` | 0 | 0.408497 | 0.408497 – 0.408497 | 0.408497 | 0.169935 | YES |

## The gate rows — `ALL-removable`, both attacks

`ALL-removable` is every family except the forced ones (`volatility-frozen`, `funding-line`, `p7-shape`, `repeat-chg`). Both attacks are printed. **This report does not say which of them decides the acceptance gate**; that is open question JQ-R04-GATE (`exam-prep/third-fix/juror-questions/JQ-R04-GATE.md`).

| attack | observed | chance line (best 1%) | beats it |
|---|---|---|---|
| nearest-neighbour same-coin | 0.408497 | 0.169935 | YES |
| nearest-neighbour same-coin, tie-free (0 cards with a tied nearest neighbour) | 0.408497 | 0.169935 | YES |
| pair AUC | 0.574149 | 0.513603 | YES |

## T3 — does the card say which clock hours it covers?

Two cards are "detected" as covering the same hours when they print 3 consecutive rows that are identical in the named column(s). The truth is the start hours: two cards share a clock hour when their 48-hour spans intersect (the relation `14_overlap_map.py` measured).

| columns used | pairs | truly sharing an hour | detected | detection rate | false positives | false-positive rate | note |
|---|---|---|---|---|---|---|---|
| `BTC+ETH` | 0 | 0 | 0 |  | 0 |  | column(s) not printed on this card set |
| `chg%` | 46665 | 495 | 10 | 0.020202 | 1 | 2.2e-05 | 3 consecutive identical rows |
| `close` | 46665 | 495 | 0 | 0.0 | 2 | 4.3e-05 | 3 consecutive identical rows |
| `quote vol` | 46665 | 495 | 34 | 0.068687 | 2726 | 0.059043 | 3 consecutive identical rows |
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
| `exam-prep/review-4/rerun/identity/run-45d062efe77c9251/identity-audit-blinded-strict.csv` | `0651b1de1eb6d1af844b91d00bdad4a229a9c38c855899678394aad19bdaa171` |
| `exam-prep/review-4/rerun/identity/run-45d062efe77c9251/hour-linkage-blinded-strict.csv` | `b590bc5d04b4f84892454165db1069f02f105734595d3df38dfa720800c1dab7` |

