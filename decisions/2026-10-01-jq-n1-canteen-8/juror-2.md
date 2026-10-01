# Juror 2 · JQ-N1 (parts 1–4) with JQ-CANTEEN-8 (parts a, b)

Written 2026-10-01 without seeing any other juror's answer. I opened nothing
in `decisions/2026-10-01-jq-n1-canteen-8/` except this file, which I wrote.

---

## 1 · Answer

**JQ-CANTEEN-8 (a): yes.** Two calm moments of one coin may overlap. TACTICS 2
sets no calm-to-calm spacing, and a jury already settled this point 3–0 on
2026-09-19 (`decisions/2026-09-19-calm-separation/verdict.md`).

**JQ-CANTEEN-8 (b): does not arise**, because (a) is "yes".

**JQ-N1-1: start-hour.** Two moments are "in the same hour" when they begin in
the same clock hour.

**JQ-N1-2: does not arise** under start-hour. If the referee settles part 1 on
a wider reading, my conditional answer is **component**, and the second
convention (earliest/latest) does not arise. Of the two options, component is
the only one that never splits a pair the rule says "count as a single event".
Greedy-clique can split such a pair.

**JQ-N1-3: yes (scope `any`).** Two moments of one coin may be one event. Under
start-hour this happens only when two cards of one coin share a start hour.
Such cards show one and the same 24-hour movement, which is what TACTICS 7
line 127 describes: "a moment appearing in several cards". On the observation
cards this choice changes no number: the `any` and `cross-coin` rows are the
same under start-hour.

**JQ-N1-4: representative.** Each event counts once, and the shuffle runs over
n = number of events.
- **4a:** the rules do not settle which card represents an event. They require
  only that the choice is fixed before the result is opened and does not
  depend on any answer or label (RULES 6). The question's example (earliest by
  start hour, ties by lowest card number) meets that requirement, and I accept
  it as procedure. Under start-hour every card of an event has the same start
  hour, so in practice the choice is always the lowest card number.
- **4b:** the event takes the label of its representative card. Under
  representative, the event *is* that card, with that card's answer and that
  card's key label. No separate mixing convention is needed, so 4b follows
  from 4a.

**How the parts depend on each other.**
- Part 2 depends on part 1.
- The answer to part 3 is the same whichever resolution is chosen. Its effect
  is not: under start-hour it touches only identical-hour pairs.
