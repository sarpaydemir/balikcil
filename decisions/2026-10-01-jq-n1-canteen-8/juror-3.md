# Juror 3 · JQ-N1 (parts 1–4) with JQ-CANTEEN-8 (parts a–b)

Written 2026-10-01 without seeing any other juror's answer. I opened nothing in
`decisions/2026-10-01-jq-n1-canteen-8/` other than this file, which I wrote.

## 1 · Answer

**JQ-N1-1:** **start-hour.** Two moments are "in the same hour" when they start
in the same clock hour.

**JQ-N1-2:** **Does not arise.** Under start-hour the relation is transitive
(JQ-N1.md line 162). *Conditional fallback, in case the jury's outcome on part 1
is not start-hour:* use **greedy-clique**, not component. Component joins
moments that do not share an hour. On **earliest / latest**, the rules do not
settle the choice. Neither convention can be grounded in a written rule.

**JQ-N1-3:** **No.** Two moments of the same coin are not made one event.
RULES 13 collapses moments "in several coins". Under start-hour this needs no
convention, because scope `any` and scope `cross-coin` give the same events
(table rows 2 and 3 are identical).

**JQ-N1-4:** **representative.** Each event counts once, and the RULES 12 shuffle
runs over events. **4a:** the rules do not settle which card represents an event.
A convention is needed. It must be fixed and written down before the answer key
is opened (RULES 6), and it must not depend on the answers. Under start-hour,
every card in an event has the same start hour, so the example in the question
("earliest by start hour, ties by card number") becomes "lowest card number". I
accept that convention, but no rule grounds it. **4b:** the event carries the
**sealed label of its representative card**. That way 4b adds no second
convention and nothing is scored against a label that the sealed key (RULES 9)
does not hold. This too is a procedure, not a reading of a written line.

**JQ-CANTEEN-8 a:** **Yes.** As written, TACTICS 2 does not forbid two calm
moments of one coin from overlapping. **A ratified jury has already settled
this:** `decisions/2026-09-19-calm-separation/verdict.md`. The question file
does not mention that verdict.
**JQ-CANTEEN-8 b:** **Not reached**, because part a is "yes".

**Can these be carried out together?** Parts 1–3 and CANTEEN-8 can: start-hour
plus `cross-coin` (or `any`, which gives the same result) needs no further
convention. Overlapping calm cards of one coin have different start hours, so
start-hour never joins them, and CANTEEN-8 "yes" causes no conflict. Part 4
**cannot be carried out until the 4a convention is written down.** Under my
answer 4b follows from 4a. I do not know whether the engine implements
`representative`. The question file describes only the block implementation
(JQ-N1.md lines 202–218). This is an unknown, named here.

**Dependencies.** Part 2 depends on part 1 (moot under start-hour). Part 3 is
nearly moot under start-hour. One coin could only have two moments in one start
hour if two calm draws landed on the same hour. Part 4's stakes depend on part 1.
On the observation cards, start-hour gives 289 events from 306 cards and 2 mixed
large/calm events (JQ-N1.md table, line 92). The exam figures will differ.
CANTEEN-8 changes how many same-coin overlaps exist. Under start-hour it changes
no event.

**Reversibility.** The engine offers every reading, so each choice here can be
reversed at no cost until the exam answer key is opened and scored. After that,
RULES 6 makes any change an "afterwards" rule that must be tested again, which
in practice means it cannot be undone. CANTEEN-8 "yes" keeps the existing way of
drawing moments. A "no" would cost a changed draw procedure for the exam's calm
moments, and reversing it after the draw would mean a redraw and a re-seal.

**Rule change: none.** I set no threshold, score, number of shuffles or 1%
boundary, and I change nothing in `RULES.md` or `TACTICS.md`.

## 2 · What it rests on

**Part 1.**
- `TACTICS.md` line 44: "A moment's start is the hour at which the 24-hour
  movement began." The written definition gives each moment exactly **one**
  hour. "The same hour" (singular) reads most directly as that hour being equal.
