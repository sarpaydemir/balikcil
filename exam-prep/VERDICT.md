# Verdict — the two problems before the exam

Mateo · data engineer · 2026-09-19 (system clock, RULES 23)

This file says whether each problem is solved and nothing about how. The
working is in the other files of `exam-prep/`.

---

## R-04 — the exam may not be blind

**SOLVED, against the standard written below, with a residual that is measured
and named and not zero.**

The standard I set, and by which a reviewer may disagree with me:

1. No field whose absolute level is a coin's signature may identify a card's
   coin, or link two cards of the same coin, better than the RULES 12 chance
   line. **Met.**
2. No printed column may identify which clock hours a card covers.
   **Met.**
3. The pooled attack over *everything* an exam candidate can see must also sit
   at the chance line. **Not met, and it cannot be met** — the reason is a
   small number of fields that the **frozen** canteen book and TACTICS 3
   require to stay on the card. Each is named, with its measured size, in
   `exam-prep/R-04-blindness.md` §7. Removing any of them would mean changing
   a rule after the fact, which RULES 6 forbids.
4. Nothing that the frozen canteen book asks an exam candidate for may be
   destroyed. **Met, and checked by script on every card.**

Two things the reviewer should weigh before accepting this verdict:

- Everything was measured on the **306 observation cards**, because `exam/` is
  closed to this run. The acceptance gate for the exam itself is written down
  as a step the exam-building run must perform before the answer key is sealed.
  Until that step runs, R-04 is solved *on the material I was allowed to see*.
- The attacker I used is a script reading all 306 cards at once. An exam
  candidate has no tools and reads no files (RULES 10). I measured the stronger
  adversary and did not measure the weaker one.

**No change to `RULES.md` is required.** The fix implements RULES 9 more
completely than TACTICS 6 does; it does not alter RULES 9. It **does** go
beyond TACTICS 6's list of what is hidden, and every step beyond that list is
named in `exam-prep/decisions-and-open-questions.md`.

---

## N-1 — collapse before counting

**SOLVED as far as one person is allowed to solve it. The instrument exists,
is tested and is cross-checked. The last step is not mine and is named.**

The standard I set:

1. One deterministic implementation, producing a true partition, checked on
   every run. **Met.**
2. It must reproduce, on the 306 observation cards, the counts an independent
   earlier script measured for the same relation. **Met, exactly.**
3. Every reading of RULES 13's wording that the written rules allow is
   implemented and measured, and none is chosen by me. **Met.**
4. A judge cannot compute a chance line without supplying an event map.
   **Met — the function refuses.**
5. The effect of collapsing is measured, not asserted. **Met.**

**What is not done, and why it is not mine:** RULES 13's phrase "in the same
hour" can be read more than one way, and the readings do not give the same
numbers. That is a wording that can be read two ways and a choice that changes
the numbers — an **open question under RULES 33**, which says it is never
answered by one person. It is written out as four numbered questions for three
jurors in `exam-prep/N-1-collapse.md` §7, together with every measurement a
juror needs to rule. Until that ruling exists, the judge's script cannot be
pointed at a configuration.

**A juror should read §7 there, not a paraphrase of it.** I have deliberately
kept the numbers out of this file: a question handed to jurors through a
summary is a question with a thumb on it.

One thing the laboratory should know before it rules, and I state it without
numbers here for the same reason: **my measurement does not support the
strongest form of the complaint N-1 makes.** Part of the correction is large
and part of it is negligible, depending on which reading is ratified. The
measurement is in `exam-prep/N-1-collapse.md` §6.

**No change to `RULES.md` is required.**

---

## A steer in the instruction I was given

I was asked to report one if I found it. I found no result and no prediction in
the instruction. One sentence leans: it speaks of what a later run needs "to
count events correctly", which presumes the current counting is wrong. My
measurement came out mixed rather than confirming that presumption, and I have
said so above rather than let the presumption stand. Two further near-misses
and the full reasoning are in `exam-prep/decisions-and-open-questions.md` §C.

---

## Where the rest is

| file | what it holds |
|---|---|
| `exam-prep/R-04-blindness.md` | the blindness standard, the measurements, the residuals, what the exam-building run must do |
| `exam-prep/N-1-collapse.md` | the collapse standard, the readings, the open question, what the judge's script must do |
| `exam-prep/decisions-and-open-questions.md` | ten decisions I took that the instruction did not cover, five questions I refused to answer, and the steer check |
| `exam-prep/collapse/` | the event maps and the shuffle calibration, with run records |
| `exam-prep/identity/` | the audits of the raw and the blinded card sets |
| `exam-prep/blind-proof/` | four blinded copies of the 306 observation cards, one per configuration |
| `scripts/15_event_collapse.py` `16_identity_audit.py` `17_blind_cards.py` `18_residual_diagnostic.py` `lab_cards.py` | the instruments |

Nothing under `exam/` was read or written by this run.

---
---

# Second-fix run · 2026-10-01 — acting on `exam-prep/REVIEW.md`

Mateo · data engineer · appended 2026-10-01 (system clock, RULES 23). **Nothing
above this line was changed.** The text above is the first run's verdict of
2026-09-19; its SHA-256 as reviewed was
`c5bd5532615ee28fc3016ba2cc07246b428c5d19dcb8b580df5d5752ccb96cf0` and its
first 5,512 bytes still hash to that value. Where this section corrects a claim
above, it says what was claimed, what it is now and why. The working is in
`exam-prep/second-fix/SECOND-FIX.md`; this section says what happened, not how.

## The two problems now

