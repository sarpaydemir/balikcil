# JQ-R04-GATE · juror 1

Juror 1 of at least three. Written 2026-10-01 without seeing any other juror's
answer. I did not open or list any other file in this folder.

## 1 · Answer

**C: the gate fails if either attack, nearest neighbour or pair AUC, beats its
own RULES 12 chance line on the `ALL-removable` row of the exam cards.** The
cards count as blind only if neither attack beats its line.

There is one subsidiary point. I hold it with lower confidence (see part 4), and
it is separate from the main answer so the split can be counted cleanly. Where
the two versions of the nearest-neighbour score differ on the exam cards, the
**tie-averaged version** should be read against its own line. The
lower-card-number tie-break measures partly how the cards are numbered, and that
is not what the gate claims to test.

**Optional second part:** this does not bear on my answer, and the rules I may
read do not settle it. I give no answer to it (reason in 2e).

**Rule change:** none. This answer reads a step written in an exam-prep file. It
changes nothing in `RULES.md` and sets no threshold, score or chance line. Both
lines are the RULES 12 lines the audit already computes. No number is mine.

## 2 · What it rests on

**(a) What the gate exists to check.** The rule it protects is `RULES.md` line 41:

> "9. In the exam the coin name and the date are hidden."

The step's own sentence (question file lines 55–57) defines failure as a
property of the cards:

> "If `ALL-removable` beats its chance line on the exam cards, the cards are not
> blind and the gate has failed."

The question file lines 82–87 describe the two attacks as two separate ways of
recovering the coin. Nearest neighbour asks "*can a card be matched to its own
coin?*" and pair AUC asks "*does similarity carry coin information on average?*"
Each one, if it beats its line, shows that coin identity can be recovered from
what is printed on the card. If either shows that, the coin name is not "hidden"
in the sense of RULES 9, and so "the cards are not blind". Under D, a card set
on which cards can be matched to their own coin far beyond chance would still
pass, just because the average over all pairs did not move. A card set that has
been shown to give up its coin cannot be called blind. A and B each throw away
an attack the step's author had written into the audit. The step names no
attack, so neither A nor B is the narrower reading. Each is an unexplained
choice of one instrument.

**(b) The burden is on blindness, not on the attack.** The gate is a check
that must be passed "before the answer key is sealed" (question file line 54).
That is the moment `RULES.md` lines 41–42 and `TACTICS.md` lines 108–109 fix:

> "The answer key is sealed before the exam: its fingerprint is written into
> `LEDGER.md`." (RULES 9)

The section that RULES 9 sits in is headed `RULES.md` line 32: "## B · Not
deceiving ourselves". The gate's job is to stop the laboratory from deceiving
itself that the exam is blind. Evidence of a leak from either instrument is
evidence against that claim. For blindness to be declared, it has to survive
every attack the laboratory has written.

