# Fourth-fix checks — run `516027c6c9f215d6`

Written by `scripts/30_fourth_fix_checks.py` at 2026-10-01T22:11:24Z (system clock, RULES 23); free disk at start 12394766336 bytes. Criteria: `exam-prep/fourth-fix/criteria-written-before-measuring.md`.

## H-1 · the engine's key check (K-14)

| attempt | result | K-14 expects | detail |
|---|---|---|---|
| q4-0 true map, true key | **accepted** | accepted | events 58, key_check matched, record event_map_sha256 021cab6b1ab3… |
| q4-1 one coin changed, true key | **refused** | refused | ValueError: the event map was not made from the moments of the answer key: its moments finge |
| q4-2 extra moment, true key | **refused** | refused | ValueError: the event map was not made from the moments of the answer key: its moments finge |
| q4-3 forged hour, instance method patched to return the key | **refused** | refused | ValueError: the event map was not made from the moments of the answer key: its moments finge |
| q4-4 forged hour, subclass overriding moments_sha256() | **refused** | refused | TypeError: events must be an EventMap returned by collapse() or identity_map(), not a EM |
| q4-5 forged hour, .moments overwritten with the true tuple | **refused** | refused | ValueError: the event map does not match what its own configuration card-span/component/any  |
| H1-6 TRUE map wrapped in a subclass, true key | **refused** | refused | TypeError: events must be an EventMap returned by collapse() or identity_map(), not a EM |
| G1 forged hours (half the moments moved 1,000 h), true key | **refused** | refused | ValueError: the event map was not made from the moments of the answer key: its moments finge |
| G1 key omitted | **refused** | refused | TypeError: chance_line() missing 1 required keyword-only argument: 'key_moments_sha256' |
| G1 key None | **refused** | refused | ValueError: the event map was not made from the moments of the answer key: its moments finge |
| H1-8 configuration label changed after construction | **refused** | refused | ValueError: the event map's configuration label 'card-span/greedy-clique/cross-coin' is not  |
| H1-9 same_coin_keep changed after construction | **refused** | refused | ValueError: the event map's configuration label 'card-span/greedy-clique/cross-coin' is not  |
| H1-10 a plain list of events | **refused** | refused | TypeError: events must be an EventMap returned by collapse() or identity_map(), not a list |
| H1-11 true map, instance sha256() patched to a constant | **accepted** | accepted | events 58, key_check matched, record event_map_sha256 021cab6b1ab3… |
| H1-12 'latest' card-span map, true key | **accepted** | accepted | events 124, key_check matched, record event_map_sha256 c8164274b16f… |
| H1-13 'latest' requested with component | **refused** | refused | ValueError: same_coin_keep='latest' exists only for greedy-clique with cross-coin under move |

Every attempt as K-14 requires: **True**. The record's `event_map_sha256` equals `EventMap.sha256()` of the true map (formula unchanged): True. With `sha256()` patched on the instance, the record still carries the true fingerprint: True.

## H-2 · keep the latest (K-15)

| definition | events, earliest | events, latest | latest = q1 literal | latest = p1b | literal path with earliest = engine | events in one partition only |
|---|---|---|---|---|---|---|
| move-window | 168 | 168 | True | True | True | 4 |
| card-span | 125 | 124 | True | True | True | 21 |

