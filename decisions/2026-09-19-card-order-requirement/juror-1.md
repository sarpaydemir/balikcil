# Juror 1 — open question, 2026-09-19 09:05 UTC

**Question:** what does `TACTICS.md` section 4 require of the order in which the
cards reach a watcher?

---

## 1 · Answer

Section 4 imposes **one requirement with two prongs**, both about how the cards
are *given* to a watcher (not about the order in which a watcher chooses to read
what it has been given):

- **Prong A — shuffled.** The delivery order must be a randomised order of the
  pooled set of cards. It must not be an order derived from any property of the
  cards themselves: not chronological by moment start, not grouped or blocked by
  coin, not in card-number order, not ordered by moment type. "All the cards of
  the 10 coins" form one pool, and the shuffle is over that pool.
- **Prong B — the two kinds interleaved.** Large-movement cards and calm-moment
  cards must travel in the **same stream**, mixed. They may not be segregated:
  not all of one kind before all of the other, and not delivered as separate
  groups, files or streams by kind.

**The yes/no test a checker can apply to a given order O of N cards:**

1. Does O contain both kinds? If one kind is absent from what a watcher is
   given, **no**.
2. Is O equal to (or a stable grouping of) any ordering derivable from card
   attributes — moment start time, coin, card id, moment type — ascending or
   descending? If yes, **no** (fails prong A).
3. Do all cards of one kind precede all cards of the other kind, or are the two
   kinds handed over as separate groups? If yes, **no** (fails prong B).
4. Was the order produced by a randomising procedure over the pooled set? If it
   can be shown it was not, **no**. (See the limit on this in part 3: from the
   sequence alone a checker can only *falsify* prong A, never confirm it.)

An order that survives 1–4 satisfies section 4 as written.

**What section 4 admits two readings of, and does not choose between:** *how
strict* "interleaved" is.

- **Reading A (gloss):** the colon makes "large moments and calm moments
  interleaved" a description of what shuffling the pooled set achieves. Any
  output of a fair shuffle passes, including one that by chance contains a long
  run of one kind.
- **Reading B (extra constraint):** "interleaved" is a second, independent
  demand on the sequence, so a shuffle output that happens to clump the kinds
  must be rejected and redrawn.

Section 4 contains no words choosing between them, and it supplies no run-length
limit that reading B would need. I record the split rather than resolve it; I
note only that reading B cannot be applied at all without a maximum-run number,
and **setting that number is outside a juror's scope (RULES 33)** and is
nowhere in the written rules. So the *checkable* content of section 4 today is
prong A plus the no-segregation floor of prong B.

**What section 4 does not settle at all** (I am not answering these; they are
separate open questions):

- whether all four watchers get the **same** order or four different orders;
- whether the shuffle's **seed is recorded** anywhere (section 4 says nothing;
  TACTICS 1 records a seed for the draw, and RULES 29 ties a run number to the
  fingerprint of its input — whether "input" reaches the free-observation card
  order is its own question);
- whether card identifiers may encode the coin, the date or the kind.

**Reversibility.** Prong A and prong B are cheap to satisfy *before* cards are
handed over: regenerating an order costs nothing but a rerun of the ordering
step. Once a watcher has read cards in a non-conforming order and written notes,
the fault is **not repairable in place** — the notes were formed under the
order, so the remedy is a fresh re-read of all the cards by the affected
watcher(s) in a fresh context. I have not measured what that re-read costs in
tokens or time, and I do not estimate it here (RULES 19).

---

## 2 · What it rests on

`TACTICS.md`, section 4 "Free observation", line 80 — the whole of the
requirement:

> "- Cards are given in shuffled order: large moments and calm moments
>   interleaved."

The word **"given"** is what puts the duty on whoever hands the cards over, not
on the watcher.

`TACTICS.md`, section 4, line 78–79 — what "all" and the pool mean:

> "- The four watchers (Ingrid, Kenji, Amara, Lukas) read all the cards of the 10
>   coins. Each takes notes from their own field of view."

Since the watcher reads **all** the cards of **the 10 coins**, the set to be
shuffled is the pooled set across coins; that is why grouping by coin is not a
"shuffled order".

`TACTICS.md`, section 2, lines 36–43 — the two kinds named in line 80 exist and
are distinct, so "interleaved" has a definite referent:

> "- **Large-movement moment:** the places where the coin rose or fell the most
>   within 24 hours."

> "- **Calm moment:** the same number as the large moments, chosen at random. At
>   least 72 hours away from any large movement."

Because the two kinds are equal in number, prong B's floor (no segregation)
bites on a real, balanced pool.

`.claude/agents/watcher-high.md`, lines 44–46 — the laboratory's own reading of
line 80, stated to the agent that receives the cards:

> "Cards arrive in **shuffled order.** Among them are moments of large movement
> and moments where nothing at all happened, and **you are not told which is
> which.**"

