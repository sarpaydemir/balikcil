# Juror-file check — run `bbb740248b0c8717`

Written by `scripts/28_juror_file_check.py` at 2026-10-01T20:38:38Z (system clock).

## N · numbers: 61 checks, 0 failed

| file | expected text (as recomputed) | source | found |
|---|---|---|---|
| JQ-R04-GATE.md | / `strict-flags` (the recommended one) / `e05144718b909704` / 44 / 0.4085 (0.1699) — beats / 0.5741 (0.5136) — beats / | audit e05144718b909704, ALL-removable | yes |
| JQ-R04-GATE.md | / `strict` / `1f2ae3cf3a5b2044` / 44 / 0.4085 (0.1699) — beats / 0.5741 (0.5136) — beats / | audit 1f2ae3cf3a5b2044, ALL-removable | yes |
| JQ-R04-GATE.md | / `rank` / `96f1d17e27b8afaf` / 47 / 0.4477 (0.1699) — beats / 0.5814 (0.5132) — beats / | audit 96f1d17e27b8afaf, ALL-removable | yes |
| JQ-R04-GATE.md | / `ratio` / `12b07f79e74f0be7` / 40 / 0.4052 (0.1732) — beats / 0.6155 (0.5126) — beats / | audit 12b07f79e74f0be7, ALL-removable | yes |
| JQ-R04-GATE.md | / `strict-flags`, price at 3 decimals / `ded6a9caaf77d910` / 44 / 0.4346 (0.1765) — beats / 0.5770 (0.5137) — beats / | audit ded6a9caaf77d910, ALL-removable | yes |
| JQ-R04-GATE.md | blinded version, it is **44 features** | audit e05144718b909704 features_used | yes |
| JQ-R04-GATE.md | (the row went from 23 to 43 features) | review-2 p6.out; second-fix audit d70dd7b545bfce8a | yes |
| JQ-R04-GATE.md | (43 → 44) | audit e05144718b909704 | yes |
| JQ-R04-GATE.md | from 0.4085 to 0.3987 (line 0.1732; residual diagnostic run `03bf5fc1560d1e33` | residual 03bf5fc1560d1e33 | yes |
| JQ-R04-CONTENT.md | / typical level of the ranked column / **0.5295** (0.5135) — beats / **0.1541** (0.1403) — beats / | audit e05144718b909704 trades-level | yes |
| JQ-R04-CONTENT.md | / how many values repeat in the column / **0.5852** (0.5127) — beats / **0.2222** (0.1623) — beats / | audit e05144718b909704 repeat-trades | yes |
| JQ-R04-CONTENT.md | / 2 decimals (first run) / 36 / **0.5421** (0.5107) / **0.1408** (0.1387) / **0.5968** (0.5132) / **0.1946** (0.1334) / | audits e05144718b909704 / ded6a9caaf77d910; k1 manifest | yes |
| JQ-R04-CONTENT.md | / 3 decimals (the fewest at which rounding makes no new repeats) / 0 / **0.5636** (0.5127) / **0.1510** (0.1401) / **0.6300** (0.5123) / **0.2545** (0.1547) / | audits e05144718b909704 / ded6a9caaf77d910; k1 manifest | yes |
| JQ-R04-CONTENT.md | audit run `e05144718b909704` | run id | yes |
| JQ-R04-CONTENT.md | `e05144718b909704` (2 decimals) | run id | yes |
| JQ-R04-CONTENT.md | `ded6a9caaf77d910` (3 decimals) | run id | yes |
| JQ-R04-DATE.md | run `e05144718b909704`, T4 | run id | yes |
| JQ-R04-DATE.md | **100 of 306** cards print at least one US release name; **30** distinct | T4 | yes |
| JQ-R04-DATE.md | **13** of the 30 names fall on exactly one release day | T4 | yes |
| JQ-R04-DATE.md | **18** cards carry one of them. The 13: | T4 | yes |
| JQ-R04-DATE.md | every one of the 13 release-day names | T4 | yes |
| JQ-R04-DATE.md | **243 of the 495** card | raw T3 13d935bb5cf78346 | yes |
| JQ-R04-DATE.md | **0 false matches among 46,170** pairs | raw T3 13d935bb5cf78346 | yes |
| JQ-R04-DATE.md | **99** cards print at least one release with an hour offset | grep over strict-flags cards | yes |
| JQ-N1.md | / none / independent per card / 0.5719 / 0.5588 / 0.5654 (306) / 0.5654 / 0.5588 – 0.5719 / | E-4 35925ca8acf60690; G-2 212dd7ecffc51263 | yes |
| JQ-N1.md | / start-hour / any / independent per card / 0.5719 / 0.5523 / 0.5744 (289) / 0.5675 / 0.5606 – 0.5744 / | E-4 35925ca8acf60690; G-2 212dd7ecffc51263 | yes |
| JQ-N1.md | / start-hour / any / one per event / 0.5654 / 0.5588 / 0.5744 (289) / 0.5675 / 0.5606 – 0.5744 / | E-4 35925ca8acf60690; G-2 212dd7ecffc51263 | yes |
| JQ-N1.md | / move-window / component / any / one per event / 0.5621 / 0.5948 / 0.6031 (131) / 0.6031 / 0.5878 – 0.6183 / | E-4 35925ca8acf60690; G-2 212dd7ecffc51263 | yes |
| JQ-N1.md | / move-window / greedy-clique / any / one per event / 0.5588 / 0.5980 / 0.5901 (161) / 0.5901 / 0.5776 – 0.6025 / | E-4 35925ca8acf60690; G-2 212dd7ecffc51263 | yes |
| JQ-N1.md | / card-span / component / any / independent per card / 0.5719 / 0.5588 / 0.6552 (58) / 0.6552 / 0.6552 – 0.6552 / | E-4 35925ca8acf60690; G-2 212dd7ecffc51263 | yes |
| JQ-N1.md | / card-span / component / any / one per event / 0.5686 / 0.5621 / 0.6552 (58) / 0.6552 / 0.6552 – 0.6552 / | E-4 35925ca8acf60690; G-2 212dd7ecffc51263 | yes |
| JQ-N1.md | / card-span / greedy-clique / any / one per event / 0.5621 / 0.6013 / 0.6121 (116) / 0.6121 / 0.5948 – 0.6293 / | E-4 35925ca8acf60690; G-2 212dd7ecffc51263 | yes |
| JQ-N1.md | with probability 0.058 | G-2 | yes |
| JQ-N1.md | 0.0196 or more with probability 0.0018 | G-2 | yes |
| JQ-N1.md | 0.0261 or more with probability below 0.0001 | G-2 | yes |
| JQ-N1.md | steps of   0.0065 | G-2 | yes |
| JQ-N1.md | that range is 0.0160 to 0.0345 wide | G-2 | yes |
| JQ-N1.md | 12 events     under move-window and 30 under card-span | G-5 | yes |
| JQ-N1.md | unchanged: 168 and 125) | G-5 | yes |
| JQ-N1.md | found 4 and 21 (card-span: 125 events against     124) | review-2 p1b.out | yes |
| JQ-N1.md | summary row 'no collapse' = ['306', '306', '1', '0', '0', '1'] | collapse-summary bec532fa008e0e01 | yes |
| JQ-N1.md | summary row 'start-hour / – / any' = ['289', '274', '3', '2', '0', '1'] | collapse-summary bec532fa008e0e01 | yes |
| JQ-N1.md | summary row 'start-hour / – / cross-coin' = ['289', '274', '3', '2', '0', '1'] | collapse-summary bec532fa008e0e01 | yes |
| JQ-N1.md | summary row 'move-window / component / any' = ['131', '49', '8', '52', '15', '2'] | collapse-summary bec532fa008e0e01 | yes |
| JQ-N1.md | summary row 'move-window / component / cross-coin' = ['136', '56', '8', '52', '10', '2'] | collapse-summary bec532fa008e0e01 | yes |
| JQ-N1.md | summary row 'move-window / greedy-clique / any' = ['161', '68', '6', '49', '10', '2'] | collapse-summary bec532fa008e0e01 | yes |
| JQ-N1.md | summary row 'move-window / greedy-clique / cross-coin' = ['168', '78', '6', '50', '0', '1'] | collapse-summary bec532fa008e0e01 | yes |
| JQ-N1.md | summary row 'card-span / component / any' = ['58', '10', '20', '37', '25', '5'] | collapse-summary bec532fa008e0e01 | yes |
| JQ-N1.md | summary row 'card-span / component / cross-coin' = ['62', '13', '20', '39', '26', '4'] | collapse-summary bec532fa008e0e01 | yes |
| JQ-N1.md | summary row 'card-span / greedy-clique / any' = ['116', '32', '7', '56', '13', '3'] | collapse-summary bec532fa008e0e01 | yes |
| JQ-N1.md | summary row 'card-span / greedy-clique / cross-coin' = ['125', '41', '7', '60', '0', '1'] | collapse-summary bec532fa008e0e01 | yes |
| JQ-CANTEEN-8.md | / both calm, **same coin** / **21** / **10** / | G-3 | yes |
| JQ-CANTEEN-8.md | / both calm, different coins / 114 / 53 / | G-3 | yes |
| JQ-CANTEEN-8.md | / one calm, one large, different coins / 206 / 97 / | G-3 | yes |
| JQ-CANTEEN-8.md | / both large, different coins / 154 / 101 / | G-3 | yes |
| JQ-CANTEEN-8.md | / one calm, one large, same coin / 0 / 0 / | G-3 | yes |
| JQ-CANTEEN-8.md | / both large, same coin / 0 / 0 / | G-3 | yes |
| JQ-CANTEEN-8.md | "135 calm+calm overlapping pairs out of 495" | G-3 | yes |
| JQ-CANTEEN-8.md | their cards start 14 hours apart, so their before windows   share 10 hours and their card spans 34 | G-3 | yes |
| JQ-CANTEEN-8.md | `212dd7ecffc51263` (G-3) | run id | yes |
| JQ-B1.md | the four facts of 'What is established' | G-4 212dd7ecffc51263 | yes |

