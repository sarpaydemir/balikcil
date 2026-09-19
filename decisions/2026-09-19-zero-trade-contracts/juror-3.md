# Juror 3 — the zero-trade contracts

**Question:** should the 42 contracts that have 1d kline rows covering the
period but not one trade inside it be in the universe or not?

**Scope note (RULES 33):** I read this as a *definition* question — what the
written phrase "contract that traded during this period" means — which is what a
juror is allowed to settle. I set no threshold, no score and no trading rule,
and I propose no change to `RULES.md`.

---

## 1 · Answer

**No — the 42 do not belong in the universe; excluding them is what the
laboratory's own written definition says, and the universe of 795 is correct.**

---

## 2 · What it rests on

**`TACTICS.md` line 7** — the definition itself:

> `- **Universe:** every Binance USDT perpetual futures contract that traded during`
> `  this period.`

The operative word is **traded**. It is a verb about trades happening, not about
rows existing. Measured fact from `data/universe/excluded-no-trades.txt`: all 42
rows carry `total_trades_in_period,0` — 42 of 42, none with a nonzero value. A
contract with zero trades inside the period did not trade during this period, so
line 7 does not admit it.

**`TACTICS.md` line 9** — the sentence that says *why* the archive is used:

> `  from today's exchange, so that coins which died during the period are included`

The purpose of reading the archive instead of the live exchange is named
explicitly: to catch coins that **died during the period**. The 42 died *before*
it — their last trade is outside the window entirely. The archive clause is
there to widen the universe up to the period's edge, not past it. And that
intent is already honoured for the contracts that were kept: ten symbols in
`data/universe/universe.csv` have more than 300 zero-trade days inside the
period (e.g. `LEVERUSDT` with 362) and are still in the universe, because each
traded at least once inside it. So the kept set is exactly "died during the
period, included" and the excluded set is exactly "was already dead".

**`TACTICS.md` lines 40–41** — what including them would mean downstream:

> `  - For a coin that did not trade all year this count shrinks in proportion to`
> `    its lifetime: one moment per 18 days.`

