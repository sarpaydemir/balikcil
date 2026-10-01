# Juror 3 · JQ-R04-DATE a–c with JQ-R04-CONTENT a–c

Written 2026-10-01. I did not see any other juror's answer and did not look for one. In
`decisions/2026-10-01-jq-r04-date-content/` I opened nothing; I wrote only this file.

---

## 0 · The reading that runs through all six parts

All six parts come down to one question: what does the blinding do to the card? My answer has three
parts, and every part below rests on them:

1. **What RULES 9 hides about the date** is the date and time *as printed*, plus the specific
   items TACTICS 6 lists. These are a printed date or time, or a date inside the release
   calendar. RULES 9 does not also hide whatever a reader could *infer* about the date from
   fields that TACTICS 3 puts on the card. No ratified verdict says the date has to be
   un-inferable, and no date-identification test has been measured. (DATE a, b, c.)
2. **The coin side is different, but only because the laboratory has already ratified a measured
   standard for it.** The JQ-R04-GATE verdict fails the exam cards when either attack beats its
   RULES 12 line. All three jurors on that question grounded it in RULES 9 (RULES.md line 41).
   JQ-R04-CARRIES defines when a column carries a coin signature. So when a column carries a
   measured coin signature, that is a RULES 9 matter under ratified law. RULES 9 is the rule and
   TACTICS 6 is how the laboratory planned to meet it. Where the plan measurably falls short,
   the blinding may hide more. (CONTENT a, and through it b3.)
3. **The blinding may hide, coarsen or rescale. It may not add.** The exam card is the
   observation card's "before" section with things hidden. It cannot carry information the
   card does not print, apart from what TACTICS 6 itself prescribes. (CONTENT c, and a
   condition on b1.)

DATE asks whether removal is *required*. CONTENT-a asks whether removal is *permitted*. These two
modalities do not conflict: answering "not required" to DATE and "permitted" to CONTENT-a is
consistent. I do **not** extend the CONTENT-a permission to date fields. Nobody asked about that,
and no ratified date standard exists to ground it.

---

## 1 · Answers

**JQ-R04-DATE-a: No.** RULES 9 and TACTICS 6 ("the date and time") do not require removing the
bitcoin/ethereum columns. They print no date or time. TACTICS 3 places them on the card "over
the same hours", so any faithful rendering of them links cards that share hours. What was
measured is that link between cards (243 of 495 true pairs, 0 false matches). Placing a card in
time was not measured. A link between cards is not the date.

**JQ-R04-DATE-b: No.** TACTICS 6 line 107 hides "the date in the release calendar", which is the
printed date. It does not hide the release *name*. The name is the content TACTICS 3 line 62
puts on the card. TACTICS 6 treats the coin the same way: it hides "the coin name inside
announcements", meaning the literal string, and not the kind of announcement a reader might use
to infer the coin.

**JQ-R04-DATE-c: No.** TACTICS 6 line 103 hides "the date and time" as printed. A relative offset
reveals clock time only to a reader who brings in outside knowledge of a release's publication
time. The rules do not ask for that kind of hiding, and it has not been measured.

**JQ-R04-CONTENT-a: Yes, with one qualification.** The blinding may leave out a column that
TACTICS 3 puts on the card when that column carries a measured coin signature in the rendering
the exam card would otherwise use. Signature here is defined by JQ-R04-CARRIES and tested on exam
cards before use. The qualification: the permission rests on RULES 9 and the measurement **alone**.
"Nothing the frozen canteen book reads it" is not part of what makes the omission permissible.
The laboratory deliberately keeps exam construction blind to the canteen's ideas (TEAM.md
lines 70–71). If a column some frozen rule reads ever carries a signature, that is a conflict
this answer does not resolve (see §5).

**JQ-R04-CONTENT-b: b1 is permitted. b2 is permitted. b3 is permitted only under the condition of
CONTENT-a.**
- **b1** (actual price rebased to 100, fixed decimals) is the literal rendering in TACTICS 6.
  It has one condition, which follows from CONTENT-c: it may not print more precision than the
  price the raw card prints. I could not check the raw card's precision.
