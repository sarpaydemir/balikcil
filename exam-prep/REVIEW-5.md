# Review 5 — the fifth pre-exam run's juror files (`exam-prep/fifth-fix/`)

Mateo · data engineer, reviewing posture · first clock read
2026-10-01T22:43:49Z, this file written after 2026-10-01T22:47:21Z (system
clock, RULES 23) · free disk 12,389,568,512 bytes at 22:43:49Z,
12,389,167,104 bytes at 22:47:21Z · nothing was downloaded.

I did not do the work under review and was not told how it was done. I
review only what the fifth run changed or added. Criteria, fixed before any
check or probe of mine was run:
`exam-prep/review-5/criteria-written-before-ruling.md`. Probes and their
outputs side by side: `exam-prep/review-5/probes/`.

**This file names option effects and the instrument's grounds for its
forced families. It must not reach a juror or a referee** (HANDED-FORWARD
fifth-fix C-5; RULES 6).

**Opened:** `RULES.md`, `TACTICS.md`; `exam-prep/` — `REVIEW-4.md` and its
criteria file, REVIEW-2 lines 220–275, REVIEW-3 lines 160–250,
`JUROR-QUESTIONS.md`, the fifth-fix folder (FIFTH-FIX, criteria, the four
juror files, builder, fingerprints), the four fourth-fix juror files (by
`diff`; CONTENT lines 95–170 read), `VERDICT.md` lines 299–320 and 503–end,
`HANDED-FORWARD.md` headings and lines 400–end, `README.md` (appended part),
`third-fix/juror-questions/JQ-R04-GATE.md` lines 1–161, `R-04-blindness.md`
lines 175–200 and 285–320; `decisions/2026-10-01-jq-r04-gate/verdict.md`;
`scripts/29_identity_audit_exact.py` (lines 55–115, 217–345, 390–445,
720–745), `scripts/32_juror_file_check_fifth.py` (lines 1–80, 330–360, and
its file-access lines), `exam-prep/fifth-fix/make_fifth_fix_files.py`
(lines 1–40 and its file-access lines); `canteen/2026-09-19-sofia.md`
lines 112–120, 221–225, 229–234, 245–246, 251, 268–270, 667–671.
**Not opened:** `exam/`; the rest of `decisions/` (the names `juror-1.md`,
`juror-2.md`, `juror-3.md` appeared in a directory listing; not opened);
`instructions/`; `LEDGER.md`; `reports/`; `external/`; `notes/`; `cards/`,
`data/`, `TEAM.md`, root `README.md` (allowed, not needed); any
`scripts/exam_*` (not read, not run; three bytecode names appear in a
listing of `scripts/__pycache__/`); git history (`git status` only);
anything outside the Balıkçıl folder. No memory or session-log search.

---

## 1 · Rulings, row by row

Tests: REVIEW-2 (i)–(v) as REVIEW-3 §5 applied them; REVIEW-4's (vi) as its
criteria file fixes it (L1 / L2 / L3; fails only if it leans **and** is not
needed); the coupling test of REVIEW-4's criteria (REVIEW-3 §5's test for
GATE: no row in a coupled group can be answered by choosing by the combined
effect on whether material passes).

