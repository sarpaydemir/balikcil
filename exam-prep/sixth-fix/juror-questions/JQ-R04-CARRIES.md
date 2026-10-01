# JQ-R04-CARRIES · When does a printed column "carry a measured coin signature"? — two parts

Referred by: Mateo · data engineer · sixth-fix run · 2026-10-01 (system
clock). **You do not need to open anything under `exam-prep/`; what you
need is quoted here.**

## What you open

- this file
- `RULES.md` (lines cited below)
- `TACTICS.md` (lines cited below)

## Why this is asked, and when

Another question, put to other jurors **after** this one is ratified
(JQ-R04-CONTENT, part a), asks: "May the blinding leave out a column that
TACTICS 3 puts on the card, when nothing the frozen canteen book asks for
reads it and, in the rendering the exam card would otherwise carry, it
carries a measured coin signature?" It is asked about the trade-count
column. Whether a column carries a measured coin signature on the exam
cards will be measured before any exam card is used. That measurement needs
a definition, and no written rule gives one. This question asks for it. The
ratification sentence of your answer is given to those jurors, and the run
that applies their answer applies yours. It is used for that question only.

## What you decide, and what you may not

You decide a **definition** (RULES 33): what "carries a measured coin
signature" means when it is said of one printed column of an exam card —
which of the audit's two attacks decide it (part a), and which of
the audit's features count as the column's (part b). You do **not** decide
the chance line (RULES 12 fixes it: 1,000 shuffles, the best 1%), a
threshold, a score or a trading rule; you do not decide whether a column
may be left out (that is the other question, and its jurors are not you);
and you do not change a rule.

You answer this question on its own: the jurors who answer it answer no
other question about how exam cards are blinded.

Answer both parts; they are read together. For each: your answer; the file
and line it rests on, quoted (RULES 34); the strongest case against your
answer; your confidence, 1–5. "Other" is allowed, with reasons. Listing an
option is not recommending it.

If you think a part cannot be answered as a definition — for example
because choosing among its options sets how strict a test is, which would be
a threshold — say so: a threshold is not a juror's (RULES 33).

---

## The rule text

- `RULES.md` line 41 (RULES 9): "In the exam the coin name and the date are
  hidden."
- `RULES.md` lines 51–52 (RULES 12): "The chance line is not invented. The
  answers are shuffled 1,000 times, and the real result must fall inside the
  best 1%."
- `RULES.md` lines 119–121 (RULES 33): "A juror decides procedure and
  definition only: never a trading rule, never a threshold or score, and
  never a change to a rule in this file."
- `TACTICS.md` lines 50–51 (§3, the card): "the 24 hours before the start,
  hour by hour; plus a one-line summary of the previous 7 days."
- `TACTICS.md` line 56 (§3, on the card): "price, volume, trade count, taker
  buy/sell pressure".
- `TACTICS.md` lines 101–103 (§6, hidden): "the coin name" · "the date and
  time".

---

## How the audit measures a coin signature

The audit turns what a card prints into numbers, called **features** (for
example the typical level of a column, or how many of its values repeat),
and groups them into **families**. For a set of features it asks whether
they tell which coin a card is, by two attacks, each compared with its own
RULES 12 chance line (coin labels shuffled 1,000 times, best 1%):

- **pair AUC** — over every pair of cards, does similarity on these
  features separate same-coin pairs from different-coin pairs (0.5 =
  nothing)?
- **nearest neighbour** — for each card, is the most similar other card the
  same coin?

An attack **beats** its line when its result is above the line; a result
equal to its line does not beat it. A feature that has the same value on
every card of the set measured, or is missing on any card of it, is not
used.

The nearest-neighbour attack is computed in two versions, because several
other cards can be exactly equally similar to a card: one averages over all
of them; the other picks the one with the lowest card number, so its result
can depend on how the cards happen to be numbered. Where no card has such a
tie, the two are the same number. Where they disagree on whether the
attack beats its line, this question does not settle it: the run that
measures stops, and the point is referred before any exam card is used.

### The trade-count column, in the audit as it stands

On a blinded card the trade-count column is printed as each hour's rank
among the card's 24 hours. The audit computes features from it in three
families:

- `trades-level` — the typical level of the column (the logarithm of its
  median). The same family also holds one feature read from the
  previous-7-day line, not from the column: the average hourly trade count,
  on cards whose line prints one.
- `repeat-trades` — how many distinct values the column prints, and the
  largest number of hours that print one same value. Nothing else is in
  this family.
- `shape-scale-free` — the spread of the logarithms of the column's values,
  and how closely each hour's logarithm follows the previous hour's. The
  same family holds these two features for seven other columns as well
  (`quote vol`, `open int`, `depth -1%`, `depth +1%`, `L/S acct`,
  `top L/S pos`, `taker L/S`).

The audit tests each family as a whole, with both attacks. It does not
today test a column's own features as one set apart from the families.
Which features are computed from which column is read from the audit's
code, not chosen; for any other column it is read the same way, and the
run that measures records it and is reviewed.

---

## Part a · Which attack decides?

**Question a.** On the features that part b counts as the column's, when
does the column carry a measured coin signature?

- **A** — when the pair AUC beats its line.
- **B** — when the nearest neighbour beats its line.
- **C** — when **either** beats its line.
- **D** — only when **both** beat their lines.
- **Other**, with reasons.

## Part b · Which features count as the column's?

**Question b.** Which of the audit's features does part a's test read, when
it asks whether a column carries a measured coin signature?

- **own features, as one set** — every feature computed from the column's
  own printed values and from nothing else, tested together as one set (for
  the trade-count column: its typical level, its two repeat features and its
  two shape features; not the previous-7-day feature). The audit gains this
  set as a row of its own. Ground: a column's signature is what its own
  values carry; a feature read from another line or column belongs to that
  one.
- **every family that reads the column** — each family holding at least
  one feature computed from the column, tested as the audit tests it today;
  the column carries a signature when any of them does by part a (for the
  trade-count column: `trades-level`, `repeat-trades`, `shape-scale-free`).
  Ground: the families are the units the audit measures and reports, and
  each of these measures the column.
- **only families made of the column alone** — each family every feature of
  which, as the audit uses it on the card set measured, is computed from the
  column's own printed values and from nothing else; the column carries a
  signature when any of them does by part a (for the trade-count column:
  `repeat-trades`, and `trades-level` only where the previous-7-day feature
  is not used on that card set). Ground: a measurement shows this column's
  signature only where nothing but this column feeds it, and the families
  are the units the audit measures.
- **Other**, with reasons.

---

## What follows from the answers — not to steer

Whatever you answer, every feature the audit computes is measured on the
exam cards and named in the exam manifest with its number. Your answer
decides only when the other question's condition, "it carries a measured
coin signature", holds. It does not decide whether a column may be left out.
Neither answer changes `RULES.md`.