- **b2** (start at 100 and apply the printed `chg%` in turn) is also "the price … converted to a
  number starting from 100". It is computed from the card's own printed price changes, and it
  differs from b1 only by rounding. TACTICS 3 line 71 puts rounding on every number on the card.
- **b3** (no price column; `chg%` stays) does not meet TACTICS 6 on its own terms, because the
  parenthesis describes a converted number that *is shown*. b3 is therefore permitted only by
  the CONTENT-a route: the rendering the exam card would otherwise carry must carry a measured
  coin signature on exam cards. The choice among the permitted renderings, and the number of
  decimals, is engineering and is not mine. I set no number.

**JQ-R04-CONTENT-c: No.** A ranked column on an exam card must come from the values the card
prints. Hours the raw card prints as equal must stay tied. Ranking from values before the card
writer's rounding adds an order the card never carried. The blinding may hide and coarsen; it may
not add.

### Where parts depend on each other

- **CONTENT-a ↔ CONTENT-c.** Under my "no" to c, the trade-count column is ranked from printed
  values. The ties that rounding creates ("1k", "5k") therefore stay on the exam card. Those ties
  are the "repeat" features that JQ-R04-CARRIES-b counts as the column's own. So c = no makes it
  more likely that part a's condition is met, and CONTENT-a then allows the column to be left
  out. Had I answered c = yes, the finer ranking would have been one way to try to lower the
  signature. I reject it on what the card carries, not on what the audit would show.
- **CONTENT-b ↔ CONTENT-a and c.** b3 rests entirely on CONTENT-a. b1's precision condition
  comes from CONTENT-c. If the referee's majority goes "no" on CONTENT-a, my b3 falls.
- **DATE a–c ↔ CONTENT-a.** These are consistent because "required" and "permitted" are different
  questions. My DATE answers would change if a measurement showed the date or time recoverable
  from these fields, or if a ratified verdict set a date standard like the coin gate (see §4).

---

## 2 · What it rests on

**RULES 9 and its scope.**
- `RULES.md` line 41: "In the exam the coin name and the date are hidden."
- `README.md` lines 42–43: "Cards from the exam coins are shown, but only the part before the
  movement. The coin name and date are hidden."
- `TEAM.md` lines 68–69 (Nadia): "writes the script that prepares the exam cards. Strips the names
  and dates, hides the price, seals the answer key." "Strips … dates" is an operation on
  printed things.

