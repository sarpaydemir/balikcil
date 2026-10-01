# Review 7 — the seventh pre-exam run and its question to the user (`exam-prep/USER-QUESTIONS.md`)

Mateo · data engineer, reviewing posture · first clock read
2026-10-01T23:45:59Z, this file written after 2026-10-01T23:54:31Z (system
clock, RULES 23) · free disk 12,370,382,848 bytes at 23:45:59Z,
12,053,204,992 bytes at 23:54:31Z (the drop is not this review's: its files
total a few tens of kilobytes) · nothing was downloaded.

I did not do the work under review and was not told how it was done.
Criteria, fixed before opening `exam-prep/seventh-fix/` and before any check
or probe: `exam-prep/review-7/criteria-written-before-ruling.md`. Probes and
outputs side by side: `exam-prep/review-7/probes/`.

**This file discusses what the answers of U-1 and of the withdrawn
JQ-R04-CONTENT-d do. It must not reach a juror or a referee** (HANDED-FORWARD
seventh-fix C-5; RULES 6).

**Opened:** `RULES.md`, `TACTICS.md`; the three verdicts the instruction
names (`jq-r04-gate`, `jq-n1-canteen-8`, `jq-r04-carries`); `exam-prep/` —
`README.md`, `JUROR-QUESTIONS.md`, `USER-QUESTIONS.md`, `REVIEW-6.md`, the
seventh-fix folder (SEVENTH-FIX, criteria, FINGERPRINTS, the check run's
`.json` and `.clock`), `HANDED-FORWARD.md` lines 285–296 and 400–680 plus
headings, `VERDICT.md` lines 300–316 and 800–941 plus headings and a `grep`,
the withdrawn `sixth-fix/juror-questions/JQ-R04-CONTENT-d.md`, the DATE and
CONTENT juror files by `grep` and lines 75–82, 139–150 (DATE) and 139–150
(CONTENT), `third-fix/juror-questions/JQ-R04-GATE.md` lines 40–100 and a
`grep` for figures; `scripts/29_identity_audit_exact.py` lines 217–470 and
720–790 plus `grep`s; `scripts/34_seventh_fix_check.py` lines 1–80, 200–300
and 480–530. `git status` once (working tree only); `stat` (times only) on
the three permitted verdicts and on files of `exam-prep/`.
**Not opened:** `exam/`; any `scripts/exam_*` (not read, not run; three
bytecode names appear in a listing of `scripts/__pycache__/`); the rest of
`decisions/` — **but I listed the names of the folders in `decisions/` once,
at the start, before narrowing my scope**; I opened nothing in them beyond
the three verdicts; `instructions/`, `LEDGER.md`, `reports/`, `external/`,
`notes/`; `canteen/`, `cards/`, `data/`, `TEAM.md`, root `README.md`
(allowed, not needed); git history (no log, show or diff); anything outside
the Balıkçıl folder. No memory or session-log search.

---

## 1 · Item 1 — whose question: **jurors**

**Ruling: the whole of JQ-R04-CONTENT-d (U-1 part 1 and part 2) is a
procedure and a definition that jurors may decide under RULES 33. No
answer it offers makes or changes a rule.** What is the user's is a
possible *later* question that is not part of this row (last bullet).

Grounds, each from a file I may read:

1. **The RULES 33 test** (`RULES.md` lines 119–121): a juror may not decide
   "a trading rule, … a threshold or score, and … a change to a rule in this
   file". No answer of the row is a trading rule, a number or a score. None
   changes a word of `RULES.md`: RULES 9 (line 41) hides "the coin name and
   the date", and under every answer neither is printed. None changes
   TACTICS 3 or 6: which fields stay is decided by other rows, and U-1 itself
   says no answer changes what jurors rule there.
2. **What is being read is an exam-prep text.** `ALL-removable` and its
   clause "minus the families that must stay on the card because a frozen
   canteen rule or TACTICS requires them" are written in the exam
   preparation (`third-fix/juror-questions/JQ-R04-GATE.md` lines 64–66,
   quoting `R-04-blindness.md`), not in `RULES.md`. Whether a field a ruling
   keeps is one "TACTICS requires" is the reading of that clause's word
   "requires" — "a wording that can be read two ways", which is what
   `RULES.md` lines 112–114 call an open question.
3. **The binding verdicts treat the same kind of choice as procedure.** The
   GATE verdict (§6) ratified "which measurement(s) the gate applies" as
   procedure over a reasoned threshold objection; the CARRIES verdict (§6)
   ratified "which features count as the column's" as definition. Which
   features the gate grades is of the same kind. The JQ-N1 verdict ratified
   a reading of what RULES 13's "same hour" requires — a choice that changes
   the counts — as definition.
