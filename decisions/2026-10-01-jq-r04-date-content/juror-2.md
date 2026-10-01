# Juror 2 · JQ-R04-DATE a–c with JQ-R04-CONTENT a–c

Written 2026-10-01 (date from the session context, not guessed) by juror 2,
without seeing any other juror's answer. I opened nothing in
`decisions/2026-10-01-jq-r04-date-content/` except this file, which I created.

## 0 · The one reading all six parts rest on

The six parts ask the same thing in six places: what may the blinding do to
the observation card when it makes an exam card? The laboratory's documents
name exactly two kinds of act:

- **strip** what is printed as a name or a date/time (TACTICS 6 lines 102, 103,
  105, 107; TEAM.md lines 68–69: "Strips the names and dates, hides the price");
- **convert** a level that betrays the coin into a relative form that TACTICS 6
  names (line 104 "the price itself (converted to a number starting from 100)",
  line 106 "the Wikipedia number itself (given as a ratio to the coin's own
  average)").

Nothing in RULES, TACTICS, TEAM or README names a third act: removing a whole
field that TACTICS 3 puts on the card, or adding to the card information the
raw card does not print. TACTICS 6 lines 99–100: "The cards contain only the
'before' section". Every item on the hiding list takes something away or makes
it coarser. None adds anything.

So my answers are: nothing more has to be stripped than what is printed as a
date or time (DATE a–c: no); no TACTICS 3 field is removed (CONTENT-a: no;
CONTENT-b: b3 not permitted); and nothing finer than the printed card is added
(CONTENT-c: no; CONTENT-b: b1 and b2 permitted within that limit). The parts
depend on each other through this one reading. If a referee finds the reading
wrong for one part, it is probably wrong for the others too. I say where below.

---

## 1 · Answers

**JQ-R04-DATE-a: No.** RULES 9 and TACTICS 6 do not require removing the
bitcoin/ethereum columns. Those columns print no date and no time. What they do
is let two cards be placed in the *same* hours, which is simultaneity, not a
date.

**JQ-R04-DATE-b: No.** Hiding "the date in the release calendar" covers a date
printed in the release line. That includes a date or year printed *inside* a
name (as the "Born YYYY-YYYY" masking already treats it). It does not cover a
release name that lets a reader with outside knowledge work out the date.

**JQ-R04-DATE-c: No.** Hiding "the date and time" covers a printed clock time.
It does not cover an hour offset to a release, even when a reader with outside
knowledge of that release's public clock time could work out the card's clock
hour from the offset.

**JQ-R04-CONTENT-a: No, though not for the reason the "no" option gives.** I do
not rest on TACTICS 6 being a closed list. I rest on three things. No document
gives the blinding the act of removing a TACTICS 3 field. The condition in the
question ("nothing the frozen canteen book asks for reads it") makes the exam
card's content depend on the canteen book, which TEAM.md lines 70–71 exist to
prevent. And a removal chosen that way can only take information from the
rivals RULES 11 sets against the recipe, never from the recipe. What happens to
a column that stays and carries a signature is JQ-R04-CONTENT-d, which is not
mine.

**JQ-R04-CONTENT-b: b1 and b2 are permitted, b3 is not.**
- **b1** is TACTICS 6's own wording. My answer to c adds one limit: it must be
  the price the raw card prints, rebased. It must not be a rebased value carrying
  precision the raw card does not print. I do not know how the raw card prints
  price, so I state this as a condition and do not claim it is met or broken.
- **b2** is the price converted to a number starting from 100, with only the
  rounding the card already carries (TACTICS 3 line 71). It adds nothing that is
  not on the card.
- **b3** removes the TACTICS 3 "price" field. It also leaves nothing for TACTICS
  6's "(converted to a number starting from 100)" to describe.
- **Dependency:** b3 stands or falls with CONTENT-a. If the ratified outcome on
  CONTENT-a is "yes", b3 would be permitted under that outcome's conditions. One
  of those conditions is that nothing in the frozen book reads the price column.
  I cannot check that: I may read only five excerpts of the book, and they show
  only S-1's fallback.

**JQ-R04-CONTENT-c: No.** A ranked column on an exam card must be computed from
the values the raw card prints, so hours the raw card prints as equal get equal
ranks. Ranking from values before the card writer's rounding adds an order that
the observation card never carried.

