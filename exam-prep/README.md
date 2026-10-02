# `exam-prep/` — the ground prepared before any exam card exists

Mateo · data engineer · 2026-09-19 (system clock, RULES 23)

This folder holds the working behind two problems the canteen measured and
stopped at: **R-04**, whether the exam is blind at all, and **N-1**, collapsing
cards that share a clock hour into one event before anything is counted.

Nothing here is a trading rule, a threshold in a score, or an interpretation of
a card. It is instruments and measurements.

## Read in this order

| file | what it is |
|---|---|
| `VERDICT.md` | solved or not solved, for each problem. Says nothing about how. |
| `R-04-blindness.md` | the blindness standard, what the raw card leaks, what the blinding closes, what it cannot close and why, and the acceptance gate the exam-building run must run |
| `N-1-collapse.md` | the collapse standard, the readings of RULES 13 that the rules allow, what each counts, what collapsing does to a chance line, and the open question left for three jurors |
| `decisions-and-open-questions.md` | ten decisions I took that the instruction did not cover, five questions I refused to answer, and the steer check on my own instruction |
| `FINGERPRINTS.md` | SHA-256 of every file in this folder except the card files, and of the five scripts |

## The measured output

| folder | what is in it |
|---|---|
| `collapse/` | `events.csv` (every card's event under every configuration), `collapse-summary.csv`, `shuffle-calibration.csv`, `collapse-manifest.md`, `runs/` |
| `identity/` | one audit per card set — raw and four blinded configurations — plus the hour-linkage tables, the residual diagnostic, and `runs/` |
| `blind-proof/<variant>/` | 306 blinded cards, the truth file that lets the audit attack them, the blinding manifest and `runs/` |

The blinded cards in `blind-proof/` are blinded copies of the **observation**
cards. They are a proof that the instrument works and a fixture the reviewer
can attack. **They are not exam cards** and no exam card exists yet.

## The instruments

| script | what it does |
|---|---|
| `scripts/lab_cards.py` | reads a card — raw or blinded — into a plain dict |
| `scripts/15_event_collapse.py` | the collapse engine, the cluster-level shuffle, the chance line that refuses to run without an event map |
| `scripts/16_identity_audit.py` | three de-anonymisation attacks with permutation chance lines |
| `scripts/17_blind_cards.py` | the blinding transform, configurable, with its own guards |
| `scripts/18_residual_diagnostic.py` | where the leftover coin signal on a blinded set comes from |

Every one of them writes an append-only run record (RULES 29, 30), reads the
system clock rather than guessing it (RULES 23), and records free disk space.
Every constant is defined at the top of its file with the rule or the document
it came from.

## What this run did not touch

`exam/` — not read, not written. `decisions/`, `instructions/`, `LEDGER.md`,
`reports/` — not read. Nothing outside the Balıkçıl folder was read, with any
tool or from the command line.

---

## Addendum · second-fix run, 2026-10-01

Appended by Mateo (second-fix run); nothing above was changed. After the
review (`REVIEW.md`), a second run acted on it. Read, in this order:
`VERDICT.md` (its appended section), `JUROR-QUESTIONS.md`,
`second-fix/SECOND-FIX.md`, `second-fix/criteria-written-before-measuring.md`,
`second-fix/juror-questions/`, `second-fix/checks/`,
`second-fix/FINGERPRINTS.md`. New outputs live in `second-fix/` and in
`collapse/run-756cf4ea156d92c3/`; nothing written by the first run was
overwritten.

---

## Addendum · third-fix run, 2026-10-01

Appended by Mateo (third-fix run); nothing above was changed (its first 3,605
bytes still hash to `c704496b…9d375`). After the second review
(`REVIEW-2.md`), a third run acted on it. Read, in this order: `VERDICT.md`
(its last appended section), `JUROR-QUESTIONS.md` (re-issued; the earlier
index is kept at `third-fix/JUROR-QUESTIONS-as-of-second-fix.md`),
`HANDED-FORWARD.md` (what the exam-building run and the judge's script must
do), `third-fix/THIRD-FIX.md`, `third-fix/criteria-written-before-measuring.md`,
`third-fix/juror-questions/`, `third-fix/checks/`, `third-fix/FINGERPRINTS.md`.
New outputs live in `third-fix/` and in `collapse/run-bec532fa008e0e01/`;
nothing written by an earlier run was overwritten.

---

## Addendum · fourth-fix run, 2026-10-01

Appended by Mateo (fourth-fix run); nothing above was changed (its first
4,375 bytes still hash to `4daca76f…032a`). After the third review
(`REVIEW-3.md`), a fourth run acted on it. Read, in this order: `VERDICT.md`
(its last appended section), `JUROR-QUESTIONS.md` (re-issued; earlier
versions kept), `HANDED-FORWARD.md` (**its last section only**: it is
complete), `fourth-fix/FOURTH-FIX.md`,
`fourth-fix/criteria-written-before-measuring.md`,
`fourth-fix/juror-questions/`, `fourth-fix/checks/`,
`fourth-fix/FINGERPRINTS.md`. New outputs live in `fourth-fix/`; nothing
written by an earlier run was overwritten.

---

## Addendum · fifth-fix run, 2026-10-01

Appended by Mateo (fifth-fix run); nothing above was changed (its first
5,042 bytes still hash to `03225075…69fc`). After the fourth review
(`REVIEW-4.md`), a fifth run acted on it. Read, in this order: `VERDICT.md`
(its last appended section), `JUROR-QUESTIONS.md` (re-issued; earlier
versions kept), `HANDED-FORWARD.md` (**its fourth-fix and fifth-fix sections
together**: the fifth-fix section replaces A-0.1, A-0.4 and B-1 and adds
C-5), `fifth-fix/FIFTH-FIX.md`, `fifth-fix/criteria-written-before-correcting.md`,
`fifth-fix/juror-questions/`, `fifth-fix/checks/`, `fifth-fix/FINGERPRINTS.md`.
New outputs live in `fifth-fix/` and in `scripts/32_juror_file_check_fifth.py`;
nothing written by an earlier run was overwritten, apart from
`JUROR-QUESTIONS.md`, whose earlier version is kept at
`fifth-fix/JUROR-QUESTIONS-as-of-fourth-fix.md`.

---

## Addendum · sixth-fix run, 2026-10-01

Appended by Mateo (sixth-fix run); nothing above was changed (its first
5,937 bytes still hash to `f25a710f…acbb`). After the fifth review
(`REVIEW-5.md`), a sixth run acted on it for the DATE and CONTENT rows only.
Read, in this order: `VERDICT.md` (its last appended section),
`JUROR-QUESTIONS.md` (re-issued; earlier versions kept; it now states the
order in which the juror groups sit), `HANDED-FORWARD.md` (**its fourth-fix,
fifth-fix and sixth-fix sections together**: the sixth-fix section replaces
A-0.1 and C-5 and adds A-0.7 and A-0.8), `sixth-fix/SIXTH-FIX.md`,
`sixth-fix/criteria-written-before-correcting.md`,
`sixth-fix/juror-questions/`, `sixth-fix/checks/`,
`sixth-fix/FINGERPRINTS.md`. New outputs live in `sixth-fix/` and in
`scripts/33_juror_file_check_sixth.py`; nothing written by an earlier run was
overwritten, apart from `JUROR-QUESTIONS.md`, whose earlier version is kept
at `sixth-fix/JUROR-QUESTIONS-as-of-fifth-fix.md`.

---

## Addendum · seventh-fix run, 2026-10-01

Appended by Mateo (seventh-fix run); nothing above was changed (its first
6,936 bytes still hash to `923ec68d…d322`). After the sixth review
(`REVIEW-6.md`), a seventh run acted on it for JQ-R04-CONTENT-d only, and
corrected the index's statuses. Read, in this order: `VERDICT.md` (its last
appended section), `USER-QUESTIONS.md` (new: questions for the user, not for
jurors), `JUROR-QUESTIONS.md` (re-issued; earlier versions kept),
`HANDED-FORWARD.md` (**its fourth-fix, fifth-fix, sixth-fix and seventh-fix
sections together**: the seventh-fix section replaces A-0.1, C-5 and step 1
of A-0.4), `seventh-fix/SEVENTH-FIX.md`,
`seventh-fix/criteria-written-before-correcting.md`, `seventh-fix/checks/`,
`seventh-fix/FINGERPRINTS.md`. New outputs live in `seventh-fix/`, in
`USER-QUESTIONS.md` and in `scripts/34_seventh_fix_check.py`; nothing written
by an earlier run was overwritten, apart from `JUROR-QUESTIONS.md`, whose
earlier version is kept at `seventh-fix/JUROR-QUESTIONS-as-of-sixth-fix.md`.

