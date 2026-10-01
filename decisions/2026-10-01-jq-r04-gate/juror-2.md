# JQ-R04-GATE · juror 2

Question: `exam-prep/third-fix/juror-questions/JQ-R04-GATE.md` (read whole).
Which statistic decides whether exam cards are blind enough to use?

---

## 1 · Answer

**C. The gate fails if either attack beats its own RULES 12 chance line.** The
gate passes only if neither the pair AUC nor the nearest-neighbour score beats
its line.

Scope: this answer picks how two existing measurements combine into one
pass/fail. It sets no number, no chance line, no threshold, no score and no
trading rule. It changes no rule. Each attack is still judged against its own
line exactly as RULES 12 fixes it (1,000 shuffles, best 1%).

## 2 · What it rests on

**(a) What the gate protects is a requirement that must hold.**
`RULES.md` line 41 (RULES 9): "In the exam the coin name and the date are
hidden." `TACTICS.md` lines 101–102: "**What is hidden:** / - the coin name".
The rule says the name *is* hidden. It does not say "is hidden on average" or
"is hidden unless only one kind of test can recover it." The two attacks are
described in the question (lines 82–87) as asking two different things: "*can a
card be matched to its own coin?*" and "*does similarity carry coin information
on average?*" If either one finds coin identity beyond its chance line, the
documents give no reason to treat the requirement as met. Under A or B, a
measured leak from the other attack would be ignored. Under D, a measured leak
from one attack would be cancelled out by the other attack's silence.

**(b) Everywhere the laboratory writes a pass with several tests, it joins them
with "and". A favourable claim needs every test to come out favourable.**
`TACTICS.md` lines 130–134: "**Passing condition** (written before the result):
the paper with a recipe … - beats the chance line, **and** - beats Tomás,
**and** - beats the simple rule."
`TACTICS.md` lines 155–158: "**Passing condition:** - compound return positive
in both halves, **and** - beats 99% of the random rival, **and** - the account
is not zeroed …"
`RULES.md` lines 66–67 (RULES 18): "If one half wins and the other loses, that
is not a finding."
For the gate, the favourable claim is "these cards are blind." Following the
laboratory's own pattern, that claim passes only if *both* attacks come out
favourable (neither beats its line). That is option C. Option D reverses the
pattern: one favourable result out of two would be enough for the favourable
claim.

**(c) A pass is already weak evidence, so the gate should not be made weaker
still.**
`RULES.md` lines 76–77 (RULES 22): "'Could not be measured' never turns into
'no problem'." The question itself says (lines 69–75) that `ALL-removable` "is
**not** 'everything about a card that could identify its coin'" and that
"Nothing guarantees that no other channel exists outside the list." A pass can
only ever mean "two attacks on the listed features found nothing." A fail is
the only result that carries firm information. Rules A, B and D throw away
some of the fail signals the audit actually produces.

**(d) Fixing the rule before the result, and the irreversible side.**
`RULES.md` lines 34–35 (RULES 6): "The rule is written first, the result is
opened second." `TACTICS.md` line 22: "**Draw number:** `20260913`. Written
before the draw; it does not change." There is one set of exam coins.
- A **false fail** under C costs rework: re-blind, re-run the audit, re-check.
  That is reversible. It costs engineering time, and that cost has not been
  measured.
- A **false pass** under A, B or D means the answer key is sealed and the exam
  is sat on cards that leak identity. Once those results have been seen, RULES
  6 stops anyone from re-drawing the gate and re-using the same exam coins
  cleanly. In practice that is irreversible.
Where the rules do not choose, I lean toward the reversible error.

**Earlier verdicts.** I read all seven `decisions/2026-09-19-*/verdict.md`.
None of them settles any part of this question. The nearest is
`2026-09-19-calm-separation`, which ratified that calm moments of one coin need
no minimum distance from each other. That bears only on the optional second
part, because it means overlapping same-coin cards can occur by design.

**The optional second part (forbid time-overlapping neighbours?).** The rules
do not settle this, and I do not adopt it. It does not change my answer. The
rule the question cites does not say what the question attributes to it.
`RULES.md` lines 53–54 (RULES 13) read: "Moments occurring in several **coins**
in the same hour count as a single event. If the whole market moved together,
that is one event." That is about simultaneous moments across *different*
coins in scoring. It is not about two cards of *one* coin whose windows
overlap. The closer text is `TACTICS.md` line 127, "A moment appearing in
several cards in the same hour counts as a single event", and it sits under §7
Scoring (Greta), not under blinding. Neither rule tells an identity audit to
exclude anything. Whether an exam candidate who can link overlapping cards has
learned something the blinding should stop is a real question. It would be a
separate open question, and nobody has posed it to me.

**Should a rule change?** No change. RULES 33 (`RULES.md` lines 120–121): a
juror never decides "a change to a rule in this file", and the user has
declined to be asked. Nothing here needs one. This answer reads a step written
by a run. It does not touch `RULES.md`.

## 3 · The strongest case against my answer