Random moment sets (q1's generator, seed 20260913, 200 sets), sets that differ:

- move-window: latest vs q1 literal: 0 of 200
- move-window: literal earliest vs engine earliest: 0 of 200
- card-span: latest vs q1 literal: 0 of 200
- card-span: literal earliest vs engine earliest: 0 of 200

Table row of each `+latest` configuration, in JQ-N1's columns:

| configuration | events | events of 1 card | largest event | events holding a large and a calm card | events holding 2+ cards of one coin | largest same-coin count | block: events that cannot move | block: cards in them |
|---|---|---|---|---|---|---|---|---|
| move-window / greedy-clique / cross-coin + latest | 168 | 78 | 6 | 50 | 0 | 1 | 1 | 5 |
| card-span / greedy-clique / cross-coin + latest | 124 | 39 | 7 | 60 | 0 | 1 | 0 | 0 |

Accepted (K-15): **True**.

## H-3 · the exact audit (K-13)

Against REVIEW-3 q2 (tied cards exact, tie-free score, its line, its verdict, at 4 decimals):

| card set | family | q2 tied (exact) | audit tied | q2 tie-free (line) | audit tie-free (line) | equal |
|---|---|---|---|---|---|---|
| blinded-strict-flags | `price-level` | 20 | 20 | 0.1471 (0.1797) | 0.1471 (0.1797) | True |
| blinded-strict-flags | `volatility-frozen` | 0 | 0 | 0.1601 (0.1765) | 0.1601 (0.1765) | True |
| blinded-strict-flags | `volume-level` | 306 | 306 | 0.1186 (0.1285) | 0.1186 (0.1285) | True |
| blinded-strict-flags | `trades-level` | 300 | 300 | 0.1541 (0.1403) | 0.1541 (0.1403) | True |
| blinded-strict-flags | `openint-level` | 303 | 303 | 0.1420 (0.1310) | 0.1420 (0.1310) | True |
| blinded-strict-flags | `depth-level` | 305 | 305 | 0.1471 (0.1313) | 0.1471 (0.1313) | True |
| blinded-strict-flags | `ratio-level` | 167 | 167 | 0.1345 (0.1648) | 0.1345 (0.1648) | True |
| blinded-strict-flags | `taker-buy` | 304 | 304 | 0.1198 (0.1311) | 0.1198 (0.1311) | True |
| blinded-strict-flags | `funding-line` | 305 | 305 | 0.1519 (0.1248) | 0.1519 (0.1248) | True |
| blinded-strict-flags | `p7-shape` | 0 | 0 | 0.1503 (0.1797) | 0.1503 (0.1797) | True |
| blinded-strict-flags | `shape-scale-free` | 0 | 0 | 0.1471 (0.1732) | 0.1471 (0.1732) | True |
| blinded-strict-flags | `repeat-close` | 293 | 293 | 0.1408 (0.1387) | 0.1408 (0.1387) | True |
| blinded-strict-flags | `repeat-chg` | 301 | 301 | 0.1429 (0.1345) | 0.1429 (0.1345) | True |
| blinded-strict-flags | `repeat-volume` | 304 | 304 | 0.1297 (0.1298) | 0.1297 (0.1298) | True |
| blinded-strict-flags | `repeat-trades` | 236 | 236 | 0.2134 (0.1619) | 0.2134 (0.1619) | True |
| blinded-strict-flags | `repeat-takerbuy` | 304 | 304 | 0.1212 (0.1327) | 0.1212 (0.1327) | True |
| blinded-strict-flags | `repeat-openint` | 289 | 289 | 0.2028 (0.1427) | 0.2028 (0.1427) | True |
| blinded-strict-flags | `repeat-ratio` | 5 | 5 | 0.1863 (0.1765) | 0.1863 (0.1765) | True |
| blinded-strict-flags | `repeat-depth` | 273 | 273 | 0.2147 (0.1423) | 0.2147 (0.1423) | True |
| blinded-strict-flags | `granularity-close` | 304 | 304 | 0.1948 (0.1337) | 0.1948 (0.1337) | True |
| blinded-strict-flags | `ALL-removable` | 0 | 0 | 0.4085 (0.1699) | 0.4085 (0.1699) | True |
| blinded-strict-flags-k1 | `trades-level` | 300 | 300 | 0.1541 (0.1403) | 0.1541 (0.1403) | True |
| blinded-strict-flags-k1 | `repeat-close` | 293 | 293 | 0.1510 (0.1401) | 0.1510 (0.1401) | True |
| blinded-strict-flags-k1 | `repeat-trades` | 236 | 236 | 0.2134 (0.1619) | 0.2134 (0.1619) | True |
| blinded-strict-flags-k1 | `granularity-close` | 257 | 257 | 0.2525 (0.1567) | 0.2525 (0.1567) | True |
| blinded-strict-flags-k1 | `ALL-removable` | 0 | 0 | 0.4346 (0.1765) | 0.4346 (0.1765) | True |
| blinded-strict-flags-unrounded | `price-level` | 20 | 20 | 0.1471 (0.1797) | 0.1471 (0.1797) | True |
| blinded-strict-flags-unrounded | `volatility-frozen` | 0 | 0 | 0.1601 (0.1765) | 0.1601 (0.1765) | True |
| blinded-strict-flags-unrounded | `trades-level` | 304 | 304 | 0.1256 (0.1256) | 0.1256 (0.1256) | True |
| blinded-strict-flags-unrounded | `ratio-level` | 306 | 306 | 0.1202 (0.1250) | 0.1202 (0.1250) | True |
| blinded-strict-flags-unrounded | `funding-line` | 305 | 305 | 0.1519 (0.1248) | 0.1519 (0.1248) | True |
| blinded-strict-flags-unrounded | `p7-shape` | 0 | 0 | 0.1503 (0.1797) | 0.1503 (0.1797) | True |
| blinded-strict-flags-unrounded | `shape-scale-free` | 0 | 0 | 0.1373 (0.1765) | 0.1373 (0.1765) | True |
| blinded-strict-flags-unrounded | `repeat-close` | 293 | 293 | 0.1408 (0.1387) | 0.1408 (0.1387) | True |
| blinded-strict-flags-unrounded | `repeat-chg` | 301 | 301 | 0.1429 (0.1345) | 0.1429 (0.1345) | True |
| blinded-strict-flags-unrounded | `repeat-trades` | 306 | 306 | 0.1210 (0.1248) | 0.1210 (0.1248) | True |
| blinded-strict-flags-unrounded | `repeat-openint` | 304 | 304 | 0.1221 (0.1285) | 0.1221 (0.1285) | True |
| blinded-strict-flags-unrounded | `repeat-ratio` | 306 | 306 | 0.1220 (0.1282) | 0.1220 (0.1282) | True |
| blinded-strict-flags-unrounded | `repeat-depth` | 302 | 302 | 0.1194 (0.1291) | 0.1194 (0.1291) | True |
| blinded-strict-flags-unrounded | `granularity-close` | 304 | 304 | 0.1948 (0.1337) | 0.1948 (0.1337) | True |
| blinded-strict-flags-unrounded | `ALL-removable` | 0 | 0 | 0.2386 (0.1765) | 0.2386 (0.1765) | True |

Against the third-fix audit, every set:

| card set | exact run | third-fix run | T3 CSV identical | T4 identical | features identical | cells that differ |
|---|---|---|---|---|---|---|
| raw-observation | `9777f422fd2d2b41` | `4858581e2eb08704` | True | True | True | 34 |
| blinded-ratio | `989b8f21b23e0310` | `12b07f79e74f0be7` | True | True | True | 39 |
| blinded-rank | `446adf64f8e8235c` | `96f1d17e27b8afaf` | True | True | True | 33 |
| blinded-strict | `45d062efe77c9251` | `1f2ae3cf3a5b2044` | True | True | True | 36 |
| blinded-strict-flags | `9ff0ffec3fe21ebe` | `e05144718b909704` | True | True | True | 28 |
| blinded-strict-flags-k1 | `762815a877c19551` | `ded6a9caaf77d910` | True | True | True | 32 |
| blinded-strict-flags-unrounded | `d6557e91f9f97f7b` | `34095384f8b94ab7` | True | True | True | 9 |

Every cell that differs (third-fix → exact):

| card set | family | column | third-fix | exact |
|---|---|---|---|---|
| raw-observation | `trades-level` | pair_auc | 0.71236 | 0.712365 |
| raw-observation | `trades-level` | auc_chance_1pct | 0.51217 | 0.512173 |
| raw-observation | `funding-line` | pair_auc | 0.719539 | 0.719538 |
| raw-observation | `repeat-close` | pair_auc | 0.563626 | 0.563862 |
| raw-observation | `repeat-close` | auc_chance_1pct | 0.513268 | 0.513194 |
| raw-observation | `repeat-chg` | pair_auc | 0.523074 | 0.523354 |
| raw-observation | `repeat-chg` | auc_chance_1pct | 0.51347 | 0.513649 |
| raw-observation | `repeat-volume` | pair_auc | 0.506038 | 0.505981 |
| raw-observation | `repeat-volume` | auc_chance_1pct | 0.512154 | 0.512135 |
| raw-observation | `repeat-trades` | nn_same_coin_accuracy | 0.215686 | 0.205882 |
| raw-observation | `repeat-trades` | pair_auc | 0.58522 | 0.585348 |
| raw-observation | `repeat-trades` | auc_chance_1pct | 0.513129 | 0.513105 |
| raw-observation | `repeat-trades` | cards_with_tied_nn | 231 | 236 |
| raw-observation | `repeat-trades` | nn_tie_low | 0.091503 | 0.078431 |
| raw-observation | `repeat-trades` | nn_tie_free | 0.22216 | 0.213445 |
| raw-observation | `repeat-trades` | nn_tie_free_chance_1pct | 0.163043 | 0.162172 |
| raw-observation | `repeat-takerbuy` | pair_auc | 0.502733 | 0.50287 |
| raw-observation | `repeat-takerbuy` | auc_chance_1pct | 0.511336 | 0.511422 |
| raw-observation | `repeat-openint` | pair_auc | 0.621051 | 0.621996 |
| raw-observation | `repeat-openint` | auc_chance_1pct | 0.513538 | 0.51359 |
| raw-observation | `repeat-openint` | nn_tie_free_chance_1pct | 0.143574 | 0.144287 |
| raw-observation | `repeat-ratio` | auc_chance_1pct | 0.512059 | 0.512058 |
| raw-observation | `repeat-ratio` | cards_with_tied_nn | 4 | 5 |
| raw-observation | `repeat-depth` | pair_auc | 0.535063 | 0.535053 |
| raw-observation | `repeat-depth` | auc_chance_1pct | 0.513994 | 0.513996 |
| raw-observation | `repeat-btceth` | pair_auc | 0.497586 | 0.497578 |
| raw-observation | `repeat-btceth` | auc_chance_1pct | 0.512573 | 0.512524 |
| raw-observation | `repeat-btceth` | cards_with_tied_nn | 269 | 271 |
| raw-observation | `repeat-btceth` | nn_tie_free | 0.11594 | 0.114688 |
| raw-observation | `repeat-btceth` | nn_tie_free_chance_1pct | 0.149852 | 0.149097 |
| raw-observation | `granularity-close` | pair_auc | 0.716714 | 0.716709 |
| raw-observation | `granularity-close` | auc_chance_1pct | 0.513752 | 0.513759 |
| raw-observation | `granularity-close` | cards_with_tied_nn | 294 | 295 |
| raw-observation | `granularity-close` | nn_tie_free_chance_1pct | 0.141389 | 0.140266 |
| blinded-ratio | `trades-level` | pair_auc | 0.52623 | 0.526249 |
| blinded-ratio | `trades-level` | auc_chance_1pct | 0.513451 | 0.513459 |
| blinded-ratio | `funding-line` | nn_same_coin_accuracy | 0.153595 | 0.150327 |
| blinded-ratio | `funding-line` | pair_auc | 0.592679 | 0.592675 |
| blinded-ratio | `funding-line` | auc_chance_1pct | 0.5112 | 0.511202 |
| blinded-ratio | `funding-line` | cards_with_tied_nn | 184 | 186 |
| blinded-ratio | `funding-line` | nn_tie_low | 0.091503 | 0.088235 |
| blinded-ratio | `funding-line` | nn_tie_high | 0.53268 | 0.535948 |
| blinded-ratio | `funding-line` | nn_tie_free | 0.183139 | 0.182594 |
| blinded-ratio | `funding-line` | nn_tie_free_chance_1pct | 0.162366 | 0.162494 |
| blinded-ratio | `repeat-close` | pair_auc | 0.542144 | 0.541608 |
| blinded-ratio | `repeat-close` | auc_chance_1pct | 0.510666 | 0.510755 |
| blinded-ratio | `repeat-chg` | pair_auc | 0.523074 | 0.523354 |
| blinded-ratio | `repeat-chg` | auc_chance_1pct | 0.512879 | 0.512968 |
| blinded-ratio | `repeat-trades` | nn_same_coin_accuracy | 0.232026 | 0.22549 |
| blinded-ratio | `repeat-trades` | pair_auc | 0.58522 | 0.585348 |
| blinded-ratio | `repeat-trades` | auc_chance_1pct | 0.512746 | 0.512775 |
| blinded-ratio | `repeat-trades` | cards_with_tied_nn | 231 | 236 |
| blinded-ratio | `repeat-trades` | nn_tie_low | 0.091503 | 0.078431 |
| blinded-ratio | `repeat-trades` | nn_tie_free | 0.22216 | 0.213445 |
| blinded-ratio | `repeat-trades` | nn_tie_free_chance_1pct | 0.16227 | 0.161858 |
| blinded-ratio | `repeat-takerbuy` | pair_auc | 0.505484 | 0.505313 |
| blinded-ratio | `repeat-takerbuy` | auc_chance_1pct | 0.513182 | 0.512732 |
| blinded-ratio | `repeat-openint` | nn_same_coin_accuracy | 0.111111 | 0.104575 |
| blinded-ratio | `repeat-openint` | nn_chance_1pct | 0.169935 | 0.173203 |
| blinded-ratio | `repeat-openint` | pair_auc | 0.53459 | 0.534734 |
| blinded-ratio | `repeat-openint` | auc_chance_1pct | 0.512409 | 0.512364 |
| blinded-ratio | `repeat-openint` | cards_with_tied_nn | 283 | 284 |
| blinded-ratio | `repeat-openint` | nn_tie_free | 0.11507 | 0.114634 |
| blinded-ratio | `repeat-openint` | nn_tie_free_chance_1pct | 0.148615 | 0.148424 |
| blinded-ratio | `repeat-ratio` | cards_with_tied_nn | 3 | 5 |
| blinded-ratio | `repeat-depth` | pair_auc | 0.538332 | 0.538307 |
| blinded-ratio | `repeat-depth` | auc_chance_1pct | 0.512939 | 0.512936 |
| blinded-ratio | `repeat-depth` | nn_tie_free | 0.18171 | 0.181438 |
| blinded-ratio | `repeat-depth` | nn_tie_free_chance_1pct | 0.149343 | 0.149987 |
| blinded-ratio | `granularity-close` | pair_auc | 0.596809 | 0.599532 |
| blinded-ratio | `granularity-close` | auc_chance_1pct | 0.513207 | 0.512967 |
| blinded-ratio | `granularity-close` | nn_tie_free | 0.194551 | 0.194823 |
| blinded-ratio | `granularity-close` | nn_tie_free_chance_1pct | 0.133443 | 0.133656 |
| blinded-rank | `funding-line` | nn_same_coin_accuracy | 0.153595 | 0.150327 |
| blinded-rank | `funding-line` | pair_auc | 0.592679 | 0.592675 |
| blinded-rank | `funding-line` | auc_chance_1pct | 0.5112 | 0.511202 |
| blinded-rank | `funding-line` | cards_with_tied_nn | 184 | 186 |
| blinded-rank | `funding-line` | nn_tie_low | 0.091503 | 0.088235 |
| blinded-rank | `funding-line` | nn_tie_high | 0.53268 | 0.535948 |
| blinded-rank | `funding-line` | nn_tie_free | 0.183139 | 0.182594 |
| blinded-rank | `funding-line` | nn_tie_free_chance_1pct | 0.162366 | 0.162494 |
| blinded-rank | `repeat-close` | pair_auc | 0.542144 | 0.541608 |
| blinded-rank | `repeat-close` | auc_chance_1pct | 0.510666 | 0.510755 |
| blinded-rank | `repeat-chg` | pair_auc | 0.523074 | 0.523354 |
| blinded-rank | `repeat-chg` | auc_chance_1pct | 0.512879 | 0.512968 |
| blinded-rank | `repeat-volume` | pair_auc | 0.506038 | 0.505981 |
| blinded-rank | `repeat-volume` | auc_chance_1pct | 0.511512 | 0.511495 |
| blinded-rank | `repeat-trades` | nn_same_coin_accuracy | 0.232026 | 0.22549 |
| blinded-rank | `repeat-trades` | pair_auc | 0.58522 | 0.585348 |
| blinded-rank | `repeat-trades` | auc_chance_1pct | 0.512746 | 0.512775 |
| blinded-rank | `repeat-trades` | cards_with_tied_nn | 231 | 236 |
| blinded-rank | `repeat-trades` | nn_tie_low | 0.091503 | 0.078431 |
| blinded-rank | `repeat-trades` | nn_tie_free | 0.22216 | 0.213445 |
| blinded-rank | `repeat-trades` | nn_tie_free_chance_1pct | 0.16227 | 0.161858 |
| blinded-rank | `repeat-takerbuy` | pair_auc | 0.505484 | 0.505313 |
| blinded-rank | `repeat-takerbuy` | auc_chance_1pct | 0.513182 | 0.512732 |
| blinded-rank | `repeat-openint` | pair_auc | 0.621051 | 0.621996 |
| blinded-rank | `repeat-openint` | auc_chance_1pct | 0.513329 | 0.513399 |
| blinded-rank | `repeat-openint` | nn_tie_free_chance_1pct | 0.141941 | 0.142742 |
| blinded-rank | `repeat-ratio` | cards_with_tied_nn | 4 | 5 |
| blinded-rank | `repeat-depth` | pair_auc | 0.535063 | 0.535053 |
| blinded-rank | `repeat-depth` | auc_chance_1pct | 0.51332 | 0.513322 |
| blinded-rank | `granularity-close` | pair_auc | 0.596809 | 0.599532 |
| blinded-rank | `granularity-close` | auc_chance_1pct | 0.513207 | 0.512967 |
| blinded-rank | `granularity-close` | nn_tie_free | 0.194551 | 0.194823 |
| blinded-rank | `granularity-close` | nn_tie_free_chance_1pct | 0.133443 | 0.133656 |
| blinded-strict | `trades-level` | pair_auc | 0.529516 | 0.52952 |
| blinded-strict | `trades-level` | auc_chance_1pct | 0.513496 | 0.513493 |
| blinded-strict | `funding-line` | nn_same_coin_accuracy | 0.153595 | 0.150327 |
| blinded-strict | `funding-line` | pair_auc | 0.592679 | 0.592675 |
| blinded-strict | `funding-line` | auc_chance_1pct | 0.5112 | 0.511202 |
| blinded-strict | `funding-line` | cards_with_tied_nn | 184 | 186 |
| blinded-strict | `funding-line` | nn_tie_low | 0.091503 | 0.088235 |
| blinded-strict | `funding-line` | nn_tie_high | 0.53268 | 0.535948 |
| blinded-strict | `funding-line` | nn_tie_free | 0.183139 | 0.182594 |
| blinded-strict | `funding-line` | nn_tie_free_chance_1pct | 0.162366 | 0.162494 |
| blinded-strict | `repeat-close` | pair_auc | 0.542144 | 0.541608 |
| blinded-strict | `repeat-close` | auc_chance_1pct | 0.510666 | 0.510755 |
| blinded-strict | `repeat-chg` | pair_auc | 0.523074 | 0.523354 |
| blinded-strict | `repeat-chg` | auc_chance_1pct | 0.512879 | 0.512968 |
| blinded-strict | `repeat-volume` | pair_auc | 0.506038 | 0.505981 |
| blinded-strict | `repeat-volume` | auc_chance_1pct | 0.511512 | 0.511495 |
| blinded-strict | `repeat-trades` | nn_same_coin_accuracy | 0.232026 | 0.22549 |
| blinded-strict | `repeat-trades` | pair_auc | 0.58522 | 0.585348 |
| blinded-strict | `repeat-trades` | auc_chance_1pct | 0.512746 | 0.512775 |
| blinded-strict | `repeat-trades` | cards_with_tied_nn | 231 | 236 |
| blinded-strict | `repeat-trades` | nn_tie_low | 0.091503 | 0.078431 |
| blinded-strict | `repeat-trades` | nn_tie_free | 0.22216 | 0.213445 |
| blinded-strict | `repeat-trades` | nn_tie_free_chance_1pct | 0.16227 | 0.161858 |
| blinded-strict | `repeat-takerbuy` | pair_auc | 0.502733 | 0.50287 |
| blinded-strict | `repeat-takerbuy` | auc_chance_1pct | 0.513045 | 0.513118 |
| blinded-strict | `repeat-takerbuy` | nn_tie_free_chance_1pct | 0.132817 | 0.132718 |
| blinded-strict | `repeat-openint` | pair_auc | 0.621051 | 0.621996 |
| blinded-strict | `repeat-openint` | auc_chance_1pct | 0.513329 | 0.513399 |
| blinded-strict | `repeat-openint` | nn_tie_free_chance_1pct | 0.141941 | 0.142742 |
| blinded-strict | `repeat-ratio` | cards_with_tied_nn | 4 | 5 |
| blinded-strict | `repeat-depth` | pair_auc | 0.535063 | 0.535053 |
| blinded-strict | `repeat-depth` | auc_chance_1pct | 0.51332 | 0.513322 |
| blinded-strict | `granularity-close` | pair_auc | 0.596809 | 0.599532 |
| blinded-strict | `granularity-close` | auc_chance_1pct | 0.513207 | 0.512967 |
| blinded-strict | `granularity-close` | nn_tie_free | 0.194551 | 0.194823 |
| blinded-strict | `granularity-close` | nn_tie_free_chance_1pct | 0.133443 | 0.133656 |
| blinded-strict-flags | `trades-level` | pair_auc | 0.529516 | 0.52952 |
| blinded-strict-flags | `trades-level` | auc_chance_1pct | 0.513496 | 0.513493 |
| blinded-strict-flags | `repeat-close` | pair_auc | 0.542144 | 0.541608 |
| blinded-strict-flags | `repeat-close` | auc_chance_1pct | 0.510666 | 0.510755 |
| blinded-strict-flags | `repeat-chg` | pair_auc | 0.523074 | 0.523354 |
| blinded-strict-flags | `repeat-chg` | auc_chance_1pct | 0.512879 | 0.512968 |
| blinded-strict-flags | `repeat-volume` | pair_auc | 0.506038 | 0.505981 |
| blinded-strict-flags | `repeat-volume` | auc_chance_1pct | 0.511512 | 0.511495 |
| blinded-strict-flags | `repeat-trades` | nn_same_coin_accuracy | 0.232026 | 0.22549 |
| blinded-strict-flags | `repeat-trades` | pair_auc | 0.58522 | 0.585348 |
| blinded-strict-flags | `repeat-trades` | auc_chance_1pct | 0.512746 | 0.512775 |
| blinded-strict-flags | `repeat-trades` | cards_with_tied_nn | 231 | 236 |
| blinded-strict-flags | `repeat-trades` | nn_tie_low | 0.091503 | 0.078431 |
| blinded-strict-flags | `repeat-trades` | nn_tie_free | 0.22216 | 0.213445 |
| blinded-strict-flags | `repeat-trades` | nn_tie_free_chance_1pct | 0.16227 | 0.161858 |
| blinded-strict-flags | `repeat-takerbuy` | pair_auc | 0.502733 | 0.50287 |
| blinded-strict-flags | `repeat-takerbuy` | auc_chance_1pct | 0.513045 | 0.513118 |
| blinded-strict-flags | `repeat-takerbuy` | nn_tie_free_chance_1pct | 0.132817 | 0.132718 |
| blinded-strict-flags | `repeat-openint` | pair_auc | 0.621051 | 0.621996 |
| blinded-strict-flags | `repeat-openint` | auc_chance_1pct | 0.513329 | 0.513399 |
| blinded-strict-flags | `repeat-openint` | nn_tie_free_chance_1pct | 0.141941 | 0.142742 |
| blinded-strict-flags | `repeat-ratio` | cards_with_tied_nn | 4 | 5 |
| blinded-strict-flags | `repeat-depth` | pair_auc | 0.535063 | 0.535053 |
| blinded-strict-flags | `repeat-depth` | auc_chance_1pct | 0.51332 | 0.513322 |
| blinded-strict-flags | `granularity-close` | pair_auc | 0.596809 | 0.599532 |
| blinded-strict-flags | `granularity-close` | auc_chance_1pct | 0.513207 | 0.512967 |
| blinded-strict-flags | `granularity-close` | nn_tie_free | 0.194551 | 0.194823 |
| blinded-strict-flags | `granularity-close` | nn_tie_free_chance_1pct | 0.133443 | 0.133656 |
| blinded-strict-flags-k1 | `trades-level` | pair_auc | 0.529516 | 0.52952 |
| blinded-strict-flags-k1 | `trades-level` | auc_chance_1pct | 0.513496 | 0.513493 |
| blinded-strict-flags-k1 | `repeat-close` | pair_auc | 0.563626 | 0.563862 |
| blinded-strict-flags-k1 | `repeat-close` | auc_chance_1pct | 0.512749 | 0.512765 |
| blinded-strict-flags-k1 | `repeat-chg` | pair_auc | 0.523074 | 0.523354 |
| blinded-strict-flags-k1 | `repeat-chg` | auc_chance_1pct | 0.512879 | 0.512968 |
| blinded-strict-flags-k1 | `repeat-volume` | pair_auc | 0.506038 | 0.505981 |
| blinded-strict-flags-k1 | `repeat-volume` | auc_chance_1pct | 0.511512 | 0.511495 |
| blinded-strict-flags-k1 | `repeat-trades` | nn_same_coin_accuracy | 0.232026 | 0.22549 |
| blinded-strict-flags-k1 | `repeat-trades` | pair_auc | 0.58522 | 0.585348 |
| blinded-strict-flags-k1 | `repeat-trades` | auc_chance_1pct | 0.512746 | 0.512775 |
| blinded-strict-flags-k1 | `repeat-trades` | cards_with_tied_nn | 231 | 236 |
| blinded-strict-flags-k1 | `repeat-trades` | nn_tie_low | 0.091503 | 0.078431 |
| blinded-strict-flags-k1 | `repeat-trades` | nn_tie_free | 0.22216 | 0.213445 |
| blinded-strict-flags-k1 | `repeat-trades` | nn_tie_free_chance_1pct | 0.16227 | 0.161858 |
| blinded-strict-flags-k1 | `repeat-takerbuy` | pair_auc | 0.502733 | 0.50287 |
| blinded-strict-flags-k1 | `repeat-takerbuy` | auc_chance_1pct | 0.513045 | 0.513118 |
| blinded-strict-flags-k1 | `repeat-takerbuy` | nn_tie_free_chance_1pct | 0.132817 | 0.132718 |
| blinded-strict-flags-k1 | `repeat-openint` | pair_auc | 0.621051 | 0.621996 |
| blinded-strict-flags-k1 | `repeat-openint` | auc_chance_1pct | 0.513329 | 0.513399 |
| blinded-strict-flags-k1 | `repeat-openint` | nn_tie_free_chance_1pct | 0.141941 | 0.142742 |
| blinded-strict-flags-k1 | `repeat-ratio` | cards_with_tied_nn | 4 | 5 |
| blinded-strict-flags-k1 | `repeat-depth` | pair_auc | 0.535063 | 0.535053 |
| blinded-strict-flags-k1 | `repeat-depth` | auc_chance_1pct | 0.51332 | 0.513322 |
| blinded-strict-flags-k1 | `granularity-close` | nn_same_coin_accuracy | 0.215686 | 0.20915 |
| blinded-strict-flags-k1 | `granularity-close` | nn_chance_1pct | 0.173203 | 0.176471 |
| blinded-strict-flags-k1 | `granularity-close` | pair_auc | 0.630049 | 0.630346 |
| blinded-strict-flags-k1 | `granularity-close` | auc_chance_1pct | 0.512271 | 0.512305 |
| blinded-strict-flags-k1 | `granularity-close` | cards_with_tied_nn | 256 | 257 |
| blinded-strict-flags-k1 | `granularity-close` | nn_tie_low | 0.052288 | 0.04902 |
| blinded-strict-flags-k1 | `granularity-close` | nn_tie_free | 0.254526 | 0.252484 |
| blinded-strict-flags-k1 | `granularity-close` | nn_tie_free_chance_1pct | 0.154744 | 0.156651 |
| blinded-strict-flags-unrounded | `repeat-close` | pair_auc | 0.542144 | 0.541608 |
| blinded-strict-flags-unrounded | `repeat-close` | auc_chance_1pct | 0.510666 | 0.510755 |
| blinded-strict-flags-unrounded | `repeat-chg` | pair_auc | 0.523074 | 0.523354 |
| blinded-strict-flags-unrounded | `repeat-chg` | auc_chance_1pct | 0.512879 | 0.512968 |
| blinded-strict-flags-unrounded | `repeat-depth` | auc_chance_1pct | 0.507118 | 0.507119 |
| blinded-strict-flags-unrounded | `granularity-close` | pair_auc | 0.596809 | 0.599532 |
| blinded-strict-flags-unrounded | `granularity-close` | auc_chance_1pct | 0.513207 | 0.512967 |
| blinded-strict-flags-unrounded | `granularity-close` | nn_tie_free | 0.194551 | 0.194823 |
| blinded-strict-flags-unrounded | `granularity-close` | nn_tie_free_chance_1pct | 0.133443 | 0.133656 |

Gate row (`ALL-removable`) in the exact audit:

| card set | features | NN (line) | tied cards | tie-free (line) | pair AUC (line) |
|---|---|---|---|---|---|
| raw-observation | 56 | 0.624183 (0.173203) YES | 0 | 0.624183 (0.173203) YES | 0.706435 (0.512713) YES |
| blinded-ratio | 40 | 0.405229 (0.173203) YES | 0 | 0.405229 (0.173203) YES | 0.615496 (0.5126) YES |
| blinded-rank | 47 | 0.447712 (0.169935) YES | 0 | 0.447712 (0.169935) YES | 0.581433 (0.513237) YES |
| blinded-strict | 44 | 0.408497 (0.169935) YES | 0 | 0.408497 (0.169935) YES | 0.574149 (0.513603) YES |
| blinded-strict-flags | 44 | 0.408497 (0.169935) YES | 0 | 0.408497 (0.169935) YES | 0.574149 (0.513603) YES |
| blinded-strict-flags-k1 | 44 | 0.434641 (0.176471) YES | 0 | 0.434641 (0.176471) YES | 0.577011 (0.51371) YES |
| blinded-strict-flags-unrounded | 26 | 0.238562 (0.176471) YES | 0 | 0.238562 (0.176471) YES | 0.545585 (0.51371) YES |

Accepted (K-13): **True**.

## H-4 · what the unrounded-rank rendering changes (K-16)

On the 306 observation cards; `strict-flags` against the unrounded-rank set, paired by `source_card`. "Tied on the raw card": the hour prints the same token as another hour of the same column on the raw card's before table. "Ranked apart": such an hour gets a different rank from an hour it ties with, on the unrounded-rank card.

| column | cards where the two renderings differ | cards with a printed tie | hours tied on the raw card | of those, ranked apart | cards with an hour ranked apart |
|---|---|---|---|---|---|
| `quote vol` | 48 | 48 | 119 | 119 | 48 |
| `trades` | 298 | 299 | 4585 | 4567 | 298 |
| `taker buy%` | 227 | 227 | 798 | 798 | 227 |
| `open int` | 190 | 192 | 1309 | 1302 | 190 |
| `L/S acct` | 304 | 304 | 4884 | 4860 | 304 |
| `top L/S pos` | 306 | 306 | 5626 | 5626 | 306 |
| `taker L/S` | 267 | 267 | 1482 | 1482 | 267 |
| `depth -1%` | 62 | 66 | 339 | 275 | 62 |
| `depth +1%` | 78 | 78 | 368 | 365 | 78 |

Cards with at least one hour ranked apart in any ranked column: **306 of 306**.

## H-5 · same coin, same start hour

Coin-and-start-hour combinations carrying two or more observation moments: **0**.

## Inputs

Run number `516027c6c9f215d6` = SHA-256 over this script and 957 input files (the 306 cards, the probes and audit outputs named above, the two card sets of H-4).

