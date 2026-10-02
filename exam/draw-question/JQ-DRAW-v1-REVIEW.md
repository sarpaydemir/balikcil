# JQ-DRAW · Review before any juror sits

**Reviewer:** data-engineer, Mode B, reviewing posture. I did not write `JQ-DRAW.md`.
**Clock (system, UTC):** 2026-10-02T00:14:32Z, read during the review.
**File reviewed:** `open-questions/JQ-DRAW.md`, SHA-256
`56dcaa89c983010f39ea9cf46869314abe5f332cb299ef82799e048aa654e97c` (read at the start of
the review and again just before this file was written; it was the same both times).

Line numbers below are the reviewed file's own line numbers unless another file is named.
This review does not say which outcome is right, and it proposes no outcome.

---

## 1 · Is the draw unsettled?

**Open, within everything I was allowed to read.**

Where I looked:

- `TACTICS.md` §6 lines 99–100: this gives the counts (400; 200 and 200) and the source
  (the exam coins). It says nothing about which moments are chosen when the pool holds more.
- `TACTICS.md` §2 lines 33–44: this defines how moments are found for each coin. Line 42 ("chosen at
  random") applies to how the pool's calm moments are found. It does not cover a later
  choice of cards from the pool.
- `TACTICS.md` §1 line 22: this names the draw number for "the draw" of §1, which is the coin draw.
  It does not say that the number also seeds any later draw.
- `TACTICS.md` §4 line 78: "all the cards of the 10 coins". This applies to observation and has no
  counterpart for the exam.
- `RULES.md` 6, 9, 13, 33–35; `README.md` lines 32–45; `TEAM.md` lines 67–74 (Nadia),
  111–119 (jurors).
- The ten verdicts I may read: `decisions/2026-09-19-*/verdict.md` (7 files),
  `decisions/2026-10-01-jq-n1-canteen-8/verdict.md`,
  `decisions/2026-10-01-jq-r04-gate/verdict.md`,
  `decisions/2026-10-01-jq-r04-carries/verdict.md`. All ten begin `RATIFIED`. None of them decides
  how exam cards are chosen from the pool. `2026-09-19-large-moment-selection` and
  `2026-09-19-calm-separation` decide how the pool is formed. `jq-n1-canteen-8` decides how
  cards that share an hour are counted.

The pool's own report says the same thing (`exam/moments/pool-report.json`, key
`not_done_here`). It is a working file and is recorded here only as a cross-check.

I could not exclude the following (see §6): `LEDGER.md` may record a user decision on this, and the
verdict in `decisions/2026-10-01-jq-r04-date-content/` may touch it. I may read neither.

---

## 2 · Fit per part

Standards: (S1) answerable from what it names, the four root documents and the ratified
verdicts; (S2) every outcome can follow as stated, with no further unstated choice that
changes the numbers; (S3) leans toward no answer, and every figure is needed and correct;
(S4) offers "settled" and "outside"; (S5) inside RULES 33; (S6) points a juror at no working
file, script, run output or review.

| part | S1 | S2 | S3 | S4 | S5 | S6 | overall |
|---|---|---|---|---|---|---|---|
| JQ-DRAW-a (lines 52–65) | **not fit** | fit | fit | fit | fit | **not fit** | **not fit** |
| JQ-DRAW-b (lines 67–81) | fit | **not fit** | **not fit** | fit | fit | fit | **not fit** |
| JQ-DRAW-c (lines 83–94) | fit (open item C3) | **not fit** | **not fit** (in §7) | fit | fit | fit | **not fit** |

Faults in sections that are not parts:

| section | fault | standard |
|---|---|---|
| §3 preamble, lines 49–50 | F-ORDER | S3 (correctness) |
| §4, lines 113–117 | F-CONV, F-COMB | S2 |
| §5, lines 121–123 | open item (see §6 below) | S1 |
| §7, lines 136–215 | F-LEAK, F-FACTS, F-ARG, F-SCRIPT | S3, S6, identification |

### Part a

**A1 (S1, S6) · the measure behind lines 58–59.** The outcome at lines 58–60 ranks by "the way
`TACTICS.md` §2 measured it when it found the moment". `TACTICS.md` §2 (lines 33–44) states
no measure. It says only "rose or fell the most within 24 hours" on hourly closes. The measure
was fixed by a script reading, in `scripts/06_find_moments.py`, docstring lines 13–17: the
close-to-close simple return, ranked by its absolute value. A juror cannot learn from the files
the question names what this outcome ranks by. The sentence attributes to a root document
something the document does not say, and the content of the outcome rests on a script that the
file does not name.

Measured: with a different measure that §2's words also allow (the absolute log return over the
same window), the top 200 of the pool's 339 large-movement moments differ in **8 of 200**
moments. The measure is therefore a choice that changes the numbers.

The other outcomes in part a are fit on every standard. On its own, each listed outcome can be
carried out.

### Part b

