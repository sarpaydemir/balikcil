# Open question — what may a watcher in a later run be given of its own earlier runs?

Juror 1 · 2026-09-19 · answered independently, in a fresh context, having seen
no other juror's answer (RULES 33).

Scope: the watcher's **own** earlier runs only. Batch count, batch size and run
order are not mine; the other watchers' notes are not mine; no threshold, score
or trading rule is set here; no rule in `RULES.md` is changed (RULES 33).

---

## 1 · Answer

A watcher in a later run may be given only the run's bookkeeping — its field of
view, its round number, which batch it is reading, the batch file, and a file to
write into — and **may not be given its own earlier notes, nor any summary,
count, carry-over or paraphrase of them**, because the instruction may contain
no result (RULES 3) and the laboratory deliberately gave the watcher definitions
no memory between runs (`TEAM.md`).

## 2 · What it rests on

**(a) The definitions deny cross-run memory on purpose, and say why.**
`TEAM.md`, "Structural decisions" (lines 168–170):

> "No definition has persistent `memory`. A watcher accumulating opinions
> between runs would break the blind exam."

The named mechanism is the `memory` feature, but the stated reason is about
**opinions accumulating between runs**, not about a particular tool. Opinions
pasted into the instruction accumulate exactly as opinions held in memory do.
Reading the reason as mechanism-specific would let the instruction do what the
definition was written to prevent.

**(b) An instruction may not carry a result or a steer.**
`RULES.md` rule 3 (lines 15–17):

> "Agents are not told what to look for, only what they may look at. An
> instruction contains no result, no prediction, and no 'pay attention to X'
> steer."

