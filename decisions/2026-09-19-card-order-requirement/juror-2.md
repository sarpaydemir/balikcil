# Juror 2 — what TACTICS 4 requires of the order in which cards reach a watcher

Question answered: **what does `TACTICS.md` section 4 require of the order in
which the cards reach a watcher?**

---

## 1 · Answer

TACTICS 4 requires that the sequence in which a watcher receives cards be the
output of a **shuffle applied to the whole set of cards the watcher is to read**,
and that the two kinds of moment be **mixed through that one sequence rather
than segregated** — in short, **the position of a card in the stream must not
tell you what kind of card it is.**

An order can be checked against this with five yes/no tests. The order **fails**
if any of tests 2–5 is answered "yes".

1. **Completeness / both kinds present.** Does the sequence contain all the
   cards of the 10 observation coins, and are both large-movement moments and
   calm moments in it? (Must be **yes**.)
2. **Inherited order.** Can the sequence be reproduced by sorting the cards on
   some card attribute — moment kind, coin, card number, timestamp, file
   listing order? If yes, it is not shuffled → fail.
3. **Segregation by kind.** Is there a cut point such that all the large moments
   lie on one side of it and all the calm moments on the other? Or is each kind
   delivered as one unbroken run? If yes → fail ("interleaved" is denied).
4. **Segregation by coin.** Is the sequence grouped so that all of one coin's
   cards are contiguous, coin after coin? If yes → fail (that is the unshuffled
   generation order, not a shuffle).
5. **Positional rule for the kind.** Does some fixed rule from position to kind
   hold across the sequence — strict alternation large/calm/large/calm, every
   even position calm, every third card large? If yes → fail. Strict
   alternation fails *both* limbs: it is not a shuffle, and it makes the kind
   readable off the position.

A uniformly random permutation of the full card set, drawn without reference to
the card's kind or coin, passes all five by construction. That is the ordinary
way to satisfy the section, and it is what the section's plain words describe.

**Where the section stops — and it does stop.** The sentence carries two
clauses joined by a colon, and it does not say whether the second is a gloss on
the first or an extra constraint:

- **Reading A (gloss).** "Shuffled" is the requirement; "large moments and calm
  moments interleaved" only names the consequence. A plain random shuffle
  satisfies it even if chance produces a long run of one kind.
- **Reading B (extra constraint).** Interleaving is required *in addition*, so a
  shuffle that happens to deliver, say, many same-kind cards in a row must be
  re-drawn or stratified.

**Section 4 does not choose between A and B, and nothing else in `TACTICS.md` or
`RULES.md` chooses for it.** Reading B needs a run-length or balance limit to be
checkable, and no such number appears anywhere in the two files. **Supplying
that number is not a juror's business** (RULES 33: "never a threshold or
score"), so I state the gap rather than close it. Test 3 above is the part of
interleaving that *is* checkable without inventing a number: total segregation
is forbidden under either reading.

Two further gaps I found and do **not** fill, because section 4 is silent:

- **Same order for all four watchers, or one shuffle each?** Section 4 says
  every watcher reads all the cards; it says nothing about whether they share a
  permutation.
- **Must the shuffle be seeded and reproducible?** Section 4 says nothing. The
  laboratory's habit elsewhere is to make draws reproducible (TACTICS 1), and
  RULES 29 makes runs reproducible from their input, but neither is a statement
  about *this* line, so I record it as a gap, not as a requirement read into the
  section.

One sub-point the section's own wording does settle against a shuffle taken
loosely: for the **pilot**, the section fixes the card *set* ("the same 10
cards"), not the order. Holding the order constant across the two effort levels
is what the pilot's purpose demands (see the quote from `watcher-high.md` in
§2), but the words of section 4 do not require it. I flag it; I do not decide
it, because the pilot's run arrangement was put outside my question.

