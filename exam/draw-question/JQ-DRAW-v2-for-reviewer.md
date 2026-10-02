# JQ-DRAW version 2 · notes for the reviewer and the next reviewer

**Private to `exam/`. Not for jurors.** Author: data-engineer, Mode B.
**Clock (system, UTC):** 2026-10-02T00:31:24Z, read when this file was written.
**Question file:** `open-questions/JQ-DRAW.md`, SHA-256
`4e521cd7d7c2355653cb4dd589786ffb933d030620514bb499be773e80da13a2`.
**Check script:** `scripts/exam_36_draw_question_v2_check.py`, SHA-256
`ff5e48674b5865c9aa9059bbc3011a80e8c144a173be94e3789d016180722a92`.
**Check record of the final file:** `exam/draw-question/JQ-DRAW-v2-check-ace4c9ebfe38bc8a.json`
(result PASS). The runs log is `exam/draw-question/v2-check-runs.jsonl`.

Review line numbers below are those of `JQ-DRAW-v1-REVIEW.md`. Question line
numbers are those of the version 2 file named above.

**Why these sections are here and not in the question file.** My instruction
asks for a section for the reviewer and a section for the next reviewer. The
first version put its reviewer section inside the juror-readable file, and the
review found four faults there (F-LEAK, F-FACTS, F-ARG/C2, F-SCRIPT). A section
that answers a review has to point at that review, and the standard forbids
pointing a juror at a review. So both sections live here, under `exam/`. The
question file carries nothing addressed to a reviewer. That was my decision. My
instruction did not cover it.

---

## A · For the reviewer: how each standard was checked