- Part 4 assumes start-hour. Under start-hour the mixed large+calm events
  number 2 on the observation cards (question's table). Under the wider
  readings they number 37–60, and representative events would stand for
  chains of up to 20 cards. I would not hold 4a/4b at the same confidence
  under a wider reading.
- CANTEEN-8 (a) "yes" leaves same-coin calm overlaps in the set. Under
  start-hour those overlaps stay separate events unless the two start hours
  are identical, so CANTEEN-8 has almost no effect on JQ-N1 under my answers.

**Can the four answers be carried out together?** Yes: start-hour + `any` +
representative (4a as above, 4b = representative card's label). Unknown, by
name: I was not allowed to open the engine. JQ-N1 says it offers both scopes
and the block shuffle. It does not say whether it offers representative
scoring. If it does not, representative is engineering still to be written,
and that must be done before the exam result is opened (RULES 6).

---

## 2 · What it rests on

### CANTEEN-8 (a), (b)
- `decisions/2026-09-19-calm-separation/verdict.md` lines 48–50: "**RATIFIED
  3–0** · Section 2 of TACTICS.md requires no minimum distance between two calm
  moments of the same coin. The 48-hour clause sits inside the large-movement
  definition; the calm bullet defines separation only as 72 hours from any
  large movement."
- `TACTICS.md` lines 36–39: the 48-hour clause is a sub-bullet under
  "**Large-movement moment:**" (line 36): "  - Of two moments closer than 48
  hours to each other, only the larger counts."
- `TACTICS.md` lines 42–43: "**Calm moment:** the same number as the large
  moments, chosen at random. At least 72 hours away from any large movement."
  This is the only spacing written for a calm moment, and it is relative to
  large movements.
- `RULES.md` lines 34–36 (RULES 6): "A rule is not changed after looking at a
  result. If it is changed it counts as a new rule, carries the 'afterwards'
  label, and is tested again." A calm-to-calm spacing would add a clause to
  TACTICS 2. That is a new rule, not a reading. It would also be added after
  the 306 observation cards and their overlap counts were already seen.
- The 48 h / 24 h spacings offered in part (b) come from
  `data/overlap/overlap-manifest.md`, a measurement file (as quoted in
  JQ-CANTEEN-8 lines 80–83), and from the shape of the card (TACTICS 3). Neither
  is written as a spacing rule. If the answer to (a) were "no", a juror would
  be choosing a number of hours, which RULES 33 forbids (lines 120–121: "never
  a threshold or score").

### JQ-N1-1
- `RULES.md` lines 53–54: "Moments occurring in several coins in the same
  hour count as a single event." The rule says "the same hour", singular.
- `TACTICS.md` line 44: "A moment's start is the hour at which the 24-hour
  movement began." This is the only line in the laboratory's documents that
  gives a moment an hour. It gives exactly one.
- `TACTICS.md` line 127: "A moment appearing in several cards in the same hour
  counts as a single event." The subject is *one* moment shown on *several*
  cards. With "one page per moment" (`TACTICS.md` line 48), the cards in
  question are those whose moment has the same hour. I do not read this line
  as saying that the 48-hour spans of different cards share an hour, which is
  the card-span ground.
- Structural ground: start-hour is the only reading under which the text alone
  turns moments into events. The question says so itself (JQ-N1 line 162):
  "Under start-hour the relation is transitive and part 2 does not arise."
  The two wider readings need a chain-breaking rule. The question calls the
  greedy-clique rule "a stated convention, not an observation" (line 125), and
  its sub-rule "a second convention, written in no rule" (lines 133–134). A
  reading that needs unwritten rules to work is weaker than one that needs
  none (RULES 34: an answer rests on a written line).
- Reductio: if the wider readings are applied as literally as the rule's words
  allow, the result is component (see part 2). Component chains can join
  moments whose start hours are any distance apart. The question's table shows
  events of up to 20 cards under card-span/component (line 98). I did not
  measure the time span of those events. The logic alone shows that "the same
  hour" would stop limiting anything.

### JQ-N1-2 (conditional)
- `RULES.md` lines 53–54: "... count as a single event." If A and B must be one
  event, and B and C must be one event, then A, B and C are one event, because
  being the same event is transitive. The rule's own words therefore produce
  the transitive closure, which is **component**.
- Greedy-clique gives up this property. A moment that shares an hour with two
  others can be put into one event while the other is left for a later round,
  so two moments that share an hour can end up in different events. That
  contradicts the sentence the convention is meant to carry out. The question
  states it as unwritten (lines 125, 133–134).

### JQ-N1-3
- `TACTICS.md` line 127: "A moment appearing in several cards in the same hour
  counts as a single event." This is the scoring rule in Greta's section, and
  it says "cards", not "coins".
- `RULES.md` lines 53–54 says which moments *must* be one event (those of
  several coins in one hour). It does not say that moments of one coin *may
  not* be. The two lines do not conflict: `any` satisfies both.
- `TACTICS.md` line 39 (48 h between large moments of one coin) and line 43
  (72 h between a calm moment and a large movement) rule out a same-hour
  same-coin pair in every case except two calm moments. Such a pair, with an
  identical start hour, is the same coin over the same 48 hours: one moment
  on two cards, the case line 127 names.
- JQ-N1 lines 92–93: the start-hour rows for `any` and `cross-coin` are
  identical (289 / 274 / 3 / 2 / 0 / 1).

### JQ-N1-4
- `TACTICS.md` line 127: "... **counts** as a single event." Under block, a
  3-card event still contributes three answers to the real result. It is
  moved as a unit in the shuffle, but in the score it counts three times.
  Representative counts it once, as the line says.
- `RULES.md` line 53, the second sentence of RULES 13: "If the whole market
  moved together, that is one event." "One event", not one event weighted by
  how many coins were drawn.
- 4a: `RULES.md` lines 34–35: "The rule is written first, the result is opened
  second." This is the only constraint the documents put on the choice. No
  line names a card.
- 4b: it follows from the definition of representative given in the question
  (JQ-N1 line 219: "each event is replaced by one card"). A card carries its
  own key label.

---

## 3 · The strongest case against my answer

**Against CANTEEN-8 "yes".** Two calm cards of one coin that start 14 hours
apart share 34 of their 48 hours, so they are not two independent
observations. The laboratory already spaces every other pair of a coin's
moments, and a careful designer would not have meant calm moments to be the
one exception. RULES 13 shows the laboratory cares about double counting. On
this view the missing calm-to-calm spacing is an oversight in the drafting,
not a choice. My reply: that is an argument for *adding* a rule. Under RULES 6
that is a new rule, and RULES 33 forbids a juror to make it. The double
counting it worries about is what RULES 13 / JQ-N1 handle at scoring time. One
more point against my use of precedent: nothing in RULES G says a ratified
verdict binds a later jury. I rely on it as the same question already
answered. If a referee holds that verdicts do not bind, my answer still stands
on TACTICS lines 36–43 alone.

**Against start-hour (the strongest objection to my whole answer).** RULES 13's
second sentence states the purpose: a market-wide move is one event. Each
coin's start hour is chosen separately, as the hour where *its own* largest
24-hour change began. In one market-wide drop, coins can begin their moves
some hours apart. Start-hour would then count one market move as several
events, which defeats the rule's stated purpose. The small collapse it
produces on the observation cards (306 → 289; JQ-N1 line 92) fits that
worry. A moment "occurs" over 24 hours (TACTICS 2 calls it a 24-hour
movement), so "occurring in the same hour" can fairly mean that the two
movements share an hour (move-window). I take this seriously. I still choose
start-hour because the wider readings cannot be carried out from the text
without unwritten conventions, and because the literal version of them
(component) lets "the same hour" join moments that are days apart. I have not
measured how often a market-wide move in the exam set spreads over adjacent
start hours. If it is common, start-hour does not serve RULES 13's purpose
well.

**Against component as the conditional part 2.** Component can join moments
far apart in time. It also does not deliver `cross-coin` (10 and 26 same-coin
events; JQ-N1 lines 179–183), so it is an odd partner for anyone who reads
RULES 13 as "several coins" only. Greedy-clique keeps every event within one
real shared hour, which is closer to the spirit of "same hour".

**Against `any` in part 3.** RULES 13 says "in several coins". Read strictly,
a rule about cross-coin coincidence gives no warrant to merge moments of one
coin. Under start-hour the point is almost empty: no observation case exists.

**Against representative (part 4).** RULES 12 line 51 says "The answers are
shuffled", meaning all of them. Representative throws away every answer but
one in each multi-card event. Block keeps every card and makes the event the
unit of the shuffle, which is a correct statistical way to treat correlated
cards. It needs no 4a or 4b and is already implemented and checked (JQ-N1
lines 202–218). Representative also needs 4a, which rests on no written line.
That is the same weakness I hold against greedy-clique. My distinction is
that 4a's convention contradicts no written sentence, while greedy-clique's
can split a pair the rule says to join. Against 4b: one could argue that an
event holding a large card is a market moment that moved, so it should be
labelled large whatever card represents it.

---

## 4 · Confidence, and what would change my mind

| part | answer | confidence (1–5) | what would change my mind |
|---|---|---|---|
| CANTEEN-8 a | yes | 5 | A written line in RULES or TACTICS that spaces calm moments of one coin; or a ruling that the 2026-09-19 calm-separation verdict answered a different question. |
| CANTEEN-8 b | does not arise | 5 | Only if (a) became "no". Then I would answer "other": the rules give no spacing, and choosing 48 h or 24 h is choosing a number. |
| JQ-N1-1 | start-hour | 3 | A written line giving a moment more than one hour, or a measurement showing exam market-wide moves routinely spread over adjacent start hours. |
| JQ-N1-2 | does not arise; conditionally component | 3 | A written line that limits an event to moments that all share one hour. That would make greedy-clique the text, not a convention. |
| JQ-N1-3 | any | 4 | A line saying same-coin moments must never be merged. |
| JQ-N1-4 | representative | 3 | A reading of TACTICS 7 line 127 that ties "counts as a single event" to the shuffle unit rather than the score. |
| JQ-N1-4a | earliest by start hour, then lowest card number (a choice, not a reading) | 2 | Any written line naming a representative. |
| JQ-N1-4b | the representative card's label | 3 | A line that defines an event's label separately from its cards. |

**Reversible and irreversible.**
- Every JQ-N1 answer is a definition that a script applies to a sealed key. It
  costs a re-run to reverse **before** the exam result is opened. After that,
  any change is "afterwards" (RULES 6) and must be tested again.
- CANTEEN-8 "yes" changes nothing now.
- A "no" would change how exam calm moments are drawn. If the exam draw and
  answer key already exist, reversing a "no" later would mean a redraw and a
  reseal. JQ-N1 line 84 speaks of "the sealed answer key"; I could not check
  whether it exists yet.

**Rule change:** none. Nothing here changes `RULES.md` or sets a threshold, a
score, a number of shuffles, the 1% line, or a trading rule.

---

## Faults in the question I am reporting

1. **CANTEEN-8 does not mention the ratified answer to its own part (a).**
   `decisions/2026-09-19-calm-separation/verdict.md` already rules, 3–0, that
   TACTICS 2 requires no calm-to-calm minimum distance. JQ-CANTEEN-8 offers
   "no" as an open option and argues for it ("TACTICS 2 spaces every other
   pair of one coin's moments, and calm moments are no exception", line
   125–127). The ratified verdict rejected that reasoning: "The 48-hour clause
   sits inside the large-movement definition". Re-referring a ratified point
   without saying so invites a second jury to reverse the first.
2. **Measured results and emphasis in the question (possible RULES 3 steer).**
   Both files carry counts measured on the observation cards. They are not
   exam results. However, the 2026-09-19 calm-separation referee judged
   measured pair counts in a juror question to be a RULES 3 fault (verdict
   lines 26–30). JQ-N1 also bolds one figure ("**26**", line 99) and adds
   "more than card-span/component/any's 25" (line 183), which draws attention
   to a weakness of one option. Lines 185–191 tell the juror which
   combinations "can" and "cannot" be carried out. That is accurate, but it
   is guidance toward some options. In my own reasoning I did not rest
   on any count except the identity of the two start-hour rows (line 92–93),
   which I used only to show that part 3 changes no number there.
3. **Part 1's card-span ground misreads TACTICS 7 line 127**, in my view. The
   line's subject is one moment on several cards, not overlapping card spans.
   This is a disagreement, not a leak.

I saw no steer in the coordinator's instruction itself.

## Files I read

- `exam-prep/fifth-fix/juror-questions/JQ-N1.md`
- `exam-prep/fifth-fix/juror-questions/JQ-CANTEEN-8.md`
- `RULES.md`, `TACTICS.md`, `TEAM.md`, `README.md` (whole)
- `decisions/2026-09-19-{calm-separation, large-moment-selection,
  card-order-requirement, zero-trade-contracts, tokenized-equity,
  effort-level, watcher-across-runs}/verdict.md`
- `decisions/2026-10-01-jq-r04-gate/verdict.md`

One glob was run, with the exact pattern the instruction permits:
`decisions/2026-09-19-*/verdict.md`. Nothing in `exam/` was opened or listed.

## Assumptions not covered by the instruction

- **A1.** A ratified verdict from 2026-09-19 is the laboratory's settled
  reading on its question unless the user changes a rule. RULES G does not
  say so in words.
- **A2.** On whether a coin can have two calm moments with an identical start
  hour, I rely on JQ-N1's statement that none exist in the observation set
  (line 139–140). I could not check whether the calm draw allows it at all.
- **A3.** Whether the engine implements representative scoring is unknown to
  me (see Answer).
- **A4.** Whether the exam moments are already drawn and the key sealed is
  unknown to me.
