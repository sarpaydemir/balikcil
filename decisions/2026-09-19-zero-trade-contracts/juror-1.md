# Juror 1 — the zero-trade contracts

**Question:** should the 42 contracts that have 1d kline rows covering the
period but not one trade inside it be in the universe or not?

**Date:** 2026-09-19 · **Juror:** 1 of 3 (RULES 33) · answered without seeing
any other juror's answer, and with `LEDGER.md`, `instructions/` and `exam/`
unopened.

---

## 1 · The answer, in one sentence

**No — the 42 do not belong in the universe:** `TACTICS.md` defines the
universe as the contracts *that traded* during the period, and a contract with
zero trades inside the period did not trade during it, so the exclusion that
was made is what the written documents say.

---

## 2 · What it rests on

### The defining sentence

`TACTICS.md`, lines 7–8:

> - **Universe:** every Binance USDT perpetual futures contract that traded
>   during this period.

The verb is "traded" and its object is "during this period". The 42 have, by
measurement, zero trades during this period —
`data/universe/excluded-no-trades.txt`, line 6 onward, column
`total_trades_in_period` reads `0` on all 42 rows (41 of them alongside
`days_with_data = 365`, `BTCSTUSDT` alongside `303`). A row whose `volume`,
`quote_volume` and `count` are all `0` is not a trade; it is the archive
continuing to publish.

### The sentence that is offered as the counter-reading, read in full

`TACTICS.md`, lines 8–10:

> The list is built from the archive (`data.binance.vision`), not from today's
> exchange, so that coins which died during the period are included too.

This sentence carries its own purpose clause, and the purpose is narrow: it
exists so that **coins which died during the period** are not lost. A coin that
died *during* the period traded during the period — its death is an event
inside our window and we want it. The 42 died **before** 2025-09-01: all 42
have `total_trades_in_period = 0`, so their last trade is earlier than the
period's first day. Including them does not serve the purpose this sentence
states; it goes past it. The clause is an instruction to use the archive as the
*source*, not a definition of membership — the definition is the sentence
above it.

That the laboratory already honours the "died during the period" purpose is
measurable in the kept list: `data/universe/universe.csv` line 401,

> `LEVERUSDT,2023-03-30,2025-09-03,365,0.0,small,2025-09-01,2026-08-31,2025-09-01,362,3,1342826,457,2026-08,`

— a contract with 362 zero-trade days and 3 trading days inside the period,
**kept**. The dead-during-the-period case is in. Only the dead-before case is
out.

### What the rest of the tactics do with such a contract

`TACTICS.md`, line 36:

> - **Large-movement moment:** the places where the coin rose or fell the most
>   within 24 hours.

and line 41:

> - For a coin that did not trade all year this count shrinks in proportion to
>   its lifetime: one moment per 18 days.

A frozen contract's price is constant for all 365 rows, so every 24-hour
movement is exactly 0 and its lifetime inside the period is 0 days: it yields
zero large moments, and since the calm moments are "the same number as the
large moments" (`TACTICS.md`, line 43), zero calm moments too. It therefore
yields zero cards, and `TACTICS.md` line 49 — "**One page per moment**" —
has nothing to write. Admitting these 42 would put into the draw contracts that
cannot produce a single card for observation, a single exam card, or a single
money-test trade.