4. **The laboratory already puts "what RULES 9 requires" to jurors.**
   JQ-R04-DATE question a (DATE lines 75–82) asks whether RULES 9 requires
   removing a column that gives the date away in another form although no
   date is printed; JQ-R04-CONTENT question a (CONTENT lines 139–146) asks
   whether a column carrying "a measured coin signature" may be left out,
   one answer reading "RULES 9 is the rule". Both were ruled inside RULES 33
   by REVIEW-6 §1. U-1's own ground — that deciding "whether the coin is
   'hidden' when its name is not printed but the card still gives the coin
   away measurably" is "a standard …, not the meaning of a word" — is the
   same structure as DATE-a.
5. **The same outcome already exists without the user.** Four groups of
   features are named-not-graded under every answer (U-1 point 3; audit
   `FORCED_FAMILIES`, lines 429–436). If leaving a measured channel
   ungraded were by itself a rule, that exemption would be one too; U-1
   leaves it outside the question and no reviewed file put it to the user.
6. **RULES 33's first sentence** (`RULES.md` line 116): "An open question is
   never answered by one person". If the row is a definition, a single
   answer by the user would breach it; a wrong juror classification, by
   contrast, is caught by the referee's scope check (RULES 35).

**The user's part, which is not this row.** If, under the answer jurors
ratify, a kept field fails the gate and no permitted printing passes, the
exam can proceed only by changing what TACTICS 3 puts on the card or what
TACTICS 6 hides, or by accepting the channel — that is the user's
(`RULES.md` lines 3–4). It is the case third-fix `VERDICT.md` point 3 (lines
311–313) reserved: "If no engineering closes what is left, whether a
measured channel that cannot be removed is acceptable under RULES 9 is a
question about a rule, which is the user's." It arises only after a gate
result, and only then.

**This is a judgement against two earlier ones.** REVIEW-6 §3 left the scope
contested and found the case for "outside" the stronger for two options;
the seventh run classed the whole row outside (SEVENTH-FIX §2). Neither
weighed grounds 4–6. The seventh run's point that option "no" alone is not
a question holds and is answered by keeping all options with jurors. I name
the disagreement; a referee or the user may draw the line elsewhere.

## 2 · Item 2 — `USER-QUESTIONS.md`: **not fit to be put to the user**

Tests F1–F6 (criteria file). Passes first:

