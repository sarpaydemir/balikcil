# Juror 3 — the selection of large-movement moments

**Question:** Under `TACTICS.md` section 2, what procedure selects a coin's
large-movement moments, and in what order do the section's clauses operate?

**Date:** 2026-09-19 · **Role:** juror (one of three, answered independently)

---

## 1 · Answer

Section 2 prescribes **one selection pass in which the 48-hour separation is a
constraint applied *while* the moments are being chosen, not a cull applied
*after* a set of 20 has already been fixed.** The count clause (20 per year, or
one per 18 days of lifetime) is a **quota on the delivered list**, and the
selection stops when the quota is filled.

Implementable statement:

1. **Series.** Use hourly closing prices for the coin over the period of
   `TACTICS.md` section 0.
2. **Candidates.** For every hour `h` at which both `close(h)` and `close(h+24)`
   exist, form one candidate whose *start* is `h` and whose *size* is the
   magnitude of the change from `close(h)` to `close(h+24)`, irrespective of
   sign. Rises and falls go into **one pooled ranking** by size.
3. **Quota `N`.** `N = 20` for a coin that traded the whole year; for a coin
   that did not, `N` = its lifetime divided by 18 days. (The rounding of that
   division, and whether "lifetime" ends at the last trade or at the end of the
   period, are gaps the section does not fill — see §3.)
4. **Selection.** Walk the candidates in descending order of size. Take a
   candidate if its start hour is **48 hours or more** away from the start hour
   of every candidate already taken; otherwise skip it. Stop when `N` moments
   have been taken, or when the candidate list is exhausted.
5. **Output.** The taken moments, each timestamped by its start hour. A coin
   with enough well-separated candidates therefore receives **exactly `N`**
   moments.
6. **Calm moments** then number the same as the large moments actually produced,
   drawn at random with every start at least 72 hours from any large movement.

**Order of the clauses:** the bullet order in the file is *not* the order of
operations. The definition bullet ("rose or fell the most within 24 hours")
generates and ranks candidates; the 48-hour bullet is a **filter on the
selection**; the "largest 20 / one per 18 days" bullets are a **stopping
condition** that the 48-hour filter runs *inside*, not before. The sentence
about a moment's start is a definition used by the 48-hour bullet, and it
operates first of all.

**The competing reading, named.** The other available reading is: take the top
20 candidates by size, *then* discard, inside those 20, the smaller of any pair
closer than 48 hours. I do not think the section prescribes it, for the reasons
in §2, but the section never writes an explicit ordering marker, so a referee
could legitimately record this point as "the file does not say it in so many
words". The two readings **differ in how many moments they yield**: the
quota-preserving reading delivers the full quota whenever the coin has enough
separated candidates; the truncate-then-prune reading delivers *no more than*
the quota and, for hourly candidates, in general **substantially fewer**,
because windows starting one, two or three hours apart describe very nearly the
same movement and so the largest 20 windows of a year are mostly repetitions of
a handful of episodes. I have measured nothing; the direction of that difference
follows from the candidate construction, the size of it does not and I do not
state one.

**Reversible / irreversible.** Both readings are re-runnable by script from the
price data, so the choice is reversible at the selection step. What it costs to
reverse anything already built on a list is the separate jury's question, and I
do not touch it.

---

## 2 · What it rests on

All quotations are from `/home/user/balikcil/TACTICS.md`, section 2 unless
stated.

Lines 34–44, the whole section, are:

> - Hourly closing prices are used. *(line 34)*
> - **Large-movement moment:** the places where the coin rose or fell the most
>   within 24 hours. *(lines 35–36)*
>   - The largest 20 of the year are taken for each coin. *(line 37)*
>   - Of two moments closer than 48 hours to each other, only the larger counts.
>     *(line 38)*
>   - For a coin that did not trade all year this count shrinks in proportion to
>     its lifetime: one moment per 18 days. *(lines 39–40)*
> - **Calm moment:** the same number as the large moments, chosen at random. At
>   least 72 hours away from any large movement. *(lines 41–42)*
> - A moment's start is the hour at which the 24-hour movement began. *(line 43)*

**(a) The quota is a density of delivered moments — the 18-day clause.**
"this count shrinks in proportion to its lifetime: **one moment per 18 days**"
(lines 39–40). A year is 365 days and 365 ÷ 20 = 18.25; the 18-day figure is the
20-per-year rate restated as a rate. A rate of *one moment per 18 days* is a
statement about how many moments a coin ends up with. Under the
truncate-then-prune reading the delivered rate would be neither 20 per year nor
one per 18 days but an uncontrolled leftover, different for every coin, and the
sentence would describe nothing the laboratory actually produces. Under the
quota-preserving reading the sentence is exactly true of the output.