That is not hypothetical. With the 42 in, the small group is 175
(instruction's table, stated as computed), and all 42 have median daily
`quote_volume` exactly `0.0`, the lowest value the ranking in `TACTICS.md`
lines 17–19 can take —

> **large / mid / small:** every other coin, ranked by its median daily
> trading volume (`quote_volume`) over the period

— so all 42 land inside the bottom group. `universe.csv` already contains **46**
kept contracts whose `median_daily_quote_volume` is exactly `0.0` (measured:
46 matching rows out of the 795 in `data/universe/universe.csv`); with the 42
added, 88 of the 175 small contracts would have a median of exactly zero and 42
of those 88 would be untestable. Under a uniform draw without replacement from
the small group, the chance that the **observation** draw's 2 small coins
include at least one of the 42 is 42.3%, and that the **exam** draw's 4 small
coins include at least one is 67.0% (both computed from 42 and 175, under that
stated assumption). A roughly-two-in-three chance of handing Nadia a frozen
contract is what the inclusive reading buys.

### The honesty requirement is already met by the exclusion

`RULES.md`, lines 76–77 (RULES 22):

> In the report, unresolved things are listed one by one, by name. "Could not
> be measured" never turns into "no problem".

The 42 are written out by name with their day and trade counts in
`data/universe/excluded-no-trades.txt`. So the exclusion is not a silent drop,
which is the failure mode RULES 20 and 22 exist to prevent.

### Scope check (RULES 33)

`RULES.md`, lines 119–121:

> A juror decides procedure and definition only: never a trading rule, never a
> threshold or score, and never a change to a rule in this file.

What I am deciding is a definition: what "that traded during this period"
means. I am **not** setting a minimum-activity threshold. If anyone reads this
answer as authority for a floor above zero — "at least 30 trading days", "at
least X in volume" — that is a threshold, it is outside a juror's scope, and
this answer does not supply it. The only line I am reading is the one between
"traded" and "did not trade", and that line is in the sentence itself, not in
my judgement.

---

## 3 · The strongest case against my own answer

**The bright line I am endorsing is written in code as a number, and numbers
are not mine to set.** `scripts/03_build_universe.py`, line 77, reads
`MIN_TRADES_IN_PERIOD = 1`. The file argues at lines 70–76 that this is not a
tuning threshold but the sentence written as code. That argument is good but
not airtight: the difference between `LEVERUSDT` (3 trading days out of 365,
kept) and any of the 42 (0 trading days, dropped) is a difference of three days
of trading, and both contracts are equally incapable of yielding the 20 large
moments `TACTICS.md` line 38 asks for. If the real reason to drop the 42 is
"nothing can be measured on them", then that reason applies to a stretch of
the kept list too, and drawing the line exactly at 1 is arbitrary in substance
even if it is exact in wording. A juror who holds that "the documents do not
settle it, so nothing should be cut" would keep all 837 and let the moment
scripts produce whatever they produce — that reading never has to pick a
number at all, and picking no number is safer than picking one. It is also the
reading that protects best against survivorship-flavoured selection: we are,
after all, removing exactly the deadest contracts in the archive from a study
about what happens before coins move.

My reasons for not taking that reading, stated so they can be attacked: (a)
`TACTICS.md` line 7 does contain a verb, and refusing to give "traded" any
content is not neutrality, it is a different definition; (b) the inclusive
reading does not actually avoid a number — it silently sets the minimum to
zero, and zero is also a choice; (c) the 42 are not merely sparse, they are
outside the period entirely, since their last trade predates 2025-09-01, and a
period-scoped universe that admits contracts whose whole life is outside the
period has stopped scoping by period.

A second, weaker objection I want on the record: the inclusive reading changes
the two cuts (4344202.7566115 → 3934018.3418 and 1838834.05961 → 1556496.922371,
the instruction's computed figures), which moves genuinely-traded contracts
between `large`, `mid` and `small`. Whichever way this is answered, some real
contract changes group for a reason that has nothing to do with itself. That
is a cost of the exclusive reading too, not only of the inclusive one, and I do
not pretend otherwise; I judge it smaller than seating untestable contracts in
the draw, but that is a judgement.

---

## 4 · Confidence, and what would change my mind

**Confidence: 4 of 5.**

Four and not five because the case against in part 3 is real: the line at
"one trade" is exact in wording but coarse in substance, and I cannot fully
separate my reading of `TACTICS.md` line 7 from the fact that the
implementation files I was permitted to read (see the leak note below) already
argue for it.

What would change my mind, concretely:

1. **A trade.** If any of the 42 is shown to have a non-zero `count` on any day
   inside 2025-09-01 → 2026-08-31, that contract traded during the period and
   belongs in the universe under the same sentence I am citing. Right now
   `excluded-no-trades.txt` reports `0` for all 42.
2. **A card from a frozen contract.** If the moment-finding script can produce
   even one usable large-movement moment from constant-price, zero-volume rows,
   my functional argument collapses and only the wording is left.
3. **A second definitional sentence.** If a document open to me were shown to
   define the universe a second time in terms of *rows in the archive* rather
   than *trading*, `TACTICS.md` line 7 would no longer be the only definition
   and the question would be genuinely two-sided on the text.
4. **A downstream rule that needs them.** If any step in `TACTICS.md` 2–8
   required the full archive list — a delisting study, a survivorship control —
   then dropping the 42 would remove data a later step consumes. I found no such
   step; `TACTICS.md` 2–8 all operate on price, volume and moments, which these
   contracts do not have.

What would **not** change my mind: that a run is in progress and reversal is
expensive. `RULES.md` lines 34–35 (RULES 6) — "The rule is written first, the
result is opened second. A rule is not changed after looking at a result." —
means the direction of travel of the current run has no standing in a question
about what the rule says. I would have written the same answer if the reversal
cost were zero, and I would have written "include them" if the text had said so
while a run was mid-flight.

---

## Leak notes (reported as required, not as a complaint)

Three things in this task carried information toward an answer. I report them
so the referee can weigh my independence honestly.

1. **The implementation files state the coordinator's conclusion and its
   reasoning.** `data/universe/excluded-no-trades.txt`, lines 3–5: "Excluded
   from the universe because the instruction and TACTICS 0 both say 'contracts
   that TRADED'." And `scripts/03_build_universe.py`, lines 70–76, argues the
   same case at length. `LEDGER.md` and `instructions/` were closed to me to
   keep the coordinator's answer out of my head, but these two permitted files
   contain that answer and its argument in plain text. I read
   `TACTICS.md` first, before either of them, but I cannot claim I reached my
   reading untouched — I can only say that part 2's argument from lines 8–10
   (the purpose clause) and part 2's argument from moments and cards are mine
   and appear in neither file.
2. **`scripts/03_build_universe.py`, lines 21–29** records that two other
   TACTICS 1 ambiguities "were resolved by the coordinator in this run's
   instruction". That is a second window onto closed material, and it shows
   the coordinator resolving open questions alone before RULES 33 existed.
   Not my question, but it is visible from where I sit.
3. **The instruction mentions that a run is in progress and depends on this
   answer.** It disclaims the pressure in the same paragraph and explicitly
   invites the opposite answer, which is the right way to do it, but a juror
   who is told the cost of one answer has been told something. It did not move
   me; I note it because a jury that was steered is not a jury and the user
   should be able to see the steer and judge for themselves.
