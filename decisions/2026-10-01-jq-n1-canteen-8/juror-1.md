# Juror 1 · JQ-N1 (parts 1–4) with JQ-CANTEEN-8 (parts a–b)

Written 2026-10-01. I did not see any other juror's answer. In this folder I
opened nothing except this file, which I wrote.

---

## 1 · Answer

**JQ-N1-1.** I choose **start-hour**: two moments are "in the same hour" when
they begin in the same clock hour.

**JQ-N1-2.** **This does not arise.** Under start-hour the relation is
transitive (JQ-N1.md line 162). *Conditional, only in case the referee's
outcome on part 1 is not start-hour:* the written rules do not settle part 2.
Component joins moments that share no hour. Greedy-clique, with its
earliest/latest sub-convention, is a convention that the question file itself
says no rule contains. I would not pick either one on any written ground.

**JQ-N1-3.** I choose **any**, which under start-hour means this: two moments of
one coin that have the same start hour are one moment shown on two cards, so
they count as one event (TACTICS 7). Under start-hour, "any" and "cross-coin"
give the same partition on the observation cards (JQ-N1.md table, rows 2–3).
The choice only matters for an exact same-coin, same-start-hour duplicate. The
question file says there are none in the observation cards (line 139).

**JQ-N1-4.** I choose **block**. Every card and every answer is kept, and each
event moves as one unit in the shuffle. **4a and 4b do not arise.** *Conditional,
in case the outcome is representative:* the written rules settle neither 4a
nor 4b.

**JQ-CANTEEN-8 a.** **Yes**, two calm moments of the same coin may overlap.
**A ratified verdict already settles this.** `decisions/2026-09-19-calm-separation`
held that TACTICS 2 "requires no minimum distance between two calm moments of
the same coin". Answering "no" would put a minimum distance (24 h or 48 h)
between them, which contradicts that ratified outcome. I read the question as
being about the **same coin** only, as the file frames it.

**JQ-CANTEEN-8 b.** **This does not arise**, because part a is "yes".

**Can the four JQ-N1 answers be carried out together?** Yes, as far as the
question file reports. Start-hour, any and block are all offered by the engine.
The file says that under start-hour no observation-card event has a size that
no other event shares (line 214), so block has nothing that cannot move. I could
not check the engine myself because `scripts/` is closed to me. That
"0 unmovable events" figure is for the observation cards. **On the exam cards
it has not been measured.**

**Should any rule change?** No change. Every answer above reads the rules as
written. None of them needs RULES.md or TACTICS.md to change, and the user has
declined to be asked.

---

## 2 · What it rests on

### JQ-N1-1 · start-hour

- `RULES.md` lines 53–54: "Moments occurring in several coins **in the same
  hour** count as a single event." The words are "the same hour", singular and
  definite. Each of the two moments must have one hour of its own, and the two
  hours must be equal.
- `TACTICS.md` line 44: "A moment's start is the hour at which the 24-hour
  movement began." In the written rules this is the **only** line that gives a
  moment a single hour. Move-window and card-span instead replace "the same
  hour" with "some hour in common". That is a different relation and the words
  do not say it.
- `TACTICS.md` line 127: "A moment appearing in several cards in the same hour
  counts as a single event." This again says "the same hour", singular.
- Only start-hour turns the words into a partition with nothing added. The
  question file says so itself. At line 162: "Under start-hour the relation is
  transitive and part 2 does not arise." At lines 125–126, greedy-clique is "a
  stated convention, not an observation". At line 134, its earliest/latest
  choice is "a second convention, written in no rule". So the wider readings
  cannot be carried out from the written rules alone. Someone has to write a
  new convention to complete them, and they would be writing it with the
  observation-card counts already known. `RULES.md` lines 34–36 (RULES 6): "The
  rule is written first, the result is opened second. … If it is changed it
  counts as a new rule, carries the 'afterwards' label". I take a reading that
  needs no new convention to be better grounded than one that does.

### JQ-N1-2 · does not arise

- `exam-prep/fifth-fix/juror-questions/JQ-N1.md` line 162, quoted above.
- For the conditional, line 134 ("a second convention, written in no rule") and
  lines 141–148 show that "earliest" and "latest" give different partitions
  (4 differing events under move-window, 21 under card-span). Whichever of the
  two a juror chose, it would rest on nothing written.

### JQ-N1-3 · any

- `TACTICS.md` line 127: "A moment appearing in **several cards** in the same
  hour counts as a single event." Under start-hour, two cards of one coin with
  one start hour show the same coin over the same 48 hours. That is literally
  one moment appearing in several cards.
- `RULES.md` lines 53–54 say "in several coins". That phrase states when
  different coins' moments merge. It does not forbid merging two cards of one
  coin. RULES 13 is silent on that case and TACTICS 7 covers it, so the two do
  not conflict.
- JQ-N1.md table, rows "start-hour / – / any" and "start-hour / – / cross-coin":
  the figures are the same (289 events, 0 same-coin events). JQ-N1.md lines
  186–187 add: "under start-hour no event in this card set holds two moments of
  one coin".

### JQ-N1-4 · block