| standard | how I checked it | result |
|---|---|---|
| Answerable by a juror who reads only what it names, plus the four root documents and the ten verdicts given | I read the four root documents and the ten verdicts. Every line the question cites was checked against them: `TACTICS.md` 22, 33–44, 36–38, 42, 99–100; RULES 33, 34; `TEAM.md` 113–115. Every pool fact a juror needs is stated in §1 and measured (section C). §6 lists the ten verdict folders by suffix, and each suffix matches exactly one folder. The eleventh folder (date-content) is not listed, and I did not read it. | met, within what I could read |
| Every outcome can follow as stated | §4 specifies the listed random outcomes completely: list order, generator, the order of the draws, and the order of symbols. Fact 3 makes the list order total. The tie rule makes Largest total. §5 states honestly which ratified combinations cannot be carried out, and it no longer claims that every combination works. Parts c and d are asked whatever the juror answers elsewhere, so a ratified c or d never depends upon one juror's own a or b. Feasibility of Symbol-matched was measured after Even chance (seeds 1–1000) and after Largest. | met. The Python version is not measured (section E). |
| Leans toward no answer: figure | Only the figures needed are given. Magnitudes of the mechanics effects and of the measure effect are left out of the question; they are recorded here only. | met |
| Leans toward no answer: passage, precedent | No outcome quotes a passage in its favour. No verdict is cited in any part. The question gives no reasons for or against any outcome. | met |
| Leans toward no answer: order, emphasis, space | The order rule is stated and is accurate (question lines 79–82). Each listed outcome is two to four lines long. The cross-reference from Draw number to fact 5 that was in the first draft was removed, so that no option sits beside an argument. | met |
| Every figure needed and correct | Section C below. Every figure was re-measured by `exam_36`. | met |
| "Settled" and "Outside" offered | In every part (question lines 56–65, and in each part's list). | met |
| Inside RULES 33 | Each part picks a procedure or a seed for choosing among moments that already exist. None sets a threshold, a score or a trading rule. None changes a rule. The counts 400/200/200 are excluded (§2). | met |
| Points at no working file, script, run output or review | Files named: the four root documents, the ten verdicts, and the question itself. "Python's `random.Random`" names a library, not a laboratory file. Nothing mentions a scan, a check script or a record. | met |
| Nothing that could identify an exam coin, a date or a price | `exam_36` scan, run on the final file: 0 matches over 134 tokens, in any case and as whole words. The tokens were symbols, base names, project names, search-hit ids and names, and every word of 4 or more letters in those. The scan also covered date and clock patterns, 8-digit runs, month and weekday names, decimals and thousands separators. The draw number is referred to only by its `TACTICS.md` line. The verdict folders are named without their dates. | met. See section D for the drafts. |

## B · For the next reviewer: what happened to each fault the review named

| review location | outcome in version 2 |
|---|---|
| §2 part a, S1/S6 (A1, review line 72) | Fixed. Fact 4 states the measure in full and says that `TACTICS.md` §2 names none. Nothing is attributed to a root document that it does not say, and no script is named. Fact 4 also states that the log measure changes the 200 largest. A juror can therefore choose the measure through Largest or Other, or reject it. |
| §2 part b, S2 (B1, review line 90) | Fixed. Symbol-matched depends upon the ratified part a only through the 200 cards it chooses. §5 says when that holds and when it does not, and it drops the claim that every combination can be carried out. |
| §2 part b, S3 (B2, review line 96) | Fixed. Both the list and the rule changed. One stated rule, (i) and (ii) at question lines 67–77, produces exactly the two procedures listed in each of parts a and b. |
| §2 part c, S2 (C1, review line 105) | Fixed. Part c is no longer conditional upon the juror's own answers. The new part d is not conditional either. Each part is answered by itself (question line 53). The unusable combinations are listed in §5. |
| §2 part c, S3 (C2, review line 112) | Fixed. The question file contains no argument for any outcome. |
| §2 part c, open item (C3, review line 116) | Acted upon. Fact 5 states the earlier uses of the draw number neutrally, as "at least two", which is what I verified: the coin draw and the pool's calm choice. Reason: Draw number is the one concrete seed listed, and leaving this fact out would hide something bearing upon the only listed seed. It is stated in §1, away from the option. Whether stating it leans is for the reviewer to judge. |
| §2 part c, S2 not measured (C4, review line 123) | Not resolved. §4 step 2 now requires the exact Python version to be written down before the draw, so the draw can be reproduced. Whether `sample` gives the same output across Python 3 versions is still unmeasured. I have only Python 3.14.4, and I did not read the interpreter's library source, which lies outside this folder. |
| §2 F-ORDER (review line 129) | Fixed. The order sentence (question lines 79–82) now describes the order actually used. |
| §2 F-CONV (review line 134) and review §4 (line 177) | Fixed. Every mechanic that the review measured as changing the numbers is now part of the question: the four section-4 mechanics through part d, and the size measure through part a and fact 4. Part d's preamble says that each one changes which moments are drawn (re-measured, section C). |
| §2 F-COMB (review line 136) | Fixed. See B1 and C1 above. |
| §2 F-FACTS (review line 138) | Fixed by removal. The question file makes no claim about how many pool facts it holds. The no-ties fact is not stated, and the tie rule is kept. |
| §2 F-SCRIPT (review line 144) | Fixed by removal. The question file mentions no scan, script or coordinator copy. |
| §2 F-LEAK (review line 148) and review §3 (line 152) | Fixed. Nothing in the question describes a scan or names a matched word. The final scan has zero matches of any kind, in any case (section D). |
| §2 table row for §5 (review line 67) and review §6 (line 221) | Fixed. §6 names exactly the ten verdict folders the jurors are given. |
| review §6, `LEDGER.md` not read (line 216 onward) | Still open. I did not read `LEDGER.md` either, because it was forbidden to me. |

### Where I disagree with the reviewer (RULES 32)

There is no finding I disagree with. In two places I went further than the
review asked, and I record them so the next reviewer can object:

1. The review's §3 judged that the generic project-name words its own scan
   matched did not identify a coin. I nonetheless reworded the question until
   the broad scan matched nothing at all. My reason is
   `open-questions/README.md`: "not even as a word matched by a scan". Section D
   says what this cost.
2. Where the review asked only that the conventions be put to jurors, I put
   them as a separate part (d) with one fully stated procedure. I did not offer
   several alternative mechanics. Every alternative I could write would be a
   procedure of my own invention, offered for no reason the written rules give.
   A juror who wants another procedure can state it under Other. A reviewer
   could hold that a single concrete procedure leans, as the single concrete
   seed in part c might. I flag this rather than settle it.

## C · Measured figures (exam_36, record `JQ-DRAW-v2-check-ace4c9ebfe38bc8a.json`)

| claim in the question | measured |
|---|---|
| fact 1 | 339 large-movement and 339 calm moments in the pool |
| fact 2 | equal in all 20 exam coins; 1 coin has 0 of each |
| fact 3 | no two moments share start hour and symbol |
| fact 4, measure | all 678 stored changes reproduce from the exam hourly klines as close(t0+23h) / close(t0−1h) − 1, using 06's own loader, with 0 mismatches at 4 decimals |
| fact 4, log measure | the 200 largest by \|simple\| and by \|log\| differ in 8 of 200 |
| fact 5 | `TACTICS.md` line 22's number = pool-report `seed` = `04_draw.py` SEED (fed to `random.Random`) = `06` SEED (fed to `random.Random` by `exam_27`) |
| part d, list order (large, under Even chance) | differs in every seed of 1–1000: 67–95 of 200 (median 82) |
| part d, list order (calm, Even chance after Largest) | 65–95 of 200 (median 82), every seed |
| part d, sample vs shuffle-then-take-first (large) | 139 of 200, every seed |
| part d, sample vs shuffle-then-take-first (calm) | 139 of 200, every seed |
| part d, a first vs b first (both Even chance) | 69–95 of 200 (median 82), every seed |
| part d, symbol order ascending vs descending, Symbol-matched after Even chance | 62–92 of 200 (median 77), every seed |
| part d, symbol order ascending vs descending, Symbol-matched after Largest | 19–37 of 200 (median 29), every seed |
| `sample(list, 0)` leaves the generator state unchanged | true, every seed |
| Symbol-matched feasible after Even chance (every seed) and after Largest | true |
| reviewer only: large-movement sizes distinct at full precision | 339 distinct of 339, so the tie rule never acts |

The draw number is excluded from the seeds, so no part of the real exam draw
was computed. For Largest, only counts were kept, never the set itself.

## D · Scan history (matched words recorded here only)

- Run `72e1369b2e144eac` (first draft): FAIL with 20 matches, all of them
  generic words. 18 were the singular word "coin" (and "Coin"). It occurs in
  the name of a project that a ticker search returned for one exam coin, and
  it is not that exam coin's own base name or symbol. 2 were "tokenized". It
  occurs in a search-hit id and name for one exam coin, and it reached the
  draft through the folder name of the tokenized-equity verdict. Neither word
  is an exam coin's symbol or base name.
- Fix: the question uses "symbol" for an exam coin, and plural "coins", which
  the whole-word scan does not match. It names every verdict folder by a short
  suffix of the same form, so that the one suffix that had to drop a word does
  not stand out as shortened.
- Runs `cf3bcd205edf44e3` and `ace4c9ebfe38bc8a`: PASS, 0 matches.

## E · Open items and decisions not covered by my instruction

1. **Python version (C4).** Unmeasured across versions; see section B.
2. **Moments sharing a start hour across symbols.** The pool has moments of
   different symbols that start in the same hour (`pool-report.json`,
   `measured_checks.shared_start_hours`). The jq-n1-canteen-8 verdict, which
   jurors are given, makes such cards count once. The question keeps the first
   version's scope fence ("how cards that share an hour are counted or
   scored"). It does not state this fact, and it lists no event-level draw.
   I judged the fact not needed for any listed outcome, and I judged that
   stating it would add emphasis. A juror can still propose an event-aware draw
   under Other. **This is my judgement, and I flag it for the coordinator.**
3. **Symbol order.** §4 orders symbols alphabetically. The first version used
   positions in the exam-coin list, which is not alphabetical. I changed this
   so that §4 refers to no laboratory file. It is a choice inside the single
   listed procedure, and jurors can reject it through part d.
4. **Identifier.** `JQ-DRAW`, marked "Version: 2". It is not renamed.
5. **The eleventh verdict** (date-content): not read.