- **F2, quotations:** 16 quotations and 2 cited ranges, each found in the
  cited lines and in the file (my probe p2, 18 checks, 0 failed; the seventh
  run's script 34 U-group agrees). The four groups match the audit's
  `FORCED_FAMILIES` and their features (lines 231–237, 263–270, 278–293,
  339–346, 414). The manifest sentence matches HANDED-FORWARD A-7 (lines
  285–288). The GATE verdict line 72 quotation is exact.
- **F3:** A, B, C, "Other" and "a definition for jurors after all" cover
  the answers the rules leave open, with part 2's two reaches.
- **F5, the file itself:** no measured figure, no size, no pass or fail.

Faults, by section of the file:

| section | test | fault |
|---|---|---|
| title line of U-1 | F4 | Asks about a field that "must stay"; answer B covers fields the rulings only *allow*. The title frames the question as C's case. |
| "What you need to know", point 3 (the path it cites) and "What is deliberately not here" | **F5** (RULES 6) | Point 3 cites `exam-prep/third-fix/juror-questions/JQ-R04-GATE.md`; that file's lines 130–134 give the graded row's results on blinded observation cards in five rows (four configurations and a variant), every one "beats". The last section tells the user such measurements exist "including the file cited in point 3" and that "whether to look at them before answering is yours". That is an invitation to open a result before writing the rule — the order RULES 6 (lines 34–35) forbids — and the result it points to shows how the answer that grades kept fields fares. The quotation can be sourced without the invitation; whether the GATE path must appear at all is for the next run. |
| "What you need to know", point 4 | F2 (not verifiable by me; likely stale) | "None of those rulings exists yet." At my clock `decisions/2026-10-01-jq-r04-date-content/verdict.md` exists (shown by `git status`; not opened). If it ratifies, the sentence is untrue now. |
| "Which written rule it touches, and why it is a rule question rather than a definition" | **F2, F4** | (a) The first bullet's ground — "Under answers B and C below, the exam can go ahead with cards on which the laboratory has measured a coin signature. The answer therefore decides what RULES 9 requires" — holds equally for A: under every answer the four groups are ungraded whatever they measure (the file's own point 3). The implied contrast is untrue, and it presents A as the answer that accepts no signature. (b) "Answer A on its own moves nothing" is true of the audit's code, not of the written definition: where a ruling holds that TACTICS requires a field, the definition's words ("TACTICS requires them") move it out, and A keeps it graded. So A is presented as the baseline, which it is only on one reading. (c) "The other side" ends with a review's preference ("the second found the case for the user the stronger one") — a precedent offered against one of the listed answers ("a definition for jurors after all"), with nothing on the other side; and it omits that RULES 33 (line 116) bars any one person from answering an open question, and that DATE-a and CONTENT-a put "what RULES 9 requires" to jurors (§1 grounds 4 and 6). (d) "Why now": RULES 6 is given as the reason to ask now, but under A the file says the matter can still "come back to you" after the gate has run; so the passage weighs RULES 6 against A only. |
| "Part 2", the "Wide" bullet | **F2** | "under B with this reach no feature it computes today would be graded" holds only if no ruling requires a printed field masked; the bullet's own exception ("unless a ruling requires it removed or masked") and DATE's "must be masked or removed" (DATE line 144) make it conditional. |
| "Part 2", the "Wide" bullet, and "How the answer is used" | **F6** | Where the wide reach leaves the graded set empty, the audit prints "no features left after blinding" for the row (lines 744–758) — neither "beats" nor not — and the fifth-fix A-0.4 step 4 passes the gate "only when … step 3 is graded". What the gate then does (passes, fails, stops) is not said here nor in HANDED-FORWARD; the run would have to choose. |
| "Part 2", closing paragraph | F6 | The stop "where it is unclear whether a ruling's words reach a field" is promised "under either reach"; HANDED-FORWARD seventh-fix A-0.4 step 1 (lines 646–649) names it **only under the wide reach**. The user is told of a stop the run is not required to make. |

Blemishes, noted, not ruled: "nearest-neighbour attack" and "pair AUC
attack" appear only inside the verdict quotation, unexplained (F1); "the
nine columns printed as ranks" assumes the reader knows the blinding (F1);
`TACTICS.md` §3's list runs to line 64, the file cites 55–62.

**Not a fault:** the file gives each answer a consequence and no reason;
it names the four groups without grounds (REVIEW-6 §2.2 applied); its
statements about the gate, the GATE verdict and the audit's code are true.

## 3 · Item 3 — handed forward checkable yes or no: **no**

The seventh-fix section of `HANDED-FORWARD.md` (lines 583–680):

- **A-0.1** (lines 605–622): checkable yes/no — eight named ratifications,
  the user's answer or its replacement, a date order, disjoint juror sets.
  It still reads as if only the user can answer U-1; if item 1 is accepted,
  it needs the juror route as its main case.
- **A-0.4 step 1** (lines 624–656): **not checkable yes/no**, for three
  reasons. (1) The empty graded set (§2, F6): the check's "does the row
  pass by steps 2–4" has no answer when the audit returns "no features
  left". (2) Lines 641–645 require naming, for every moved feature, "the
  ratified outcome or outcomes that allow or keep that field on the card";
  under the wide reach a field no ruling addresses (for example the open
  interest column) is kept by TACTICS 3, not by a ratified outcome, so the
  check's "every moved feature traced to … an outcome" cannot be met. (3)
  The stops listed (lines 646–649) differ from those U-1 promises the user
  (§2, last row); a run that meets HANDED-FORWARD can break U-1's promise.
- **C-5** (lines 660–680): checkable yes/no.

## 4 · Item 4 — the index shows each row's true status: **no**; carries no wording, option or number: **yes**

- **JQ-R04-CARRIES-a, -b** read "commissioned — being answered", and the
  order section says "Now: the JQ-R04-CARRIES group … being answered".
  `decisions/2026-10-01-jq-r04-carries/verdict.md` reads **RATIFIED**
  (3–0 and 2–1); its file time is 23:33:46Z, **before** the index's
  23:36:38Z (file system times, not git). The seventh run took the status
  from its instruction (SEVENTH-FIX §5 item 7).
- **JQ-R04-DATE-a … -c, JQ-R04-CONTENT-a … -c** read "waiting — not to be
  commissioned until JQ-R04-CARRIES is ratified". That condition is met;
  and a file `decisions/2026-10-01-jq-r04-date-content/verdict.md` exists.
  I did not open it, so I cannot say their true status; I can say it is
  not "waiting until CARRIES is ratified".
