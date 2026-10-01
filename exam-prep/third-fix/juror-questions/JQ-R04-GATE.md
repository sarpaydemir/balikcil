# JQ-R04-GATE · Which statistic decides whether exam cards are blind enough to use?

Referred by: Mateo · data engineer · second-fix run · 2026-10-01 (system clock).
Corrected by: Mateo · third-fix run · 2026-10-01 (system clock) — the
description of the feature list the gate reads now says what the list is and
that it is not complete by construction; the dependence of the
nearest-neighbour score on card numbering is stated; the measured table shows
only audits on which every option gives the same result, and the reason for
referring no longer says which option would have passed earlier material.
Raised by the review of the first exam-preparation run (`exam-prep/REVIEW.md`
§3.3 and §3.6 item 1). **You do not need to open that file or anything else
under `exam-prep/`; what you need is quoted here.**

## What you open

- this file
- `RULES.md` (lines cited below)
- `TACTICS.md` (lines cited below)

## What you decide, and what you may not

You decide a **procedure** (RULES 33): which of two measurements, or which
combination of them, decides a pass/fail step that the exam-building run must
take before the answer key is sealed. You do **not** decide the chance line
(RULES 12 fixes it: 1,000 shuffles, the best 1%), a threshold, a score or a
trading rule, and you do not change a rule. You also do not decide which
features the audit reads; that is engineering, and it is described below so
that you know what the gate can and cannot see.

Give: your answer; the file and line it rests on, quoted (RULES 34); the
strongest case against your answer; your confidence, 1–5. "Other" is allowed,
with reasons. Listing an option is not recommending it.

---

## The rule text

- `RULES.md` line 41: "In the exam the coin name and the date are hidden."
- `RULES.md` lines 51–52 (RULES 12): "The chance line is not invented. The
  answers are shuffled 1,000 times, and the real result must fall inside the
  best 1%."
- `RULES.md` lines 34–35 (RULES 6): "The rule is written first, the result is
  opened second. A rule is not changed after looking at a result."
- `TACTICS.md` lines 101–107 (§6): the list of what is hidden on an exam card
  (coin name; date and time; the price itself, converted to a number starting
  from 100; the coin name inside announcements; the Wikipedia number; the date
  in the release calendar).

## The step whose wording is open

The first exam-preparation run wrote this step for the run that will build
the exam cards (its file `exam-prep/R-04-blindness.md` §8 step 3, quoted):

> Re-run `scripts/16_identity_audit.py` on the exam cards before the answer
> key is sealed … This is the acceptance gate … If `ALL-removable` beats its
> chance line on the exam cards, the cards are not blind and the gate has
> failed.

### What `ALL-removable` is

The audit turns what an exam candidate can see on a card into numerical
**features** (for example the typical level of a column, how many of its 24
values repeat, the smallest step between two printed prices), grouped into
families. `ALL-removable` is **every feature in the audit's current list**,
minus the families that must stay on the card because a frozen canteen rule
or TACTICS requires them. On the 306 observation cards, in the recommended
blinded version, it is **44 features**.

It is **not** "everything about a card that could identify its coin". It holds
only what has been written into the audit, and the list has grown as channels
were found: after the review of the first run, the repeat structure of
every column was added (the row went from 23 to 43 features), and one
channel measured afterwards — the smallest step between two printed prices
— was **outside the list** until the third-fix run added it (43 → 44). Nothing guarantees that
no other channel exists outside the list.

### The two attacks

The audit attacks `ALL-removable` in **two** ways, each against its own
RULES 12 chance line (labels shuffled 1,000 times, best 1%):

- **nearest neighbour** — for each card, find the most similar other card;
  count how often it is the same coin. It asks: *can a card be matched to its
  own coin?*
- **pair AUC** — over every pair of cards, how well similarity separates
  same-coin pairs from different-coin pairs (0.5 = no information). It asks:
  *does similarity carry coin information on average?*

One property of the nearest-neighbour attack you should know: when two other
cards are **exactly** equally similar to a card, the audit picks the one with
the lower card number, so where that happens the score depends on how the
cards are numbered. The audit now also prints a version that averages over
every such tie and does not depend on the numbering, with its own chance
line. On the `ALL-removable` row of the observation cards no card has an
exactly tied nearest neighbour, so the two versions are the same number
there.

The sentence says "its chance line" but there are two. **Which one decides?**

The same run's own standard, for single families of features (its "Level 1"),
required a family to fail **both** attacks; for the pooled row the gate uses,
it did not say.

## The options the wording leaves open

- **A** — the gate fails if the pair AUC beats its line.
- **B** — the gate fails if the nearest-neighbour score beats its line.
- **C** — the gate fails if **either** beats its line.
- **D** — the gate fails only if **both** beat their lines.
- **Other**, with reasons.

### An optional second part

Two cards of one coin whose 48-hour windows overlap print some of the same
hours, so they are near-copies of each other; RULES 13 (`RULES.md` lines
53–54) treats moments in the same hour as one event. **Should the
nearest-neighbour attack be forbidden from matching a card to a card that
shares clock hours with it?** Answer only if you think it bears on your
answer above.

## What has been measured — on the observation cards, not the exam cards

Nothing has been measured on exam cards. On the 306 observation cards, in
five blinded versions, with the audit as it stands after the third-fix run
(`ALL-removable`; sources: `scripts/16_identity_audit.py`, runs
named in the table, folder `exam-prep/third-fix/identity/`):

| blinded version | audit run | features in `ALL-removable` | nearest neighbour (its line) | pair AUC (its line) |
|---|---|---|---|---|
| `strict-flags` (the recommended one) | `e05144718b909704` | 44 | 0.4085 (0.1699) — beats | 0.5741 (0.5136) — beats |
| `strict` | `1f2ae3cf3a5b2044` | 44 | 0.4085 (0.1699) — beats | 0.5741 (0.5136) — beats |
| `rank` | `96f1d17e27b8afaf` | 47 | 0.4477 (0.1699) — beats | 0.5814 (0.5132) — beats |
| `ratio` | `12b07f79e74f0be7` | 40 | 0.4052 (0.1732) — beats | 0.6155 (0.5126) — beats |
| `strict-flags`, price at 3 decimals | `ded6a9caaf77d910` | 44 | 0.4346 (0.1765) — beats | 0.5770 (0.5137) — beats |

The number of features differs between versions because they print
different fields, and the audit drops a feature that has the same value on
every card of a set. On every row no card has an exactly tied nearest
neighbour, so both versions of the nearest-neighbour score give the number
shown.

On every one of these card sets **both** attacks beat their lines, so the
gate fails under A, B, C and D alike. **Your answer therefore cannot change
whether today's material passes.** It decides how a later exam-card set will
be judged.

Optional second part, measured on the recommended version (`strict-flags`):
forbidding time-overlapping neighbours moves the nearest-neighbour score
from 0.4085 to 0.3987 (line 0.1732; residual diagnostic run
`03bf5fc1560d1e33`, same folder).

## Why this is referred and not decided by the engineer

The sentence can be read four ways. On an earlier, shorter version of the
audit the four readings did **not** all give the same pass/fail on the
observation cards; which of them passed is deliberately not given here, so
that the choice is made on the wording and not on its result (RULES 6).
RULES 33 calls a wording that can be read more than one way, with readings
that change the outcome, an open question. The engineer has seen those
numbers; RULES 6 is the reason the choice should not be made by somebody who
has.
