# Review 2 — the second pre-exam fix (`exam-prep/second-fix/`)

Mateo · data engineer, reviewing posture · started 2026-10-01T19:37:34Z, this
file written after 2026-10-01T19:58:57Z (system clock, RULES 23) · free disk at
start 12,429,283,328 bytes, at 19:58:57Z 12,426,309,632 bytes · nothing was
downloaded.

I did not do the work under review and was not told how it was done. Every
number below is either re-run with the second run's own scripts into
`exam-prep/review-2/rerun/`, or recomputed by a probe of my own in
`exam-prep/review-2/probes/` (code and output side by side). Where I state a
number I name the probe or the run that produced it.

**Opened:** `exam-prep/` (all), `scripts/` (the non-`exam_` instruments, read
and run), `cards/`, `data/overlap/` (manifest and `pairs.csv`),
`canteen/2026-09-19-sofia.md` (§2.2–2.3, §4 items 3–5, §5, §7–9), `RULES.md`,
`TACTICS.md`, `TEAM.md`. The root `README.md` was not needed and not opened. Git objects
of this repository (`git show 7735d08:…`, `git diff` scoped to `exam-prep`
`scripts` `canteen` `cards` `data` `RULES.md` `TACTICS.md`).
**Not opened:** `exam/`, `decisions/`, `instructions/`, `LEDGER.md`,
`reports/`, `external/`, `notes/`, `canteen/2026-09-19-viktor.md`, any
`scripts/exam_*` (not run, not read), anything outside the Balıkçıl folder. No
memory or session-log search.

---

## 1 · Rulings

| problem | ruling |
|---|---|
| **R-04 · is the exam blind?** | **Not solved.** I agree with the second run. The acceptance-gate row (`ALL-removable`) beats its chance line on **both** attacks on every blinded variant, and that outcome survives every check I could put to it (§3.1). |
| **N-1 · collapse before counting** | **Solved only under two conditions.** The instrument defects the first review found are repaired and I reproduced the repair independently (§3.2). Conditions: **(1)** JQ-N1 is corrected where §5 says and then ratified (RULES 33–35) — until a configuration is ratified nothing can be counted; **(2)** the judge's run must check that the `moments_sha256` in every `chance_line()` record equals the fingerprint of the moments taken from the sealed answer key — the engine accepts an event map built from forged moments under a collapsed label (§4.3). |

---

## 2 · What I re-ran (the second run's own scripts, outputs in `exam-prep/review-2/rerun/`)

Command file: `exam-prep/review-2/rerun.sh`; log `exam-prep/review-2/rerun.log`
(19:38:19Z → 19:45:19Z). Scripts 24 and 25 have no `--out`; they were imported
and their `OUT_DIR` pointed at `rerun/checks/` so nothing was written into
`exam-prep/second-fix/`.

| run | script | result |
|---|---|---|
| `756cf4ea156d92c3` | `15_event_collapse.py` | same run number; `events.csv`, `collapse-summary.csv`, `shuffle-calibration.csv` byte-identical; manifest identical except clock, disk and path lines |
| `151e6ccdc930d4b4` | `17_blind_cards.py` (K-1 set) | same run number; all 306 cards and the truth file byte-identical; combined fingerprint `ffda9e30…b492` reproduced |
| `13d935bb5cf78346` `d91cfc33459a0270` `5fce3f6fbe815bae` `7173272492382a51` `d70dd7b545bfce8a` `4a33cb19150e9718` | `16_identity_audit.py` (raw + 5 blinded sets) | same run numbers; every audit CSV and hour-linkage CSV byte-identical; run records differ only in `output_dir` |
| `6f3cffc734151ae1` `9cdd61c13254bc69` | `18_residual_diagnostic.py` | same run numbers; reports identical except clock/disk; records identical |
| `28b29921e160d204` | `24_review_checks.py` | same run number; report identical except clock/disk lines; record identical |
| `35925ca8acf60690` | `25_instrument_checks.py` | same run number; report identical except clock/disk lines; record identical |

