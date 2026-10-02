# JQ-DRAW version 2 · Review before any juror sits

**Reviewer:** data-engineer, Mode B, reviewing posture. I did not write either version of
`JQ-DRAW.md`, the first review, or the author's notes.
**Clock (system, UTC):** 2026-10-02T00:34:41Z at the start of the review; 2026-10-02T00:42:09Z
just before this file was written.
**File reviewed:** `open-questions/JQ-DRAW.md`, SHA-256
`4e521cd7d7c2355653cb4dd589786ffb933d030620514bb499be773e80da13a2` (read at the start and again
just before this file was written; the same both times, and the same as the author's notes name).

Line numbers are the reviewed file's own unless another file is named. "v1 review line N" means
`exam/draw-question/JQ-DRAW-v1-REVIEW.md`. Outcomes are referred to by line number, not restated.
This review does not say which outcome is right, and it proposes no outcome and no wording.

---

## 1 · Standards

The standards the laboratory's reviews have applied to juror questions, as my instruction lists them:

- **S1** answerable by a juror who reads only what the file names, the four root documents and the
  ten verdicts the jurors will be given;
- **S2** every outcome able to follow as stated, with no unstated choice that changes the numbers;
- **S3** leaning toward no answer by figure, passage, precedent, order, emphasis or space;
- **S4** every figure needed and correct;
- **S5** "already settled" and "outside what a juror may decide" offered as answers;
- **S6** inside RULES 33;
- **S7** pointing at no working file, script, run output or review.

## 2 · Fit per part

| part | S1 | S2 | S3 | S4 | S5 | S6 | S7 | overall |
|---|---|---|---|---|---|---|---|---|
| JQ-DRAW-a (lines 84–96) | fit | **not fit** (G1, G2) | fit | fit | fit | fit | fit | **not fit** |
| JQ-DRAW-b (lines 98–111) | fit (see G3) | **not fit** (G1, G2) | **not fit** (G3) | fit | fit | fit | fit | **not fit** |
| JQ-DRAW-c (lines 113–121) | fit | fit | fit (see §5, C3) | fit | fit | fit | fit | **fit** |
| JQ-DRAW-d (lines 123–143, §4 lines 147–163) | fit | **not fit** (G2) | **not fit** (G5) | **not fit** (G4) | fit | fit | fit | **not fit** |

Sections that are not parts but carry faults: §3 (lines 51–82): G1, G2, G3. §4 (lines 147–163):
G1, G2. §5 (lines 165–193): G1, G2. §1, §2, §6, §7: no fault found.

### G1 (S2) · an outcome at line 58 or 94 / 109 that draws at random has no draw procedure

Lines 58–59 ask a juror who chooses that outcome only to cite and "say what they require".
Only the outcome at lines 62–65 is required to state how its draw is carried out. §4
(line 149) "covers the outcomes listed in parts a and b", which are the outcomes at lines 88–93
and 102–108. §5 (lines 179–193) lists as not carried out "an Other ... that draws at random and does
not state how" (line 188), but not the case where the outcome at line 94 or line 109 is ratified
with content that draws at random.

So a ratified outcome of that kind leaves every §4 mechanic unstated: list order, generator use,
draw order and symbol order. Each of those changes which moments are drawn (measured, §6 below:
19 to 139 of 200, depending on the mechanic). The file neither covers the case nor lists it in §5.
For part b this case is not remote: TACTICS line 42 itself says "chosen at random".

### G2 (S2) · an outcome at line 62 that draws at random, beside a listed one that draws at random

§3 lines 62–65 require such an outcome to take its seed from part c and to state "whether it comes
before or after the other part's draw". §4 step 2 (lines 154–155) makes "the whole draw" use "one
generator, created once". Step 3 (line 157) puts part a's draw first when part a's ratified outcome is
the one at line 88. Step 4 (line 163) says the generator "is used for nothing else".

Two cases are left open:

- Part a ratified as the outcome at line 96, drawing at random, and part b ratified as a listed
  outcome that draws at random, with part d ratified as the outcome at line 139. The file does not
  say whether part a's draw uses §4's generator, which step 4 seems to forbid, or a second generator
  from the same seed, which repeats the same random stream.
- Part b ratified as the outcome at line 111 drawing at random and stating that it comes first,
  with part a ratified as the outcome at line 88 under §4. That contradicts step 3.

Neither case is listed in §5. Both change which moments are drawn (the a-first and b-first figure
in §6 below).

### G3 (S1, S3) · the restatement of `TACTICS.md` line 42 at lines 74–75

Lines 74–75 say that, for calm moments, `TACTICS.md` §2 "says the same number as the large-movement
moments of the same symbol, chosen at random (line 42)". Line 42 reads "the same number as the large
moments, chosen at random". The words "of the same symbol" are not in it. The reading is a
defensible one, because §2 lines 36–41 speak of each coin, but it is a reading, and it is presented
as what the line says.

It also decides the listing. Under rule (ii) at lines 71–72, the other reading of "the same number"
(as many calm cards as large-movement cards in total) gives the same procedure as rule (i). Part b
would then list one procedure, not two. This is the only place where the file restates a passage
in words that match one listed outcome and are not the passage's own. It is the same kind of fault
as v1 review A1 (v1 review line 72), which was about attributing to a root document what it does not
say, but narrower.

By contrast, "largest first (lines 36–38)" at lines 73–74 is supported in the given verdict
`decisions/2026-09-19-large-moment-selection/verdict.md` line 63 ("Moments are taken
largest-first"). I do not count it as a fault.

### G4 (S4) · the measured claim at lines 128–129 says more than was measured

Lines 128–129 say that a draw "picked different moments whenever any one of these was done
differently". What was measured (the author's record and my own re-run, seeds 1–1000) is one
alternative for each item: hour-then-symbol against symbol-then-hour, `sample` against
shuffle-then-take-first, part a's draw first against part b's draw first, and ascending against
descending symbol order. The sentence states a general result.

It is not true in general. Using the generator another way, by drawing positions with
`sample(range(n), 200)` and taking the moments at those positions, picks **the same moments as
`sample(list, 200)` in 1000 of 1000 seeds**. Each of the four items does change the draw under the
alternative measured, so the fact behind the sentence holds. The sentence as worded does not.

### G5 (S3) · part d lists one procedure, with no stated rule for why that one

Lines 67–77 give the rule by which parts a and b list their procedures, and part a and part b each
list two. Part d lists one concrete procedure (line 139), and §4 gives it seventeen lines. Every
other procedure must be written out in full by the juror under line 142–143, while the outcome at
lines 140 and 141 requires a written rule or a RULES 33 limit.

The file states no rule for why this procedure, and not another, is listed. The procedure is not
taken from anything a juror is given. Its symbol order echoes `TACTICS.md` lines 20–21, but the file
does not say so. The single concrete option, given a section of its own, is the path of least
effort, and I judge that this leans by emphasis and space. The author flagged this risk (notes, §B
item 2), and I do not agree that it is acceptable as it stands.

Part c is not faulted on the same ground. Its one listed outcome (line 118) is the only seed number
the root documents write. A juror can see why it is listed, and any other number would come from
the juror.

## 3 · Anything that could identify an exam coin, a date or a price

**No.**

- **Coin.** I ran my own scan, broader than the author's. It used every exam symbol, every base
  ticker, every name, search-hit id and search-hit name in `exam/data/external/coin-names.json`,
  and every word of **2 or more** letters in those (145 tokens). Matching was whole-word in any
  case. I also ran a substring scan for every base ticker of 3 or more letters.
  - The whole-word scan matched one ordinary function word, which also occurs inside one exam
    coin's multi-word project name. It is not a symbol, a base ticker, or a whole project name. It
    is used throughout the file in its ordinary sense, and nothing in the file ties it to a coin. I
    do not write it here.
  - The substring scan matched nothing.
  - The author's own scan (`JQ-DRAW-v2-check-ace4c9ebfe38bc8a.json`, a 4-letter minimum) records 0
    matches over 134 tokens. I read the record and did not re-run the script (it writes under
    `exam/draw-question/`).
  - The file uses "symbol" for an exam coin and never prints one.
  - I also checked the documents the jurors will be given, the four root documents and the ten
    verdicts, for every exam symbol, base ticker and project name (whole word, case-sensitive):
    0 matches in each.
- **Date.** The digit runs are line numbers, rule numbers, the counts 200 and 400, "24" (hours),
  and "8" in a folder suffix. There are no date or clock patterns. The draw number is referred to
  by its `TACTICS.md` line and not printed. The verdict folders are named without their dates.
- **Price.** There are no decimals and no price figures.

## 4 · The first review's faults, and the author's departures

| v1 review fault (line) | status in version 2 |
|---|---|
| A1, measure (72) | **Resolved.** Fact 4 (lines 27–33) states the measure, says §2 names none, and names no script. The stored change of all 678 moments reproduces with 0 mismatches. |
| B1, dependence on part a (90) | **Resolved as named.** The outcome at lines 105–108 depends only on 200 chosen moments, and §5 says when that is met. G1 and G2 are new gaps of the same family. |
| B2, list against rule (96) | **Resolved for parts a and b** (lines 67–77 generate exactly their lists, given the reading in G3). The same kind of gap is new in part d (G5). |
| C1, conditional on own answers (105) | **Resolved.** Lines 115–116 and 125–126 condition on ratified outcomes. Line 53 has every part answered by itself. |
| C2, argument a juror reads (112) | **Resolved.** The file holds no reviewer section and no argument. |
| C3, prior use of the draw number (116) | **Acted on; I judge it fit.** See §5. |
| C4, Python version (123) | **Not resolved.** Line 155 now requires the version to be written down before the draw, which makes the draw reproducible. Whether `sample` gives the same output across versions is still unmeasured. I also have only Python 3.14.4. |
| F-ORDER (129) | **Resolved.** Lines 79–82 describe the order actually used in every part. |
| F-CONV (134; v1 review §4, 177) | **Resolved for the four mechanics and the measure.** Two author-side choices remain (§6, item 4). |
| F-COMB (136) | **Resolved as named.** The false "every combination" claim is gone, and §5 lists cases. It is incomplete (G1, G2). |
| F-FACTS (138) | **Resolved.** There is no claim about how many facts the file holds. |
| F-SCRIPT (144) | **Resolved.** No scan, script or record is mentioned. Lines 128–129 describe a measurement without naming any file, and I do not count that as pointing (S7). |
| F-LEAK (148; v1 review §3, 152) | **Resolved.** See §3 above. |
| §5 row, verdict list (67; v1 review §6, 221) | **Resolved.** Each of the ten suffixes at lines 201–210 ends exactly one folder under `decisions/`, and together they are the ten my instruction names. |
| `LEDGER.md` not read (216) | **Still open.** I may not read it either. |

The author's stated departures (notes §B, "Where I disagree"):

1. **Rewording until the broad scan matched nothing: holds.** One cost is the use of "symbol" for
   a coin. The alphabetical order that §4 and line 92–93 rely on is the same whether a symbol is
   read with or without its quote suffix, and the same in any case (checked). So the word changes
   no draw.
2. **One fully stated procedure for part d: does not hold, in my judgement.** See G5.

The author's other choices:

- **Symbol order alphabetical instead of the exam list's order** (notes §E item 3): holds. It
  removes a reference to a laboratory file.
- **Reviewer sections moved to `exam/`**: holds.

Two statements in the author's notes, §A, do not match what I found:

- the S2 row says every outcome can follow (see G1 and G2);
- the passage row says no outcome is backed by a passage (see G3).

## 5 · Open items I was asked to judge, or that the author flagged

- **Fact 5 (v1 C3).** Correct: `scripts/04_draw.py` and `scripts/exam_27_find_moments.py` both
  seed `random.Random` with the line-22 number. Other scripts carry it too, so "at least two" is
  an honest lower bound.

  Needed: line 22 says "Written before the draw", and a juror weighing the outcomes at lines 118
  and 119 cannot otherwise know the number's later uses.

  It is stated in §1, away from the option, with no valuation, and it can be read for or against
  reuse. I judge it does not lean.
- **Shared start hours across symbols** (notes §E item 2). Measured: 47 start hours are shared by
  more than one symbol, holding 111 of the pool's 678 moments. The file does not say so.

  RULES 13, `TACTICS.md` line 127 and the canteen-8 verdict, all given to jurors, tell a juror that
  such cards count once. The §2 fence (line 45) excludes counting and scoring, not drawing, so an
  event-aware draw remains open under line 96 / 111.

  No listed outcome needs the figure. I judge its absence not a fault, and I record it for the
  coordinator.

## 6 · Measured, and item 4: author's choices not put to jurors

Every random measurement uses **seeds 1–1000, never the draw number**. The scripts read the
line-22 number only to assert it is not among them. Only counts of differing moments were kept.
Nothing was written but this file.

| claim or choice | result |
|---|---|
| fact 1 | 339 large-movement, 339 calm |
| fact 2 | equal for every symbol in the exam list; one symbol has 0 of each; no pool symbol outside the list |
| fact 3 | true |
| fact 4, measure | 678 of 678 stored changes reproduce from the exam hourly klines; 0 mismatches |
| fact 4, log ranking | top 200 by \|simple\| and by \|log\| differ in 8 of 200 |
| large sizes distinct | 339 of 339 at full precision and at the stored 4 decimals, so the tie rule at lines 92–93 never acts |
| list order, part a (hour-symbol vs symbol-hour) | 67–95 of 200 differ (median 82), 0 seeds identical |
| `sample` vs shuffle-then-take-first, part a | 139 of 200, every seed |
| part a first vs part b first, part a | 69–95 (median 82), 0 identical |
| symbol order ascending vs descending, after a random part a | 62–92 (median 77), 0 identical |
| within-symbol list order (hour ascending vs descending), per-symbol draw after the ranking outcome | 20–41 (median 32), 0 identical |
| `sample(list, 200)` vs `sample(range(n), 200)` then index | **identical in 1000 of 1000** (G4) |
| `sample(list, 0)` leaves the generator state unchanged | 1000 of 1000 |
| per-symbol draw feasible after the ranking outcome | yes; counts sum to 200 |

**Item 4: choices by the author that the question does not put to jurors and that could change
which moments are drawn:**

1. **Python version** (line 155–156). Unmeasured; only 3.14.4 is present. The file requires the
   version to be recorded, not chosen by jurors.
2. **Seed representation** (line 154–155 with line 118 / 121). `random.Random` seeded with a
   number's text gives a different stream from the number itself. Measured on seeds 1–1000, part
   a's random outcome differs in **68–102 of 200** (median 82), 0 identical. The file says "number"
   (lines 115–121), which points to the integer. I judge this fixed in substance by that word, and
   I record it.
3. Everything else that changes the draw (list order, generator use, draw order, symbol order,
   within-symbol order, size measure) is put to jurors through part d and fact 4.

Two choices that I checked do not change the draw:

- the tie rule;
- whether "symbol" is read with or without the quote suffix.

## 7 · What I could not do

- **`LEDGER.md`**: not read (forbidden). A user decision on the exam draw could be recorded there.
- **`decisions/2026-10-01-jq-r04-date-content/`**: not opened for reading. See §8 for one slip.
- **Other Python versions**: not tested (C4, item 4.1).
- **`scripts/exam_36_draw_question_v2_check.py` was not re-run**, because it writes a record and
  appends to a log under `exam/draw-question/`, and I may write only this file. I re-measured its
  facts and mechanics independently, with inline commands that wrote nothing.
- **`exam-prep/`, `instructions/`, `reports/`, `external/`, `cards/`, `notes/`, `canteen/`, git
  history**: not read.

## 8 · Choices and slips not covered by my instruction

- **Wider token set.** I widened the coin scan to words of 2 or more letters and added a substring
  pass. The match it produced is described, not named.
- **Alternatives used in measurement.** I chose the index-based draw (G4), the text seed (item
  4.2) and the descending within-symbol order as alternatives. They are illustrations, not
  proposals.
- **Slip 1.** While counting verdict lines I ran one command that opened the first line of
  `decisions/2026-10-01-jq-r04-date-content/verdict.md` with its output discarded to `/dev/null`.
  I saw none of its content. It was outside what I may look at, and I record it.
- **Slip 2.** One command printing the ten given verdicts produced output too long for the
  terminal. The tool saved it to a file outside this folder. I did not open that file, and I read
  the verdicts from `decisions/` instead.
- **Interpreter and caches.** Running Python reads its own library outside this folder. That is
  inherent in running scripts, which my instruction allows. All runs used `-B`, and
  `scripts/__pycache__` is unchanged (last modified 2026-10-01T22:15Z).

## 9 · Fingerprints (SHA-256)

| file | SHA-256 |
|---|---|
| `open-questions/JQ-DRAW.md` (reviewed) | `4e521cd7d7c2355653cb4dd589786ffb933d030620514bb499be773e80da13a2` |
| `exam/draw-question/JQ-DRAW-v2-for-reviewer.md` | `2a7af14d9e0d314cba033db0d945b1e84d8bf2063e8f45a295026b88b9ceb8e6` |
| `exam/draw-question/JQ-DRAW-v2-check-ace4c9ebfe38bc8a.json` | `3f39827a29ae2499a43acf63314bcff3e8971d55220ad54e1152d3e6d5927909` |
| `exam/draw-question/v2-check-runs.jsonl` | `e85c646a1321547c6345a004855753ebbe1fa63af80ef81edb8597928b8df579` |
| `exam/draw-question/JQ-DRAW-v1-REVIEW.md` | `0535fa77a386af2ecfe6298840f9a701556d46ecc49d55f988034df161d6964f` |
| `exam/draw-question/JQ-DRAW-v1-withdrawn.md` | `56dcaa89c983010f39ea9cf46869314abe5f332cb299ef82799e048aa654e97c` |
| `scripts/exam_36_draw_question_v2_check.py` | `ff5e48674b5865c9aa9059bbc3011a80e8c144a173be94e3789d016180722a92` |
| `exam/moments/moments.csv` | `8d5c42a4499f3dfa6f79417e51be1b5adb248a3a04e580c1dfddb5a238f7386a` |
| `exam/moments/pool-report.json` | `08e49c4348e88cb367ae2e8ca71dcadd79a7b6d4bb8c62c55b24520e942462e3` |
| `exam/draw/exam-coins.txt` | `b92a2212c166dc61a6aed6f0533d4b9031924cb7f865d0687d748039c2a25f50` |
| `exam/data/external/coin-names.json` | `c241e86ff876d1f92667a1545cfcc2decfc25e96a6b6ae882e9cea5df296dd92` |
| `scripts/06_find_moments.py` | `c73447af580959f92915ca5ab291cf976afc23646ed746725397b627a6d924d0` |
| `scripts/04_draw.py` | `72f261d05d82ddd20de1f35c3e70a97650ea528f9be9963e016882bd356fc822` |
| `scripts/exam_27_find_moments.py` | `4231d03f4ac7b26024d66509c364a1a1549b361266fa63ac215253a1fcd48c1a` |
| `TACTICS.md` | `66f03b3f26764bb734294efa35b8efc124f2d99a0af8d53b4bdb52db513b695a` |
| `RULES.md` | `0a9d00e77acc9530cdf1a9605094d5340e904345270020c622b012146055faca` |
| `TEAM.md` | `fb39280cc9ec2b5421d79eb19f8f3cdcf0e0715d2720386efbe68894791b91b0` |
| `README.md` | `b4de866e2c6bc13a37ecc599410ec68e5aab3d51329c8e2678fa47c3a926d180` |
