# JQ-R04-CONTENT · May the blinding remove or recompute a field TACTICS 3 puts on the card? — three parts

Referred by: Mateo · data engineer · second-fix run · 2026-10-01 (system clock).
Corrected by: Mateo · third-fix run · 2026-10-01 (system clock) — part a: the
paragraph arguing about whether removal would help is removed, and the
premise now includes the one place the frozen canteen book names a trade
count; part b: the price-step figures are recomputed on the printed decimals,
and the nearest-neighbour figures are given in a form that does not depend on
how the cards are numbered.
Corrected by: Mateo · fourth-fix run · 2026-10-01 (system clock) — part a now
shows the trade-count column in both renderings that have been built, and its
question says which rendering it is about; every figure in parts a and b now
comes from an audit that compares distances exactly (the earlier audit
compared them in floating point, and some figures moved in the third or
fourth decimal; no "beats" changed); part c is new: it asks the point the
third review found no row answered.
Part a was first referred by the first exam-preparation run as its question
Q-5; part b arises from the review of that run (`exam-prep/REVIEW.md` §3.2)
and from the second-fix run's measurements; part c from the review of the
third-fix run (`exam-prep/REVIEW-3.md` §5). **You do not need to open
anything under `exam-prep/` except JQ-R04-DATE, which you answer too; what
you need is quoted here.**

## What you open

- this file
- `exam-prep/fourth-fix/juror-questions/JQ-R04-DATE.md` (answered by you too)
- `RULES.md` (lines cited below)
- `TACTICS.md` (lines cited below)
- `canteen/2026-09-19-sofia.md` lines 112–120 (the frozen canteen book's rule
  S-1), lines 221–225 (its blocker B-2), lines 245–246 (its blocker B-3),
  lines 268–270 (its blocker B-4) and lines 667–671 (its §4 item 4) — all
  quoted below as well

## What you decide, and what you may not

You decide a **definition** (RULES 33): what TACTICS 3's list of what is on a
card, TACTICS 3's "Numbers are rounded" and TACTICS 6's "the price itself
(converted to a number starting from 100)" permit a blinding to do, given
RULES 9. You do **not** decide a threshold, a score or a trading rule; you do
not change a rule; and you may not change anything the frozen canteen book
reads (RULES 6).

Answer together with JQ-R04-DATE
(`exam-prep/fourth-fix/juror-questions/JQ-R04-DATE.md`), by the same jurors:
both read RULES 9 against the TACTICS 3 list, and separate answers could
contradict each other. Parts a and c of this file bear on each other (see
part a).

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
- `TACTICS.md` line 57 (§3, on the card): "open interest, long/short ratios
  (5-minute archive)"; line 59: "order book depth".
- `TACTICS.md` line 71 (§3): "Numbers are rounded and the card is kept short."
- `TACTICS.md` lines 101–104 (§6, hidden): "the coin name" · "the date and
  time" · "the price itself (converted to a number starting from 100)".
- `canteen/2026-09-19-sofia.md` lines 114–120 (the frozen rule S-1): "at least
  one row whose hourly close-to-close change is |5.00%| or more. Read it from
  the `chg%` column. If an exam card does not print `chg%`, compute it from
  the `close` column as close(h)/close(h-1) - 1".
- `canteen/2026-09-19-sofia.md` lines 221–225 (the frozen blocker B-2):
  "Rule no: B-2 · the `taker L/S` column may not be read / Trigger : always —
  the column is excluded from every score. … Exit : n/a. It lifts only when
  somebody checks the column against the 5-minute taker archive and states a
  trade-count floor."
- `canteen/2026-09-19-sofia.md` lines 245–246 (the frozen blocker B-3):
  "any hour of the card prints `open int` = 0 between live neighbours. On
  such a card no open-interest statistic may be computed."
- `canteen/2026-09-19-sofia.md` lines 268–270 (the frozen blocker B-4): "the
  `depth -1%` or `depth +1%` column repeats one identical value for three or
  more consecutive hours. On such a card and such hours no depth statistic
  may be computed."
- `canteen/2026-09-19-sofia.md` lines 667–671 (§4 item 4): "**The trade-count
  floor under `taker L/S`.** No watcher names a number. … **How determined:**
  by Mateo/Nadia against the 5-minute taker archive, as a data-cleaning
  decision, not a trading decision. Until then B-2 excludes the column
  outright, which needs no number."

