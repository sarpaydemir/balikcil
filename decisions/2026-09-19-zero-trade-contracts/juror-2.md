# Juror 2 — the zero-trade contracts

**Question:** should the 42 contracts whose in-period kline rows are frozen
placeholders (price unchanged, `volume`, `quote_volume`, `count` all `0`, not one
trade inside 2025-09-01 → 2026-08-31) be in the universe or not?

**Scope note (RULES 33):** I answer only the definition — what the written
universe sentence means. I decide no trading rule, no threshold, no score, and I
propose no change to `RULES.md`.

---

## 1 · Answer, in one sentence

**No — the 42 belong outside the universe; excluding them is what the
laboratory's own universe sentence says, and the draw made from the 795 stands.**

---

## 2 · What it rests on — file and line, quoted

**a. The defining sentence is about trading, not about listing.**

`TACTICS.md`, lines 7–8:

> - **Universe:** every Binance USDT perpetual futures contract that traded during
>   this period.

The 42 have zero trades inside the period — the fact is recorded by name in
`data/universe/excluded-no-trades.txt`, lines 7–48, every row ending in a
`total_trades_in_period` of `0`, e.g. line 11:

> `BALUSDT,365,0,2020-09-01,2026-08-31`

A contract that made no trade in the period did not trade during the period. On
the plain reading of the defining sentence it is not in the universe.

**b. The "coins which died" clause does not rescue them; it is already
honoured.**

`TACTICS.md`, lines 8–10:

> The list is built from the archive (`data.binance.vision`), not
>   from today's exchange, so that coins which died during the period are included
>   too.

This clause protects coins that died **during** the period — they traded, then
stopped. It is satisfied by the current build, not violated by it:
`data/universe/universe.csv` keeps 46 contracts whose median daily volume over
the period is `0.0` precisely because they died mid-period, e.g. line 445:

> `MKRUSDT,2020-08-13,2025-09-08,365,0.0,small,2025-09-01,2026-08-31,2025-09-01,357,8,2915883,459,2026-08,`

— 8 trading days, 357 zero-trade days, 2.9 million trades, kept, ranked `small`.
The 42 are not coins that died during the period; every one of them was already
dead when the period opened (`last_day_with_trades_in_period` does not exist for
them at all). The kept set proves the clause bites where it was meant to bite,
and the exclusion does not touch it.

**c. Including them would put contracts into the draw that the later steps
cannot process at all.**

`TACTICS.md`, line 41 (moments):

> - For a coin that did not trade all year this count shrinks in proportion to
>     its lifetime: one moment per 18 days.

A contract with zero in-period lifetime yields zero moments, therefore zero
cards, therefore nothing for a watcher, the exam or the score recipe to be
applied to. And `RULES.md`, lines 62–63:

> 16. Entry happens at the first real price after the signal. At a moment known in
>     advance (a payment time, an announcement time) the candle's open price does
>     not count as the fill price, because nobody could buy at it.

The frozen placeholder price is the paradigm case of a price nobody could buy
at. A money-test contract drawn from the 42 could never be entered under RULES
16. Reading the universe sentence so that it admits them would hand the draw
members that TACTICS 2, TACTICS 3, TACTICS 6 and RULES 16 each independently
cannot use.

**d. The exclusion was performed in the honest form the rules require.**

`RULES.md`, lines 76–77:

> 22. In the report, unresolved things are listed one by one, by name. "Could not
>     be measured" never turns into "no problem".

The 42 are written out by name with their day counts and trade counts
(`data/universe/excluded-no-trades.txt`), and `scripts/03_build_universe.py`
lines 263–267 write that header deliberately. This does not by itself decide the
question, but it means the choice was made in the open and is reversible; nothing
was dropped silently.

---

## 3 · The strongest case against my own answer

The strongest case for **including** them is textual, and it is not weak:

1. `TACTICS.md` line 8 says the list is **"built from the archive … not from
   today's exchange."** One can read the whole sentence as: the archive's own
   in-period coverage *is* the membership test, and "traded during this period"
   is loose prose for "was a live contract in the archive during this period."
   On that reading, filtering by trade count adds a criterion nobody wrote down.

2. `scripts/03_build_universe.py` line 77 introduces
   `MIN_TRADES_IN_PERIOD = 1`. The script argues at length (lines 62–76) that
   this is the instruction's sentence written as code and not a tuning
   parameter — but it is still a number that appears in no document TACTICS or
   RULES contains, and it moved both tertile cuts and therefore the draw. RULES
   6 ("the rule is written first, the result is opened second") is exactly about
   choices of this kind being made where they cannot be re-chosen later.

3. The same script's docstring, lines 21–23, records that two TACTICS 1 wording
   points "were resolved by the coordinator in this run's instruction." That is
   the pattern RULES 33 now forbids — "least of all by the coordinator alone" —
   and it invites the suspicion that this third resolution came from the same
   place. A juror should weigh the answer, not its author; I note it and set it
   aside, but it is the honest reason to distrust the status quo here.

4. Inclusion is cheap in one respect: a contract that can produce no moment
   would simply produce no card, so the harm my point (c) describes is partly
   self-limiting. The real cost of inclusion is the shifted cuts (4344202.76 →
   3934018.34 and 1838834.06 → 1556496.92), i.e. reshuffled group membership —
   a cost the instruction states as measured fact.

Why it still does not persuade me: reading 2 requires "traded" to mean something
other than traded, while the kept 46 mid-period deaths show the laboratory's own
implementation already distinguishes *died during* from *dead before* — and only
the second is at issue. Objection 3 is a reason to check the answer, which is
what three jurors are for, not a reason to flip it.

---

## 4 · Confidence and what would change my mind

**Confidence: 4 / 5.**

It would change my mind if:

- any document open to me defined the universe by listing status or by archive
  coverage rather than by trading — I found none in `RULES.md`, `TACTICS.md`,
  `README.md` or `TEAM.md`;
- the `count` column were shown to be unreliable for these contracts, i.e. the
  42 did trade in the period and the archive merely fails to say so. That is a
  data-quality claim, checkable against the 1d rows, and it would dissolve the
  question rather than answer it;
- the laboratory ruled that "at least one trade" is a **threshold** rather than
  the meaning of the word "traded". If it is a threshold, no juror may set it
  (RULES 33, `TEAM.md` line 116) and it must be settled by whoever may. My
  answer is the reading of the word, not the setting of a number.

---

## 5 · Leak check on my instruction (RULES 3)

Two items I report rather than rule on, neither of which changed my answer:

- The instruction states **"A run is currently in progress that depends on the
  present answer."** It disclaims itself in the next sentence, but it is
  one-directional cost pressure toward the status quo and would have been safer
  omitted.
- The instruction supplies the two group-cut values for **both** branches. These
  are results of the universe build (not of the exam or of any test), and they
  are given symmetrically for both readings, so I do not treat them as a steer —
  but they are numbers a juror did not need in order to read a sentence.

No "pay attention to X" sentence was present. `exam/`, `LEDGER.md`,
`instructions/`, `notes/`, `canteen/`, `cards/` and `reports/` were not opened,
and nothing outside `/home/user/balikcil` was read.