**(b) Only the quota-preserving reading determines a single list.** The 48-hour
clause is written pairwise — "Of two moments closer than 48 hours to each other,
only the larger counts" (line 38). Applied to a *fixed* set as a post-filter, a
pairwise rule does not determine an answer where three or more moments chain.
Take moments at hours 0, 40 and 80 with sizes 10, 11 and 12: suppressing every
moment that has a larger moment within 48 hours leaves only the hour-80 moment,
whereas resolving the pairs one at a time from the largest downwards leaves the
hour-80 *and* the hour-0 moments. The section supplies no rule for that chain.
Read as a constraint during a descending walk, the same sentence is complete:
"the larger counts" means the already-taken, larger moment keeps its place and
the later, smaller one is skipped. The instruction asks for a procedure
"precisely enough that two people implementing it from your answer would produce
the same list"; of the two readings, only this one reaches that standard from
the text alone.

**(c) The clauses are constraints, not a numbered sequence.** Where `TACTICS.md`
means an ordering it marks it. Section 1, line 15–16: a new coin is "Assigned
**first and exclusively** — a new coin is not also ranked by volume." Section 2
carries no such marker anywhere. Bullet order in a definition block is therefore
not evidence of operation order, and the harmonious reading — the one under
which all three sub-bullets are true of the finished list at once — governs.

**(d) The pooled, sign-blind ranking.** "the places where the coin **rose or
fell** the most" (line 36) with "The **largest 20**" (line 37) — a single set of
20, not 20 up and 20 down. Line 38 compares two arbitrary moments by which is
"the larger"; that comparison is only meaningful between a rise and a fall if
size is measured without sign, so one pooled ranking by magnitude is the reading
the section's own comparison presupposes.

**(e) The 48 hours is measured start-to-start.** "A moment's start is the hour at
which the 24-hour movement began" (line 43) gives a moment exactly one time
coordinate, and it is the only one the section defines; "closer than 48 hours to
each other" (line 38) therefore compares start hours. Note the consequence: 48
hours is twice the 24-hour window, so two accepted moments never overlap and
always leave a clear day between them.

**(f) The count propagates downstream, so it is not a cosmetic choice.** "**Calm
moment:** the same number as the large moments" (line 41). Whatever the large
count is, the calm count copies it, and section 3 line 47 writes "One page per
moment" — the card count follows too.

**(g) Nothing outside section 2 supplies the missing order.** I checked the whole
of `RULES.md`, `README.md` and `TEAM.md` for a rule that would fix it. The
nearest candidates do not apply: RULES 13, "Moments occurring in several coins in
the same hour count as a single event. If the whole market moved together, that
is one event", and `TACTICS.md` line 127, "A moment appearing in several cards in
the same hour counts as a single event", are both *cross-coin* rules that bite at
scoring time, not within-coin selection rules; `README.md` line 34 says only
"Each coin's large-movement moments and calm moments are found"; `TEAM.md`
lines 16–17 assign the work to Mateo without describing it. So: no other file
settles the order. That is where I looked (RULES 19–20 discipline).

---

## 3 · The strongest case against my answer

**The clauses really are written in sequence, and I am overriding the page.**
The three sub-bullets sit under the definition in the order: take the largest 20
— then prune pairs within 48 hours — then scale the count for short-lived coins.
A reader implementing top-down does precisely the truncate-then-prune procedure,
and that reader is not doing violence to anything: the file is titled "Tactics —
**step by step**" (line 1). Moreover, line 38 says "Of two **moments** closer
than 48 hours", and section 2 defines "moment" as a *selected* large-movement
moment, not as one of the thousands of hourly candidates. On that vocabulary the
48-hour clause can only be operating on a set already selected — i.e. on the
20 — which is exactly the reading I rejected. My answer has to read "moments" as
"candidates for momenthood", and the file never uses the word that way.

**The 18-day clause can be read as being about the parameter, not the output.**
"**this count** shrinks in proportion to its lifetime" most directly refers to
the count in the previous bullet — the number *taken* — and a number taken can
perfectly well be trimmed afterwards. On that reading (a) collapses.

**The indirect phrasing of the calm clause cuts against me.** If the large count
were always the quota exactly, the author could have written "20 of these too".
Writing "the same number as the large moments" (line 41) is what one writes when
the large count is a computed leftover that has to be referenced rather than
stated. (This is weakened but not destroyed by the fact that the lifetime
scaling makes the count coin-dependent under either reading, so indirect phrasing
was needed anyway.)

