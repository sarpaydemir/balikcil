# Juror 2 — open question: what may a watcher in a later run be given of its own earlier runs?

Date: 2026-09-19 · Role: `juror` (one of at least three, RULES 33) · Scope: the
watcher's own earlier work only.

## 1 · Answer

A watcher in a later run may be given only **administrative** material about its
own earlier runs — which batch it is now reading, which card numbers it has
already been given, its field of view, its round number, and the path of the
file it now writes to — and **may not be given the substance of its own earlier
work**: not its earlier notes, not its earlier report, not a summary,
recollection or carry-forward of either.

## 2 · What it rests on

**(a) The structural decision that removed cross-run carry-over on purpose.**
`TEAM.md`, "Agent definitions", structural decisions:

> "No definition has persistent `memory`. A watcher accumulating opinions
> between runs would break the blind exam."

This is the only line in the laboratory's documents that speaks directly about a
watcher *between runs*. It does not merely disable a setting; it names the harm
— a watcher accumulating opinions across runs — and removes it. Handing the same
watcher its own earlier notes as a file to read reproduces exactly that harm
through a different door. The `memory:` key and a named file path are two
mechanisms for one thing: the second run's opinions being shaped by the first
run's opinions rather than by the cards in front of it.

**(b) Everything a watcher gets, it gets because the instruction names it.**
`.claude/agents/watcher-high.md`, "The wall":

> "**You read only inside the Balıkçıl folder, and only the files named in the
> instruction.** You never look at a file outside this folder."

So the question "what may a watcher be given" is the question "what may the
instruction name". The same file enumerates what the instruction carries, and
prior work is not in the list — `watcher-high.md` front matter, line 3:

> "The field of view (exchange behaviour · the crowd · the outside world · price
> itself) and the round number are stated in the instruction."

and "Round":

> "**Round 1:** you read only your own cards and write your own notes. You **do
> not** read the other watchers' notes."
> "The instruction states which round you are in. If it does not say, it is
> round 1."

Round 1 is defined as cards in, notes out. Nothing else is provided for. A
second batch is still round 1 work: `TACTICS.md` 4 is the free-observation step,
and the reading of notes is deferred to a separate stage — `TACTICS.md` 5:
"**Round 2:** everybody reads the other three's notes and agrees or disagrees
while citing card numbers."

**(c) An instruction may not carry a result.** `RULES.md` 3:

> "Agents are not told what to look for, only what they may look at. An
> instruction contains no result, no prediction, and no 'pay attention to X'
> steer."