Also verified: all 51 rows of `exam-prep/second-fix/FINGERPRINTS.md` match the
files; the six first-run files that gained an addendum start with exactly their
reviewed bytes (checked against `git show 7735d08:…`, whose hashes equal REVIEW
§8); the 9 rows of the first-run `FINGERPRINTS.md` that no longer match are
exactly the files the second run appended to or changed, as its addendum says;
`REVIEW.md` is unchanged; nothing in `exam-prep/` or `scripts/` changed after
commit `87685d5`.

---

## 3 · The second run's outcomes against the first review — do they hold?

### 3.1 · R-04 items

| review item | second run says | holds? | how established |
|---|---|---|---|
| §3.6 item 1 (gate must name its statistic) | referred, JQ-R04-GATE | **holds** — it is a procedure question (RULES 33); the instrument now prints both attacks and decides neither (read in `16_identity_audit.py`, seen in the re-run reports) | re-run |
| §3.6 item 2 (close channel: close or name; extend audit) | partly done | **holds as stated.** Audit extension: the `repeat-*` features equal my own count from the card text on every card (0 mismatches in 6,732 + 6,732 + 7,956 feature values, p3 A). K-1: manufactured ties 36 cards at 2 decimals, 0 at 3, under half-even, half-up and float formatting alike (p2 B). Not closed by decimals: `repeat-close` pair AUC 0.5421 → 0.5636, K-4 granularity pair AUC beats at both renderings. **But two of the four "beats" in the K-1 comparison table are not properties of the cards** (§4.1, §4.2). | re-run, p2, p3, p3b |
| §3.6 item 3 (release-name channel to jurors) | referred, JQ-R04-DATE b (+a, c) | **holds**, with a correction to the count it hands the jurors (§4.4) | p2 A |
| §1.1 first defect | done ("field"; T3 bullet row; T4) | **holds with a caveat**: T4 counts a name as single-day by the day the *card starts*, not the day the release *falls*; by release day it is 13 names on 18 cards, not 11 on 13 (§4.4) | p2 A |
| §1.1 second defect | referred with item 1 | holds | — |
| §2.3 | done | holds (recipe reproduces all five combined fingerprints) | rerun 24, own hash of the K-1 set |
| §3.1 | done | holds (C-1 reproduced) | rerun 24 |
| §3.5(a) | done | holds (C-5 reproduced: C018 C019 C041 C058 C059) | rerun 24 |
| §3.5(b) | done | holds (23.7% / 85.7%) | rerun 24 |

**The R-04 ruling itself is robust.** On `strict-flags` the gate row is
nearest neighbour 0.392157 (line 0.169935) and pair AUC 0.569908 (line
0.513821); my own Mann-Whitney AUC gives 0.569908 (p3 B). At 43 features no
card has a tied nearest neighbour, so the NN score does not depend on card
order (p3b). Moving the three removable families that touch a frozen rule or
TACTICS (`repeat-depth`, `repeat-openint`, `repeat-close`) to the forced side —
one at a time or all together — still beats both lines (all three forced: NN
0.284314 vs 0.166667, AUC 0.535269 vs 0.514174; p6). So the outcome does not
turn on K-2's classification. Every blinded variant fails both attacks (ratio
0.3824/0.6105, rank 0.4346/0.5773, strict and strict-flags 0.3922/0.5699, K-1
0.4183/0.5720; re-run CSVs).

### 3.2 · N-1 items

