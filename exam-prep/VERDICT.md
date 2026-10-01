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

---
---

# Third-fix run · 2026-10-01 — acting on `exam-prep/REVIEW-2.md`

Mateo · data engineer · appended 2026-10-01 (system clock, RULES 23).
**Nothing above this line was changed**: the first 12,256 bytes of this file
are the file as the second review found it (SHA-256
`d83c2b85fe8548634193fa60d8c98e090559b7211f6066b21727a4482835fab5`). This
section says what happened, not how; the working is in
`exam-prep/third-fix/THIRD-FIX.md`, and what later runs must do is in
`exam-prep/HANDED-FORWARD.md`.

## The two problems now

| problem | second-fix verdict | now |
|---|---|---|
| **R-04 · is the exam blind?** | NOT SOLVED | **NOT SOLVED.** The acceptance-gate row still beats its chance line on both attacks on every blinded version of the observation cards, including a new version built this run that ranks the unrounded source values; that version reduces the leak and does not close it. |
| **N-1 · collapse before counting** | instrument repaired; not yet usable | **The instrument is repaired and both of the second review's conditions are acted on, but N-1 is not usable yet:** the corrected counting questions await jurors and the referee (condition 1), and the key check is now enforced by the engine while its correct use is handed forward to the judge's script (condition 2). |

## Outcome of every REVIEW-2 item

Numbering: `exam-prep/third-fix/THIRD-FIX.md` §1.

| item | outcome |
|---|---|
| R2-1 | **Done**; ratification **referred to jurors**. |
| R2-2 | **Done** in the engine; **handed forward** (HANDED-FORWARD B-2). |
| R2-3 | **Done.** |
| R2-4 | **Done.** |
| R2-5 | **Done**; the review's re-marking **disputed in part** (D-1). |
| R2-6 | **Done** (withdrawn, reduced to a statement); the check on the exam set **handed forward** (A-5). |
| R2-7 | **Done.** |
| R2-8 | **Done.** |
| R2-9 | **Done.** |
| R2-10 | **Done**; commissioning **referred to the coordinator**. |
| R2-11 | **Done**; **handed forward** (A-3). |
| R2-12 | **Done**; **handed forward** (A-4). |
| R2-13 | **Done.** |
| R2-14 | **Done** (correction recorded). |
| R2-15 | **Done** (correction recorded). |
| R2-16 | **Done** (correction recorded); **disputed in part** (D-1). |
| R2-17 | **Handed forward** as information, not as a requirement. |
| R2-18 | **Not done**; **referred to the coordinator** (THIRD-FIX R2-18). |
| R2-19 | R-04 **not closed** — what closure depends on is below, and the work that depends on no juror answer was done; whether the run working under `exam/` may proceed is **referred to the coordinator**. |

## The juror rows

| identifier | outcome |
|---|---|
| JQ-N1-1 | unchanged (fit) |
| JQ-N1-2 | corrected — checked: fit |
| JQ-N1-3 | corrected — checked: fit |
| JQ-N1-4 | corrected — checked: fit |
| JQ-CANTEEN-8 | corrected (written out as a juror file) — checked: fit |
| JQ-R04-GATE | corrected — checked: fit |
| JQ-R04-DATE-a | unchanged (fit) |
| JQ-R04-DATE-b | corrected — checked: fit |
| JQ-R04-DATE-c | unchanged (fit) |
| JQ-R04-CONTENT-a | corrected — checked: fit |
| JQ-R04-CONTENT-b | corrected — checked: fit |
| JQ-B1 | corrected by withdrawal: it is a statement, not a juror question |

Every corrected row was checked against the five tests REVIEW-2 applied
(THIRD-FIX §3), and every number and line citation in the corrected files
against its source (`scripts/28_juror_file_check.py`, run
`bbb740248b0c8717`: 61 checks, 0 failed). `exam-prep/JUROR-QUESTIONS.md` was
re-issued; it carries no wording, options or numbers of any question, and its
earlier version is kept byte for byte at
`exam-prep/third-fix/JUROR-QUESTIONS-as-of-second-fix.md`.

## What R-04's closure depends on

1. The ratified outcomes of **JQ-R04-GATE**, **JQ-R04-DATE-a**,
   **JQ-R04-DATE-b**, **JQ-R04-DATE-c**, **JQ-R04-CONTENT-a** and
   **JQ-R04-CONTENT-b**.
2. **And on engineering not yet found.** On today's material, under any
   reading of the gate that involves pair AUC, the gate row still beats its
   line even when the features of the price column and of the trade-count
   column are both taken out. Which outcomes would combine with which
   engineering is recorded in THIRD-FIX §4.5, marked **not for juror files**:
   a juror who saw it could choose a definition by its effect (RULES 6), so
   it must not be put in an instruction to a juror.
3. If no engineering closes what is left, whether a measured channel that
   cannot be removed is acceptable under RULES 9 is a question about a rule,
   which is the user's. That point has not been reached.

