# Open question · a watcher across more than one run

**Question:** under the laboratory's written documents, what may a watcher in a
later run be given of its own earlier runs?

Juror 3 · 2026-09-19 · answered independently, no other juror's answer read.

---

## 1 · Answer

A watcher's later run may be given only the scope facts every instruction
already carries — its field of view, its round number, the cards of that batch
and the file to write its notes to — and **nothing of the substance of its own
earlier runs**: not its earlier notes, not a summary or digest of them, not a
carried-over conclusion, hypothesis or "keep watching X" line.

## 2 · What it rests on

**(a) An instruction may not carry a result back into an agent — and a watcher
note is a result.** `RULES.md` line 15-17, rule 3:

> "Agents are not told what to look for, only what they may look at. An
> instruction contains no result, no prediction, and no 'pay attention to X'
> steer."

A note in the format TACTICS 4 requires — `card no · what I saw · why I think
so · how sure I am (1–5)` (`TACTICS.md` line 80) — is a recorded observation
with a stated confidence. Putting it into the instruction of the same watcher's
second run puts a result into an instruction. Rule 3 does not exempt a result
because the agent that produced it wore the same name; it forbids the
instruction from containing one. The same prohibition is repeated to the watcher
in its own definition, `.claude/agents/watcher-high.md` line 114-116:

> "The instruction tells you **what you may look at**, never **what to look
> for.** If you see a steer, a result, or a 'pay attention to X' sentence in the
> instruction, report it — that is a leak."

A watcher handed its own run-1 note would, on the letter of that line, be
obliged to report its own instruction as a leak.

**(b) The laboratory has already decided that a watcher does not accumulate
across runs, and said why.** `TEAM.md` line 168-169:

> "No definition has persistent `memory`. A watcher accumulating opinions
> between runs would break the blind exam."

The configured fact is the missing `memory` setting; the stated harm is wider
than the mechanism — "accumulating opinions between runs". Handing the notes
back in the instruction produces exactly the harm the setting was removed to
prevent. Reading the sentence as barring only one route to that harm would make
the stated reason idle.

**(c) What *is* given fresh each run is named, and it is scope, not substance.**
`.claude/agents/watcher-high.md` line 3 (the definition's own description):

> "The field of view (exchange behaviour · the crowd · the outside world · price
> itself) and the round number are stated in the instruction."

and line 109-110:

> "**You read only inside the Balıkçıl folder, and only the files named in the
> instruction.**"

and line 72:

> "You write your notes to the file named in the instruction, under `notes/`."

A later run is therefore told who it is, which round it is in, which files it
may read and where to write — all of it supplied afresh, none of it remembered.
That list is the whole of what a second run legitimately needs.

**(d) Reading notes is a round-2 permission, granted explicitly, and no such
permission exists for one's own.** `.claude/agents/watcher-high.md` line 120-127:

> "**Round 1:** you read only your own cards and write your own notes. You **do
> not** read the other watchers' notes.
> **Round 2:** if the instruction explicitly allows it, you read the others'
> notes and agree or disagree while citing card numbers. ...
> The instruction states which round you are in. If it does not say, it is
> round 1."

The design is that note-reading is switched on by an explicit, named permission.
There is no written permission anywhere in `RULES.md`, `TACTICS.md`, `TEAM.md`,
`README.md` or `watcher-high.md` that switches on reading one's own earlier
notes; the default the last line sets is round 1, which is card-reading and
note-writing only.

**(e) The documents already place the joining-up of a watcher's notes somewhere
else — after observation, not inside it.** `TACTICS.md` line 86-87:

> "**Round 1:** everybody writes their notes into the `canteen/` folder.
> **Round 2:** everybody reads the other three's notes and agrees or disagrees
> while citing card numbers."

and `TEAM.md` line 47-48 (Sofia): "collects the notes, runs the discussion."
A watcher's notes from batch 1 and batch 9 meet each other in the canteen, in
Sofia's hands, keyed by card number — which is why `TACTICS.md` line 81 insists
"A note without a card number does not count." Nothing is lost by a later run
not seeing its earlier notes; the recombination step exists by name.

**(f) The batches are disjoint, so no continuity information is needed to avoid
duplicate or missed work.** `data/card-order/order-manifest.md` line 96:

> "| **every card in exactly one batch** | **pass** - 306 cards, 306 batch
> slots, 0 duplicates, 0 missing |"

and line 73: "A card's batch is decided by its position in the order and by
nothing else - not its coin, not its kind, not its date."

**Two boundary cases this answer resolves, and one it does not.**

- *Resolved — bare bookkeeping is not substance.* A list of card numbers already
  covered carries no observation and no opinion; nothing I read forbids it. By
  (f) it is also unnecessary, so the safe practice is to omit it.
- *Resolved — the notes file must not be a back door.* If a later run is pointed
  at the same `notes/` file that already holds its earlier notes, appending
  forces it to read them and (a) and (b) are breached through the file rather
  than through the instruction. The clean form is one notes file per run, named
  in that run's instruction as line 72 provides.