| problem | earlier in this file | now |
|---|---|---|
| **R-04 · is the exam blind?** | "SOLVED, against the standard written below, with a residual that is measured and named and not zero" | **NOT SOLVED.** The review's conditions were acted on, and the measurement the review required, applied to every printed column as it asked, shows a removable coin-identity channel that no earlier file named — one family of it is, by pair AUC, larger than any channel named before on the blinded cards; the acceptance gate fails on the observation cards under every reading of it. Not closable in this run. SECOND-FIX §4. |
| **N-1 · collapse before counting** | "SOLVED as far as one person is allowed to solve it" (the review: "Not solved") | **Instrument repaired, tested, and the defects the review found are closed. Not yet usable**: the counting definition is open and referred (JQ-N1). SECOND-FIX §3. |

Corrections of the four standard lines marked "Met" above:

- R-04 line 1 ("Met") — **not met**: two level families beat a chance line on
  the recommended blinding, not one. Why: review §3.1, re-measured.
- R-04 line 2 ("Met") — **met for columns only**; the line was written about
  columns and a bullet line carries a date channel, now referred (JQ-R04-DATE).
- N-1 line 4 ("Met — the function refuses") — **was met only in its literal
  wording**; it is now met as the review asked. Why: review §4.3, re-measured.
- N-1 line 3 and 5 stand. Line 5's measurement is corrected: SECOND-FIX §5
  row 10.

All thirteen corrections, each with its source: SECOND-FIX §5.

## Outcome of every review item

| review item | outcome |
|---|---|
| §3.6 item 1 | **Referred to jurors** — JQ-R04-GATE. |
| §3.6 item 2 | **Partly done.** Named with its numbers: done. The audit extended to every printed column: done. Closed: **not done** — the rendering route was tried and measured, and did not close it; the remaining routes change what TACTICS 6 shows and are **referred** (JQ-R04-CONTENT part b). Recording it in the exam manifest: **not done** (the manifest lives under `exam/`); required of the exam-building run (SECOND-FIX §8). |
| §3.6 item 3 | **Referred to jurors** — JQ-R04-DATE part b (with parts a and c). |
| §4.5 item 1 | **Done.** |
| §4.5 item 2 | **Done.** |
| §4.5 item 3 | **Done**, and **referred** — JQ-N1. |
| §4.5 item 4 | **Done.** |
| §1.1, first defect | **Done.** |
| §1.1, second defect | **Referred** with §3.6 item 1. |
| §1.2 | **Done** (with §4.5 items 2 and 4). |
| §2.3 | **Done.** |
| §3.1 | **Done** (correction recorded). |
| §3.5(a) | **Done** (correction recorded). |
| §3.5(b) | **Done** (correction recorded). |
| §4.2, last paragraph | **Done** (in JQ-N1). |
| §4.3 | **Done** (with §4.5 item 4). One part cannot be done in code and is named: a caller can always write his own shuffle outside the module. |

## Where I dispute the review, with reasons (RULES 32)

1. **§4.2, "the bug is real and the §6 conclusion survives it."** Disputed in
   part. After the repair the spread of the block line against the card-level
   line roughly doubles, and in two configurations the block line ends above
   the representative line, which the review says it stays "far below".
   Differences of the size the first run called "barely moves" are within the
   random variation measured between two draws of one and the same null.
   Numbers: SECOND-FIX §4 item 1 and 2.
2. **§4.3, last table row, "reproduces the un-collapsed card-level line
   exactly" in both modes.** True in representative mode; in block mode the
   reviewed code drew from the same distribution but gave a different line.
   Minor. SECOND-FIX §2, C-10.
3. **§3.2 and §3.6 item 2, that the `close` channel is "removable" by a
   rendering choice.** The manufactured part is removable and was removed; the
   column's coin signature was not, and grew. SECOND-FIX §3.
4. **§3.6, "With those three discharged, what remains is what the document
   already says honestly."** Disputed: the audit extension the review itself
   required shows a further channel. SECOND-FIX §4.

## Open questions referred

Twelve rows, indexed for the coordinator in `exam-prep/JUROR-QUESTIONS.md`.
Ten are written by this run in `exam-prep/second-fix/juror-questions/`. Two
were already open in the canteen book and are indexed so that none is lost:
JQ-B1 (re-written here so a juror can answer it standalone) and JQ-CANTEEN-8
(read from the canteen book directly). I cannot see `LEDGER.md`, so I cannot
tell whether either of those two was already put to jurors.

Everything referred is procedure or definition. Nothing in scope of a juror
was kept back, and nothing outside it — no threshold, score or trading rule —
was referred.

## `RULES.md`

**No change to `RULES.md` is required by anything this run did or referred.**
One path is named so it is not discovered late: if the jurors rule that no
field TACTICS 3 puts on a card may be removed or recomputed, and the
engineering route named in SECOND-FIX §4 does not close the remaining channel,
then the exam cannot be made blind by the laboratory's own measure while every
TACTICS field stays. Whether a named, measured channel is acceptable under
RULES 9 at that point is a question about a rule, which is the user's, not a
juror's. Nothing has reached that point.

## A steer in the instruction I was given

I found no result, no prediction and no fix chosen for me. Two mild
presumptions, named rather than left unsaid: the index requirement ("one row
per open question that jurors must answer before the exam") presumes there
will be open questions — there are, for reasons the review itself states; and
the instruction's file name, which I saw in `git status` without opening the
file, calls this run a "second fix", which presumes a fix is what is needed —
for R-04 this run's finding is that it is not yet fixable here.

## What this run did not do

SECOND-FIX §10, nine items. The two that matter most: **R-04 is not solved**,
and **nothing was measured on exam cards.**

Nothing under `exam/` was read or written by this run.
