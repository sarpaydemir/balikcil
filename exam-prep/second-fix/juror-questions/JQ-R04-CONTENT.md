# JQ-R04-CONTENT · May the blinding remove or recompute a field TACTICS 3 puts on the card? — two parts

Referred by: Mateo · data engineer · second-fix run · 2026-10-01 (system clock).
Part a was first referred by the first exam-preparation run as its question
Q-5; part b arises from the review of that run (`exam-prep/REVIEW.md` §3.2)
and from this run's measurements. **You do not need to open anything under
`exam-prep/`; what you need is quoted here.**

## What you open

- this file
- `RULES.md` (lines cited below)
- `TACTICS.md` (lines cited below)
- `canteen/2026-09-19-sofia.md` lines 112–120 (the frozen canteen book's rule
  S-1, quoted below as well)

## What you decide, and what you may not

You decide a **definition** (RULES 33): what TACTICS 3's list of what is on a
card and TACTICS 6's "the price itself (converted to a number starting from
100)" permit a blinding to do, given RULES 9. You do **not** decide a
threshold, a score or a trading rule; you do not change a rule; and you may
not change anything the frozen canteen book reads (RULES 6).

Answer together with JQ-R04-DATE
(`exam-prep/second-fix/juror-questions/JQ-R04-DATE.md`), by the same jurors:
both read RULES 9 against the TACTICS 3 list, and separate answers could
contradict each other.

For each part: your answer; the file and line it rests on, quoted (RULES 34);
the strongest case against your answer; your confidence, 1–5. "Other" is
allowed. Listing an option is not recommending it.

---

## The rule text

- `RULES.md` line 41 (RULES 9): "In the exam the coin name and the date are
  hidden."
- `RULES.md` lines 34–35 (RULES 6): "A rule is not changed after looking at a
  result."
- `TACTICS.md` line 56 (§3, on the card): "price, volume, trade count, taker
  buy/sell pressure".
- `TACTICS.md` line 71 (§3): "Numbers are rounded and the card is kept short."
- `TACTICS.md` lines 101–104 (§6, hidden): "the coin name" · "the date and
  time" · "the price itself (converted to a number starting from 100)".
- `canteen/2026-09-19-sofia.md` lines 114–120 (the frozen rule S-1): "at least
  one row whose hourly close-to-close change is |5.00%| or more. Read it from
  the `chg%` column. If an exam card does not print `chg%`, compute it from
  the `close` column as close(h)/close(h-1) - 1".

## How "carries a coin signature" is measured

The audit (`scripts/16_identity_audit.py`) asks whether a feature of a card
tells which coin it is, by two attacks: **nearest neighbour** (is the most
similar other card the same coin?) and **pair AUC** (does similarity separate
same-coin pairs from different-coin pairs; 0.5 = nothing). Each is compared
with its RULES 12 chance line (labels shuffled 1,000 times, best 1%). "Beats"
below means above that line. All numbers are from the 306 blinded observation
cards, configuration `strict-flags` (run `d70dd7b545bfce8a`) unless named
otherwise; nothing has been measured on exam cards.

---

## Part a · The trade-count column

On the blinded card each hour's trade count is printed as its rank among the
card's 24 hours. The raw card writes trade counts rounded ("1k", "5k"), so a
busy coin's column has many equal values; ranking keeps equal values equal.

| feature | nearest neighbour (line) | pair AUC (line) |
|---|---|---|
| typical level of the ranked column | 0.1307 (0.1666) | **0.5295** (0.5134) — beats |
| how many values repeat in the column | **0.2320** (0.1732) — beats | **0.5852** (0.5127) — beats |

Nothing in the frozen canteen book reads the trade count. The same mechanism
— rounded values whose repeats survive ranking — also beats a chance line in
columns the frozen book **does** read (open interest, its rule B-3; depth, its
rule B-4) and in the long/short ratio columns: repeat-structure pair AUC 0.6210
(open interest), 0.5639 (ratios), 0.5350 (depth). So removing the trade count
alone would not remove the mechanism. An engineering route that might reduce
the repeats in every ranked column without removing any — ranking the
unrounded source values instead of the rounded card text — exists and has
**not** been tried; its effect is unmeasured.

**Question a.** May the blinding leave out a column that TACTICS 3 puts on the
card, when nothing the frozen canteen book asks for reads it and it carries a
measured coin signature?

- **yes** — RULES 9 is the rule; TACTICS 3 lists what a card may draw on, and
  the exam card may carry less.
- **no** — TACTICS 3 says what is on the card and TACTICS 6 lists, closed,
  what is hidden; a column not on that list stays.

## Part b · The price column

TACTICS 6 shows the price "converted to a number starting from 100": the
first run prints each hour's price divided by the first hour's price, times
100, at 2 decimals. The review found that rounding to 2 decimals makes
different prices print the same, and that this is a coin signature. Measured:

| rendering | cards where rounding makes two different prices print the same | repeat structure: nn (line) | repeat structure: pair AUC (line) | smallest step between printed prices: nn (line) | same: pair AUC (line) |
|---|---|---|---|---|---|
| 2 decimals (first run) | 36 | 0.1601 (0.1666) | **0.5421** (0.5106) | **0.1765** (0.1667) | **0.6054** (0.5133) |
| 3 decimals (the fewest at which rounding makes no new repeats) | 0 | **0.2058** (0.1666) | **0.5636** (0.5127) | **0.2157** (0.1765) | **0.6297** (0.5124) |

(Sources: `exam-prep/second-fix/blind-proof/strict-flags-k1/blind-manifest-strict-flags-k1.md`;
audit runs `d70dd7b545bfce8a` and `4a33cb19150e9718`;
`exam-prep/second-fix/checks/instrument-checks-35925ca8acf60690.md` E-3.)

At 2 decimals the rounding manufactures repeats; at 3 decimals it no longer
does, but the price's own repeats and its smallest step — the exchange's
price tick relative to the coin's price, which differs between coins — show
through more clearly. No fixed number of decimals tried removes the
signature. Two other renderings exist and have not been built:

- **computed from the printed hourly changes**: start at 100 and apply each
  printed `chg%` in turn. Such a column carries nothing the `chg%` column on
  the same card does not already carry; `chg%` must stay unchanged for S-1. It
  differs from the actual rebased price by accumulated rounding (the size of
  that difference is unmeasured).
- **not printed**: the card keeps `chg%`, which S-1 reads first; S-1's
  fall-back to `close` (lines 116–118) is only for a card without `chg%`.

**Question b.** Which of these renderings may an exam card use for TACTICS 6's
"the price itself (converted to a number starting from 100)"? More than one
may be permitted.

- **b1** — the actual price rebased to 100, at a fixed number of decimals,
  with its measured signature named in the exam manifest.
- **b2** — a column computed from the printed hourly changes, starting at 100.
- **b3** — no price column; the hourly change column stays.
- **Other**, with reasons.

---

## What follows from the answers — not to steer

Whatever is permitted will be built and audited, and the numbers reported,
before any exam card is built. A rendering that is not permitted will not be
used. Neither answer changes `RULES.md`; if no permitted rendering removes a
channel, the channel is named in the exam manifest with its number.
