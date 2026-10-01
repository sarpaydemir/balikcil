# Review 7 — criteria, written before ruling

Mateo · data engineer, reviewing posture · written 2026-10-01, after
2026-10-01T23:46:17Z (system clock, RULES 23).

Written after opening, to know what is under review: `RULES.md`,
`TACTICS.md`, `exam-prep/README.md`, `exam-prep/JUROR-QUESTIONS.md`,
`exam-prep/USER-QUESTIONS.md`, `exam-prep/REVIEW-6.md`, and the three
verdicts the instruction names. Written **before** opening
`exam-prep/seventh-fix/` (SEVENTH-FIX, its criteria, its checks), the
seventh-fix section of `HANDED-FORWARD.md` or `VERDICT.md`, the withdrawn
`JQ-R04-CONTENT-d` file, and before running any check or probe.

## Item 1 · Whose question

- **Jurors** if every answer the row offers only reads a definition or a
  procedure: it sets no threshold or score, makes no trading rule, and
  changes nothing in `RULES.md` (RULES 33, lines 119–121), nor what TACTICS
  says is on or hidden from the card.
- **User** if an answer, once carried out, would decide what RULES 9 (or
  TACTICS 6) requires of an exam, or change a rule (lines 3–4).
- **Split** if some part is a definition jurors may decide and some part is
  not. I name each part by identifier only.
- I rule on what the text of the rules says, not on what result an answer
  would give. I measure no option effect.

## Item 2 · Fit to be put to the user — six tests

- **(F1) Self-contained.** A reader who has not opened `exam-prep/` can
  follow it: every term used is explained in the file or quoted.
- **(F2) True.** Every statement of fact is true of the files and code as
  they stand at my clock read; every citation (file and line) contains what
  the file says it contains. Checked by a script, quotation by quotation.
- **(F3) Complete.** It offers every answer the written rules leave open,
  including "Other" and "this is not yours".
- **(F4) No lean.** No figure, passage, precedent, order or emphasis favours
  one answer: each answer's consequence stated with matching weight; no
  answer described only by its costs; no earlier review's preference shown
  unless answered on the other side and needed.
- **(F5) No result (RULES 6).** It carries no measured result — on
  observation or exam cards — from which the user could tell which answer
  passes the gate, and points to no file where the result is, unless the
  pointer is needed and stated neutrally.
- **(F6) Carried out.** Each answer can be composed into a graded set by
  the run that builds the gate without a further choice that changes the
  numbers; where a choice remains, the file says who makes it.
- A fault fails the file if it would lead the user to a wrong belief, or
  lean, or leave an answer impossible to carry out. A wording blemish that
  does none of these is noted, not ruled.

## Item 3 · Handed forward

Each step the seventh-fix section of `HANDED-FORWARD.md` adds or replaces is
checkable yes/no by the run that must meet it: it names what is checked, on
which file, and what counts as met, without a judgement left to that run.

## Item 4 · Index

- Each row's status matches the files I may read (the three verdicts, the
  question files, `USER-QUESTIONS.md`), at my clock read.
- The index carries no wording, option or number of any question (its own
  lines 24–25 promise this). I check by script against the question files.
- What I cannot see (the rest of `decisions/`) I name as not seen, and do
  not turn into "no problem".