A watcher's own earlier notes are, by their required format, results and
opinions: `TACTICS.md` section 4 (line 81) — "Note format: `card no · what I
saw · why I think so · how sure I am (1–5)`" — and `.claude/agents/watcher-high.md`
(lines 67–68): "'What I saw' is a measured observation… 'Why I think so' is your
opinion." Handing that back into the next run is a "pay attention to X" steer
written in the watcher's own hand. `RULES.md` rule 7 (line 37) — "Free
observation produces ideas, not evidence" — confirms that what would be handed
back is an idea, not a settled fact that could be treated as data.

**(c) The permitted channel is the instruction, and only the instruction.**
`.claude/agents/watcher-high.md` (lines 109–110):

> "**You read only inside the Balıkçıl folder, and only the files named in the
> instruction.**"

So the question "what may it be given?" is the question "what may the
instruction name?" — and (b) answers it. The same file establishes that the
bookkeeping items *are* to be given: line 3 — "The field of view (exchange
behaviour · the crowd · the outside world · price itself) and the round number
are stated in the instruction" — and line 72 — "You write your notes to the file
named in the instruction, under `notes/`." Naming a batch file and a field of
view carries no observation; it is the same kind of statement as the round
number, which the definition requires.

**(d) A consequence that follows, and must not be left as a back door.**
Because the write target is named by the instruction (line 72), a **shared**
notes file reused across runs would hand the watcher its own earlier notes the
moment it opens the file to append. To keep (a) and (b) intact, each run must
write to its own file. Which naming scheme is used is an engineering detail; that
the runs must not share one file is the part that follows from the rules above.
Card numbers make the notes joinable downstream regardless: `TACTICS.md` 4 line
82 — "A note without a card number does not count."

**(e) Nothing is lost that the laboratory needed the watcher to hold.**
Aggregation across all cards is downstream work, not the watcher's:
`TACTICS.md` section 5 (lines 86, 89–90) — "everybody writes their notes into the
`canteen/` folder" … "**Sofia** writes down the survivors" — and `TEAM.md`
(line 54) — Sofia "Cannot: invent an idea. Every rule rests on at least one
watcher note and a card number."

**Reversible or irreversible.** Withholding is the **reversible** reading: if the
referee, a later jury or the user decides earlier notes may be carried, the
remaining batches can be run that way and nothing already written is invalidated.
Giving them is the **irreversible** reading: a note written while looking at the
watcher's own earlier conclusions cannot be cleaned afterwards — the only repair
is to discard those notes and re-read the batch from scratch. Cost of that
repair: one full re-read per contaminated batch at `opus`/effort high. I have
measured no token figure myself; `data/card-order/order-manifest.md` line 65
gives ~99,140 tokens of cards per batch of 34, and labels it an **estimate**
resting on assumptions it also labels. Under an unsettled question, the
reversible reading is the one to take.

## 3 · The strongest case against my own answer

Four points, honestly put.

1. **Expressio unius in the round rule.** `.claude/agents/watcher-high.md`
   (lines 120–121) says of Round 1: "you read only your own cards and write your
   own notes. You **do not** read the other watchers' notes." It forbids the
   *others'* notes by name and is silent on the watcher's own. A reader can
   fairly say: the one prohibition that was written out is the only one there is,
   and "write your own notes" describes a single continuing body of notes.
2. **RULES 3 sits under a heading about the old project.** Section A is titled
   "The wall — nothing leaks in from the old project". Rule 3 can be read as
   scoped to that: no *old-project* result in an instruction. Under that reading
   a watcher's own fresh notes are not what rule 3 was aimed at. — My answer
   survives this narrowing anyway, because ground (a) in `TEAM.md` is independent
   of rule 3; but the narrowing does weaken ground (b), and I do not pretend
   otherwise.
3. **The documents assume one watcher reading everything.** `TACTICS.md` 4
   (lines 78–79): "The four watchers (Ingrid, Kenji, Amara, Lukas) read all the
   cards of the 10 coins." Batching is an implementation fact, not a written one,
   and my answer converts one watcher-over-306-cards into nine strangers who each
   saw 34. That has a named cost: `.claude/agents/watcher-high.md` (lines 95–96)
   — "An observation resting on a single event is an observation, not a rule.
   Write down how many cards you saw it in." A watcher with no memory of earlier
   batches can only count inside its own batch, so every count it writes is a
   floor, not the true count. The instruction to each run should say so, or the
   counts will be read as whole-set counts and understate.
4. **Amnesia is not free.** The four things a watcher "must know" include not
   restating price (line 93) and flagging market-wide moves (lines 90–92). Those
   are per-card judgements and survive batching; but genuine cross-batch
   structure — "this pattern recurs" — will only ever be visible to Sofia, and
   only if the notes are rich enough. That is a real loss, and it is the price
   of the rule I am reading.

Against all four, the decisive fact remains that `TEAM.md` states the harm by
name — "A watcher accumulating opinions between runs would break the blind exam"
— and the blind exam is where the laboratory's evidence comes from
(`README.md` line 49: "Evidence comes only from steps 5 and 6").

## 4 · Confidence

**4 of 5.**

What would change my mind:
- A line in `RULES.md` or `TACTICS.md` (I found none in either file, read in
  full) that treats a watcher's notes file as cumulative across runs, or that
  names a "later run" at all.
- The user deciding otherwise. `RULES.md` line 3–4: "If one must change, the
  user is asked first, and then it is written into `LEDGER.md`." That is not
  mine to do, and I do not propose it.
- A showing that the counting requirement (case-against point 3) cannot be
  repaired downstream by Sofia from card numbers. If it cannot, the cost of my
  answer is higher than I have priced it — though even then the remedy is a
  different aggregation step, not feeding notes back into observation.

---

**Where I looked:** `RULES.md` (whole), `TACTICS.md` (whole), `README.md`
(whole), `TEAM.md` (whole), `.claude/agents/watcher-high.md` (whole),
`data/card-order/order-manifest.md` (whole). Nothing else was opened; `exam/`
was not opened, listed or named; no other file in this folder was read.

**What the instruction did not cover, that I assumed by name:**
- That "given" covers both the instruction text and any file the instruction
  names. I treated the two as one channel; `.claude/agents/watcher-high.md`
  lines 109–110 supports this, but the question did not define "given".
- That a watcher's write target may be a per-run file. Whether the runs share one
  notes file is not written down anywhere I was allowed to read; I assumed it is
  an open engineering choice and stated only the constraint the rules impose
  on it.

**Steer in the instruction:** none that I judge to be a leak. Closest call — the
sentence "Each run starts in a fresh context: a watcher in its second run
remembers nothing of its first" states the status quo of the mechanism, which
leans slightly toward the amnesia reading; I record it, but it names a technical
fact, not a result, a prediction or a "pay attention to X". The instruction
otherwise told me what I may look at and not what to look for (RULES 3).
