# JQ-R04-CARRIES · juror 1

Written 2026-10-01 without seeing any other juror's answer. In
`decisions/2026-10-01-jq-r04-carries/` I opened nothing; I only wrote this file.

## 1 · Answer

**JQ-R04-CARRIES-a: C.** A printed column carries a measured coin signature
when **either** attack, pair AUC or nearest neighbour, beats its own RULES 12
chance line on the feature set that part b counts as the column's.

**JQ-R04-CARRIES-b: own features, as one set.** The test reads every feature
computed from the column's own printed values and from nothing else, tested
together as one set, as a new row of the audit. For the trade-count column that
means its typical level, its two repeat features and its two shape features. It
does not include the previous-7-day feature. As the audit already does, any
feature that has the same value on every card, or is missing on any card, is
dropped and the run records that.

**How the parts depend on each other.** Answer a does not depend on answer b. It
would be C under any of the part-b options. Answer b does limit how many tests
answer a combines. With one set there are exactly two tests: one set, two
attacks. If the "every family" or "column-alone families" reading won part b,
then C would combine up to six tests for the trade-count column (three families,
two attacks each). That makes the multiple-test objection under 3(a) below
heavier. I would still answer C, but with lower confidence (see 4).

The question can be answered as posed. Both parts ask what a phrase means and
which existing measurements it refers to. Neither part asks me to set a number:
the chance line stays the RULES 12 line for each attack.

## 2 · What it rests on

**Part a.**

- This laboratory has already decided how the two attacks combine when the
  question is "does this set of features tell which coin a card is."
  `decisions/2026-10-01-jq-r04-gate/verdict.md` line 72: "**The gate fails if
  either the nearest-neighbour attack or the pair AUC attack beats its own RULES
  12 chance line on the exam cards.** Split: 3–0." The object was different: the
  `ALL-removable` row, verdict line 30. The concept is the same. The question
  file describes both attacks as answering one question, lines 74–76: "For a set
  of features it asks whether they tell which coin a card is, by two attacks,
  each compared with its own RULES 12 chance line". If a column-level signature
  were defined by D, A or B while the gate is defined by C, the same audit would
  use two definitions of "tells which coin a card is". A set of features could
  then fail the gate and still not count as "carrying a signature". This ratified
  verdict does not settle part a, because its object was a different row. But it
  fixes the laboratory's reading of the concept, and C keeps that reading
  consistent.
- `RULES.md` lines 51–52 (RULES 12): "The chance line is not invented. The
  answers are shuffled 1,000 times, and the real result must fall inside the
  best 1%." Each attack is a separate result with its own line (question file
  lines 75–76). If either result falls inside the best 1%, a signature has been
  *measured*. Under D, a measurement that beat its chance line would be ignored
  because a different measurement did not. Under A or B, one of the audit's two
  measurements would be thrown away. No written line favours one attack over the
  other (I looked in `RULES.md`, `TACTICS.md`, `TEAM.md`, `README.md` and the
  question file, and found none).
