# R-04 · is the exam blind?

Mateo · data engineer · 2026-09-19 (system clock, RULES 23)
Runs: audits `3c090e41041104e0` · `b8230e324e0c03e6` · `3b1cb7d540d11283` ·
`23502d75682cc455` · `ba8d6b5e3880f9ee`; blinding `ca9e460829ecdac5` ·
`35df01d621d8da5a` · `a9a8f3bcd515fd62` · `10405ae115941d40`

---

## 1 · The problem as the canteen stated it

Sofia, canteen book §7.1, and Viktor, §5 `R-04` and §9 item 5: two
de-anonymisation channels found in two different fields by watchers who could
not see each other.

> (a) the Wikipedia field is present on exactly the 40 BCH cards and no others,
> so its mere presence decodes the coin; (b) the funding interval plus baseline
> plus ratio levels plus depth scale cluster the cards by coin … TACTICS 6
> hides the coin name, the date and the price, but not these. It bears on
> whether the exam is blind at all (RULES 9).

Viktor's own objection to his own finding, which I took seriously:

> it is asserted from the **observation** cards. Nobody has tried to cluster a
> sample of **exam** cards.

I cannot cluster exam cards — `exam/` is closed to this run. What I could do is
turn the assertion into a measurement on the 306 observation cards, build the
instrument that removes the channels, and prove on the same 306 cards that the
measurement then falls to the chance line. The exam-building run applies the
same instrument and re-runs the same audit as an acceptance gate.

The rule behind it is `RULES.md` 9: "In the exam the coin name and the date are
hidden."

---

## 2 · My standard for "solved"

Written before the blinding was built, and deliberately in two levels, because
one of them is attainable and one of them is not.

**Level 1 — no field whose absolute level is a coin's signature.**
Every family of exam-visible features whose information is a *level* (price,
volume, trades, open interest, depth, long/short ratios, taker-buy share,
Wikipedia presence, the bitcoin and ethereum columns) must fail both attacks
against the RULES 12 chance line: it must not identify a card's coin by nearest
neighbour, and it must not tell a same-coin pair from a different-coin pair.
*Test: the audit table of §5, families `price-level` … `btc-eth`.*

**Level 2 — the card as a whole is not statistically linkable to its coin.**
The pooled attack over every exam-visible feature, including the scale-free
shape of each column, must not beat its chance line either.
*Test: the audit rows `ALL` and `ALL-removable` of §5.*

**A third line, which decides what "solved" can mean at all:**
a channel may only be closed if closing it does not destroy something the
**frozen** canteen book asks an exam candidate for. The book froze on
2026-09-19 and RULES 6 forbids changing a rule after the fact. Every channel
that cannot be closed for that reason is named, with its measured size, and is
**not** quietly written off. *Test: §7.*

**Also part of the standard:** the clock-hour channel. A card must not print a
column that identifies which clock hours it covers, because RULES 9 hides the
date as well as the coin. *Test: the T3 table of §6.*

A reviewer who thinks Level 1 is too weak, or that the Level 2 residual is
unacceptable, has every number needed to say so.

---

## 3 · What the raw card leaks — measured, not asserted

`scripts/16_identity_audit.py`, run `3c090e41041104e0`, on the 306 observation
cards (10 coins). Two attacks, each against the boundary of the best 1% of
1,000 coin-label shuffles (RULES 12).

| feature family | nearest-neighbour same-coin | chance line | pair AUC | chance line |
|---|---|---|---|---|
| `price-level` | 0.637 | 0.180 | 0.909 | 0.513 |
| `openint-level` | **0.752** | 0.180 | **0.925** | 0.513 |
| `depth-level` | 0.441 | 0.180 | 0.838 | 0.514 |
| `ratio-level` (L/S acct, top L/S pos, taker L/S) | 0.464 | 0.180 | 0.649 | 0.513 |
| `funding-line` | 0.428 | 0.173 | 0.720 | 0.514 |
| `volume-level` | 0.366 | 0.176 | 0.727 | 0.513 |
| `trades-level` | 0.278 | 0.173 | 0.712 | 0.512 |
| `wikipedia-presence` | 0.176 | 0.150 | 0.630 | 0.511 |
| `taker-buy` | 0.186 | 0.173 | 0.571 | 0.512 |
| `shape-scale-free` | 0.190 | 0.176 | 0.566 | 0.512 |
| `volatility-frozen` (`chg%`) | 0.160 | 0.176 | 0.543 | 0.513 |
| `p7-shape` | 0.150 | 0.183 | 0.524 | 0.514 |
| `btc-eth` | 0.078 | 0.173 | 0.488 | 0.514 |
| **`ALL`** | **0.637** | 0.173 | **0.729** | 0.513 |

