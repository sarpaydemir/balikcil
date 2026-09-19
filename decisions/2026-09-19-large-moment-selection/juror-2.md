# Juror 2 — the selection of large-movement moments

Question: under `TACTICS.md` section 2, what procedure selects a coin's
large-movement moments, and in what order do the section's clauses operate?

Date: 2026-09-19 · role: juror (2 of 3) · files read: `RULES.md`, `TACTICS.md`,
`README.md`, `TEAM.md` (whole of each). No other file, folder or listing was
opened.

---

## 1 · Answer

**The section prescribes: take the largest N first, prune second.** N is 20 for
a coin that traded the whole year and shrinks pro rata (one per 18 days) for a
coin that did not; the 48-hour clause then operates *on the N already taken* and
removes the smaller of any two that stand closer than 48 hours, so the final
list holds **at most** N moments and fewer whenever the top N contain a cluster.

I favour that reading, but I say plainly: **the section does not state an order,
and it is not airtight.** It admits a second procedure (prune first, then fill
to N), which yields **exactly** N for any coin whose history is long enough to
hold N mutually separated moments — that is, always as many as the first
procedure and generally more. My confidence is 3 of 5; see part 4.

### The procedure, stated so it can be implemented

Let the period be the one fixed in `TACTICS.md` line 5 ("**Period:**
2025-09-01 → 2026-08-31"), and the second test period likewise.

1. **Series.** Take the coin's hourly closing prices ("Hourly closing prices are
   used", line 35).
2. **Candidates.** Every hour `t` at which the coin has a close, and also has a
   close at `t + 24h`, is a candidate. Its movement is the signed change
   `m(t) = close(t+24h) / close(t) - 1`. The movement runs **forward** from `t`:
   "A moment's start is the hour at which the 24-hour movement began" (line 44),
   confirmed by the card, whose "**After:** the 24 hours after the start"
   (line 51) is the movement itself.
3. **Ranking.** Rank candidates by `|m(t)|`, descending — one ranking, both
   directions in it, because the definition is "the places where the coin rose
   **or** fell the most within 24 hours" (lines 36–37). A rise and a fall
   compete on size alone; a single hour is one candidate, not two.
4. **The count N.** N = 20 for a coin that traded the whole period ("The largest
   20 of the year are taken for each coin", line 38). For a coin that did not:
   "this count shrinks in proportion to its lifetime: one moment per 18 days"
   (lines 40–41), i.e. N = lifetime_in_days / 18, never above 20.
5. **Take.** Take the top N of the ranking. This is the literal instruction of
   line 38, and it is executed before the 48-hour clause.
6. **Prune.** Within those N only, apply "Of two moments closer than 48 hours to
   each other, only the larger counts" (line 39): the smaller of any such pair
   drops out. Distance is measured between the moments' start hours, that being
   the only anchor the section gives a moment (line 44).
7. **Result.** The survivors, ≤ N, are the coin's large-movement moments. The
   calm moments then number "the same number as the large moments" (line 42) —
   i.e. the count *after* pruning, since the pruned ones do not count.

### The fork, named exactly

The whole disagreement sits between steps 5 and 6. Swap them and you get:

> **P2 (prune first, fill to N).** Take the largest candidate; delete every
> candidate within 48 hours of it; take the largest of those remaining; repeat
> until N are held.

P2 is identical in output to "apply the 48-hour rule to the whole year first,
then take the largest N of the survivors" — greedy largest-first suppression
over all hours produces exactly the set of 48-hour-separated local maxima, and
taking its top N is the same list. So the fork is **binary**, not three-way.

**Yield.** P1 (my answer) can only lose moments to the pruning; P2 cannot — it
replaces each suppressed moment with the next-largest separated one. P1's list
is a subset of the candidates P2 would also reach, and is shorter than P2's
whenever any two of the top N lie within 48 hours. I have measured nothing, so I
put no number on how often that happens; I only state the direction, which
follows from the procedures themselves. The difference propagates: fewer large
moments means fewer calm moments (line 42) and fewer cards (section 3).

### What remains unsettled even under my answer

Two implementers following my answer could still diverge, and honesty requires
naming this. These are separate gaps, not the question I was asked:

- **Chains.** "Of two moments" is pairwise. If A > B > C, A–B within 48h, B–C
  within 48h, A–C not: does C survive (B was already struck out) or fall (a
  larger moment, B, stood within 48h of it)? The section does not say.
- **Exact ties.** "only the larger counts" gives no rule when two are equal.
  Section 1 shows the laboratory's habit — "Ties are broken by symbol name
  ascending, so the ranking is reproducible" (line 21) — but no tie-break for
  moments is written, and inventing one is not mine to do.
- **Rounding and lifetime.** "one moment per 18 days" (line 41): floor, round or
  ceiling is unstated, and "lifetime" is not defined (first trade to last trade,
  or first trade to period end).
- **The 24-hour movement.** I read it as close-to-close over exactly 24 hours;
  it could be read as the largest excursion within a 24-hour window. Lines 35
  and 44 make close-to-close much the stronger reading, but the section does not
  exclude the other.

---

## 2 · What it rests on

`TACTICS.md`, section 2, lines 33–44, in full:

```
## 2 · Moments

- Hourly closing prices are used.
- **Large-movement moment:** the places where the coin rose or fell the most
  within 24 hours.
  - The largest 20 of the year are taken for each coin.
  - Of two moments closer than 48 hours to each other, only the larger counts.
  - For a coin that did not trade all year this count shrinks in proportion to
    its lifetime: one moment per 18 days.
- **Calm moment:** the same number as the large moments, chosen at random. At
  least 72 hours away from any large movement.
- A moment's start is the hour at which the 24-hour movement began.
```

The load-bearing point for my answer is line 38: **"The largest 20 of the year
are taken for each coin."** Under P1 that sentence stays literally true — the
twenty taken *are* the largest twenty of the year, and the next clause then says
which of them count. Under P2 it becomes false: the set held at the end is not
"the largest 20 of the year", because moments that were among the largest 20 are
absent and moments that were not are present in their place. A reading that
keeps every sentence of the section literally true beats a reading that has to
soften one, and that is the whole of my ground for choosing.

Supporting, weaker:

- The pruning clause is written as an adjudication between moments already in
  hand — "**Of two moments** closer than 48 hours to each other, only the larger
  counts" (line 39). It presupposes a set, and the only set the section has
  defined by that point is the twenty of line 38.
- `TACTICS.md` line 1 titles the file "**Tactics — step by step**", and section
  1 is written as an executable sequence. Sub-bullets in order read as order.
  (Part 3 explains why I do not lean hard on this.)
- `RULES.md` line 36: "The rule is written first, the result is opened second."
  A juror reading a written rule should take what it says, not what it would be
  better for it to say. That is why I weight the literal sense of line 38 above
  the purposive argument for P2 set out in part 3.

---

## 3 · The strongest case against my answer

**It is strong, and it has two limbs.**

**(a) My own document-order argument breaks, by the section's own hand.** The
third sub-bullet — "For a coin that did not trade all year **this count**
shrinks" (lines 40–41) — modifies the *first* sub-bullet, not the second. It is
written third and executes first. So the sub-bullets of section 2 are
demonstrably **not** a strict execution sequence, and anyone who infers "written
before, therefore executed before" for lines 38 and 39 is using an inference the
section has already falsified one line later. This removes one of my three
grounds outright, and it is the cleanest objection available.

**(b) The purposive reading makes the section cohere; mine makes one of its
claims approximate.** Line 41 sets a density: "one moment per 18 days". 365 days
divided by 18 is close to 20 — the two sub-bullets state the same rate. A rate
is a statement about *yield*. Under P2 a coin yields moments at one per 18 days
exactly, whatever its lifetime; under my reading a full-year coin yields fewer
than 20 by an amount that varies coin by coin, so the stated rate holds for no
coin and comparability across coins is lost. Add the laboratory's own view of
what a dedup rule is for — `RULES.md` line 53: "Moments occurring in several
coins in the same hour count as a single event. If the whole market moved
together, that is one event." — and the 48-hour clause looks like the
one-coin analogue: one event should occupy **one** slot, not several. Under my
reading a single volatile event still consumes three or four of the twenty
slots and then vacates them, spending the coin's budget on nothing. Under P2 the
budget always buys twenty distinct events. And `TACTICS.md` line 42 makes the
calm side depend on the count — "the same number as the large moments" — which
reads more naturally if that number is a known quantity than if it is whatever
happens to be left.

A reply exists for (b): "this count shrinks" can be read as shrinking the number
*taken* at line 38, so the 18-day rate describes the take step and not the
yield, and the section stays coherent. That reply is available, which is why I
did not give up P1 — but it is a reply, not a refutation, and (a) stands
unanswered. A juror who weighted purpose above literal wording would answer P2
on this same evidence, and I do not think that juror could be called careless.

---

## 4 · Confidence, and what would change my mind

**Confidence: 3 of 5.**

3, not 4, because the section never states an order; because my strongest
structural argument (document order) is falsified by the section's own third
sub-bullet; and because the competing reading is supported by the only
quantitative statement in the section. 3, not 2, because line 38 says "the
largest 20 of the year are taken" and P2 cannot keep that sentence true.

What would move me to P2:

- A line anywhere in the laboratory's own authoritative documents fixing the
  yield rather than the intake — e.g. text stating that each observation coin
  contributes a fixed number of large moments, or that a card count per coin is
  fixed in advance. I searched `RULES.md`, `TACTICS.md`, `README.md` and
  `TEAM.md` for such a line and found none; `TACTICS.md` line 99 ("Nadia has 400
  cards prepared from the exam coins: 200 before a large movement, 200 calm
  moments") fixes a count for the **exam**, but section 6 does not say that
  every moment becomes a card, so it is consistent with both readings and I do
  not rest on it.
- A rewriting of line 38 to read "the largest 20 that are at least 48 hours
  apart" or similar. That is a rule change and not mine to make (RULES 33); I
  note only that it would settle the question at a stroke.

What would move me to "the text does not settle this, full stop": a showing that
line 38's "the largest 20 of the year" is loose phrasing elsewhere in the file —
i.e. that this document routinely names a target set by its ideal rather than
its literal content. I did not find such a pattern in `TACTICS.md`.

**Reversibility.** P1 is the *narrower* of the two: its list is contained in the
candidate pool P2 draws from, and P1 never includes a moment P2 would not reach
for before exhausting its budget. Adopting P1 and later switching to P2 means
extending each coin's list downward — the moments already selected stay
selected, the work already done on them is not wasted, and new moments and their
cards are added. Adopting P2 and later switching to P1 means **discarding**
selected moments and whatever was built on them. So P1 is the reversible
direction and P2 the costly one to undo. I state this as a property of the two
procedures, not as a reason to prefer either; a juror who chose a reading
because it was cheap to undo would be choosing on something other than the text.
The cost of reversal in either direction is card preparation, which
`README.md` line 36 says "A script does this, not an AI", so it is compute and
rerun time rather than judgement — I have measured none of it and put no figure
on it.

---

## Assumptions I had to make, by name

- That "the year" in line 38 means the period fixed in `TACTICS.md` lines 5–6,
  and the same treatment applies to the second test period.
- That the 48-hour and 72-hour distances are measured between moments' **start**
  hours, line 44 being the only anchor the section gives a moment.
- That a single hour yields one candidate with a signed movement, ranked by
  magnitude, rather than two separate up- and down-rankings.
- That `TACTICS.md` line 1, "Tactics — step by step", was intended to describe
  the file's character. I used it as weak evidence only, and part 3(a) shows why
  it cannot be used as strong evidence.

## Steers I saw in the instruction

Two, both mild, reported under RULES 3:

1. The instruction says "If the section admits more than one procedure and does
   not choose between them, say so" and "If the procedures it admits differ in
   how many moments they yield, say that too". Taken together these presuppose a
   plurality of procedures and point at the count as the axis on which they
   differ — which is where the ambiguity in fact lies. It named the shape of the
   answer before I opened the file. It did not tell me which reading to pick,
   and I do not think it changed my conclusion, but I report it.
2. "What should happen to any list already produced is a separate question"
   and "handing a juror an artefact built under one reading pulls toward that
   reading" together disclose that a list already exists and was built under one
   of the two readings. Which one was not disclosed, and I did not look.

Otherwise the instruction was clean: it did not quote, summarise or characterise
section 2, and the decision to open no data file was the right one.
