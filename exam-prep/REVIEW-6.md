# Review 6 — the sixth pre-exam run's juror files (`exam-prep/sixth-fix/`)

Mateo · data engineer, reviewing posture · first clock read
2026-10-01T23:13:33Z, this file written after 2026-10-01T23:23:41Z (system
clock, RULES 23) · free disk 12,381,564,928 bytes at 23:13:33Z,
12,380,585,984 bytes at 23:23:41Z · nothing was downloaded.

I did not do the work under review and was not told how it was done. I
review only the rows of the index whose status is "to be commissioned" or
"waiting". Criteria, fixed before any sixth-fix juror file was opened and
before any check or probe was run:
`exam-prep/review-6/criteria-written-before-ruling.md`. Probes and outputs
side by side: `exam-prep/review-6/probes/`.

**This file discusses what options do and the audit's grounds for its
forced families. It must not reach a juror or a referee** (HANDED-FORWARD
sixth-fix C-5, "nothing under `exam-prep/` that the row does not name";
RULES 6).

**Opened:** `RULES.md`, `TACTICS.md`;
`decisions/2026-10-01-jq-r04-gate/verdict.md`,
`decisions/2026-10-01-jq-n1-canteen-8/verdict.md`; `exam-prep/` —
`README.md`, `JUROR-QUESTIONS.md`, `REVIEW-5.md` and its criteria file,
REVIEW-4 lines 1–160 and its criteria file, REVIEW-2 lines 226–320,
REVIEW-3 lines 176–300, the sixth-fix folder (SIXTH-FIX, criteria, the four
juror files, FINGERPRINTS, the snapshot files by `grep`/`awk`), the fifth-fix
DATE and CONTENT files (by `diff`), the fourth-fix CONTENT file (option b1,
by `grep`), FIFTH-FIX (by `grep`), `VERDICT.md` lines 300–320 and 649–end,
`HANDED-FORWARD.md` headings, lines 165–240 and 400–end,
`third-fix/juror-questions/JQ-R04-GATE.md` lines 50–70 and a `grep` for
figures; `scripts/29_identity_audit_exact.py` lines 217–460 and 720–745
plus `grep`s; `scripts/33_juror_file_check_sixth.py` lines 1–200 and
560–663; `canteen/2026-09-19-sofia.md` only through probe p2 (the cited
lines). `git status` once (working tree only).
**Not opened:** `exam/`; the rest of `decisions/`; `instructions/`;
`LEDGER.md`; `reports/`; `external/`; `notes/`; `cards/`, `data/`,
`TEAM.md`, root `README.md` (allowed, not needed); any `scripts/exam_*`
(not read, not run; three bytecode names appear in a listing of
`scripts/__pycache__/`); git history (no log, show or diff of commits);
anything outside the Balıkçıl folder. One tool output was too large and was
saved by the harness to a file outside this folder; I did not open it and
re-ran the command with a narrower scope. No memory or session-log search.

---

## 1 · Rulings, row by row

Tests (criteria file): REVIEW-2 (i)–(v) as REVIEW-3 §5 states them; (vi) as
REVIEW-4's criteria fix it (L1 / L2 / L3; fails only if it leans **and** is
not needed); the coupling test; REVIEW-5's deletion test; determinacy as
REVIEW-5 §2 and §4 applied (ii); reading lists as REVIEW-5's criteria.