| review item | second run says | holds? | how established |
|---|---|---|---|
| §4.5 item 1 (fix block shuffle, recompute) | done | **holds.** My own union-find and a literal greedy-clique written from JQ-N1's wording reproduce all 11 partitions of `events.csv` exactly (p1). My own checker passes the repaired `block_shuffle_indices()` on 1,000 draws for every configuration and on a constructed example with same-size events, where it really moves events (3,080 moves in 6,000 event-draws) — the review's own example cannot move anything, as the second run says (p1). | p1, re-run |
| §4.5 item 2 (standard line testing the shuffle) | done | holds | read + p1 |
| §4.5 item 3 (re-issue Q3, Q4 names block) | done, referred JQ-N1 | **holds for the re-issue; the re-issued file has one defect** (§5, JQ-N1-2). Every number in the JQ-N1 table reproduces from my own partitions (p1). | p1 |
| §4.5 item 4 (`chance_line()` carries config) | done | **holds with a condition**: an event map built by `collapse()` from forged moments is accepted under a collapsed label (§4.3) | p4 |
| §1.2 | done | holds | p1 |
| §4.2 last paragraph | done, in JQ-N1 part 4 | holds (immovable counts 0 / 1 event 8 or 5 cards / 2 events 23 cards / 3 events 44 cards / 0 reproduced, p1) | p1 |
| §4.3 | done | holds with the §4.3 condition | p4, rerun 25 |

### 3.3 · Where the second run disputes the first review — which side the material supports

1. **"The bug is real and the §6 conclusion survives it"; block stays "far
   below" representative.** The second run: spread roughly doubles; block ends
   above representative in two configurations; 0.013 differences are noise.
   **Material, split:**
   - *Spread grows* — supported. Block minus card-level runs −0.0261 to +0.0392
     (reproduced). For a 306-card line the support moves in steps of 0.006536;
     two independent lines from one null differ by ≥ 2 steps (0.0131) with
     probability 0.058, by ≥ 3 steps (0.0196) 0.0018, by ≥ 4 steps (0.0261)
     below 0.0001 (exact, p5; checked by simulation, p5b). The ends of the
     corrected range are beyond that.
   - *Block above representative in two rows* — **not supported.** The
     representative null is exactly computable. In
     `move-window/component/cross-coin` the reported representative line 0.5882
     sits at the low edge of its own spread; the exact 1% point is 0.6029,
     above block's 0.5980. In `move-window/greedy-clique/any` the representative
     line's own 95% spread is 0.5776–0.6025 and block's 0.5980 is inside it.
   - *The review's "far below"* — **not supported either** at the move-window
     and greedy-clique readings, where block and representative lines are
     within the representative column's own spread. It holds at
     `card-span/component` (representative 0.6552–0.6613 exact against block
     0.5523–0.5621).
   - *"0.013 differences are noise"* — supported for 306-card lines (a 2-step
     gap has probability 0.058), **understated for the representative column**,
     whose 95% spread at n = 116–168 is between 0.016 and 0.035 wide (p5).
2. **§4.3, block mode "reproduces the un-collapsed line exactly".** Second run
   supported: running the reviewed engine (`git show 7735d08`) myself with the
   identity partition gives block 0.558824, representative 0.571895, plain
   card-level shuffle 0.571895.
3. **§3.2, the `close` channel is "removable" by a rendering choice.** Split:
   the second run is right that no number of decimals closes it (pair AUC grows
   from 0.5421 to 0.5636 at 3 decimals, robust to card order). The review is
   not refuted: the two renderings that might close it (computed from `chg%`, or
   no price column) are also rendering choices; whether they are permitted is
   JQ-R04-CONTENT b, unanswered.
4. **§3.6, "with those three discharged, what remains is what the document
   already says".** Second run supported, robustly (§3.1 above).

The first review also mis-listed one release name (it names *American Time Use
Survey*; by the review's own stated method that name's cards start on two days,
2026-06-25 and 2026-06-26, so it is not single-day; the right eleventh name is
*Employer Costs for Employee Compensation*). The second run's list is right
under that method; its §2 calls C-4 "identical" without noting the list
differed. Minor.

---

## 4 · Findings of my own probes

### 4.1 · The nearest-neighbour attack on few-integer-feature families is decided by card numbering

