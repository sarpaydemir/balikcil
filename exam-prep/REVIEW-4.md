# Review 4 — the fourth pre-exam fix (`exam-prep/fourth-fix/`)

Mateo · data engineer, reviewing posture · first clock read
2026-10-01T21:56:13Z, this file written after 2026-10-01T22:15:45Z (system
clock, RULES 23) · free disk 12,396,265,472 bytes at 21:56:13Z,
12,394,434,560 bytes at 22:15:45Z · nothing was downloaded.

I did not do the work under review and was not told how it was done. Every
number below is either re-run with the fourth run's own scripts into
`exam-prep/review-4/rerun/`, or recomputed by a probe of my own in
`exam-prep/review-4/probes/` (code and output side by side). The criteria I
rule by were written before I checked any figure:
`exam-prep/review-4/criteria-written-before-ruling.md`.

**This file states measured effects of options on coin signatures and on
chance lines. It must not reach a juror or a referee of any row below**
(RULES 6; the same reason REVIEW-3 §10 (a) gave).

**Opened:** `exam-prep/` (README, index, REVIEW-3, the fourth-fix folder,
the fourth-fix sections of `VERDICT.md` and `HANDED-FORWARD.md`, the
third-fix GATE file, REVIEW-3's probe list, `R-04-blindness.md` lines
170–200, the k1 blinding manifest lines 60–75, card sets and truth files by
script); `scripts/` (15, 29, 30, 31 read in the parts named below; 06 lines
60–66, 130–200); `cards/` (by script; headers of C010, C011, C175; C175's
before table); `canteen/2026-09-19-sofia.md` (lines 112–120, 180–215,
221–270, 577–585, 667–671, 877–945, and its heading list);
`decisions/2026-10-01-jq-r04-gate/verdict.md`; `RULES.md`, `TACTICS.md`.
`git status` was run once (working tree only).
**Not opened:** `exam/`; the rest of `decisions/`; `instructions/`;
`LEDGER.md`; `reports/`; `external/`; `notes/`; `TEAM.md` and the root
`README.md` (allowed, not needed); any `scripts/exam_*` (not read, not run;
three of their names appear in a directory listing of `scripts/__pycache__/`
that I printed); git history (no `git log`, `git show`, `git diff`);
anything outside the Balıkçıl folder. No memory or session-log search.

---

## 1 · Rulings

| problem | ruling |
|---|---|
| **R-04 · is the exam blind?** | **Not solved.** The gate row (`ALL-removable`) beats both of its lines on all six blinded versions of the observation cards (re-run, §3; p6). Under the ratified JQ-R04-GATE outcome (the gate fails if either attack beats its own line) the gate therefore fails on every material measured. Six of the seven rulings HANDED-FORWARD A-0.1 requires are outstanding, and none of their rows can be commissioned as the files stand (§2). |
| **N-1 · collapse before counting** | **Solved only under three conditions.** The engine reproduces; REVIEW-3's conditions on the engine are met — the key check no longer trusts the object it checks (H-1 reproduced) and "keep the latest" is the wording, applied over every clock hour (H-2 reproduced, and a third literal implementation of mine agrees, p3). Conditions: **(1)** the JQ-N1 file and JQ-CANTEEN-8 are corrected where §2 says, and the group is then commissioned and ratified under RULES 33–35; **(2)** the judge's script meets HANDED-FORWARD B-1 … B-5, including B-3's separate recomputation of `event_map_sha256` from the sealed key, repeated by the review of the judge's run; **(3)** B-1's check also confirms, on the sealed key, that no coin has two moments at one start hour, or that card ids are of fixed width — the engine breaks that tie by the id as a string, not by card number (§6.3). |

---

## 2 · The juror rows (the reviews' standard plus test (vi))