The moment count is proportional to the coin's trading lifetime inside the
period. For these 42 that lifetime is zero days, so the rule yields zero
large-movement moments and, by TACTICS 2 ("the same number as the large
moments"), zero calm moments. A frozen price series cannot produce a moment, a
card, an exam question or a trade signal. Included, they would contribute
nothing at every later step.

**`TACTICS.md` line 17** — the one place they *would* change something:

> `  - **large / mid / small:** every other coin, ranked by its median daily`

Their median daily `quote_volume` is 0 by construction, so their entire effect on
the laboratory is to add 42 zero-volume entries at the bottom of the ranking and
thereby move both tertile cuts down (4344202.7566115 → 3934018.3418 and
1838834.05961 → 1556496.922371, per the instruction's table). That is: contracts
that cannot themselves produce a single observation would decide which *live*
contracts count as `large` rather than `mid`. Nothing in `TACTICS.md` asks for
that, and line 7 is what keeps it from happening.

**`scripts/03_build_universe.py` lines 74–76** — the implementation already
satisfies the honesty rules, which matters for how the exclusion was done, not
only whether:

> `# 365 rows in the period and has not traded once. Contracts excluded by this`
> `# line are written out by name to excluded-no-trades.txt, never dropped`
> `# silently (RULES 20, 22).`

RULES 22 (`RULES.md` line 76: "unresolved things are listed one by one, by
name") is met: the 42 are named in a file with their day counts and trade
counts, not quietly discarded.

---

## 3 · The strongest case against my own answer

The strongest case for including them has three legs, and I think it is a real
case, not a straw man.

**(a) The word "traded" is never defined, so somebody had to supply a number.**
`TACTICS.md` nowhere says how many trades make a contract "traded", and
`scripts/03_build_universe.py` line 77 writes `MIN_TRADES_IN_PERIOD = 1`. One
can argue that 1 is a number that appears in no laboratory document — and RULES
33 (`RULES.md` line 120: "never a threshold or score") says exactly this kind of
number is not an implementer's to choose. Under that reading the honest move is
the one that invents no number at all: take every contract the archive publishes
for the period, all 837, and let the group rules sort them out.

**(b) `TACTICS.md` line 9 can be read as sourcing, not filtering.** "The list is
built from the archive, not from today's exchange" can be read as: *membership is
archive presence for the period*, and "traded during this period" is a loose
description of why the archive is the right source rather than a test each
symbol must pass. All 42 have rows covering the period; 41 of them have all 365.
That reading needs no interpretation of what a `0` in `volume`, `quote_volume`
and `count` means.

**(c) Excluding requires interpreting the data.** The exclusion rests on the
claim that a frozen row with three zeros is a placeholder for a dead contract.
That is a reading of the data, and the laboratory's instinct is to avoid
readings.

**Why it does not move me.** On (a): "at least one trade" is not a threshold in
the RULES 33 sense — it is the minimum content the verb "traded" can carry, the
boundary between *some* and *none*. A tunable threshold would be a number that
could sensibly have been 5 or 100; this one cannot be anything but 1 without
becoming a judgement, and nobody proposed a different value. The gap the
instruction is worried about does not exist at 1. On (b): line 7's grammar puts
"that traded" as a restrictive clause on "contract", and line 9's stated purpose
("died **during** the period") draws the boundary at the same place; the two
sentences agree. On (c): no interpretation is needed — `count` is the archive's
own documented trade-count column and it reads 0 on every one of their days.
"Zero trades" is a measured fact, not a reading.

I also note, without leaning on it, that answering "exclude" is the answer that
keeps the pre-written text as written, which is the posture of RULES 6
(`RULES.md` line 34: "The rule is written first, the result is opened second").
I am deliberately giving no weight to the run in progress: cost is not an
argument, and if my reading had come out the other way I would have said so.

---

## 4 · Confidence and what would change my mind

**Confidence: 4 of 5.**

Not 5, because the word "traded" genuinely is undefined in `TACTICS.md` and leg
(a) above is a fair objection about who gets to supply the missing number.

What would change my mind, concretely:

1. **A documented meaning of `count` other than "number of trades"** — if the
   Binance archive's own documentation shows a 0 in `count` can coexist with real
   trades, the measurement under the exclusion is wrong and the 42 must come back
   in pending a correct measurement.
2. **Any one of the 42 showing a nonzero trade day inside the period.** I checked
   all 42 rows of `data/universe/excluded-no-trades.txt`: 0 of 42 have a nonzero
   `total_trades_in_period`. If a re-measurement finds even one, that contract
   belongs in the universe by line 7 and my answer changes for it.
3. **A written line making universe membership archive presence** — a sentence in
   `TACTICS.md` or `RULES.md` saying membership is "has rows in the period"
   rather than "traded in the period" would settle it against me immediately.
4. **A demonstration that the group cuts are meant to be computed over the
   archive rather than over traded contracts** — if `TACTICS.md` line 17's "every
   other coin" is shown to mean every archived contract, the ranking argument in
   part 2 falls.

What would *not* change my mind: the size of the re-run, or which contracts the
draw happens to land on under either answer.

---

## 5 · Steers I am obliged to report (RULES 3)

`RULES.md` line 15–16: "Agents are not told what to look for... An instruction
contains no result, no prediction, and no 'pay attention to X' steer." Three
things in my instruction sit against that line. I flag them; I do not claim they
changed my answer.

1. **The instruction states the decision already taken:** "Those 42 contracts
   were **excluded** ... and the draw was made from the 795 that remain." The
   stated reason for closing `LEDGER.md` to me was that "a juror who reads the
   answer before answering is not a juror" — but the answer arrived in the
   instruction itself. This is the most serious of the three, because the
   closure was rendered ineffective.
2. **The instruction contains computed results:** universe sizes, group sizes and
   both pairs of cut values for both options. These are results within RULES 3's
   plain meaning, even though both columns were given even-handedly.
3. **An asymmetric sentence about cost:** "A run is currently in progress that
   depends on the present answer... If your answer is that the 42 belong in the
   universe, say so." The disclaimer is explicit and I credit it, but only one of
   the two answers is named as the costly one, which makes the framing asymmetric
   even where the numbers are not.
