# Third-fix checks — run `212dd7ecffc51263`

Written by `scripts/26_third_fix_checks.py`. Every number below is counted by that script.

| field | value |
|---|---|
| run number (RULES 29) | `212dd7ecffc51263` |
| full input fingerprint | `212dd7ecffc512639e2794fe88045a4386ec830787435dadfc4cc1d4dbfcb1b4` |
| written at (system clock, UTC, RULES 23) | 2026-10-01T20:59:30Z |
| free disk space at start (bytes) | 12405866496 |
| `scripts/26_third_fix_checks.py` SHA-256 | `b68ef1be773e9829d9e803e7420d722c1cf3836a1ef5a674cb6df64db36aa796` |
| `scripts/15_event_collapse.py` SHA-256 | `e59cecb7c8e455f5cd8625130b962ba343bc168f53699667e5ac132ddbed2fe6` |

## G-1 · what `chance_line()` accepts and refuses (third-fix engine)

Fingerprint of the true moments (`moments_fingerprint()`): `7c900a10b379b85edb0eed000d698997cdc87e4733f7f3da25c9ed3080eb14f6`.

| attempt | result | detail |
|---|---|---|
| true moments, card-span/component/any, key of the true moments | accepted | config card-span/component/any, 58 events, boundary 0.558824, key_check matched |
| identity_map() of the true moments, key of the true moments | accepted | config none/none/none, 306 events, boundary 0.558824, key_check matched |
| REVIEW-2 p4 attempt 1: start hours moved 1,000 h apart, key of the true moments | ValueError | the event map was not made from the moments of the answer key: its moments fingerprint c67e773424f913ba is not the key's '7c900a10b379b85e' |
| REVIEW-2 p4 attempt 1b: one card's start hour moved, key of the true moments | ValueError | the event map was not made from the moments of the answer key: its moments fingerprint a5ef644c7d4cbfc4 is not the key's '7c900a10b379b85e' |
| key omitted | TypeError | chance_line() missing 1 required keyword-only argument: 'key_moments_sha256' |
| key given as None | ValueError | the event map was not made from the moments of the answer key: its moments fingerprint 7c900a10b379b85e is not the key's 'None' |
| LIMIT: forged map passed with its OWN moments fingerprint (what a judge who does not read the key could do) | accepted | config card-span/component/any, 298 events, boundary 0.571895, key_check matched |

## G-2 · K-9, the representative column computed exactly

Exact null (hypergeometric), the same synthetic answers and representatives as `15_event_collapse.py`. `reported` is the simulated value in `exam-prep/collapse/run-756cf4ea156d92c3/shuffle-calibration.csv`; `2.5% – 97.5%` is the spread of the statistic the instrument reports (the 10th largest of 1000 draws), a description, not a threshold.

| configuration | n | representative, reported | exact 1% point | spread of the reported statistic, 2.5% – 97.5% | card-level (iid / event-constant) | block (iid / event-constant) |
|---|---|---|---|---|---|---|
| `none/none/none` | 306 | 0.5654 | 0.5654 | 0.5588 – 0.5719 | 0.5719 / 0.5719 | 0.5588 / 0.5588 |
| `start-hour/component/any` | 289 | 0.5744 | 0.5675 | 0.5606 – 0.5744 | 0.5719 / 0.5654 | 0.5523 / 0.5588 |
| `start-hour/component/cross-coin` | 289 | 0.5744 | 0.5675 | 0.5606 – 0.5744 | 0.5719 / 0.5654 | 0.5523 / 0.5588 |
| `move-window/component/any` | 131 | 0.6031 | 0.6031 | 0.5878 – 0.6183 | 0.5719 / 0.5621 | 0.5654 / 0.5948 |
| `move-window/component/cross-coin` | 136 | 0.5882 | 0.6029 | 0.5882 – 0.6176 | 0.5719 / 0.5654 | 0.5654 / 0.5980 |
| `move-window/greedy-clique/any` | 161 | 0.5901 | 0.5901 | 0.5776 – 0.6025 | 0.5719 / 0.5588 | 0.5654 / 0.5980 |
| `move-window/greedy-clique/cross-coin` | 168 | 0.5893 | 0.5893 | 0.5774 – 0.6012 | 0.5719 / 0.5621 | 0.5588 / 0.5752 |
| `card-span/component/any` | 58 | 0.6552 | 0.6552 | 0.6552 – 0.6552 | 0.5719 / 0.5686 | 0.5588 / 0.5621 |
| `card-span/component/cross-coin` | 62 | 0.6613 | 0.6613 | 0.6290 – 0.6613 | 0.5719 / 0.5654 | 0.5588 / 0.5523 |
| `card-span/greedy-clique/any` | 116 | 0.6121 | 0.6121 | 0.5948 – 0.6293 | 0.5719 / 0.5621 | 0.5523 / 0.6013 |
| `card-span/greedy-clique/cross-coin` | 125 | 0.6000 | 0.6000 | 0.6000 – 0.6160 | 0.5719 / 0.5654 | 0.5458 / 0.5719 |