Standard: REVIEW-2's tests (i)–(v) as REVIEW-3 applied them, and test (vi),
the one this review's instruction adds. How I apply (vi) is fixed in the
criteria file: an item fails when it **leans** — L1 shows what choosing an
option does to an outcome the laboratory acts on (whether material passes, a
coin signature, how strict a chance line is) where the question and its
options do not refer to that outcome; L2 reports an earlier choice on the
open point itself; L3 argues one option outside the options list — **and**
it is **not needed** to answer. The laboratory's own precedent for L1 is the
GATE file, lines 154–157 ("so that the choice is made on the wording and
not on its result (RULES 6)").

| row | ruling | why |
|---|---|---|
| JQ-N1-1 | **not fit** | (vi) L1: the part 4 table (`JQ-N1.md` lines 224–240) gives the 1% boundary under each reading of part 1 (start-hour rows against move-window and card-span rows), i.e. how strict each reading makes the chance line. Part 1 asks for a reading of "the same hour"; the table is not needed for it. (i)–(v) pass; the top table reproduces (rerun collapse = runs `756cf4ea…`, `bec532fa…`). |
| JQ-N1-2 | **not fit** | (vi) L1: the same table gives component against greedy-clique boundaries. Part 2's own correction passes (i)–(v): both conventions are stated in parallel; 168/168 with 4, and 125/124 with 21, and both "latest" table rows reproduce (rerun of 30 H-2) and agree with my own literal implementation (p3); G-5's figures and the inviting sentence are gone. |
| JQ-N1-3 | **fit** | Every row of the part 4 table is scope `any`, so it does not bear on part 3's options. Counts reproduce. Its group cannot be commissioned until N1-1, -2, -4 and CANTEEN-8 are fixed. |
| JQ-N1-4 | **not fit** | (vi) L1: the part 4 table and the "how large random variation alone is" block (lines 224–259) put the block and representative boundaries side by side for each configuration; part 4 asks which way events are used, and can be answered without them. L2: part 4a's "that is the convention the calibration below used" (lines 217–219) is an earlier choice on 4a itself. The block mechanism and its immovable-event counts (lines 206–213) are a description of what the option does and pass; "latest" counts (1 event, 5 cards; 0) reproduce (p3). |
| JQ-CANTEEN-8 | **not fit** | (vi) L2: lines 61–63 quote the drawing script's own reading of the open point ("TACTICS 2 puts no minimum distance between two *calm* moments. None is imposed here.", `scripts/06_find_moments.py` lines 63–65), listed among the rule texts, in nearly the words of option "yes". Not needed: the chair's quote (lines 57–60) states the premise, and lines 114–118 say how the observation moments were drawn. Everything else passes: the two written definitions of "overlap" are each grounded in a written usage; counts, 14 / 10 / 34 h and line citations verified (C010 and C011 start 2026-07-16 00:00 and 14:00). |
| JQ-R04-DATE-a | **not fit** | (vi) L2: lines 77–78, "The first run removed these columns from its blinded cards and said it was acting on a reading it could not settle alone." It reports an earlier choice in the direction of "yes" and is not needed. The 243 / 495 and 0 / 46,170 figures are the question's premise and pass (REVIEW-3). |
| JQ-R04-DATE-b | **fit** | The description of the release line (names and offsets kept) is what the card prints, needed for the question; the 13 names, 100 / 30 / 13 / 18 and the caveat pass. |
| JQ-R04-DATE-c | **fit** | 99 passes; the offset is what the card prints. |
| JQ-R04-CONTENT-a | **not fit** | (vi) L1 for part c, carried by part a: table rows 3–4 (lines 131–132), the second half of lines 134–136 and lines 159–162 show that ranking from the values before rounding leaves the trade-count column with no coin signature either attack finds, so that part a does not arise for that column. Part a is conditional ("when … it carries a measured coin signature") and can be answered without them; REVIEW-3 §5 allowed stating the premise without figures. (v) passes: every figure is the exact audit's (rerun byte-identical; tie-free verdicts exact, p1; pair AUC exact, p9). Also the shared defect below. |
| JQ-R04-CONTENT-b | **not fit, only because of the shared defect below** | Its own text passes (i)–(vi): the price-column figures are the premise of option b1 ("its measured signature"); 36 / 0 and all eight figures reproduce (rerun, p1, p9); the near-line note is right (7 of 1,000 shuffles at or above 0.1408, p1). |
| JQ-R04-CONTENT-c | **not fit** | (vi) L1: lines 254–255 ("What the second way does to the trade-count column's measured coin signature is in part a") send the juror to the effect of option "yes" on a coin signature; neither the question nor its options refer to a signature. The H-4 table is the premise (the finer order exists) and reproduces independently from the raw and blinded cards (p2: every cell, 306 of 306); the guard paragraph (lines 231–236) describes what the rendering does and passes. Also the shared defect below. |

**Shared defect of the three CONTENT rows (§4).** The closing paragraph
(`JQ-R04-CONTENT.md` lines 276–279, "if no permitted rendering removes a
channel, the channel is named in the exam manifest with its number") and
option b1's "with its measured signature named in the exam manifest" (lines
207–208) tell the jurors that a channel which must stay is named and the
exam proceeds. Under the ratified GATE outcome, with `ALL-removable` as the
audit defines it, such a channel stays in the graded row. Which of the two
holds is not written anywhere (§4).

### What must change before the groups can be commissioned

- **JQ-N1:** take the part 4 boundary table and the random-variation block
  out of the juror file (they can go to the referee), with 4a's reference to
  the calibration's choice; keep the block mechanism and its counts.
- **JQ-CANTEEN-8:** remove the quotation of the drawing script's reading
  (lines 61–63), or reduce it to the fact already in lines 114–118.
- **JQ-R04-DATE-a:** remove lines 77–78.
- **JQ-R04-CONTENT-a / -c:** remove part a's rows for the values before
  rounding, the sentence that reports their effect, the paragraph at lines
  159–162 and part c's pointer at lines 254–255; state part a's premise
  without saying which rendering meets it.
- **JQ-R04-CONTENT (all parts):** the shared defect, after the coordinator
  settles the link in §4.

No passage needs a new number. Each fix is a deletion, apart from the
consequence sentences, whose wording depends on §4.

## 3 · The couplings

- **JQ-N1-1…4 with JQ-CANTEEN-8 — stand.** Same span arithmetic; part a of
  CANTEEN-8 changes how many same-coin overlaps part 3 governs.
- **JQ-R04-DATE-a…c with JQ-R04-CONTENT-a…c — stand.** All six read RULES 9
  against TACTICS 3 and 6; part c (the rank source) belongs here, as
  REVIEW-3 said. Parts a and c genuinely bear on each other (a's condition
  depends on c's rendering), so they should stay together; the coupling is
  also the route by which part a's figures reach part c, which is why those
  figures must go (§2), not the coupling.
- **JQ-R04-GATE alone — stood, and is now ratified.** Its outcome now bears
  on the CONTENT group through the composition of `ALL-removable` (§4). That
  is not a coupling of jurors; it is a link the coordinator must settle
  before the CONTENT group is commissioned.

## 4 · The ratified JQ-R04-GATE verdict against the files still to be commissioned

**One contradiction, conditional, on RULES 9.** The verdict (§ "Ratification")
makes the exam cards fail when either attack beats its own RULES 12 line on
`ALL-removable`. The GATE file (§ "What `ALL-removable` is", lines 59–67)
defines that row as every audited feature minus the families "that must stay
on the card because a frozen canteen rule or TACTICS requires them"; the
audit codes that list once (`scripts/29_identity_audit_exact.py`,
`FORCED_FAMILIES`, lines 429–436: `volatility-frozen`, `funding-line`,
`p7-shape`, `repeat-chg`). `JQ-R04-CONTENT.md` § "Part b" (option b1) and
§ "What follows from the answers — not to steer" read RULES 9 as satisfied
when a channel that must stay is named in the exam manifest. They agree only
if a field that a ratified CONTENT outcome keeps on the card leaves
`ALL-removable` (becomes "required"); if the coded list stands, a ratified
b1 (or a "no" to part a) keeps a measured signature inside the graded row,
and on the observation cards those families beat their lines (§2). No file
says which; HANDED-FORWARD A-0.4 grades the row as coded. The GATE file
(lines 26–28) calls the feature list engineering; whether a juror ruling
moves a family out of the row is not engineering of the list but a link
between two rulings, and I do not settle it.

**Not contradictions, named so they are not lost:**

- **Gap.** `JQ-R04-CONTENT.md` § "How 'carries a coin signature' is
  measured" does not say whether one attack beating its line is enough for
  "carries a measured coin signature"; the verdict reads the gate as
  "either". Today every CONTENT figure beats on both attacks or on neither,
  so nothing turns on it on this material; part a's answer is said to govern
  later material (lines 159–162, which §2 removes in any case).
- **RULES 12, "equal does not beat".** CONTENT's convention (lines 105–106)
  agrees with RULES 12: with the line taken as the 10th largest of 1,000
  shuffles, a value equal to it has at least 10 shuffles at or above it. The
  one equal cell (`trades-level`, values before rounding, 0.125607 against
  0.125607) has 117 shuffles at or above it (p1).
- **RULES 13.** The verdict records no answer to the GATE file's optional
  second part, so there is no GATE reading of RULES 13 for JQ-N1 to
  contradict; the referee check REVIEW-3 suggested has nothing to compare.
- **Outside the juror files:** `HANDED-FORWARD.md`, fourth-fix section,
  A-0.4 says that when the two nearest-neighbour versions disagree "the gate
  is **not** graded". Under the ratified outcome a gate whose pair AUC beats
  its line has failed whatever the nearest neighbour does. A-0.4 must be
  restated against the ratified outcome. It also still says "the statistic
  JQ-R04-GATE ratifies" as if pending.

## 5 · What I re-ran (outputs in `exam-prep/review-4/rerun/`)

Command file `exam-prep/review-4/rerun.sh`, log `exam-prep/review-4/rerun.log`
(21:57:10Z → 22:12:33Z). Scripts 30 and 31 were imported with `OUT_DIR`
pointed at `rerun/checks/`. Comparison: p5.

| run | script | result |
|---|---|---|
| `a0ecf6970d86b199` | `15_event_collapse.py` (`002bb406…e4f6`) | same run number; three CSVs byte-identical, and identical to runs `756cf4ea156d92c3` and `bec532fa008e0e01` |
| `721b2448f1722ccf` | the intermediate engine `a2e16ff0…` | **not reproducible**: that version no longer exists and git history is closed to me; its three CSVs equal `a0ecf6970d86b199`'s (cmp) |
| `9777f422fd2d2b41` `9ff0ffec3fe21ebe` `989b8f21b23e0310` `446adf64f8e8235c` `45d062efe77c9251` `762815a877c19551` `d6557e91f9f97f7b` | `29_identity_audit_exact.py` (`cfc4bdcb…d03f`) | same run numbers; all 14 CSVs byte-identical; reports and records differ only in clock, disk and output-path lines |
| `516027c6c9f215d6` | `30_fourth_fix_checks.py` | same run number; record byte-identical; report differs only in its clock line |
| `4b4d4795eb488c94` | `31_juror_file_check_fourth.py` | **same run number only in place**: the script hashes the path of script 30's record, so a run with `OUT_DIR` moved gets another number (mine: `94890bb9bf623a10`, 59 checks, 0 failed). p7 ran the script's own source in place with every write refused: run number `4b4d4795eb488c94`, and the script's own append-only check found the recomputed record equal to the stored one ("already recorded", exit 0). Nothing was written. |

Also: all 80 rows of `exam-prep/fourth-fix/FINGERPRINTS.md` match, before
and after my work; the six appended files start with exactly the bytes
REVIEW-3 fingerprinted; no file under `exam-prep/` or `scripts/` changed
after the fourth run's first clock read other than its own fingerprint file
(p0). The gate rows of the float audit (script 16, the runs the GATE file
cites) and of the exact audit are identical in every column on all five
GATE sets (p6). `make_jq_n1.py`, run with its output redirected, gives the
issued JQ-N1 except the three placeholders **and one sentence added by hand
that FOURTH-FIX §8 item 14 does not mention** (part 4, the "latest" immovable
counts; the sentence is correct, p3) (p4).

## 6 · Findings of my own probes

1. **The tie-free verdicts are exact (p1).** Script 29 compares distances
   exactly but sums the tie-free score in floating point and compares
   `obs > line` in floating point. Recomputed as fractions for the observed
   labels and all 1,000 shuffles, every verdict in the juror files is the
   same.
2. **Pair AUC is exact (p9)**: an independent exact Mann–Whitney computation
   gives all eight pair-AUC figures the CONTENT file shows, at 6 decimals.
   The AUC chance lines were reproduced by re-run only.
3. **Card-number tie-break.** Both conventions break a same-coin, same-hour
   tie by the card id as a string (`_greedy_literal()` sorts on `(hour, id)`;
   the default path on `(start_dt, id)`). JQ-N1 says "card number". With
   ids of one width (C001 … C306) these agree; it never arises on the
   observation cards (H-5: 0). Whether exam ids are of one width is under
   `exam/`.
4. **No time-zone dependence (p8):** the engine gives the same four event
   maps under four machine time zones (UTC, and three with offsets that are
   not whole hours: Pacific/Chatham, America/St_Johns, Asia/Kathmandu).

## 7 · What the coordinator must act on

1. Have the files corrected as §2 lists; the groups are not commissionable
   until then.
2. Settle, and record, whether a field that a ratified CONTENT outcome keeps
   on the card leaves `ALL-removable` (§4); then make CONTENT's consequence
   sentences true under that answer. Whether this is engineering or an open
   question is yours to record; by RULES 33 it is a choice that changes the
   numbers.
3. Have HANDED-FORWARD A-0.4 restated against the ratified outcome (§4).
4. `exam-prep/JUROR-QUESTIONS.md` still shows JQ-R04-GATE as "being
   answered"; and its DATE/CONTENT rows hand jurors the whole canteen book,
   while the CONTENT file cites five line ranges and the DATE file none.
   The whole book includes § 7 item 1, which reads TACTICS 6 against RULES 9
   in the chair's own words; giving only the cited lines avoids that.
5. The verdict (§ 3) says every GATE juror's grounding includes "earlier
   verdicts". Whether that means `exam-prep/VERDICT.md` — whose third-fix
   section carries the result-before-rule information REVIEW-3 §10 (a) said
   must not reach a GATE juror — is not visible to me. Check it.
6. This file, and the fourth-fix VERDICT/FOURTH-FIX sections, carry option
   effects; none may reach a juror or referee.

## 8 · What I could not do, by name

1. **Nothing measured on exam cards**; `exam/` is closed.
2. **Run `721b2448f1722ccf` re-run** — its engine version is gone (§5).
3. **Script 31 under its number by an ordinary re-run** — not possible by
   construction; done in place under a write guard (§5).
4. **The GATE jurors' answers** — not opened (only the verdict is
   permitted): what "earlier verdicts" are, and how they read RULES 9 and 13,
   is not visible.
5. **Whether any juror file was commissioned already** — `LEDGER.md` is
   closed.
6. **AUC chance lines, DATE figures, CANTEEN-8 counts** — reproduced by
   re-run or taken from REVIEW-3, not recomputed independently by me.
7. **"Leans" is a judgement.** I fixed how I apply it before checking any
   figure; another reviewer could draw the line elsewhere, most plausibly on
   CANTEEN-8's quotation and DATE-a's sentence.
8. **Whether exam card ids are of one width** (§6.3) — under `exam/`.

## 9 · Decisions I took that the instruction did not cover

1. **How to apply test (vi)** — the criteria file (L1–L3, "needed").
2. **Test (vi) applied to unchanged rows** (DATE-a…c), because item 1 of my
   instruction covers every row "to be commissioned"; its last paragraph
   ("need not re-review what REVIEW-3 already ruled on") I read as covering
   (i)–(v) only.
3. **The CONTENT consequence sentences ruled a shared defect** of all three
   CONTENT rows, which is the only reason CONTENT-b is not fit.
4. **The GATE row itself was not ruled**: it is ratified, not "to be
   commissioned".
5. **Script 31 run in place under a write guard** (p7), so that the stated
   run number could be tested without writing into another run's folder.
6. **p3 scans window edges, not every clock hour**: coverage only rises at a
   window's first hour, so the earliest hour of largest coverage is always
   one; the comment in p3 says so. Its moment kinds come from the engine's
   `events.csv` (kind is not on a card); coin and start hour are read from
   the card headers and cross-checked.
7. **A bytecode file was written by my probe p1** into `scripts/__pycache__/`
   (`29_identity_audit_exact.cpython-314.pyc`, SHA-256 `7b7a7c4e…3f73`, at
   21:58:08Z; p0 had shown no such file before). That is outside the folder
   I may write to. I deleted it at 22:15Z, restoring the folder; the other
   probes and the re-run were run with `PYTHONDONTWRITEBYTECODE=1` or wrote
   nothing there.
8. **`pkill -f` was used once** to stop my first, too slow, version of p3;
   its output file was then rewritten by the completed run.

## 10 · Steer check

My instruction gives no result, prediction or verdict. Named, mildly:
"two juries are commissioned on your ruling" presumes the juries follow
this ruling, and puts weight on a quick "fit". Test (vi) is introduced after
the fourth run finished, so rows can fail a test their author was not
given; that is a fact about the rulings above, not a defect of the run.
The git status supplied at start carried only commit subjects of the forms
"work:", "ledger:" and "auto:", and an untracked instruction file name; no
result.

## 11 · How to reproduce

- `bash exam-prep/review-4/rerun.sh` (append-only by run number).
- `python3 exam-prep/review-4/probes/<name>.py`, outputs in the `.out` files
  beside them: p0 fingerprints, p1 exact tie-free nulls, p2 rank-source
  counts, p3 literal greedy-clique, p4 (`make_jq_n1` redirected; diff),
  p5 re-run comparison, p6 gate rows, p7 script 31 in place, p8 time zones,
  p9 exact pair AUC. Run with `PYTHONDONTWRITEBYTECODE=1`.
- Constants: `SHUFFLES`, `TOP_FRACTION`, `SEED` imported from the
  instruments. No threshold was introduced.

## 12 · Fingerprints

`exam-prep/review-4/FINGERPRINTS.md`. This file's own SHA-256 is in my
report to the coordinator. I wrote this file and `exam-prep/review-4/`, and
edited nothing else (the deleted cache file in §9 item 7 was my own).
