# Blinding manifest — card set `strict-flags-k1`

Written by `scripts/17_blind_cards.py`. It records what was done to every field and counts what survived. It draws no conclusion and reads nothing under `exam/`.

| field | value |
|---|---|
| run number (RULES 29) | `2a53d1de158a2b2c` |
| full input fingerprint | `2a53d1de158a2b2c829567192310e2b9ee2658cbacb30ceda740f4af2420b198` |
| written at (system clock, UTC, RULES 23) | 2026-10-01T20:48:43Z |
| free disk space at start (bytes) | 12408029184 |
| source cards | `cards`, 306 cards |
| configuration | `levels=rank;btceth=drop;funding=flags;takerbuy=rank;p7=no-scale;ratio_dp=3;close_dp=no-new-ties->3` |
| card-number shuffle seed | `20260913` (TACTICS 1 draw number) |
| `scripts/17_blind_cards.py` SHA-256 | `a37bd20fc4b0e1c2ddfb89a10caec11529363c06fb2d19550f95f41471379548` |

## What was done to each field

| field | before | after |
|---|---|---|
| coin name | printed in the header | removed (TACTICS 6) |
| start hour | printed in the header | removed (TACTICS 6) |
| card number | `C###`, in moment order | `B###`, shuffled with the draw seed, so the number carries no time |
| After section | printed | removed (TACTICS 6) |
| `close` | the coin's price | rebased so h-24 = 100.000, 3 decimals (TACTICS 6; `--close-dp no-new-ties`) |
| `chg%` | hourly percentage change | **unchanged** — the frozen canteen book's S-1 reads it at 5.00% absolute (RULES 6) |
| `quote vol` | the coin's own level | rank among the card's 24 rows, exact zeros kept |
| `trades` | the coin's own level | rank among the card's 24 rows, exact zeros kept |
| `open int` | the coin's own level | rank among the card's 24 rows, exact zeros kept |
| `L/S acct` | the coin's own level | rank among the card's 24 rows, exact zeros kept |
| `top L/S pos` | the coin's own level | rank among the card's 24 rows, exact zeros kept |
| `taker L/S` | the coin's own level | rank among the card's 24 rows, exact zeros kept |
| `depth -1%` | the coin's own level | rank among the card's 24 rows, exact zeros kept |
| `depth +1%` | the coin's own level | rank among the card's 24 rows, exact zeros kept |
| `taker buy%` | a share, 0–100 | rank among the card's 24 rows |
| `BTC`, `ETH` | the market's hourly change | removed |
| previous-7-day volume and trades | the coin's own level | not printed |
| funding line | count, every rate, the interval | `flags` rendering |
| US releases | release names carrying calendar dates | dates stripped, relative offsets kept (TACTICS 6); every card checked and the script stops if a year, a month name or a quarter survives |
| Wikipedia page views | present on some coins only | removed |
| prediction market | names the instrument in words | removed |
| exchange announcements | a per-card reason string | one canonical sentence on every card |

## What the frozen canteen book needs, and whether it survived

| quantity | count |
|---|---|
| B-3 · cards printing an open-interest zero, blinded | 4 |
| B-3 · cards printing an open-interest zero, raw | 4 |
| B-4 · cards with a depth run of >= 3, blinded (3 dp) | 5 |
| B-4 · cards with a depth run of >= 3, raw | 5 |
| S-1 · cards whose largest |chg%| is unchanged | 306 |
| cards_written | 306 |

The script stops rather than writing a card if a B-3 zero is lost, if the largest `|chg%|` moves, or if the rounding fabricates a B-4 depth run that the raw card did not have.

## Choosing the number of decimals by measurement

| decimals | cards where the rounding fabricates a run of 3 identical depth values | 
|---|---|
| 2 | 31 |
| 3 | 0 |
| 4 | 0 |

`RATIO_DP` is set to 3.

## The decimals of the rebased `close`

| decimals | cards on which two hours print the same rebased `close` although the raw card printed two different values |
|---|---|
| 2 | 36 |
| 3 | 0 |

`--close-dp no-new-ties` -> 3 decimals.

## Fingerprints

| file | SHA-256 |
|---|---|
| `exam-prep/review-3/rerun/blind/strict-flags-k1/truth-strict-flags-k1.csv` | `02546086447ddf4bbdcb0e224e1b672a5fa7986dfabe2de0174b5063190a4e13` |
| the 306 blinded cards, combined | `ffda9e30f02724a2958e4ec604a8d66c205d804f3f9082886f7ee903d44eb492` |