With one or two whole-number features almost every card has a tied nearest
neighbour (e.g. 293 of 306 for `repeat-close`), and the audit breaks ties by
the lowest card index. Exact range of the NN score over every tie-break, and
its mean under random tie-breaks (p3b): `repeat-close` 0.0098–0.8856,
`repeat-volume` 0.0000–0.9771, `repeat-openint` 0.0458–0.8627, K-4 granularity
0.0065–0.9510. Measured against the audit's own lines, the reported NN verdict
and the verdict of the tie-break mean disagree on **`repeat-volume`** (reported
beats, mean 0.1297 below line 0.1536), **`repeat-openint`** (reported does not
beat, mean 0.2028 above line 0.1732) and **`depth-level`** (marginal) on
`strict-flags`, and on **`repeat-close` on the K-1 set** (reported 0.2059
beats, mean 0.1510 below line 0.1667). Raw cards and the K-1 set have the same
`repeat-close` features and the same tie range; only the card order differs.
The second run named this (§4 item 4) but concluded blinded sets "are not
biased"; unbiased on average, yes, but a single reported NN verdict on these
families is a property of the card numbering, not of the cards. Pair AUC uses
average ranks and is unaffected; the 43-feature gate row has no ties.

### 4.2 · The K-4 granularity probe computes steps in floating point

`scripts/25_instrument_checks.py` E-3 subtracts parsed floats. On the printed
decimals the feature takes 13 distinct values at 2 decimals and 91 at 3, not 23
and 126 (p2 C). Recomputed on exact decimal differences (p3 D): at 2 decimals
NN 0.143791 (line 0.169935) — **does not beat**, where E-3 reports 0.176471
beats; pair AUC 0.596809 (line 0.513207) still beats. At 3 decimals NN 0.215686
beats, AUC 0.630049 beats. So the granularity channel exists by pair AUC; its
NN "beats" at 2 decimals does not. SECOND-FIX §8 step 3 tells the exam-building
run to run this probe "as E-3 shows", which would carry the defect forward.

### 4.3 · The event-map guard accepts forged moments

`chance_line()` re-derives a map from the moments it carries, but nothing ties
those moments to the real ones. `collapse()` fed start hours moved 1,000 h
apart returns a map labelled `card-span/component/any` that is the identity
partition; it is accepted and gives the un-collapsed block line (0.558824).
Moving a single card's start hour gives an accepted 59-event map under the same
label. Both records carry a `moments_sha256` that differs from the true one —
detectable only if someone compares it with the moments of the sealed key;
SECOND-FIX §8 does not ask anyone to. A constructed `EventMap` with a false
label and a subclass with an overwritten `.config` are refused (p4).

### 4.4 · The release-name count handed to jurors is by card start day

