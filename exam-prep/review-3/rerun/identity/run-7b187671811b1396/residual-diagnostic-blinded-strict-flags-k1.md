# Residual diagnostic — card set `blinded-strict-flags-k1`

Written by `scripts/18_residual_diagnostic.py`. It asks one question: how much of the leftover nearest-neighbour signal on a blinded card set is simply two cards of the same coin covering overlapping clock hours, which no blinding can separate because they are near-copies of each other.

| field | value |
|---|---|
| run number (RULES 29) | `7b187671811b1396` |
| written at (system clock, UTC, RULES 23) | 2026-10-01T20:59:27Z |
| cards | 306 |
| feature set | the audit's `ALL-removable` (forced families left out: `volatility-frozen`, `funding-line`, `p7-shape`, `repeat-chg`) |
| shuffles (RULES 12) | 1000 |
| seed | `20260913` |
| `scripts/18_residual_diagnostic.py` SHA-256 | `9db9f7b06cb773fe269603882576f01a89af8ac092ed01773cbc63cbf4acb429` |

| time-overlapping cards forbidden as neighbours | features | nearest-neighbour same-coin | chance line (best 1%) | mean of the null | beats chance |
|---|---|---|---|---|---|
| no | 44 | 0.4346 | 0.1765 | 0.1198 | YES |
| yes | 44 | 0.4248 | 0.1765 | 0.1200 | YES |

