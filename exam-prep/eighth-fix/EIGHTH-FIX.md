# Eighth fix — acting on `exam-prep/REVIEW-7.md`, and on the REVIEW-6 items about JQ-R04-CONTENT-d left open

Mateo · data engineer · eighth-fix run · first clock read
2026-10-02T00:04:29Z, this file written after 2026-10-02T00:15:20Z (system
clock, RULES 23) · free disk 11,480,244,224 bytes at 00:04:29Z,
11,476,267,008 bytes at 00:15:20Z · nothing was downloaded.

**This file is a working file. It discusses what the answers of a juror
question do. It must not reach a juror or a referee** (HANDED-FORWARD
eighth-fix C-5; RULES 6).

Criteria, written after the pre-run snapshots and before any file outside
this folder was written: `exam-prep/eighth-fix/criteria-written-before-correcting.md`.

**Opened:** `RULES.md`, `TACTICS.md`, `TEAM.md`, root `README.md`; the four
ratified verdicts the instruction names (`decisions/2026-10-01-jq-r04-gate/`,
`-jq-n1-canteen-8/`, `-jq-r04-carries/`, `-jq-r04-date-content/`,
`verdict.md` only); `exam-prep/` — `REVIEW-7.md` and its criteria,
`REVIEW-6.md` and its criteria, the REVIEW-5 and REVIEW-4 criteria files,
REVIEW-5 lines 1–225, REVIEW-4 lines 38–160, REVIEW-3 lines 176–300,
REVIEW-2 lines 226–320, REVIEW lines 474–553 and a `grep`,
`SEVENTH-FIX.md`, `README.md`, `JUROR-QUESTIONS.md`, `USER-QUESTIONS.md`,
`VERDICT.md` lines 803–941 and its headings, `HANDED-FORWARD.md` lines
400–680 and its headings, the sixth-fix DATE, CONTENT and withdrawn
CONTENT-d juror files, `third-fix/juror-questions/JQ-R04-GATE.md` lines
1–161; `scripts/29_identity_audit_exact.py` lines 55–120, 217–470, 725–765
and a `grep`; `scripts/34_seventh_fix_check.py` whole. `git status` twice
(working tree only); `stat` (times only) on the four verdict files and two
`exam-prep/` files.
**Not opened:** `exam/`; any `scripts/exam_*` (not read, hashed or run;
three bytecode names appear in a listing of `scripts/__pycache__/`); in
`decisions/`, anything but the four `verdict.md` files (the juror files
beside them were not opened, listed by name only once at the start, and
not `stat`-ed); `instructions/`, `LEDGER.md`, `reports/`, `external/`,
`notes/`; `canteen/` (allowed; not needed — nothing this run wrote quotes
it or decides what it reads); `cards/`, `data/` (allowed; not needed); git
history; anything outside the Balıkçıl folder. One command's output was too
large and the harness saved it to a file outside this folder; I did not
open that file and re-ran the reads one file at a time. No memory or
session-log search. Every script run used `PYTHONDONTWRITEBYTECODE=1` and
`python3 -B`; `scripts/__pycache__/` held the same nine names before and
after; no cache under `exam-prep/eighth-fix/`.

---

## 1 · Items and their outcomes

REVIEW-7 does not number its requirements. I number them here, in order of
appearance. The REVIEW-6 items keep the numbers SEVENTH-FIX §1 gave them.