- JQ-N1 group, JQ-R04-GATE, JQ-B1: true. JQ-R04-CONTENT-d "withdrawn": true
  of the files; whether it should be withdrawn is item 1.
- **Wording, options, numbers:** none (probe p3). The index shares no
  seven-word run with U-1 or with any question file except provenance lines
  ("by Mateo … run 2026-10-01 system clock"); its numbers are rule numbers,
  part numbers, canteen line ranges and SHA-256 values; script 34's
  I-checks agree.

## 5 · Reproduction (outputs in `exam-prep/review-7/probes/`)

| what | result |
|---|---|
| `scripts/34_seventh_fix_check.py --dry --show` (p1) | run `54f349416e0e76c1`, 100 checks, 99 ok, 1 FAIL: "no new exam-prep file outside seventh-fix/", which lists my own `review-7/` files. The run number differs from the record (`97f03e98c28ed3ad`) only through the input "(listing of exam-prep/)": all 4,550 file inputs of the recorded run hash as recorded (my check against `runs/97f03e98c28ed3ad.json`). Nothing written. |
| quotations (p2, my script) | 18 checks, 0 failed |
| index (p3, my script) | statuses listed; shared wording and numbers as §4 |
| `exam-prep/seventh-fix/FINGERPRINTS.md` (p4) | 14 of 14 SHA-256 match (`sha256sum -c`); the four juror files hash as that file says |
| audit | SHA-256 `cfc4bdcb…d03f`, as HANDED-FORWARD names |

Every run used `PYTHONDONTWRITEBYTECODE=1` and `python3 -B`;
`scripts/__pycache__/` held the same nine names before and after; no cache
under `exam-prep/review-7/`.

## 6 · What I could not do, by name

1. **The DATE/CONTENT verdict** — not opened (closed). Whether it ratifies,
   refuses, or was commissioned before the CARRIES ratification, I cannot
   say; so the truth of U-1 point 4 and the DATE/CONTENT statuses is open.
2. **Whether the DATE/CONTENT jurors sat** with the clause naming
   JQ-R04-CONTENT-d as answered "by other jurors" (SEVENTH-FIX §4 item 3).
   If they did, their premise changed after they answered. Not checkable by
   me.
3. **`LEDGER.md`** — whether any ratification is recorded there.
4. **The user's view of item 1.** My ruling is a judgement on the text;
   the user, or a referee's scope check, may draw it elsewhere.
5. **Nothing measured on exam cards**; `exam/` is closed. I measured no
   option effect on purpose.
6. **"Leans" and "needed" are judgements.** I fixed criteria first; another
   reviewer could weigh the "Why now" passage differently.

## 7 · Decisions I took that the instruction did not cover

1. **I ruled item 1 "jurors"**, against REVIEW-6 §3's lean and the seventh
   run's classification, on grounds neither weighed (§1 grounds 4–6).
2. **I treated a pointer plus an invitation to a result as a RULES 6 fault**
   (§2, F5), although the file carries no figure itself.
3. **I opened the withdrawn d file and the DATE/CONTENT question lines** to
   test U-1's grounds and the classification; all under `exam-prep/`, which
   I may read.
4. **I used `stat` for file times** of the three permitted verdicts and of
   `exam-prep/` files; not for anything else in `decisions/`.
5. **I ran script 34 only with `--dry`**, so nothing was written into the
   seventh run's folder.
6. **Probe width of seven words** in p3 is my choice for a text probe, not
   a threshold.

## 8 · Steer check

My instruction gives no result. Named, mildly: item 1's "whether the row
belongs to the user **at all**" frames doubt about the user route; the
model-choice reason ("a question that leans, or that states something
untrue, decides the rule for them") puts weight on finding faults. My
ruling in §1 rests on cited text, not on those words. "The coordinator, who
has not opened `USER-QUESTIONS.md`" is information. The git status supplied
at start carried commit subjects "work:", "auto: working tree", "ledger:",
the untracked DATE/CONTENT verdict path, this review's instruction name, and
an untracked instruction named
`instructions/2026-10-01-2346-data-engineer-exam-moments.md` (not opened).
If that run builds exam cards before HANDED-FORWARD A-0.1 is met, the order
breaks; I cannot tell from a name.

## 9 · Fingerprints

`exam-prep/review-7/FINGERPRINTS.md`. This file's own SHA-256 is in my
report to the coordinator. I wrote only this file and `exam-prep/review-7/`.
No commit.