- The word in the phrase is "measured" (question file line 17: "it carries a
  measured coin signature"). Under C, the phrase holds exactly when the audit
  has measured a signature by one of its two declared measurements.
- What the signature threatens: `RULES.md` line 41 (RULES 9): "In the exam the
  coin name and the date are hidden." `TACTICS.md` lines 101–102: "**What is
  hidden:** - the coin name".

**Part b.**

- `TACTICS.md` lines 50–51 separate the hour-by-hour columns from the summary
  line: "the 24 hours before the start, hour by hour; plus a one-line summary of
  the previous 7 days." The previous-7-day average trade count is printed on
  that summary line, not in the column (question file lines 104–106: "one
  feature read from the previous-7-day line, not from the column"). So it is not
  the column's.
- `TACTICS.md` line 56 lists "trade count" as its own item "on the card", next
  to price, volume and taker pressure. The column is one item of the card, and
  what it "carries" is what its own printed values carry. Features of
  `quote vol`, `open int`, `depth -1%` and the others in `shape-scale-free`
  (question file lines 112–114) are features of other columns.
- That rules out "every family that reads the column". Under that reading the
  trade-count column would "carry a signature" whenever `shape-scale-free` beats
  its line, even if the beat comes entirely from `open int` or `depth +1%`. The
  phrase is said "of one printed column" (question file line 29). A reading that
  credits the column with another column's signature does not define it.
- That also rules out "only families made of the column alone". Under that
  reading the column's two shape features are never tested. They sit only in a
  mixed family, so a signature carried by the column's shape would go unmeasured
  (question file lines 110–111 and 116–117: "It does not today test a column's
  own features as one set apart from the families."). That reading also changes
  with the card set (lines 157–158: "`trades-level` only where the
  previous-7-day feature is not used on that card set"). So whether the column
  is tested on its level at all would depend on what another printed line
  happens to show. The own-set reading has neither defect: every feature of the
  column, and nothing else.
- Which features come from which column is not mine to choose. Question file
  lines 118–120: "Which features are computed from which column is read from the
  audit's code, not chosen; for any other column it is read the same way, and
  the run that measures records it and is reviewed." My answer only says to take
  all of them, together and alone.
- Timing (RULES 6, `RULES.md` lines 34–35: "The rule is written first, the
  result is opened second."). The new row is defined here before any exam-card
  measurement (question file lines 20–21: "will be measured before any exam card
  is used"). Defining it now is writing the rule first.

## 3 · The strongest case against my answer

**(a) Against C.**

1. *Combining two 1% tests makes a stricter-than-written test.* Under C a column
   is declared signature-carrying more easily than by either attack alone.
   Choosing C over D therefore sets how often a column is wrongly found to carry
   a signature. The question itself warns (lines 45–47) that a choice which
   "sets how strict a test is … would be a threshold". On that view none of A–D
   is mine, and the honest answer would be "not a juror's". My reply: the gate
   jury met the same objection, and the referee ratified C as procedure
   (`decisions/2026-10-01-jq-r04-gate/verdict.md` lines 42–52 and 64). Each
   attack is still judged against its own unmodified RULES 12 line. No rule
   gives a combined error rate. The objection is still real, and a referee could
   accept it.
2. *Here the cautious side is not obvious.* At the gate, a false fail was "the
   side that can be undone" (gate verdict line 44). In this question, "carries a
   signature" is the condition under which the other jurors ask whether a
   TACTICS 3 column may be left out (question file lines 16–19). So a false
   positive under C could help remove a column that `TACTICS.md` line 56 puts
   "on the card". That is a departure from the card definition, not a cautious
   step. D would guard against that. My reply: whether a column may be left out
   is explicitly not mine (question file lines 33–34). A definition of
   "measured signature" should not be bent to favour one outcome of that other
   question, and C is what keeps it identical to the ratified gate. But this
   argument has weight, and it is the one most likely to move a referee.

**(b) Against "own features, as one set".**

1. *Dilution.* Both attacks work on similarity across the whole feature set.
   Five features tested together can hide a strong signature carried by two of
   them (say, the repeat features), because the other three add noise to every
   pair's similarity. `repeat-trades` alone might beat its line while the own
   set does not. Under "column-alone families" that signature would count. Under
   my answer it would not, so my reading can say "no signature" when part of the
   column measurably carries one. Splitting into subsets would fix this only by
   adding tests, which is the strictness problem from 3(a)1 again.
2. *It needs a measurement the audit does not make today.* The other two options
   use the families "the audit measures and reports" (question file lines
   151–152 and 159–160). The own-set row is new. A referee could say a juror who
   adds a row is designing a test, not defining a phrase. My reply: the question
   offers this row itself (line 143: "The audit gains this set as a row of its
   own"). Which features go into it is read from code, not chosen (lines
   118–120). And defining the unit a phrase refers to is a definition.

## 4 · Confidence

- **Part a: 4 of 5.** The ratified gate verdict and the absence of any written
  preference between the attacks both point to C. I would move to "not a
  juror's: this sets strictness" if a referee or a written line held that how
  the attacks combine is a threshold. That would also call the gate verdict into
  question. I would move to D if a written line said a signature must be
  confirmed by both attacks.
- **Part b: 3 of 5.** The textual ground, `TACTICS.md` lines 50–51 and 56, is
  clear about what belongs to the column. The dilution objection is real, and I
  cannot measure its size. I am not allowed to and I have no results. I would
  move to "column-alone families" if a written line made the audit's existing
  families the laboratory's units of decision. I would also move if the run that
  measures showed that the column's features cannot be computed as one set
  without a choice that is not read from code.
- **Reversibility.** Both answers can be reversed cheaply until an exam card is
  used: re-running the audit with a different reading is script work (estimate:
  one audit run, no new data). Once an exam card has been used under a blinding
  that relied on this definition, the reversal costs the exam itself, because
  RULES 9 cannot be restored after the cards are seen. That part is
  irreversible.
- **Rule change: none.** This answer defines a phrase and names the measurements
  it reads. It changes nothing in `RULES.md` and sets no threshold, score or
  chance line. Both lines are RULES 12 lines, 1,000 shuffles and the best 1%.
  It does not decide whether any column may be left out.

## Files read

- `exam-prep/sixth-fix/juror-questions/JQ-R04-CARRIES.md`
- `RULES.md`, `TACTICS.md`, `TEAM.md`, `README.md`, each in full
- `decisions/2026-09-19-{zero-trade-contracts, tokenized-equity, calm-separation,
  large-moment-selection, effort-level, watcher-across-runs,
  card-order-requirement}/verdict.md`
- `decisions/2026-10-01-jq-r04-gate/verdict.md`,
  `decisions/2026-10-01-jq-n1-canteen-8/verdict.md`

To list the `verdict.md` files I ran one glob limited to
`decisions/2026-09-19-*/verdict.md`. It matched only verdict files. I opened
nothing in `exam/` and nothing else in `exam-prep/` or `decisions/`.

## Assumptions

- **Same concept as the gate.** I assume that "tells which coin a card is"
  (question file lines 74–76) means the same thing at the gate and for one
  column. Part a leans on this.
- **The summary line is not part of the column.** I assume the
  "previous-7-day line" in the question is the TACTICS 3 "one-line summary of
  the previous 7 days", a separate printed line.
- **Nearest-neighbour tie versions.** I take the question's own rule (lines
  89–95) as it stands: wherever the two versions disagree on beating the line,
  the run stops and refers the point. This holds even under C when pair AUC has
  already beaten its line. I do not override it.

## Steer

None found in the coordinator's instruction. The question file contains context
about the downstream question (JQ-R04-CONTENT) and a section titled "not to
steer". That section states consequences symmetrically and leaks no result. It
does reveal that this definition feeds a decision about leaving out the
trade-count column. I treated that as context and set it aside when choosing,
except where I name it as an objection (3(a)2).