- *Not resolved by the documents, and not mine to settle:* the file-naming and
  collation mechanics themselves — one file per batch versus per watcher, and
  who concatenates them for the canteen. That is coordinator bookkeeping, not
  procedure the documents fix.

**Reversible or irreversible.** Giving less is reversible: a watcher's own
earlier notes can still reach it later through the canteen and round 2, which
`watcher-high.md` line 122-124 already provides for. Giving the earlier notes is
irreversible *within that run* — a context cannot un-see them, and the only
remedy is to discard that batch's notes and re-run the batch in a fresh context.
Cost of that remedy, per batch: re-reading 34 cards, which the manifest puts at
"largest batch of 34 cards ~99140 tokens" (`order-manifest.md` line 65) — the
manifest labels every token figure there an **estimate**, and so do I. I have
measured no token count myself.

## 3 · The strongest case against my own answer

The honest case for "the documents do not settle this":

`TEAM.md` line 168 sits under the heading "Structural decisions" (line 160) and
is written in the indicative about configuration — *"No definition has
persistent `memory`."* It states what the eight agent files contain, not what an
instruction may contain. Its stated reason invokes the blind exam, and a watcher
never sits the blind exam: `TACTICS.md` line 110-115 lists the five who sit it
(Hana, Tomás, Greta, the simple rule, the coin flip), and `TEAM.md` line 23-24
says of each watcher only "**Cannot:** see exam cards." So the reason attached to
line 169 does not obviously reach the case in front of me, and a rationale that
misses its target is weak ground for a prohibition.

Against my ground (d), the sharpest cut: `watcher-high.md` line 120-121 bars
exactly one thing in round 1 — "you do not read the **other watchers'** notes."
Having gone to the trouble of naming whose notes are barred, the document
arguably implies one's own are not. The same clause is the closest the corpus
comes to addressing note-reading during observation, and it is silent on the
present question by apparent choice of words.

And against my ground (a): RULES 3's purpose, given in its own heading "A · The
wall — nothing leaks in from the old project" (`RULES.md` line 6), is to keep
*the old laboratory's* opinions out of new eyes — `README.md` line 18-21: "we
worked for months in the old laboratory and accumulated a pile of opinions. So
that those opinions do not colour the new watchers' eyes..." A watcher's own
note from batch 1 is not from the old project; it is Balıkçıl's own, produced
under Balıkçıl's rules and already destined for the canteen. Reading RULES 3 to
bar it stretches a wall built against one thing to hold back another.

If that case is right, the correct answer is not mine but "the documents do not
settle it, and the jury should say so." I weighed it seriously. I do not adopt
it, for two reasons: RULES 3's sentence is written as a flat property of
instructions with no source-qualifier ("An instruction contains no result"), and
`watcher-high.md` line 114-116 restates it to the watcher without any
old-project qualifier at all; and the expressio-unius reading of line 120-121
proves too much, since it would equally license the instruction to hand back
everything else a fresh context lacks, which line 169 plainly means to prevent.

## 4 · Confidence, and what would change my mind

**Confidence: 4 of 5.** The substance half of the answer (no earlier notes, no
summary, no carried-over conclusion) I hold at 4. The bookkeeping half (bare
card numbers permissible but unnecessary) I hold at 3 — it rests on an absence
of prohibition rather than on a line, and I say so.

What would change my mind:

- A line I did not find that grants a watcher, or a continuation run, explicit
  access to its own earlier notes — as `watcher-high.md` line 122 grants round-2
  access to the others'. That would settle it against me outright.
- A line making RULES 3 a wall-only rule in terms, i.e. qualifying "result" as
  "result from outside Balıkçıl". Then ground (a) falls and I would drop to
  confidence 2, resting only on TEAM.md 168-169.
- Being shown that a watcher's own notes are structurally required inside a
  later observation run for something the canteen cannot do later. I could not
  construct such a need, since batches are disjoint (`order-manifest.md` line 96)
  and notes are joined by card number (`TACTICS.md` line 81).

What would **not** change my mind: an argument from convenience, or from the
cost of nine separate runs. Neither is a line in a document.

---

### Files read

`RULES.md` (whole) · `TACTICS.md` (whole) · `README.md` (whole) · `TEAM.md`
(whole) · `.claude/agents/watcher-high.md` (whole) ·
`data/card-order/order-manifest.md` (whole). Nothing else was opened; no
folder-wide search was run; `exam/` was not opened, listed or named, and no
other file in this decision folder was read.

### Assumed, because the instruction did not cover it

1. That "given" covers both what an instruction puts in front of the watcher and
   what it lets the watcher read from disk. I answered for both, since the same
   lines govern both.
2. That a written summary or digest of the earlier notes counts as substance,
   not bookkeeping. I treat it as substance: RULES 3 forbids "a result", and a
   digest of results is results.
3. That the coordinator, not a juror, owns the notes-file naming mechanics. I
   declined to fix them.