| row | fit? | RULES 33 scope | why |
|---|---|---|---|
| JQ-R04-CARRIES-a | **fit** | **inside** | (i) the file quotes all it needs; every quotation found in its lines (p2). (ii) each of A–D is carried out by the audit as it stands; where the nearest-neighbour versions disagree the run stops and refers (A-0.7), the same stop REVIEW-5 §5 accepted for the gate. (iii)/(vi) the options are the GATE question's set with no grounds attached; neither the ratified GATE outcome nor any earlier choice is shown (no L2); no figure (no L1). The tie paragraph describes a mechanism the stop needs. Scope: a definition; the objection that choosing among A–D sets how strict a test is (a threshold) is the same objection the GATE referee weighed and ratified as procedure (§5 and §6 of that verdict); the file invites jurors to raise it (lines 45–47). |
| JQ-R04-CARRIES-b | **fit** | **inside** | (ii) each option names its families for the trade-count column, and every name and feature it states matches the audit's code (p3: `trades-level` = level + the previous-7-day feature; `repeat-trades` = two features, nothing else; `shape-scale-free` = two features for each of eight columns; absent or constant features dropped; "beats" is strictly above). Option one needs a new audit row; A-0.7 says how. One ground per option; no figure; no precedent. |
| JQ-R04-DATE-a | **fit** | **inside** | Changes are the header, source notes and closing paragraph only (`diff`); figures unchanged (script 33 N; reproduced by REVIEW-3/-4). The closing paragraph no longer states any gate consequence; it says where the rest is decided, which is true. No pointer to a review, script or run remains (my `grep`). |
| JQ-R04-DATE-b | **fit** | **inside** | As DATE-a. |
| JQ-R04-DATE-c | **fit** | **inside** | As DATE-a. |
| JQ-R04-CONTENT-a | **fit** — provided the CARRIES group is ratified before it sits, as the index orders | **inside** | REVIEW-5's gap (§2) is answered by a question put first to other jurors; the added paragraph names that question without its options or outcome (no L2) and is the premise of the condition (needed). With a ratified definition, "yes" and "no" can both be carried out; the residual nearest-neighbour stop is named, not hidden. The heading that defined "carries" is gone (E-5). |
| JQ-R04-CONTENT-b | **fit** | **inside** | REVIEW-5's only ground (the gate's fail condition in the shared closing paragraph, L1) is gone: the paragraph now names CONTENT-d and gives no consequence. Judgement noted, not ruled: since the fifth fix removed b1's clause "with its measured signature", the table's need rests on the file's "given RULES 9" frame, not on b1's wording; REVIEW-5 saw the same text and did not fail it, and I do not either. Another reviewer could. |
| JQ-R04-CONTENT-c | **fit** | **inside** | Only its source note changed; no effect shown. |
| JQ-R04-CONTENT-d | **not fit** | **contested** — not ruled inside (§3) | **(ii)** options "yes" and "only where no permitted rendering leaves it out" cannot be carried out without a further choice that changes the numbers (§2.1). **(vi) L2**, not needed: the quoted ground for `p7-shape` (lines 100–101) (§2.2). Passes: option "no" is now determinate (a fixed list; REVIEW-5 §4 (ii) cured); every quotation matches its source lines (p2: GATE lines 55–57 and 64–66, verdict line 72, audit lines 431–434, RULES and TACTICS lines); the "inside the row" sentence is true of the code (p3); the GATE file path is gone; it sits alone. |

**Groups.** The JQ-R04-CARRIES group (a, b): both rows fit; it can be
commissioned now. The DATE/CONTENT group (DATE-a … -c, CONTENT-a … -c): all
six rows fit; it can be commissioned once JQ-R04-CARRIES is ratified, as the
index says. JQ-R04-CONTENT-d: **cannot be commissioned** until corrected.
It sits alone, so its state does not hold up either group; but HANDED-FORWARD
fifth-fix A-0.4 step 1 composes the gate row from its ratified outcome, so
R-04 cannot close without it.

## 2 · JQ-R04-CONTENT-d — the two grounds

### 2.1 · (ii) "a field the ratified answers keep" is not fixed

Options "yes" and "only where…" turn on which fields "the ratified answers
to JQ-R04-DATE and to JQ-R04-CONTENT parts a–c keep … on the exam card".
That is clear for a field a question names and an answer keeps
(the bitcoin and ethereum columns under a "no" to DATE-a). It is not clear
for:

1. **The eight ranked columns other than the trade count.** No question
   decides whether they stay; CONTENT-c decides only where their order comes
   from. Yet the d file's new section "What the other questions decide"
   (lines 111–121) lists "where the order of the ranked columns comes from"
   among the decisions that "may keep a field on the card", right after
   lines 107–109 name "the other ranked columns" as inside the row. A run
   composing the row can read a ratified CONTENT-c answer as keeping them,
   or not.
2. **The reach of a ratified "no" to CONTENT-a.** Its ground is general:
   "TACTICS 3 says what is on the card and TACTICS 6 lists, closed, what is
   hidden; a column not on that list stays" (CONTENT lines 146–147). Read
   with d's "yes" ("stays because TACTICS, as they read it, requires it"),
   it can keep the trade-count column only (the part's subject) or every
   TACTICS-3 column not on the hidden list.

Under the wide reading, options "yes" and "only where…" move the features of
most families of the row out of it; under the narrow one, only those of the
named fields. HANDED-FORWARD fifth-fix A-0.4 step 1 makes the run name "the
ratified outcome that keeps that field on the card" for each feature moved,
but does not say which outcomes count as keeping. That is a choice that
changes the numbers, made by nobody (RULES 33); the same test REVIEW-5 §4
applied to option "no". The options' text is unchanged from the fifth fix,
and REVIEW-5 did not raise this. The sixth fix's new section makes the wide
reading more available.

### 2.2 · (vi) L2 — the ground quoted for `p7-shape`

Lines 100–101 give the audit's ground for keeping `p7-shape` out of the row:
"TACTICS 3 puts a previous-7-day summary on the card". That is a script's
choice on the open point itself: it treats "TACTICS 3 puts it on the card"
as "TACTICS requires it", which is option "yes"'s reading
("stays because TACTICS, as they read it, requires it there"). Nothing
answers it on the other side. In particular, the file does not say that
the audit keeps the other two features of the same previous-7-day line
(`p7:log_avg_trades`, `p7:log_avg_vol`) **inside** the row (p3). So it
leans.

**Needed?** REVIEW-5 §4 said that telling jurors which families are outside
the row "or why" would be "a needed" precedent. That was for the fifth
wording of option "no" ("by its own words"), which could not be applied
without knowing the grounds. The sixth wording of "no" is a fixed list
("only the four families listed above"), and the file says "This question
does not ask about these four". The names are now needed; the grounds are
not. So the `p7-shape` ground fails (vi). The other three grounds cite the
frozen book and do not lean either way. **This disagrees with REVIEW-5 §4's
"needed".** The reason is that the basis for that ruling, the old wording
of option "no", no longer exists.

## 3 · RULES 33 scope

- **Inside:** CARRIES-a, CARRIES-b, DATE-a … -c, CONTENT-a … -c (§1).
- **CONTENT-d — contested; I do not rule it inside.** Option "no" is inside:
  it reads a definition and moves nothing. Options "yes" and "only where…",
  once ratified, would leave a measured coin channel on exam cards
  ungraded. "Only where…" does so exactly in the case the third-fix
  `VERDICT.md` (point 3, lines 310–312) reserved for the user: "whether a
  measured channel that cannot be removed is acceptable under RULES 9 is a
  question about a rule, which is the user's". "Yes" goes further than that
  case. The case for inside is that d reads the GATE file's definition of
  `ALL-removable` (an exam-prep text, not `RULES.md`), and that the file
  tells jurors to say so if they think otherwise (lines 147–150). Which
  reading holds is for d's referee (RULES 35, scope) or the user. On my
  reading, the case for "outside" is the stronger one for those two
  options. I name the point and do not settle it.

## 4 · Contradiction with a ratified verdict

**None, in any row reviewed.**

- **JQ-R04-GATE verdict.** d quotes line 72 exactly (p2) and says it does
  not reopen it. DATE and CONTENT no longer state the gate's rule.
  CARRIES-a may ratify a different attack rule for "carries" than the
  gate's "either". That is a different measurement on different features,
  and both can be applied to the same cards. It is a divergence by design,
  not a contradiction. Gaps still open, named before: the verdict does not
  say how the row is composed (d is meant to fill that), nor which
  nearest-neighbour version is "the attack" (A-0.8).
- **JQ-N1 / JQ-CANTEEN-8 verdict.** No reviewed row reads RULES 13, the
  event unit, or calm spacing. DATE-a's "card pairs that truly share an
  hour" describes the identity audit's overlap-of-windows measurement. It
  is not a reading of RULES 13's "same hour", so it cannot contradict the
  ratified start-hour reading. A referee might confuse the two; they are
  different measures.

## 5 · The order of sitting and its couplings — **stand**, with three notes

- CARRIES before DATE/CONTENT: needed, because CONTENT-a's condition uses
  the CARRIES definition. CONTENT-d alone, at any time: its options are
  conditional on the other outcomes and need none of them to be answered.
  Three disjoint juror sets: each pair of groups would otherwise let one set
  of jurors choose by combined effect (REVIEW-3 §5, REVIEW-5 §3). The
  DATE/CONTENT coupling stands (REVIEW-3/-4). CARRIES-a with -b stands (one
  definition in two halves).
- What crosses between groups: CARRIES quotes CONTENT-a's question (not its
  options); d names the subjects of DATE/CONTENT (not their questions or
  options); DATE/CONTENT get the CARRIES ratification sentence only. None
  of these shows a figure or an option effect.
