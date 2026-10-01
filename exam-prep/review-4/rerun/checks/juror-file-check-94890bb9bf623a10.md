# Juror-file check (fourth-fix) — run `94890bb9bf623a10`

Written by `scripts/31_juror_file_check_fourth.py` at 2026-10-01T22:12:32Z (system clock).

## N and G · numbers: 59 checks, 0 failed

| file | expected text (as recomputed) | source | found |
|---|---|---|---|
| JQ-N1.md | under move-window     both give **168** events, and **4** events | 30 H-2 | yes |
| JQ-N1.md | under card-span "earliest" gives **125** events and     "latest" **124**, and **21** events appear in one partition only | 30 H-2 | yes |
| JQ-N1.md | / move-window / greedy-clique / cross-coin, keep latest / 168 / 78 / 6 / 50 / 0 / 1 / | 30 H-2 table row | yes |
| JQ-N1.md | / card-span / greedy-clique / cross-coin, keep latest / 124 / 39 / 7 / 60 / 0 / 1 / | 30 H-2 table row | yes |
| JQ-N1.md | 1 event (5 cards) under move-window, 0 under card-span | 30 H-2 table row | yes |
| JQ-N1.md | In the observation cards no coin has two moments at the same start hour, | 30 H-5 | yes |
| JQ-N1.md | fourth-fix-checks-516027c6c9f215d6.md | run id | yes |
| JQ-N1.md | `a0ecf6970d86b199`   reproduce every output of that run byte for byte | cmp of the three CSVs | yes |
| JQ-N1.md | passage from '## The scale of the choice' to '## Part 1' is byte-identical to the third-fix file | third-fix text; table = run 756cf4ea156d92c3 | yes |
| JQ-N1.md | summary row 'no collapse' = ['306', '306', '1', '0', '0', '1'] | collapse-summary a0ecf6970d86b199 | yes |
| JQ-N1.md | summary row 'start-hour / – / any' = ['289', '274', '3', '2', '0', '1'] | collapse-summary a0ecf6970d86b199 | yes |
| JQ-N1.md | summary row 'start-hour / – / cross-coin' = ['289', '274', '3', '2', '0', '1'] | collapse-summary a0ecf6970d86b199 | yes |
| JQ-N1.md | summary row 'move-window / component / any' = ['131', '49', '8', '52', '15', '2'] | collapse-summary a0ecf6970d86b199 | yes |
| JQ-N1.md | summary row 'move-window / component / cross-coin' = ['136', '56', '8', '52', '10', '2'] | collapse-summary a0ecf6970d86b199 | yes |
| JQ-N1.md | summary row 'move-window / greedy-clique / any' = ['161', '68', '6', '49', '10', '2'] | collapse-summary a0ecf6970d86b199 | yes |
| JQ-N1.md | summary row 'move-window / greedy-clique / cross-coin' = ['168', '78', '6', '50', '0', '1'] | collapse-summary a0ecf6970d86b199 | yes |
| JQ-N1.md | summary row 'card-span / component / any' = ['58', '10', '20', '37', '25', '5'] | collapse-summary a0ecf6970d86b199 | yes |
| JQ-N1.md | summary row 'card-span / component / cross-coin' = ['62', '13', '20', '39', '26', '4'] | collapse-summary a0ecf6970d86b199 | yes |
| JQ-N1.md | summary row 'card-span / greedy-clique / any' = ['116', '32', '7', '56', '13', '3'] | collapse-summary a0ecf6970d86b199 | yes |
| JQ-N1.md | summary row 'card-span / greedy-clique / cross-coin' = ['125', '41', '7', '60', '0', '1'] | collapse-summary a0ecf6970d86b199 | yes |
| JQ-N1.md | passage from '## Part 1' to '## Part 2' is byte-identical to the third-fix file | third-fix text | yes |
| JQ-N1.md | passage from 'What the two ways do to the 1% boundary' to '## The strongest objection' is byte-identical to the third-fix file | third-fix text (E-4, G-2) | yes |
| JQ-N1.md | passage from '## The strongest objection' is byte-identical to the third-fix file | third-fix text | yes |
| JQ-R04-CONTENT.md | / from the printed values / typical level of the ranked column / **0.5295** (0.5135) — beats / **0.1541** (0.1403) — beats / | exact audit 9ff0ffec3fe21ebe | yes |
| JQ-R04-CONTENT.md | / from the printed values / how many values repeat in the column / **0.5853** (0.5128) — beats / **0.2134** (0.1619) — beats / | exact audit 9ff0ffec3fe21ebe | yes |
| JQ-R04-CONTENT.md | / from the values before rounding / typical level of the ranked column / 0.4997 (0.5033) — does not beat / 0.1256 (0.1256) — does not beat / | exact audit d6557e91f9f97f7b | yes |
| JQ-R04-CONTENT.md | / from the values before rounding / how many values repeat in the column / 0.5012 (0.5081) — does not beat / 0.1210 (0.1248) — does not beat / | exact audit d6557e91f9f97f7b | yes |
| JQ-R04-CONTENT.md | audit run   `9ff0ffec3fe21ebe`) | run id | yes |
| JQ-R04-CONTENT.md | audit run `d6557e91f9f97f7b`) | run id | yes |
| JQ-R04-CONTENT.md | / 2 decimals (first run) / 36 / **0.5416** (0.5108) / **0.1408** (0.1387) / **0.5995** (0.5130) / **0.1948** (0.1337) / | exact audit; k1 manifest | yes |
| JQ-R04-CONTENT.md | / 3 decimals (the fewest at which rounding makes no new repeats) / 0 / **0.5639** (0.5128) / **0.1510** (0.1401) / **0.6303** (0.5123) / **0.2525** (0.1567) / | exact audit; k1 manifest | yes |
| JQ-R04-CONTENT.md | decimals, 0.1408 against 0.1387; | exact audit | yes |
| JQ-R04-CONTENT.md | audit runs `9ff0ffec3fe21ebe` (2 decimals) and `762815a877c19551` (3 decimals) | run ids | yes |
| JQ-R04-CONTENT.md | / `L/S acct` / 4,884 / 4,860 / 304 / | 30 H-4 | yes |
| JQ-R04-CONTENT.md | / `depth +1%` / 368 / 365 / 78 / | 30 H-4 | yes |
| JQ-R04-CONTENT.md | / `depth -1%` / 339 / 275 / 62 / | 30 H-4 | yes |
| JQ-R04-CONTENT.md | / `open int` / 1,309 / 1,302 / 190 / | 30 H-4 | yes |
| JQ-R04-CONTENT.md | / `quote vol` / 119 / 119 / 48 / | 30 H-4 | yes |
| JQ-R04-CONTENT.md | / `taker L/S` / 1,482 / 1,482 / 267 / | 30 H-4 | yes |
| JQ-R04-CONTENT.md | / `taker buy%` / 798 / 798 / 227 / | 30 H-4 | yes |
| JQ-R04-CONTENT.md | / `top L/S pos` / 5,626 / 5,626 / 306 / | 30 H-4 | yes |
| JQ-R04-CONTENT.md | / `trades` / 4,585 / 4,567 / 298 / | 30 H-4 | yes |
| JQ-R04-CONTENT.md | Every one of the 306 cards has at least one such hour | 30 H-4 | yes |
| JQ-R04-CONTENT.md | run `516027c6c9f215d6`, H-4 | run id | yes |
| JQ-R04-CONTENT.md | q2: share of further shuffles at or above the observed repeat-close score is below the 1% boundary's share and near it (0.0065) | review-3 q2_tiefree_strict-flags.out | yes |
| JQ-R04-CONTENT.md | passage from 'What the frozen canteen book does with t' to '**Question a.**' is byte-identical to the third-fix file | third-fix text | yes |
| JQ-R04-DATE.md | passage from '## What you decide' to 'These three parts should be an' is byte-identical to the third-fix file | third-fix text | yes |
| JQ-R04-DATE.md | passage from 'For each part: your answer' is byte-identical to the third-fix file | third-fix text | yes |
| JQ-CANTEEN-8.md | passage from '## What you decide' to 'Answer together with JQ-N1' is byte-identical to the third-fix file | third-fix text | yes |
| JQ-CANTEEN-8.md | passage from '## What has been measured' to "The canteen chair's figure" is byte-identical to the third-fix file | third-fix text; counts = 26 G-3, REVIEW-3 q3 | yes |
| JQ-CANTEEN-8.md | passage from '## Part a' is byte-identical to the third-fix file | third-fix text | yes |
| JQ-CANTEEN-8.md | Their cards start 14 hours apart, so their before windows share 10 hours | cards C010, C011 | yes |
| JQ-CANTEEN-8.md | while their card spans share 34 | cards C010, C011 | yes |
| JQ-R04-GATE.md (third-fix, not written) | SHA-256 55e7b95c9bc4beb7eb78418ed230270661d14ed92876bb13d047d1b853f816ce | instruction | yes |
| JQ-R04-GATE.md (third-fix, not written) | blinded-strict-flags: the GATE row's figures equal the exact audit's / 0.4085 (0.1699) — beats / 0.5741 (0.5136) — beats /; features 44; tied cards 0 | exact audit 9ff0ffec3fe21ebe | yes |
| JQ-R04-GATE.md (third-fix, not written) | blinded-strict: the GATE row's figures equal the exact audit's / 0.4085 (0.1699) — beats / 0.5741 (0.5136) — beats /; features 44; tied cards 0 | exact audit 45d062efe77c9251 | yes |
| JQ-R04-GATE.md (third-fix, not written) | blinded-rank: the GATE row's figures equal the exact audit's / 0.4477 (0.1699) — beats / 0.5814 (0.5132) — beats /; features 47; tied cards 0 | exact audit 446adf64f8e8235c | yes |
| JQ-R04-GATE.md (third-fix, not written) | blinded-ratio: the GATE row's figures equal the exact audit's / 0.4052 (0.1732) — beats / 0.6155 (0.5126) — beats /; features 40; tied cards 0 | exact audit 989b8f21b23e0310 | yes |
| JQ-R04-GATE.md (third-fix, not written) | blinded-strict-flags-k1: the GATE row's figures equal the exact audit's / 0.4346 (0.1765) — beats / 0.5770 (0.5137) — beats /; features 44; tied cards 0 | exact audit 762815a877c19551 | yes |

