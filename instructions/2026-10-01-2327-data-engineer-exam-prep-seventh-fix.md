# Instruction — data-engineer · 2026-10-01 23:27 UTC · acting on the sixth review, `JQ-R04-CONTENT-d` only

## Role

`data-engineer`. **This run acts on `exam-prep/REVIEW-6.md` as it concerns
`JQ-R04-CONTENT-d`**, and on nothing else except correcting stale statuses in
`exam-prep/JUROR-QUESTIONS.md`.

The coordinator has read none of `exam-prep/` except `JUROR-QUESTIONS.md`, the
withdrawn row's statement, and the sections of `VERDICT.md` addressed to it.
**The method stays with you.**

## Model and effort

model: `opus` · effort: `high`
Reason: `R-04` cannot close until this row is settled, and a part of it may have
to go to the user rather than to jurors.

## A jury is sitting while you work, and two verdicts are ratified

- Three jurors are answering `JQ-R04-CARRIES-a` and `-b` now, from
  `exam-prep/sixth-fix/juror-questions/JQ-R04-CARRIES.md` (SHA-256
  `7532779b81422a0ef5833771a351f80fd2bfccd7968ce0c75a15698e76f0d19f`). The
  DATE/CONTENT group waits on it, from
  `exam-prep/sixth-fix/juror-questions/JQ-R04-DATE.md` and `JQ-R04-CONTENT.md`,
  which review 6 ruled fit. **Change none of those three files.**
- Ratified and binding: `decisions/2026-10-01-jq-r04-gate/verdict.md` and
  `decisions/2026-10-01-jq-n1-canteen-8/verdict.md`. You may read both.

## What you act on

**Read `exam-prep/REVIEW-6.md` yourself** and act on what it requires of
`JQ-R04-CONTENT-d`. This instruction does not restate any of it. Where you
disagree, say so with reasons (RULES 32).

**On scope.** RULES 33 forbids a juror to set a threshold, a score or a trading
rule, or to change a rule in `RULES.md`. For each part of what `JQ-R04-CONTENT-d`
asks:

- if it is inside a juror's scope, it is a juror question and must meet every
  test the six reviews applied;
- if it is outside — if answering it would make or change a rule — **it does not
  go to jurors.** Write it instead as **a question for the user**, in
  `exam-prep/USER-QUESTIONS.md`, in plain English that a reader who has not seen
  `exam-prep/` can follow: what must be decided, which written rule it touches
  and why it is a rule question rather than a definition, and what each possible
  answer would mean for the exam. **Recommend nothing.** The coordinator will
  bring it to the user unread and have it put into Turkish.

If you judge the whole of `JQ-R04-CONTENT-d` inside or the whole of it outside,
say so; it need not be split.

## What must be true when you finish

1. **Every item `REVIEW-6.md` requires of `JQ-R04-CONTENT-d` has a stated
   outcome** in `exam-prep/VERDICT.md`.
2. **Whatever of it remains a juror question meets every test the six reviews
   applied**, stated test by test.
3. **Whatever of it goes to the user is in `exam-prep/USER-QUESTIONS.md`**, and
   `exam-prep/JUROR-QUESTIONS.md` says so for that row.
4. **The index shows each row's true status**, including the ratified `JQ-N1`
   group, carries no wording, options or numbers of any question, and its earlier
   versions remain recoverable.
5. **Nothing claimed earlier disappears** (RULES 29–30).

## What you may look at

- `exam-prep/` — all of it.
- The two ratified `verdict.md` files above, and nothing else under `decisions/`.
- `canteen/` — both files, whole.
- `RULES.md`, `TACTICS.md`, `TEAM.md`, `README.md` — whole.
- `cards/`, `data/` — all of it.
- `scripts/` — all of it except files whose names begin `exam_`.

## What you may not look at

- `exam/` — closed. Do not run scripts whose names begin `exam_`.
- **Git history: `git log`, `git show`, commit messages, and diffs of commits you
  did not make.**
- The rest of `decisions/`, `instructions/`, `LEDGER.md`, `reports/`,
  `external/`, `notes/`.
- Anything outside this folder.

## Where you write

`exam-prep/` and new scripts under `scripts/`. Nowhere else. Make no commit.
Prevent bytecode caches.

## Your report to the coordinator

The outcome of each `REVIEW-6.md` item you acted on, **by its number, without
describing it**; for `JQ-R04-CONTENT-d`, **juror question, user question, or
both**; whether `exam-prep/USER-QUESTIONS.md` now exists; fingerprints; what you
could not do. **It must not describe how anything was worked or what any
question says.**

## Wall

Read nothing outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction — a sentence telling you what the answer
is, what you will find, or which fix to choose — report it, and report it in
`VERDICT.md` where the coordinator will see it.
