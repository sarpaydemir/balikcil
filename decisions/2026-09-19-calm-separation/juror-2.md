# Juror 2 — TACTICS 2 and the separation of calm moments

**Question:** under `TACTICS.md` section 2, is there a minimum distance
required between two calm moments belonging to the same coin?

**Juror:** 2 of 3 · 2026-09-19 · model `opus`, effort high
**Read:** `TACTICS.md`, `RULES.md`, `README.md`, `TEAM.md`,
`data/moments/moments.csv` (first 6 lines).
No other juror's answer was read; no file in `decisions/` other than the one I
wrote was opened.

---

## 1 · Answer

No — section 2 states no minimum distance between two calm moments of the same
coin; the only separation it imposes on a calm moment is from large movements,
and the 48-hour clause it does contain sits inside the large-movement
definition and cannot be applied to calm moments as written.

## 2 · What it rests on

The whole of the relevant passage, `TACTICS.md` lines 35–44, with its
indentation preserved:

```
- **Large-movement moment:** the places where the coin rose or fell the most
  within 24 hours.
  - The largest 20 of the year are taken for each coin.
  - Of two moments closer than 48 hours to each other, only the larger counts.
  - For a coin that did not trade all year this count shrinks in proportion to
    its lifetime: one moment per 18 days.
- **Calm moment:** the same number as the large moments, chosen at random. At
  least 72 hours away from any large movement.
- A moment's start is the hour at which the 24-hour movement began.
```

Three things in that text carry the answer.

