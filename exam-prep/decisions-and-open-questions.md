# Decisions I made, and questions I refused to answer

Mateo · data engineer · 2026-09-19 (system clock, RULES 23)

The instruction told me to solve two problems and said "You decide" what
"solved" has to mean. It did not cover everything the work needed. Everything
below is either a decision I took that the instruction did not cover, or a
question I did not answer because the rules say one person may not.

---

## A · Decisions I took

Each is a data-preparation decision. None of them is a trading rule, a
threshold in a score, or a change to a rule in `RULES.md`.

**D-1 · The recommended exam-card configuration is `strict-flags`, not
`ratio`.**
Both meet nothing by themselves; `strict-flags` closes the level channels *and*
the scale-free shape channel, `ratio` closes only the level channels (pair AUC
over everything removable: 0.505 against a 0.513 chance line, versus 0.573).
The cost is real and I state it: under `strict-flags` an exam candidate sees
**ranks, not multiples** — "this hour's volume was the 3rd smallest of the 24"
rather than "4.5× the median". Nothing in the frozen canteen book reads a
volume multiple; every idea that did was red-stamped. But Tomás, who sits the
exam on common sense with no recipe (RULES 11), loses material. **If the
laboratory would rather keep the multiples, `ratio` is built, audited and
ready, and its residual is measured.** This is the decision I am least sure of.

**D-2 · The bitcoin and ethereum columns are dropped from the blinded card.**
They fingerprint the clock hour exactly: they tie 243 of 495 truly overlapping
card pairs together with **zero** false positives in 46,170 non-overlapping
pairs. RULES 9 hides the date. TACTICS 3 puts the columns on the card and
TACTICS 6 does not list them as hidden, so this is an extension of TACTICS 6,
not an application of it. Nothing in the frozen canteen book reads them, and
every idea built on them was red-stamped (Viktor §5, A-10; Amara's own
before-window means of 1.76 against 1.73). **A reasonable person could say the
date is only "hidden" when it is not *printed as a date*, and keep the
columns.** That reading is one switch away (`--btceth keep`).

**D-3 · The Wikipedia and prediction-market lines are dropped entirely.**
Sofia's frozen book says "DROP THE FIELD" for both, for her own reasons. I add
a second: each also prints the coin. The prediction-market line on C001 reads
`Polymarket search over \`Broadcom • Robinhood Token\`, \`AVGO\``; the
Wikipedia `MISSING` reason on the NOK cards reads "CoinGecko returned no coin
whose symbol equals `NOK`". Scrubbing the words would have worked too; dropping
is what the frozen book already asked for.

**D-4 · The funding line is reduced to three yes/no facts.**
The three are exactly the three the frozen book asks a candidate for: B-5
(does the payment count match the stated interval), U-2 (did the interval
change), U-3 (is the whole window at one rate). No count, no interval, no rate,
no dispersion is printed. This is the narrowest rendering that does not break a
frozen blocker. It still leaks (pair AUC 0.573); the leak is the funding regime
itself and cannot be removed without deleting B-5 from a frozen book.

**D-5 · `chg%` is left exactly as it is.**
It is a coin fingerprint (pair AUC 0.543) and it is the only column the frozen
book's only surviving signal reads, at an absolute 5.00%. RULES 6 forbids
re-cutting a frozen rule. So the leak stays and is named rather than fixed.

**D-6 · Three decimals for a ratio, chosen by measurement.**
In the `ratio` configuration, rounding to 2 decimals fabricates a run of three
identical `depth` values — which is exactly the pattern blocker B-4 reads — on
**31** cards that did not have one. At 3 decimals: **0**. At 4: **0**. The
smallest number that fabricates nothing is 3. The count is re-measured on every
run and written into the blinding manifest.

**D-7 · `greedy-clique` is a stated convention.**
A set of overlapping time windows has no unique partition into "groups sharing
an hour". Some deterministic rule is needed to get a partition at all, and I
wrote one down — take the clock hour covered by the most still-unassigned
moments, ties to the earliest hour then the lowest card number — rather than
leaving the engine unable to offer that reading. It is labelled a convention in
the code, in the manifest and here. The alternative, `component`, is also
built.