## How "carries a coin signature" is measured

The audit asks whether a feature of a card tells which coin it is, by two
attacks, each compared with its RULES 12 chance line (labels shuffled 1,000
times, best 1%):

- **pair AUC** — does similarity separate same-coin pairs of cards from
  different-coin pairs (0.5 = nothing)?
- **nearest neighbour** — is the most similar other card the same coin? The
  figures below use the version that, when several cards are exactly equally
  similar, averages over all of them; the audit's other version picks the
  lowest card number, and for features like these, where most cards have
  such ties, its result depends on how the cards happen to be numbered.

"Beats" below means above that attack's own chance line; a figure equal to
its line does not beat it. All numbers are from the 306 blinded observation
cards, measured by `scripts/29_identity_audit_exact.py` (folder
`exam-prep/fourth-fix/identity/`), with the run named at each table; nothing
has been measured on exam cards.

---

## Part a · The trade-count column

On the blinded card each hour's trade count is printed as its rank among the
card's 24 hours. The raw card writes trade counts rounded ("1k", "5k"), so a
busy coin's column has many equal values. Two ways of ranking have been
built (part c asks which are permitted):

- **from the printed values** — hours the raw card prints as equal get the
  same rank (the configuration called `strict-flags`, audit run
  `9ff0ffec3fe21ebe`);
- **from the values before rounding** — the rank of the value the card
  writer had before it rounded (otherwise the same configuration, audit run
  `d6557e91f9f97f7b`).

| rendering | feature | pair AUC (line) | nearest neighbour (line) |
|---|---|---|---|
| from the printed values | typical level of the ranked column | **0.5295** (0.5135) — beats | **0.1541** (0.1403) — beats |
| from the printed values | how many values repeat in the column | **0.5853** (0.5128) — beats | **0.2134** (0.1619) — beats |
| from the values before rounding | typical level of the ranked column | 0.4997 (0.5033) — does not beat | 0.1256 (0.1256) — does not beat |
| from the values before rounding | how many values repeat in the column | 0.5012 (0.5081) — does not beat | 0.1210 (0.1248) — does not beat |

So the column carries a measured coin signature when it is ranked from the
printed values, and, on these 306 cards, none that either attack finds when
it is ranked from the values before rounding.

What the frozen canteen book does with the trade count: **no rule, blocker,
score or exit in it reads a card's trade count.** Trade counts appear in it
as evidence cited in the basis of B-2 and B-3 (lines 229–234 and 251), and in
one place that bears on the future: blocker B-2 — which keeps the `taker L/S`
column out of every score — lifts only when "somebody checks the column
against the 5-minute taker archive and states a trade-count floor" (lines
224–225); the book assigns that check to a data-cleaning step against the
archive (lines 667–671). No floor has been stated, so B-2 is in force and no
trade count is read today. The book does not say whether a stated floor would
be applied to the trade count printed on a card or to the archive.

**Question a.** May the blinding leave out a column that TACTICS 3 puts on the
card, when nothing the frozen canteen book asks for reads it and, in the
rendering the exam card would otherwise carry, it carries a measured coin
signature?

- **yes** — RULES 9 is the rule; TACTICS 3 lists what a card may draw on, and
  the exam card may carry less.
- **no** — TACTICS 3 says what is on the card and TACTICS 6 lists, closed,
  what is hidden; a column not on that list stays.

If your answer to part c permits ranking from the values before rounding and
that rendering is used, the condition of this question is not met for the
trade-count column on today's measurements; your answer to part a then
governs any other column, or exam material, on which the condition is met.

Whether leaving the column out would close the coin signature of the card as
a whole is an engineering question and is not asked here; the answer is
measured and reported whichever way you rule.

## Part b · The price column

TACTICS 6 shows the price "converted to a number starting from 100": the
first run prints each hour's price divided by the first hour's price, times
100, at 2 decimals. The review found that rounding to 2 decimals makes
different prices print the same, and that this is a coin signature. Measured:

