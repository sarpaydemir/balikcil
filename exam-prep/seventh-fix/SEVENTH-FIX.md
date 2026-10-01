# Seventh fix — acting on `exam-prep/REVIEW-6.md`, JQ-R04-CONTENT-d only

Mateo · data engineer · seventh-fix run · first clock read
2026-10-01T23:27:09Z, this file written after 2026-10-01T23:40:37Z (system
clock, RULES 23) · free disk 12,379,213,824 bytes at 23:27:09Z,
12,372,901,888 bytes at 23:40:37Z · nothing was downloaded.

**This file is a working file. It discusses what the options of a withdrawn
juror question do. It must not reach a juror or a referee** (HANDED-FORWARD,
seventh-fix section, C-5).

Criteria, written after the pre-run snapshots and before any file outside
`exam-prep/seventh-fix/` was written:
`exam-prep/seventh-fix/criteria-written-before-correcting.md`.

**Opened:** `RULES.md`, `TACTICS.md`; `decisions/2026-10-01-jq-r04-gate/verdict.md`,
`decisions/2026-10-01-jq-n1-canteen-8/verdict.md`; `exam-prep/` —
`REVIEW-6.md` (whole) and its criteria file, `REVIEW-5.md` (whole) and its
criteria file, the REVIEW-4 criteria file, REVIEW-3 lines 176–300, REVIEW-2
lines 220–320, `JUROR-QUESTIONS.md`, `VERDICT.md` (whole),
`HANDED-FORWARD.md` (headings, lines 137–306, 400–578), `README.md` (lines
60–132), `sixth-fix/SIXTH-FIX.md`, `sixth-fix/FINGERPRINTS.md` (first 40
lines), `sixth-fix/pre-run-fingerprints.txt` (first 5 lines), the sixth-fix
DATE, CONTENT and CONTENT-d juror files (read; not changed), a `grep` of the
CARRIES file for mentions of part d or the user (none; not otherwise read),
`third-fix/juror-questions/JQ-R04-GATE.md` lines 40–100, a `grep` of
`fifth-fix/FINGERPRINTS.md`; `scripts/29_identity_audit_exact.py` lines
217–470 and a `grep`. `git status` twice and `git ls-files` once on this
run's folder (working tree and index only).
**Not opened:** `exam/`; the rest of `decisions/` (a directory name,
`decisions/2026-10-01-jq-r04-date-content/`, appeared untracked in
`git status`; not opened — see §6 item 6); `instructions/`; `LEDGER.md`;
`reports/`; `external/`; `notes/`; `canteen/`, `cards/`, `data/`,
`TEAM.md`, root `README.md` (allowed, not needed); any `scripts/exam_*`
(not read, hashed or run; their bytecode names appear in a listing of
`scripts/__pycache__/`); git history; anything outside the Balıkçıl folder.
No memory or session-log search. Every script run used
`PYTHONDONTWRITEBYTECODE=1` and `python3 -B`; `scripts/__pycache__/` held the
same nine names before and after.

---

## 1 · REVIEW-6's items and their outcomes

REVIEW-6 does not number its requirements. I number here, in order of
appearance, every item, and act on those that concern JQ-R04-CONTENT-d and
on the index's stale statuses.