- **Note 1 — the index is stale on the JQ-N1 group.** The order section
  ("Now: … (being answered)") and the five JQ-N1 / JQ-CANTEEN-8 rows say
  "commissioned — being answered". `decisions/2026-10-01-jq-n1-canteen-8/verdict.md`
  reads RATIFIED. Its file time is 22:58:07Z, earlier than the index's
  23:03:33Z (file system, not git). The R-04 order does not depend on
  it.
- **Note 2 — "the ratification sentence" is singular; CARRIES has two
  parts.** If the referee writes one sentence per part (as the
  JQ-N1/CANTEEN-8 verdict does), the commission should give the sentence(s)
  covering both parts. Whether a sentence alone is intelligible to
  DATE/CONTENT jurors without the CARRIES file (for example a family name)
  depends on how the referee words it. They are not asked to apply it.
- **Note 3.** If CARRIES is refused, the DATE/CONTENT group waits, as the
  index says. Nothing else is affected.

## 6 · The sixth run's stated extensions of REVIEW-5 (sixth-fix VERDICT)

1. **GATE file path removed from d — holds.** That file carries the gate
   row's measured figures on blinded observation cards (its lines 130–134,
   every configuration "beats"). A d juror who opened it would see an
   effect of d's options (L1). The quotations stay and match (p2).
2. **CONTENT's heading no longer defines "carries" — holds.** The old
   heading told part a's jurors what "carries" means while CARRIES is asked
   to define it (L2, not needed). The text under it is unchanged and
   describes how the file's figures were made.
3. **CARRIES apart from d as well — holds.** With one set of jurors, a
   narrow "carries" with d "no", or a broad one with any d, could be chosen
   by combined effect on the same column. This is REVIEW-5 §3's structure,
   and it holds without any figure.

The sixth run's criteria also add tests (vii) and (x). (vii) is REVIEW-4's
contradiction test plus "say where it is decided"; I applied the former.
(x) is from its instruction and is not one of REVIEW-2 … -5's tests. I
checked it as a fact (no pointer in the four files, my `grep`; script 33 X)
and ruled nothing on it alone.

## 7 · Reproduction (outputs in `exam-prep/review-6/probes/`)