| item | where | outcome |
|---|---|---|
| R7-1 | REVIEW-7 §1: whose question — jurors | **Acted on.** The coordinator routes the row to jurors (instruction); JQ-R04-CONTENT-d is written again as a juror question, `exam-prep/eighth-fix/juror-questions/JQ-R04-CONTENT-d.md`, with "not a juror's" among its answers, so the scope line stays open to jurors and to the referee (RULES 35). |
| R7-2 | §1, "The user's part, which is not this row" | **Recorded; unchanged.** The later rule question (a kept field that fails the gate with no permitted printing that passes) stays the user's, as third-fix point 3 says; nothing this run wrote closes or opens it. |
| R7-3 | §1, last paragraph: a judgement against two earlier ones; a referee or the user may draw the line elsewhere | **Recorded.** Both routes stay reachable: the answer "not a juror's", the referee's scope check, and U-1 kept for return (HANDED-FORWARD eighth-fix A-0.1 item 3). |
| R7-4 | §2: U-1 not fit to be put to the user (faults in title, point 3 and the closing section, point 4, the rule section a–d, the "Wide" bullet, the empty set, the stops) | **Recorded, not corrected.** U-1 is marked superseded with its text kept; it is not to be put to the user now. HANDED-FORWARD eighth-fix A-0.1 item 3 requires every fault named in REVIEW-7 §2 to be corrected, and a review to find U-1 fit, before it is ever put to the user. Each fault was also used as a test of the new juror file (§2 below). |
| R7-5 | §2 blemishes (unexplained attack names; "nine columns printed as ranks"; TACTICS §3 cited as 55–62) | **Recorded** for U-1; in the new juror file both attacks and the ranked columns are explained, and TACTICS §3's list is cited as lines 55–64. |
| R7-6 | §3: A-0.1 must have the juror route as its main case | **Done**: HANDED-FORWARD eighth-fix A-0.1. |
| R7-7 | §3: A-0.4 step 1 not checkable — (1) the empty graded set; (2) a field kept by TACTICS 3 rather than by a ratified outcome cannot be traced as required; (3) its stops differ from those promised | **Done**: eighth-fix A-0.4 step 1 — step 1b (empty row), a header that traces each moved feature to its field and to the part of the ratified outcome that moves it, and stops 1c i–iv, which are the stops the juror file names, in its order (script 35 D and H). |
| R7-8 | §3: C-5 checkable | **Recorded**; replaced by eighth-fix C-5 (adds the new file, `REVIEW-7.md`, this folder and the A-0.9 record to what is never given). |
| R7-9 | §4: JQ-R04-CARRIES rows and the order section untrue | **Done**: ratified, naming `decisions/2026-10-01-jq-r04-carries/verdict.md`. |
| R7-10 | §4: DATE/CONTENT rows untrue | **Done**: ratified, naming `decisions/2026-10-01-jq-r04-date-content/verdict.md` (opened by this run: RATIFIED). |
| R7-11 | §4: JQ-N1 group, GATE, JQ-B1 true; d "withdrawn" true of the files | **Recorded**; the d row now names the new file and reads "written — not yet reviewed, not commissioned". |
| R7-12 | §4: the index carries no wording, option or number | **Kept**; script 35 I (no option or question sentence of nine juror files; no new number other than a run date and a HANDED-FORWARD item id; no answer label more often than before). |
| R7-13 | §5: reproduction | **Recorded.** |
| R7-14 | §6 items 1–6, what REVIEW-7 could not do | 1: **resolved** — the DATE/CONTENT verdict reads RATIFIED (file time 23:44:48Z). 2: **still not checkable** (the DATE/CONTENT juror files under `decisions/` are closed to me); the clause they read, that JQ-R04-CONTENT-d is answered "by other jurors", is true again under the juror route. 3: **not checkable** (`LEDGER.md` closed). 4: **recorded** (U-1 kept for return). 5: **same** — nothing measured on exam cards. 6: **recorded**. |
| R7-15 | §7, REVIEW-7's own decisions | **Recorded.** |
| R7-16 | §8, steer check: an untracked instruction named for exam moments; "if that run builds exam cards before A-0.1 is met, the order breaks" | **Referred to the coordinator**; I cannot see it. |
| R6-6 | REVIEW-6 §1: d not fit on (ii) and (vi) L2; scope contested | **Done, differently from the seventh run**: the row is a juror question again; (ii) §2 T-ii, (vi) §2 T-vi, scope §2 T-iv. The seventh run's withdrawal is superseded, not erased: its file, U-1 and its HANDED-FORWARD section stay. |
| R6-7 | §1 "Groups": R-04 cannot close without d (A-0.4 step 1) | **Done**: eighth-fix A-0.4 step 1 composes the row from d's ratified outcome. R-04 still waits on it. |
| R6-8 | §2.1: which ratified outcomes "keep" a field is not fixed | **Done**: the outcomes now exist and are quoted; each answer names its set from the code, the quoted outcomes and two records (A-0.7 for every printed column; new A-0.9) — §2 T-ii. |
| R6-9 | §2.2: the `p7-shape` ground (L2); names needed, grounds not | **Done**: the four groups are named without any ground; the inside list now also names the two previous-7-day figures that stay inside (script 35 D). |
| R6-10 | §3: scope contested | **Done**: "not a juror's" is an answer; the referee checks scope; refusal on scope or that answer sends the question to U-1. |
| R6-11 | §4: no contradiction with a ratified verdict | **Checked again against all four** (§3 below): none. |
| R6-15 | §6 extension 1: GATE file path removed from d | **Holds**: the new file quotes the GATE file without its path (script 35 D: no path into `exam-prep/`). |
| R6-17 | §8 item 2: how many features each reading moves — not measured | **Same**: not measured, on purpose. |

## 2 · JQ-R04-CONTENT-d, test by test

