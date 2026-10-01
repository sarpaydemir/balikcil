# Sixth fix — acting on `exam-prep/REVIEW-5.md`, DATE and CONTENT rows only

Mateo · data engineer · sixth-fix run · first clock read 2026-10-01T22:50:55Z,
this file written after 2026-10-01T23:08:16Z (system clock, RULES 23) ·
free disk 12,384,276,480 bytes at 22:59:50Z, 12,383,346,688 bytes at
23:08:16Z · nothing was downloaded.

**This file is a working file. It says why passages were moved or removed
and where the removed provenance lives. It must not reach a juror or a
referee** (HANDED-FORWARD, sixth-fix section, C-5).

Criteria, written before any juror file, the index, `VERDICT.md` or
`HANDED-FORWARD.md` was changed:
`exam-prep/sixth-fix/criteria-written-before-correcting.md`.

**Opened:** `RULES.md`, `TACTICS.md`; `exam-prep/` — `REVIEW-5.md` (whole),
`review-5/criteria-written-before-ruling.md`,
`review-4/criteria-written-before-ruling.md`, REVIEW-3 lines 176–245 and
288–300, REVIEW-2 lines 226–303, a `grep` of REVIEW.md, `JUROR-QUESTIONS.md`,
`VERDICT.md` (whole), `fifth-fix/FIFTH-FIX.md`, its criteria file, the
fifth-fix JQ-R04-DATE and JQ-R04-CONTENT files, `HANDED-FORWARD.md`
(headings, lines 380–490), `third-fix/juror-questions/JQ-R04-GATE.md`
lines 1–161, `review-3/probes/q2_tiefree_strict-flags.out` (a `grep`),
`fifth-fix/pre-run-fingerprints.txt` (its `scripts/` lines),
`review-2/rerun/blind-k1/cards/B001.md` lines 1–45; a `grep` of the
fifth-fix JQ-N1 and JQ-CANTEEN-8 files for paths (read only);
`decisions/2026-10-01-jq-r04-gate/verdict.md`; `canteen/2026-09-19-sofia.md`
lines 108–122, 218–272, 662–673; `scripts/29_identity_audit_exact.py`
lines 1–172, 217–450, 720–745; `scripts/32_juror_file_check_fifth.py`
lines 1–60.
**Not opened:** `exam/`; the rest of `decisions/`; `instructions/`;
`LEDGER.md`; `reports/`; `external/`; `notes/`; `TEAM.md`, the root
`README.md`, `cards/`, `data/` (allowed, not needed); any `scripts/exam_*`
(not read, not hashed, not run; their bytecode names appear in a listing of
`scripts/__pycache__/`); git history (`git status --porcelain` was run once, at the end, to list what this run wrote; no log, show or diff); anything outside the Balıkçıl
folder. No memory or session-log search. One tool output was too large to
show and was saved by the harness to a file outside this folder; I did not
open that file and re-ran the command with a narrower scope instead (twice:
a directory listing and a `cat` of `VERDICT.md`). Every script run used
`PYTHONDONTWRITEBYTECODE=1` and `python3 -B`; `scripts/__pycache__/` held
the same nine names before and after.

---

## 1 · REVIEW-5's items and their outcomes

REVIEW-5 does not number its requirements. I number here, in order of
appearance, every item that concerns the DATE or CONTENT rows, and name the
rest as outside this run.

