# Juror 3 — open question · the order in which cards reach a watcher

**Question:** what does `TACTICS.md` section 4 require of the order in which the
cards reach a watcher?

**Date:** 2026-09-19 · **Role:** juror (RULES 33–34) · **Model/effort:** opus / high

---

## 1 · Answer

Section 4 imposes **one requirement with two checkable halves, and leaves one
boundary case unsettled.**

The requirement, stated so a given order can be checked yes/no:

> **(a) Production.** The sequence handed to a watcher must be a *shuffle*: a
> permutation of the whole pool of cards of the 10 observation coins, produced
> by a randomising procedure, and not by any property of the cards — not the
> card's type, not its coin, not its date, not its creation or file order.
>
> **(b) Result.** In the delivered sequence the large-movement cards and the
> calm cards must be **mixed, not segregated**: the sequence must not present
> the two types as separate stretches (all large then all calm, or a sequence
> that decomposes into type-blocks), and a watcher must not be able to infer a
> card's type from its position in the sequence.

How to check a given order:

1. **(b) is checked on the sequence itself.** Take the delivered order, label
   each card large/calm, and ask: are the two labels distributed through the
   sequence, or does the sequence fall into stretches of one label? If the
   position of a card predicts its label, the order **fails**. This is
   answerable by inspection, with no number invented.
2. **(a) is *not* checkable on the sequence alone** and this is the sharpest
   thing I can say about the requirement. "Shuffled" is a property of the
   *procedure*, not of the output: every order, including the worst one, is a
   possible output of a fair shuffle. So (a) can only be checked against the
   record of how the order was produced — the procedure, and the input it was
   given. An order with no such record cannot be shown to satisfy (a); it can
   only be shown to satisfy (b).

Two consequences that follow directly and can be checked:

- The pool that is shuffled is **all the cards of the 10 coins together**
  (section 4: the watchers "read all the cards of the 10 coins"), so an order
  that keeps one coin's cards together, or keeps each coin's cards in time
  order, fails (a) even if it happens to pass (b).
- The requirement attaches to **the sequence as the watcher experiences it.**
  If the cards reach a watcher in more than one delivery, the no-segregation
  test of (b) applies across the whole sequence, not inside one delivery only.
  (How many deliveries, and how large, is not mine — see §5.)

**What the section does not choose between.** The colon in line 80 can be read
two ways, and the section does not say which:

- **Reading A (apposition).** "shuffled order: large moments and calm moments
  interleaved" = *shuffle the deck; the point of doing so is that the two types
  arrive mixed.* One act, randomisation, with its purpose named.
- **Reading B (two constraints).** *Randomise, and in addition enforce
  interleaving* — at the limit, strict alternation large/calm/large/calm.

I hold that the section **does** exclude the strict-alternation limit of
Reading B, because a strictly alternating order makes every card's type
predictable from its position, which is the one thing a shuffle is there to
prevent; strict alternation is a deterministic order, not a shuffled one. Note
that strict alternation is arithmetically *possible* here — TACTICS 2 gives
"the same number as the large moments" of calm moments — so it is not ruled out
by counting, only by the word "shuffled".

But the **weak form of Reading B is genuinely unsettled**: if a fair,
unconstrained shuffle happens to place a long stretch of same-type cards
together, section 4 does not say whether that order must be re-drawn or
constrained, or whether it stands because the procedure was honest. Reading A
says it stands; weak Reading B says re-draw. **Nothing in section 4, or
anywhere else in the files I was allowed to read, chooses.** Saying which one
wins would require fixing a number ("how long a stretch is too long"), and
RULES 33 forbids a juror to set one. So: unsettled, and it is the next open
question if anyone needs it settled.

**What every reading forbids** — the safe, unanimous core: an order built
coin-by-coin or date-by-date, and an order in which the two types arrive
separated. An order can be failed on those grounds under any reading.

**Reversible or irreversible.** Fixing the order *before* the watchers run is
reversible and cheap: nothing about the cards themselves changes, only the
sequence they are handed in. Fixing it *after* watchers have read and written
notes is not: the notes were taken under the order effect, and correcting the
order means re-running free observation for all four watchers over all the
cards of the 10 coins, and discarding the notes already written. I have not
measured that cost and I do not write a number for it; RULES 25 puts the
measurement of the first 10 cards' tokens in `LEDGER.md`, which I did not read.

---

## 2 · What it rests on

**`TACTICS.md`, section 4 "Free observation", line 80** — the whole of the
requirement:

> `- Cards are given in shuffled order: large moments and calm moments interleaved.`

