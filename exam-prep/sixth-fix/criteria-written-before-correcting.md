# Sixth-fix run — criteria written before correcting

Mateo · data engineer · sixth-fix run · first clock read 2026-10-01T22:50:55Z;
this file written after the clock read 2026-10-01T22:59:50Z (system clock,
RULES 23) and before any juror file, the index, `VERDICT.md` or
`HANDED-FORWARD.md` was changed. Free disk at 22:59:50Z: 12,384,276,480
bytes. Nothing is downloaded by this run.

By this time I had read: `RULES.md`, `TACTICS.md`; `exam-prep/REVIEW-5.md`,
`exam-prep/review-5/criteria-written-before-ruling.md`,
`exam-prep/review-4/criteria-written-before-ruling.md`, REVIEW-3 §5 (tests,
what must change, couplings) and §8, REVIEW-2 §5 and §6,
`exam-prep/JUROR-QUESTIONS.md`, `exam-prep/VERDICT.md` (whole),
`exam-prep/fifth-fix/FIFTH-FIX.md`, its criteria file, the fifth-fix
JQ-R04-DATE and JQ-R04-CONTENT files, `HANDED-FORWARD.md` (headings, the end
of the fourth-fix section and the fifth-fix section),
`exam-prep/third-fix/juror-questions/JQ-R04-GATE.md` lines 1–161,
`decisions/2026-10-01-jq-r04-gate/verdict.md`; `scripts/29_identity_audit_exact.py`
(lines 1–172 and 217–450); `canteen/2026-09-19-sofia.md` lines 108–122,
218–272, 662–673; one blinded observation card
(`exam-prep/review-2/rerun/blind-k1/cards/B001.md`, lines 1–45); and a `grep`
of the fifth-fix JQ-N1 and JQ-CANTEEN-8 files and the GATE file for paths to
`exam-prep/`, reviews, working files and scripts (read only; not changed).

A snapshot of the SHA-256 of every file under `exam-prep/` was taken before
anything was written: `exam-prep/sixth-fix/pre-run-fingerprints.txt`.

## 0 · Scope

This run acts on `REVIEW-5.md` as it concerns the DATE and CONTENT rows. It
does not change the JQ-N1 or JQ-CANTEEN-8 files (three jurors are answering
them), the JQ-R04-GATE file or its verdict (ratified), or any earlier file.
Corrected files are new files under `exam-prep/sixth-fix/juror-questions/`.

## 1 · The tests every DATE, CONTENT (and new) row is held to

A row to be commissioned is **fit** only when it passes all of:

- **(i)–(v)** — REVIEW-2's tests as REVIEW-3 §5 states them: (i) a juror
  reading only the files its row names can answer it; (ii) every outcome it
  offers can follow from the instrument or rule it is about; (iii) its
  wording does not lean; (iv) it is inside RULES 33; (v) no number is shown
  to a juror as measured that the instrument does not support, or that is
  not what the file says it is.
- **(vi)** — exactly as `exam-prep/review-4/criteria-written-before-ruling.md`
  fixes it (L1 effect of an option, L2 precedent, L3 one-sided argument; an
  item fails only when it leans **and** is not needed). A shared section
  fails every row that reads it.
- **(vii)** — no contradiction with the ratified JQ-R04-GATE verdict, in the
  sense of the same criteria file; a sentence that tells jurors what happens
  to a field after their answer must be true under the ratified verdict, or
  say where that is decided.
- **(viii) coupling** — REVIEW-4's criteria / REVIEW-3 §5: no row in a
  coupled group can be answered by choosing by the combined effect on
  whether material passes. Applied as REVIEW-3 §5 and REVIEW-5 §3 applied
  it: jurors who decide what the gate grades (or how a grading condition is
  defined) do not also choose which fields or renderings stay.
- **(ix) deletion** — REVIEW-5's criteria: a passage removed is gone;
  nothing left points at it; a premise it supplied, if still needed, is
  still supplied.
- **(x) pointers** — this run's instruction, item 3: no juror file of these
  rows names, in its header or anywhere else, a review, `VERDICT.md`,
  `HANDED-FORWARD.md` or a working file (any `*-FIX.md`, criteria file,
  manifest, check, probe, run record or run number, or a folder of them).
  A file path may appear only for a file on the row's own reading list, for
  `RULES.md` / `TACTICS.md` / the canteen book, and for the ratified verdict
  `decisions/2026-10-01-jq-r04-gate/verdict.md`, which is quoted. The
  provenance removed from juror files is kept for reviewers in
  `exam-prep/sixth-fix/SIXTH-FIX.md`.

I add no test beyond (x), which the instruction adds.

## 2 · How corrections are made

1. A corrected file is written from the fifth-fix file of the same name;
   every change is named in `SIXTH-FIX.md` with the REVIEW-5 item or the
   instruction item it answers. The fifth-fix files are not touched.
2. **No new measured number.** Every figure in a corrected or new file must
   be in the fifth-fix DATE or CONTENT file. Allowed besides: line numbers
   of a passage quoted for the first time, each checked by script; rule and
   blocker identifiers; counts read from the audit's code (how many
   features a family holds), checked by script; the run's date line.
3. A choice that changes the numbers and that no written rule settles is not
   settled by me (RULES 33). If it must be answered before a group can be,
   it is written as a juror question answered **before** that group sits,
   and the index says so (this run's instruction).
4. Where REVIEW-5 rules a coupling fails, the reviews' ruling governs (this
   run's instruction withdraws the earlier "in the group it bears on").

## 3 · The index

- No wording, option or number of any question. Digits only inside
  identifiers, file paths, line ranges of a reading list, SHA-256 values,
  and the dates of its own history lines.
- Every row shows its true status; the order in which groups must sit is
  stated, by identifier only, in words.
- Reading lists name no review, `VERDICT.md`, `HANDED-FORWARD.md` or
  working file; they name the group's current juror files, `RULES.md`,
  `TACTICS.md`, the canteen book by line ranges only, and (where a row needs
  an earlier group's outcome) only that outcome's ratification sentence.
- Every earlier version is kept byte for byte and named with its SHA-256.

## 4 · What counts as done

Every REVIEW-5 item that concerns the DATE or CONTENT rows gets one of:
done; referred to jurors (identifier); handed forward (item); referred to
the coordinator (reason); recorded (nothing required); cannot be done
(error). The checks of §1 (x), §2.2 and §3 that a script can make are made
by `scripts/33_juror_file_check_sixth.py`, with an append-only record
(RULES 29–30), and quoted with its run number. The judgement tests (iii),
(vi), (viii) are mine and are stated row by row; a reviewer may draw the
line elsewhere.

No threshold is introduced anywhere.
