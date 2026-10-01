# Questions for the user

Written by Mateo · data engineer · seventh-fix run · 2026-10-01 (system
clock, RULES 23).

A question is here when answering it would make or change a rule, which no
juror may do (RULES 33) and which, by the first lines of `RULES.md`, needs
the user. Each question is written so that it can be answered without
opening the laboratory's exam-preparation files: what you need is explained
and quoted here. **Nothing here recommends an answer. Listing an answer is
not recommending it.**

---

## U-1 · When a field must stay on the exam card and still gives the coin away, does the exam's blindness check count it?

(This replaces a juror question, `JQ-R04-CONTENT-d`, which the data
engineer's seventh-fix run withdrew from jurors because it judged it to be a
question about a rule. You may judge otherwise; see the last answer of
part 1.)

### What you need to know

**1 · The exam hides the coin.** `RULES.md` line 41 (RULES 9): "In the exam
the coin name and the date are hidden." `TACTICS.md` lines 101–107 list
what is hidden on an exam card: "the coin name" · "the date and time" ·
"the price itself (converted to a number starting from 100)" · "the coin
name inside announcements" · "the Wikipedia number itself (given as a ratio
to the coin's own average)" · "the date in the release calendar".
`TACTICS.md` §3 (lines 55–62) lists what a card carries, for example
"price, volume, trade count, taker buy/sell pressure" and "bitcoin and
ethereum, over the same hours". What jurors are deciding about some of
these fields on exam cards is in point 4.

**2 · The blindness check (the "gate").** Before the exam's answer key is
sealed, a script, the laboratory's identity audit, reads all the exam cards
and tries to tell which cards belong to the same coin from the numbers
printed on them alone. From each card it computes many measured quantities,
called **features**: for example the typical level of a column, or how many
of a column's 24 values repeat. It attacks them in two ways, each compared
with its own chance line from RULES 12 (`RULES.md` lines 51–52: "The chance
line is not invented. The answers are shuffled 1,000 times, and the real
result must fall inside the best 1%."). Jurors have already ruled how the
gate decides, and that ruling stands
(`decisions/2026-10-01-jq-r04-gate/verdict.md` line 72): "The gate fails if
either the nearest-neighbour attack or the pair AUC attack beats its own
RULES 12 chance line on the exam cards." If the gate fails, the exam cards
are judged not blind and are not used.

**3 · What the gate grades.** The gate does not grade every feature. Its
written definition grades a set called `ALL-removable`, which is (quoted
from the gate's definition as it was put to jurors,
`exam-prep/third-fix/juror-questions/JQ-R04-GATE.md` lines 64–66): "every
feature in the audit's current list, minus the families that must stay on
the card because a frozen canteen rule or TACTICS requires them". (The
"frozen canteen book" is the laboratory's book of trading rules written from
the observation cards; `TACTICS.md` line 94: "Then the canteen book
freezes".) Today
four groups of features are outside the graded set:

- the column of hourly price changes;
- how many values repeat in that same column;
- the funding line;
- the price change and the high–low range printed in the one-line summary
  of the previous 7 days.

This question does not ask about these four, and no answer below changes
them. **Every feature, graded or not, is measured on the exam cards and
written, with its size, in the exam's manifest** (the record written with
the exam cards). The question is only which features can make the gate
fail.

**4 · Which fields stay on the exam card is being decided by jurors.**
Separate juror questions decide, under RULES 9 and TACTICS 3 and 6, what may
or must happen on an exam card to: the bitcoin and ethereum columns; the
names of US economic releases, and their offsets in hours, in the release
line; the trade-count column; how the price column is printed; and how the
nine columns printed as ranks get their order. Their rulings may keep a
field on the card, may allow more than one way of printing it (one of which
may leave it out), or may require it to be removed or masked. None of those
rulings exists yet. You do not need their questions to answer this one.

### What must be decided

When the jurors' rulings keep a field on the exam card, and the audit finds
on the exam cards that the features computed from that field still tell
coins apart better than chance, **does that make the gate fail?**

There are two parts. Part 2 is needed only if the answer to part 1 is B or
C.

### Which written rule it touches, and why it is a rule question rather than a definition

- **RULES 9** (`RULES.md` line 41, quoted above). Under answers B and C
  below, the exam can go ahead with cards on which the laboratory has
  measured a coin signature. The answer therefore decides what RULES 9
  requires of an exam: whether the coin is "hidden" when its name is not
  printed but the card still gives the coin away measurably. That is a
  standard the exam is held to, not the meaning of a word.
- **Changing a rule needs you.** `RULES.md` lines 3–4: "These rules do not
  change. If one must change, the user is asked first, and then it is
  written into `LEDGER.md`." Under answer A below, if a field the rulings
  keep fails the gate and no other way of printing it passes, the exam can
  go ahead only if a rule changes (what TACTICS 3 puts on the card, or what
  TACTICS 6 hides) or the signature is accepted. Either is yours.
- **Jurors may not.** `RULES.md` lines 119–121 (RULES 33): "A juror decides
  procedure and definition only: never a trading rule, never a threshold or
  score, and never a change to a rule in this file."
- **Why now.** `RULES.md` lines 34–35 (RULES 6): "The rule is written first,
  the result is opened second. A rule is not changed after looking at a
  result." Left open, the same question would reach you after the gate had
  been run on the exam cards, that is, after a result.
- **The other side.** The question can also be read as a definition: what
  the gate grades is set by the gate's own written definition, a text of the
  laboratory's exam preparation and not of `RULES.md`, and asking whether a
  field kept by a juror's ruling is one "that ... TACTICS requires" reads
  that definition. On that reading jurors could answer it. The two reviews
  of the juror question found the matter contested; the second found the
  case for the user the stronger one for answers B and C. Answer A on its
  own moves nothing and could be a juror's answer, but a juror question
  left with that one answer would not be a question. So the whole question
  is put to you.

### Part 1 · The answers, and what each would mean for the exam

- **A · The gate counts it.** The gate grades every feature the audit
  computes, except the four groups listed above. A field the rulings keep is
  graded like any other.
  *For the exam:* if such a field gives the coin away better than chance on
  the exam cards, the gate fails and the exam cards are not used. The
  laboratory then looks for another permitted way of printing that field
  that the audit no longer catches; if there is none, the matter comes back
  to you as a question about a rule (changing what TACTICS 3 puts on the
  card or what TACTICS 6 hides, or accepting the signature). Part 2 is not
  needed.

- **B · The gate does not count it; it is named, not graded.** A feature
  computed from a field that the rulings allow on the exam card, and that
  the exam card prints, is measured and named in the manifest with its size,
  but cannot make the gate fail.
  *For the exam:* the exam can go ahead with a coin signature measured on
  its cards in those fields; the manifest says how large it is; whoever
  reads the exam's result has to weigh that a candidate may have had that
  hint. Part 2 decides which fields this covers.

- **C · The gate counts it only where the card could do without the
  field.** A field that the rulings allow no exam card to be without is
  named, not graded, as in B. A field that the rulings allow but that some
  permitted way of printing the card leaves out is graded whenever the exam
  card prints it, as in A.
  *For the exam:* for a field the card cannot do without, as B; for a field
  it can do without, as A: if it gives the coin away, the gate fails unless
  the card leaves it out or prints it in a permitted way the audit no longer
  catches. Part 2 decides which fields this covers.

- **Other**, with reasons. Or: **this is a definition for jurors after
  all.** In that case a juror question has to be written again so that each
  of its answers can be carried out, and reviewed, before any juror sits.

### Part 2 · Only under B or C: which fields count as kept by the rulings

A ruling about one field may give a reason that, read generally, also
covers other fields (for example, a ruling that a column `TACTICS.md` §3
lists must stay could be read as covering only the column it was asked
about, or every column §3 lists).

- **Narrow · only the fields a ruling is about:** the bitcoin and ethereum
  columns, the release names, the release hour offsets, the trade-count
  column and the price column, each only as its own ruling says. Every
  other field is graded as under A (apart from the four groups listed
  above).
- **Wide · every field `TACTICS.md` §3 puts on the card**, unless a ruling
  requires it removed or masked (and, under C, unless a ruling allows a card
  without it), with each ruling read as far as its words reach. This takes
  in fields no juror question names, such as the other ranked columns and
  the numbers in the previous-7-day summary that are graded today.
  Mechanically, as the audit's code stands, every feature it computes is
  computed from a field `TACTICS.md` §3 lists; so under B with this reach
  no feature it computes today would be graded, and under C with this reach
  a feature would be graded only where a ruling allows a card without its
  field.

Under either reach: which features are computed from which field is read
from the audit's code, not chosen. Where it is unclear whether a ruling's
words reach a field, or a feature is computed from a field that is counted
and from one that is not, the run that builds the gate stops and the case
goes back to the coordinator; it is not settled by that run.

### What is deliberately not here

No measured figure: no count of features left graded under any answer
beyond what the answers' own wording implies, no size of any feature, and
nothing on whether the gate has passed or failed under any answer on the
observation cards measured so far. Such measurements exist in the
laboratory's exam-preparation files (`exam-prep/`), including the file cited
in point 3. They are left out for the reason the laboratory keeps them from
jurors: so that the choice rests on the wording and not on its result
(RULES 6). Whether to look at them before answering is yours. **Nothing has
been measured on exam cards.**

### How the answer is used

The run that builds the exam's blindness check composes the graded set as
your answer says, and names in its record every feature it moves out of the
graded set, the field it is computed from, and the part of your answer that
moves it. No answer changes the four groups listed in point 3, the gate's
ratified rule in point 2, or anything the jurors rule about which fields
stay.
