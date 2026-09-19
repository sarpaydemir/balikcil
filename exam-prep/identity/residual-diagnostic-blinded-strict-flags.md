# Residual diagnostic — card set `blinded-strict-flags`

Written by `scripts/18_residual_diagnostic.py`. It asks one question: how much of the leftover nearest-neighbour signal on a blinded card set is simply two cards of the same coin covering overlapping clock hours, which no blinding can separate because they are near-copies of each other.

| field | value |
|---|---|
| run number (RULES 29) | `ca8b0bc394468298` |
| written at (system clock, UTC, RULES 23) | 2026-09-19T14:13:12Z |
| cards | 306 |
| feature set | the audit's `ALL-removable` |
| shuffles (RULES 12) | 1000 |
| seed | `20260913` |
| `scripts/18_residual_diagnostic.py` SHA-256 | `52ebb0a115656fad7341ec22db1d98859b48a09788e1c306118ff472ecda2015` |

| time-overlapping cards forbidden as neighbours | features | nearest-neighbour same-coin | chance line (best 1%) | mean of the null | beats chance |
|---|---|---|---|---|---|
| no | 23 | 0.1895 | 0.1667 | 0.1194 | YES |
| yes | 23 | 0.1732 | 0.1699 | 0.1197 | YES |