## L · line citations, with the cited text

| juror file | cites | text of the cited lines |
|---|---|---|
| JQ-CANTEEN-8.md | canteen/2026-09-19-sofia.md 918–933 | ## 8 · The open question I do not answer /  / **May two calm moments overlap each other?** TACTICS 2 spaces large moments 48 / hours apart and keeps calm moments 72 hours from a large one, but says **nothing** / about calm-to-calm. Instances verified value by value: C161/C162 (15 h apart, / both calm, funding sequences overlapping exactly — Kenji round-2 A4/A5), / C084/C085 (33 h apart, both calm, 15 byte-identical rows — Amara round-2 C5, / Lukas b05 X15), C050/C051/C052 (one ~85-hour stretch, byte-identical rows — / Lukas b06 §4, Kenji round-2 A6), C010/C011 (10 h overlap, both calm — Ingrid b03 / §E, Kenji b03 G34, Amara b03 §4, Lukas b03 §A). The manifest measures it at / **135 calm+calm overlapping pairs out of 495**. /  / Ingrid (b09 §G) referred it to a juror rather than deciding it, and Lukas / round-2 §D calls that the correct handling and the only instance of it in the 27 / files. **This is an open question under RULES 33 and I do not answer it.** A / juror decides procedure and definition; the canteen chair does not. |
| JQ-CANTEEN-8.md | TACTICS.md 38–39 | - The largest 20 of the year are taken for each coin. / - Of two moments closer than 48 hours to each other, only the larger counts. |
| JQ-CANTEEN-8.md | TACTICS.md 42–43 | - **Calm moment:** the same number as the large moments, chosen at random. At / least 72 hours away from any large movement. |
| JQ-CANTEEN-8.md | TACTICS.md 44–44 | - A moment's start is the hour at which the 24-hour movement began. |
| JQ-CANTEEN-8.md | TACTICS.md 50–53 | - **Before:** the 24 hours before the start, hour by hour; plus a one-line / summary of the previous 7 days. / - **After:** the 24 hours after the start. Shown only in free observation, never / in the exam. |
| JQ-CANTEEN-8.md | RULES.md 53–54 | 13. Moments occurring in several coins in the same hour count as a single event. / If the whole market moved together, that is one event. |
| JQ-CANTEEN-8.md | canteen/2026-09-19-sofia.md 920–922 | **May two calm moments overlap each other?** TACTICS 2 spaces large moments 48 / hours apart and keeps calm moments 72 hours from a large one, but says **nothing** / about calm-to-calm. Instances verified value by value: C161/C162 (15 h apart, |
| JQ-CANTEEN-8.md | scripts/06_find_moments.py 63–65 | R5  TACTICS 2 puts no minimum distance between two *calm* moments. None is / imposed here. How many calm pairs ended up closer than 48 h is measured and / written into the manifest. |
| JQ-CANTEEN-8.md | canteen (bare) 203–204 | C010 and C011 overlap by ten hours (Ingrid b03 §E, Kenji b03 G34, / Amara b03 §4, Lukas b03) so they are nearer one observation than two. |
| JQ-N1.md | RULES.md 53–54 | 13. Moments occurring in several coins in the same hour count as a single event. / If the whole market moved together, that is one event. |
| JQ-N1.md | TACTICS.md 127–127 | - A moment appearing in several cards in the same hour counts as a single event. |
| JQ-N1.md | TACTICS.md 44–44 | - A moment's start is the hour at which the 24-hour movement began. |
| JQ-N1.md | TACTICS.md 39–39 | - Of two moments closer than 48 hours to each other, only the larger counts. |
| JQ-N1.md | TACTICS.md 43–43 | least 72 hours away from any large movement. |
| JQ-N1.md | RULES.md 51–52 | 12. The chance line is not invented. The answers are shuffled 1,000 times, and / the real result must fall inside the best 1%. |
| JQ-R04-CONTENT.md | canteen/2026-09-19-sofia.md 112–120 | ``` / Rule no: S-1 · the magnitude gate / Trigger  : In the card's Before table (rows h-24 .. h-1, 24 rows), at least one / row whose hourly close-to-close change is /5.00%/ or more. / Read it from the `chg%` column. If an exam card does not print / `chg%`, compute it from the `close` column as / close(h)/close(h-1) - 1 — a percentage change is unchanged by / TACTICS 6's rebasing of price to a number starting from 100, so the / trigger is computable on a card whose price is hidden. |
| JQ-R04-CONTENT.md | RULES.md 41–41 | 9. In the exam the coin name and the date are hidden. The answer key is sealed |
| JQ-R04-CONTENT.md | RULES.md 34–35 | 6. The rule is written first, the result is opened second. A rule is not changed / after looking at a result. If it is changed it counts as a new rule, carries |
| JQ-R04-CONTENT.md | TACTICS.md 56–56 | - price, volume, trade count, taker buy/sell pressure |
| JQ-R04-CONTENT.md | TACTICS.md 57–57 | - open interest, long/short ratios (5-minute archive) |
| JQ-R04-CONTENT.md | TACTICS.md 71–71 | Numbers are rounded and the card is kept short. The AI never sees raw seconds. |
| JQ-R04-CONTENT.md | TACTICS.md 101–104 | - **What is hidden:** / - the coin name / - the date and time / - the price itself (converted to a number starting from 100) |
| JQ-R04-CONTENT.md | canteen/2026-09-19-sofia.md 114–120 | Trigger  : In the card's Before table (rows h-24 .. h-1, 24 rows), at least one / row whose hourly close-to-close change is /5.00%/ or more. / Read it from the `chg%` column. If an exam card does not print / `chg%`, compute it from the `close` column as / close(h)/close(h-1) - 1 — a percentage change is unchanged by / TACTICS 6's rebasing of price to a number starting from 100, so the / trigger is computable on a card whose price is hidden. |
| JQ-R04-CONTENT.md | canteen/2026-09-19-sofia.md 221–225 | Rule no: B-2 · the `taker L/S` column may not be read / Trigger  : always — the column is excluded from every score. / Direction: none — blocker on the data. / Exit     : n/a. It lifts only when somebody checks the column against the / 5-minute taker archive and states a trade-count floor. |
| JQ-R04-CONTENT.md | canteen/2026-09-19-sofia.md 245–246 | Trigger  : any hour of the card prints `open int` = 0 between live neighbours. / On such a card no open-interest statistic may be computed. |
| JQ-R04-CONTENT.md | canteen/2026-09-19-sofia.md 268–270 | Trigger  : the `depth -1%` or `depth +1%` column repeats one identical value / for three or more consecutive hours. On such a card and such hours / no depth statistic may be computed. |
| JQ-R04-CONTENT.md | canteen/2026-09-19-sofia.md 667–671 | 4. **The trade-count floor under `taker L/S`.** No watcher names a number. Amara / round-2 E4 calls it "the single most testable data-integrity claim in the / three sets of notes". **How determined:** by Mateo/Nadia against the 5-minute / taker archive, as a data-cleaning decision, not a trading decision. Until / then B-2 excludes the column outright, which needs no number. |
| JQ-R04-CONTENT.md | canteen (bare) 229–234 | (card-verified both, and adds that C236's hour carries **4k trades**, / not a thin hour, which kills the innocent thin-hour explanation); / Ingrid · round 2 B4 (card-verified both; C264 prints 174.20 on 246 / trades, 252.83 on 128, 1518.43 on 231 and 0.00 on 14); Amara · / round 2 C4 (card-verified C259 h-15: `taker L/S` 119.53 while the / SAME ROW's `taker buy%` is 47.3, on 333 trades — the two columns |
| JQ-R04-CONTENT.md | canteen (bare) 224–225 | Exit     : n/a. It lifts only when somebody checks the column against the / 5-minute taker archive and states a trade-count floor. |
| JQ-R04-CONTENT.md | canteen (bare) 667–671 | 4. **The trade-count floor under `taker L/S`.** No watcher names a number. Amara / round-2 E4 calls it "the single most testable data-integrity claim in the / three sets of notes". **How determined:** by Mateo/Nadia against the 5-minute / taker archive, as a data-cleaning decision, not a trading decision. Until / then B-2 excludes the column outright, which needs no number. |
| JQ-R04-CONTENT.md | canteen (bare) 116–118 | Read it from the `chg%` column. If an exam card does not print / `chg%`, compute it from the `close` column as / close(h)/close(h-1) - 1 — a percentage change is unchanged by |
| JQ-R04-DATE.md | RULES.md 41–41 | 9. In the exam the coin name and the date are hidden. The answer key is sealed |
| JQ-R04-DATE.md | RULES.md 43–44 | 10. An agent sitting the exam cannot use tools and cannot read files. A paper / where tool use is observed is void. |
| JQ-R04-DATE.md | TACTICS.md 55–62 | **What is on the card** (where data exists): / - price, volume, trade count, taker buy/sell pressure / - open interest, long/short ratios (5-minute archive) / - funding rate, payment interval and its changes / - order book depth (only the moment days are downloaded; the files are large) / - Binance and Korean exchange announcements (listing, delisting, warning) / - bitcoin and ethereum, over the same hours / - US release calendar (inflation, employment, rate decision) |
| JQ-R04-DATE.md | TACTICS.md 101–107 | - **What is hidden:** / - the coin name / - the date and time / - the price itself (converted to a number starting from 100) / - the coin name inside announcements / - the Wikipedia number itself (given as a ratio to the coin's own average) / - the date in the release calendar |