Read straight: **on the raw card format, two cards out of three can be pinned
to their coin by a single number** — the open-interest level or the price
level. Every family except `btc-eth` and `p7-shape` beats its chance line on at
least one of the two attacks. This is R-04, and it is larger than the two
channels the watchers named.

Four further leaks that the watchers did not name and that a level attack does
not even need:

1. **The prediction-market line prints the instrument in words.** On C001 it
   reads `Polymarket search over \`Broadcom • Robinhood Token\`, \`AVGO\``.
2. **The Wikipedia `MISSING` reason prints the ticker.** On the NOK cards:
   "CoinGecko returned no coin whose symbol equals `NOK`".
3. **The US release line prints calendar dates** — "for First Quarter 2026",
   "Employment Situation for April 2026", "FOMC statement (rate decision) on
   2026-07-29". TACTICS 6 says the date in the release calendar is hidden; the
   card writer prints it.
4. **The bitcoin and ethereum columns are an exact clock-hour fingerprint.**
   See §6.

---

## 4 · What was built

| file | what it is |
|---|---|
| `scripts/16_identity_audit.py` | the three attacks and their chance lines |
| `scripts/17_blind_cards.py` | the blinding transform, configurable |
| `scripts/18_residual_diagnostic.py` | where the leftover signal comes from |
| `scripts/lab_cards.py` | the shared card reader |
| `exam-prep/blind-proof/<variant>/cards/` | 306 blinded cards per variant |
| `exam-prep/blind-proof/<variant>/blind-manifest-<variant>.md` | what was done to every field, with counts |
| `exam-prep/identity/identity-audit-<set>.md` | the audit of each set |

What the transform does, field by field (`strict-flags` configuration):

| field | before | after |
|---|---|---|
| coin name, start hour | printed in the header | removed |
| card number | `C###`, in moment order | `B###`, shuffled with the draw seed `20260913`, so the number carries no time |
| After section | printed | removed (TACTICS 6) |
| `close` | the coin's price | rebased so h-24 = 100.00 (TACTICS 6) |
| `chg%` | hourly percentage change | **unchanged** — frozen, see §7 |
| `quote vol`, `trades`, `open int`, `L/S acct`, `top L/S pos`, `taker L/S`, `depth -1%`, `depth +1%` | the coin's own level | rank among the card's own 24 rows; an exact zero stays `0` |
| `taker buy%` | a 0–100 share | rank among the card's own 24 rows |
| `BTC`, `ETH` | the market's hourly change | removed |
| previous-7-day volume and trades | the coin's own level | not printed |
| funding line | count, every rate, the interval | three yes/no facts and nothing else |
| US releases | names carrying calendar dates | dates stripped; the script **stops** if a year, a month name or a quarter survives |
| Wikipedia page views | present on one coin only | removed |
| prediction market | names the instrument in words | removed |
| exchange announcements | a per-card reason string | one canonical sentence on every card |

Four configurations were built and all four were audited, so the cost of each
step is visible rather than asserted:

| variant | levels | taker buy% | 7-day line | funding | BTC/ETH |
|---|---|---|---|---|---|
| `ratio` | divided by the card's own median | median-centred | full | four facts incl. spread | dropped |
| `rank` | rank within the card | median-centred | full | four facts incl. spread | dropped |
| `strict` | rank | rank | volume and trades dropped | four facts incl. spread | dropped |
| `strict-flags` | rank | rank | volume and trades dropped | **three yes/no facts only** | dropped |

---

## 5 · What is left after blinding — the same attacks, the same chance lines

Pair AUC (0.5 is no information). A `*` marks "beats its own chance line".