Un-collapsed card-level line (n = 306): exact 1% point 0.5654; the reported statistic falls between 0.5588 and 0.5719 (2.5% – 97.5%). The support moves in steps of 0.006536; the probability that two independent reported lines differ by at least 1, 2, 3, 4 steps is 0.5155, 0.0582, 0.0018, 0.0.

## G-3 · K-8, overlapping card pairs

Source `data/overlap/pairs.csv` (run `12ce59e2902a0034`), 495 pairs whose 48-hour card spans share at least one clock hour (the manifest's definition). `before windows` = the subset whose 24-hour before windows share an hour (start gap <= 23 h).

| kinds · coins | card spans share an hour | before windows share an hour |
|---|---|---|
| calm+calm · different coins | 114 | 53 |
| calm+calm · same coin | 21 | 10 |
| calm+large · different coins | 206 | 97 |
| large+large · different coins | 154 | 101 |

Same-coin pairs:

| pair | kinds | start gap (h) | shared hours | before windows share an hour |
|---|---|---|---|---|
| C010/C011 | calm+calm | 14 | 34 | yes |
| C039/C040 | calm+calm | 20 | 28 | yes |
| C040/C041 | calm+calm | 44 | 4 | no |
| C050/C051 | calm+calm | 7 | 41 | yes |
| C050/C052 | calm+calm | 38 | 10 | no |
| C051/C052 | calm+calm | 31 | 17 | no |
| C071/C072 | calm+calm | 28 | 20 | no |
| C079/C080 | calm+calm | 36 | 12 | no |
| C084/C085 | calm+calm | 33 | 15 | no |
| C092/C093 | calm+calm | 4 | 44 | yes |
| C161/C162 | calm+calm | 15 | 33 | yes |
| C162/C163 | calm+calm | 43 | 5 | no |
| C163/C164 | calm+calm | 33 | 15 | no |
| C176/C177 | calm+calm | 3 | 45 | yes |
| C204/C205 | calm+calm | 45 | 3 | no |
| C205/C206 | calm+calm | 35 | 13 | no |
| C210/C211 | calm+calm | 11 | 37 | yes |
| C224/C225 | calm+calm | 33 | 15 | no |
| C291/C292 | calm+calm | 15 | 33 | yes |
| C293/C294 | calm+calm | 18 | 30 | yes |
| C297/C298 | calm+calm | 3 | 45 | yes |

`data/moments/moment-manifest.md` records 20 consecutive same-coin calm pairs closer than 48 h (it counts neighbours in time only, so a run of three close calm moments counts 2 there and 3 pairs here).

## G-4 · the facts JQ-B1 rests on

| fact | value |
|---|---|
| `canteen/2026-09-19-sofia.md` line 187 | `Trigger  : the contract is AVGOUSDT or NOKUSDT.` |
| contracts the frozen trigger names | AVGOUSDT, NOKUSDT |
| each named contract is in `data/draw/observation-coins.txt` | {'AVGOUSDT': True, 'NOKUSDT': True} |
| `data/draw/draw-manifest.md` records `"disjoint": true` | True |
| `data/draw/draw-manifest.md` records `"observation_x_exam_overlap": []` | True |

Nothing under `exam/` was read. Whether the exam cards are in fact built from the drawn exam list is for the exam-building run to confirm (`exam-prep/HANDED-FORWARD.md`).

## G-5 · greedy-clique under cross-coin: which moment of a coin is kept

The engine keeps, in the chosen window, the earliest moment of each coin (by start hour, then card number). The same loop with only that choice reversed (keep the latest):

| definition | copy equals engine | events, keep earliest | events, keep latest | events in one partition only | events holding both kinds, earliest / latest |
|---|---|---|---|---|---|
| `move-window` | True | 168 | 168 | 12 | 50 / 50 |
| `card-span` | True | 125 | 125 | 30 | 60 / 60 |

## Inputs

| file | SHA-256 |
|---|---|
| `canteen/2026-09-19-sofia.md` | `650daccc526353c4418509f98a6147fd678de5808d139cfc9273dcaef92662de` |
| `data/draw/draw-manifest.md` | `b4fc76a6436a3ce9bc76a9598d0aec2e8920b54f046badd58a83ac76230e8e7c` |
| `data/draw/observation-coins.txt` | `336f2cf885319ae0fcfe2c3020c7ae20f7b7dff1a826230d16b8bcd7c4b81d08` |
| `data/moments/moment-manifest.md` | `b50937ab7655d5d61be5c21f8e9637997bf5e4132c6b00fb039a65e9b866c0b4` |
| `data/overlap/pairs.csv` | `ff77674cf36644e333afdac98e2c6d7e4f83961e34745d7e329259b06baf301d` |
| `exam-prep/collapse/run-756cf4ea156d92c3/shuffle-calibration.csv` | `0c4b27f9556086644ff5ad9137322a06854f64b78daf9bf1babebd73115b5cd7` |