**Reversibility.** Everything above is a reading of existing text, so adopting
it is reversible at the cost of re-shuffling and re-issuing card sequences; no
measurement, note or ledger number depends on it yet. If watchers have already
read cards under a different order, reversing costs the observation run itself —
notes taken under one order cannot be re-taken under another by the same agent
without contaminating them. That is the irreversible side, and it is why this
should be settled before, not after, cards go out. Whether any built order meets
the answer is explicitly not mine.

---

## 2 · What it rests on

The whole of the requirement is one line. `TACTICS.md`, section 4, line 80:

> Cards are given in shuffled order: large moments and calm moments interleaved.

Its immediate context, `TACTICS.md` lines 78–79, fixes what "the cards" means
and who receives them:

> The four watchers (Ingrid, Kenji, Amara, Lukas) read all the cards of the 10
> coins. Each takes notes from their own field of view.

— which is why test 1 asks for the full set and why test 4 treats coin-grouping
as unshuffled: a single watcher's stream spans all ten coins.

`TACTICS.md` line 74 (the pilot line), for the card-set-vs-order point:

> **Pilot:** the same 10 cards are read at two effort levels.

`.claude/agents/watcher-high.md`, lines 52–54, is the laboratory's own gloss on
the same line, and it is what grounds the "position must not reveal the kind"
formulation:

> Cards arrive in **shuffled order.** Among them are moments of large movement
> and moments where nothing at all happened, and **you are not told which is
> which.**

The same file, lines 19–21, is what makes order-constancy matter for the pilot:

> **Nothing else differs.** If you ever find a difference between the two other
> than the effort line, the name, the description and this paragraph, stop and
> report it — the comparison would be invalid.

`TACTICS.md` line 43 shows the two kinds are equal in number, so strict
alternation is arithmetically available and has to be excluded on other grounds
(tests 2 and 5), not by counting:

> **Calm moment:** the same number as the large moments, chosen at random.

`RULES.md` 33, lines 120–121, is why I leave the interleaving criterion
unquantified:

> A juror decides procedure and definition only: never a trading rule, never a
> threshold or score, and never a change to a rule in this file.

For the reproducibility gap, the nearest neighbouring text — `TACTICS.md` line
21, "Ties are broken by symbol name ascending, so the ranking is reproducible",
and `RULES.md` 29, lines 95–96, "Every run has a number: the fingerprint of its
input. The same input gives the same number and the same result." Neither
mentions the observation shuffle; that is precisely my point in calling it a
gap.

**Where I looked before saying the section settles nothing more.** I read the
whole of `TACTICS.md`, `RULES.md`, `README.md`, `TEAM.md` and
`.claude/agents/watcher-high.md`. Outside section 4, the only other mentions of
card order I found are the `watcher-high.md` lines quoted above and its round
rules (lines 120–124), which govern *what* a watcher may read in each round, not
the sequence. `README.md` step 3 (lines 40–41 region) describes free observation
without mentioning order at all. `RULES.md` contains no rule about card order;
RULES 9 hides names and dates in **the exam**, not in free observation.

---

## 3 · The strongest case against my own answer

**The blinding rationale is weaker than my formulation implies, and that could
make test 5 too strict.** In free observation the watcher sees the "After"
section — `TACTICS.md` line 52: "**After:** the 24 hours after the start. Shown
only in free observation, never in the exam." A watcher therefore learns each
card's kind by reading it. So "the position must not tell you what kind it is"
buys very little concealment: the card tells you anyway, one card later. On that
view the real purpose of the line is only to stop the watcher reading twenty
large moments in a row and then twenty calm ones — an order effect, a drift of
attention — and a schedule that alternates strictly would serve that purpose
perfectly well. If that is the purpose, my test 5 forbids something the section
never meant to forbid, and the honest requirement would be just tests 1–4.

I do not think this defeats the answer, because "shuffled" is an ordinary word
and strict alternation is not a shuffle by any ordinary use of it — test 5's
verdict on alternation already follows from test 2 alone. But it does mean test
5 is doing less independent work than it appears to, and someone who reads the
colon as an exhaustive gloss (Reading A) can fairly say test 5 is redundant
rather than required.

