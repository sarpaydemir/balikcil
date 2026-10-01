# Review checks — run `28b29921e160d204`

Written by `scripts/24_review_checks.py` against the instruments as reviewed (commit `7735d08`). Every number below is counted by that script; the review's own figure is quoted next to it where the review gives one.

| field | value |
|---|---|
| run number (RULES 29) | `28b29921e160d204` |
| full input fingerprint | `28b29921e160d204c3e9b501a1c56691be42c528d22b4e8d0947ce26ae30b80d` |
| written at (system clock, UTC, RULES 23) | 2026-10-01T19:44:20Z |
| free disk space at start (bytes) | 12426891264 |
| `scripts/24_review_checks.py` SHA-256 | `de072d80820344a7ad6f73980fb99cfb0e0c5d129e6f8682bc6b06e50909f14c` |

## C-1 · REVIEW §3.1 — level-carrying families that beat a chance line

| variant | family | nn | line | beats | pair AUC | line | beats |
|---|---|---|---|---|---|---|---|
| `ratio` | `volume-level` | 0.186275 | 0.179739 | YES | 0.528896 | 0.512822 | YES |
| `ratio` | `trades-level` | 0.212418 | 0.176471 | YES | 0.52623 | 0.513451 | YES |
| `ratio` | `openint-level` | 0.127451 | 0.133987 | no | 0.505179 | 0.503379 | YES |
| `ratio` | `taker-buy` | 0.166667 | 0.179739 | no | 0.563111 | 0.513622 | YES |
| `rank` | `volume-level` | 0.183007 | 0.179739 | YES | 0.527862 | 0.512206 | YES |
| `rank` | `trades-level` | 0.196078 | 0.179739 | YES | 0.529441 | 0.513128 | YES |
| `rank` | `openint-level` | 0.130719 | 0.153595 | no | 0.513841 | 0.511796 | YES |
| `rank` | `taker-buy` | 0.166667 | 0.179739 | no | 0.563111 | 0.513622 | YES |
| `strict` | `trades-level` | 0.130719 | 0.166667 | no | 0.529516 | 0.513496 | YES |
| `strict` | `openint-level` | 0.130719 | 0.153595 | no | 0.513841 | 0.511796 | YES |
| `strict-flags` | `trades-level` | 0.130719 | 0.166667 | no | 0.529516 | 0.513496 | YES |
| `strict-flags` | `openint-level` | 0.130719 | 0.153595 | no | 0.513841 | 0.511796 | YES |

## C-2 · REVIEW §3.2 — the `close` repeat-structure probe

Review figures (`strict-flags`): `closeset` nn 0.1601 / line 0.1667, AUC 0.5421 / line 0.5107; `volatility-frozen`+`closeset` nn 0.1830 / 0.1732, AUC 0.5569 / 0.5136; `ALL-removable`+`closeset` nn 0.2451 / 0.1732, AUC 0.5172 / 0.5141.

| variant | feature set | features | nn | line | pair AUC | line |
|---|---|---|---|---|---|---|
| `ratio` | `volatility-frozen` | 3 | 0.160131 | 0.176471 | 0.542629 | 0.513267 |
| `ratio` | `closeset` | 2 | 0.160131 | 0.166667 | 0.542144 | 0.510666 |
| `ratio` | `volatility-frozen+closeset` | 5 | 0.183007 | 0.173203 | 0.556899 | 0.513583 |
| `ratio` | `ALL-removable` | 19 | 0.212418 | 0.169935 | 0.572619 | 0.513541 |
| `ratio` | `ALL-removable+closeset` | 21 | 0.245098 | 0.173203 | 0.576157 | 0.513879 |
| `rank` | `volatility-frozen` | 3 | 0.160131 | 0.176471 | 0.542629 | 0.513267 |
| `rank` | `closeset` | 2 | 0.160131 | 0.166667 | 0.542144 | 0.510666 |
| `rank` | `volatility-frozen+closeset` | 5 | 0.183007 | 0.173203 | 0.556899 | 0.513583 |
| `rank` | `ALL-removable` | 26 | 0.232026 | 0.169935 | 0.520307 | 0.513273 |
| `rank` | `ALL-removable+closeset` | 28 | 0.264706 | 0.173203 | 0.528236 | 0.513224 |
| `strict` | `volatility-frozen` | 3 | 0.160131 | 0.176471 | 0.542629 | 0.513267 |
| `strict` | `closeset` | 2 | 0.160131 | 0.166667 | 0.542144 | 0.510666 |
| `strict` | `volatility-frozen+closeset` | 5 | 0.183007 | 0.173203 | 0.556899 | 0.513583 |
| `strict` | `ALL-removable` | 23 | 0.189542 | 0.166667 | 0.504928 | 0.513011 |
| `strict` | `ALL-removable+closeset` | 25 | 0.245098 | 0.173203 | 0.517172 | 0.514068 |
| `strict-flags` | `volatility-frozen` | 3 | 0.160131 | 0.176471 | 0.542629 | 0.513267 |
| `strict-flags` | `closeset` | 2 | 0.160131 | 0.166667 | 0.542144 | 0.510666 |
| `strict-flags` | `volatility-frozen+closeset` | 5 | 0.183007 | 0.173203 | 0.556899 | 0.513583 |
| `strict-flags` | `ALL-removable` | 23 | 0.189542 | 0.166667 | 0.504928 | 0.513011 |
| `strict-flags` | `ALL-removable+closeset` | 25 | 0.245098 | 0.173203 | 0.517172 | 0.514068 |