| item | where in REVIEW-5 | outcome |
|---|---|---|
| R5-1 | §1, rows JQ-N1-1 … -4, JQ-CANTEEN-8 | **outside this run** (not DATE/CONTENT); files untouched. The index now shows their true status (commissioned, being answered; ruled fit). |
| R5-2 | §1, JQ-R04-DATE-a "fit on its own text"; group not commissionable (§3) | **done**: file corrected (closing paragraph, pointers; E-1, E-4); the row stays fit; its group now waits only on JQ-R04-CARRIES. |
| R5-3 | §1, JQ-R04-DATE-b, -c | **done**, as R5-2. |
| R5-4 | §1, JQ-R04-CONTENT-a "not fit" — the gap of §2 | **referred to jurors**: new rows **JQ-R04-CARRIES-a** and **-b**, answered **before** the DATE/CONTENT group, by other jurors; CONTENT part a names it; **handed forward** (A-0.7). |
| R5-5 | §1, JQ-R04-CONTENT-b "not fit" — (vi) L1 through the closing paragraph | **done**: the closing paragraph no longer states the gate's consequence; it names where the rest is decided (E-1). |
| R5-6 | §1, JQ-R04-CONTENT-c "fit on its own text" | **done**: only its source note changed (E-4); fit. |
| R5-7 | §1, JQ-R04-CONTENT-d "not fit" — coupling and (ii) | **done**: see R5-10 and R5-12. |
| R5-8 | §1 "Groups" | **done**: the DATE/CONTENT group is now JQ-R04-DATE-a … -c with JQ-R04-CONTENT-a … -c; its order after JQ-R04-CARRIES is in the index. |
| R5-9 | §2, the gap must be answered before the group; route is the coordinator's | **referred to jurors** (as R5-4), by the route the sixth-fix instruction chose (§6 below). |
| R5-10 | §3, part d's coupling; "the coordinator must choose" | **done**: the coordinator withdrew the fifth instruction's sentence where it conflicts with a review's coupling ruling. Part d is a file of its own (`JQ-R04-CONTENT-d.md`), answered alone, by jurors who sit on no other R-04 row (E-2). |
| R5-11 | §3, last sentence: the closing paragraph CONTENT-b's jurors read must stop showing the gate consequence | **done** (E-1), in both DATE and CONTENT. |
| R5-12 | §4 (ii): d's option "no" not determinate; the file does not say which families are outside the row or why | **done**: the four families outside the row are named with the reason the audit's code gives for each (quoted, checked); option "no" is reworded so that it is determinate (E-3). |
| R5-13 | §4 (iv): contested, not ruled | **recorded**; not ruled by me. Part d keeps its paragraph telling jurors to say so if they find it a question about a rule; whether that suffices is the referee's scope check or the user's (VERDICT "For the coordinator"). |
| R5-14 | §5: no contradiction; a gap outside the rows (which nearest-neighbour version the gate's "attack" is) | **recorded** and **handed forward** as a named gap (A-0.8); the same stop is used for JQ-R04-CARRIES (A-0.7). |
| R5-15 | §6, disagreement 2's consequence "not followed through" | **done** with R5-4. |
| R5-16 | §7, reading lists comply; canteen range 112–120 carries two and a half lines beyond the quotation, named not ruled | **recorded; unchanged**: those lines are the rest of the frozen rule S-1's own trigger, which a juror may need to cite whole (RULES 34), and REVIEW-5 found they read toward b1 and b3 alike. |
| R5-17 | §7, cited not listed (CONTENT part a cites canteen lines 229–234 and 251; CANTEEN-8 cites others) | **recorded; unchanged.** CONTENT part a quotes what its question needs; those lines are the watcher evidence under B-2 and B-3 (card numbers, observation coin names and dates) that no question asks about, so adding them would give more than needed. REVIEW-5 ruled (i) not failed. CANTEEN-8 is outside this run. |
| R5-18 | §7, pointers inside listed files (DATE and CONTENT headers name reviews; CONTENT names a review-3 probe) | **done for every DATE/CONTENT file and both new files** (E-4; required also by the instruction, item 3). **Cannot be done** for JQ-N1, JQ-CANTEEN-8 (three jurors are answering them; the instruction forbids changing them) and JQ-R04-GATE (ratified): they still name working files — see §5. |
| R5-19 | §9 items 4–5, §10, §11 | **recorded**; nothing required. R4-9 is still not visible to me. |

## 2 · Changes, with reasons (RULES 32)

- **E-1 · Closing paragraphs of DATE and CONTENT** (R5-5, R5-11, (vii)). The
  CONTENT paragraph stated that a graded channel fails the gate if either
  attack beats its line; read with part b's table, it showed what option b1
  does to whether material passes (REVIEW-5 §1). Both paragraphs now say
  that the field stays and what the audit measures from it is named in the
  exam manifest with its number, and that "what else follows … is decided by
  a separate question, JQ-R04-CONTENT-d, which other jurors answer; it is
  not yours to decide." That is true under the ratified verdict and says
  where the rest is decided, as test (vii) requires, without the fail
  condition.
- **E-2 · Part d moved out** (R5-7, R5-10). Text kept: the gate step, the
  ratified sentence, the definition of `ALL-removable`, the premise
  sentence, the question (only "to parts a–c here" became "to JQ-R04-CONTENT
  parts a–c"), options "yes" and "only where…", the scope paragraph, and the
  "read from the audit's code" sentence (checked word for word by script,
  D). Added: who answers it and why; what the other questions decide,
  without their options or answers; the rule texts it now needs on its own
  (RULES 6, 9, 12; TACTICS §3 and §6, quoted, checked). **Removed: the path
  of the GATE juror file**, which carries the gate row's measured figures on
  the observation cards; a d-juror who opened it would see an effect of
  d's options (L1). The quotations from it stay, attributed to "the
  acceptance-gate question (JQ-R04-GATE)".
- **E-3 · Part d, the four families outside the row and option "no"**
  (R5-12). REVIEW-5: "Telling them would be a precedent, but it would be a
  needed one." The four names and the code's reason for each are quoted
  from `scripts/29_identity_audit_exact.py` lines 431–434; the file says
  the question does not ask about them. Option "no" now reads: "a field
  that stays on the card because jurors ruled that it may or must stay is
  not thereby one that TACTICS requires; only the four families listed
  above stay outside the row, and the features of every field the ratified
  answers keep stay in it, and the gate grades them." It no longer turns on
  "by its own words", which could not separate a kept column from
  `p7-shape`; it is carried out by a fixed list.
- **E-4 · Pointers** (R5-18; instruction item 3). Removed from DATE and
  CONTENT: the header history naming `exam-prep/REVIEW.md` and `REVIEW-3.md`
  (replaced by a short history without file names; every earlier version is
  kept); every script path, run number, working folder, manifest, the
  SECOND-FIX pointer and the review-3 probe; "The review found" became "A
  check found". The facts stay; the sources are in §3. Two section numbers
  of a review (3.4, 3.2) disappear with the pointers; no figure does
  (checked, N).
- **E-5 · CONTENT's section heading** "How 'carries a coin signature' is
  measured" became "How the figures in this file are measured". Kept, it
  would have told part a's jurors what "carries" means while
  JQ-R04-CARRIES is asked to define it — a precedent on the open point
  (L2), not needed. Its text is unchanged.
- **E-6 · CONTENT part a, one paragraph added**: what "carries a measured
  coin signature" means is fixed by JQ-R04-CARRIES, answered before them
  by other jurors; its ratification sentence is given to them; they are not
  asked to apply it. "What you open" gains that sentence; the index lists
  it.
- **E-7 · New file JQ-R04-CARRIES** (R5-4, R5-9). Part a: which attack
  decides (pair AUC; nearest neighbour; either; both; other) — the same
  option set as the GATE question, with no precedent shown (the GATE
  verdict and the first run's "both" for single families are precedents on
  an analogous point; neither is needed, and showing one would lean). Part
  b: which features count as the column's (own features as one set; every
  family that reads the column; only families made of the column alone;
  other), each with one ground, and for the trade-count column the families
  each option names, read from the audit's code (checked, Q). The
  nearest-neighbour tie versions are described, with the stop the gate
  already uses if they disagree; the file says this question does not
  settle that (R5-14). No measured figure.
- **E-8 · The index** re-issued: new rows, true statuses, the order in
  which groups sit, three disjoint juror sets, the CARRIES ratification
  sentence on the DATE/CONTENT lists; the fifth-fix index kept byte for
  byte at `exam-prep/sixth-fix/JUROR-QUESTIONS-as-of-fifth-fix.md`.
- **E-9 · HANDED-FORWARD**, sixth-fix section appended: A-0.1 and C-5
  replaced; A-0.7 (applying CONTENT-a with the CARRIES definition) and A-0.8
  (the named gap) added.
- **E-10 · `exam-prep/README.md`**, a reading-order addendum appended, as
  each earlier run did.

## 3 · Provenance removed from juror files, kept here for reviewers

| juror file, place | figure or passage | source |
|---|---|---|
| DATE part a | 243 of 495; 0 of 46,170 | `scripts/16_identity_audit.py`, run `13d935bb5cf78346`, T3 |
| DATE part b | 100 of 306; 30; 13; 18; the 13 names | `scripts/16_identity_audit.py`, run `e05144718b909704`, T4 |
| DATE part c | 99 cards | a `grep` count; command in `exam-prep/second-fix/SECOND-FIX.md` §6 |
| CONTENT, how figures are measured | the audit | `scripts/29_identity_audit_exact.py`, folder `exam-prep/fourth-fix/identity/` |
| CONTENT part b, first column | 36; 0 | `exam-prep/second-fix/blind-proof/strict-flags-k1/blind-manifest-strict-flags-k1.md` |
| CONTENT part b, attack figures | 2 decimals / 3 decimals | audit runs `9ff0ffec3fe21ebe` / `762815a877c19551` |
| CONTENT part b, seed note | "a verdict this close can change with the seed" | `exam-prep/review-3/probes/q2_tiefree_strict-flags.out` (REVIEW-3 §3, R2-16 row: 0.65% of 2,000 further shuffles) |
| CONTENT part c, table | H-4 counts | `scripts/30_fourth_fix_checks.py`, run `516027c6c9f215d6`, H-4 |
| CONTENT-d, gate step and row definition | quotations | `exam-prep/third-fix/juror-questions/JQ-R04-GATE.md` lines 55–57 and 64–66 |
| CONTENT-d, the four families | quotations | `scripts/29_identity_audit_exact.py` lines 429–436 (`FORCED_FAMILIES` and its comment) |
| CONTENT-d premise; CARRIES family description | features and families | `scripts/29_identity_audit_exact.py` `card_features()` (from line 217), `REPEAT_GROUP` and `FAMILIES` (from line 395), `standardise()` (line 450) |

## 4 · The rows, row by row

Tests: criteria §1 — (i)–(v), (vi), (vii), (viii) coupling, (ix) deletion,
(x) pointers. Script checks: `scripts/33_juror_file_check_sixth.py`, run
named in `VERDICT.md`'s sixth-fix section. Judgement tests ((iii), (vi),
(viii)) are mine.

