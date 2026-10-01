# Fifth fix — acting on `exam-prep/REVIEW-4.md`

Mateo · data engineer · fifth-fix run · first clock read 2026-10-01T22:25:48Z,
this file written after 2026-10-01T22:34:36Z (system clock, RULES 23) ·
free disk 12,392,706,048 bytes at 22:25:48Z, 12,391,337,984 bytes at
22:34:36Z · nothing was downloaded.

**This file is a working file. It names what each option of part d does
mechanically and why passages were removed. It must not reach a juror or a
referee** (HANDED-FORWARD, fifth-fix section, C-5).

Criteria, written before any juror file was changed:
`exam-prep/fifth-fix/criteria-written-before-correcting.md`.

**Opened:** `RULES.md`, `TACTICS.md`; `exam-prep/` — `REVIEW-4.md`,
`review-4/criteria-written-before-ruling.md`, `README.md`,
`JUROR-QUESTIONS.md`, `VERDICT.md` (fourth-fix section; third-fix section
lines 296–320), `HANDED-FORWARD.md` (fourth-fix section), the four
fourth-fix juror files, `third-fix/juror-questions/JQ-R04-GATE.md`,
`REVIEW-3.md` lines 176–190 (its list of tests) and a grep of it;
`decisions/2026-10-01-jq-r04-gate/verdict.md`; `canteen/2026-09-19-sofia.md`
lines 108–122, 218–272, 660–675 and its heading list;
`scripts/29_identity_audit_exact.py` (lines 1–130, 217–350, 395–445,
715–745), `scripts/31_juror_file_check_fourth.py` (lines 1–60 and a grep).
**Not opened:** `exam/`; the rest of `decisions/`; `instructions/`;
`LEDGER.md`; `reports/`; `external/`; `notes/`; `TEAM.md`, the root
`README.md`, `cards/`, `data/` (allowed, not needed); any `scripts/exam_*`
(not read, not hashed, not run; their bytecode names appear in a listing of
`scripts/__pycache__/`); git history; anything outside the Balıkçıl folder.
No memory or session-log search. No script was run that writes bytecode
(`PYTHONDONTWRITEBYTECODE=1`, `python3 -B`); the listing of
`scripts/__pycache__/` was the same nine names before and after.

---

## 1 · REVIEW-4's items and their outcomes

REVIEW-4 does not number its requirements. I number them here, in the order
they appear in it.

| item | where in REVIEW-4 | outcome |
|---|---|---|
| R4-1 | §2 JQ-N1 | **done**: part 4's boundary table, the random-variation block and 4a's reference to the calibration's convention removed; block mechanism and its counts kept. Extension E-1 (§2 below). |
| R4-2 | §2 JQ-CANTEEN-8 | **done**: the quotation of `scripts/06_find_moments.py` lines 63–65 removed. |
| R4-3 | §2 JQ-R04-DATE-a | **done**: the two sentences of lines 77–78 removed. |
| R4-4 | §2 JQ-R04-CONTENT-a / -c | **done**: rows 3–4, the sentence reporting their effect, the paragraph of lines 159–162 and part c's pointer of lines 254–255 removed; part a's premise stated without figures. Extension E-2. |
| R4-5 | §2 shared defect; §4 contradiction; §7 item 2 | **referred to jurors**: new row **JQ-R04-CONTENT-d** in the DATE/CONTENT group (§3). The consequence sentences of JQ-R04-CONTENT and JQ-R04-DATE now say that part d decides it; option b1's trailing clause removed. Extension E-3. |
| R4-6 | §4 last bullet; §7 item 3 | **done**: HANDED-FORWARD fifth-fix section replaces A-0.4 (stated against the ratified outcome) and A-0.1 (GATE ratified; part d added). |
| R4-7 | §7 item 4, GATE status | **done**: the index shows JQ-R04-GATE as ratified, with its verdict file. |
| R4-8 | §7 item 4, canteen book | **done**: the six DATE/CONTENT rows (and the new seventh) give the canteen book only by the five line ranges JQ-R04-CONTENT names. |
| R4-9 | §7 item 5, "earlier verdicts" | **cannot be done by this run**: the GATE jurors' answers, their commission (`instructions/`) and `LEDGER.md` are closed to me. **Referred to the coordinator** (§5). |
| R4-10 | §7 item 6 | **done for every list this run writes** (index; C-5 in HANDED-FORWARD). Whether any earlier commission complied is not visible to me. |
| R4-11 | §1 N-1 condition 3; §6.3 | **handed forward**: HANDED-FORWARD fifth-fix B-1. |
| R4-12 | §1 N-1 condition 1 | files corrected (R4-1, R4-2); commissioning and ratification **referred to the coordinator**. |
| R4-13 | §1 N-1 condition 2 | **handed forward**, already in force (fourth-fix B-2 … B-5; B-1 as replaced). |
| R4-14 | §4 gap: whether one attack beating its line is enough for "carries a measured coin signature" | **not acted on** — REVIEW-4 names it as a gap, not a requirement, and this run is narrow. It is a definition that can change numbers on exam material; **referred to the coordinator** as a possible open question. |
| R4-15 | §4 RULES 13 note | **recorded**: the ratified GATE verdict gives no reading of RULES 13, so the referee check the fourth-fix VERDICT ("For the coordinator", item 2) asked for has nothing to compare. |
| R4-16 | §5, `make_jq_n1.py` and the hand-added sentence | **recorded**. The fifth-fix JQ-N1 is built from the **issued** fourth-fix file, not from `make_jq_n1.py`, by `exam-prep/fifth-fix/make_fifth_fix_files.py`, which asserts every edit; `make_jq_n1.py` is not changed. |
| R4-17 | §5, run `721b2448f1722ccf` not reproducible | **recorded**; nothing this run can do (its engine version no longer exists in the working tree). |
| R4-18 | §1 R-04 ruling | R-04 **not solved** (VERDICT). |