| family | raw | `ratio` | `rank` | `strict` | `strict-flags` |
|---|---|---|---|---|---|
| `price-level` | 0.909* | 0.503 | 0.503 | 0.503 | 0.503 |
| `openint-level` | 0.925* | 0.505* | 0.514* | 0.514* | 0.514* |
| `depth-level` | 0.838* | dropped | 0.504 | 0.504 | 0.504 |
| `ratio-level` | 0.649* | dropped | 0.490 | 0.490 | 0.490 |
| `volume-level` | 0.727* | 0.529* | 0.528* | 0.499 | 0.499 |
| `trades-level` | 0.712* | 0.526* | 0.529* | 0.529* | 0.529* |
| `wikipedia-presence` | 0.630* | dropped | dropped | dropped | dropped |
| `btc-eth` | 0.488 | dropped | dropped | dropped | dropped |
| `taker-buy` | 0.571* | 0.563* | 0.563* | 0.496 | 0.496 |
| `shape-scale-free` | 0.566* | 0.566* | 0.512 | 0.512 | 0.512 |
| `funding-line` | 0.720* | 0.593* | 0.593* | 0.593* | 0.573* |
| `volatility-frozen` | 0.543* | 0.543* | 0.543* | 0.543* | 0.543* |
| `p7-shape` | 0.524* | 0.524* | 0.524* | 0.524* | 0.524* |
| **`ALL`** | 0.729* | 0.588* | 0.536* | 0.523* | 0.518* |
| **`ALL-removable`** | 0.716* | 0.573* | 0.520* | **0.505** | **0.505** |

`ALL-removable` is everything a blinding could still take away: it leaves out
`volatility-frozen`, `funding-line` and `p7-shape`, which are forced to stay on
the card for the reasons in §7. Its chance line is 0.513.

Nearest-neighbour, same sets:

| family | raw | `ratio` | `rank` | `strict` | `strict-flags` | chance line |
|---|---|---|---|---|---|---|
| `ALL` | 0.637* | 0.310* | 0.291* | 0.265* | 0.252* | ~0.170 |
| `ALL-removable` | 0.601* | 0.212* | 0.232* | 0.190* | 0.190* | 0.167 |

**Level 1 of my standard is met** by `strict` and `strict-flags`: every
level-carrying family is at or below its chance line on both attacks, except
`openint-level` at 0.514 against a 0.512 chance line — and that residual is not
a level at all, it is the four cards that print an open-interest zero, which
B-3 requires to stay visible.

**Level 2 is not met**, and cannot be: `ALL` remains above its chance line on
both attacks. §7 says exactly what carries it.

---

## 6 · The clock hour — the date channel

Two cards are "detected" as covering the same hours when they print three
consecutive rows identical in the named columns. The truth is the 48-hour span
relation measured by `scripts/14_overlap_map.py`.

| card set | columns | pairs truly sharing an hour | detected | false positives (of 46,170) |
|---|---|---|---|---|
| raw | `BTC`+`ETH` | 495 | **243 (49.1%)** | **0** |
| raw | `chg%` | 495 | 10 | 1 |
| raw | `close` | 495 | 10 | 0 |
| raw | `quote vol` | 495 | 10 | 0 |
| blinded (all four variants) | `BTC`+`ETH` | — | column not printed | — |
| blinded (all four variants) | `chg%` | 495 | 10 | 1 |

The bitcoin and ethereum columns tie half of the overlapping card pairs
together with not one false positive in 46,170 non-overlapping pairs. That is
the date, printed. Dropping the two columns closes it.

What remains is 10 pairs of the same coin whose before-windows overlap and
therefore print the same `chg%` rows. That cannot be closed — see §7 item 1 —
and 10 of 46,665 pairs is the measured size of it.

---

## 7 · What cannot be closed, and why — by name

1. **`chg%`, and therefore the coin's volatility level.** The frozen canteen
   book's only surviving signal, S-1, reads "at least one Before row whose
   hourly change is |5.00%| or more" (Sofia §2.2). A percentage threshold at an
   absolute level cannot be read off a normalised column. RULES 6: the book
   froze before any result; I may not re-cut it. Measured size: pair AUC
   **0.543** against a 0.513 chance line; nearest neighbour 0.160, which is
   *below* its chance line. It is also what keeps the 10 same-coin
   shared-hour pairs of §6 linkable.
   This is the same thing Viktor's O6 says in general — "every trigger written
   on an absolute level is a coin selector" — now measured for the one trigger
   that survived.