**(c) Which error can be undone.** A failed gate happens before sealing. The
cards can be re-blinded and the audit re-run. That costs engineering work but
loses no data (cost not measured; estimate: one audit run per re-blinded
version, the same kind of run as the five in the question's table). A wrongly
passed gate cannot be undone once the exam has been sat. The exam coins are a
fixed draw:

> "**Draw number:** `20260913`. Written before the draw; it does not change."
> (`TACTICS.md` line 22)
> "**Exam:** a different 20 coins (6 · 6 · 4 · 4)" (`TACTICS.md` line 24)

An exam sat on leaky cards burns those 20 coins, because no second set of
unseen exam coins is provided for. C puts the burden on the side that can be
reversed. D puts it on the side that cannot. This is reasoning from written
rules, not a rule written anywhere. I mark it as inference.

**(d) The list is incomplete, which argues against weakening.** The question
file lines 69–75 say:

> "It is **not** 'everything about a card that could identify its coin' …
> Nothing guarantees that no other channel exists outside the list."

The gate can already miss channels that are outside the list. That is a
limitation, and it is recorded (RULES 22, `RULES.md` lines 76–77: "'Could not be
measured' never turns into 'no problem'"). Reading the gate as D would add a
second, avoidable way of missing a leak on top of the one that cannot be
avoided. (I flag this passage as a possible steer in part 6. It still states a
fact the reader needs.)

**(e) Why the nearest-neighbour score should be read in its tie-averaged
version (subsidiary).** The question file lines 89–93 say:

> "when two other cards are **exactly** equally similar to a card, the audit
> picks the one with the lower card number, so where that happens the score
> depends on how the cards are numbered."

The gate's claim is about card content: "the cards are not blind". A pass or
fail that changes when the same cards are renumbered is not a property of the
cards. The tie-averaged version, "does not depend on the numbering, with its own
chance line" (lines 93–94), measures what the sentence claims. This sets no
number, because both versions and both lines already exist.

**(f) Why I leave the second part open.** RULES 13 (`RULES.md` lines 53–54)
reads: "Moments occurring in several coins in the same hour count as a single
event." `TACTICS.md` line 127 places it under §7 Scoring: "A moment appearing in
several cards in the same hour counts as a single event." Both are about
counting results as events. Neither says what an identity audit may match.
Whether two cards of one coin that share printed hours should count as a leak
depends on whether a candidate sees both cards together. The files I may read
do not say that. My answer to part 1 is the same whichever way this goes. Under
C, the forbidden-overlap version would be a third reading of the
nearest-neighbour attack, and choosing between them is a separate open question.
It should not be absorbed into this one.

**Earlier verdicts.** I read all seven `decisions/2026-09-19-*/verdict.md`.
None of them settles this question. The nearest in kind is
`decisions/2026-09-19-card-order-requirement/verdict.md`, which ratified that a
juror does not set a number ("RULES 33 forbids a juror to set one"). My answer
keeps to that.

## 3 · The strongest case against my answer

**(i) C loosens the RULES 12 line without saying so.** RULES 12 (`RULES.md`
lines 51–52): "the real result must fall inside the best 1%." Two tests, each
at 1%, with failure if either one beats its line: on perfectly blind cards the
gate would wrongly fail more often than 1%. The bound is 2% (estimate: a union
bound, lower to the extent the two attacks are correlated). So C in effect
gives the gate a false-fail rate of up to about 2%, and a juror may not move a
chance line. **My reply:** C adds no number. Each attack is read against its own
unmodified RULES 12 line. Applying a correction such as halving each line would
be a new threshold, and that is closed to me. The extra false-fail risk falls on
the side that can be undone (2c). The objection still has real weight. A reader
who takes RULES 12 as governing the gate as a whole, rather than each
measurement in it, would call C a breach and D the reading that keeps the gate's
false-alarm rate at or below 1%. D's false-fail rate is at or below the smaller
of the two rates, so it never exceeds 1%.

**(ii) The singular "its chance line" means one attack.** The author wrote
"its chance line", singular, and probably had one statistic in mind. If so, A
or B is the faithful reading. C adds a test the author did not write, and under
RULES 6 (`RULES.md` lines 34–36, "The rule is written first … A rule is not
changed after looking at a result") adding a test now is a change. **My reply:**
I cannot tell which statistic was meant. The only file that could show it,
`exam-prep/R-04-blindness.md`, is closed to me. Choosing A or B would be a
guess. C is the only reading that drops nothing the author put into the audit.

**(iii) The run's own Level 1 standard may be D.** Question file lines 100–102:
"required a family to fail **both** attacks". If that means a family was judged
identifying only when both attacks beat their lines, then the run's own
standard is D. Reading the pooled row differently from the single families would
be inconsistent. **My reply:** the sentence reads two ways. A family "failing"
an attack most naturally means the attack failed to identify the coin through
it. The family is then cleared only if neither attack works, and that is C. I
cannot settle this without the closed file, so I do not rest my answer on it.
If the closed file shows Level 1 was D, this objection gets much stronger.

**(iv) Nearest neighbour may be measuring an artefact.** Cards of one coin with
overlapping 48-hour windows are near-copies (question file lines 114–116). Under
C, a nearest-neighbour score driven only by that overlap fails the gate, even
though it may say nothing about whether a candidate could name the coin. C
inherits every artefact of either attack.

## 4 · Confidence

**Main answer (C): 3 of 5.** C against D: 4. C against A or B: 3, because
objection (ii) cannot be ruled out without the closed file.

What would change my mind:
- A written statement in a file I may read that RULES 12's 1% applies to the
  gate as a whole and not to each measurement. That would make (i) decisive and
  move me to D, or to "the rules do not settle this".
- The author's text in `exam-prep/R-04-blindness.md` showing that "its chance
  line" referred to one named attack (I would move to that attack), or that
  Level 1 was D.
- A written statement that the exam candidate never sees two cards of one coin
  together. That would weaken the case that nearest-neighbour matching is a
  leak a candidate could use, and with it the case for B's half of C.

**Subsidiary point (tie-averaged nearest neighbour): 2 of 5.** A stricter
reader could fail the gate if either version beats its line. If the exam cards'
numbering is itself correlated with coin, the numbering-dependent version would
be picking up a real leak, and it would be the wrong instrument for it.

**Reversibility.** All four readings can be reversed at no cost now, because
nothing has been measured on exam cards (question file line 123). Once the
exam-card audit is run and opened, a change of reading is an "afterwards" rule
under RULES 6 and must be labelled as such. A gate that passes followed by a
sat exam cannot be reversed: the 20 exam coins are fixed by `TACTICS.md` lines
22–24.

## 5 · Files read

- `exam-prep/third-fix/juror-questions/JQ-R04-GATE.md`, whole
- `RULES.md`, `TACTICS.md`, `TEAM.md`, `README.md`, whole
- the seven `decisions/2026-09-19-*/verdict.md` files: `zero-trade-contracts`,
  `tokenized-equity`, `calm-separation`, `large-moment-selection`,
  `effort-level`, `watcher-across-runs`, `card-order-requirement`

To find the verdict files I ran one glob, `decisions/2026-09-19-*/verdict.md`.
It matched only those seven files. I opened nothing else under `decisions/`,
`exam-prep/` or `exam/`.

## 6 · Assumptions and possible steers

**Assumptions, by name:**
- I took the quotations in the question file from `exam-prep/R-04-blindness.md`
  to be accurate. I could not check them.
- I took the "cards" in "the cards are not blind" to mean card content, as a
  candidate sees it.
- In 2c I assumed that no replacement exam coins exist. I base that on
  `TACTICS.md` lines 22–24, which provide for none.

**Possible steers and leaks in the question file (RULES 3):**
- It contains measured results: the table on lines 128–134 and the
  overlap-restricted score on lines 147–150. It then states that every option
  fails today's material (lines 142–145). The stated aim is to neutralise the
  results, but they are still results inside an instruction. My answer does not
  rest on them.
- Lines 69–75 ("Nothing guarantees that no other channel exists outside the
  list") and lines 89–96 (the tie-break property, "you should know") are
  pay-attention-to-X passages. The first leans toward a stricter reading such
  as C. I used the first as a fact in 2d and say so here.
- Lines 100–102, the Level 1 sentence, invite a consistency argument. Because
  of how it is worded, it could push a reader toward D or toward C.
- Lines 154–157 say the readings diverged on an earlier audit but deliberately
  withhold which reading passed. I saw nothing that tells me which.

In the coordinator's instruction itself I saw no steer. Its line "because an
outcome it offers cannot follow" reads to me as generic.