**`TACTICS.md`, section 4, line 78–79** — fixes the pool that is shuffled:

> `- The four watchers (Ingrid, Kenji, Amara, Lukas) read all the cards of the 10`
> `  coins. Each takes notes from their own field of view.`

**`TACTICS.md`, section 2, line 42–43** — why both types exist in the pool in
equal number, which is what makes strict alternation arithmetically possible
and therefore worth excluding explicitly:

> `- **Calm moment:** the same number as the large moments, chosen at random. At`
> `  least 72 hours away from any large movement.`

**`.claude/agents/watcher-high.md`, lines 51–55** — the laboratory's own
paraphrase of line 80, which drops the word "interleaved" and replaces it with
the *effect* the order must have on the watcher. This is my main ground for
reading the clause after the colon as the purpose of the shuffle, and for
stating (b) as "cannot infer type from position":

> `Cards arrive in **shuffled order.** Among them are moments of large movement and`
> `moments where nothing at all happened, and **you are not told which is which.**`

Also from that file, lines 54–55, the reason the mixing matters — the calm
cards are not filler:

> `If you see no large movement in a card's "after" section, that card is a calm`
> `moment — and **it matters just as much as the other kind**`

**`TACTICS.md`, section 3, line 51–53** — the fact that in free observation the
watcher *can* tell the two apart from the card's own content, so the order's job
is not concealment but the removal of an ordering artefact:

> `- **After:** the 24 hours after the start. Shown only in free observation, never`
> `  in the exam.`

**`RULES.md`, rule 33, lines 118–121** — why I stop short of choosing inside
the weak Reading B:

> `A juror decides procedure and definition`
> `    only: never a trading rule, never a threshold or score, and never a change`
> `    to a rule in this file.`

**Where I looked and found nothing further.** I read the whole of `RULES.md`,
`TACTICS.md`, `README.md`, `TEAM.md` and `.claude/agents/watcher-high.md`, and
searched each of those five files by name for `shuffl|interleav|order|random`
(case-insensitive). Results: **"interleaved" occurs exactly once in all five
files — `TACTICS.md` line 80.** "Shuffled order" occurs twice — `TACTICS.md`
line 80 and `watcher-high.md` line 51. The other hits are the chance-line
shuffling of *answers* (`TACTICS.md` 125, 136; `RULES.md` 12), the random
trade-time rival (`TACTICS.md` 147, 157), "order book depth" (`TACTICS.md` 59,
`TEAM.md` 42) and the random choice of calm moments (`TACTICS.md` 42). `README.md`
has no hit at all. **Neither "shuffled" nor "interleaved" is defined anywhere in
the files I may read, and no seed, no procedure and no per-watcher clause is
given for the card order.** I did not read `LEDGER.md`, `scripts/`, `cards/`,
`decisions/` or `instructions/` — closed to me by the instruction — so a
definition may exist there; see §4.

---

## 3 · The strongest case against my own answer

**The strongest objection: I have read a purpose into the text that the text
does not state, and I have used an agent definition to override the rule file.**

Line 80 says "interleaved". It does not say "not inferable from position", and
it does not say "randomised production with a record". Those are my words. The
word actually on the page, *interleave*, in its ordinary sense means to lay
alternately — and TACTICS 2 makes the counts equal, so strict alternation is
exactly what the author could have meant and could have implemented. Under that
reading my answer is wrong in a way that matters: an order I would pass (a fair
shuffle with an accidental run of same-type cards) fails, and an order I
explicitly fail (strict alternation) passes.

My reply is that strict alternation contradicts "shuffled" in the same
sentence — but that reply is weaker than it looks, because a *constrained*
shuffle (shuffle within each type, then alternate) is both shuffled and
alternating, and satisfies both words at once. That construction is the real
threat to my answer and I could not rule it out from the text. I rule it out
only on the ground that it makes type positionally predictable, and that ground
comes from `watcher-high.md` — an **agent definition**, which the definition
itself subordinates to the rule files: "If anything below contradicts those
files, **those files win**" (`watcher-high.md`, lines 28–30). I am using the
subordinate document to settle a reading of the superior one. That is legitimate
as evidence of how the laboratory has understood its own rule, but it is not
authority, and a referee would be right to mark it.

**A second, narrower objection.** I asserted the shuffle runs over the whole
pool including across coins. Line 80 only mentions the *type* dimension. A
reader could hold that the section settles only the type dimension and says
nothing about coin or chronology — in which case an order grouped by coin but
type-mixed inside each coin would pass. I think "Cards are given in shuffled
order" is unqualified and so covers the whole delivered set, and that the clause
after the colon names the dimension that matters most rather than the only one
constrained. But the text does not say this, and I may be over-reading.