- `RULES.md` lines 51–52 (RULES 12): "**The answers** are shuffled 1,000 times".
  The thing shuffled is the answers, and block keeps every one of them.
  Representative throws away every answer except one per event.
- `TACTICS.md` lines 99–100: "Nadia has 400 cards prepared from the exam coins:
  200 before a large movement, 200 calm moments." Also line 110: "all get the
  same 400 cards". Block scores the exam as it was built. Under representative,
  the scored set and its large/calm balance would depend on 4a and 4b, and no
  written line defines either one.
- `RULES.md` lines 41–42 (RULES 9): "The answer key is sealed before the exam".
  Under representative, 4b has to give a single label to an event whose sealed
  key holds both a `large` and a `calm` card (JQ-N1.md lines 224–226). Either a
  convention overrides one of the sealed labels, or 4a's arbitrary choice of
  card decides it. Block reads the sealed labels as they are.
- RULES 13 is still honoured in the chance line. `TACTICS.md` lines 125–127
  place "counts as a single event" directly under the chance-line bullet, and
  under block each event is a single unit of the shuffle. JQ-N1.md lines
  210–213: the block implementation "moves an event only onto an event of the
  same size, card for card … because only then can an event keep its internal
  pattern".
- Under start-hour, block needs **no** convention beyond the recorded
  implementation (JQ-N1.md lines 205–209). Representative needs two (4a, 4b),
  and no written line supplies either.

### JQ-CANTEEN-8 a · yes

- `decisions/2026-09-19-calm-separation/verdict.md` line 50 (RATIFIED 3–0):
  "Section 2 of TACTICS.md requires no minimum distance between two calm
  moments of the same coin. The 48-hour clause sits inside the large-movement
  definition; the calm bullet defines separation only as 72 hours from any
  large movement."
- `TACTICS.md` lines 42–43: "**Calm moment:** the same number as the large
  moments, chosen at random. At least 72 hours away from any large movement."
  The only spacing written for a calm moment is its distance from a large one.
- `TACTICS.md` line 39: "Of two moments closer than 48 hours to each other, only
  the larger counts." This sits under the large-movement bullet, and "the
  larger" has no meaning between two calm moments, which are chosen at random
  and not by size.
- JQ-CANTEEN-8.md lines 78–84: the "card spans" definition of overlap is written
  in `data/overlap/overlap-manifest.md`, which is a measurement manifest and not
  RULES or TACTICS. The "before windows" definition is derived (lines 85–87).
  So "no" would need a spacing that neither RULES nor TACTICS writes.

### JQ-CANTEEN-8 b · does not arise

- JQ-CANTEEN-8.md line 130: "Only if part a is 'no'".

### Where the parts depend on each other

- Part 2 depends on part 1. Under start-hour it is empty.
- Part 3 depends on part 1. Under start-hour, "any" and "cross-coin" differ only
  for exact same-coin duplicates.
- Part 4 depends on part 1. The fact that block has no unmovable event on the
  observation cards is a fact about start-hour (JQ-N1.md line 214). Under
  card-span/component the same choice would leave 23–44 of 306 cards unmovable.
- CANTEEN-8 a interacts with part 1. With "yes" and start-hour together,
  overlapping calm cards of one coin with **different** start hours remain
  separate events. Nothing in my combined answer merges them. See the case
  against, below.

---

## 3 · The strongest case against my answer

**Against start-hour (part 1).** This is the strongest objection to my whole
answer. RULES 13's second sentence states a purpose: "If the whole market moved
together, that is one event." A large moment is the 24-hour window where a
coin moved most (TACTICS lines 36–37). When the market falls, each coin's
largest-move window can start one or two hours apart from the others. Under
start-hour those stay separate events, although in plain English the market
moved together. A 24-hour movement does "occur" across 24 hours, so two
movements running at the same time do occur "in the same hour". TACTICS line 61
shows "bitcoin and ethereum, over the same hours" on every card. One market move
can therefore literally "appear in several cards", which is TACTICS 7's
wording, and that wording fits card-span. Start-hour collapses only 306 → 289.
So RULES 13 hardly bites, and Viktor's question "Did the whole market move?"
(`TEAM.md` line 59) is left mostly to the skeptic rather than to the count. A
referee could reasonably hold that a reading under which a rule barely acts
cannot be what the rule meant. I reply that the purpose cannot be met without
adding an unwritten chain-breaking convention, and that a juror reads the
rules but does not write the missing piece. I admit, though, that "the rules do
not settle part 1" is a respectable answer too.

**Against block (part 4).** RULES 13 says moments "**count** as a single event".
Under block, a paper that is right on three cards of one event scores three hits
in the real result. Only the null distribution treats the event as one unit. On
the plain meaning of "count", representative is the more literal reading. Block
also has a structural flaw: "an event whose size no other event shares never
moves" (JQ-N1.md lines 213–214). The cards of such an event are never shuffled,
which strains "the answers are shuffled". It also fixes that event's hits into
every shuffled paper, which makes the test more conservative. Whether the exam
cards contain such an event under start-hour **has not been measured**. If a
market-wide move on the exam produced a unique-sized event, block would
silently leave it out of the shuffle.