1. **C quietly loosens the RULES 12 line.** `RULES.md` lines 51–52: "the real
   result must fall inside the best 1%." Two tests, each at 1%, joined by "fail
   if either" give a false-fail rate on truly blind cards of up to about 2%
   (estimate, union bound). The true rate depends on how correlated the two
   attacks are, and that has not been measured. "The chance line is not
   invented". Someone can fairly argue that C creates a new combined line that
   nobody wrote, which would be a juror setting a threshold (RULES 33). My
   reply is that each result is still judged against its own unmodified RULES
   12 line, the rules say nothing about combining, and the error falls on the
   cautious side. Even so, the objection is real. A referee could judge that
   *any* of A–D is a choice about a combined error rate and therefore not a
   juror's to make. If so, the honest answer becomes "the rules do not settle
   this."
2. **The gate sentence says "its chance line", singular.** Its author may have
   meant one specific statistic. The same run's Level 1 standard "required a
   family to fail **both** attacks" (question lines 100–102). That points to
   D, or to whichever single statistic the author treated as the main one.
   Consistency with the author's own standard is a fair way to read an unclear
   sentence. My reply is that Level 1 judged *single families* in order to
   decide which family carries identity. There, requiring both attacks avoids
   wrongly blaming one family. An acceptance gate for a whole card set has the
   opposite harm, and the author left the pooled row open on purpose. I also
   cannot check what "fail" means in the Level 1 text. It could mean "is
   caught by" or "survives", and the source is closed to me.
3. **C brings nearest-neighbour noise into a hard gate.** Question lines 89–96
   say the NN score depends on card numbering when there are exact ties. Same-
   coin cards with overlapping windows are near-copies, so NN can beat its line
   because of shared hours rather than coin identity. The pair AUC (A) is the
   steadier statistic. A gate that can fail for reasons unrelated to RULES 9 is
   a worse gate. My reply is that this argues for fixing the NN variant, which
   is engineering or a separate question. It does not argue for ignoring NN.
   I also accept that the question does not say which NN version (tie-
   dependent or tie-averaged) is "the nearest-neighbour score". Under C that
   choice can matter, and I name it below as unresolved.

## 4 · Confidence: 3 / 5

I would change my mind if:
- a laboratory document I may read names one designated statistic for the
  pooled-row gate, or shows that the Level 1 "both" standard was meant as the
  acceptance rule. Then B, A or D would follow from the text.
- the referee rules that choosing how two 1% tests combine is setting a
  threshold (objection 1). Then my answer becomes "the rules do not settle
  this; refer to the user", and I would accept that.

**Reversibility.** This choice can be reversed at no cost until the audit is
run on exam cards. After that, under RULES 6, any change counts as an
"afterwards" rule and must be tested again.

---

## Files read

- `exam-prep/third-fix/juror-questions/JQ-R04-GATE.md` (whole)
- `RULES.md`, `TACTICS.md`, `TEAM.md`, `README.md` (whole)
- `decisions/2026-09-19-{zero-trade-contracts,tokenized-equity,calm-separation,large-moment-selection,effort-level,watcher-across-runs,card-order-requirement}/verdict.md`
  (found with one glob limited to exactly the pattern
  `decisions/2026-09-19-*/verdict.md`)

Nothing else. I opened nothing under `exam/`, nothing else under `exam-prep/`,
and nothing else in `decisions/2026-10-01-jq-r04-gate/`.

## What I had to assume

- **The direction of "beats".** "Beats its chance line" means the attack
  recovers coin identity better than the best 1% of shuffles. That is a leak,
  and the gate fails.
- **Which NN version counts (unresolved).** The question does not say whether
  "the nearest-neighbour score" in B and C is the tie-dependent version or the
  tie-averaged version. My answer does not pick one. If they ever differ on
  exam cards, that is a new open question. I note only that coin identity does
  not depend on card numbering.
- **The meaning of "fail" in Level 1 (unverified).** Its source is closed to
  me.
- **The Mateo framing.** I assumed that "referred by Mateo" with "corrected by
  Mateo" describes a single author's question, and that no answer from another
  juror is embedded in it. I saw none.

## Steers seen in the question

1. **Measured results are in the question** (the table, lines 128–134; the
   second-part figures, lines 147–150). RULES 3 (`RULES.md` lines 15–17) says
   an instruction carries "no result". The figures are disclosed to show that
   all options give the same outcome today. Line 143–144 says, "Your answer
   therefore cannot change whether today's material passes." That lowers the
   apparent cost of the strictest option, which is C, the one I chose. I may
   have been pushed by it. I tried to ground C in the text and not in
   cheapness, but I report the pressure.
2. **The consistency cue toward D.** Lines 100–102 ("The same run's own
   standard … required a family to fail **both** attacks") point to one
   option. I treated it as an argument and answered it (objection 2). It is
   still a pointer.
3. **A misquoted rule.** Lines 115–116 say "RULES 13 … treats moments in the
   same hour as one event". The rule speaks of moments "in several coins". The
   paraphrase makes the second part look grounded in RULES when it is not.
4. **The disclosure about the earlier audit.** Lines 154–157 say the readings
   once disagreed but withhold which reading passed. That is handled correctly
   and is not a steer.

The coordinator's instruction carried no steer that I could see.