By the day the release actually falls (card start hour + printed offset), 13
names fall on a single day of this card set and 18 cards carry one; by card
start day (T4's definition) 11 and 13. The two names T4 misses are *American
Time Use Survey* and *People with Health Conditions or Difficulties that Limit
Work*. Separately, "on one calendar day of this card set" is within-set
uniqueness, not publication frequency; the list includes *Employer Costs for
Employee Compensation*, which — from general knowledge, not from any file here
and not measured — is a quarterly release. 99 of 306 cards print an hour
offset, 1 prints names without one, 9 carry the FOMC "no clock time" note
(reproduced, p2 A).

### 4.5 · Card numbers on blinded sets are derivable from public constants

Every blinded set (four first-run, one second-run) maps `B###` to the same
source card, and that mapping is exactly `random.Random(20260913).shuffle` over
the `C###` order (p2 D). 20260913 is the draw number printed in TACTICS 1. On
observation cards the `C###` order is grouped by coin. An exam candidate has no
tools (RULES 10), so this is not a channel to the candidate; it is a property
of the blinding the exam-building run should know before it numbers exam cards.
Not a review item; I name it and decide nothing.

### 4.6 · The calm-overlap number in the canteen book counts different-coin pairs

Of the 135 calm+calm overlapping pairs in `data/overlap/pairs.csv`, 114 are
pairs of different coins and **21 are same-coin**; the 21 same-coin
overlapping pairs in the whole set are all calm+calm (own count). The four
examples the canteen gives are all same-coin.

---

## 5 · The juror questions, row by row

A row is **fit** when a juror reading only the files its row names can answer
it, every outcome it offers can follow from the instrument or rule it is
about, its wording does not lean, and it is inside RULES 33. I treat a number
presented to a juror as measured, which the instrument does not support, as
failing the first condition (RULES 19: the juror would be answering from a
wrong file). All citations of `RULES.md` and `TACTICS.md` line numbers in the
five files were checked against the files and are correct.

| row | ruling | why |
|---|---|---|
| JQ-N1-1 | **fit** | readings, grounds and counts all reproduce (p1); options balanced; definition only |
| JQ-N1-2 | **not fit** | the greedy-clique description omits what the instrument does under `cross-coin`: it counts coins, not moments, and when two moments of one coin cover the hour it keeps the earliest. That rule is not in the file and changes events: keeping the latest instead changes 21 events at card-span (125 → 124 events) and 4 at move-window (p1b). A juror choosing greedy-clique + cross-coin chooses a convention he was not shown. |
| JQ-N1-3 | **fit** | every count reproduces (p1); the coupling to part 2 is stated |
| JQ-N1-4 | **fit** | numbers reproduce; immovable events stated; 4a/4b are definitions. Recommended, not required: the noise sentence understates the representative column's spread (§3.3); the exact representative lines in p5 could replace the simulated ones |
| JQ-R04-GATE | **not fit** | it tells the juror `ALL-removable` is "every measurable feature of a card that the blinding could still remove". It is the audit's feature list (43 features on `strict-flags`); a probe outside it (K-4) beats by pair AUC on both renderings (§4.2). A juror weighing which attack should decide is told the row is complete when it is not. |
| JQ-R04-DATE-a | **fit** | 243 of 495, 0 of 46,170 reproduce (re-run T3); both readings available in the instrument |
| JQ-R04-DATE-b | **fit** | the question is a definition and its answer does not turn on 11 vs 13. Correction recommended (§4.4): give the count by release day (13 names, 18 cards), and say the measure is within-set uniqueness, not publication frequency |
| JQ-R04-DATE-c | **fit** | 99 reproduces; the unmeasured part is stated as unmeasured |
| JQ-R04-CONTENT-a | **not fit** | (1) it leans: after the evidence, the only argument given is that leaving the column out would not remove the mechanism and that an untried route exists — reasons against "yes" — when the question asks what TACTICS *permits*, not whether removal helps; (2) its premise "nothing in the frozen canteen book reads the trade count" is incomplete: the book names a trade-count floor as the condition for lifting B-2 (`canteen/2026-09-19-sofia.md` lines 224–225 and 667–671) |
| JQ-R04-CONTENT-b | **not fit** | its evidence table shows two nearest-neighbour "beats" that the instrument does not support: K-4 at 2 decimals (a floating-point artifact; on the printed decimals 0.1438 vs line 0.1699, §4.2) and `repeat-close` at 3 decimals (decided by card numbering; tie-break mean 0.1510 below line 0.1667, §4.1). Both count against option b1, the only rendering measured. |
| JQ-B1 | **not fit** | B-1's frozen trigger names two contracts, both observation coins, and TACTICS 1 draws "a different 20 coins" for the exam, so under the frozen trigger options B and C can never fire on an exam card. The closing instruction ("say also what the trigger … means for an exam set that does not contain those two contracts") asks the juror to extend a frozen trading rule's trigger to a class, which RULES 33 and the file's own "you do not change B-1's trigger" forbid. |
| JQ-CANTEEN-8 | **not fit** | the passage the row points to gives "135 calm+calm overlapping pairs out of 495"; 114 of those are different-coin pairs that TACTICS 2's per-coin spacing does not govern, and only 21 are same-coin (§4.6); "overlap" is not defined (card span, before window?); no outcome is stated, and a "no" needs a calm-to-calm spacing that a juror may not set (RULES 33: no threshold) unless the question derives it from a written definition |

### What must change, for each row that is not fit

These are changes to `exam-prep/` that the next run makes; this review edits
no other run's file.

- **JQ-N1-2** — in part 2 (and part 3's greedy-clique bullet) state what
  `greedy-clique` does under `cross-coin`: it counts coins, not moments, and
  keeps the earliest moment of a coin; say that this is a convention and that
  the alternative changes events (p1b numbers), so a juror who picks this
  combination can rule on it or say "other".
- **JQ-R04-GATE** — replace "every measurable feature … could still remove"
  with what the row is: the audit's current feature list, its count, and that
  at least one measured channel (K-4) is not in it. Recommended in addition:
  say that the NN score depends on card numbering wherever features tie (none on
  the observation gate row, §4.1); and either drop the first-run row of the
  measured table or say why showing it does not reproduce the RULES 6 problem
  the file gives as its reason for referring.
- **JQ-R04-CONTENT-a** — either remove the paragraph after the table that
  argues removal would not help, or give the case on both sides with equal
  weight; add the B-2 lift condition (trade-count floor, the two canteen
  passages above) to the premise.
- **JQ-R04-CONTENT-b** — recompute the K-4 column on the printed decimals; for
  1–2 feature probes report pair AUC only, or report the NN tie range (§4.1);
  re-mark which cells beat.
- **JQ-B1** — first establish, and state in the file, whether any exam card can
  satisfy B-1's frozen trigger. If none can, the row has no outcome to decide
  and should be withdrawn or reduced to a statement; if the laboratory wants
  the instrument class, that is a new rule (RULES 6), not a juror question.
  Remove the closing sentence that asks for the trigger's meaning.
- **JQ-CANTEEN-8** — write it out as a juror file like the others: define
  "overlap" from a written source; give the same-coin count (21, all calm+calm)
  beside the 135; state what each answer would require, and, for "no", what
  written definition fixes the spacing so no juror sets a number; name its
  coupling to JQ-N1 part 3 in the index's third column.

Because JQ-N1's parts and the DATE/CONTENT parts are to be answered together,
**neither group can be commissioned until its unfit parts are fixed.**

---

## 6 · Does `exam-prep/JUROR-QUESTIONS.md` carry the content of a question?

It carries **no wording, no options and no numbers** of any question; the only
numbers in it are line numbers locating a passage (`lines 918–933`). It does
carry each question's **subject** in four identifiers (GATE, DATE, CONTENT,
B1) and in one entry of the "files a juror needs" column
(`data/overlap/overlap-manifest.md`), and the CANTEEN-8 row points straight at
the passage that is that question's wording. Whether a subject counts as
content is not settled by my instruction; I name it and do not decide it.
Neutral identifiers (numbers only) would remove it.

---

## 7 · What the coordinator must act on

1. R-04 is not solved; SECOND-FIX §8 says no exam card is to be built until it
   is. A concurrent run is working under `exam/`; whether it may proceed is not
   mine.
2. Six juror rows are not fit (§5); a run must correct them in `exam-prep/`
   before juror groups are commissioned.
3. Two instrument defects reach the exam-building run through SECOND-FIX §8:
   the floating-point K-4 probe (§4.2) and the order-dependent NN verdicts on
   tied features (§4.1).
4. N-1's condition (2): the judge's script must verify `moments_sha256`
   against the sealed key (§4.3).
5. One observation outside the review items for the exam-building run (§4.5).

---

## 8 · What I could not do, by name

1. **Nothing measured on exam cards**; `exam/` is closed to me.
2. **"Nothing under `exam/` was read" by the second run** — not verifiable
   without reading `exam/`.
3. **The block-mode null is not exactly computable** (restricted permutations);
   its noise is not measured here, only the card-level and representative ones.
4. **Publication frequency of release names** — not measured; the quarterly
   remark in §4.4 is general knowledge, not a measurement.
5. **Whether JQ-B1 or the canteen §8 question was already put to jurors** —
   `LEDGER.md` is closed to me.
6. **Whether exam source cards are numbered by coin** (§4.5) — unknown.
7. **Raw cards not rebuilt**; upstream data not re-downloaded.

---

## 9 · Decisions I took that the instruction did not cover

1. **No mode named.** The instruction names none of the modes A/B/C; I
   followed its explicit list of what I may open and write.
2. **Probe scripts live in `exam-prep/review-2/probes/`**, not `scripts/`,
   because the instruction allows writes only there.
3. **Scripts 24 and 25 were run by import with `OUT_DIR` redirected**, since
   they have no `--out` and would otherwise write into `exam-prep/second-fix/`.
4. **That import let Python write two bytecode caches**
   (`scripts/__pycache__/24_review_checks.cpython-314.pyc`,
   `…/25_instrument_checks.cpython-314.pyc`, both untracked, created 19:44–19:45Z
   by my run). They are outside where I may write; I deleted them and added
   `PYTHONDONTWRITEBYTECODE=1` to `rerun.sh` (marked as added after the run).
   The other caches under `scripts/__pycache__/` were not rewritten (their
   timestamps predate my run).
5. **The fitness rule in §5** — that a number shown to a juror as measured,
   which the instrument does not support, fails "can answer from the files".
6. **Diagnostic repetition counts of my own**: 4,000 repetitions in p5b (a
   sanity check of p5's exact formula only; nothing is reported from it), and
   the tie-break "mean" in p3/p3b, which is exact and needs none.
7. **Alternative K-2 classifications in p6** — a sensitivity check, not a
   proposal.

---

## 10 · Steer check

My instruction contains no result, no prediction and no verdict. One mild
presumption: item 2 tells me the second run disputes the first review before I
looked (true, as it turned out). Separately, and not in the instruction: the
git status supplied to my session at start, and the `git log` I ran, show
commit subjects that state the second run's verdict ("R-04 not solved, N-1
instrument repaired, 12 juror questions indexed") and that a review 2 was
launched. I saw the verdict before I opened any file. My R-04 ruling rests on
§3.1's measurements, not on that subject line.

---

## 11 · How to reproduce

- `bash exam-prep/review-2/rerun.sh` — every second-fix run, into
  `exam-prep/review-2/rerun/` (append-only; an existing identical run is
  skipped).
- `python3 exam-prep/review-2/probes/<name>.py`, outputs in the `.out` files
  beside them: p1 (independent collapse, block-shuffle checker), p1b (greedy
  cross-coin convention), p2 (release names, K-1 ties, K-4 distinct values,
  card-number mapping), p3 (repeat features from text, own AUC, NN tie range,
  K-4 float vs exact), p3b (tie range for every family), p4 (`chance_line()`
  guard attempts), p5 (exact noise), p5b (simulation check of p5), p6 (gate
  sensitivity to K-2).
- Constants used: `SHUFFLES = 1000`, `TOP_FRACTION = 0.01`, `SEED = 20260913`,
  imported from the instruments; no threshold was introduced.

## 12 · Fingerprints

The SHA-256 of every file I wrote, and of the files I reviewed as I found them,
are in `exam-prep/review-2/FINGERPRINTS.md`. This file's own SHA-256 is in my
report to the coordinator.

I wrote this file and `exam-prep/review-2/`. I edited no other run's file and
nothing under `exam/`, `scripts/`, `cards/`, `data/` or `canteen/` (the two
bytecode caches in §9 item 4 were created by me and deleted by me).