**How the parts fit together.** CONTENT-a and CONTENT-c bear on each other, as
the question says. Under my c, the trade-count column is ranked from printed
values and keeps its ties. If that rendering carries a measured signature (as
defined by the ratified JQ-R04-CARRIES), my a still says the column stays, and
CONTENT-d governs what follows. CONTENT-b's b1 limit and its b3 refusal come
from c and a respectively. The DATE parts depend on each other only through the
shared reading in §0.

---

## 2 · What it rests on

### Common ground

- `RULES.md` line 41 (RULES 9): "In the exam the coin name and the date are
  hidden."
- `TACTICS.md` lines 99–107: "The cards contain only the 'before' section. /
  **What is hidden:** / the coin name / the date and time / the price itself
  (converted to a number starting from 100) / the coin name inside announcements
  / the Wikipedia number itself (given as a ratio to the coin's own average) /
  the date in the release calendar"
- `TEAM.md` lines 68–69 (Nadia): "writes the script that prepares the exam cards.
  Strips the names and dates, hides the price, seals the answer key."
- `README.md` lines 41–42: "Cards from the exam coins are shown, but only the
  part before the movement. The coin name and date are hidden."
- The laboratory's ratified juries have read TACTICS lists literally and refused
  to add conditions the text does not write. One example is
  `decisions/2026-09-19-tokenized-equity/verdict.md` line 35: "The definition
  contains no fourth condition restricting the underlying to cryptocurrency."
  Another is `decisions/2026-09-19-calm-separation/verdict.md` line 50: "the calm
  bullet defines separation only as 72 hours from any large movement". These are
  precedents for the method, not rulings on this question.

### DATE-a

- `TACTICS.md` line 61, on the card: "bitcoin and ethereum, over the same hours".
  A market-wide column shown "over the same hours" must print identical values on
  two cards that share hours. The linkage measured in the question (DATE.md lines
  64–69: 243 of 495 true shared-hour pairs, 0 false among 46,170) comes from the
  field TACTICS 3 itself places on the card, not from a failure to hide something.
- `TACTICS.md` line 103 hides "the date and time". Linking two cards gives
  neither. DATE.md lines 72–73: "a reader who remembered market history could in
  principle place a card in time; that has not been measured." Under RULES 19/22
  (`RULES.md` lines 71, 76–77: "'Could not be measured' never turns into 'no
  problem'"), an unmeasured channel is named as unmeasured. It does not turn into
  a removal.

### DATE-b

- `TACTICS.md` line 107 hides "the date in the release calendar". It does not
  hide the calendar or its names. Compare line 105, where the authors did reach
  *inside* free text when they meant to: "the coin name inside announcements".
  They wrote no "date inside release names" item.
- `TACTICS.md` line 62 puts on the card "US release calendar (inflation,
  employment, rate decision)". A rate decision falls on a small number of
  scheduled, public days a year (general knowledge, not measured by the
  laboratory). So the name "rate decision" alone already narrows the date for a
  reader who knows the schedule. A "yes" would either mask a release type TACTICS
  3 names explicitly, or need a line for how precisely a name must pin the date
  before it is masked. That line is a threshold, and RULES 33 (`RULES.md` lines
  119–121: "never a threshold or score") forbids a juror to set one.
- DATE.md lines 111–112: "Whether an exam candidate without tools (RULES 10)
  actually can has not been measured." DATE.md lines 105–108: how often each of
  the 13 releases is published "has not been measured."

### DATE-c

- `TACTICS.md` line 103: "the date and time". The offset is relative. The first
  run's treatment (strip the calendar date, keep the name and an hour offset) is
  the same kind of act as TACTICS 6's own conversions: hide the absolute value,
  keep the relative one.
- `TACTICS.md` line 62 again: a release on an hourly card is informative because
  of *when* it falls relative to the hours shown. An offset of zero, or any
  offset, together with a known publication time, would reveal the clock hour, so
  a "yes" reaches the timing of every release TACTICS 3 lists. Whether a field
  that is kept should also lose its timing is engineering (DATE.md lines 27–28)
  and not mine.
- DATE.md lines 129–130: "How many of those releases have a fixed public time,
  and whether a tool-less candidate knows it, has not been measured."

### CONTENT-a

- No line in `RULES.md`, `TACTICS.md`, `TEAM.md` or `README.md` gives the
  blinding the act of removing a TACTICS 3 field. I read all four files in full.
  `TACTICS.md` line 55, "**What is on the card** (where data exists):", makes a
  field conditional on *data existing*, not on blinding.
- Where TACTICS 6 does deal with a TACTICS 3 field that betrays the coin by its
  level, it converts the field and keeps it: line 104 (price) and line 106
  (Wikipedia). It removes nothing listed in TACTICS 3.
- `TEAM.md` lines 70–71, Nadia: "Cannot: read the observation notes or the
  canteen. So that she does not build the exam around the ideas." The question's
  condition, "when nothing the frozen canteen book asks for reads it", is a
  canteen-dependent rule for building the exam card. Columns the book reads would
  stay and columns it does not read would go. That is building the card around
  the ideas, even when the motive is protective.
- `RULES.md` lines 45–50 (RULES 11) and `TACTICS.md` lines 110–112 and 132–134:
  everyone gets "the same 400 cards", and the recipe paper must beat "Tomás, with
  no recipe, on common sense alone". `TEAM.md` lines 85–86: "if the team cannot
  beat Tomás, it learned nothing by watching." Removing only fields the recipe
  does not read cannot take an input away from the recipe. It can take one away
  from Tomás. Whether the trade count would help Tomás is not measured, so the
  size and even the sign of that tilt are unmeasured. The tilt is structural, and
  it points in the direction section B of RULES ("Not deceiving ourselves")
  exists to guard against.
- `canteen/2026-09-19-sofia.md` lines 224–225 (B-2 lifts "when somebody checks
  the column against the 5-minute taker archive and states a trade-count floor")
  and lines 669–671 (determined "against the 5-minute taker archive, as a
  data-cleaning decision"). The premise "nothing the frozen book reads it" holds
  only while B-2 is in force and no floor has been stated. CONTENT.md lines
  136–137 says the book does not say whether a floor would apply to the printed
  count. So the premise is not stable.
- Settled law I apply without changing: JQ-R04-CARRIES (as quoted in my
  instruction) fixes what "carries a measured coin signature" means.
  `decisions/2026-10-01-jq-r04-gate/verdict.md` line 72: "The gate fails if
  either the nearest-neighbour attack or the pair AUC attack beats its own RULES
  12 chance line on the exam cards." Neither verdict says a field may be removed
  to pass the gate, and I read neither as saying so.

### CONTENT-b

- `TACTICS.md` line 104: "the price itself (converted to a number starting from
  100)". b1 is this text. b2 is a number starting from 100 that follows the price
  through the card's own printed changes. Its gap from b1 is accumulated rounding,
  and `TACTICS.md` line 71 says "Numbers are rounded". CONTENT.md lines 180–183
  says the size of that gap is unmeasured. b3 prints no converted number at all.
- `TACTICS.md` line 56 lists "price" first among what is on the card. For b3 the
  CONTENT-a ground applies.
- `canteen/2026-09-19-sofia.md` lines 116–120: S-1 reads `chg%` and falls back to
  `close` only "If an exam card does not print `chg%`". Under b1 or b2, `chg%`
  stays unchanged and S-1 is unaffected.

### CONTENT-c

- `TACTICS.md` line 71: "Numbers are rounded and the card is kept short." The
  observation card's numbers are rounded. That card is what the watchers saw and
  what the frozen book was written from.
- `TACTICS.md` lines 99–107: the exam card is the "before" section with the
  listed items hidden. Hiding coarsens. It never refines.
- `RULES.md` lines 34–35 (RULES 6): "The rule is written first, the result is
  opened second. A rule is not changed after looking at a result." The frozen
  book's rules were written against rounded cards. An exam card that orders hours
  the raw card prints as equal presents a different object to the same rules.
  CONTENT.md's table (lines 223–233) counts such hours on all nine columns and on
  all 306 cards.

---

## 3 · The strongest case against my answers

**Against DATE a–c (one case for all three).** RULES 9 says the date is
*hidden*, and a date that can be read off the card is not hidden, whatever form
it takes. The candidate is the same kind of model that may know the BLS
calendar, the FOMC schedule, 8:30 ET release times, and perhaps large market
days. TACTICS 6 hides "the date and time", not just "the printed date". Time of
day is singled out there, and an offset to a CPI or employment release gives it
to anyone who knows when those releases are published. On this view my "no" lets
a known leak stand because it has not been measured yet. Once the exam is sat,
that cannot be undone, while masking a name or an offset loses little. On b in
particular: names that occur on one day a year (CONTENT figures of 13 names, 18
cards) are much closer to "the date in another form" than "rate decision" is.
One can say "the date is hidden" excludes them without setting a numeric line,
by the plain test "does this name, by itself, identify a calendar date?".

My reply: that test still needs a line (does a month-and-day without a year
count? does one of a few days a year count?). The year is not printed. And TACTICS
3 deliberately put a release calendar of named, scheduled releases on an hourly
card. The "no" outcome still names and numbers the channel in the exam manifest
(DATE.md lines 145–147), so nothing is hidden from the user. The case is real all
the same, and it is strongest for **c**.

**Against CONTENT-a (the case I find hardest to answer).** RULES 9 sits above
TACTICS (`RULES.md` lines 3–4: "These rules do not change"). The laboratory has
ratified a gate that reads RULES 9 as measured unidentifiability on exam cards
(gate verdict line 72). If a conversion cannot close a column's measured
signature (CONTENT.md lines 176–177: "No fixed number of decimals tried removes
the signature", for price), keeping the column keeps the card in breach of RULES
9 as the laboratory reads it, and a how-to list should yield to the rule. The
blinding already does more than TACTICS 6 lists: it ranks nine columns, a
conversion TACTICS 6 never names. So "only TACTICS 6's acts" is not how the
laboratory has worked. TEAM.md lines 70–71 is about Nadia choosing cards or
features to *favour* ideas. Keeping the frozen book's inputs intact protects RULES
6 and favours nothing. The tilt against Tomás is unmeasured and could go either
way: an unread, coin-identifying column might mislead him as easily as help him.

My reply: the ratified gate says when the gate fails, not what the blinding may
then do. CONTENT-d (other jurors) governs a field that stays. And no document
grants removal. But my "no" may leave the laboratory with a gate that cannot be
passed by any permitted act, which is a real cost, and the act of converting nine
columns to ranks does weaken my claim that the documents name only two acts.

**Against b3 refused.** The CONTENT-a case applies here too. In addition, `chg%`
already carries the price path and S-1 reads `chg%`, so b3 removes nothing
informative except a convenience. And "the price itself" being hidden is satisfied
best by not printing it.

My reply: that convenience matters to a candidate who "cannot use tools"
(`RULES.md` line 43). A tool-less reader cannot easily compound 24 changes in
their head, so b3 changes what the card tells the human-style reader. And
TACTICS 6's parenthetical describes a converted number being shown.

**Against b2 permitted.** b2 is not "the price itself" converted. It is a
reconstruction whose error grows over 24 steps by an unmeasured amount. If that
error is larger than the card's own rounding of a price would be, b2 is a
different column wearing the price's name.

**Against CONTENT-c.** Ranks are already not the printed value: once a field is
ranked, the rounded token is gone in any case. TACTICS 3 rounds to keep the card
"short", and a rank from 1 to 24 is short whichever values it is computed from.
The field is "trade count", not "rounded trade count". Ranking from printed values
also manufactures the ties (CONTENT.md lines 110–111) that are themselves a coin
signature. My reply: the order between tied hours is information the observation
card did not print and the frozen book was not written against. The cost of
refusing it falls on the side that can be measured and reported.

---

## 4 · Confidence and what would change my mind

| part | answer | confidence | what would change my mind |
|---|---|---|---|
| DATE-a | no | 4 | A measurement that the exam-candidate agent, without tools, places cards in time from the bitcoin/ethereum rows above its RULES 12 line. Or a laboratory document that reads "the date" as anything that dates the card. |
| DATE-b | no | 3 | A measurement that the tool-less candidate dates cards from release names above chance. Or a ratified reading that "the date in the release calendar" means the date the calendar entry *reveals* rather than the date it *prints*. |
| DATE-c | no | 3 | The same as b, for clock hour from offsets. Of the three DATE parts this is the "no" I hold least firmly. |
| CONTENT-a | no | 3, my least certain part | A line in RULES, TACTICS, TEAM or README, or a ratified verdict, that gives the blinding a removal act. Or a reading of the gate verdict, which I have only as its ratification sentence, that ties failure to removal. |
| CONTENT-b | b1, b2 yes · b3 no | 3 (b1: 4 · b2: 3 · b3: 3, tied to CONTENT-a) | For b2: a measurement that its accumulated difference from b1 exceeds the card's own rounding of a rebased price. For b3: a ratified "yes" on CONTENT-a. |
| CONTENT-c | no | 4 | A document that defines the exam card from the card writer's sources rather than from the printed card. |

**Reversible and irreversible.** Every answer is reversible until exam cards are
built, sealed and sat. Reversing costs a rebuild and re-audit of the blinding
(size unmeasured). After the exam is sat, none is reversible: a paper sat on a
card later found to leak cannot be un-sat. The DATE "no"s carry the irreversible
risk if a leak turns out to be real. The manifest's numbering of each channel is
what keeps that risk visible.

**Rule change: none.** I change nothing in `RULES.md` or `TACTICS.md`. I set no
threshold, score, chance line or trading rule. Engineering choices (how a field
is masked, which decimals are used) are not mine, and neither is the choice among
the permitted renderings b1 and b2. If that choice changes the numbers, it is a
further open question.

---

## 5 · Files read

- `exam-prep/sixth-fix/juror-questions/JQ-R04-DATE.md` (whole)
- `exam-prep/sixth-fix/juror-questions/JQ-R04-CONTENT.md` (whole)
- `RULES.md`, `TACTICS.md`, `TEAM.md`, `README.md` (whole)
- `canteen/2026-09-19-sofia.md` lines 112–120, 221–225, 245–246, 268–270, 667–671
  only
- `decisions/2026-09-19-{zero-trade-contracts,tokenized-equity,calm-separation,large-moment-selection,effort-level,watcher-across-runs,card-order-requirement}/verdict.md`,
  `decisions/2026-10-01-jq-r04-gate/verdict.md`,
  `decisions/2026-10-01-jq-n1-canteen-8/verdict.md`
- The JQ-R04-CARRIES outcome, only as quoted in my instruction.

I ran one glob, scoped to the named pattern `decisions/2026-09-19-*/verdict.md`,
to find the verdict files. I did not open `exam/`, any other file under
`exam-prep/`, or any other file under `decisions/`.

## 6 · Assumptions I had to make

- **The ranked rendering of the nine columns.** I take it as the question's given
  and do not rule on whether it is permitted. My §0 reading does not obviously
  license it, and I flag that.
- **How the raw card prints price.** Unknown to me, so b1's limit is stated as a
  condition, not a finding.
- **"rate decision" and publication times.** That a rate decision falls on few
  public days and that many US releases have fixed public clock times is general
  knowledge, not a laboratory measurement. It is used only as an argument and no
  number is attached.
- **What the rest of the frozen book reads.** I saw five excerpts. Anything I say
  about the price column depends on the question file's statement about S-1.
- **Not asked, flagged, not decided.** TACTICS 3 line 62 describes the calendar as
  "(inflation, employment, rate decision)". Several of the 13 names quoted in
  DATE-b do not obviously fall under those words. Whether the release line may
  carry releases outside that parenthesis is a separate question I do not answer.

## 7 · Steers and leaks

- Both question files carry measured results (DATE.md lines 66–69, 90–104,
  127–129; CONTENT.md lines 160–171, 223–236). An earlier referee treated measured
  counts in a juror question as a RULES 3 fault
  (`decisions/2026-09-19-calm-separation/verdict.md` lines 26–27). I report the
  same here. I rested my answers on the text, not the counts.
- Mild framing in CONTENT.md. Lines 179–185 present b2 and b3 with their
  objections already answered ("carries nothing the `chg%` column ... does not
  already carry"; "S-1's fall-back ... is only for a card without `chg%`").
  Lines 210–212 describe the before-rounding ranking with "the watchers ... did
  not see", which is the core of the "no" on c. I reached c from TACTICS 3 line 71
  and TACTICS 6 independently, but a referee should know the question leans that
  way.
- DATE.md lines 110–111 ("could date the card from its name alone") lean toward
  "yes" on b. They are balanced by lines 111–112.
- My instruction contains no result and no "pay attention to X". I saw no other
  juror's answer to this question.