A watcher note is, by its prescribed format, a result plus an opinion plus a
confidence — `TACTICS.md` 4: "Note format: `card no · what I saw · why I think
so · how sure I am (1–5)`." An instruction that hands a watcher twenty of its own
such lines before batch 4 is an instruction containing results, and in practice a
"pay attention to X" steer: X is whatever the watcher happened to notice in
batch 1. RULES 3 forbids that whoever the author of X was, including the watcher
itself.

**(d) The administrative half is permitted by the same rule.** RULES 3 draws the
line at *what to look for* versus *what you may look at*. "You are reading batch
04, cards at positions 103–136" names no observation; `data/card-order/order-manifest.md`
already establishes that batch membership is content-free: "A card's batch is
decided by its position in the order and by nothing else - not its coin, not its
kind, not its date." Telling a watcher which card numbers it has already been
given therefore transmits no result, and is the minimum needed to avoid handing
the same card twice.

**(e) The loss is recovered elsewhere, not by the watcher.** The one real cost of
my answer is `watcher-high.md`, "Four things you must know", item 4: "An
observation resting on a single event is an observation, not a rule. Write down
how many cards you saw it in." Split across nine batches, a watcher can only
count inside its own batch. The documents put that aggregation in another pair of
hands: `TACTICS.md` 5 — "**Sofia** writes down the survivors" — and `TEAM.md`,
Sofia: "Every rule rests on at least one watcher note and a card number." The
cross-batch count is Sofia's arithmetic over the notes, not a watcher's memory.

**(f) Reversibility.** Giving nothing is the reversible reading: if the jury or a
later decision says carry-over is acceptable, the earlier batches' notes are
still on disk and can be handed forward at any time, at no cost. Giving the notes
is the irreversible reading: a watcher that has read its own earlier notes cannot
un-read them, and the only repair is re-reading those cards from a fresh context.
The cost of that repair is one full batch re-read per contaminated batch —
`order-manifest.md` puts a batch at ~99,140 tokens of cards (**estimate**, and
the manifest labels it one: "Every token number below is therefore an
**estimate**"). I write no token number of my own; I have measured nothing.

## 3 · The strongest case against my answer

The honest case against is that **no document says this, and I am arguing from
one sentence about a configuration key.** `TEAM.md`'s line sits under "Structural
decisions" and describes what the eight agent definitions contain; read narrowly
it says only "we did not set `memory: true`", and a reason given in passing
("would break the blind exam") is not a rule in `RULES.md`. The stated harm is
arguably already prevented by other means: the watchers do not sit the exam at
all, and `TEAM.md` says of Hana, "Does not see the observation notes or the
canteen; only the recipe" — so a watcher's accumulated opinions cannot reach the
exam paper except through Sofia's recipe, which is what the exam is meant to test
anyway. On that reading, the blind exam is not endangered by a watcher recalling
its own batch-1 notes, and my citation (a) proves less than I claim.

Against that narrow reading there is a real cost. A watcher carved into nine
contexts is nine watchers. `TACTICS.md` 4 says "The four watchers (Ingrid, Kenji,
Amara, Lukas) read all the cards of the 10 coins" — the document describes four
readers of the whole set, and my answer delivers thirty-six readers of ninth-sized
sets, none of whom can honour "write down how many cards you saw it in" across
the set. Someone could fairly argue that continuity of the *same* watcher's own
prior notes is the least contaminating way to restore what the document assumed,
and that the round rules were written about *other* watchers' notes — the
prohibition in `watcher-high.md` is literally "You **do not** read the other
watchers' notes", and the word "other" is doing work I am reading past.

I do not think this wins, for the reason in (e): the aggregation the document
assumes is assigned to Sofia, and buying it back through watcher self-recall
would also buy back anchoring — a watcher that has told itself in batch 1 that
funding flips matter will find funding flips in batch 4. But it is a genuine
cost, not a straw man, and it is the part of my answer I would most want the
referee to look at.

I should also name a second, sharper hazard I cannot fully evaluate and did not
invent: `order-manifest.md` records that the order is "merged strictly
alternating, so no two neighbours share a kind". A watcher that carries its own
prior classifications forward has more material from which to reason about that
alternation than one that does not. This applies within a batch as well as
across batches, so it does not decide the question by itself — but it argues in
the same direction as my answer, and against the counter-case.

## 4 · Confidence, and what would change my mind

**Confidence: 4 of 5.**

I am confident about the direction (nothing substantive carries across runs) and
less confident about the exact boundary of the administrative half — in
particular whether a later instruction may name the earlier notes file as an
*append target* without the watcher reading it. I did not resolve that; a
separate file per run avoids the question entirely and costs nothing.

What would change my mind:

- A line in `RULES.md`, `TACTICS.md`, `TEAM.md` or `README.md` that contemplates
  a watcher reading its own prior notes, or that assigns the cross-batch count
  to the watcher rather than to the canteen. I looked for one in the whole of all
  four files and in `.claude/agents/watcher-high.md` and
  `data/card-order/order-manifest.md`, and found none.
- A demonstration that Sofia cannot in fact do the cross-batch aggregation from
  the notes as filed — that would make my (e) false and the cost of my answer
  real rather than recoverable.
- A user decision. My answer is procedure only; it changes no rule in `RULES.md`
  and sets no threshold, no score and no trading rule (RULES 33).

## Notes on this run

**Files I read, in full:** `/home/user/balikcil/RULES.md`,
`/home/user/balikcil/TACTICS.md`, `/home/user/balikcil/README.md`,
`/home/user/balikcil/TEAM.md`,
`/home/user/balikcil/.claude/agents/watcher-high.md`,
`/home/user/balikcil/data/card-order/order-manifest.md`. Nothing else, no
folder-wide search, nothing from `exam/`, nothing outside this folder, and no
other juror's answer.

**What I had to assume, by name:** (i) that reading a second batch is round 1
work — `watcher-high.md` says "If it does not say, it is round 1", which supports
it, but no document addresses a batched round explicitly; (ii) that the notes of
earlier batches remain on disk and available to Sofia — `TACTICS.md` 5 assumes
notes are in `canteen/`, which I was not permitted to check.

**Steer in the instruction:** none found. The one sentence I weighed is "Each run
starts in a fresh context: a watcher in its second run remembers nothing of its
first" — it states the mechanical status quo and does not say what may be
*given*, so I do not read it as a steer, but I name it so the referee can judge.

**One thing I must report:** `data/card-order/order-manifest.md` raises a
*different* open question inside a file I was told to read — whether
"interleaved" means strictly alternating or merely mixed. That is not the
question put to me and I have not answered it; it is flagged here only so it is
not lost.
