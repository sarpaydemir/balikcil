# Juror 1 — TACTICS 2: minimum distance between two calm moments of the same coin

Question: under `TACTICS.md` section 2, is there a minimum distance required
between two calm moments belonging to the same coin?

## 1 · Answer

**No — section 2 requires no minimum distance between two calm moments of the
same coin; the only separation it imposes on a calm moment is 72 hours from any
large movement, and the 48-hour clause belongs to the large-movement
definition.**

## 2 · What it rests on

`TACTICS.md`, section 2 · Moments, lines 35–44. The section as written:

```
- Hourly closing prices are used.
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

Four things in that text carry the answer.

**(a) Nesting.** The 48-hour clause — `TACTICS.md` line 39, "Of two moments
closer than 48 hours to each other, only the larger counts." — is an indented
sub-bullet of **Large-movement moment** (line 36). Its two siblings under the
same parent are unambiguously about large moments only: line 38, "The largest 20
of the year are taken for each coin", and line 40, "For a coin that did not trade
all year **this count** shrinks in proportion to its lifetime". **Calm moment**
(line 42) is a sibling of **Large-movement moment**, not a child of it, so the
sub-bullets do not reach it.

**(b) "Only the larger counts" cannot be executed on calm moments without
inventing a rule.** Calm moments are, by line 42, "chosen at random"; they have
no ordering by size that the selection uses. Choosing "the larger" of two calm
moments would be selection by magnitude of movement — the opposite of the reason
calm moments exist. Applying line 39 to calm moments therefore requires a
tie-break the section does not contain (keep the earlier? redraw?). Reading a
rule in a way that obliges you to invent its operative half is not reading it.

**(c) The calm bullet borrows explicitly when it borrows.** Line 42 says calm
moments are "**the same number as the large moments**". The author cross-
references the large-moment definition where he wants it to carry over. He
carries over the count; he does not carry over the 48-hour clause. He then
states the one separation requirement he does want, in his own words, in the
next sentence: line 43, "At least 72 hours away from any large movement." A
requirement stated for one relation (calm-to-large) and not for the other
(calm-to-calm) is not a gap by accident of drafting; it sits in the same
sentence pair.

**(d) A dropping filter contradicts the pinned count.** Line 39 is a filter that
removes moments. Line 42 pins the number of calm moments to the number of large
ones. Applying (d) to calm moments would reduce the calm count below the large
count, breaking line 42, unless replacements are redrawn — a mechanism the
section does not describe.

Nowhere else in the permitted files is there a general separation rule that
would reach calm-to-calm distance. I looked at the whole of `RULES.md`, the
whole of `TACTICS.md`, `README.md` and `TEAM.md`. The two nearby
de-duplication rules are about something else: `RULES.md` line 53, "Moments
occurring in several coins in the same hour count as a single event", and
`TACTICS.md` line 127, "A moment appearing in several cards in the same hour
counts as a single event." Both are *across* coins or cards, both are about
**counting** an event at scoring time, and neither governs the *selection*
distance between two moments of one coin. `README.md` line 35 ("Each coin's
large-movement moments and calm moments are found") and `TEAM.md` line 17 add
nothing on separation.

One measured observation from the one data file I was allowed, offered only as
evidence that the text and the artefact agree on the reading above, not as a
conclusion about the artefact: in `data/moments/moments.csv`, AVGOUSDT has 7
calm rows and 7 large rows (lines 2–15) — the counts are equal, as line 42
requires. The `rank_in_coin` column is filled for `large` rows and empty for
`calm` rows, i.e. the artefact maintains an ordering by size for large moments
and none for calm ones.

## 3 · The strongest case against my own answer

The clause says "Of two **moments**" — not "of two large-movement moments". Its
two sibling bullets name their subject narrowly ("the largest 20", "this
count"); this one does not. On a drafting-conventions argument that asymmetry
cuts against me: the author narrowed the neighbours and left this one general,
which can be read as a de-duplication principle meant for the whole moment list,
placed under the first definition simply because that is where moments are first
described. Under that reading a calm moment is still "a moment", and the clause
binds it.

The purposive case is stronger still. `TACTICS.md` line 44 fixes a moment's
start as "the hour at which the 24-hour movement began", and section 3 gives
each card the 24 hours before the start plus the 24 hours after. Two calm
moments of one coin less than 48 hours apart therefore produce cards whose
windows overlap: the watchers read substantially the same hours twice, and
Viktor's fifth question — `TEAM.md` line 61, "Is the same thing present in calm
moments too?" — is answered against a calm sample that is less independent than
its count suggests. That is a real methodological cost, and the laboratory
demonstrably cares about exactly this kind of double-counting (`RULES.md` line
53; `TACTICS.md` line 127). If the drafter had been asked, he might well have
said yes.

Against my point 2(b) specifically: calm rows in `data/moments/moments.csv` do
carry a `move_24h_pct` (e.g. `AVGOUSDT-C-20260507T2000` at 4.1945), so "the
larger" is arithmetically computable for calm moments; my claim that the clause
cannot be executed is a claim about sense, not about arithmetic.

What defeats all of that, for me, is that the purposive case argues for what the
rule *should* say. Deciding that is changing a rule, which RULES 33 forbids a
juror and RULES.md lines 3–4 reserve to the user. I answer what the section
requires, and it requires 72 hours from a large movement and nothing else.

Note on the shape of the answer: "no minimum is required" and "the section is
silent on calm-to-calm distance" are the same finding described from two sides.
The section is silent on that distance; because a selection procedure applies
only the constraints it states, silence here means no constraint. I say "no
minimum is required" rather than "the text does not settle this" because the
silence is not an ambiguity — the section states a separation requirement for
calm moments in the very sentence where a calm-to-calm one would have gone.

## 4 · Confidence, and what would change my mind

**4 of 5.**

Would change my mind:
- a line anywhere in the permitted files stating a general minimum separation
  between moments of one coin, or defining "moment" in a way that makes line 39
  explicitly apply to both kinds — I found none in the four files named above;
- an earlier or Turkish source text of section 2 (`KURALLAR.md` is named in
  `RULES.md` line 138 as the original of the *rules* file; I do not know whether
  a Turkish original of `TACTICS.md` exists, and I did not look for one) showing
  the 48-hour clause standing outside the large-movement definition;
- a demonstration that line 42's "the same number as the large moments" is
  satisfied by a redraw mechanism stated somewhere I did not read, which would
  dissolve my argument (d).

Would **not** change my mind: any argument that the 48-hour separation would
produce a better calm sample. That may be true and is not this question.

**Reversibility.** My answer is the reversible one in an important sense: it
asserts that a constraint is absent, and a later decision by the user could add
it. The opposite answer is the one that costs work, because it declares an
existing artefact non-conforming. I am not asked what follows for
`data/moments/moments.csv` and I propose nothing about it.

---

### Procedural note — a steer in my instruction (RULES 3)

My instruction is careful — it does not quote section 2, it says explicitly that
neither answer has been taken and that the measured pairs "bear on neither
answer". I record two things anyway, because RULES 3 says an instruction
"contains no result, no prediction, and no 'pay attention to X' steer":

1. It supplies a **measured result about the laboratory's own artefact**: "20
   pairs of calm moments that are adjacent in time within their own coin and
   less than 48 hours apart; 21 pairs in total". That is a result, delivered
   into an instruction.
2. More to the point, both numbers are measured **at 48 hours**. The question
   asked me is open ("is there a minimum distance"), but the evidence framing
   names one candidate threshold and no other, which anchors the question on the
   48-hour clause before I open the file. A neutral framing would have reported
   the distribution of within-coin calm-to-calm gaps without selecting a cut, or
   reported nothing.

Neither changed my answer — I read section 2 before rereading the framing, and
my reasoning rests on the nesting and the wording of lines 36–43, not on the
counts — but the anchoring is real and I report it as instructed.

### Files I read

`/home/user/balikcil/TACTICS.md` (whole) ·
`/home/user/balikcil/RULES.md` (whole) ·
`/home/user/balikcil/README.md` (whole) ·
`/home/user/balikcil/TEAM.md` (whole) ·
`/home/user/balikcil/data/moments/moments.csv` (first 25 lines only).

Nothing in `exam/`, `decisions/`, `LEDGER.md`, `instructions/`, `notes/`,
`canteen/`, `cards/`, `reports/`, `scripts/`, the rest of `data/`, or anything
outside this folder was opened, listed or searched. No glob or content search
was run at all; every read was a named file.

### What I had to assume

- That the markdown indentation of `TACTICS.md` lines 38–41 is deliberate and
  carries meaning. My argument (a) depends on it; arguments (b), (c) and (d) do
  not.
- That `data/moments/moments.csv` is the moment list section 2 describes; the
  instruction says so and the file's columns (`kind` = `calm`/`large`,
  `start_hour_utc`, `rank_in_coin`) match the section. I used it only as
  corroboration.
- That no Turkish original of `TACTICS.md` exists that I was entitled to
  consult. I did not search for one, because searching would have required a
  folder-wide glob, which my instruction forbids.
