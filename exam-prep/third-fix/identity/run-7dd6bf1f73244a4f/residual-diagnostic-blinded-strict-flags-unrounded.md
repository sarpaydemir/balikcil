# Residual diagnostic — card set `blinded-strict-flags-unrounded`

Written by `scripts/18_residual_diagnostic.py`. It asks one question: how much of the leftover nearest-neighbour signal on a blinded card set is simply two cards of the same coin covering overlapping clock hours, which no blinding can separate because they are near-copies of each other.

| field | value |
|---|---|
| run number (RULES 29) | `7dd6bf1f73244a4f` |
| written at (system clock, UTC, RULES 23) | 2026-10-01T20:25:45Z |
| cards | 306 |
| feature set | the audit's `ALL-removable` (forced families left out: `volatility-frozen`, `funding-line`, `p7-shape`, `repeat-chg`) |
| shuffles (RULES 12) | 1000 |
| seed | `20260913` |
| `scripts/18_residual_diagnostic.py` SHA-256 | `9db9f7b06cb773fe269603882576f01a89af8ac092ed01773cbc63cbf4acb429` |

| time-overlapping cards forbidden as neighbours | features | nearest-neighbour same-coin | chance line (best 1%) | mean of the null | beats chance |
|---|---|---|---|---|---|
| no | 26 | 0.2386 | 0.1765 | 0.1201 | YES |
| yes | 26 | 0.2255 | 0.1765 | 0.1203 | YES |

