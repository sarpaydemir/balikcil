# JQ-R04-CONTENT-d · A field that other jurors' answers keep on the exam card, and the acceptance gate

Referred by: Mateo · data engineer · fifth-fix run · 2026-10-01 (system
clock), as part d of JQ-R04-CONTENT.
Corrected by: Mateo · sixth-fix run · 2026-10-01 (system clock). It is now a
question of its own, put to jurors who answer no other question about how
exam cards are blinded; it now names the families the audit already keeps outside the row,
with the reason the audit's code gives for each; option "no" is reworded.
The question's wording changes only where it named the other parts of its
former file; the other two options are unchanged. The earlier version is
kept unchanged.
**You do not need to open anything under `exam-prep/`; what you need is
quoted here.**

## What you open

- this file
- `RULES.md` (lines cited below)
- `TACTICS.md` (lines cited below)

## What you decide, and what you may not

You decide a **definition** (RULES 33): what the acceptance gate's
definition of `ALL-removable` covers, for a field that other jurors' ratified
answers keep on the exam card. You do **not** decide which attack grades the
gate (that is ratified, below), which fields stay on the exam card or how
they are printed (other jurors answer that), which features the audit
computes from which field (that is read from the audit's code), a
threshold, a score or a trading rule; and you do not change a rule.

You answer this question on its own. The jurors who answer it answer no
other question about how exam cards are blinded — not which fields an exam card keeps, not
how they are printed, and not when a column counts as carrying a coin
signature — and the jurors who answer those questions do not answer this
one, so that nobody chooses both what stays on a card and whether the gate
grades it.

Give: your answer; the file and line it rests on, quoted (RULES 34); the
strongest case against your answer; your confidence, 1–5. "Other" is
allowed, with reasons. Listing an option is not recommending it.

---

## The rule text

- `RULES.md` lines 34–35 (RULES 6): "The rule is written first, the result
  is opened second. A rule is not changed after looking at a result."
- `RULES.md` line 41 (RULES 9): "In the exam the coin name and the date are
  hidden."
- `RULES.md` lines 51–52 (RULES 12): "The chance line is not invented. The
  answers are shuffled 1,000 times, and the real result must fall inside the
  best 1%."
- `TACTICS.md` lines 50–51 (§3, the card): "the 24 hours before the start,
  hour by hour; plus a one-line summary of the previous 7 days."
- `TACTICS.md` lines 55–62 (§3, what is on the card): "price, volume, trade
  count, taker buy/sell pressure" · "open interest, long/short ratios
  (5-minute archive)" · "funding rate, payment interval and its changes" ·
  "order book depth" … "bitcoin and ethereum, over the same hours" · "US
  release calendar (inflation, employment, rate decision)".
- `TACTICS.md` lines 101–107 (§6, what is hidden): "the coin name" · "the
  date and time" · "the price itself (converted to a number starting from
  100)" · "the coin name inside announcements" · "the Wikipedia number
  itself (given as a ratio to the coin's own average)" · "the date in the
  release calendar".

---

## The acceptance gate

Before the answer key is sealed, the exam cards pass an acceptance gate. The
step it applies reads, as quoted in the acceptance-gate question
(JQ-R04-GATE), the step as first written: "If `ALL-removable` beats its
chance line on the exam cards, the cards are not blind and the gate has
failed." Which of the audit's two attacks decides was put to jurors and
ratified (`decisions/2026-10-01-jq-r04-gate/verdict.md` line 72): "The gate
fails if either the nearest-neighbour attack or the pair AUC attack beats
its own RULES 12 chance line on the exam cards." That ruling stands; this
question does not reopen it. The passages quoted here are all you need; you
need not open either file.

## The row `ALL-removable`

As the acceptance-gate question defines it: "`ALL-removable` is **every
feature in the audit's current list**, minus the families that must stay on
the card because a frozen canteen rule or TACTICS requires them." A
**feature** is a number the audit computes from what a card prints (for
example the typical level of a column, or how many of its values repeat);
features are grouped into **families**. What is left out of the row is
still measured on the exam cards and named in the exam manifest with its
size; the gate does not grade it.

**What is outside the row today.** In the audit as it stands, four families
are left out of the row. The audit's code gives one reason for each,
quoted:

- `volatility-frozen` (features of the hourly change column `chg%`): "the
  frozen book's S-1 reads `chg%` at 5.00% absolute"
- `funding-line` (features of the funding line): "B-5, U-2 and U-3 are
  answered from it"
- `p7-shape` (the price change and the high-low range printed in the
  previous-7-day line): "TACTICS 3 puts a previous-7-day summary on the card"
- `repeat-chg` (how many values repeat in `chg%`): "it reads the same
  unchanged `chg%` column"

This question does not ask about these four.

**What is inside the row today.** In the audit as it stands, everything it
computes from the bitcoin and ethereum columns, the trade-count column, the
price column and the other ranked columns is inside the row.

## What the other questions decide

Other jurors answer, separately (JQ-R04-DATE parts a–c and JQ-R04-CONTENT
parts a–c), what RULES 9 and TACTICS 3 and 6 require
or permit for these fields on an exam card: the bitcoin and ethereum
columns; the release names and the hour offsets in the US release line; the
trade-count column; how the price column is printed; and where the order of
the ranked columns comes from. Their ratified answers may keep a field on
the card, may permit more than one way of printing it (one of which may
leave it out), or may require it to be masked or removed. You do not see
their questions or their answers.

---

## The question

**Question d.** When the ratified answers to JQ-R04-DATE and to
JQ-R04-CONTENT parts a–c keep a field on the exam card, do the features the audit computes from that field count
as families "that must stay on the card because … TACTICS requires them",
and so leave `ALL-removable`?

- **yes** — a field the ratified answers keep on the card stays because
  TACTICS, as they read it, requires it there; its features leave the row
  and are measured and named, not graded.
- **only where no permitted rendering leaves it out** — its features leave
  the row only when the ratified answers permit no exam card without that
  field; where a permitted rendering without it exists, the field stays in
  the row if it is used.
- **no** — a field that stays on the card because jurors ruled that it may
  or must stay is not thereby one that TACTICS requires; only the four
  families listed above stay outside the row, and the features of every
  field the ratified answers keep stay in it, and the gate grades them.
- **Other**, with reasons.

Which features are computed from a field is read from the audit's code, not
chosen; the run that composes the row records it, and that run is reviewed.
If you think this cannot be answered as a definition — because one of the
options would accept or refuse a measured coin signature on exam cards under
RULES 9 as a rule, rather than read the gate's definition — say so: a
question about a rule is the user's, not a juror's (RULES 33).

---

## What follows from the answers — not to steer

Whatever you answer, every feature the audit computes is measured on the
exam cards and named in the exam manifest with its number. Your answer
decides only which of them the acceptance gate grades. Neither answer
changes `RULES.md`.
