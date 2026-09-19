# Blinding manifest — card set `strict-flags`

Written by `scripts/17_blind_cards.py`. It records what was done to every field and counts what survived. It draws no conclusion and reads nothing under `exam/`.

| field | value |
|---|---|
| run number (RULES 29) | `10405ae115941d40` |
| full input fingerprint | `10405ae115941d409318881b40a72cdde85dcf8646f4d28993bb76d7163efac5` |
| written at (system clock, UTC, RULES 23) | 2026-09-19T14:18:54Z |
| free disk space at start (bytes) | 16111312896 |
| source cards | `cards`, 306 cards |
| configuration | `levels=rank;btceth=drop;funding=flags;takerbuy=rank;p7=no-scale;ratio_dp=3` |
| card-number shuffle seed | `20260913` (TACTICS 1 draw number) |
| `scripts/17_blind_cards.py` SHA-256 | `ee064204016f110d18ceb4feda2c6f6f8c3c78ce97a0cf7d3f34e225f86f9515` |

## What was done to each field

| field | before | after |
|---|---|---|
| coin name | printed in the header | removed (TACTICS 6) |
| start hour | printed in the header | removed (TACTICS 6) |
| card number | `C###`, in moment order | `B###`, shuffled with the draw seed, so the number carries no time |
| After section | printed | removed (TACTICS 6) |
| `close` | the coin's price | rebased so h-24 = 100.00 (TACTICS 6) |
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

## Fingerprints

| file | SHA-256 |
|---|---|
| `exam-prep/blind-proof/strict-flags/truth-strict-flags.csv` | `02546086447ddf4bbdcb0e224e1b672a5fa7986dfabe2de0174b5063190a4e13` |
| the 306 blinded cards, combined | `49dc65c3af35a57ba7acf77bb1696a94272b7f2451e7b7e2fe05a2dcb631e8f6` |