**Under-determinacy is a weak argument from silence.** My point (b) says the
post-filter reading fails to name a chain rule and therefore cannot be meant. But
`TACTICS.md` leaves other things unnamed and simply expects the engineer to pick
something sensible — the section names no tie-break for two equal-sized moments
either (section 1 line 21 has one, "Ties are broken by symbol name ascending, so
the ranking is reproducible"; section 2 has none), and no rounding rule for
lifetime ÷ 18 days. If silence does not invalidate the section on those points,
it should not invalidate a reading on this one.

**Honest weight.** I find (a) and (b) together stronger than these, chiefly
because the truncate-then-prune reading makes the section's own 18-day rate
untrue of everything the laboratory produces. But a juror who answered "the
section does not settle the order" would not be making an error, and I would not
call that answer wrong.

---

## 4 · Confidence, and what would change my mind

**Confidence: 3 of 5.**

3 and not higher because the section contains **no explicit ordering marker**,
because the file elsewhere shows the author marks order when order matters, and
because the word "moments" in line 38 genuinely reads more naturally as
"selected moments". 3 and not lower because two independent considerations — the
one-per-18-days rate, and the fact that only one reading produces a determinate
list from the text alone — point the same way.

**What would change my mind, toward truncate-then-prune or toward "not
settled":**

- any line in a document I was not permitted to read (`LEDGER.md`, an agent
  definition, the moment-finding script's specification) that states the order
  explicitly, or that records a rounding/tie-break convention implying one
  reading. The referee, or a juror with wider access, should check that before
  ratifying.
- a showing that 365 ÷ 20 ≈ 18.25 is coincidence — e.g. that 18 days was chosen
  for an unrelated reason — which would dissolve argument (a).
- a chain-resolution rule for the pairwise filter found anywhere in the
  laboratory's own documents, which would dissolve argument (b).

**What would not change my mind:** any count of moments that some already-built
list happens to contain. A list built under one reading is evidence about the
implementer, not about the text (RULES 6: "The rule is written first, the result
is opened second"), and I deliberately did not look at one.

---

## Gaps I am naming and not filling (RULES 22, RULES 33)

These are unsettled by section 2 under **either** reading, and none of them is
mine to decide:

1. **Rounding** of `lifetime ÷ 18 days` to a whole number of moments.
2. **"Lifetime"** — first trade to last trade, or first trade to the end of the
   period, for a coin that died mid-period.
3. **Tie-break** between two candidates of exactly equal size (section 1 line 21
   has a convention for the draw; section 2 states none).
4. **Size measured how** — percentage change or absolute price change. Percentage
   is the ordinary reading for a coin, but line 36 says only "rose or fell the
   most" and does not say.
5. Whether the 48-hour separation is `> 48` or `>= 48` hours ("closer than 48
   hours", line 38, reads as strictly less than 48 being forbidden, so `>= 48` is
   accepted — I have stated that in §1.4, and flag it here as the one borderline
   I did resolve on the wording).

---

## Files read

- `/home/user/balikcil/TACTICS.md` (whole)
- `/home/user/balikcil/RULES.md` (whole)
- `/home/user/balikcil/README.md` (whole)
- `/home/user/balikcil/TEAM.md` (whole)

Nothing else was opened, listed or searched. `exam/`, `decisions/`, `LEDGER.md`,
`instructions/`, `notes/`, `canteen/`, `cards/`, `reports/`, `scripts/`, `data/`
were not touched, and no search was run that was not scoped to one of the four
files above. I have not seen any other juror's answer.

## Steers I saw in the instruction

Reported under RULES 3, without claiming they decided my answer:

1. **"What should happen to any list already produced is a separate question for
   a separate jury"** — this tells the juror that a list exists and that its fate
   is in doubt, which hints that the list came out wrong under one reading. That
   is context a blind juror did not need.
2. **"If the procedures it admits differ in how many moments they yield, say that
   too"** — conditional in form, but it pre-suggests both that more than one
   procedure may be admitted and that the live difference is a difference in
   *count*. It raises the salience of the answer before the file is opened.
3. **"this laboratory has learned that handing a juror an artefact built under
   one reading pulls toward that reading"** — good practice, correctly applied,
   but the sentence again signals that an artefact was built under one reading.

The instruction's opening discipline — "this instruction does not quote,
summarise or characterise any part of it" — was kept, and the question itself was
put neutrally.

## Assumptions the instruction did not cover

- I assumed "the section" means `TACTICS.md` section 2 in full, lines 33–44,
  including the calm-moment and moment-start lines, since they bear on the
  large-moment procedure.
- I assumed I could cite `RULES.md`, `README.md` and `TEAM.md` to show that the
  order is *not* settled elsewhere; the instruction permitted reading them.
- I assumed a year of the period is 365 days, from `TACTICS.md` section 0
  ("2025-09-01 → 2026-08-31"), in order to check 365 ÷ 20 against the 18-day
  figure. That arithmetic is stated, not measured from data.