**(a) Scope by structure.** The 48-hour clause is `TACTICS.md` line 39, a
second-level bullet indented under the `Large-movement moment` bullet of line
36. Its two siblings — line 38, *"The largest 20 of the year are taken for each
coin."*, and lines 40–41, *"For a coin that did not trade all year this count
shrinks in proportion to its lifetime: one moment per 18 days."* — are
unarguably about large movements alone: a count of 20 and a lifetime-scaled
count are properties of the large-movement selection, and the calm bullet then
refers back to them from the outside (*"the same number as the large
moments"*). A clause whose two siblings are large-movement-only, sitting at the
same indent under the same parent, is large-movement-only. Line 42's calm
bullet returns to the outer level, i.e. it is a sibling of line 36, not of line
39.

**(b) Scope by operability.** Line 39 ends *"only the larger counts."* That
clause needs an ordering by size to do anything. Large moments have one — line
37, *"rose or fell the most within 24 hours"*, and line 38's *"largest 20"*.
Calm moments have no such ordering: line 42 says they are *"chosen at
random"*. Applied to two calm moments, "only the larger counts" either has no
referent, or, if one forced the 24-hour move size onto it, it would silently
replace random selection with a pick-the-biggest-mover rule — which contradicts
the same sentence that defines them. A rule that cannot be executed against
calm moments without contradicting their definition is not a rule about calm
moments.

The artefact records exactly this asymmetry. `data/moments/moments.csv` line 1
is the header `moment_id,symbol,kind,start_hour_utc,start_ms,move_24h_pct,rank_in_coin`,
and in the rows I read the `rank_in_coin` field is filled for `large` rows
(line 4: `AVGOUSDT-L-20260601T1000,...,7.7153,6`) and **empty** for `calm` rows
(line 2: `AVGOUSDT-C-20260507T2000,...,4.1945,` — trailing empty field). I cite
this only as evidence that "the larger" has no meaning for a calm moment, not
as evidence of what the section requires; what a script did is not what a
sentence says (RULES 6).

**(c) What the calm bullet does say.** Lines 42–43 state a count, a selection
method and exactly one distance constraint: *"At least 72 hours away from any
large movement."* The author of this section was demonstrably willing to write
a separation requirement for calm moments when one was wanted, and wrote one
—naming its counterparty as *"any large movement"*, not "any other moment".
Nothing in the section names calm-to-calm distance.

**Two neighbouring rules that might look like they answer this, and do not.**
`RULES.md` line 53 (rule 13): *"Moments occurring in several coins in the same
hour count as a single event. If the whole market moved together, that is one
event."* — that is across coins, and it is a counting rule, not a selection
constraint. `TACTICS.md` line 127: *"A moment appearing in several cards in the
same hour counts as a single event."* — that is section 7, scoring, and again
merges events at scoring time rather than forbidding a selection. Neither
imposes a within-coin minimum distance, and neither deduplicates anything more
than an hour apart. I looked for a within-coin calm-to-calm separation in the
whole of `TACTICS.md`, the whole of `RULES.md`, the whole of `README.md` and
the whole of `TEAM.md`; `README.md` lines 34–36 describe this step only as
*"Each coin's large-movement moments and calm moments are found."* and add no
constraint. There is none.

**Answer type.** This is a "the section does not require it" answer, not a
"the text does not settle this" answer. The distinction matters: section 2 is a
selection procedure, and a selection procedure binds by what it states. For the
narrow question put to me — *is a minimum distance required?* — an unstated
constraint is an absent constraint, so the answer is no. What I am **not**
saying is that the section deliberately decided calm moments may cluster; on
that further question the text is genuinely silent, and it is silent in a way
that could reasonably be called a gap rather than a choice. See part 3.

**Out of scope, deliberately.** Whether the existing 153 calm moments should
stand, be reselected, or be flagged is not mine and I propose nothing about it.
I set no threshold, no score and no trading rule, and I propose no change to
`RULES.md` (RULES 33, `RULES.md` lines 120–121: *"A juror decides procedure and
definition only: never a trading rule, never a threshold or score, and never a
change to a rule in this file."*).

## 3 · The strongest case against my own answer

The honest version of the other side has three legs, and the first two are
good.

**The word is "moments", not "large-movement moments".** Line 39 says *"Of two
moments closer than 48 hours to each other"*. The section is titled *"2 ·
Moments"* (line 33), and the section uses the bare word "moment" generically
elsewhere at the same nesting level of meaning — line 44, *"A moment's start is
the hour at which the 24-hour movement began."*, plainly governs both kinds,
and line 35, *"Hourly closing prices are used."*, governs both as well. So the
section's own habit is that unqualified "moment" means either kind. If the
author had meant line 39 narrowly, "of two such moments" or "of two large
movements" cost two words. Against my reading, the indentation is carrying an
enormous amount of weight for a document written in prose bullets rather than
as a specification — and lines 35 and 44 show the author was relaxed about
where a generally-applicable sentence sits.

**The purpose argument.** Section 2 exists to produce a sample of situations to
be turned into cards (`TACTICS.md` line 48, *"One page per moment."*) and then
read by watchers and, for the exam coins, scored. Two calm moments of the same
coin nineteen hours apart share most of their "before" window — line 50,
*"**Before:** the 24 hours before the start"* — so they are close to the same
card twice. The laboratory visibly cares about this kind of double-counting:
`RULES.md` line 53 and `TACTICS.md` line 127 both exist to stop one event
counting twice, and `TEAM.md` line 60 gives the skeptic the standing question
*"Does it rest on a single event?"*. A reading that lets one coin's calm sample
pile into a single window serves those purposes worse. If the 48-hour clause is
there to keep the sample from being one situation counted twice, that reason
applies to calm moments with equal force.

**The weak leg.** *"Only the larger counts"* could be read as merely the
tie-break attached to a generally-applicable 48-hour rule — the separation
being general, the tie-break specified only for the case where sizes exist, and
left to the random draw where they do not. I call this the weak leg because it
rescues the general reading by assuming a mechanism (draw one at random, drop
the other) that appears nowhere in the file; that is writing the rule, not
reading it.

**Where this leaves me.** The counter-case establishes that a calm-to-calm
separation would be *reasonable* and possibly *intended*. It does not establish
that line 39 as written *requires* one, because line 39 as written cannot be
executed on two calm moments without importing a selection mechanism the file
does not contain. My answer turns on that gap between "would have been sensible"
and "is required", and RULES 6 (`RULES.md` line 35: *"The rule is written
first, the result is opened second."*) makes that gap the one that matters here.

**Reversible / irreversible.** My reading is the reversible one. "No separation
required" leaves the existing 153 calm moments standing and changes no
artefact; if a later jury or the user reads the section the other way, the cost
is rerunning the moment-finding script and regenerating the affected cards —
work, but bounded, and nothing observed by a watcher is invalidated because no
card has been read yet (`README.md` lines 79–80: *"No card has been written and
no watcher has run yet."*). The other reading is the less reversible one: it
would drop moments from a sample already fingerprinted, and once watcher notes
exist against card numbers, reselection breaks the note-to-card link that
`TACTICS.md` line 82 makes mandatory (*"A note without a card number does not
count."*). That asymmetry is a reason to move slowly, not a reason to prefer my
answer, and I have not let it do any work in part 2.

## 4 · Confidence

**4 of 5.**

Four and not five because the generic word "moments" in line 39 and the
generically-scoped lines 35 and 44 are a real defect in the text, and because
I am reading indentation in a prose document as though it were a
specification.

Four and not three because the alternative reading requires inventing a
selection mechanism the file does not contain, and because the calm bullet
states its own separation constraint and names a different counterparty.

**What would change my mind**

- A line anywhere in `TACTICS.md`, `RULES.md`, `README.md` or `TEAM.md` — I
  have read all four in full — that applies a distance constraint between two
  moments of the same kind, or that names calm-to-calm distance. I found none.
- The Turkish original of this section, if section 2 also descends from a
  Turkish source as `RULES.md` does (`RULES.md` lines 139–141: *"This file was
  originally written in Turkish as `KURALLAR.md`."*). If the original used a
  word there that unambiguously means "moment of any kind", the generic reading
  gets much stronger. I have not seen such a file and did not look for one
  outside the four documents named in my instruction. Note that for `RULES.md`
  the English text is authoritative (line 141: *"this English text is now **the
  authoritative version.**"*); whether the same holds for `TACTICS.md` is not
  stated in anything I read, and is itself an open question I am not answering.
- Being shown that the 48-hour clause predates the calm-moment bullet — i.e.
  that it was written when "moment" had only one kind, and was never rescoped.
  That would make the narrow reading an accident of editing rather than a
  choice. I have no evidence either way; the place such evidence would live,
  `LEDGER.md` and `instructions/`, is closed to me for this question.

---

## Notes on the instruction

**A steer, reported under RULES 3** (`RULES.md` lines 15–16: *"Agents are not
told what to look for... An instruction contains no result, no prediction, and
no 'pay attention to X' steer."*).

The instruction did well in one respect: it declined to quote or summarise
section 2 and said so. But it then supplied two measured results about
`data/moments/moments.csv` — *"20 pairs of calm moments that are adjacent in
time within their own coin and less than 48 hours apart"* and *"21 pairs in
total within a coin and less than 48 hours apart"* — and I take this to be a
partial framing leak, for two reasons:

1. **It chose the window.** Section 2 contains more than one interval: 24
   hours, 48 hours, 72 hours, 18 days. By measuring at **48** hours and at no
   other distance, the instruction told me before I opened the file which
   clause was suspected of applying and which pairing (calm-to-calm) was at
   issue. Had it been silent, I would have had to find the candidate clause
   myself. The disclaimer *"They bear on neither answer"* is true of the
   direction of the answer but not of the framing: it narrowed the question.

2. **One sentence is contradicted by the numbers beside it.** The instruction
   says *"neither has been implemented in preference to the other in anything
   you may read"*. But 20 calm-to-calm pairs under 48 hours apart in
   `data/moments/moments.csv` **is** the no-separation reading implemented in
   an artefact I was told to look at. The accurate sentence would have been
   that the artefact implements one reading and that this is not evidence of
   what the section requires (RULES 6). I flag this as an accuracy fault rather
   than a steer — if anything it cuts against the answer I reached, since it
   understates an existing implementation that agrees with me.

Neither point told me what to conclude, and I do not think my answer moved
because of them; I reached it from the indentation and from "only the larger
counts", both visible before the pair counts could matter. I report them
because RULES 3 is about what the instruction contains, not about whether it
worked.

**What I had to assume, by name**

- That the indentation shown by my file reader reflects the file's actual
  bytes, and that two-space nesting under a bullet means subordination to it.
  I did not open `TACTICS.md` with any tool that would show raw whitespace.
- That `TACTICS.md` section 2 is current and unamended. The place an amendment
  would be recorded, `LEDGER.md`, is closed to me for this question, so I
  cannot confirm it.
- That "distance" in the question means time along the coin's own timeline
  measured between moment starts as defined at `TACTICS.md` line 44, since the
  instruction did not define it.

**Wall**

I read only the five files listed at the top, all inside `/home/user/balikcil`,
each by absolute path. I opened no folder-wide glob and ran no search. I did not
open, list or name anything in `exam/`, and did not read any other file in
`decisions/`, `LEDGER.md`, `instructions/`, `notes/`, `canteen/`, `cards/`,
`reports/`, `scripts/`, or anything under `data/` other than the one permitted
file. No memory or session-log search was run. I saw no other juror's answer.
