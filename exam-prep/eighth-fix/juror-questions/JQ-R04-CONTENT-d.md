# JQ-R04-CONTENT-d · Which features of what an exam card prints does the acceptance gate grade?

Referred by: Mateo · data engineer · fifth-fix run · 2026-10-01 (system
clock), as part d of JQ-R04-CONTENT.
Rewritten by: Mateo · eighth-fix run · 2026-10-02 (system clock). Every
earlier version is kept unchanged; you do not need any of them.
**You do not need to open anything under `exam-prep/` or `decisions/`; what
you need is quoted here.**

## What you open

- this file
- `RULES.md` (lines cited below)
- `TACTICS.md` (lines cited below)

That is your whole reading list. Verdict files are cited below as sources
only; the sentences you need from them are quoted here.

## What you decide, and what you may not

You decide a **definition** (RULES 33): what the acceptance gate's
definition of its graded set covers, for a field that an exam card prints.
You do **not** decide which attacks grade the gate, which fields stay on an
exam card or how they are printed, or what "carries a measured coin
signature" means (other jurors have answered those; their outcomes are
quoted below and stand); you do not decide which features the audit
computes from which field (that is read from the audit's code), a
threshold, a score or a trading rule; and you do not change a rule. If you
judge that this question is not a juror's to answer at all, that is one of
the answers offered below.

You answer this question on its own. The jurors who answer it answered no
other question about how exam cards are blinded, and are not given those
questions or their answers beyond the outcome sentences quoted here.

Give: your answer; the file and line it rests on, quoted (RULES 34); the
strongest case against your answer; your confidence, 1–5. "Other" is
allowed, with reasons. Listing an option is not recommending it.

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
- `TACTICS.md` lines 55–64 (§3, what is on the card), for example: "price,
  volume, trade count, taker buy/sell pressure" · "open interest,
  long/short ratios (5-minute archive)" · "funding rate, payment interval
  and its changes" · "bitcoin and ethereum, over the same hours" · "number
  of people viewing the page on Wikipedia (daily)".
- `TACTICS.md` lines 101–107 (§6, what is hidden): "the coin name" · "the
  date and time" · "the price itself (converted to a number starting from
  100)" · "the coin name inside announcements" · "the Wikipedia number
  itself (given as a ratio to the coin's own average)" · "the date in the
  release calendar".
- `TACTICS.md` line 94 (§5): "Then the canteen book freezes". The **frozen
  canteen book** is the laboratory's book of trading rules, written from the
  observation cards and frozen before the exam.

A **field** here is one thing TACTICS 3 puts on the card: a column of the
hour-by-hour table (one value per hour), or a line of the card (the
for example the previous-7-day summary, the funding line, the Wikipedia
line, the US release line).

---

## The acceptance gate

Before the exam's answer key is sealed, a script, the laboratory's identity
audit, reads all the exam cards and tries to tell which cards belong to the
same coin from what they print alone. From each card it computes
**features**: numbers computed from what the card prints (for example the
typical level of a column, or how many of its 24 values repeat). It attacks
a set of features in two ways, each compared with its own RULES 12 chance
line:

- **nearest neighbour** — for each card, find the most similar other card;
  count how often it is the same coin;
- **pair AUC** — over every pair of cards, how well similarity separates
  same-coin pairs from different-coin pairs.

The step the gate applies reads, as quoted in the acceptance-gate question
(JQ-R04-GATE), the step as first written: "If `ALL-removable` beats its
chance line on the exam cards, the cards are not blind and the gate has
failed." Which attack decides was put to jurors and ratified
(`decisions/2026-10-01-jq-r04-gate/verdict.md` line 72): "The gate fails if
either the nearest-neighbour attack or the pair AUC attack beats its own
RULES 12 chance line on the exam cards." That ruling stands; this question
does not reopen it.

## The graded set, `ALL-removable`

The gate grades only the set called `ALL-removable`, which its written
definition (as the acceptance-gate question, JQ-R04-GATE, gives it) makes
"every feature in the audit's current list, minus the
families that must stay on the card because a frozen canteen rule or
TACTICS requires them". **Every feature, graded or not, is measured on the
exam cards and named, with its size, in the record written with the exam
cards.** What is outside the set cannot make the gate fail.

**What is outside the set in the audit as it stands.** Four groups of
features:

- the average and the largest absolute value, and the spread, of the
  hourly price-change column (`chg%`);
- how many values repeat in that same column;
- everything computed from the funding line;
- the price change and the high–low range printed in the previous-7-day
  line.

This question does not ask about these four, and no answer below changes
them.

**What is inside the set in the audit as it stands.** Every other feature:
everything the audit computes from the price column; from the volume,
trade-count, taker-buy, open-interest, three long/short-ratio and two
order-book-depth columns; from the bitcoin and ethereum columns; the
average hourly volume and the average hourly trade count printed in the
previous-7-day line; and whether the Wikipedia line is present. Each of
these features is computed from one field only. The audit computes no
feature from the US release line or from announcements.

## What other jurors ratified

Quoted up to each answer; the verdicts' reasons and splits are not given
here. Source: `decisions/2026-10-01-jq-r04-date-content/verdict.md` lines
39–47, and `decisions/2026-10-01-jq-r04-carries/verdict.md` lines 107 and
109.

- JQ-R04-DATE-a: "Do RULES 9 and TACTICS 6 require removing columns that
  identify clock hours? **No.**" (The question was about the bitcoin and
  ethereum columns.)
- JQ-R04-DATE-b: "Does hiding "the date in the release calendar" cover
  release *names* that identify the day? **No.**"
- JQ-R04-DATE-c: "Does hiding "the date and time" cover clock hour revealed
  by an offset plus outside knowledge of release times? **No.**"
- JQ-R04-CONTENT-a: "May the blinding remove a TACTICS 3 field when nothing
  frozen reads it and it carries a measured coin signature? **Yes** — when
  both conditions hold: nothing the frozen canteen book reads it, and in
  the rendering the exam card would otherwise carry, it carries a measured
  coin signature as JQ-R04-CARRIES defines one."
- JQ-R04-CONTENT-b, the price column: "**b1** (actual price rebased to 100,
  fixed decimals): Permitted." · "**b2** (computed from printed chg%,
  starting from 100): Permitted." · "**b3** (no price column; chg% stays):
  Permitted only if and as far as CONTENT-a yes."