**B1 (S2) · dependence on part a.** The outcome at lines 71–73 takes its per-coin counts from
"as part a gives it". If part a's ratified outcome is "Outside", it supplies no per-coin
counts. If it is "Settled" or "Other", it may supply none. In those cases the outcome cannot be
carried out without a further choice. Lines 117, 153–154 and 161 say every combination can be
carried out, and that is not true for these combinations.

**B2 (S3) · the list against the file's own rule for what is listed.** Lines 177–179 give the
rule for leaving a procedure unlisted: it would need an allocation rule or a number that is
supplied nowhere. Part a and part b are not built the same way. Part a lists a procedure that
draws nothing at random. Part b lists only procedures that draw at random. The stated rule does
not explain this difference. Either the list in part b, or the rule as stated at lines 177–179,
must change so that the two agree. I do not say which.

### Part c

**C1 (S2) · conditional on each juror's own answers.** Lines 85–88 condition part c on "your
answers to parts a and b". Each part is counted separately, so the ratified a and b can draw at
random while part c's ratified outcome is "Does not arise" or "Outside", which leaves no seed.
Part c can also split three ways because each juror answered it under a different condition.
The file does not say what happens in either case. This is the same fault as B1, and it falls
under the same false claim at lines 117 and 161.

**C2 (S3) · argument a juror reads.** Section 7 is part of the file a juror receives. Lines 173–176
give a reason why one part-c outcome is the natural one. A juror reads that reason before
answering, which is a lean by passage. The fix belongs in §7, not in part c's list.

**C3 (open item, not judged).** The number cited at line 89 has already seeded one random draw
while the pool was being made. `exam/moments/pool-report.json` key `seed`, and
`scripts/exam_27_find_moments.py` lines 57 and 135, show that it seeded the selection of the pool's
calm moments. The file does not say this, and a juror cannot find it in the files the question
names. I do not judge whether a juror needs it, or whether stating it would itself lean. I list
it for the coordinator.

**C4 (S2, not measured).** Line 105 pins the generator to "Python 3 `random.Random(seed)`" with
no minor version. I ran Python 3.14.4 only. I did not check whether `sample` gives the same
output for the same seed on other Python 3 versions.

### Sections outside the parts

**F-ORDER (§3, lines 49–50).** The file says that outcomes with a short name are listed in
alphabetical order. The three fixed outcomes also carry short names in bold ("Settled",
"Outside", "Other"). They are listed last, which is not alphabetical among all named outcomes.
The sentence as written is not accurate.

**F-CONV (§4).** See §4 of this review. The mechanics change the numbers.

**F-COMB (§4 line 117; §7 lines 151–154, 161).** See B1 and C1.

**F-FACTS (§7).** Lines 139–140 and 165–166 say the only pool facts in the file are the two in
§1. The file states two more measured pool facts: line 104 (no two moments share start hour and
coin) and lines 149–150 (no two large-movement moments share a size). Both are true (§5 of this
review). The fact at lines 149–150 is not needed by any juror, because the tie rule is stated
anyway. The claim at lines 139–140 and 165–166 is not accurate.

**F-SCRIPT (§7, line 194 onward).** This text tells the juror that a script scanned the file and
that the source of the §1 facts went to the coordinator. It points at working output without
naming it. A juror who receives §7 also receives this.

**F-LEAK (§7, lines 200–202).** See §3 of this review.

---

## 3 · Anything that could identify an exam coin, a date or a price

**Coin: yes, lines 200–202,** read together with lines 194–198. Lines 194–198 say the scan looked
for every exam coin's symbol and base name, for date and time patterns and month names, and for
decimals. Lines 200–202 then name the two words matched "in other case". One of those words is
not a month name, a date pattern or a decimal. A reader can therefore infer that it is the base
name of an exam coin, and that names one of the 20 exam coins. I have not written the coin here.

**Date: no.** There are no date or clock patterns and no month names in date use. The only
lower-case month-word matches are the verb at lines 44, 63, 79, 92, 139 and 201. The draw number
is referred to by its line in `TACTICS.md` (line 89) and is not printed.

**Price: no.** There are no decimals and no price figures.

Method. I ran `scripts/exam_35_draw_question_check.py`, the author's check: 0 hits and 13
other-case matches. I also ran my own scan, which goes beyond the author's. It covered every
exam coin's project name, its search-hit names and ids, and each word of 4 or more letters in
those names, taken from `exam/data/external/coin-names.json`, matched as whole words in any
case. It found only ordinary words. One is a generic word that appears in a coin's project name
and in the file's own vocabulary (lines 5–202). The other is a common noun at line 197. Neither
identifies a coin from the file's text. The one identification above comes from the scan
description, not from a match.

---

## 4 · The author's conventions: do they change the numbers?

Per my instruction, a convention that changes the numbers is part of the question, not a
convention.

To avoid computing any part of the real exam draw, every random measurement below uses
**seeds 1–1000, not the draw number**. Each figure counts the moments that differ out of 200.