| row | (i) | (ii) | (iii) | (iv) | (v) | (vi) | (vii) | (viii) | (ix) | (x) | result |
|---|---|---|---|---|---|---|---|---|---|---|---|
| JQ-R04-DATE-a | yes | yes/no both carried out (mask; stays) | wording unchanged; fit in reviews 2–5 | definition | 243/495, 0/46,170 unchanged | L2 sentence gone (fifth fix); closing paragraph shows no gate effect | closing paragraph true, names where decided | group has no gate-side row | nothing points at part d; "three parts" | pass | **fit** |
| JQ-R04-DATE-b | yes | yes | unchanged | definition | 100/30/13/18 unchanged | as DATE-a | as DATE-a | as DATE-a | as DATE-a | pass | **fit** |
| JQ-R04-DATE-c | yes | yes | unchanged | definition | 99 unchanged | as DATE-a | as DATE-a | as DATE-a | as DATE-a | pass | **fit** |
| JQ-R04-CONTENT-a | yes, with the CARRIES ratification sentence | **now yes**: "carries" is fixed before the group sits (A-0.7); one residual stop named (nearest-neighbour versions disagree) | question and options unchanged; the added paragraph names a question, not an outcome | definition | no figure | added paragraph needed (premise of the condition), no lean; heading no longer defines "carries" (E-5) | none | CARRIES chosen by other jurors | — | pass | **fit** |
| JQ-R04-CONTENT-b | yes | yes | unchanged | definition | figures unchanged (reproduced by REVIEW-4) | **the L1 item is gone** (E-1); b's figures are b1's premise | as DATE-a | d no longer in the group | — | pass | **fit** |
| JQ-R04-CONTENT-c | yes | yes | unchanged | definition | H-4 unchanged | no effect shown | as DATE-a | as CONTENT-b | — | pass | **fit** |
| JQ-R04-CONTENT-d | yes | **now yes** for "no" (fixed list) and "yes"; middle option carried out from the ratified answers | one ground per option; "no" reworded | definition, **contested** (R5-13), scope paragraph kept | no measured figure; premise and quotations checked (Q) | four-family list is a needed precedent (REVIEW-5 §4); GATE file path removed (E-2) | quotes the verdict; does not reopen it | **alone; disjoint jurors** | — | pass | **fit by my tests; not reviewed** |
| JQ-R04-CARRIES-a | yes | yes; nearest-neighbour disagreement stops and is referred | same option set as GATE; no grounds, no precedent | definition; scope objection invited | no measured figure | no effect, no precedent, no one-sided argument | does not touch the gate | **alone; disjoint jurors** | — | pass | **fit by my tests; never reviewed** |
| JQ-R04-CARRIES-b | yes | yes; option one needs a new audit row (A-0.7 says how) | one ground per option | definition | code facts checked (Q) | as CARRIES-a | as CARRIES-a | as CARRIES-a | — | pass | **fit by my tests; never reviewed** |