| item | where in REVIEW-6 | outcome |
|---|---|---|
| R6-1 | §1, JQ-R04-CARRIES-a, -b: fit, inside | **outside this run**; file untouched (hash checked). Index status corrected to "commissioned — being answered; ruled fit by the sixth review" (the instruction says three jurors are answering now). |
| R6-2 | §1, JQ-R04-DATE-a … -c: fit, inside | **outside this run**; file untouched. Index status: waiting; ruled fit by the sixth review. |
| R6-3 | §1, JQ-R04-CONTENT-a: fit provided CARRIES is ratified first | **outside this run**; file untouched; the index keeps the order. |
| R6-4 | §1, JQ-R04-CONTENT-b: fit; a judgement noted | **outside this run**; recorded. |
| R6-5 | §1, JQ-R04-CONTENT-c: fit | **outside this run**; recorded. |
| R6-6 | §1, JQ-R04-CONTENT-d: not fit on (ii) and (vi) L2; scope contested | **done by withdrawal**: the row is withdrawn from jurors and its subject is put to the user as U-1 (`exam-prep/USER-QUESTIONS.md`); §2–§3 below. |
| R6-7 | §1 "Groups": d cannot be commissioned until corrected; R-04 cannot close without it (A-0.4 step 1) | **done**: A-0.4 step 1 now composes the row from the user's recorded answer to U-1 (HANDED-FORWARD, seventh-fix section); A-0.1 replaced accordingly. R-04 still cannot close without that answer. |
| R6-8 | §2.1, (ii): which ratified outcomes "keep" a field is not fixed (the eight other ranked columns; the reach of CONTENT-a's answer); A-0.4 step 1 does not say | **done**: U-1 part 2 asks the reach (narrow or wide), and each answer of U-1 is written so that it can be carried out; A-0.4 step 1 states how each is carried out and where it stops (§3). |
| R6-9 | §2.2, (vi) L2: the ground quoted for `p7-shape`; names needed, grounds not | **done**: the juror file is withdrawn; U-1 names the four groups outside the graded set **without** any ground. I agree with REVIEW-6, including its disagreement with REVIEW-5 §4. |
| R6-10 | §3, RULES 33 scope: contested, not ruled; case for "outside" stronger for "yes" and "only where…"; "no" inside | **done**: classed — **the whole of JQ-R04-CONTENT-d is outside a juror's scope** and goes to the user (§2). This goes one step beyond REVIEW-6 for option "no"; reasons in §2. |
| R6-11 | §4, no contradiction with either ratified verdict | **recorded**; U-1 quotes the GATE verdict's line 72 and changes nothing in it; it touches nothing the JQ-N1 verdict reads. |
| R6-12 | §5 note 1: the index is stale on the JQ-N1 group | **done**: the five rows read "ratified", with the verdict path; the order section says so. |
| R6-13 | §5 note 2: "the ratification sentence" is singular; CARRIES has two parts | **outside this run** (it concerns the CARRIES and DATE/CONTENT commissions); **referred to the coordinator**; the index's reading lists are unchanged. |
| R6-14 | §5 note 3: CARRIES refused → DATE/CONTENT waits | **recorded.** |
| R6-15 | §6, the sixth run's three extensions hold | **recorded.** Extension 1 is moot for jurors now that d is withdrawn; U-1 quotes the GATE file and does name its path, for the user, with a note that it contains measurements (§4 item 5). |
| R6-16 | §6, tests (vii) and (x) | **recorded.** |
| R6-17 | §7–§8, reproduction and what REVIEW-6 could not do | **recorded**; §8 item 2 (how many features each reading moves) is not measured here either. |
| R6-18 | §9–§11 | **recorded**; nothing required. |

## 2 · Scope: why the whole of JQ-R04-CONTENT-d goes to the user (RULES 32)

Test (criteria): a part is outside when an option, once ratified, would make
or change a rule; accepting or refusing, as a standard, a measured coin
channel on exam cards under RULES 9 counts as one.

1. **Options "yes" and "only where…" are outside.** Once ratified, each
   lets exam cards carry a coin channel the audit has measured as beating
   its RULES 12 line without failing the gate. That settles what RULES 9
   ("the coin name … hidden") demands of the exam — a standard, not the
   reading of a word. The second-, third-, fifth- and sixth-fix verdicts
   reserved exactly this case for the user (third-fix point 3: "a question
   about a rule, which is the user's"); REVIEW-5 §4 and REVIEW-6 §3 named
   it; REVIEW-6 found the case for "outside" the stronger one.
2. **Option "no" is, on its own, inside** (REVIEW-6 §3: "it reads a
   definition and moves nothing"). But a juror question stripped of the two
   outside options offers one answer. That is not a question: its wording
   would lean by construction (test (iii)), and "other" alone does not cure
   it. Splitting would also put "no" to jurors while the alternatives sit
   with the user: two deciders for one choice.
3. **The reach (REVIEW-6 §2.1) goes with it.** Which fields count as
   "kept" decides how much measured signature is left ungraded under the
   outside options; it has no effect under "no". So it belongs to whoever
   decides those options. It could be argued that the reach is a reading of
   juror outcomes and so a definition; I name that and did not write it as
   a juror question, because it is needed only if the user chooses an
   outside option, and a conditional juror row written now would have to be
   reviewed for a case that may never arise. If the coordinator or a
   reviewer prefers it as a juror question, it can be written then.
4. **RULES 6.** Left with jurors and answered "no", the same rule question
   would reach the user after the gate had been run on the exam cards
   (third-fix point 3), that is, after a result. Asked now, it is answered
   before any exam card is measured.

**The opposite case**, written into U-1 itself: the gate's definition is an
exam-preparation text, not `RULES.md`; whether a field kept by a juror's
ruling is one "that … TACTICS requires" reads that definition, so jurors
could answer it. U-1 gives the user the option to return it to jurors.

So JQ-R04-CONTENT-d is **user question only**; **no part of it remains a
juror question**.

## 3 · U-1 against the criteria (`criteria-written-before-correcting.md`)

| criterion | how U-1 meets it | checked by |
|---|---|---|
| 1 · followable without `exam-prep/` | every term used is explained in the file (gate, features, `ALL-removable`, frozen canteen book, manifest); identifiers appear only to say what U-1 replaces and in one file path | reading; script 34 U (identifiers) |
| 2 · what, which rule, why rule not definition, and the other side | sections "What must be decided" and "Which written rule it touches …" (RULES 9, the preamble, RULES 33, RULES 6), with "The other side" | reading |
| 3 · each answer determinate | A: a fixed list (the four `FORCED_FAMILIES`). B and C: with part 2's narrow reach, a fixed list of fields, each as its own ruling says; with the wide reach, every TACTICS 3 field except those a ruling removes (or, under C, lets a card do without). Feature-to-field is read from the code. Two named stops refer back (unclear reach of a ruling's words; a feature from two fields); REVIEW-5 §5 and REVIEW-6 §1 accepted stop-and-refer | reading; HANDED-FORWARD A-0.4 step 1 states the procedure |
| 4 · recommends nothing | each answer has a definition and a "for the exam" consequence and no reason for it; no ground is given for the four groups (REVIEW-6 §2.2); two sentences of an earlier draft were removed before recording because they leaned (the sentence that fields "are printed on the exam card unless a ruling says otherwise" presumed a reading jurors are deciding; "cannot be changed, RULES 6" was a mis-citation, replaced by `TACTICS.md` line 94) | reading; script 34 U (no recommending words) |
| 5 · no measured figure | no figure; the file says so, and why, and that figures exist | script 34 U (numbers on a declared list; no decimal) |
| 6 · quotations exact | 16 quotations, each found in its cited lines and in the file; two cited ranges checked | script 34 U |

**One mechanical statement, needed.** Under B with the wide reach the gate
would grade no feature the audit computes today, because every family
prefix of the audit maps to a field TACTICS 3 lists (script 34 U, 26
prefixes; every feature key written in `card_features()` is covered). This
is what the option does mechanically (REVIEW-4's criteria: needed, passes),
not a measurement.

## 4 · What I could not do, by name

1. **Nothing measured on exam cards**; `exam/` is closed.
2. **No juror question remains**, so nothing of d could be tested as a
   juror question; U-1 has not been reviewed.
3. **The DATE and CONTENT juror files now say something no longer true**:
   their closing paragraphs (DATE lines 147–149, CONTENT lines 260–262) say
   that what follows for a field that stays "is decided by a separate
   question, JQ-R04-CONTENT-d, which other jurors answer". It now goes to
   the user. The instruction forbids changing those files; their operative
   clause ("it is not yours to decide") stays true. Whether a run corrects
   them before the DATE/CONTENT group sits (it waits on CARRIES) is the
   coordinator's.
4. **Whether the user's answer, or any ratification, is in `LEDGER.md`** —
   closed to me.
5. **U-1 names the GATE juror file's path**, which carries measured
   figures. For the user that is a source, not a reading list; U-1 says
   figures exist and that looking first is the user's choice. A reviewer
   may prefer the path removed.
6. **`decisions/2026-10-01-jq-r04-date-content/`** appeared, untracked, in
   `git status` during this run. I did not open it. If it means the
   DATE/CONTENT group has been commissioned before JQ-R04-CARRIES is
   ratified, that would break the order the index and A-0.1 set; I cannot
   tell from a name.
7. **Three files of this run were already tracked by git** when I ran
   `git ls-files` (the criteria file and the two pre-run snapshots). I made
   no commit; some other process did. I did not look at any commit.
8. **The numbers check and the option-leak check are helpers**: the first
   compares token sets, the second the first 40 characters of 62 option and
   question sentences. Neither proves that no content could slip through;
   the index was also read line by line.

## 5 · Decisions I took that the instruction did not cover

1. **Numbering REVIEW-6's items** R6-1 … R6-18 (§1).
2. **The whole of d to the user**, rather than splitting option "no" off
   to jurors (§2 point 2), and **the reach put to the user with it**, not
   as a conditional juror question (§2 point 3).
3. **U-1's answer set**: A, B, C mirror d's three options; "Other" and
   "return it to jurors" added; part 2's narrow and wide reaches are the two
   readings REVIEW-6 §2.1 names.
4. **The four groups named without grounds** in U-1, and **no figure**,
   applying REVIEW-6 §2.2 and REVIEW-4's L1 to a user question.
5. **The d file kept unchanged** (no "withdrawn" banner added), so that
   nothing claimed earlier disappears; the index and HANDED-FORWARD carry
   the withdrawal. A commission is made from the index.
6. **HANDED-FORWARD amended** (A-0.1, A-0.4 step 1 and its check, C-5),
   because REVIEW-6 §2.1 names A-0.4 step 1's gap and A-0.1 named d.
7. **CARRIES status "being answered"** taken from the instruction, the only
   source I may read for it.
8. **USER-QUESTIONS.md is barred from jurors** (index and C-5), because it
   lists what the gate does with a kept field.

## 6 · How to reproduce

`PYTHONDONTWRITEBYTECODE=1 python3 -B scripts/34_seventh_fix_check.py --dry
--show` runs every check and writes nothing. **Run of record:
`97f03e98c28ed3ad`** — 100 checks, 100 ok, 0 failed; first recorded
2026-10-01T23:40:23Z, re-run at once with `PYTHONHASHSEED=7`: same run
number, same bytes, nothing new written. Its inputs are this script, every
file of the pre-run `exam-prep/` snapshot, only the pre-run bytes of the
three appended files (so the sections this run appended to `VERDICT.md`,
`HANDED-FORWARD.md` and `README.md` are not inputs and are not checked by
the script beyond their prefix; nor is this file), the index,
`USER-QUESTIONS.md`, the juror files, the audit, `RULES.md`, `TACTICS.md`
and the two verdicts.
