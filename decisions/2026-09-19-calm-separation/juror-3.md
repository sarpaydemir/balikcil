# Juror 3 — TACTICS 2 and the separation of calm moments

**Question:** under `TACTICS.md` section 2, is there a minimum distance required
between two calm moments belonging to the same coin?

---

## 1 · Answer

**No — section 2 requires no minimum distance between two calm moments of the
same coin:** the 48-hour rule is written inside the *large-movement* definition
and its test ("only the larger counts") has no operand for calm moments, whose
only stated distance constraint is 72 hours away from a large movement.

This is not the same as "the section is silent and therefore anything goes". The
section is silent on calm-to-calm spacing, and under this laboratory's own
discipline a selection constraint that is not written is not in force
(`RULES.md` 6, quoted in part 2). Silence here yields "no requirement", not "the
question is undecidable".

## 2 · What it rests on

### a) The structure of `TACTICS.md` section 2 (lines 33–44)

The 48-hour rule is a sub-bullet of **Large-movement moment**, not a statement
of the section. Quoting the section verbatim, indentation included:

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

Three things follow from the layout:

1. The 48-hour line (`TACTICS.md` line 39) sits at the same indent level as
   "The largest 20 of the year are taken for each coin" (line 38) and the
   pro-rata line (lines 40–41). All three are procedure for building the
   large-movement list. The calm definition begins at the outer indent (line 42)
   and carries its own — single — constraint.
2. The calm definition states exactly one distance requirement: *"At least 72
   hours away from any large movement."* (`TACTICS.md` line 43). It states a
   count ("the same number as the large moments") and a selection method
   ("chosen at random"). It states no calm-to-calm distance.
3. The section does know how to speak about both kinds at once — line 44, *"A
   moment's start is the hour at which the 24-hour movement began"*, is written
   at the outer level, after both definitions. The 48-hour line was not written
   there.

### b) "Only the larger counts" cannot be evaluated for calm moments

`TACTICS.md` line 39: *"Of two moments closer than 48 hours to each other, only
the larger counts."* The rule is not a spacing rule with a separate remedy; the
remedy **is** the rule, and it resolves a conflict by magnitude. Large moments
are magnitude-ranked by construction — line 37, *"the places where the coin rose
or fell the most within 24 hours"*, and line 38, *"The largest 20 of the year"*.
Calm moments are *"chosen at random"* (line 42); a calm moment has no size that
makes it the one that "counts", and picking the larger of two calm moments would
be selecting calm moments by movement size, which contradicts their own
definition.

The laboratory's own artefact shows the same structure. `data/moments/moments.csv`
header and rows (lines 1, 4, 2):

```
moment_id,symbol,kind,start_hour_utc,start_ms,move_24h_pct,rank_in_coin
AVGOUSDT-L-20260601T1000,AVGOUSDT,large,2026-06-01T10:00Z,1780308000000,7.7153,6
AVGOUSDT-C-20260507T2000,AVGOUSDT,calm,2026-05-07T20:00Z,1778184000000,4.1945,
```

`rank_in_coin` is filled for `large` and empty for `calm`. I cite this only to
show that the magnitude ordering the 48-hour test needs exists for one kind and
not for the other — not as evidence of what the rule means.

### c) A cross-kind reading of line 39 would be redundant

If line 39 were read as covering every pair of moments regardless of kind, its
calm-versus-large half would be swallowed by the stricter line 43 (72 hours ≥ 48
hours). A rule whose cross-kind half is dead on arrival is more naturally read as
intra-list, which is where it is written.

### d) Adding the requirement now would be a new rule, not a reading

`RULES.md` 6: *"The rule is written first, the result is opened second. A rule is
not changed after looking at a result. If it is changed it counts as a new rule,
carries the 'afterwards' label, and is tested again."* A moment list already
exists. Reading an unwritten separation into section 2 at this point is
rule-writing after the result, and `RULES.md` 33 puts it outside a juror's
authority in any case: *"A juror decides procedure and definition only: never a
trading rule, never a threshold or score, and never a change to a rule in this
file."* I therefore say what the section requires and stop.

### e) Reversibility