| row | ruling | why |
|---|---|---|
| JQ-N1-1 | **fit** | The shared part 4 boundary table is gone (L1 cleared). Nothing left points at it; the closing paragraph keeps only the top table's 289 / 58 (the premise). |
| JQ-N1-2 | **fit** | As N1-1. |
| JQ-N1-3 | **fit** | Only the shared closing paragraph changed (E-1); it is correct against the top table. |
| JQ-N1-4 | **fit** | Table and random-variation block gone; 4a's "that is the convention the calibration below used" gone (L2 cleared); block mechanism and immovable-event counts kept. 4b's "see the table above" now points at the top table, whose mixed-label column gives the 37–60 it cites. |
| JQ-CANTEEN-8 | **fit** | The script-comment quotation (L2) is gone; the premise of how the moments were drawn stays (lines 66–70 and 115–119). |
| JQ-R04-DATE-a | **fit** on its own text | The sentence REVIEW-4 named (L2) is gone. The new closing clause (points to CONTENT part d) is true and shows no effect: no coin-signature figure for the bitcoin/ethereum columns is in either file. Its group cannot be commissioned (§3). |
| JQ-R04-DATE-b | **fit** on its own text | Only the shared closing paragraph changed; as DATE-a. |
| JQ-R04-DATE-c | **fit** on its own text | As DATE-b. |
| JQ-R04-CONTENT-a | **not fit** | (ii), with (i): the gap of §2. The fifth version ties question a's condition to a measurement on exam cards (lines 135–137) and, with every figure removed, no longer says which features make "the column carries a measured coin signature" nor whether one attack beating is enough. A ratified "yes" or "no" cannot then be carried out without a further choice that changes the numbers (RULES 33). |
| JQ-R04-CONTENT-b | **not fit** | (vi) L1, through the new shared closing paragraph: lines 323–326 tell the group that a graded channel that stays fails the gate when either attack beats; part b's table shows every b1 figure beating both lines. Read together, the file shows what b1 does to whether material passes the gate. Question b and its options do not refer to the gate, and the sentence is not needed for b (it is needed only for d). The cause is d's place in the group (§3). The removal of b1's trailing clause is correct. |
| JQ-R04-CONTENT-c | **fit** on its own text | The pointer to part a's effect (L1) is gone. Part c shows no coin-signature figure, so the closing paragraph gives c's jurors no effect to read. Its group cannot be commissioned (§3). |
| JQ-R04-CONTENT-d | **not fit** | **Coupling:** a question on what the gate grades has been put to the jurors who choose the renderings it grades (§3). **(ii):** option "no" cannot be carried out as worded (§4). Passes: (v) — the three quotations match their lines (p5; also script 32's Q). The premise sentence (lines 288–290) is true of the audit's code (p3, independent of script 32). It shows no measured figure. (vii) — no contradiction with the verdict (§5). (iv) is contested and I do not rule on it (§4). |

**Groups.** JQ-N1-1 … -4 with JQ-CANTEEN-8: all five rows are fit, so the
group can be commissioned under RULES 33–35 (still subject to N-1's other
two conditions, REVIEW-4 §1). JQ-R04-DATE-a … -c with JQ-R04-CONTENT-a … -d:
**cannot be commissioned** while CONTENT-a, -b and -d are not fit.

## 2 · The gap REVIEW-4 named (§4 "Gap"), and why it must now be answered first

REVIEW-4 found the gap harmless *on today's material*: every CONTENT figure
beat on both attacks or on neither, and part a's figures fixed which
features were meant ("typical level of the ranked column", "how many values
repeat in the column"). The fifth run removed all part a figures and their
row labels (E-2, rightly; §6). It also wrote (lines 135–137): "Whether the
column carries a measured coin signature on exam cards is measured by the
audit before any exam card is used. Question a asks about the case where it
does." So:

1. The condition will be applied to **new material**, where the two attacks
   need not agree. The ratified gate reads "either"; the file says nothing.
2. The file no longer says **which features** count as the column's. The
   audit has a level family (`trades-level`, which also holds a feature
   read from the 7-day line), a repeat family (`repeat-trades`), and a
   pooled family (`shape-scale-free`) that mixes eight columns
   (`scripts/29_identity_audit_exact.py`, `FAMILIES`).

Neither is engineering: each changes which columns are left out, and so the
numbers (RULES 33). **It must be answered before the DATE/CONTENT group can
be: JQ-R04-CONTENT-a is not fit until it is.** No other row turns on it:
part b's question and options are unconditional, and part d's options do not
use "carries". How it is answered (a sub-part put to the same jurors, or
something else) is the coordinator's choice. I do not choose.

## 3 · The coupling: part d in the DATE/CONTENT group

REVIEW-3 §5 ruled that JQ-R04-GATE should stay alone: "Jurors who choose the
gate statistic should not also choose the renderings it will grade. Coupling
them would let one set of jurors pick definitions by their combined
effect." REVIEW-4's criteria took this as the coupling test. Part d decides
what the gate grades. It sits in the group that decides which fields and
renderings stay (DATE a–c, CONTENT a–c). The group's files now show both
halves:

- part b: every price rendering tried carries a signature that beats both
  lines ("No fixed number of decimals tried removes the signature");
- lines 323–326 (and part d's options): a channel that stays and is graded
  fails the gate if either attack beats; one that is not graded is named
  only.

So one set of jurors can choose b and d by their combined effect on whether
exam material passes. That fails the coupling test. The same structure
holds without any figure for part a: "no" to a together with "no" to d
fails the gate whenever a's case arises, if "carries" means what the gate
means (§2).

FIFTH-FIX §3 and the fifth-fix VERDICT ("A steer in the instruction I was
given") say the fifth run's instruction told it to write the question "in
the group it bears on". That instruction and REVIEW-3 §5 cannot both be
followed for this question. **The coordinator must choose.** I name the
conflict and do not resolve it. If part d moves out of the group, the
closing paragraph that CONTENT-b's jurors read still has to stop showing the
gate consequence (§1, CONTENT-b).

## 4 · Part d's options

**(ii) — option "no" is not determinate.** It reads: "only what a frozen
canteen rule or TACTICS requires by its own words leaves the row; a field
that stays because of a juror reading stays in the row". The audit's forced
list already contains `p7-shape`, and the instrument gives one ground for
it: "TACTICS 3 puts a previous-7-day summary on the card"
(`scripts/29_identity_audit_exact.py` line 433; p3 prints it). That is the
same ground that option "no" of DATE-a and of CONTENT-a gives for keeping a
column: "TACTICS 3 says what is on the card". So suppose a column is kept by
a ratified "no" to a. Under d's "no", it is at once "required by TACTICS by
its own words" (as `p7-shape` is held to be) and "a field that stays because
of a juror reading". The run that builds the row cannot apply the option
without a further choice. The file also does not tell jurors which families
are outside the row or why. That fact is the premise option "no" needs.
Telling them would be a precedent, but it would be a needed one.

**(iv) — contested, not ruled.** Options "yes" and "only where no permitted
rendering leaves it out" would, once ratified, leave a measured coin channel
on exam cards ungraded when it stays. The third-fix VERDICT (lines 311–313)
says whether such a channel is acceptable under RULES 9 is "a question about
a rule, which is the user's". FIFTH-FIX §3 answers that the GATE file's own
definition is being read, not RULES 9. Part d tells jurors to say so if they
think otherwise (lines 311–314). Whether that is enough is the referee's
scope check (RULES 35) or the user's. Since d is not fit on the two grounds
above, my ruling does not turn on this.

## 5 · Contradiction with the ratified JQ-R04-GATE verdict

**None in any row to be commissioned.** Part d quotes the verdict's line 72
exactly and says it does not reopen it. The closing paragraphs of CONTENT and
DATE state the gate as "either attack beats its line on the row", which
matches the verdict. The verdict says nothing about how the row is made up,
and part d's options change only that. This is a gap, not a contradiction,
under the criteria. One gap is outside the rows: in HANDED-FORWARD
fifth-fix A-0.4 step 3, when the two nearest-neighbour versions disagree and
pair AUC has not failed the gate, the gate is "not graded" and the
coordinator is told. The verdict does not say which nearest-neighbour
version is "the attack". The step stops; it does not contradict.

## 6 · The fifth run's stated disagreements with REVIEW-4 (fifth-fix VERDICT)

1. **The part 4 table goes to nobody, not to the referee — holds.**
   REVIEW-4 itself says both "can go to the referee" (§2) and "none may
   reach a juror or referee" (§7 item 6). None of the referee's six checks
   (RULES 35) needs an option's effect. The stricter reading loses nothing.
2. **Part a's rows 1–2 removed as well — holds.** Keeping them would show
   only the rendering where the signature exists, which REVIEW-3 §5 (iii)
   ruled not fit. REVIEW-4 also asked that the premise be stated "without
   saying which rendering meets it". **But** the removal also took away the
   only statement of which features the condition is about. Together with
   lines 135–137, that makes REVIEW-4's gap operative (§2). The disagreement
   holds; its consequence was not followed through.
3. **DATE's closing paragraph has CONTENT's defect — holds.** `btc-eth` and
   `repeat-btceth` are inside `ALL-removable` (p3), so under the ratified
   gate a "no" to DATE a would leave them graded unless d says otherwise.
   Pointing to d is right. That d itself is not fit is §3–§4.

## 7 · The index's reading lists

- **No list names a review, `VERDICT.md`, `HANDED-FORWARD.md` or a working
  file.** Script 32's `I list` checks and my reading agree. Every list
  names only the group's current juror files, `RULES.md`, `TACTICS.md`, and
  for DATE/CONTENT, five canteen ranges. JQ-R04-GATE is shown as ratified.
- **Nothing beyond need, with one judgement.** The ranges give the frozen
  rules S-1, B-2, B-3, B-4 and §4 item 4, which parts a and b quote. Range
  112–120 also carries two and a half lines of S-1's own trigger text that
  the file does not quote: "a percentage change is unchanged by TACTICS 6's
  rebasing of price to a number starting from 100, so the trigger is
  computable on a card whose price is hidden". These lines are part of a
  frozen rule that jurors may need to cite whole (RULES 34), and they can
  be read toward b1 and toward b3 alike. I do not rule them a lean. I name
  them.
- **Cited, not listed (not a "beyond" issue; noted).** CONTENT part a cites
  canteen lines 229–234 and 251 as evidence (they hold watcher citations
  with card numbers). CANTEEN-8 cites lines 203–204, 918–933, 920–922 and
  926. No list gives them. The fifth run's own criteria §3 says lists give
  the canteen "by the line ranges its juror files cite". Script 32 checked
  the lists only against CONTENT's "What you open". Each file quotes what
  its question needs, so (i) is not failed.
- **Pointers inside listed files (noted, unchanged text, not ruled).** The
  CONTENT header (lines 17–20) and DATE header (lines 16–18) name
  `exam-prep/REVIEW.md` / `REVIEW-3.md`. CONTENT line 183 names a review-3
  probe output. C-5 forbids handing these over. A juror who followed a
  pointer would leave the list. FIFTH-FIX §2 records this as not edited.

## 8 · Reproduction (outputs in `exam-prep/review-5/`)

| what | result |
|---|---|
| builder `make_fifth_fix_files.py --out exam-prep/review-5/rebuild` (p1) | exit 0; all four files byte-identical to the issued ones (`cmp`) |
| `scripts/32_juror_file_check_fifth.py --dry` (p2) | **same run number `6a8b8a6dc1c92be7`**, 77 checks; 76 ok, 1 FAIL: `U new files`. The failure is my own `exam-prep/review-5/` files, which did not exist at the fifth run. `U unchanged` passes: no file in the fifth run's snapshot has changed since. Nothing written (`--dry`). |
| `exam-prep/fifth-fix/FINGERPRINTS.md` (p4) | 16 of 16 SHA-256 match (`sha256sum -c`) |
| part d premise (p3) | true: every feature computed from BTC/ETH, `trades`, `close` and the other eight ranked columns falls in a family outside `FORCED_FAMILIES`; audit SHA-256 `cfc4bdcb…d03f` (same as REVIEW-4's) |
| part d quotations (p5) | GATE lines 55–57 and 64–66, verdict line 72: each found in its lines and in part d |

`scripts/__pycache__/` held the same nine names before and after. Every
run used `PYTHONDONTWRITEBYTECODE=1` and `python3 -B`; probe p3 parses the
audit with `ast` and does not import it.

## 9 · What I could not do, by name

1. **Nothing measured on exam cards**; `exam/` is closed.
2. **How many features the gate would lose under each option of d** — not
   measured, on purpose. It would be an option effect, and no ruling here
   needs it.
3. **Whether the two attacks disagree on any trade-count family on exam
   material** (§2) — under `exam/`.
4. **The fifth run's instruction** (where it says to put d "in the group it
   bears on") — under `instructions/`, closed. I rely on FIFTH-FIX §3's
   account of it.
5. **R4-9 ("earlier verdicts" of the GATE jurors)** — still not visible to
   me; the jurors' answers and `LEDGER.md` are closed.
6. **p5's citation scan is a regex.** It missed "and 251" in "lines 229–234
   and 251", which I read by eye. Its list of canteen citations is a helper,
   not proof that nothing was missed.
7. **"Leans" and "determinate" are judgements.** I fixed my criteria before
   checking. Another reviewer could draw the line elsewhere, most plausibly
   on CONTENT-b (L1 through a shared sentence) and on d's option "no".

## 10 · Decisions I took that the instruction did not cover

1. **The coupling test applied to a new row** (d) and its group, as
   REVIEW-4's criteria state it. I did not apply it only to existing
   couplings.
2. **CONTENT-b ruled not fit** because of a shared sentence whose own part
   (d) needs it. I followed REVIEW-4's rule that a shared item that leans and
   is not needed for a row fails that row.
3. **DATE-a/-b/-c and CONTENT-c ruled "fit on own text"**, separately from
   whether their group can be commissioned.
4. **Read `VERDICT.md` lines 299–320** (third-fix section) to check the
   source FIFTH-FIX §3 cites. That section carries result-before-rule
   information. I am not a juror; I quote only its point 3.
5. **Script 32 run only with `--dry`**, so that nothing was written into
   the fifth run's folder; its run number is the same either way.

## 11 · Steer check

My instruction gives no result. Named, mildly: item 3's "If it must, say
which row is not fit until it is" frames the answer as possibly a row
failure. It is conditional and does not predict. "Jurors cannot run
anything, so a fault in a juror file can only be caught here" puts weight
on finding faults. It is a reason for the model choice, not a result. The
git status supplied at start had only commit subjects of the forms "work:"
and "ledger:" and an untracked instruction file name, with no result.

## 12 · Fingerprints

`exam-prep/review-5/FINGERPRINTS.md`. This file's own SHA-256 is in my
report to the coordinator. I wrote only this file and `exam-prep/review-5/`.