## C-3 · REVIEW §3.3 — the `ALL-removable` gate rows

| variant | nn | line | beats | pair AUC | line | beats |
|---|---|---|---|---|---|---|
| `ratio` | 0.212418 | 0.169935 | YES | 0.572619 | 0.513541 | YES |
| `rank` | 0.232026 | 0.169935 | YES | 0.520307 | 0.513273 | YES |
| `strict` | 0.189542 | 0.166667 | YES | 0.504928 | 0.513011 | no |
| `strict-flags` | 0.189542 | 0.166667 | YES | 0.504928 | 0.513011 | no |

## C-4 · REVIEW §3.4 — release names (`strict-flags`)

| quantity | this script | review |
|---|---|---|
| cards printing at least one release name | 100 of 306 | 100 of 306 |
| distinct release names | 30 | 30 |
| names on exactly one calendar day | 11 | 11 |
| cards carrying such a name | 13 | 13 |
| exact-match linkage: truly overlapping pairs detected | 8 of 495 | 8 of 495 |
| exact-match linkage: false positives | 15 | 15 |

Names on exactly one calendar day: *Census of Fatal Occupational Injuries*; *Employer Costs for Employee Compensation*; *Employer-Reported Workplace Injuries and Illnesses (Annual)*; *Labor Force Characteristics of Foreign-born Workers*; *Labor Market Experience, Education, Partner Status, and Health for those Born YYYY-YYYY for Biennial*; *Productivity and Costs by Industry: Wholesale Trade and Retail Trade*; *Productivity by State*; *Summer Youth Labor Force*; *Total Factor Productivity*; *Usual Weekly Earnings of Wage and Salary Workers*; *Work Experience of the Population (Annual)*.

## C-5 · REVIEW §3.5(a) — B-4 depth runs by window

Cards with a run of 3+ identical values in a depth column inside the before window: C018 C019 C041 C058 C059 (5).

Cards whose only such run is in the after window: C017 C042 C060 C099 C139 C154 C183 C287.

| card | before bid | before ask | after bid | after ask |
|---|---|---|---|---|
| C017 | 1 | 1 | 5 | 13 |
| C018 | 24 | 1 | 24 | 2 |
| C019 | 4 | 2 | 1 | 2 |
| C041 | 3 | 3 | 1 | 1 |
| C058 | 5 | 1 | 22 | 1 |
| C059 | 24 | 1 | 24 | 1 |

Cards with an `open int` zero inside the before window: C002 C259 C263 C264.

## C-6 · REVIEW §3.5(b) — the "two-fifths" figure

Excess over the null mean: 0.070098 → 0.053517, a reduction of 23.7%. Excess over the 1% line: 0.022875 → 0.003268, a reduction of 85.7%. Review: 23.7% and 85.7%.

## C-7 · REVIEW §4.2 — the reviewed block shuffle

Events `[[c0,c1,c2],[c3],[c4,c5]]`, seed `20260913`. Draws in which at least one event read its answers from more than one source event: **166 of 200** (review: 175 of 200, seed not stated). Event-constant vectors still event-constant after permutation: **157 of 1000** (review: 138 of 1,000; a true block permutation gives all).

## C-8 · REVIEW §4.4 — same-coin events per configuration

| configuration | events | events holding 2+ cards of one coin | largest same-coin count |
|---|---|---|---|
| `card-span/component/any` | 58 | 25 | 5 |
| `card-span/component/cross-coin` | 62 | 26 | 4 |
| `card-span/greedy-clique/any` | 116 | 13 | 3 |
| `card-span/greedy-clique/cross-coin` | 125 | 0 | 1 |
| `move-window/component/any` | 131 | 15 | 2 |
| `move-window/component/cross-coin` | 136 | 10 | 2 |
| `move-window/greedy-clique/any` | 161 | 10 | 2 |
| `move-window/greedy-clique/cross-coin` | 168 | 0 | 1 |
| `none/none/none` | 306 | 0 | 1 |
| `start-hour/component/any` | 289 | 0 | 1 |
| `start-hour/component/cross-coin` | 289 | 0 | 1 |

## C-9 · REVIEW §2.3 — combined blinded-card fingerprints

Recipe: SHA-256 over the concatenation, in card-id order, of `<id>:<SHA-256 of the card file>\n`.

| variant | combined SHA-256 |
|---|---|
| `ratio` | `021bdfbbb08bad12080090ffe02287246d143e1a0a9c617120fccaea9fb604e2` |
| `rank` | `00a428658914e43da1e1372c08844488dd6bcec69bfa192a280668efdcbc3a14` |
| `strict` | `fb9b83059a6682098a6de41848e8ac9d89ebb207719986b07333fa8346d653f4` |
| `strict-flags` | `49dc65c3af35a57ba7acf77bb1696a94272b7f2451e7b7e2fe05a2dcb631e8f6` |

## C-10 · REVIEW §4.3 — the identity partition

The reviewed `chance_line()` accepted `events=[[c] for c in id_order]` in both modes. Boundaries on a synthetic coin-flip answer vector (seed `20260913`): block 0.558824, representative 0.571895; a plain card-level shuffle with the same seed: 0.571895.