## 2 · Edits beyond REVIEW-4's list, with reasons (RULES 32)

Each is allowed by criteria §2.2 (a) or (b).

- **E-1 · JQ-N1, closing paragraph** — (a). It quoted a boundary range "in
  the full table of the source file named above"; once the table and its
  source line are gone, the pointer dangles, and repairing it would send a
  juror to the file whose per-option boundaries R4-1 removed. The range was
  removed, keeping the event spread (289 against 58) from the table the
  file still carries.
- **E-2 · JQ-R04-CONTENT part a, rows 1–2 and their sentence** — (a)/(b).
  REVIEW-4 asks that part a's premise be stated "without saying which
  rendering meets it". Rows 1–2 and the sentence "So the column carries a
  measured coin signature when it is ranked from the printed values" say
  which rendering meets it; and REVIEW-3 §5 (iii) ruled the file not fit
  when it showed only the rendering where the signature exists. Keeping
  rows 1–2 alone would recreate that defect. All four rows and the sentence
  were removed; the two audit run numbers in part a's bullets, which only
  sourced those rows, were removed with them. REVIEW-3 §5 allowed stating
  the premise without figures.
- **E-3 · JQ-R04-DATE, closing paragraph** — (b). It says "A 'no' means the
  field stays and is named in the exam manifest as a known channel": the
  same consequence REVIEW-4 found in CONTENT. The bitcoin and ethereum
  columns (DATE part a) feed the families `btc-eth` and `repeat-btceth`,
  which are inside `ALL-removable` (`scripts/29_identity_audit_exact.py`,
  `FAMILIES` and `FORCED_FAMILIES`). Under the ratified gate, a "no" to
  DATE part a would leave them graded unless part d says otherwise. The
  paragraph now points to part d. REVIEW-4 ruled DATE-b and -c fit and did
  not name this paragraph; I extend its shared-defect finding by its own
  test.
- **E-4 · cross-references** to the companion juror file now name the
  fifth-fix path; JQ-R04-DATE's "all three of its parts" became "all four".
- **E-5 · JQ-R04-CONTENT "What you decide"** names part d's definition.
- **E-6 · each file's header** gains a "Corrected by" line, which says what
  was removed and that it was not needed, without describing it.
- **E-7 · one check made afterwards.** Criteria §3's last bullet said a
  juror file's "What you open" equals its row's list. The index lists, for
  each row, what its **group** needs (rows answered together go to the same
  jurors), so DATE's own list (no canteen lines) is smaller than its rows'.
  The check compares the row with the union over its group. This is a
  change made after looking, so it carries that label (RULES 6).

Not edited, and noted: the CONTENT and DATE headers cite `exam-prep/REVIEW.md`
and `exam-prep/REVIEW-3.md` as provenance, and CONTENT part b cites a
review-3 probe as the source of one sentence. None is on a reading list
(C-5 forbids giving them), and REVIEW-4 did not rule on them.

## 3 · The new row JQ-R04-CONTENT-d

**Why a juror question.** REVIEW-4 §7 item 2 leaves to the coordinator
whether "a field that a ratified CONTENT outcome keeps on the card leaves
`ALL-removable`", and says that by RULES 33 it is a choice that changes the
numbers. My instruction says such a choice is not settled by the
coordinator alone and is to be written as a juror question in the group it
bears on. It bears on every DATE and CONTENT part (all of them can keep a
field on the card), so it is part d of `JQ-R04-CONTENT.md`, answered by the
same jurors.

