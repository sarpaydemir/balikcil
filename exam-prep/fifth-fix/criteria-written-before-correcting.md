# Fifth-fix run — criteria written before correcting

Mateo · data engineer · fifth-fix run · written 2026-10-01, after the clock
read 2026-10-01T22:25:48Z (system clock, RULES 23) and before any juror file
was changed. Free disk at that read: 12,392,706,048 bytes. Nothing is
downloaded by this run.

By this time I had read: `RULES.md`, `TACTICS.md`, `exam-prep/REVIEW-4.md`,
`exam-prep/review-4/criteria-written-before-ruling.md`,
`decisions/2026-10-01-jq-r04-gate/verdict.md`, `exam-prep/JUROR-QUESTIONS.md`,
`exam-prep/README.md`, the fourth-fix and third-fix sections of
`exam-prep/VERDICT.md` (third-fix only its "What R-04's closure depends on"),
the fourth-fix section of `exam-prep/HANDED-FORWARD.md`, the four fourth-fix
juror files, `exam-prep/third-fix/juror-questions/JQ-R04-GATE.md`, REVIEW-3
§5's list of tests, the family definitions of
`scripts/29_identity_audit_exact.py` (lines 1–130, 395–445, 715–745 and the
feature names of `card_features()`), and `canteen/2026-09-19-sofia.md`
lines 108–122, 218–272, 660–675 and its heading list.

A snapshot of the SHA-256 of every file under `exam-prep/` and `scripts/`
(except `exam_*` scripts, which this run may not look at, and bytecode) was
taken before anything was written: `exam-prep/fifth-fix/pre-run-fingerprints.txt`.

## 1 · The tests every juror row is held to

A row that is to be commissioned is **fit** only when it passes all of:

- **(i)–(v)** — REVIEW-2's five tests as REVIEW-3 §5 states them: (i) a juror
  reading only the files its row names can answer it; (ii) every outcome it
  offers can follow from the instrument or rule it is about; (iii) its
  wording does not lean; (iv) it is inside RULES 33; (v) no number is shown
  to a juror as measured that the instrument does not support, or that is
  not what the file says it is.
- **(vi)** — the fourth review's test, applied exactly as
  `exam-prep/review-4/criteria-written-before-ruling.md` fixes it (L1 effect
  of an option, L2 precedent, L3 one-sided argument; an item fails only when
  it leans **and** is not needed). I do not re-define it.
- **(vii)** — no contradiction with the ratified JQ-R04-GATE verdict, in the
  sense of the same criteria file ("Contradiction with the ratified
  JQ-R04-GATE verdict"); a consequence sentence that tells jurors what
  happens to a field after their answer must be true under the ratified
  verdict, or say where that is decided.

## 2 · How corrections are made

1. Each correction REVIEW-4 §2 lists is made as the deletion it names. A
   corrected file is a copy of the fourth-fix file with those passages
   removed; it is written to `exam-prep/fifth-fix/juror-questions/`, and the
   fourth-fix file is not touched.
2. An edit REVIEW-4 does not list is made only when (a) a listed deletion
   leaves a sentence pointing at something that is no longer there, or
   (b) the defect REVIEW-4 names exists, by the same test, in a passage or
   row REVIEW-4 did not name. Every such edit is named in
   `exam-prep/fifth-fix/FIFTH-FIX.md` with its reason (RULES 32).
3. **No new number.** Every number in a corrected file must already be in
   the fourth-fix file of the same name, apart from (a) line numbers of a
   passage quoted for the first time, each checked by script against the
   cited lines, and (b) the run's own date line. A new question part carries
   **no measured figure at all**.
4. A choice that changes the numbers and that no written rule settles is not
   settled by me or by the coordinator alone (RULES 33): it is written as a
   juror question in the group it bears on, held to §1, and added to the
   index.

## 3 · The index and the reading lists

- The index names no wording, option or number of any question. Digits may
  appear only inside identifiers, file paths, line ranges of a reading list,
  SHA-256 values, and the dates of its own history lines.
- Every row shows its true status. Earlier versions are kept byte for byte
  and named with their SHA-256.
- A reading list names no file that states measured effects of options, no
  review, not `VERDICT.md`, not `HANDED-FORWARD.md`, and no working file
  (`*-FIX.md`, criteria files, checks, probes, runs). It names only the
  current juror files of its group, the root rule files, and the canteen
  book **by the line ranges its juror files cite**.
- A juror file's own "What you open" section and its index row name the same
  files.

## 4 · What counts as done

Every numbered item of REVIEW-4 gets one of: done; referred to jurors (with
the identifier); handed forward (with the HANDED-FORWARD item); referred to
the coordinator (with the reason); cannot be done (with the error).
The checks of §2–§3 are run by a script with an append-only record
(RULES 29–30), and their result is quoted with the run number.