Tests as fixed in the criteria file §1 (the seven reviews' tests, and no
other). "Script 35" is run `5d0fd28862ba755b`.

| test | how the new file meets it | checked by |
|---|---|---|
| T-i answerable from its list | every term is explained or quoted: features, both attacks, the graded set, field, the frozen canteen book, ranked columns; the outcomes it needs are quoted | reading; script 35 D (reading list) |
| T-ii determinate | **no**: a fixed list (`FORCED_FAMILIES`). **only where**: the set is the printed columns with both CONTENT-a conditions on record — A-0.7 (now for every printed column) and A-0.9 (new); lines of the card have no ratified test, so they leave; nothing else is chosen. **yes**: every printed field leaves; the set is empty. **not a juror's**: A-0.1 item 3. Every remaining choice is a named stop with who decides (the coordinator), the same four in the file and in HANDED-FORWARD | reading; script 35 D, H |
| T-iii no lean | one-line ground for each answer, including "not a juror's"; a mechanical consequence for each; no "baseline", "moves nothing", "today's" or cost language attached to one answer; neutral title | reading; script 35 D (no recommending word) |
| T-iv scope | "not a juror's" is an answer and its consequence is stated; the referee's scope check is named (RULES 35) | reading |
| T-v true | 29 quotations, each in its cited lines and in the file; two cited ranges; every statement about the audit checked against its code (forced families; inside prefixes; one field per feature; nothing from the release line or announcements; the empty-set message) | script 35 D |
| T-vi L1 | no measured figure; no pass or fail on any material; the empty-set consequence is a mechanical description, stated for every answer alike | script 35 D (no decimal; numbers on a declared list) |
| T-vi L2 | no earlier run's, script's or person's choice on the point: no forced-family ground, no review, no withdrawal, no U-1; verdicts quoted only up to each answer, without splits or reasons | script 35 D (forbidden list) |
| T-vi L3 | no argument outside the options | reading |
| T-coup | the renderings it grades are ratified; its jurors sit on no other R-04 group (A-0.1 item 2, C-5) | reading |
| T-del | the passages taken out (forced-family grounds; the "what the other questions decide" section; the closing "say so" sentence) leave nothing pointing at them; the premises they supplied are supplied by the quoted outcomes and by the "not a juror's" answer | reading; script 35 D |
| T-list | this file, `RULES.md`, `TACTICS.md` | script 35 I, D |
| T-contra | §3 | reading |
| T-order | every outcome it needs is ratified; what it is handed from other groups is their outcome sentences, which show no option effect | reading |
| T-ptr | no path into `exam-prep/`; verdict paths are cited as sources only and are not on the reading list | script 35 D |
| T-self, T-comp, T-stop | as T-i; five answers including "Other" and "not a juror's"; the four stops identical in order with HANDED-FORWARD 1c | script 35 D, H |

From REVIEW-7's U-1 faults, read as tests: the title asks which features the
gate grades, not about a field that "must stay"; nothing in the file
becomes untrue when a ruling exists (it quotes the rulings); "yes" is
described by what it does to the set, not stated unconditionally beyond
what follows from its own text; the empty set has a stated outcome; the
stops agree.

**One mechanical statement that a reader may weigh**: under "yes" the set
holds no feature, and an empty set is a stop. This is what the answer does
(T-ii, F6 of REVIEW-7), and the same stop is stated for every answer.

## 3 · The four ratified verdicts — no contradiction

- **GATE** (line 72): quoted exactly; the file says it stands; every answer
  only composes the set the rule grades.
- **JQ-N1 / JQ-CANTEEN-8**: the file reads nothing about RULES 13, events
  or calm spacing.
- **JQ-R04-CARRIES**: used only through CONTENT-a's second condition, as
  that outcome says ("as JQ-R04-CARRIES defines one"); nothing redefines it.
- **DATE/CONTENT**: the file changes no field and no printing; it uses the
  outcome sentences as its premise. **A gap, named**: the verdict's "Effect
  on exam cards" (line 56) says the fields of the DATE parts "stay on the
  exam card"; the outcome sentences (lines 39, 42) say only that the date
  rule does not require their removal and that CONTENT-a's permission
  applies to "a TACTICS 3 field". The new file and A-0.9 apply CONTENT-a's
  conditions to every column, the bitcoin and ethereum columns included,
  which is what the outcome sentences say. A reader who takes line 56 as
  keeping those columns whatever CONTENT-a's conditions would read the
  "only where" answer differently for them. I name it and do not settle
  it (§6 item 4).

## 4 · U-1