**What is hidden (closed list for dates).**
- `TACTICS.md` lines 101–107: "**What is hidden:** the coin name · the date and time · the price
  itself (converted to a number starting from 100) · the coin name inside announcements · the
  Wikipedia number itself (given as a ratio to the coin's own average) · the date in the release
  calendar". The authors did think about indirect identifiers: price level, Wikipedia level,
  the name inside announcements, the date inside the release calendar. They listed the ones they
  meant. For the release calendar they wrote "the date", not "the date and time" (compare
  line 103) and not "the release".

**What is on the card.**
- `TACTICS.md` line 50: "the 24 hours before the start, hour by hour".
- `TACTICS.md` line 61: "bitcoin and ethereum, over the same hours". This puts the shared-hour
  link into the field itself: two cards covering the same hours must print the same market
  values.
- `TACTICS.md` line 62: "US release calendar (inflation, employment, rate decision)". The field
  is *which* release. Without its name and its timing relative to the card, it says almost
  nothing.
- `TACTICS.md` line 55: "**What is on the card** (where data exists)".
- `TACTICS.md` line 71: "Numbers are rounded and the card is kept short. The AI never sees raw
  seconds."
- `TACTICS.md` lines 99–100: "The cards contain only the 'before' section." The exam card is the
  card's before section, with hides applied.

**Same-hour cards are expected by the laboratory's own text (DATE-a).**
- `RULES.md` lines 53–54 (RULES 13): "Moments occurring in several coins in the same hour count as
  a single event."
- `TACTICS.md` line 127: "A moment appearing in several cards in the same hour counts as a single
  event."
  The documents anticipate exam cards that share hours and deal with them in scoring. They do not
  list shared hours among the things hidden.

**The coin signature as a RULES 9 matter (CONTENT-a, b3).**
- `decisions/2026-10-01-jq-r04-gate/verdict.md` line 72: "**The gate fails if either the
  nearest-neighbour attack or the pair AUC attack beats its own RULES 12 chance line on the exam
  cards.**" Lines 20, 22 and 24 record that all three jurors grounded that answer in "RULES.md
  line 41".
- JQ-R04-CARRIES, as quoted in my instruction (verdict lines 107, 109): a column carries a
  signature "when **either** the pair AUC attack or the nearest-neighbour attack beats its own
  RULES 12 chance line on that set", and the trade-count set is "its typical level, its two
  repeat features and its two shape features".
- `RULES.md` lines 3–4: "These rules do not change." TACTICS.md is "Tactics — step by step"
  (line 1), the method. When the method's list measurably fails to meet the rule, the rule
  governs.

**Exam construction is blind to the canteen (the qualification on CONTENT-a).**
- `TEAM.md` lines 70–71 (Nadia): "**Cannot:** read the observation notes or the canteen. So that
  she does not build the exam around the ideas."

**Price renderings (CONTENT-b).**
- `TACTICS.md` line 104: "the price itself (converted to a number starting from 100)".
- `canteen/2026-09-19-sofia.md` lines 116–120: "Read it from the `chg%` column. If an exam card
  does not print `chg%`, compute it from the `close` column … a percentage change is unchanged
  by TACTICS 6's rebasing". Under b2 and b3 `chg%` stays, so S-1's trigger is unaffected.

**Ranking source (CONTENT-c).**
- `TACTICS.md` line 71 (above) and lines 99–100 (above).
- `JQ-R04-CONTENT.md` lines 207–212: the pre-rounding ranking "read from the same sources the raw
  card is written from … the exam card then shows an order between them that the raw card does
  not print, and the watchers … did not see."
- `RULES.md` lines 43–44 (RULES 10) and `TACTICS.md` lines 110–112: every sitter, Tomás included,
  gets the same cards. A finer order unknown to the watchers gives every sitter something the
  observation card never had.

---

## 3 · The strongest case against my answers

**Against DATE-a (the case I take most seriously).** The laboratory has ratified a gate that
treats *linkage of cards to the same coin* (pair AUC, nearest neighbour) as a breach of "the coin
name is hidden", even though linkage does not print or reveal a name. By the same logic, linking
cards to the same hours is a breach of "the date is hidden", even though no date is printed. By
the measure in the question it is a strong link (243 of 495, 0 false). My answer treats the two
sides differently. **My reply:** (i) the coin standard was ratified for the coin, and applying it
to dates by analogy would extend a verdict past its question. (ii) For this field, linkage cannot
be removed short of deleting the field, because TACTICS 3 defines it as market values "over the
same hours". (iii) RULES 13 and TACTICS 7 already foresee same-hour cards. The reply is not
airtight.

There is a second channel the question does not raise. Large moments often share hours with other
coins' moments (market-wide moves, RULES 13). Calm moments are chosen at random. So a
candidate who could see that two cards share hours might learn something about *the outcome*. I
have not measured this and it is not a date question. I name it here so it is not lost. Also, an
exam candidate that is a language model may remember large market days from the period. That has
not been measured.

**Against DATE-b.** TACTICS 6 hides "the date in the release calendar" for a reason: so the
candidate cannot place the card in time. A name that is published on one known day each year
gives the date to any reader with general knowledge. Over a one-year period, the day of the year
is the date. An exam candidate that is a language model brings exactly that kind of general
knowledge, and RULES 10 removes its tools but not its memory. On this reading the name is the
date in another form, the same way price level is the coin in another form, which is why
TACTICS 6 rebases the price. **My reply:** TACTICS 6 handles price by an explicit listed
conversion. It handles announcements by hiding the literal coin name, not the announcement's
content. For releases it wrote "the date", not the name. Whether a tool-less candidate can date a
card this way is unmeasured (JQ-R04-DATE.md lines 111–112).

There is also something else, which I do not decide: TACTICS 3 line 62 qualifies the calendar
with "(inflation, employment, rate decision)". Several of the 13 names look like neither, for
example "American Time Use Survey" and "Productivity by State". Whether that parenthesis limits
which releases belong on the card at all is a separate open question.

**Against DATE-c.** Time of day is plainly part of "the date and time". An offset plus a widely
known release clock time gives the card's clock hour to anyone who knows the time, without any
calculation. **My reply:** if inferable time of day counted as printed time, then every hourly
column with an intraday rhythm would be suspect, including volume and possibly the funding
payment marks (TACTICS 3 line 58). I have measured none of those and could not check how the
card renders funding. That reading would leave little of TACTICS 3 on the card. The authors
wrote "date and time" at line 103 and only "date" at line 107.

**Against CONTENT-a.** TACTICS 6 is introduced as *the* list of what is hidden, and nothing
in it removes a whole TACTICS 3 field. Its pattern is to *convert* (price rebased, Wikipedia as a
ratio), not to delete. A blinding that may delete any column with a measured signature gives the
preparer an open-ended power that the documents never wrote down. Removing a column the recipe
does not read costs Hana and Greta nothing but may take something away from Tomás, the rival
the recipe must beat (RULES 11). That tilts the comparison toward passing. **My reply:** the
tilt is exactly why I separate the permission from the canteen book (TEAM.md lines 70–71). The
trigger has to be the measured signature, chosen blind to which columns the recipe reads. Without
the permission, a failed gate (ratified) would have no remedy except asking the user, and the
user has declined to be asked. The case still has weight. The most defensible "no" says: the
conflict between RULES 9 and TACTICS 3 is not a juror's to resolve.

**Against CONTENT-b (b2).** "The price itself … converted" means the *price* converted, and b2 is
not the price. It is a re-integration of rounded changes, and it drifts from the price by an
amount nobody has measured. It removes the tick structure precisely because it is not the price.
**Against b3:** if the TACTICS 6 parenthesis prescribes a column, b3 deletes a prescribed field.
I only allow it through CONTENT-a, and that is as strong as CONTENT-a is.

**Against CONTENT-c.** TACTICS 6 itself computes an exam-card value from data the card does not
print: "the Wikipedia number … given as a ratio to the coin's own average" (line 106). The
coin's own average is not on a 24-hour card. So the laboratory's own blinding already uses
off-card source data. A rank of the field's true values is still that field ("trade count"), and
rounding exists to keep the card short (line 71), not to define what a field is. Also,
rounding-made ties are themselves a coin signature (as with price at 2 decimals), so keeping them
works against RULES 9. **My reply:** the Wikipedia ratio is a *listed* conversion that *replaces*
a hidden number. Pre-rounding ranks are not listed and *add* an order. "The AI never sees raw
seconds" (line 71) shows the card's resolution is chosen on purpose. Where the ties carry a
signature, CONTENT-a, not extra detail, is the permitted remedy.

---

## 4 · Confidence, and what would change my mind

| part | answer | confidence (1–5) | what would change my mind |
|---|---|---|---|
| DATE-a | no | 3 | A ratified verdict that "the date is hidden" means no measured date signature (the date equivalent of the coin gate), or a measurement that a tool-less candidate can place cards in absolute time from these columns. |
| DATE-b | no | 3 | A measurement that a tool-less candidate dates cards from release names, or a reading of TACTICS 6 line 107 that I have not considered and that ties "date" to the name. |
| DATE-c | no | 3 | The same kind of measurement for clock time, or text in the laboratory's documents defining "time" as time of day however conveyed. |
| CONTENT-a | yes, permission rests on the measured signature alone | 3 | A document line saying TACTICS 6's list is exhaustive *against* RULES 9, or a showing that the coin gate is not a RULES 9 test. |
| CONTENT-b | b1 yes (no finer than printed); b2 yes; b3 only via CONTENT-a | b1 4 · b2 3 · b3 3 | b2: a reading of "the price itself" that excludes derived paths. b3: CONTENT-a going the other way. b1: evidence the raw card prints price at a precision lower than any rendering under consideration. |
| CONTENT-c | no | 4 | A TACTICS line allowing exam renderings from pre-rounding source data beyond the listed Wikipedia ratio. |

**Reversibility.** Every answer here governs exam cards that have not been built. Before any exam
card is sat, changing course means rebuilding the cards and re-running the audit, which is
engineering work. The cost has not been measured by me. Once the exam is sat and the answer key
used, a field that should have been hidden but was shown cannot be fixed by a rebuild, and the
exam would have to be re-run on cards nobody has seen. In that sense the three DATE "no"
answers are the less reversible side: they keep fields that a later ruling might call leaks.
CONTENT-a "yes" and CONTENT-c "no" lean towards showing less, which is the side that is cheaper
to undo before the exam.

**Rule change: none.** Nothing here changes `RULES.md`. I set no threshold, score, number of
decimals or trading rule. Whether a column "carries" a signature is the ratified JQ-R04-CARRIES
test, which I did not apply.

---

## 5 · Unresolved, by name (RULES 22)

1. Whether a frozen-book rule that reads a column carrying a measured coin signature conflicts
   with RULES 9. Not asked and not resolved here.
2. Whether the frozen book reads `close` anywhere other than S-1. I could read only lines
   112–120, 221–225, 245–246, 268–270 and 667–671. If it does, b2 and b3 change that rule's
   input.
3. The precision at which the raw card prints the price. This decides whether b1 at a given
   number of decimals is "finer than printed".
4. Whether shared-hour linkage between exam cards leaks *outcome* (large moments cluster in time,
   calm moments are random). This is not a date question.
5. Whether TACTICS 3's "(inflation, employment, rate decision)" limits which releases belong on
   the card.
6. Whether a tool-less exam candidate can date or time a card from bitcoin/ethereum values,
   release names or offsets. All unmeasured.

---

## 6 · Files read

- `exam-prep/sixth-fix/juror-questions/JQ-R04-DATE.md` (whole)
- `exam-prep/sixth-fix/juror-questions/JQ-R04-CONTENT.md` (whole)
- `RULES.md`, `TACTICS.md`, `TEAM.md`, `README.md` (whole)
- `canteen/2026-09-19-sofia.md` lines 112–120, 221–225, 245–246, 268–270, 667–671 only
- `decisions/2026-10-01-jq-r04-gate/verdict.md`, `decisions/2026-10-01-jq-n1-canteen-8/verdict.md`
- `decisions/2026-09-19-{zero-trade-contracts,tokenized-equity,calm-separation,large-moment-selection,effort-level,watcher-across-runs,card-order-requirement}/verdict.md`

**Disclosure:** to find the 2026-09-19 verdict files I ran one Glob with the pattern
`decisions/2026-09-19-*/verdict.md`. It could only match `verdict.md` files, and it returned only
the seven paths above. The instruction asked that every search be scoped to a named file, and
this glob reached across `decisions/`. Nothing other than those seven paths was shown to me.

## 7 · Assumptions

- That the coin gate is a RULES 9 test. I infer this from the gate verdict's record that its
  jurors cited RULES.md line 41. I could not read the gate question itself.
- That "the rendering the exam card would otherwise carry" in CONTENT-a means the rendering
  permitted by my CONTENT-c (ranks from printed values).
- That the 2026-09-19 verdicts do not touch this question. I found nothing in them about blinding
  or card content.

## 8 · Steers and leaks seen

- **Measured results in the question files (RULES 3).** Both files carry results from the
  observation cards: 243/495 and 0/46,170; 100/306 and 13 names on 18 cards; 99 cards; the AUC
  and nearest-neighbour table; the tie-count table. The 2026-09-19 calm-separation referee
  treated measured counts in a juror instruction as a RULES 3 fault (its verdict, lines 26–27).
  They are presented neutrally, and I did not rest any answer on their size.
- **The title of DATE-a overstates what was measured.** "Columns that identify which clock hours a
  card covers": the measurement is linkage *between* cards, and the file says itself (lines
  71–73) that placing a card in time "has not been measured". The title leans towards "yes".
- **Mild asymmetry in CONTENT-b.** b2 is described by its advantage ("carries nothing the `chg%`
  column … does not already carry"), while b1 comes with its measured signatures. That leans
  towards b2. I permitted b2 on the wording of TACTICS 6, not on that sentence.
- **The coordinator's instruction** contains no steer that I could see beyond the quoted
  JQ-R04-CARRIES outcome, which binds me as settled law.
