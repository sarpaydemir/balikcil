# Seventh fix — criteria written before correcting

Mateo · data engineer · seventh-fix run · first clock read
2026-10-01T23:27:09Z; this file written at 2026-10-01T23:31:46Z (system clock),
after the pre-run snapshots (`pre-run-fingerprints.txt`,
`pre-run-scripts-fingerprints.txt`, both taken at 23:31Z) and before any
file outside `exam-prep/seventh-fix/` was written.

By this time I had read: `RULES.md`, `TACTICS.md`; `exam-prep/REVIEW-6.md`
(whole), `exam-prep/review-6/criteria-written-before-ruling.md`,
`exam-prep/review-5/criteria-written-before-ruling.md`,
`exam-prep/review-4/criteria-written-before-ruling.md`, `exam-prep/REVIEW-5.md`
(whole), REVIEW-3 lines 176–300, REVIEW-2 lines 220–320,
`exam-prep/JUROR-QUESTIONS.md`, `exam-prep/VERDICT.md` (whole),
`exam-prep/sixth-fix/SIXTH-FIX.md`, the sixth-fix DATE, CONTENT and
CONTENT-d juror files, `exam-prep/HANDED-FORWARD.md` lines 137–306 and
400–578, `exam-prep/third-fix/juror-questions/JQ-R04-GATE.md` lines 40–100,
`scripts/29_identity_audit_exact.py` lines 380–470, both ratified
`verdict.md` files. So these criteria are not blind to the files; they are
fixed before anything is changed.

## Scope of this run

`exam-prep/REVIEW-6.md` as it concerns JQ-R04-CONTENT-d, and the index's
stale statuses. Every other REVIEW-6 item is numbered and named "outside this
run". The files JQ-R04-CARRIES, JQ-R04-DATE and JQ-R04-CONTENT are not
changed (checked by hash).

## RULES 33 scope — how each part of JQ-R04-CONTENT-d is classed

- **Inside** when every option the part offers, once ratified, decides
  procedure or definition only.
- **Outside** when an option, once ratified, would by itself set a
  threshold, a score or a trading rule, or make or change a rule. Accepting
  or refusing, as a standard, a measured coin channel on exam cards under
  RULES 9 counts as a rule: the second-, third-, fifth- and sixth-fix
  verdicts reserved exactly that case for the user, and REVIEW-5 §4 and
  REVIEW-6 §3 named it.
- Where a reasonable reading puts a part on either side, I still class it
  (this instruction requires it), give my reasons, and name the other side.
- A part is not kept as a juror question if removing the outside options
  leaves it with one option: a question with one answer is not a question
  (test (iii) would fail).

## A part that stays a juror question

Must pass every test REVIEW-6's criteria list: (i)–(v) as REVIEW-3 §5 states
them; (vi) as REVIEW-4's criteria fix it (L1 / L2 / L3; fails only if it
leans and is not needed); coupling; deletion; determinacy as REVIEW-5 §2,
§4 and REVIEW-6 §2.1 applied (ii); reading lists. Stated test by test.

## A part that goes to the user

Written in `exam-prep/USER-QUESTIONS.md`. It must:

1. be followable by a reader who has not seen `exam-prep/`: no identifier,
   file or term is used without being explained in the same file;
2. state what must be decided, which written rule it touches, and why it is
   a rule question rather than a definition — and, because REVIEW-5 and
   REVIEW-6 called it contested, the opposite case too;
3. state what each possible answer would mean for the exam, and each answer
   must be **determinate** in REVIEW-6 §2.1's sense: the run that composes
   the gate's row can carry it out without a further choice that changes
   the numbers (a named stop that refers back is allowed, as REVIEW-5 §5
   and REVIEW-6 §1 accepted for the gate);
4. **recommend nothing**: no answer is given a reason the others lack
   (REVIEW-4's L3, applied to the user's text); no earlier choice on the
   open point is given as a ground (REVIEW-6 §2.2's L2 finding, applied);
5. carry **no measured figure** and no measured effect of any answer
   (RULES 6; REVIEW-4's L1, applied), and say that this is deliberate;
6. quote rule text exactly, with its file and line, checked by script.

## The index

Shows each row's true status, including the ratified JQ-N1 group; carries no
wording, options or numbers of any question (rule numbers, part letters and
SHA-256 values only, as before); the sixth-fix version is kept byte for byte
and every earlier version stays where it was (checked by hash).

## Nothing claimed earlier disappears (RULES 29–30)

`VERDICT.md`, `HANDED-FORWARD.md` and `exam-prep/README.md` are appended to,
never edited above their pre-run length (checked: prefix hash equals the
pre-run file hash). The JQ-R04-CONTENT-d file is kept unchanged. Every file
in the pre-run snapshot is unchanged at the end, except the appended ones
and the index (checked by script). Check records are append-only: a
different content under an existing run number stops the script.

No threshold, score or trading rule is introduced anywhere.