**Couplings, as they now stand.** DATE-a … -c with CONTENT-a … -c: kept
(REVIEW-3 §5; both read RULES 9 against TACTICS 3 and 6). JQ-R04-CONTENT-d:
alone. JQ-R04-CARRIES-a with -b: together (one definition in two halves; no
rendering and no gate choice in it); not with DATE/CONTENT (its jurors would
then choose both a condition and the answer that uses it) and not with d
(a narrow "carries" with a "no" to d, and a broad one with any d, act
differently on the same column — REVIEW-5 §3's structure). Three disjoint
juror sets.

## 5 · What I could not do, by name

1. **Pointers in JQ-N1, JQ-CANTEEN-8 and JQ-R04-GATE.** JQ-N1 names
   `exam-prep/N-1-collapse.md` (line 22), a collapse run and its CSV (lines
   86–87) and a fourth-fix checks file (line 148); JQ-CANTEEN-8 names two
   script runs (lines 100–101); JQ-R04-GATE names `exam-prep/REVIEW.md`,
   `exam-prep/R-04-blindness.md`, script 16 runs and a working folder.
   The first two are being answered now and must not change; GATE is
   ratified. The instruction's item 3 cannot be met for them by this run.
2. **No figure was re-measured.** No juror figure is new; the DATE and
   CONTENT figures were reproduced by REVIEW-3 and REVIEW-4, not by me.
3. **Nothing measured on exam cards**; `exam/` is closed.
4. **The new and moved rows are not reviewed.**
5. **R4-9 ("earlier verdicts")** — still not visible to me.
6. **Whether the nearest-neighbour stop (A-0.7, A-0.8) will be reached** —
   it depends on exam material.

## 6 · Decisions I took that the instruction did not cover

1. **Numbering REVIEW-5's items** R5-1 … R5-19 (§1).
2. **JQ-R04-CARRIES as a group of its own, with jurors disjoint from both
   other R-04 groups** (§4 couplings). The instruction said "answered
   before that group sits"; it did not say by whom.
3. **The two parts of JQ-R04-CARRIES and their options** (E-7). Part b's
   three options are mine, built from the audit's family structure; "other"
   is open.
4. **The nearest-neighbour tie stop in CARRIES** (E-7, A-0.7): taken from
   the stop the fifth-fix A-0.4 already uses; not put as a third part,
   because REVIEW-5 named it as a gap outside the rows.
5. **Giving the DATE/CONTENT group the CARRIES ratification sentence only**
   (E-6), rather than nothing or the whole verdict.
6. **Part d keeps its identifier JQ-R04-CONTENT-d** in a file of its own,
   so that nothing claimed earlier under that name disappears and the
   fifth-fix A-0.4 step 1 still points at it.
7. **The GATE file path removed from part d** (E-2), and every script path
   removed from juror files (E-4) — stricter than "working file".
8. **Index statuses of the JQ-N1 rows updated** to the true state (being
   answered; ruled fit), though those rows are outside this run.
9. **Pre-run snapshots**: `exam-prep/` before anything was written;
   `scripts/` (non-`exam_*`) after the juror files were drafted but before
   any script was written.

## 7 · How to reproduce, and one defect of my own

`PYTHONDONTWRITEBYTECODE=1 python3 -B scripts/33_juror_file_check_sixth.py --dry`
runs every check and writes nothing; without `--dry` it records
(append-only; a different content under an existing run number stops it).

**Run of record: `b0af115f117e9f68`** — 328 checks, 328 ok, 0 failed;
recorded at 2026-10-01T23:11:17Z and re-run at once with a different
`PYTHONHASHSEED`, which wrote nothing new (same bytes).

Superseded, kept: `ddf02843e31ff328` (23:10:34Z; 327 checks, 0 failed) —
recorded before I appended this run's addendum to `exam-prep/README.md`;
`7378a60fc1cccf97` (23:11:06Z; 328 checks, 0 failed) — the check then
treated `README.md` as appended, but its comment gave the wrong clock for
that measurement and its run number did not include `README.md`'s pre-run
prefix; both were corrected in `b0af115f117e9f68`.

**Superseded: `354ffc0d8a910e0c`.** The first recorded run (23:10:12Z,
327 checks, 0 failed) came from a version that looped over a Python `set`
when checking the DATE/CONTENT index rows, so the order of its report lines
depended on the hash seed. Re-running it at 23:10:17Z produced different
bytes under the same run number and the script stopped, as RULES 30
requires. I changed that loop to a sorted one (the script is an input, so
the run number changed), checked that three hash seeds give the same
results, and recorded again. The superseded record is kept, not deleted.
Its result (every check ok) is the same; only the line order differed.