| what | result |
|---|---|
| `scripts/33_juror_file_check_sixth.py --dry` (p1) | **same run number `b0af115f117e9f68`**, 328 checks, 327 ok, 1 FAIL: `U no new exam-prep file outside sixth-fix/`, which is my own `exam-prep/review-6/` files. Every other check, including `U unchanged`, passes. Nothing written. |
| quotations (p2, my script) | 90 checks, 0 failed: every RULES, TACTICS, canteen, GATE-file, verdict and audit passage quoted by the four files is in its cited lines and in the file that quotes it |
| audit facts (p3, `ast` + text, not imported) | 17 checks, 0 failed; audit SHA-256 `cfc4bdcb…d03f`, the same as REVIEW-4 and REVIEW-5 |
| `exam-prep/sixth-fix/FINGERPRINTS.md` (p4) | 26 of 26 SHA-256 match (`sha256sum -c`) |
| `diff` fifth → sixth DATE and CONTENT | only headers, source notes, CONTENT-a's added paragraph, CONTENT's heading, part d's removal and the closing paragraphs; no figure, question or option changed |

Every run used `PYTHONDONTWRITEBYTECODE=1` and `python3 -B`;
`scripts/__pycache__/` held the same nine names before and after.

## 8 · What I could not do, by name

1. **Nothing measured on exam cards**; `exam/` is closed.
2. **How many features or families each reading in §2.1 would move.** Not
   measured, on purpose: that would be an option effect, and the ruling
   does not need it.
3. **The sixth run's instruction** (the coordinator's withdrawal of "in the
   group it bears on"). It is under `instructions/`, which is closed. I rely
   on SIXTH-FIX §2 and VERDICT's account.
4. **Whether the GATE and JQ-N1/CANTEEN-8 ratifications are in
   `LEDGER.md`** (RULES 35). `LEDGER.md` is closed.
5. **How the CARRIES referee will word its ratification** (§5 note 2).
6. **"Leans", "needed" and "determinate" are judgements.** I fixed my
   criteria before checking. Another reviewer could draw the line elsewhere,
   most plausibly on d §2.2 (against REVIEW-5's "needed") and on CONTENT-b's
   table.

## 9 · Decisions I took that the instruction did not cover

1. **I ruled d not fit on a ground REVIEW-5 did not raise** (§2.1, option
   text unchanged since the fifth fix). The instruction asks for fitness
   under every test REVIEW-2 … -5 applied, not only under their findings.
2. **I disagreed with REVIEW-5 §4's "needed" for the grounds of the four
   families**, because the rewording of option "no" changed what is needed
   (§2.2).
3. **I reported d's scope as "contested", not inside or outside** (§3), as
   REVIEW-5 did, and gave my reading.
4. **I treated the sixth run's test (x) as a fact to report, not a fitness
   test.**
5. **I reported the stale JQ-N1 statuses in the index**, although those rows
   are outside my review, because the order section asks about them.
6. **I read GATE-file lines 50–70 and its figures by `grep`** to test
   extension 1, and audit lines beyond the quoted ones to test the files'
   premises.
7. **I ran script 33 only with `--dry`**, so that nothing was written into
   the sixth run's folder.

## 10 · Steer check

My instruction gives no result and predicts none. Named, mildly: "jurors
cannot run anything, so a fault in a juror file can only be caught here"
puts weight on finding faults. It is the reason given for the model choice.
"Do not re-review the JQ-N1 group … they are ratified" is information; it
matches the verdict file. Item 4's "or would decide a threshold, a score, a
trading rule or a change to a rule" quotes RULES 33 and frames no answer.
The git status supplied at start carried commit subjects of the forms
"work:", "ledger:" and "auto: working tree", and one untracked instruction
file name; no result.

## 11 · Fingerprints

`exam-prep/review-6/FINGERPRINTS.md`. This file's own SHA-256 is in my
report to the coordinator. I wrote only this file and `exam-prep/review-6/`.
No commit.