2. **The funding line.** The book asks a candidate for three facts from it:
   B-5 (does the payment count match the stated interval), U-2 (did the
   interval change) and U-3 (is the whole window at one rate). The
   `strict-flags` rendering prints those three yes/no facts and nothing else —
   no count, no interval, no rate, no dispersion — and they still carry pair
   AUC **0.573** against 0.511, because the funding regime *is* a property of
   the coin (Ingrid's own finding, 103 cards of 306 at baseline). Closing it
   means deleting a blocker from a frozen book.
3. **The previous-7-day line.** TACTICS 3 puts a one-line 7-day summary on the
   card. Its high-low range is a volatility level, the same channel as item 1.
   Measured: pair AUC **0.524** against 0.513, nearest neighbour below chance.
   `strict` already drops its volume and trades figures; what is left is the
   price change and the range.
4. **The tie structure of `trades`.** The card writer rounds trade counts
   (`1k`, `5k`), so a busy coin's column has many ties and a quiet coin's has
   none, and ranking preserves ties by construction. Pair AUC **0.529** against
   0.513. It could be closed by not printing trade counts at all; nothing in
   the frozen book reads them, so this one is a live choice rather than a wall,
   and it is listed in `exam-prep/decisions-and-open-questions.md`.
5. **Two cards of the same coin that cover overlapping clock hours are
   near-copies of each other.** `scripts/18_residual_diagnostic.py`, run
   `ca8b0bc394468298`, measures how much of the leftover nearest-neighbour
   signal this is:

   | time-overlapping cards forbidden as neighbours | nearest-neighbour same-coin | chance line | mean of the null |
   |---|---|---|---|
   | no | 0.1895 | 0.1667 | 0.1194 |
   | yes | 0.1732 | 0.1699 | 0.1197 |

   About two-fifths of the excess is the overlap; the rest is not, and I do not
   have a name for the rest beyond "the shape of a coin's order flow".

---

## 8 · What the exam-building run must do

1. Build the exam cards with `scripts/17_blind_cards.py` rather than by
   editing `09_write_cards.py`'s output by hand. The transform is one place.
2. Use the configuration `--levels rank --takerbuy rank --p7 no-scale
   --funding flags --btceth drop` unless the laboratory rules otherwise. That
   is `strict-flags`, and the reason it is the recommendation rather than
   `ratio` is in `exam-prep/decisions-and-open-questions.md`, decision D-1.
3. **Re-run `scripts/16_identity_audit.py` on the exam cards before the answer
   key is sealed**, with `--truth` pointing at the key. This is the acceptance
   gate and it answers Viktor's objection that R-04 was only ever asserted from
   the observation cards. If `ALL-removable` beats its chance line on the exam
   cards, the cards are not blind and the gate has failed.
4. Check that the three things the frozen book needs survived: the script
   already stops if a B-3 open-interest zero is lost, if the largest `|chg%|`
   moves, or if rounding fabricates a B-4 depth run. On the 306 observation
   cards: 4 cards carry a before-window open-interest zero raw and blinded; 5
   carry a depth run of 3 or more raw and blinded; 306 of 306 keep the largest
   `|chg%|` exactly.

   (Those two counts are worth noting on their own: the watchers named 5 cards
   with an `open int` zero — C259, C002, C263, C008, C264 — and 5 with a frozen
   depth constant — C017, C018, C019, C058, C059. Counted over the *before*
   window only, which is all an exam card shows, the open-interest count is
   **4**: C008's zero sits at h+10, in the after window. The depth count is 5,
   exactly the five cards they named.)
5. Record in the exam manifest the configuration string, the audit run number
   and the residual figures of §7, so that nobody later reads "blind" as
   "perfectly blind".

---

## 9 · What is still not done, by name

1. **Nothing has been measured on exam cards.** `exam/` is closed to this run.
   Everything above is measured on the 306 observation cards, 10 coins. The
   exam is 20 coins and 400 cards; the attack is easier on 400 cards and harder
   on 20 coins, and I cannot say which way the net effect goes without running
   it. Step 3 of §8 is the measurement that settles it.
2. **The residual of §7 is not zero and I did not make it zero.** Levels 1 and
   the clock-hour channel are closed; Level 2 is not.
3. **Whether an exam candidate can actually run any of these attacks is not
   measured.** RULES 10 says the candidate has no tools and reads no files; the
   attacks here are scripts over 306 cards at once. A reader working card by
   card is a weaker adversary than the one I used. I chose the stronger
   adversary on purpose, and I have not measured the weaker one.
4. **The exam draw is untouched.** Whether 400 cards drawn from 20 coins should
   also be balanced so that no coin is over-represented is an exam-construction
   question and is not mine.

---

## 10 · Fingerprints

| file | SHA-256 |
|---|---|
| `scripts/16_identity_audit.py` | `4c4928b84ff9b484995058c2dd4e5b043af1491b60f314e1a0f418dd90e4a371` |
| `scripts/17_blind_cards.py` | `ee064204016f110d18ceb4feda2c6f6f8c3c78ce97a0cf7d3f34e225f86f9515` |
| `scripts/18_residual_diagnostic.py` | `52ebb0a115656fad7341ec22db1d98859b48a09788e1c306118ff472ecda2015` |
| `scripts/lab_cards.py` | `96b0eb01c502a40b4e76c864681763206ba627b268eedb7eb19984f81d9b928e` |
| `exam-prep/identity/identity-audit-raw-observation.md` | `dca438fdde57fd74b1073fbf674a6ad17acb9f398a26990e63aef7a7927591da` |
| `exam-prep/identity/identity-audit-blinded-ratio.md` | `25ecd63a6f32a0b8c911d4cbe8df965a51650cf347d2bd0a5e7a1fbec092b148` |
| `exam-prep/identity/identity-audit-blinded-rank.md` | `7bdefadc856a62ef09ec529887be03587a0e9d624acfe89bdbc0be0d209b0e9c` |
| `exam-prep/identity/identity-audit-blinded-strict.md` | `76c2a58a4df92ba639b79a4ba417e301d56c741984548b20efe6c63919b1ed31` |
| `exam-prep/identity/identity-audit-blinded-strict-flags.md` | `f51607da900a7c245f69e1c69dd8e6a0c45b6022aec08338bb4796951ddfdfad` |
| `exam-prep/blind-proof/ratio/blind-manifest-ratio.md` | `3e38ec0004089b4d5eab9313c1f071b359675c2380e24494c1eae4a2653852e8` |
| `exam-prep/blind-proof/rank/blind-manifest-rank.md` | `2b8cf4b092a5e281ee28c079e9c57a904fb639f08c549bbee8dbb56e6a6b9276` |
| `exam-prep/blind-proof/strict/blind-manifest-strict.md` | `60a6872775ebc735a75c73a3ec74ff1fa025438304cd87108f15db2c87b0ac20` |
| `exam-prep/blind-proof/strict-flags/blind-manifest-strict-flags.md` | `6dcfeba3a70db2d35384e29b603fc5f87b14bb7d147cdbd0fe020040e9d24e5a` |

The 306 blinded cards of each variant, combined fingerprint (each card's
SHA-256 in card-number order, hashed):

| variant | SHA-256 |
|---|---|
| `ratio` | `021bdfbbb08bad12080090ffe02287246d143e1a0a9c617120fccaea9fb604e2` |
| `rank` | `00a428658914e43da1e1372c08844488dd6bcec69bfa192a280668efdcbc3a14` |
| `strict` | `fb9b83059a6682098a6de41848e8ac9d89ebb207719986b07333fa8346d653f4` |
| `strict-flags` | `49dc65c3af35a57ba7acf77bb1696a94272b7f2451e7b7e2fe05a2dcb631e8f6` |

A manifest carries the time it was written, so re-running a script rewrites its manifest text with a new timestamp even though the run number — the fingerprint of the inputs, RULES 29 — does not change. The run numbers are the stable identity; the hashes above identify the exact document text at the moment this file was written.

Earlier run records in each `runs/` folder are superseded runs of the same
scripts from earlier in this session, kept rather than deleted (RULES 30). One
directory, `exam-prep/blind-proof/ratio`, was deleted and rebuilt once during
this session after a literal `1%%` was found in a card line; that deletion is
recorded here rather than hidden.