Done now, because it depends on no juror answer: the granularity channel is
inside the gate's feature list; the nearest-neighbour score has an order-free
version with its own line; the audit's clock-hour test now sees ranked
columns; and the second run's untried engineering route — ranking the
unrounded source values — was built, guarded and audited (THIRD-FIX §4).

## Where I disagree with the second review (RULES 32)

- **D-1.** REVIEW-2 rightly found that two nearest-neighbour "beats" printed
  by the second run were not properties of the cards, but its replacement
  verdicts ("does not beat") compare an order-free figure with the chance
  line of the order-dependent statistic. A permutation line belongs to the
  statistic it was drawn for; against the order-free statistic's own line
  both cells beat. Reasoning and numbers: THIRD-FIX §6.
- **D-2.** Not a disagreement: REVIEW-2 §6 decided nothing about the
  identifiers, and I did not rename them (THIRD-FIX R2-18).

## `RULES.md`

**No change to `RULES.md` is required by anything this run did or referred.**
The path named by the second-fix run remains possible and is restated in
point 3 above; it has not been reached.

## A steer in the instruction I was given

I found no result, no prediction and no fix chosen for me. Two mild
presumptions, named: "if an item can only be met by a run that does not
exist yet" presumes such items exist (two do: R2-2 and R2-6's exam-set
check); "if `R-04` is not closed when you finish" presumes it may not be
(it is not, for the reasons above, which do not rest on that sentence).

Separately, and not in the instruction: the context my session started with
showed recent commit subjects of this repository, and I read them before
opening any file. Two of them say that exam data has been acquired by a run
under `exam/` (consistent with REVIEW-2 §7 item 1); one of those also says
that a "contact address" was "found sent to third parties". Neither bears on R-04 or N-1 and I looked no
further (git history is closed to me). I name the second because it may
concern the user and I cannot tell whether the coordinator knows of it.

## What this run did not do

THIRD-FIX §7a, twelve items. The ones that matter most: **R-04 is not
closed**; **nothing was measured on exam cards**; **no juror question is
ratified**.

Nothing under `exam/` was read or written by this run.

---
---

# Fourth-fix run · 2026-10-01 — acting on `exam-prep/REVIEW-3.md`

Mateo · data engineer · appended 2026-10-01 (system clock, RULES 23).
**Nothing above this line was changed**: the first 19,176 bytes of this file
are the file as the third review found it (SHA-256
`ba859a5470c9e4842350561e3aa5a84359c1e64804989c472f7f06b704f340ee`). This
section says what happened, not how; the working is in
`exam-prep/fourth-fix/FOURTH-FIX.md`, and what later runs must do is in the
last section of `exam-prep/HANDED-FORWARD.md`, which is complete on its own.

## The two problems now

| problem | third-fix verdict | now |
|---|---|---|
| **R-04 · is the exam blind?** | NOT SOLVED | **NOT SOLVED.** The audit now compares distances exactly; on every blinded version of the observation cards the acceptance-gate row still beats both of its lines, with the same figures as before. What closes R-04 is now written as a checkable standard (HANDED-FORWARD, fourth-fix section, A-0). |
| **N-1 · collapse before counting** | not usable yet | **The instrument is ready; N-1 is not usable yet.** The engine's key check no longer trusts the object it checks, and both "earliest" and "latest" conventions are implemented and checked. What remains is the jurors' and the referee's (JQ-N1 group with JQ-CANTEEN-8) and the judge's script (HANDED-FORWARD B-1 … B-5). |

## Outcome of every REVIEW-3 item

Numbering: `exam-prep/fourth-fix/FOURTH-FIX.md` §1.