This confirms prong B's direction: the presentation must not tell the watcher
the kind in advance. It also shows the kinds arrive in one stream ("among
them"), not as two deliveries.

`TACTICS.md`, section 3, line 52 — why the kind is nonetheless discoverable
*from the card's content* in free observation, which bounds what the order
requirement can be for:

> "- **After:** the 24 hours after the start. Shown only in free observation,
>   never in the exam."

`RULES.md`, rule 33, lines 118–121 — why I record the unchosen strictness of
"interleaved" instead of picking a run-length:

> "A juror decides procedure and definition only: never a trading rule, never a
> threshold or score, and never a change to a rule in this file."

---

## 3 · The strongest case against my own answer

**(a) The colon may carry the whole sentence, and prong A may be my invention.**
Read strictly, "Cards are given in shuffled order: large moments and calm
moments interleaved" states one purpose — mixing the two kinds — and "shuffled"
is merely the means named for it. On that reading the only requirement is prong
B, and an order that **deterministically alternates** large, calm, large, calm,
while being chronological within each kind, satisfies section 4 completely.
My prong A would then be a constraint I added to the text. I answered against
this because a fixed alternation is not what "shuffled" means in ordinary
English, and because a watcher who noticed the alternation could read each
card's kind off its position, which contradicts `watcher-high.md` line 46 ("you
are not told which is which"). But that second argument leans on an agent
definition, and `TACTICS.md` — not an agent file — is the authority; the agent
file could be wrong. This is the strongest objection and I do not think it is
absurd.

**(b) Prong A is not checkable on the artefact, so calling it a requirement is
awkward.** Randomness cannot be confirmed from one sequence. My test can only
*reject* orders that are visibly sorted; a hostile or careless order could be
hand-built to look random and pass every check. If a requirement is one nobody
can verify, an objector could say section 4's real, operative requirement is
only the part that can be checked — prong B — and prong A is advisory. My
answer to that is that the same is true of "chosen at random" in section 2 line
42 and the laboratory still treats that as binding, so unverifiability from the
artefact does not demote a requirement to advice. Still, the asymmetry is real
and I have written the test to reflect it (falsifiable, not confirmable).

**(c) The mixing may be pointless here, which weakens my reading of its force.**
In free observation the card carries its "After" section (`TACTICS.md` line 52),
so the watcher learns each card's kind from the card itself within seconds. If
the kind is visible anyway, someone could argue "interleaved" is a weak
housekeeping preference against clumping rather than a hard gate, and that an
order failing prong B does no damage. I think this is wrong — order effects on a
reader are exactly what an ordering rule guards against, and `watcher-high.md`
lines 53–55 make the calm cards load-bearing rather than filler — but it is an
honest argument that section 4's order line is softer than I have made it.

**(d) I may be wrong to say the section leaves the strictness unchosen.** A
reader could say the colon plainly settles it (reading A) and that I have
manufactured a split where the grammar is clear. That is possible; I kept the
split because reading B is the natural one for anyone who reads "interleaved" as
a state the sequence must exhibit, and the sentence does not exclude it.

---

## 4 · Confidence

**4 of 5** on the two-prong requirement and the yes/no test as stated.
**4 of 5** on "section 4 does not choose the strictness of interleaving".
**5 of 5** on the narrow floor: the two kinds may not be segregated into
separate blocks or separate deliveries, and the order may not be chronological
or grouped by coin.

**What would change my mind:**

- A line elsewhere in `TACTICS.md` or `RULES.md` defining "shuffled" or
  "interleaved" for this laboratory, or fixing a run-length. I looked through
  the whole of `RULES.md` (rules 1–35 plus the language note), the whole of
  `TACTICS.md` (sections 0–10), the whole of `README.md` and the whole of
  `TEAM.md`, and the only other places either word appears are `TACTICS.md`
  line 42 ("chosen at random", of calm moments), line 133 and RULES 12 ("the
  answers are shuffled 1,000 times" — the chance line, a different use), and
  `TACTICS.md` line 147 ("at random times (1,000 times)" — the money-test
  rival). None of them defines the card order. `README.md` step 3 (lines 38–39)
  describes free observation without mentioning order at all.
- Evidence that "shuffled order" was chosen in the Turkish original with a
  narrower sense than the English carries. `RULES.md` lines 139–141 say the
  English text is now authoritative, so this would be an argument about intent,
  not about authority — but it would move me.
- A decision by the user, recorded per `RULES.md` lines 3–4, choosing between
  reading A and reading B. That would settle part of my answer outright, and it
  is not mine to make.

---

## Files I read

- `/home/user/balikcil/TACTICS.md` (whole)
- `/home/user/balikcil/RULES.md` (whole)
- `/home/user/balikcil/README.md` (whole)
- `/home/user/balikcil/TEAM.md` (whole)
- `/home/user/balikcil/.claude/agents/watcher-high.md` (whole)

I opened nothing else. I did not open `exam/`, `decisions/` (beyond writing this
file), `LEDGER.md`, `instructions/`, `notes/`, `canteen/`, `cards/`, `reports/`,
`scripts/`, `data/`, the rest of `.claude/`, or anything outside this folder. I
ran no folder-wide glob and no session-log search. I have not seen any other
juror's answer.

## What I had to assume, by name

1. **That "given" means delivered/presented**, i.e. the duty falls on whoever
   hands the cards to the watcher. The instruction did not define it.
2. **That the shuffled set is the whole pooled set for one watcher**, taken from
   "read all the cards of the 10 coins" (line 78). Section 4 does not say the
   word "pool".
3. **That `.claude/agents/watcher-high.md` may be used as corroboration but not
   as authority.** Its own line 30 says `RULES.md` and `TACTICS.md` win.
4. **That "interleaved" refers to the two moment kinds of section 2** and not to
   anything else, since line 80 names them.

## Steers I saw in the instruction

Two, both mild, reported for the record under RULES 3:

1. "If the section admits more than one requirement and does not choose between
   them, say so." This is conditional and names no result, but it points at one
   particular outcome — multiplicity — before I had read the section, and a
   juror who wants to be useful is nudged toward finding it. I formed my reading
   of line 80 from the line itself and then checked it against this prompt; I
   would have reached both prongs without it, but I cannot prove that, so it is
   on the record.
2. "Nor is the batch size, the batch count or the run order." Words I was not
   otherwise given: this tells me an order exists somewhere and that it was
   built in batches. That is a small piece of the answer's context leaking in,
   though it carries no result and I did not use it.

Neither leak contains a result, a number or a prediction, so I did not treat the
jury as spoiled. The referee should weigh them.