| rendering | cards where rounding makes two different prices print the same | repeat structure: pair AUC (line) | repeat structure: nearest neighbour (line) | smallest step between two printed prices: pair AUC (line) | same: nearest neighbour (line) |
|---|---|---|---|---|---|
| 2 decimals (first run) | 36 | **0.5416** (0.5108) | **0.1408** (0.1387) | **0.5995** (0.5130) | **0.1948** (0.1337) |
| 3 decimals (the fewest at which rounding makes no new repeats) | 0 | **0.5639** (0.5128) | **0.1510** (0.1401) | **0.6303** (0.5123) | **0.2525** (0.1567) |

(Sources: `exam-prep/second-fix/blind-proof/strict-flags-k1/blind-manifest-strict-flags-k1.md`
for the first column; audit runs `9ff0ffec3fe21ebe` (2 decimals) and
`762815a877c19551` (3 decimals) for the rest. The smallest step is computed on
the printed decimal text with exact arithmetic. Every figure in bold beats
its line. One sits close to it: the repeat structure's nearest neighbour at 2
decimals, 0.1408 against 0.1387; a verdict this close can change with the
seed of the shuffles (measured by the third review:
`exam-prep/review-3/probes/q2_tiefree_strict-flags.out`).)

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

## Part c · Where a ranked column's order comes from

On the blinded card nine columns are printed as each hour's rank among the
card's 24 hours: `quote vol`, `trades`, `taker buy%`, `open int`, `L/S acct`,
`top L/S pos`, `taker L/S`, `depth -1%`, `depth +1%`. Part a describes the
two ways of ranking that have been built, for the trade count; they apply to
all nine columns alike:

- **from the printed values** — the rank of the value the raw card prints.
  Hours the raw card prints as equal get the same rank.
- **from the values before rounding** — the rank of the value the card writer
  had before it rounded it for printing, read from the same sources the raw
  card is written from (the exchange's hourly figures and the laboratory's
  own 5-minute and order-book data). Hours the raw card prints as equal can
  get different ranks: the exam card then shows an order between them that
  the raw card does not print, and the watchers, who wrote the frozen book
  from raw cards, did not see.

Checked on all 306 observation cards for the second way: every value it
ranks, rounded as the card writer rounds, gives exactly the token the raw
card prints; the hours where the raw card prints an open-interest zero (B-3)
and the hours inside a run of three or more identical printed depth values
(B-4) are the same on the raw card and on the blinded card; `chg%` is
unchanged. How much finer order it adds, counted on the same cards (an hour
"tied on the raw card" prints the same value as another hour of the same
column of the same card):

| column | hours tied on the raw card | of those, ranked apart from an hour they tie with | cards with such an hour |
|---|---|---|---|
| `quote vol` | 119 | 119 | 48 |
| `trades` | 4,585 | 4,567 | 298 |
| `taker buy%` | 798 | 798 | 227 |
| `open int` | 1,309 | 1,302 | 190 |
| `L/S acct` | 4,884 | 4,860 | 304 |
| `top L/S pos` | 5,626 | 5,626 | 306 |
| `taker L/S` | 1,482 | 1,482 | 267 |
| `depth -1%` | 339 | 275 | 62 |
| `depth +1%` | 368 | 365 | 78 |

Every one of the 306 cards has at least one such hour in at least one of the
nine columns. (Source: `scripts/30_fourth_fix_checks.py`, run
`516027c6c9f215d6`, H-4.) What the second way does to the trade-count
column's measured coin signature is in part a. Whether an exam candidate can
use the finer order is not measured.

**Question c.** May a ranked column on an exam card be computed from the
values before the card writer's rounding, so that it can order hours which
the raw card prints as equal?

- **yes** — TACTICS 3 lists the field ("trade count", "open interest", …),
  not its rounded form; rounding is how a card is kept short (TACTICS 3
  line 71), and a rank computed from the field's own values is still that
  field.
- **no** — the exam card is computed from what the card prints: TACTICS 3
  says numbers are rounded, and the frozen book was written from cards whose
  values were rounded; an order finer than the printed values is information
  the card never carried.
- **Other**, with reasons.

---

## What follows from the answers — not to steer

Whatever is permitted will be built and audited, and the numbers reported,
before any exam card is built. A rendering that is not permitted will not be
used. Neither answer changes `RULES.md`; if no permitted rendering removes a
channel, the channel is named in the exam manifest with its number.