| item | outcome |
|---|---|
| R3-1 | **Done**; ratification **referred to jurors** (JQ-N1 group). |
| R3-2 | **Done** in the engine, and **handed forward** (B-3's independent recomputation). |
| R3-3 | **Done** in the engine; its use **handed forward** (B-1). |
| R3-4 | **Done** (new audit script; figures replaced); **handed forward** (A-2). |
| R3-5 | **Done.** |
| R3-6 | **Referred to jurors** — JQ-R04-CONTENT-c. |
| R3-7 | **Done**; commissioning **referred to the coordinator**. |
| R3-8 | **Handed forward** (A-0, A-0.1 … A-0.6). |
| R3-9 | **Handed forward** (A-0.2, A-1). |
| R3-10 | **Handed forward** (A-0.4, A-2); the choice itself **not made** — a disagreement goes to the coordinator. |
| R3-11 | **Done.** |
| R3-12 | **Done** (not required). |
| R3-13 | **Referred to the coordinator** (below). |
| R3-14 | **Handed forward** as information, not as a requirement. |
| R3-15 | **Handed forward** as information; nothing decided. |
| R3-16 | **Not done**; still **referred to the coordinator**. |
| R3-17 | **Referred to the coordinator** (below). |
| R3-18 | **Done** where a juror sees such a verdict. |

## The juror rows

| identifier | outcome |
|---|---|
| JQ-N1-1 | unchanged (fit) |
| JQ-N1-2 | corrected — checked: fit |
| JQ-N1-3 | corrected — checked: fit |
| JQ-N1-4 | corrected — checked: fit |
| JQ-CANTEEN-8 | corrected — checked: fit |
| JQ-R04-GATE | unchanged (fit); **not touched** |
| JQ-R04-DATE-a | unchanged (fit) |
| JQ-R04-DATE-b | unchanged (fit) |
| JQ-R04-DATE-c | unchanged (fit) |
| JQ-R04-CONTENT-a | corrected — checked: fit |
| JQ-R04-CONTENT-b | corrected — checked: fit |
| JQ-R04-CONTENT-c | added — checked: fit |
| JQ-B1 | unchanged (withdrawn) |

"Unchanged" rows whose file had to be re-issued (because a file they point
to moved) keep their text word for word; that is checked. Every row was
checked against the standard the reviews applied (FOURTH-FIX §3), and every
number and line citation in the files issued by this run against its source
(`scripts/31_juror_file_check_fourth.py`, run `4b4d4795eb488c94`: 59 checks,
0 failed). `exam-prep/JUROR-QUESTIONS.md` is re-issued; it carries no
wording, options or numbers of any question, and both earlier versions are
kept byte for byte.

**JQ-R04-GATE does not need to change.** Its file was not touched (SHA-256
still `55e7b95c…16ce`). Every figure in its table equals the exact audit's,
and its statement that no card on the gate row has an exactly tied nearest
neighbour holds under exact arithmetic on all five versions it shows. The
one gap the third review found around it — which nearest-neighbour version
grades if an exam gate row has a tie — is handled outside the question:
HANDED-FORWARD A-0.4 and A-2 compute both and stop if they disagree. If the
coordinator prefers jurors to settle that in advance, it would be a new
question, not a change to this file.

## For the coordinator

1. **R3-17.** The third-fix section of this file ("What R-04's closure
   depends on", point 2) and `exam-prep/third-fix/THIRD-FIX.md` §4.5 say
   which readings of the gate fail on the material measured so far. Neither
   may reach a JQ-R04-GATE juror or its referee (RULES 6). I cannot see
   whether either was included in their commission.
2. **R3-13.** A referee ratifying both JQ-R04-GATE (its optional second
   part) and the JQ-N1 group should check that their two readings of
   RULES 13 do not contradict each other.
3. **R3-6.** The third review allowed a second route for the rank-source
   question: the coordinator records a reason why it is engineering. I wrote
   it as a juror question instead (JQ-R04-CONTENT-c) because the choice
   changes the numbers and no written rule settles it; the other route
   remains the coordinator's.
4. **R3-16.** Whether a subject in an identifier is content is still
   undecided.
5. **R3-7.** Both coupled groups can now be commissioned; JQ-R04-CONTENT-c is
   new and has not yet been reviewed.

## Where I disagree with the third review (RULES 32)

No disagreement. One extension: the floating-point comparison the review
found in the nearest-neighbour ties also set the pair-AUC ranks; five
pair-AUC figures shown to jurors moved in the third or fourth decimal and no verdict changed
(FOURTH-FIX C4-3).

## `RULES.md`

**No change to `RULES.md` is required by anything this run did or referred.**
The path named by the second-fix and third-fix runs (a measured channel that
cannot be removed, and whether RULES 9 accepts it) remains possible and has
not been reached.

## A steer in the instruction I was given

I found no result, no prediction and no fix chosen for me. Mild
presumptions, named: the reason given for the model choice ("two juries wait
on the questions this run is responsible for, and the exam's instruments
inherit whatever this run leaves wrong") presumes something is left wrong;
"for each juror-question row the third review rules not fit, if any" and
"if anything would require changing a rule" presume nothing. "Where the
review says a point belongs to jurors, write it as a juror question in the
group the review names" directs procedure, not an outcome; I followed it for
the rank source and say so above (item 3). The instruction tells me jurors
are answering JQ-R04-GATE now; that is information, and it is why script 16
and the GATE file were left untouched.

## What this run did not do

FOURTH-FIX §7, nine items. The ones that matter most: **R-04 is not
solved**; **nothing was measured on exam cards**; **no juror question is
ratified**.

Nothing under `exam/` was read or written by this run.

---
---

# Fifth-fix run · 2026-10-01 — acting on `exam-prep/REVIEW-4.md`

Mateo · data engineer · appended 2026-10-01 (system clock, RULES 23).
**Nothing above this line was changed**: the first 26,243 bytes of this file
are the file as the fourth review found it (SHA-256
`5ed3c26f56431a9c3705d100347f8a2c5162b01616f9200c4e6602e4aa243c4e`). This
section says what happened, not how; the working is in
`exam-prep/fifth-fix/FIFTH-FIX.md`; what later runs must do is in the
fourth-fix and fifth-fix sections of `exam-prep/HANDED-FORWARD.md`, read
together.

## The two problems now

| problem | fourth review | now |
|---|---|---|
| **R-04 · is the exam blind?** | NOT SOLVED | **NOT SOLVED.** JQ-R04-GATE is ratified; the seven other rulings R-04's standard now needs (HANDED-FORWARD fifth-fix A-0.1) are outstanding; under the ratified gate, the gate row as audited today does not pass on any blinded version of the observation cards (REVIEW-4 §1). The A-0.4 grading is restated against the ratified outcome. |
| **N-1 · collapse before counting** | solved only under three conditions | **Solved only under the same three conditions.** (1) The JQ-N1 group's files are corrected; they still need review (if the coordinator wants one), commissioning and ratification. (2) The judge's script meets HANDED-FORWARD B-1 … B-5 — handed forward. (3) The tie check on the sealed key — handed forward in the replaced B-1. |

## Outcome of every REVIEW-4 item

Numbering: `exam-prep/fifth-fix/FIFTH-FIX.md` §1.

| item | outcome |
|---|---|
| R4-1 | **Done.** |
| R4-2 | **Done.** |
| R4-3 | **Done.** |
| R4-4 | **Done**, with one extension (FIFTH-FIX §2 E-2). |
| R4-5 | **Referred to jurors** — JQ-R04-CONTENT-d (new); the dependent sentences in two files now point to it. |
| R4-6 | **Done** (HANDED-FORWARD fifth-fix A-0.4 and A-0.1). |
| R4-7 | **Done.** |
| R4-8 | **Done.** |
| R4-9 | **Cannot be done by this run** (the files that would show it are closed to me); **referred to the coordinator** (below, item 1). |
| R4-10 | **Done** for every list this run writes (index; HANDED-FORWARD C-5); earlier commissions not visible. |
| R4-11 | **Handed forward** (B-1, replaced). |
| R4-12 | Files corrected; commissioning and ratification **referred to the coordinator**. |
| R4-13 | **Handed forward** (in force). |
| R4-14 | **Not acted on** (a named gap, not a requirement); **referred to the coordinator** (below, item 2). |
| R4-15 | **Recorded.** |
| R4-16 | **Recorded.** |
| R4-17 | **Recorded**; nothing to do. |
| R4-18 | R-04 not solved (above). |

## The juror rows

| identifier | outcome |
|---|---|
| JQ-N1-1 | corrected (shared part 4 item removed; its own part's text unchanged) |
| JQ-N1-2 | corrected (as N1-1) |
| JQ-N1-3 | corrected only in the file's shared closing paragraph; its own part's text unchanged |
| JQ-N1-4 | corrected |
| JQ-CANTEEN-8 | corrected |
| JQ-R04-GATE | unchanged — **ratified**; not ruled, not to be commissioned again |
| JQ-R04-DATE-a | corrected |
| JQ-R04-DATE-b | corrected only in the file's shared closing paragraph; its own part's text unchanged |
| JQ-R04-DATE-c | corrected only in the file's shared closing paragraph; its own part's text unchanged |
| JQ-R04-CONTENT-a | corrected |
| JQ-R04-CONTENT-b | corrected |
| JQ-R04-CONTENT-c | corrected |
| JQ-R04-CONTENT-d | **added** |
| JQ-B1 | unchanged (withdrawn) |

**Fitness, row by row** (FIFTH-FIX §4, against REVIEW-2's tests (i)–(v),
REVIEW-4's test (vi) and no contradiction with the ratified GATE verdict):
every row to be commissioned — JQ-N1-1 … -4, JQ-CANTEEN-8, JQ-R04-DATE-a …
-c, JQ-R04-CONTENT-a … -d — is **fit by my ruling**; none has been reviewed
since it was corrected, and JQ-R04-CONTENT-d has never been reviewed. The
index (`exam-prep/JUROR-QUESTIONS.md`, re-issued; every earlier version kept
byte for byte) carries no wording, option or number of any question, shows
each row's status, and names in no reading list a review, `VERDICT.md`, a
working file or a file stating measured effects of options; the canteen
book is given only by the five line ranges the CONTENT file cites.
`RULES.md` and `TACTICS.md` stay whole on every list: they are the texts the
questions read, every answer must be grounded in them (RULES 34), "other"
answers may rest on any of their lines, and they state no measurement and
no earlier choice on an open point.

Checked by `scripts/32_juror_file_check_fifth.py`, run `6a8b8a6dc1c92be7`:
77 checks, 0 failed (`exam-prep/fifth-fix/checks/juror-file-check-6a8b8a6dc1c92be7.md`).

## Where I disagree with the fourth review (RULES 32)

1. **The part 4 table "can go to the referee"** (REVIEW-4 §2) against "none
   may reach a juror or referee" (§7 item 6). I sent it nowhere: a referee
   checks count, independence, grounding, split, objection and scope, and
   none of these needs an option's effect (RULES 6, 35).
2. **Part a's rows from the printed values.** REVIEW-4 lists rows 3–4 for
   removal; I removed rows 1–2 as well, because its own instruction ("state
   part a's premise without saying which rendering meets it") and REVIEW-3's
   test (iii) both fail a file that shows only the rendering where the
   signature exists (FIFTH-FIX E-2).
3. **JQ-R04-DATE's closing paragraph** has the defect REVIEW-4 found in
   CONTENT's; REVIEW-4 did not name it. Fixed the same way (E-3).

## For the coordinator

1. **R4-9 — "earlier verdicts".** The ratified GATE verdict says every
   juror's grounding included "earlier verdicts". If that means
   `exam-prep/VERDICT.md`, its third-fix section (point 2) carried
   result-before-rule information about the gate. I cannot see the
   commission or the answers. Whether the ratification stands under RULES 6
   is not mine to decide.
2. **R4-14 — a named gap.** JQ-R04-CONTENT does not say whether one attack
   beating its line is enough for "carries a measured coin signature". It
   changes nothing on today's material; it could on exam material. Whether
   to put it to the same jurors before they sit is yours; I did not, because
   the review did not require it.
3. **Commissioning before review.** Every changed row says "not reviewed
   since". Whether a fifth review precedes commissioning is yours.
4. **Part d's scope.** If its referee judges that it decides whether a
   measured coin signature may stay on exam cards ungraded — a rule, not a
   definition — it goes to the user (RULES 33), not back to me.
5. **`LEDGER.md`.** Whether JQ-R04-GATE's ratification is written there
   (RULES 35) I could not check.

## `RULES.md`

**No change to `RULES.md` is required by anything this run did or referred.**
The path named by earlier runs — a measured channel that cannot be removed,
and whether RULES 9 accepts it, which is the user's — is now nearer: part d
is the definitional reading of the gate that comes before it, and if part d
is refused on scope, that path is reached. It has not been reached.

## A steer in the instruction I was given

No result, prediction or fix chosen for me. Named, mildly: "two juries wait
on the files this run corrects" presumes the files can be corrected and puts
weight on a quick finish. "Write it as a juror question in the group it
bears on" settles a procedure REVIEW-4 §7 item 2 left to the coordinator
("whether this is engineering or an open question is yours to record"); I
followed it (R4-5) and say so here. "A ratified verdict now exists … It
binds this run" is information, and it is why A-0.4 was restated. The git
status supplied at start carried only commit subjects of the forms "work:",
"ledger:" and "auto:", and an untracked instruction file name; no result.

## What this run did not do

FIFTH-FIX §5, six items. The ones that matter most: **R-04 is not solved**;
**nothing was measured on exam cards**; **no row has been reviewed since
correction**; **R4-9 could not be checked**.

Nothing under `exam/` was read or written by this run.

---
---

# Sixth-fix run · 2026-10-01 — acting on `exam-prep/REVIEW-5.md`, DATE and CONTENT rows only

Mateo · data engineer · appended 2026-10-01 (system clock, RULES 23).
**Nothing above this line was changed**: the first 34,212 bytes of this file
are the file as the fifth review found it (SHA-256
`e5652c57e33f2927bff875093aa01ff576899c5176f4fb88a87aef442ec2472e`). This
section says what happened, not how; the working is in
`exam-prep/sixth-fix/SIXTH-FIX.md`; what later runs must do is in the
fourth-fix, fifth-fix and sixth-fix sections of `exam-prep/HANDED-FORWARD.md`,
read together.

## The two problems now

| problem | fifth-fix verdict | now |
|---|---|---|
| **R-04 · is the exam blind?** | NOT SOLVED | **NOT SOLVED.** Nothing was measured. The rulings R-04 now needs are JQ-R04-CARRIES-a and -b (new), JQ-R04-DATE-a … -c, JQ-R04-CONTENT-a … -c and JQ-R04-CONTENT-d; none is ratified. |
| **N-1 · collapse before counting** | solved only under three conditions | **Not acted on by this run.** Its juror group is being answered now. |

## Outcome of every REVIEW-5 item concerning the DATE and CONTENT rows

Numbering: `exam-prep/sixth-fix/SIXTH-FIX.md` §1.

| item | outcome |
|---|---|
| R5-1 | **Outside this run**; files untouched; index status corrected. |
| R5-2 | **Done.** |
| R5-3 | **Done.** |
| R5-4 | **Referred to jurors** — JQ-R04-CARRIES-a, -b (new), to sit before the DATE/CONTENT group; **handed forward** (A-0.7). |
| R5-5 | **Done.** |
| R5-6 | **Done.** |
| R5-7 | **Done** (with R5-10 and R5-12). |
| R5-8 | **Done.** |
| R5-9 | **Referred to jurors** (as R5-4). |
| R5-10 | **Done**, by the coordinator's withdrawal of the earlier sentence. |
| R5-11 | **Done.** |
| R5-12 | **Done.** |
| R5-13 | **Recorded**, not ruled; **referred to the coordinator** (below, item 2). |
| R5-14 | **Recorded**; **handed forward** as a named gap (A-0.8). |
| R5-15 | **Done** (with R5-4). |
| R5-16 | **Recorded**; unchanged, with reason. |
| R5-17 | **Recorded**; unchanged, with reason. |
| R5-18 | **Done** for the DATE, CONTENT, CONTENT-d and CARRIES files; **cannot be done** for JQ-N1, JQ-CANTEEN-8 (being answered) and JQ-R04-GATE (ratified) — below, item 1. |
| R5-19 | **Recorded.** |

## The juror rows

| identifier | outcome |
|---|---|
| JQ-N1-1 … -4 | unchanged (being answered; not this run's) |
| JQ-CANTEEN-8 | unchanged (being answered; not this run's) |
| JQ-R04-GATE | unchanged — **ratified** |
| JQ-R04-CARRIES-a | **added** |
| JQ-R04-CARRIES-b | **added** |
| JQ-R04-DATE-a | corrected |
| JQ-R04-DATE-b | corrected |
| JQ-R04-DATE-c | corrected |
| JQ-R04-CONTENT-a | corrected |
| JQ-R04-CONTENT-b | corrected |
| JQ-R04-CONTENT-c | corrected |
| JQ-R04-CONTENT-d | corrected (moved to a file of its own; identifier kept) |
| JQ-B1 | unchanged (withdrawn) |

**Fitness, row by row** (SIXTH-FIX §4, against REVIEW-2's (i)–(v),
REVIEW-4's (vi), no contradiction with the ratified GATE verdict, the
coupling test, REVIEW-5's deletion test, and the instruction's pointer
test): JQ-R04-DATE-a, -b, -c and JQ-R04-CONTENT-a, -b, -c — **fit**;
JQ-R04-CONTENT-d — **fit by my tests**, with its scope contested and not
ruled (R5-13); JQ-R04-CARRIES-a, -b — **fit by my tests**. None of these
has been reviewed since this run; the CARRIES rows never have. "Fit" on
(iii), (vi) and coupling is my judgement; a reviewer may draw the line
elsewhere.

**The order in which the groups must sit** (in the index, by identifier
only): the JQ-N1 group with JQ-CANTEEN-8 now; JQ-R04-CARRIES-a and -b next,
and before the DATE/CONTENT group; JQ-R04-DATE-a … -c with
JQ-R04-CONTENT-a … -c only after JQ-R04-CARRIES is ratified, given its
ratification sentence only; JQ-R04-CONTENT-d alone, at any time. The three
R-04 groups have three disjoint sets of jurors.

The index (`exam-prep/JUROR-QUESTIONS.md`, re-issued; the fifth-fix version
kept byte for byte at `exam-prep/sixth-fix/JUROR-QUESTIONS-as-of-fifth-fix.md`,
every earlier one where it was) carries no wording, option or number of any
question, and no reading list names a review, `VERDICT.md`,
`HANDED-FORWARD.md` or a working file.

Checked by `scripts/33_juror_file_check_sixth.py`, run `b0af115f117e9f68`: 328 checks, 0 failed (`exam-prep/sixth-fix/checks/juror-file-check-b0af115f117e9f68.md`). Three earlier records of the same checks (`354ffc0d8a910e0c`, `ddf02843e31ff328`, `7378a60fc1cccf97`, none failed) are kept and superseded; the first was made by a version whose check order depended on Python's hash seed, so its re-run stopped under RULES 30 (SIXTH-FIX §7).

## Where I disagree with the fifth review (RULES 32)

No disagreement. Extensions, each named with its reason in SIXTH-FIX §2:
the GATE juror file's path is removed from part d, because that file shows
the gate row's measured figures (E-2); CONTENT's section heading no longer
defines "carries" (E-5); JQ-R04-CARRIES sits apart from part d as well as
from the DATE/CONTENT group, because REVIEW-5 §3's structure holds between
them too (SIXTH-FIX §4).

## For the coordinator

1. **Pointers this run could not remove.** JQ-N1 and JQ-CANTEEN-8, which
   three jurors are answering now, name working files and script runs
   (JQ-N1 lines 22, 86–87 and 148; JQ-CANTEEN-8 lines 100–101), and the
   ratified JQ-R04-GATE file names `exam-prep/REVIEW.md` and
   `exam-prep/R-04-blindness.md`. Each file tells the juror not to open
   them; whether a juror did is for the referee's independence and
   grounding checks. I changed none of them.
2. **R5-13 — part d's scope.** If its referee judges that it decides
   whether a measured coin signature may stay on exam cards ungraded — a
   rule, not a definition — it goes to the user (RULES 33), not back to me.
3. **The nearest-neighbour stop.** If either A-0.7 or the fifth-fix A-0.4
   step 3 reaches its stop on exam material, which version of the attack
   counts is an open question (RULES 33) for you to refer.
4. **Identifiers carry subjects** (R3-16, still undecided); the new
   identifier JQ-R04-CARRIES does too.
5. **Review before commissioning** — the corrected and new rows say "not
   reviewed since" / "never reviewed"; whether a sixth review precedes
   commissioning is yours.

## `RULES.md`

**No change to `RULES.md` is required by anything this run did or referred.**
The path named by earlier runs — a measured channel that cannot be removed,
and whether RULES 9 accepts it, which is the user's — remains possible and
has not been reached; part d's scope (item 2 above) is the point at which
it would be.

## A steer in the instruction I was given

No result and no prediction. Named, because they choose a route:
(1) "write it as a juror question that is answered **before** that group
sits" chooses, for the gap REVIEW-5 §2 found, the route REVIEW-5 left to the
coordinator ("a sub-part put to the same jurors, or something else"); I
followed it (R5-4). (2) The withdrawal of the fifth instruction's sentence
("the reviews' rulings on couplings govern") settles the conflict REVIEW-5
§3 left to the coordinator, and so decides that part d leaves the
DATE/CONTENT group; I followed it (R5-10). Both are the coordinator's to
make. Mildly: "one jury waits on the files this run corrects" presumes the
files can be corrected and puts weight on speed. "Three jurors are
answering … now" is information, and it is why JQ-N1 and JQ-CANTEEN-8 were
not touched. The git status supplied at start carried only commit subjects
of the forms "work:" and "ledger:" and four untracked instruction file names;
no result.

## What this run did not do

SIXTH-FIX §5, six items. The ones that matter most: **R-04 is not solved**;
**nothing was measured on exam cards**; **no corrected or new row has been
reviewed**; **three juror files this run may not touch still name working
files**.

Nothing under `exam/` was read or written by this run.

---
---

# Seventh-fix run · 2026-10-01 — acting on `exam-prep/REVIEW-6.md`, JQ-R04-CONTENT-d only

Mateo · data engineer · appended 2026-10-01 (system clock, RULES 23).
**Nothing above this line was changed**: the first 42,122 bytes of this file
are the file as the sixth review found it (SHA-256
`e6e568e04208011041a0d3d1566b3727098d5644c51f7665abc3a5ca4f16f2a0`). This
section says what happened, not how; the working is in
`exam-prep/seventh-fix/SEVENTH-FIX.md`; what later runs must do is in the
fourth-fix, fifth-fix, sixth-fix and seventh-fix sections of
`exam-prep/HANDED-FORWARD.md`, read together.

## The two problems now

| problem | sixth-fix verdict | now |
|---|---|---|
| **R-04 · is the exam blind?** | NOT SOLVED | **NOT SOLVED.** Nothing was measured. R-04 now needs the ratified outcomes of JQ-R04-CARRIES-a, -b, JQ-R04-DATE-a … -c and JQ-R04-CONTENT-a … -c, **and the user's recorded answer to U-1** (`exam-prep/USER-QUESTIONS.md`), which takes the place of JQ-R04-CONTENT-d. None of these exists yet. |
| **N-1 · collapse before counting** | not acted on | **Not acted on by this run.** Its juror group is ratified (`decisions/2026-10-01-jq-n1-canteen-8/verdict.md`); the index now says so. N-1's other conditions (the judge's script, HANDED-FORWARD B-1 … B-5) are unchanged. |

## Outcome of every REVIEW-6 item

Numbering: `exam-prep/seventh-fix/SEVENTH-FIX.md` §1.

| item | outcome |
|---|---|
| R6-1 | **Outside this run**; file untouched; index status corrected. |
| R6-2 | **Outside this run**; files untouched; index status corrected. |
| R6-3 | **Outside this run**; recorded. |
| R6-4 | **Outside this run**; recorded. |
| R6-5 | **Outside this run**; recorded. |
| R6-6 | **Done by withdrawal**: JQ-R04-CONTENT-d is withdrawn from jurors and **referred to the user** (U-1). |
| R6-7 | **Done** (HANDED-FORWARD seventh-fix A-0.1 and A-0.4 step 1). R-04 still waits on the user's answer. |
| R6-8 | **Done**, in U-1 and in HANDED-FORWARD seventh-fix A-0.4 step 1. |
| R6-9 | **Done**; agreed. |
| R6-10 | **Done**: classed **outside, as a whole** — one step beyond REVIEW-6 (reasons: SEVENTH-FIX §2). |
| R6-11 | **Recorded**; U-1 contradicts neither ratified verdict. |
| R6-12 | **Done** (index). |
| R6-13 | **Outside this run**; **referred to the coordinator** (below, item 2). |
| R6-14 | **Recorded.** |
| R6-15 | **Recorded.** |
| R6-16 | **Recorded.** |
| R6-17 | **Recorded.** |
| R6-18 | **Recorded.** |

## JQ-R04-CONTENT-d

**User question only.** No part of it remains a juror question, so no part
of it has to meet the juror tests; its file is kept unchanged as a record,
and the index marks the row **withdrawn**, pointing to U-1.
`exam-prep/USER-QUESTIONS.md` **now exists** and holds U-1, written for a
reader who has not seen `exam-prep/`, recommending nothing and carrying no
measured figure. It has not been reviewed.

## The juror rows

| identifier | outcome |
|---|---|
| JQ-N1-1 … -4, JQ-CANTEEN-8 | unchanged — status corrected to **ratified** |
| JQ-R04-GATE | unchanged — **ratified** |
| JQ-R04-CARRIES-a, -b | unchanged — status corrected to **being answered**, ruled fit by the sixth review |
| JQ-R04-DATE-a … -c | unchanged — **waiting** for the CARRIES ratification; ruled fit by the sixth review |
| JQ-R04-CONTENT-a … -c | unchanged — **waiting** as DATE; ruled fit by the sixth review |
| JQ-R04-CONTENT-d | **withdrawn** — referred to the user (U-1) |
| JQ-B1 | unchanged (withdrawn) |

The index (`exam-prep/JUROR-QUESTIONS.md`, re-issued; the sixth-fix version
kept byte for byte at `exam-prep/seventh-fix/JUROR-QUESTIONS-as-of-sixth-fix.md`,
every earlier one where it was) shows each row's true status, carries no
wording, option or number of any question, and changes no reading list.

Checked by `scripts/34_seventh_fix_check.py`, run `97f03e98c28ed3ad`: 100
checks, 0 failed (`exam-prep/seventh-fix/checks/seventh-fix-check-97f03e98c28ed3ad.md`).

## Where I go beyond the sixth review (RULES 32)

REVIEW-6 §3 left part d's scope contested and called its option "no"
inside. I class the whole row outside: with its two outside options gone it
would offer one answer, which is not a question; and asked now, the rule
question is answered before any exam card is measured (RULES 6). Reasons and
the opposite case: SEVENTH-FIX §2. No disagreement with REVIEW-6 otherwise.

## For the coordinator

1. **U-1 goes to the user**, unread by you, as the instruction says. It
   must not reach a juror or a referee (HANDED-FORWARD seventh-fix C-5).
   The user may return it to jurors; U-1 says so.
2. **R6-13.** The DATE/CONTENT reading lists give "the ratification
   sentence" of JQ-R04-CARRIES, which has two parts. Whether the commission
   gives one sentence per part is yours; this run did not touch those lists.
3. **Two juror files this run may not touch now say something untrue**: the
   closing paragraphs of JQ-R04-DATE and JQ-R04-CONTENT say that what
   follows for a field that stays is decided by JQ-R04-CONTENT-d, "which
   other jurors answer". It now goes to the user. Their operative clause
   ("it is not yours to decide") stays true. Whether a run corrects them,
   and a review checks it, before that group sits is yours.
4. **`decisions/2026-10-01-jq-r04-date-content/`** appeared, untracked, in
   `git status` during this run. I did not open it. If the DATE/CONTENT
   group has been commissioned before JQ-R04-CARRIES is ratified, the order
   in the index and in HANDED-FORWARD A-0.1 is broken. I cannot tell from a
   name.
5. **Review before use.** U-1 and this run's HANDED-FORWARD amendments are
   not reviewed. Whether a review precedes bringing U-1 to the user is
   yours.
6. **`LEDGER.md`** — whether the two ratifications, and later the user's
   answer, are written there I cannot check.

## `RULES.md`

**This run changes nothing in `RULES.md`.** The path earlier runs named — a
measured channel that cannot be removed, and whether RULES 9 accepts it,
which is the user's — **is now reached, in advance**: U-1 asks it before any
exam card is measured. What the user answers, and whether it is recorded as
a rule, is the user's.

## A steer in the instruction I was given

No result and no prediction. Named, mildly: the model-choice reason "a part
of it may have to go to the user rather than to jurors" presumes the user
route is possible and frames the answer as a split; I classed the whole row
for the user, which the instruction allows ("If you judge … the whole of it
outside, say so"), for reasons that do not rest on that sentence (SEVENTH-FIX
§2). "Which review 6 ruled fit" and "three jurors are answering … now" are
information; they are why the three juror files were left untouched and why
the CARRIES status reads "being answered". The git status supplied at start
carried commit subjects of the forms "work:", "ledger:" and "auto: working
tree", three untracked instruction file names for JQ-R04-CARRIES jurors and
this run's own; no result.

## What this run did not do

SEVENTH-FIX §4, eight items. The ones that matter most: **R-04 is not
solved**; **nothing was measured on exam cards**; **U-1 is not reviewed**;
**two juror files now carry a stale clause this run may not correct**.

Nothing under `exam/` was read or written by this run.