**D-8 · The US release line is masked, not deleted.**
TACTICS 6 says the date in the release calendar is hidden, so the dates go and
the relative offsets in hours stay. Two things survived the first pass and are
masked rather than removed: a birth cohort in a series title ("those Born
1980-1984" → "those Born YYYY-YYYY") and quarter names without a year ("First
Quarter" → "<quarter>"). A bare "Annual" or "Biennial" is left alone: it is the
periodicity of the series, not a date. The script **stops** rather than writing
a card if a year, a month name or a quarter survives.

**D-9 · The synthetic answer vectors in the collapse calibration are
synthetic, and labelled so.**
I did not evaluate S-1, or any rule from the canteen book, on the observation
cards. Sofia's §4 item 2 asks for exactly that measurement, but it is Greta's
in Mode C, it is a result about a rule, and producing it in this run — before
the exam exists — is the kind of thing that contaminates an exam. The
calibration uses two coin-flip vectors drawn from seed `20260913` instead.

**D-10 · One output directory was deleted and rebuilt.**
`exam-prep/blind-proof/ratio` was written once with a literal `1%%` in the
order-book line. I deleted the directory, including its run record, and rebuilt
it rather than writing different content under an existing card file. Recorded
here so that it is not discovered later as a gap.

---

## B · Questions I did not answer, because RULES 33 says I may not

An open question is "a wording that can be read two ways, a gap an instruction
did not cover, a choice that changes the numbers", and it is never answered by
one person.

**Q-1 · Which reading of RULES 13's "in the same hour" governs a count?**
`start-hour` gives 289 events out of 306 cards; `card-span` gives 58. Full
statement, with every number a juror needs, in `exam-prep/N-1-collapse.md` §7.
Four parts: the reading, the resolution, the scope, and how an event is used in
the count.

**Q-2 · Is a printed column that identifies the clock hour a breach of
RULES 9's "the date is hidden"?**
I have acted as if it is (decision D-2), because I had to produce something
runnable. It is a reading of a rule and it changes what the card shows, so it
belongs to jurors, not to me. Both configurations exist.

**Q-3 · May two calm moments overlap each other?** Sofia referred this one
(her §8) and Ingrid before her. It bears on Q-1's scope part. Not answered
here either.

**Q-4 · May B-1, the tokenised-equity blocker, be applied inside the exam at
all?** Sofia ruled it out of the exam on her own reasoning and then recorded
that a different answer is a procedure question for three jurors. My work does
not change that: under the blinding, the funding interval is no longer printed,
so B-1 cannot be applied in the exam even by fingerprint. If a juror wanted it
applied, the blinding would have to be weakened on purpose.

**Q-5 · Should the `trades` column be printed at all?** Its tie structure
survives every blinding (pair AUC 0.529 against 0.513) because the card writer
rounds trade counts. Nothing in the frozen book reads it. Dropping it would
close the channel and would take a column off the card. That is a change to
what TACTICS 3 puts on a card, so it is not mine.

---

## C · A steer check on the instruction I was given

The instruction asked me to report a steer if I found one — a sentence telling
me what the answer is, what I would find, or which fix to choose.

**I found no result and no prediction in it.** Three sentences come closest and
I write them down rather than leave them unsaid:

1. "**Neither watcher, chair nor skeptic proposed a fix; they measured the
   problems and stopped, correctly. Fixing is yours.**" This says a fix exists
   to be found and calls the absence of one correct behaviour in others. It
   names no fix and points at no field. I do not treat it as a steer, but it is
   the nearest thing.
2. "**RULES 6 — whatever you fix, fix it before any exam card exists, not after
   a result.**" A pointer to a rule, i.e. scope.
3. "**Put in it whatever a later run needs in order to build a blind exam and
   to count events correctly.**" The phrase "count events correctly" presumes
   the counting is currently incorrect, which is what N-1 alleges. Since N-1 is
   the problem I was handed, the presumption is the problem statement rather
   than an answer to it — and my own measurement in
   `exam-prep/N-1-collapse.md` §6 does **not** support the strongest form of
   that allegation: cluster-level permutation on its own barely moves the
   chance line, and only the representative reading moves it a lot. I report
   the sentence because it leans one way and my measurement came out mixed.

Nothing in the instruction told me which fix to choose, and I was not told what
the other roles concluded beyond the two canteen files I was pointed at.