## L · line citations, with the cited text

| juror file | cites | text of the cited lines |
|---|---|---|
| JQ-B1.md | canteen/2026-09-19-sofia.md 935–939 | I also record, and do not answer, a second one: **whether B-1's instrument-class / exclusion may be applied at all in a blind exam, given that the only means of / applying it is the de-anonymisation channel of §7.1.** I have ruled it out of the / exam on my own reasoning above; if the laboratory wants a different answer, that / is a procedure question for three jurors, not for me. |
| JQ-B1.md | canteen/2026-09-19-sofia.md 187–187 | Trigger  : the contract is AVGOUSDT or NOKUSDT. |
| JQ-B1.md | TACTICS.md 24–24 | - **Exam:** a different 20 coins (6 · 6 · 4 · 4) |
| JQ-B1.md | scripts/04_draw.py 120–124 | for g in GROUP_ORDER:                       # pass 2: exam, from what remains / remaining = sorted(set(pools[g]) - set(obs_by_group[g])) / pick = rng.sample(remaining, EXAM_QUOTA[g]) / exam_by_group[g] = pick / exam.extend(pick) |
| JQ-B1.md | RULES.md 34–36 | 6. The rule is written first, the result is opened second. A rule is not changed / after looking at a result. If it is changed it counts as a new rule, carries / the "afterwards" label, and is tested again. |
| JQ-CANTEEN-8.md | TACTICS.md 38–39 | - The largest 20 of the year are taken for each coin. / - Of two moments closer than 48 hours to each other, only the larger counts. |
| JQ-CANTEEN-8.md | TACTICS.md 42–43 | - **Calm moment:** the same number as the large moments, chosen at random. At / least 72 hours away from any large movement. |
| JQ-CANTEEN-8.md | TACTICS.md 44–44 | - A moment's start is the hour at which the 24-hour movement began. |
| JQ-CANTEEN-8.md | TACTICS.md 50–53 | - **Before:** the 24 hours before the start, hour by hour; plus a one-line / summary of the previous 7 days. / - **After:** the 24 hours after the start. Shown only in free observation, never / in the exam. |
| JQ-CANTEEN-8.md | RULES.md 53–54 | 13. Moments occurring in several coins in the same hour count as a single event. / If the whole market moved together, that is one event. |
| JQ-CANTEEN-8.md | canteen/2026-09-19-sofia.md 920–922 | **May two calm moments overlap each other?** TACTICS 2 spaces large moments 48 / hours apart and keeps calm moments 72 hours from a large one, but says **nothing** / about calm-to-calm. Instances verified value by value: C161/C162 (15 h apart, |
| JQ-CANTEEN-8.md | scripts/06_find_moments.py 63–65 | R5  TACTICS 2 puts no minimum distance between two *calm* moments. None is / imposed here. How many calm pairs ended up closer than 48 h is measured and / written into the manifest. |
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
| JQ-R04-CONTENT.md | TACTICS.md 71–71 | Numbers are rounded and the card is kept short. The AI never sees raw seconds. |
| JQ-R04-CONTENT.md | TACTICS.md 101–104 | - **What is hidden:** / - the coin name / - the date and time / - the price itself (converted to a number starting from 100) |
| JQ-R04-CONTENT.md | canteen/2026-09-19-sofia.md 114–120 | Trigger  : In the card's Before table (rows h-24 .. h-1, 24 rows), at least one / row whose hourly close-to-close change is /5.00%/ or more. / Read it from the `chg%` column. If an exam card does not print / `chg%`, compute it from the `close` column as / close(h)/close(h-1) - 1 — a percentage change is unchanged by / TACTICS 6's rebasing of price to a number starting from 100, so the / trigger is computable on a card whose price is hidden. |
| JQ-R04-CONTENT.md | canteen/2026-09-19-sofia.md 221–225 | Rule no: B-2 · the `taker L/S` column may not be read / Trigger  : always — the column is excluded from every score. / Direction: none — blocker on the data. / Exit     : n/a. It lifts only when somebody checks the column against the / 5-minute taker archive and states a trade-count floor. |
| JQ-R04-CONTENT.md | canteen/2026-09-19-sofia.md 667–671 | 4. **The trade-count floor under `taker L/S`.** No watcher names a number. Amara / round-2 E4 calls it "the single most testable data-integrity claim in the / three sets of notes". **How determined:** by Mateo/Nadia against the 5-minute / taker archive, as a data-cleaning decision, not a trading decision. Until / then B-2 excludes the column outright, which needs no number. |
| JQ-R04-DATE.md | RULES.md 41–41 | 9. In the exam the coin name and the date are hidden. The answer key is sealed |
| JQ-R04-DATE.md | RULES.md 43–44 | 10. An agent sitting the exam cannot use tools and cannot read files. A paper / where tool use is observed is void. |
| JQ-R04-DATE.md | TACTICS.md 55–62 | **What is on the card** (where data exists): / - price, volume, trade count, taker buy/sell pressure / - open interest, long/short ratios (5-minute archive) / - funding rate, payment interval and its changes / - order book depth (only the moment days are downloaded; the files are large) / - Binance and Korean exchange announcements (listing, delisting, warning) / - bitcoin and ethereum, over the same hours / - US release calendar (inflation, employment, rate decision) |
| JQ-R04-DATE.md | TACTICS.md 101–107 | - **What is hidden:** / - the coin name / - the date and time / - the price itself (converted to a number starting from 100) / - the coin name inside announcements / - the Wikipedia number itself (given as a ratio to the coin's own average) / - the date in the release calendar |
| JQ-R04-GATE.md | RULES.md 41–41 | 9. In the exam the coin name and the date are hidden. The answer key is sealed |
| JQ-R04-GATE.md | RULES.md 51–52 | 12. The chance line is not invented. The answers are shuffled 1,000 times, and / the real result must fall inside the best 1%. |
| JQ-R04-GATE.md | RULES.md 34–35 | 6. The rule is written first, the result is opened second. A rule is not changed / after looking at a result. If it is changed it counts as a new rule, carries |
| JQ-R04-GATE.md | TACTICS.md 101–107 | - **What is hidden:** / - the coin name / - the date and time / - the price itself (converted to a number starting from 100) / - the coin name inside announcements / - the Wikipedia number itself (given as a ratio to the coin's own average) / - the date in the release calendar |
| JQ-R04-GATE.md | RULES.md 53–54 | 13. Moments occurring in several coins in the same hour count as a single event. / If the whole market moved together, that is one event. |