**What it asks** is a reading of the GATE file's own definition of
`ALL-removable` (lines 64–66) — whether a field kept by a ratified reading
of TACTICS is one "that must stay … because … TACTICS requires" it. It does
not reopen the ratified verdict (which attack decides), and it does not
decide which features are computed from which field (engineering, read from
the code, reviewed). Three options and "other": every kept field; only a
field no permitted rendering leaves out; only what a rule or TACTICS
requires by its own words.

**Held to criteria §1.** (i) every passage it needs is quoted, with file and
line, checked by script (Q); (ii) each option can be carried out — the row
is built from feature prefixes, so a later audit version can move a field's
features out (HANDED-FORWARD fifth-fix A-0.4 step 1 says how, and stops on
a feature computed from a kept and a non-kept field); (iii) each option
carries one ground taken from the definition's words; (iv) the file tells
jurors that if they find the question is about a rule, not a definition, it
is the user's — the scope objection is not hidden; (v) it shows **no
measured figure**; (vi) its only premise about the instrument is that
everything the audit computes from the fields these parts are about is
inside the row today (checked against the audit's code by script, Q) — it
says nothing about whether any material passes; (vii) it quotes the
ratified verdict and does not contradict it.

**The strongest objection to referring it** — that it is not a juror's
question at all: either it is engineering (the GATE file, lines 26–28, calls
the feature list engineering), or a "yes" would let a measured coin signature
stay on exam cards ungraded, which the third-fix VERDICT (point 3) called a
question about a rule, the user's. My reply: the feature list is
engineering, but which families count as "must stay" is the definition the
GATE file itself states, and the instrument has always left some fields
that must stay ungraded (the forced residual of `R-04-blindness.md` §7); a
juror can read that definition. Whether a referee agrees is the referee's
check of scope (RULES 35); if it refuses on scope, the point goes to the
user, and VERDICT says so.

**What each option does mechanically** (working note, not for jurors):
under "no", every field the group keeps stays graded, and a kept field that
carries a signature can fail the gate; under "yes", it is reported, not
graded; under the middle option, the rendering choice of the run that
closes R-04 decides which. No measurement of any option's effect on the
gate was made or opened by this run.

## 4 · The juror rows, row by row

Tests: criteria §1 — REVIEW-2's (i)–(v) as REVIEW-3 applied them, REVIEW-4's
(vi) as its criteria file fixes it, and (vii) no contradiction with the
ratified GATE verdict. Script checks: run of
`scripts/32_juror_file_check_fifth.py` named in §6.

| row | file | (i)–(v) | (vi) | (vii) | result |
|---|---|---|---|---|---|
| JQ-N1-1 | fifth-fix JQ-N1 | unchanged text; passed REVIEW-4 | the shared item REVIEW-4 found (part 4 table) is gone; the closing paragraph keeps only the event spread from the top table (premise) | no reading of RULES 13 in the verdict | **fit** |
| JQ-N1-2 | same | unchanged text; passed REVIEW-4 | as N1-1 | as N1-1 | **fit** |
| JQ-N1-3 | same | unchanged; REVIEW-4 fit | as N1-1 | as N1-1 | **fit** |
| JQ-N1-4 | same | the block mechanism and its counts unchanged | table, random-variation block and 4a's calibration reference gone; 4a's "for example" kept (REVIEW-4 passed it) | as N1-1 | **fit** |
| JQ-CANTEEN-8 | fifth-fix JQ-CANTEEN-8 | unchanged apart from the deletion | the quotation REVIEW-4 found (L2) is gone; the premise at lines 114–118 (now 115–119) stays | no bearing | **fit** |
| JQ-R04-GATE | third-fix, unchanged | — | — | — | **ratified**; not ruled, not to be commissioned |
| JQ-R04-DATE-a | fifth-fix JQ-R04-DATE | 243 / 495 and 0 / 46,170 unchanged | the sentence REVIEW-4 found (L2) is gone | closing paragraph points to part d (E-3) | **fit** |
| JQ-R04-DATE-b | same | unchanged | unchanged; REVIEW-4 fit | as DATE-a | **fit** |
| JQ-R04-DATE-c | same | unchanged | unchanged; REVIEW-4 fit | as DATE-a | **fit** |
| JQ-R04-CONTENT-a | fifth-fix JQ-R04-CONTENT | premise stated without figures (REVIEW-3 §5 allows it); no rendering shown alone (REVIEW-3 (iii)) | rows 1–4, the effect sentence and lines 159–162 gone | closing paragraph points to part d | **fit** |
| JQ-R04-CONTENT-b | same | its figures unchanged and reproduced by REVIEW-4 | b1's trailing clause gone; its figures are b1's premise (REVIEW-4) | closing paragraph points to part d | **fit** |
| JQ-R04-CONTENT-c | same | H-4 table unchanged and reproduced by REVIEW-4 | the pointer to part a's effect gone | as CONTENT-b | **fit** |
| JQ-R04-CONTENT-d | same | §3 | §3: no figure; one premise sentence, checked | quotes the verdict | **fit by my tests; never reviewed** |
| JQ-B1 | third-fix | — | — | — | **withdrawn**, unchanged |

"Fit" here is my ruling under the stated criteria. "Leans" is a judgement
(REVIEW-4 §8 item 7 says so of its own rulings); a reviewer may draw the
line elsewhere. None of the corrected files has been reviewed since.

**Couplings** stand as REVIEW-4 §3 found them; part d joins the
DATE/CONTENT group because every part of it can keep a field on the card.

## 5 · What I could not do, by name

1. **R4-9.** Whether the GATE jurors' "earlier verdicts" means
   `exam-prep/VERDICT.md` — whose third-fix section, point 2, says which
   readings of the gate fail on material measured then — cannot be seen
   from `decisions/2026-10-01-jq-r04-gate/verdict.md`, the only file under
   `decisions/` I may open. The commission is under `instructions/`, the
   answers under `decisions/`, the record in `LEDGER.md`: all closed. If it
   does mean that file, the GATE jurors saw results before choosing
   (RULES 6). A ratified verdict is not mine to reopen; that is the
   coordinator's, and if it reaches a rule, the user's.
2. **Whether JQ-R04-GATE's ratification is recorded in `LEDGER.md`**
   (RULES 35) — `LEDGER.md` is closed.
3. **Whether any juror or referee has already been given a file C-5
   forbids** — not visible.
4. **No figure was re-measured**: no juror figure is new; the figures that
   remain were reproduced by REVIEW-4 or REVIEW-3, not by me.
5. **Nothing measured on exam cards**; `exam/` is closed.
6. **Part d has not been reviewed**, and the corrected rows have not been
   reviewed since correction.

## 6 · Checks run

`scripts/32_juror_file_check_fifth.py` (new). Run number and result:
recorded in `exam-prep/fifth-fix/checks/runs/` and quoted in `VERDICT.md`'s
fifth-fix section; its report is `exam-prep/fifth-fix/checks/juror-file-check-<run>.md`.
What it checks: R rebuild of all four files from the fourth-fix files by the
builder; X every passage REVIEW-4 requires removed is gone; N no new number
(the only new ones are the five line numbers of part d's quotations);
Q those quotations against their source lines, and part d's premise against
the audit's `FAMILIES`, `FORCED_FAMILIES` and `REPEAT_GROUP` (read as text);
I the index (rows, no stray digits, ratified GATE status, no forbidden file
in any reading list, canteen by line ranges, reading lists equal to the
group's "What you open", earlier versions by SHA-256); U nothing earlier
changed (pre-run snapshot), appended files keep their pre-run bytes, no new
file outside `exam-prep/fifth-fix/` but the script itself.

## 7 · Decisions I took that the instruction did not cover

1. **Numbering REVIEW-4's items** R4-1 … R4-18 (§1).
2. **Part d's place, wording and three options** (§3). The options are mine,
   taken from the definition's words; "other" is open.
3. **E-1 … E-7** (§2).
4. **HANDED-FORWARD amended, not restated whole**: the fifth-fix section
   replaces A-0.1, A-0.4 and B-1 and adds C-5; a later run reads the
   fourth-fix section and the fifth-fix section. Restating everything again
   risked transcription errors in items nobody asked to change.
5. **A-0.4 step 1's stop** when a feature is computed from a kept and a
   non-kept field — a stop-and-ask, not a rule; no number.
6. **The part 4 table goes to nobody.** REVIEW-4 §2 says it "can go to the
   referee", and §7 item 6 says files carrying option effects may reach no
   juror or referee. I followed the stricter: a referee checks count,
   independence, grounding, split, objection and scope, none of which needs
   the effect of an option (RULES 6, 35).
7. **"Not reviewed since"** is written into every changed row's status, so
   the coordinator sees that commissioning before a review is a choice.
8. **The pre-run snapshot** excludes `scripts/exam_*` (my instruction closes
   them; hashing reads them) and bytecode.

## 8 · How to reproduce

- `PYTHONDONTWRITEBYTECODE=1 python3 -B exam-prep/fifth-fix/make_fifth_fix_files.py --out <empty folder>`
  rebuilds the four juror files; compare with `cmp`.
- `PYTHONDONTWRITEBYTECODE=1 python3 -B scripts/32_juror_file_check_fifth.py --dry`
  runs every check and writes nothing; without `--dry` it records
  (append-only; a different content under an existing run number stops it).