---

## Addendum · eighth-fix run, 2026-10-02

Appended by Mateo (eighth-fix run); nothing above was changed (its first
7,990 bytes still hash to `0f884ca1…502a`). After the seventh review
(`REVIEW-7.md`), an eighth run wrote JQ-R04-CONTENT-d again as a juror
question, marked U-1 superseded, and corrected the index. Read, in this
order: `VERDICT.md` (its last appended section), `JUROR-QUESTIONS.md`
(re-issued; earlier versions kept), `USER-QUESTIONS.md` (U-1 marked
superseded; text kept), `HANDED-FORWARD.md` (**its fourth-fix to eighth-fix
sections together**: the eighth-fix section replaces A-0.1, step 1 of A-0.4
and C-5, and adds A-0.9), `eighth-fix/EIGHTH-FIX.md`,
`eighth-fix/criteria-written-before-correcting.md`,
`eighth-fix/juror-questions/`, `eighth-fix/checks/`,
`eighth-fix/FINGERPRINTS.md`. New outputs live in `eighth-fix/` and in
`scripts/35_eighth_fix_check.py`; nothing written by an earlier run was
overwritten, apart from `JUROR-QUESTIONS.md` and `USER-QUESTIONS.md`, whose
earlier versions are kept at `eighth-fix/JUROR-QUESTIONS-as-of-seventh-fix.md`
and `eighth-fix/USER-QUESTIONS-as-of-seventh-fix.md`.