My answer is the **reversible** one, in this precise sense: it adds no
constraint and forecloses nothing. If the laboratory later decides — as a
written rule change, with the user asked (`RULES.md` lines 3–4) — that calm
moments need spacing, that is a re-selection of calm moments and a re-write of
their cards, i.e. re-running the moment script and the card script for the calm
half of the 10 observation coins (`TACTICS.md` 3 and `README.md` step 2: *"A
script does this, not an AI"*). The **irreversible** direction is the other one:
ruling that the section already requires 48 hours would retroactively invalidate
part of an existing measured artefact and, if any note or card were later built
on it, would pull work that has not been done into scope. I do not propose what
should happen to moments already selected; the instruction places that with
another jury and I keep to that.

## 3 · The strongest case against my own answer

The strongest opposing case is not textual pedantry, it is purpose, and it is
real:

1. **"Moments" on line 39 is unqualified, and the section is titled "Moments".**
   The drafter wrote "moments", not "large-movement moments", inside a section
   that defines two kinds. Elsewhere the laboratory uses "moment" as a
   kind-neutral word: `RULES.md` 13, *"Moments occurring in several coins in the
   same hour count as a single event"*, and `TACTICS.md` line 127, *"A moment
   appearing in several cards in the same hour counts as a single event."*
   Indentation is weak evidence of intent in a document written by hand.
2. **The purpose of a 48-hour gap applies to calm moments with equal force.** A
   moment is a 24-hour window (line 44), and a card shows *"the 24 hours before
   the start"* (`TACTICS.md` line 50). Two calm moments 14 hours apart — which
   the existing file contains, e.g. `AVGOUSDT-C-20260716T0000` and
   `AVGOUSDT-C-20260716T1400` (`data/moments/moments.csv` lines 11–12) — produce
   two cards whose windows overlap by ten of twenty-four hours. Near-duplicate
   evidence is exactly what `RULES.md` 13 and `TACTICS.md` line 127 exist to
   prevent, and what `TACTICS.md` line 131 ("the boundary of the best 1%") relies
   on not being present. On this reading, "only the larger counts" is simply the
   tie-break that happens to be available for large moments, and the obvious
   analogue for a randomly drawn calm moment is to draw again.
3. **The calm definition already borrows from the large one.** *"the same number
   as the large moments"* (line 42) shows the drafter expected the calm rule to
   inherit from the large rule rather than restate it. One could argue the
   selection hygiene is inherited the same way the count is.

What I weigh against this: the borrowing on line 42 is explicit and names exactly
one thing it borrows — the number. The counter-reading requires supplying a
remedy the text never supplies (re-draw, or drop the later one, or drop the one
nearer a large movement), and choosing among those is inventing procedure, not
reading it. It also has to explain why the 72-hour line was written into the calm
definition if calm moments were already governed by the large definition's
sub-bullets. I judge the structural reading stronger, but I do not think the
opposing case is unreasonable, and a referee should see that I do not.

## 4 · Confidence

**4 of 5.**

What would change my mind:

- A line anywhere in `TACTICS.md` or `RULES.md` that applies the 48-hour test to
  calm moments, or that defines "moment" as kind-neutral *for selection*. I read
  the whole of `RULES.md`, `TACTICS.md`, `README.md` and `TEAM.md` and found
  none; the nearest kind-neutral uses (`RULES.md` 13, `TACTICS.md` line 127) are
  about double-counting at scoring time, not about building the moment list.
- Evidence that the indentation of lines 38–41 is an artefact of the
  2026-09-18 translation from `KURALLAR.md`/the Turkish original rather than the
  drafter's intent (`RULES.md` lines 137–142 record that a translation happened;
  the note covers `RULES.md`, and I cannot tell from `TACTICS.md` itself whether
  it was translated too).
- A founding record of intent. `LEDGER.md` is closed to me by this instruction,
  and it is the one place such a record would live (`README.md` line 65:
  *"`LEDGER.md` — what happened when; append-only, no line is ever deleted"*).
  I name this as unmeasured, per `RULES.md` 22.

What would *not* change my mind: the number of short-gap pairs in the existing
file, in either direction. I reached this answer from the section's structure
before treating the file as anything more than an illustration.

---

## Files read

- `/home/user/balikcil/RULES.md` (whole)
- `/home/user/balikcil/TACTICS.md` (whole)
- `/home/user/balikcil/README.md` (whole)
- `/home/user/balikcil/TEAM.md` (whole)
- `/home/user/balikcil/data/moments/moments.csv` (lines 1–12 only)

Nothing else was opened. `exam/`, `decisions/` (including the other files in the
folder this answer is written to), `LEDGER.md`, `instructions/`, `notes/`,
`canteen/`, `cards/`, `reports/`, `scripts/` and the rest of `data/` were not
read, listed or searched, and no search was run that was not scoped to a named
file above.

## Assumptions I had to make, by name

1. **That `TACTICS.md` line 39's indentation is the drafter's and not a
   formatting accident.** I could not verify this without `LEDGER.md` or version
   history, both outside my scope. Named in part 4.
2. **That "distance" in the question means time between the two moments' starts**
   (the field `start_hour_utc` / `start_ms`), since `TACTICS.md` line 44 defines a
   moment by its start hour. The instruction did not define it.
3. **That the question asks what section 2 requires *as written today***, not
   what it ought to require.

## Steer check

Two things to report, neither disqualifying in my judgement but both worth the
referee's eye:

1. **The instruction's "measured" block contains results.** `RULES.md` 3:
   *"Agents are not told what to look for, only what they may look at. An
   instruction contains no result, no prediction, and no 'pay attention to X'
   steer."* The block gives me 20 and 21 measured pair counts from a file I was
   also allowed to read. The instruction labels them as measured and states they
   bear on neither answer, which is the right handling — but they are still
   results delivered in an instruction.
2. **One sentence of the instruction is inaccurate, and it leans one way.** The
   instruction says *"neither has been implemented in preference to the other in
   anything you may read."* `data/moments/moments.csv` — the one data file I was
   told I may read — is an implementation of the no-separation reading: it
   contains calm pairs of the same coin hours apart (lines 11–12 above). Being
   handed the existing artefact plus the count of pairs it would lose creates a
   status-quo pull toward my own answer. I note it precisely because it points
   the way I went; the referee should weigh my part 3 accordingly.

A third, smaller point: the closing line *"Six such faults have been found in
this laboratory's instructions so far, every one by the agent receiving them"*
is an expectation that I will find a seventh. That is mild pressure toward
manufacturing a fault. I have tried to report only what I can quote.

I saw no other juror's answer and made no attempt to locate one.