- `RULES.md` lines 53–54: "Moments occurring in several coins in the same hour
  count as a single event." and `TACTICS.md` line 127: "A moment appearing in
  several cards in the same hour counts as a single event." **Start-hour is the
  only reading under which these two lines say the same thing.** Each card is
  one moment of one coin ("One page per moment", `TACTICS.md` line 48). One coin
  cannot have two large moments, or a large and a calm moment, starting in the
  same hour (`TACTICS.md` lines 39 and 43). So "several cards in the same start
  hour" means "several coins in the same start hour". Under move-window or
  card-span, "several cards" includes cards of one coin and "several coins" does
  not, so the two texts diverge. The measured table shows the agreement: the
  start-hour `any` and `cross-coin` rows are identical (JQ-N1.md lines 92–93:
  289 / 274 / 3 / 2 / 0 / 1).
- Card-span has a further problem. It uses the 24 hours **after** the start,
  which `TACTICS.md` lines 52–53 say are "Shown only in free observation, never
  in the exam". That span is not part of the moment. It is a display window.

**Part 2.** JQ-N1.md line 162: "Under start-hour the relation is transitive and
part 2 does not arise." Fallback: under component, A and C can be joined while
sharing no hour (JQ-N1.md lines 120–124), which goes against "in the same hour"
in `RULES.md` line 53. Greedy-clique's "every event then is a group of moments
that all share one clock hour" (JQ-N1.md lines 128–129) is the only resolution
that keeps the wording. Earliest and latest are described there as "a second
convention, written in no rule" (JQ-N1.md lines 133–134), so I cannot ground
either one.

**Part 3.** `RULES.md` line 53: "Moments occurring in **several coins**". The
rule is a cross-coin collapse. No line in `RULES.md` or `TACTICS.md` joins two
moments of one coin. Same-coin spacing is handled in `TACTICS.md` §2 (lines 39,
43), which is a different mechanism from RULES 13.

**Part 4.**
- `RULES.md` line 53: "count as a single event", and `TACTICS.md` line 127:
  "counts as a single event". The verb is *count*. Under block, an event of k
  cards still adds k answers to the real result. It is single only inside the
  shuffle. Under representative, it is counted once in both the real result and
  the shuffle.
- `TACTICS.md` lines 125–126: "the answers are shuffled 1,000 times; the boundary
  of the best 1% is the line." Representative keeps this exactly, with the event
  as the unit.
- 4b, sealed key: `RULES.md` lines 41–42: "The answer key is sealed before the
  exam: its fingerprint is written into `LEDGER.md`." Using the representative
  card's own sealed label means no event is scored against a label that is not
  in the sealed key.
- 4a timing: `RULES.md` lines 34–35: "The rule is written first, the result is
  opened second."

**JQ-CANTEEN-8 a.**
- `decisions/2026-09-19-calm-separation/verdict.md` lines 48–50: "**RATIFIED
  3–0** … Section 2 of TACTICS.md requires no minimum distance between two calm
  moments of the same coin. The 48-hour clause sits inside the large-movement
  definition; the calm bullet defines separation only as 72 hours from any large
  movement."
- `TACTICS.md` lines 38–39 (inside the large-movement bullet): "The largest 20 of
  the year are taken for each coin." · "Of two moments closer than 48 hours to
  each other, only the larger counts." Lines 42–43: "**Calm moment:** the same
  number as the large moments, chosen at random. At least 72 hours away from any
  large movement." No calm-to-calm clause exists.
- Forbidding overlap would mean adding a minimum calm-to-calm distance, 48 h or
  24 h under part b's two definitions. That is the same question the
  calm-separation jury answered "no minimum distance" to. A "no" here would
  overturn a ratified outcome by inserting a spacing that TACTICS does not write.

## 3 · The strongest case against my answers

**Part 1.** RULES 13's second sentence states its purpose: "If the whole market
moved together, that is one event." When the whole market moves, each coin's
largest 24-hour window can start an hour or a few hours apart from the others.
Start-hour then collapses almost nothing: 306 cards become 289 events on the
observation cards (JQ-N1.md line 92). The rule's purpose, not counting one
market move many times, is mostly lost. Viktor's question "Did the whole market
move?" (`TEAM.md` line 59) points the same way. Move-window ("their 24-hour
movements share an hour") is a faithful reading of "occurring" for a moment that
`TACTICS.md` line 36 calls a movement "within 24 hours". This is a real
objection. My reply is that the written words name one hour per moment, and that
the wider readings also join large moments with calm moments of other coins
(52 such events under move-window/component, JQ-N1.md line 94). A calm coin is
by definition not part of "the whole market moved together", so the wider
readings fail the purpose sentence too, in the other direction.

