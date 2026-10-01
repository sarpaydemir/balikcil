# JQ-R04-DATE · What does "the date is hidden" require of an exam card? — three parts

Referred by: Mateo · data engineer · second-fix run · 2026-10-01 (system clock).
Part a was first referred by the first exam-preparation run as its question
Q-2; parts b and c come from the review of that run (`exam-prep/REVIEW.md`
§3.4) and from this run. **You do not need to open anything under
`exam-prep/`; what you need is quoted here.**

## What you open

- this file
- `RULES.md` (lines cited below)
- `TACTICS.md` (lines cited below)

## What you decide, and what you may not

You decide a **definition** (RULES 33): what RULES 9's "the date is hidden"
and TACTICS 6's "the date and time" and "the date in the release calendar"
cover, for the three kinds of printed information below. You do **not** decide
how a field is masked if it must be (that is engineering, and it will be
measured), a threshold, a score or a trading rule, and you do not change a
rule.

These three parts should be answered by the same jurors who answer
JQ-R04-CONTENT (`exam-prep/second-fix/juror-questions/JQ-R04-CONTENT.md`),
because all of them read the same two texts — RULES 9 against the TACTICS 3
list of what is on a card — and separate answers could contradict each other.

For each part: your answer; the file and line it rests on, quoted (RULES 34);
the strongest case against your answer; your confidence, 1–5. "Other" is
allowed. Listing an option is not recommending it.

---

## The rule text

- `RULES.md` line 41 (RULES 9): "In the exam the coin name and the date are
  hidden."
- `RULES.md` lines 43–44 (RULES 10): "An agent sitting the exam cannot use
  tools and cannot read files."
- `TACTICS.md` lines 55–62 (§3, what is on the card): "price, volume, trade
  count, taker buy/sell pressure" … "bitcoin and ethereum, over the same
  hours" · "US release calendar (inflation, employment, rate decision)".
- `TACTICS.md` lines 101–107 (§6, what is hidden): "the coin name" · "the date
  and time" · "the price itself (converted to a number starting from 100)" ·
  "the coin name inside announcements" · "the Wikipedia number itself (given
  as a ratio to the coin's own average)" · "the date in the release calendar".

An exam card shows the 24 hours before a moment, hour by hour, with no
calendar date and no clock time printed.

---

## Part a · Columns that identify which clock hours a card covers

The bitcoin and ethereum columns (TACTICS 3 line 61) print the market's
hourly change. Two cards that cover the same clock hours print identical
values in them. Measured on the 306 raw observation cards: three identical
consecutive rows in these two columns tie together **243 of the 495** card
pairs that truly share an hour, with **0 false matches among 46,170** pairs
that do not (`scripts/16_identity_audit.py`, run `13d935bb5cf78346`, T3).

They do not print a calendar date. They let two cards be placed in the same
hours, and a reader who remembered market history could in principle place a
card in time; that has not been measured.

The first run removed these columns from its blinded cards and said it was
acting on a reading it could not settle alone.

**Question a.** Does RULES 9 ("the date … hidden") and TACTICS 6 ("the date
and time") require removing a printed column whose values identify which
clock hours a card covers, although it prints no date?

- **yes** — such a column is the date in another form.
- **no** — the date is hidden when no date or time is printed; TACTICS 3 puts
  the columns on the card and TACTICS 6 does not list them.

## Part b · Release names that identify a calendar day

TACTICS 6 (line 107) hides "the date in the release calendar"; the first run
strips calendar dates from the release line and keeps each release's name
and its offset in hours. Measured on the 306 blinded observation cards
(`scripts/16_identity_audit.py`, run `d70dd7b545bfce8a`, T4):

- **100 of 306** cards print at least one US release name; **30** distinct
  names occur.
- **11** of the 30 names occur on exactly one calendar day in this card set,
  and **13** cards carry one of them. The 11: Census of Fatal Occupational
  Injuries; Employer Costs for Employee Compensation; Employer-Reported
  Workplace Injuries and Illnesses (Annual); Labor Force Characteristics of
  Foreign-born Workers; Labor Market Experience, Education, Partner Status,
  and Health for those Born YYYY-YYYY for Biennial; Productivity and Costs by
  Industry: Wholesale Trade and Retail Trade; Productivity by State; Summer
  Youth Labor Force; Total Factor Productivity; Usual Weekly Earnings of Wage
  and Salary Workers; Work Experience of the Population (Annual).

The US release calendar is public. A reader who knows when such a release is
published could date the card from its name alone. **Whether an exam
candidate without tools (RULES 10) actually can has not been measured.**

**Question b.** Does hiding "the date in the release calendar" (TACTICS 6
line 107) cover a release *name* that, by itself, lets a reader with general
knowledge identify the calendar date?

- **yes** — the name is the date in another form, and must be masked.
- **no** — TACTICS 6 hides the printed date; TACTICS 3 puts the release
  calendar on the card, and its names are what it is.

## Part c · Hour offsets to releases with public clock times

The release line keeps each release's offset from the card's start, in hours
(for example "Producer Price Index (-7 h)"). Many US releases are published at
a fixed, public clock time. A reader who knows that time can then read the
clock hour of the card's start from the offset. Counted on the 306 blinded
`strict-flags` cards (a `grep` count; the command is in
`exam-prep/second-fix/SECOND-FIX.md` §6): **99** cards print at least one
release with an hour offset. How many of those releases have a fixed public
time, and whether a tool-less candidate knows it, has not been measured.

**Question c.** Does hiding "the date and time" (TACTICS 6 line 103) cover the
time of day that an hour offset to a release with a public clock time reveals?

- **yes** — the time of day is part of "the date and time", and the offset
  reveals it.
- **no** — the offset is relative; TACTICS 6 keeps relative information, and
  hides only what is printed as a date or a time.

---

## What follows from the answers, so you can see the stakes — not to steer

A "yes" to any part means the field must be masked or removed on exam cards;
how is engineering, and the result will be audited and reported. A "no" means
the field stays and is named in the exam manifest as a known channel. Neither
answer changes `RULES.md`.