- JQ-R04-CONTENT-c: "May a ranked column come from pre-rounding values,
  ordering hours the raw card prints as equal? **No.**" (On the blinded
  card nine columns are printed as each hour's rank among the card's 24
  hours.)
- JQ-R04-CARRIES-a: "When the test in part b identifies a column's feature
  sets, the column carries a measured coin signature when **either** the
  pair AUC attack or the nearest-neighbour attack beats its own RULES 12
  chance line on that set."
- JQ-R04-CARRIES-b: "The test reads every feature computed from the
  column's own printed values and from nothing else, tested together as one
  set."

Whether a column carries a measured coin signature is measured on the exam
cards, as JQ-R04-CARRIES defines it, before any exam card is used. Which
columns the frozen canteen book reads is recorded before the exam cards are
built; where that is unclear, the point is referred, not settled by the run
that records it.

---

## The question

**Question d.** Under the ratified outcomes above, do the features
computed from a field that an exam card prints count among the families
"that must stay on the card because … TACTICS requires them", so that they
leave `ALL-removable` and are measured and named, not graded?

- **no** — "TACTICS requires" means what TACTICS requires by its own words;
  ratified outcomes that let a field stay, or that give no permission to
  leave it out, do not make it required. Only the four groups listed above
  stay outside the set; the features of every field the card prints are in
  it and graded.
- **only where the card may not be without the field** — a field that the
  ratified outcomes give no permission to leave out stays because TACTICS 3
  lists it and nothing permits a card without it, and so is required; its
  features leave the set. A field they permit to be left out is removable:
  if the card prints it, its features are in the set and graded. A field
  counts as one the card may be without only where both conditions of
  that permission (JQ-R04-CONTENT-a, quoted above) are established for it
  before the gate is run: one is measured on the exam cards, the other is
  recorded from the frozen canteen book.
- **yes** — a field the exam card prints is there because TACTICS 3 puts
  it on the card and no ratified outcome removes it, and so is required;
  its features leave the set.
- **not a juror's** — this cannot be answered as a definition: whether the
  gate grades what an exam card prints decides what RULES 9 requires of an
  exam, which is a question about a rule, and a juror may not decide it
  (RULES 33).
- **Other**, with reasons.

## What each answer does to the graded set — mechanically

Which features are computed from which field is read from the audit's
code, not chosen.

- **no:** the set is every feature the audit computes on the exam cards,
  except the four groups listed above.
- **only where the card may not be without the field:** the set holds the
  features of each column the card prints for which both conditions of
  JQ-R04-CONTENT-a are established: the measurement on the exam cards says
  it carries a measured coin signature, and the record says nothing the
  frozen canteen book reads it. The features of every other field the card
  prints leave the set. The test JQ-R04-CARRIES ratified is written for a
  column; no ratified outcome gives one for a line of the card, so under
  this answer the features computed from the previous-7-day line and the
  Wikipedia line leave the set.
- **yes:** every feature the audit computes is computed from a field the
  card prints, so under this answer the set holds no feature.
- **not a juror's:** the set is not composed from this question. If this
  is the ratified outcome, or if the referee refuses this question on
  scope (RULES 35), the question goes to the user.

Under every answer, where the run that builds the gate cannot go on, it
stops and tells the coordinator; it does not settle the point itself:

1. if the set holds no feature on the exam cards — the audit then reports
   "no features left after blinding" for it, neither attack has a result,
   and the gate is recorded as not graded;
2. if a version of the audit computes a feature from a field whose
   features leave the set and from one whose features stay;
3. under "only where the card may not be without the field": until the
   measurement and the record that answer rests on are complete for every
   column the card prints, or where either of them stops or is unclear for
   a column;
4. if a ratified "Other" cannot be carried out as written.

What follows a stop is not decided by this question.

---

## What follows from the answers — not to steer

Whatever you answer, every feature the audit computes is measured on the
exam cards and named, with its size, in the record written with the exam
cards. Your answer decides only which of them can make the gate fail. No
answer changes `RULES.md`, the gate's ratified rule, or anything other
jurors ruled about which fields stay and how they are printed.