**Second, narrower objection: test 4 may over-read.** The colon names only the
large/calm mixing. One can argue "shuffled" is defined *by* that colon and so
reaches only the kind of moment, leaving a coin-by-coin grouping permitted so
long as each coin's block is internally mixed. I reject this because "shuffled
order" governs the sentence's subject, "Cards" — all of them — and because line
78 makes the stream span all ten coins, but the reading is available and it is
the point at which my answer is least forced by the text.

**Third: I may be over-declaring ambiguity.** The instruction invited me to say
if the section admits more than one requirement. A reader less primed than I was
might simply say "shuffled, both kinds mixed together" and call it settled. My
A/B split is real, but it only bites in the case of an unlucky random draw, and
a laboratory that shuffles honestly and records its seed may never meet it.

---

## 4 · Confidence

**4 of 5** for the core: shuffle over the full card set, both kinds mixed
through one sequence, no segregation by kind or by coin, position carrying no
rule for the kind. **5 of 5** for the narrower claim that total segregation by
kind — all large then all calm — fails the line, since that reading contradicts
the word "interleaved" outright under every reading of the colon.

**4 of 5** for the claim that the section does *not* choose between Reading A
and Reading B, and therefore fixes no criterion for how much clustering a
shuffle may show.

What would change my mind:

- A line elsewhere in `TACTICS.md` or `RULES.md` — or in the card-writing or
  shuffle script's own specification, which I was not shown — that defines
  "interleaved" operationally, or that fixes the shuffle's seed and
  per-watcher scope. That would collapse the A/B gap and I would withdraw it.
- A showing that the four watchers are meant to receive *different* orders; that
  would not change tests 1–5 for any single watcher, but it would change what
  "the order" names and would settle the pilot sub-point against holding order
  constant.
- On test 4 specifically: any text indicating that cards are delivered per coin.
  I found none in the five files I read; if it exists outside them, it would
  overturn that test.

---

### Files read
`/home/user/balikcil/TACTICS.md` · `/home/user/balikcil/RULES.md` ·
`/home/user/balikcil/README.md` · `/home/user/balikcil/TEAM.md` ·
`/home/user/balikcil/.claude/agents/watcher-high.md`

Nothing in `exam/`, `decisions/`, `instructions/`, `notes/`, `canteen/`,
`cards/`, `reports/`, `scripts/`, `data/`, `LEDGER.md`, or the rest of
`.claude/` was opened or listed. No other juror's answer was seen.

### Assumed, because the instruction did not cover it
- That "section 4" means the block headed `## 4 · Free observation`
  (`TACTICS.md` lines 73–82), not the fourth bullet or the fourth item of any
  other list.
- That "the order in which the cards reach a watcher" means the sequence of
  cards a single watcher reads, not the order of the four watchers' runs — the
  run order was explicitly put outside my question.
- That `.claude/agents/watcher-high.md`, being an agent definition rather than
  `RULES.md` or `TACTICS.md`, is evidence of how the laboratory reads the line
  but cannot add a requirement the line does not carry. It calls itself a
  "working summary" whose authority yields to those two files.

### Steer seen in the instruction
Two mild ones, neither a result and neither naming a thing to look for:
1. "If the section admits more than one requirement and does not choose between
   them, say so." This is conditional, but it presupposes that finding
   ambiguity is an available and welcome outcome, and it may have pushed me
   toward the A/B split — I have said so in §3 rather than hide it.
2. "Whether any order already built meets your answer is not yours — you are not
   shown one." This discloses that an order already exists, which implies the
   question arose from a dispute about a built order. It tells me nothing about
   what that order looks like, so I do not think it coloured the answer, but it
   is more than the question needed to contain.
Neither rises to a "pay attention to X" steer under RULES 3, in my reading.