Marked superseded by one delimited block under its heading; removing the
block gives the seventh-fix file byte for byte (script 35 U); a byte copy is
at `exam-prep/eighth-fix/USER-QUESTIONS-as-of-seventh-fix.md`. Not corrected:
REVIEW-7 §2's faults stand and are handed forward as conditions on any
return (A-0.1 item 3).

## 5 · Index

Re-issued; the seventh-fix version kept byte for byte at
`exam-prep/eighth-fix/JUROR-QUESTIONS-as-of-seventh-fix.md`. Every row's
status is true against the four verdicts and the files; every ratified row
names its verdict; the d row names the new file and reads "written — not
yet reviewed, not commissioned". New numbers: none, apart from the run date
(2026-10-02) and one pointer to the HANDED-FORWARD item A-0.1. Answer
labels: none added (the phrase "not a juror's" occurs as often as in the
seventh-fix version, in its pre-existing preamble and JQ-B1 row).

## 6 · What I could not do, by name

1. **Nothing measured on exam cards**; `exam/` is closed. No option effect
   was measured, on purpose.
2. **The new juror file is not reviewed.** Every earlier juror file that
   was ratified had first been ruled fit by a review; whether one precedes
   this commission is the coordinator's.
3. **Which columns the frozen canteen book reads** — not determined. I did
   not open `canteen/`; A-0.9 requires a record by a run permitted to read
   it. The exam-building run (Mode B) may not read the canteen, so it
   cannot apply CONTENT-a's first condition itself; no earlier
   handed-forward item said who does.
4. **The DATE/CONTENT "Effect" line 56 against the outcome sentences**
   (§3): not settled; a possible open question if a run must rely on it.
5. **Whether the DATE/CONTENT jurors were commissioned after the CARRIES
   ratification** — file times (CARRIES verdict 23:33:46Z; DATE/CONTENT
   verdict 23:44:48Z) are consistent with it, but the commission time is in
   `instructions/`, which is closed.
6. **`LEDGER.md`** — whether any of the four ratifications is recorded
   there.
7. **The instruction file named for exam moments** (REVIEW-7 §8) — not
   opened; whether exam cards are being built before A-0.1 is met, I
   cannot tell. My first `git status` (00:04Z) listed nothing modified or
   untracked, my second only this run's folder; the status supplied with
   my instruction had shown two modified files under `exam/acquisition/`.
8. **Script 35 does not check the sections this run appended to
   `VERDICT.md` and `README.md`**, nor this file; only their pre-run
   prefixes are inputs.

## 7 · Decisions I took that the instruction did not cover

1. **Numbering REVIEW-7's items** R7-1 … R7-16 (§1).
2. **Answer labels and texts.** The three answers of the sixth-fix version,
   reworded so that each is carried out from the quoted ratified outcomes;
   "not a juror's" added as the instruction requires; "Other" kept.
3. **"Only where" counts a field as one the card may be without only where
   both CONTENT-a conditions are established for it**, so that lines of
   the card (no ratified test) leave the set rather than stop the run. A
   stop that would fire every time is an open question in disguise; the
   jurors who ratify this answer ratify its text. They may answer "Other".
4. **A-0.9 added**, and A-0.7 extended to every printed column under "only
   where" — needed by the answer and by CONTENT-a itself.
5. **The empty set**: read from the fifth-fix step 4 ("passes only when …
   step 3 is graded") as "not graded — stop", and stated for every answer.
6. **Outcome sentences quoted, cut before splits and reasons**; verdict
   files cited but not on the reading list (the DATE/CONTENT verdict's
   reasoning quotes `TEAM.md` and juror arguments).
7. **U-1 marked by an inserted block** rather than an appended note, so the
   mark is seen before its text; byte copy kept and removal checked.
8. **"Not a juror's" ratified by jurors sends the question to the user**,
   like a refusal on scope. The instruction names only the referee's
   refusal; a ratified answer that no juror may decide it has no other
   place to go.
9. **I did not open `canteen/`**, though allowed.
10. **Script 35 strips run dates and HANDED-FORWARD item ids** before its
    index-number check (both new in the index; neither is a question's
    number), and **excludes dotfiles** from its script listing
    (`scripts/.gitkeep`, absent from my `ls`-made snapshot). Both were
    found as check failures on the first dry run and changed before the
    run of record; the change is in the script, not in what it checks.

## 8 · How to reproduce

`PYTHONDONTWRITEBYTECODE=1 python3 -B scripts/35_eighth_fix_check.py --dry
--show` runs every check and writes nothing. **Run of record:
`5d0fd28862ba755b`** — 160 checks, 160 ok, 0 failed; first recorded
2026-10-02T00:15:10Z, re-run at once with `PYTHONHASHSEED=7`: same run
number, nothing new written.