| author's choice (where) | changes the numbers? | measured |
|---|---|---|
| list order, start hour then coin (§4 step 1, line 103) | **yes** | against coin-then-hour order: 69–95 of 200 differ (median 82); identical in 0 of 1000 seeds |
| generator and method, `random.Random(seed)` with `sample` (§4 step 2–3, lines 105–108) | **yes** | against shuffle-then-take-first-200 with the same seed: 139 of 200 differ, in every seed tried |
| part a drawn before part b, one stream (§4 step 3, lines 107–108) | **yes** | against b drawn first: 69–95 of 200 large-movement moments differ (median 82) |
| coin-by-coin, ascending line number (§4 step 3, lines 109–111) | **yes** | against descending: 58–93 of 200 calm moments differ (median 77) |
| coin with `k = 0` skipped (line 111–112) | no | a zero-size `sample` consumes no randomness (checked) |
| tie rule for the size ranking (lines 59–60) | no | 339 distinct absolute sizes among 339 large-movement moments; the rule never acts |
| measure for the size ranking, "the way §2 measured it" (lines 58–59) | **yes** | against the absolute log return: 8 of 200 differ (see A1) |
| "Python 3" with no version (line 105) | not measured | see C4 |

Under the standard in my instruction, the four §4 mechanics and the size measure are part of the
question. Line 113 ("not an outcome of this question") and line 115 (a juror may raise them
only under "Other") treat them as conventions. I do not say how they should be put to jurors.

---

## 5 · Facts in the file, checked against `exam/`

| claim (line) | checked | result |
|---|---|---|
| more than 200 of each kind (21–22) | `exam/moments/moments.csv` | true: 339 large, 339 calm |
| every coin has as many calm as large (23–24) | same | true: 19 coins with moments, all equal; 1 coin with none of either kind (0 = 0) |
| coins referred to by line 1–20 (6) | `exam/draw/exam-coins.txt` | 20 lines, no header |
| no two moments share start hour and coin (104) | same | true |
| no two large-movement moments share a size (149–150) | same, at the 4-decimal values | true: 339 distinct |
| `TACTICS.md` lines 99–100, 22; RULES 33, 34; `TEAM.md` juror answer form (13, 89, 46, 130, 127) | root documents | lines and content match |
| part a never gives a coin more than it has; coin-matched totals 200 (151–154) | follows from the above | true for the listed random and size outcomes. Not true "under every part-a outcome" (B1) |

---

## 6 · What I could not do

- **`LEDGER.md`**: not read (forbidden in this review). A user decision on the exam draw could
  be recorded there. I cannot say whether one is.
- **`decisions/2026-10-01-jq-r04-date-content/verdict.md`**: not read (not on my list). §5 of
  the file (lines 121–123) sends jurors to every `verdict.md` whose first line reads `RATIFIED`.
  I cannot confirm whether this verdict is ratified, or whether it touches the draw.
- **`exam-prep/`, `instructions/`, `reports/`, `notes/`, `canteen/`, `cards/`, git history**:
  not read.
- **Other Python 3 versions**: not tested (C4).
- **Coordinator copy of the §1 facts' source** (line 191–192): not seen. I re-measured the facts
  from `exam/` instead.

---

## 7 · Choices I made that my instruction did not cover

- I used seeds 1–1000, and not the draw number, for every random measurement. This avoids
  computing any part of the real exam draw. Size-ranking comparisons are deterministic, and only
  counts of differing moments are written.
- I chose the absolute log return as the alternative measure in A1, and shuffle-then-take as the
  alternative method in §4. They are illustrations that the choice matters, not proposals.
- I ran `git status --short` once, to confirm that I had left no bytecode or stray files. It
  listed file names (not contents) under `exam-prep/` and `reports/` that were changed by others.
  I opened none of them.
- In this file I refer to outcomes by line number rather than restating them. This keeps the
  review from carrying the options forward.

## 8 · Fingerprints (SHA-256)

| file | SHA-256 |
|---|---|
| `open-questions/JQ-DRAW.md` (reviewed) | `56dcaa89c983010f39ea9cf46869314abe5f332cb299ef82799e048aa654e97c` |
| `exam/moments/moments.csv` | `8d5c42a4499f3dfa6f79417e51be1b5adb248a3a04e580c1dfddb5a238f7386a` |
| `exam/draw/exam-coins.txt` | `b92a2212c166dc61a6aed6f0533d4b9031924cb7f865d0687d748039c2a25f50` |
| `exam/moments/pool-report.json` | `08e49c4348e88cb367ae2e8ca71dcadd79a7b6d4bb8c62c55b24520e942462e3` |
| `exam/data/external/coin-names.json` | `c241e86ff876d1f92667a1545cfcc2decfc25e96a6b6ae882e9cea5df296dd92` |
| `scripts/exam_35_draw_question_check.py` | `d053ec246cc93b08a70c1350678c5c295c82df34575ddf19de94d53e2521644c` |
| `scripts/06_find_moments.py` | `c73447af580959f92915ca5ab291cf976afc23646ed746725397b627a6d924d0` |