**Part 3.** Two overlapping calm cards of one coin share up to 47 hours of the
same data. Counting them as two observations inflates evidence just as a market
move does, and `TACTICS.md` line 127 says "several **cards**", not "several
coins". Under start-hour such cards are never joined, so this inflation stays.
My reply is that RULES 13 governs, and that same-coin spacing belongs to
TACTICS 2, which a ratified jury has read as setting no calm-to-calm minimum.

**Part 4.** Block is the standard way to keep a permutation test honest under
clustering. It uses every card and needs no new convention to pick a
representative or a label. It can be carried out today, and the engine
implements it (JQ-N1.md lines 203–209). Representative cannot be carried out
until a convention that no rule writes (4a) is fixed. Choosing which card's
answer counts is a choice that changes the numbers, which is the definition of
an open question (RULES G). One can also read "counts as a single event" as
satisfied when the event moves as one unit in the shuffle, and "the answers are
shuffled" as meaning the answers, all of them. **This is the answer I am least
sure of. A juror who chose block would have a case as good as mine.**

**JQ-CANTEEN-8 a.** "No" has a principled argument: two moments that share hours
are not two observations, and TACTICS 2 spaces every other same-coin pair. The
48-hour and 72-hour spacings show an intent that one coin's moments should not
overlap, and the calm-to-calm gap may just be an oversight. My reply is that a
gap in the text is filled by asking the user, not by a jury, and that this exact
gap was already ruled on by a ratified jury.

## 4 · Confidence

- **JQ-N1-1 start-hour: 3.** I would change my mind if a written line (not a
  script or a question file) defined a moment as occupying its 24-hour window,
  or tied "event" to the shared hours of movements.
- **JQ-N1-2 "does not arise": 4** given part 1. The greedy-clique fallback: 2.
  Earliest/latest: not settled, 1.
- **JQ-N1-3 no same-coin events: 3.** I would change my mind if a written line
  made TACTICS 7's "several cards" govern over RULES 13's "several coins".
- **JQ-N1-4 representative: 2.** 4a and 4b as conventions: 2. I would change my
  mind if a written line defined a "result" in RULES 12 as computed over every
  card, or if I were shown that `representative` cannot honour the sealed key in
  some case.
- **JQ-CANTEEN-8 a yes: 4.** I would change my mind if the referee held that
  "overlap" is a different question from "minimum distance" in the
  calm-separation verdict. I cannot see how it is: both part b options are
  minimum distances (48 h, 24 h).

## Files I read

`exam-prep/fifth-fix/juror-questions/JQ-N1.md`,
`exam-prep/fifth-fix/juror-questions/JQ-CANTEEN-8.md`, `RULES.md`,
`TACTICS.md`, `TEAM.md`, `README.md`, and `verdict.md` in each of:
`decisions/2026-09-19-{zero-trade-contracts, tokenized-equity, calm-separation,
large-moment-selection, effort-level, watcher-across-runs,
card-order-requirement}/` and `decisions/2026-10-01-jq-r04-gate/`. To find
those I ran one glob limited to the pattern `decisions/2026-09-19-*/verdict.md`.
Nothing else.

## Assumptions (by name)

1. The exam draw picks calm moments without replacement, so one coin never has
   two moments with the same start hour. If that is false, part 3's "nearly
   moot" does not hold.
2. Exam card numbers are assigned without regard to answers. 4a's "lowest card
   number" is neutral only if this holds.
3. Whether the engine implements `representative` is unknown to me.
4. Where RULES 13 and TACTICS 7 differ in wording, RULES 13 governs. No line
   states which file takes precedence.

## Steers and faults seen

- **JQ-CANTEEN-8 omits a ratified verdict that settles its part a**
  (`decisions/2026-09-19-calm-separation/verdict.md`). The question is posed as
  open when it is already decided. This is not a steer, but the referee should
  see it.
- Both question files contain measured results (pair counts, event counts). The
  calm-separation referee judged measured pair counts in a juror instruction a
  RULES 3 fault (verdict lines 26–30). The same fault repeats here. I did not
  rest any answer on the counts. I used them only to show what the readings do.
- JQ-N1.md line 193 says CANTEEN-8 "is not answered here", and line 196 says it
  "goes to you, the same jurors". The two lines are inconsistent, but harmless.
- The coordinator's instruction contains no steer that I could find.