**Against "yes" (CANTEEN-8 a).** Two calm cards of one coin whose starts are
14 h apart share 34 of their 48 hours of the same price series. They are not two
independent observations. TACTICS 2 spaces every other pair of one coin's
moments, which suggests the intent was to keep a coin's moments apart. Combined
with start-hour, my answers leave such pairs counted as **separate** events.
That is a pseudo-replication that neither RULES 13 nor the draw catches. On the
observation cards there are 10 such pairs with overlapping before windows and
21 with overlapping card spans (JQ-CANTEEN-8.md table). On the exam cards this
has not been measured. My reply is that the ratified calm-separation verdict
already ruled that TACTICS 2 sets no calm-to-calm distance, and that an
unwritten spacing cannot be read into the text. Still, this gap is a real
consequence of my combined answer. If it matters, the place to close it is a
rule change put to the user, not a juror's reading.

---

## 4 · Confidence and what would change my mind

| part | answer | confidence | what would change my mind |
|---|---|---|---|
| JQ-N1-1 | start-hour | 3 | A written line, in RULES, TACTICS, TEAM or README, that treats a moment as occupying its whole 24 (or 48) hours for the purpose of co-occurrence. Or a written chain-breaking convention that existed before the observation counts were known. |
| JQ-N1-2 | does not arise; conditional: rules do not settle it | 4 | A ratified outcome on part 1 other than start-hour would make the conditional live. I would still say no written line picks greedy-clique's sub-convention. |
| JQ-N1-3 | any | 4 | A written line saying RULES 13's "several coins" excludes same-coin merging. Or evidence that the exam draw can produce same-coin duplicates whose cards differ. |
| JQ-N1-4 | block | 3 | A written line using "count" in RULES 13 explicitly for the real score, meaning n = events. Or a measurement showing the exam's start-hour event map has unmovable events. That would weaken the "no extra convention" ground, though 4a and 4b would still be unsettled. |
| CANTEEN-8 a | yes | 4 | A finding that the calm-separation verdict was refused or withdrawn. Or a written line in TACTICS 2 putting a calm-to-calm spacing in place. |
| CANTEEN-8 b | does not arise | 5 | Only a "no" on part a. |

**Reversibility.** Every JQ-N1 choice is an engine setting, and changing it
costs nothing **until the exam result is opened**. After that, changing it is a
new rule with the "afterwards" label (RULES 6), so in practice it cannot be
reversed. CANTEEN-8 "yes" changes nothing in the draw. A "no" would mean
redrawing the exam's calm moments, re-preparing those cards and resealing the
key (RULES 9). That is the more expensive answer to undo, and its cost has not
been measured.

---

## Files I read

- `exam-prep/fifth-fix/juror-questions/JQ-N1.md`
- `exam-prep/fifth-fix/juror-questions/JQ-CANTEEN-8.md`
- `RULES.md`, `TACTICS.md`, `TEAM.md`, `README.md`, each in full
- `decisions/2026-09-19-{zero-trade-contracts, tokenized-equity, calm-separation,
  large-moment-selection, effort-level, watcher-across-runs,
  card-order-requirement}/verdict.md`
- `decisions/2026-10-01-jq-r04-gate/verdict.md`

The only listing I ran was one glob, `decisions/2026-09-19-*/verdict.md`, and it
returned only `verdict.md` files. I did not open, list or name anything in
`exam/`. I opened no other juror's file.

## Assumptions the instruction did not cover

1. **The engine's behaviour is as reported.** I took the question file's claims
   about the engine on trust: that start-hour, any and block are offered and
   behave as described, and that under start-hour no event has a unique size.
   `scripts/` is closed to me.
2. **"Same coin" scope.** I read JQ-CANTEEN-8 as covering calm moments of the
   same coin only, as its lines 71–74 frame it.
3. **Exact duplicates.** I assumed a calm moment drawn twice at the same start
   hour of one coin is one moment, not two. Whether the draw can produce that
   is not my question.
4. **Choosing before the result.** I assumed the exam result has not been
   opened, so RULES 6 still allows a choice to be made now.

## Steers and leaks I saw

- **The coordinator's instruction** has no result in it and no steer that I can
  find. Its sentence "If one of them already settles part of your question, say
  so" is neutral.
- **The question files contain measured results.** JQ-N1.md has event counts
  per reading (lines 89–101, 153–156, 214–218). JQ-CANTEEN-8.md has pair counts
  (lines 104–111). A referee has already judged measured counts in a juror
  instruction to be a valid RULES 3 fault (`decisions/2026-09-19-calm-separation/verdict.md`
  lines 26–27). These are observation-card figures, not exam figures, and they
  favour no option on their face. But they let a juror pick the reading whose
  numbers they like. My grounds are textual, and I say where I touched the
  figures: only to check executability, and in the case against.
- **JQ-CANTEEN-8 does not mention the ratified calm-separation verdict**, which
  already answered its part a. That is an omission rather than a steer. Still,
  the effect is to re-open a ratified question as though it were fresh. The
  referee should know that the question has been answered before.