**A third.** I said (a) cannot be checked from the sequence alone. Someone could
answer that this makes half my requirement uncheckable and therefore useless as
a rule, and that the practical requirement must be read as purely a property of
the resulting sequence. I accept the force of this and that is why I split the
answer into (a) and (b) rather than pretending one test covers both — but it
does mean an order with no production record sits in a state my answer cannot
resolve, only describe.

---

## 4 · Confidence

**4 out of 5** — for the core: the no-segregation test (b) and the prohibition
on coin-order/date-order delivery. Every reading of line 80 I can construct
agrees on that core.

**2 out of 5** — for the exclusion of the constrained-shuffle-then-alternate
construction. That is the weakest joint in my answer and I have written it as
such in §3.

**Unsettled, confidence not applicable** — whether a fair shuffle that produces
a long same-type stretch must be re-drawn. I claim the section does not choose,
and I am deliberately not choosing for it (RULES 33).

**What would change my mind:**

- A line in `LEDGER.md`, or a ratified entry in `decisions/`, or the
  card-delivery script, that fixes the shuffle's procedure, its seed, or defines
  "interleaved" operationally. I was not allowed to read any of those. Such a
  line, written *before* the order was built, would settle both (a) and the
  unsettled boundary case, and would beat my textual reading — RULES 6: "The
  rule is written first, the result is opened second."
- Any sentence anywhere in `TACTICS.md` or `RULES.md` using "interleaved" in a
  sense that requires alternation. I searched both files by name and there is
  none; a second occurrence would move me toward Reading B.
- Being shown that TACTICS 2's equal counts hold *per delivered sequence* and
  not merely per coin, which would make strict alternation clean to implement
  and strengthen Reading B further.

**What would not change my mind:** being shown an order that was actually built
and told it is fine. Whether a built order passes is not my question, and RULES
6 forbids fitting the rule to the result after looking at it.

---

## 5 · Out of scope, named

Things I did **not** answer, by name, so the referee can see the edges:

1. **Whether any order already built meets this requirement.** Excluded by the
   instruction; I was shown no order and looked for none.
2. **Batch size, batch count, run order.** Excluded by the instruction. My §1
   statement that (b) applies "across the whole sequence the watcher sees" is
   about where the test is applied, not about how many batches there should be
   or how big they should be.
3. **Whether the four watchers get the same order or four independent orders.**
   Section 4 says "Cards are given in shuffled order" and never says to whom,
   singular or several. **This is a real gap and I flag it rather than fill it.**
   I note only that the pilot line ("the same 10 cards are read at two effort
   levels", `TACTICS.md` line 74) makes the order a potential confound in the
   effort comparison, which `watcher-high.md` lines 19–21 says must differ in
   nothing but effort. That is an argument, not an answer, and it belongs to a
   separate jury.
4. **Any number** — how long a same-type run may be, what fraction of the
   sequence may be one type, any score. RULES 33.
5. **Any change to `RULES.md`.** None proposed. RULES 33; and RULES.md line 3:
   "These rules do not change."

---

## 6 · Files read

- `/home/user/balikcil/RULES.md` (whole)
- `/home/user/balikcil/TACTICS.md` (whole)
- `/home/user/balikcil/README.md` (whole)
- `/home/user/balikcil/TEAM.md` (whole)
- `/home/user/balikcil/.claude/agents/watcher-high.md` (whole)

Plus five name-scoped searches, one per file above, for
`shuffl|interleav|order|random`. No folder-wide glob was run. `exam/` was not
opened, listed, or named. No other juror's answer was read; I did not list the
`decisions/` folder and wrote my file into it blind. No memory-search or
session-log tool was run.

## 7 · Steer

Two things in the instruction I report rather than pass over, neither of which I
think rises to a RULES 3 breach on its own:

1. **"If the section admits more than one requirement and does not choose
   between them, say so."** This is a conditional and carries no result, but it
   does name one of the two possible outcomes and invites it. A juror primed to
   look for ambiguity is more likely to report ambiguity. I flag it because my
   answer *does* report an unsettled point, and the referee should weigh that
   the instruction suggested the shape of that finding. I believe I would have
   reached the same split from line 80's colon unprompted — the sentence is
   genuinely two-way — but I cannot prove that about myself.
2. **"Whether any order already built meets your answer is not yours — you are
   not shown one."** This tells me an order probably exists and may be in
   dispute. It is context, not a result, and it did not point me at a reading.

Nothing in the instruction told me what to look for inside section 4, named a
type of order, or suggested an answer.
