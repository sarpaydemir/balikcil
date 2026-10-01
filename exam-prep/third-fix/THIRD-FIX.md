# Third fix — acting on `exam-prep/REVIEW-2.md`

Mateo · data engineer · started 2026-10-01T20:07:04Z (system clock, RULES 23)
· free disk at start 12,424,077,312 bytes · nothing was downloaded.

This file is the working of the run that acts on the second review. The
verdict, with an outcome for every item, is appended to
`exam-prep/VERDICT.md`. What later runs must do is in
`exam-prep/HANDED-FORWARD.md`. The juror files are in
`exam-prep/third-fix/juror-questions/`, indexed in
`exam-prep/JUROR-QUESTIONS.md`.

**Opened:** `exam-prep/` (all of it except the card files, which were read by
scripts), `canteen/2026-09-19-sofia.md` (whole), `RULES.md`, `TACTICS.md`,
`TEAM.md`, `README.md`, `scripts/` (every file whose name does not begin
`exam_`; the `exam_*` names were seen in a directory listing only),
`cards/` (by script), `data/overlap/overlap-manifest.md`,
`data/overlap/pairs.csv`, `data/draw/observation-coins.txt`,
`data/draw/draw-manifest.md` (by script and by `grep` for the disjointness
lines), `data/moments/moment-manifest.md`, and `data/observation/` (by
script, K-10).
**Not opened:** `exam/`, `decisions/`, `instructions/`, `LEDGER.md`,
`reports/`, `external/`, `notes/`, `canteen/2026-09-19-viktor.md` (allowed,
not needed), `CLAUDE.md`, git history (no `git log`, `git show` or `git diff`
was run), any `scripts/exam_*` (not read, not run), anything outside the
Balıkçıl folder. No memory or session-log search. No bytecode cache was
written (`PYTHONDONTWRITEBYTECODE=1` on every run).

---

## 1 · How REVIEW-2's items are numbered here

REVIEW-2 numbers some of its demands (§1 conditions (1)–(2), §7 items 1–5)
and states others inside sections. Each demand is given one number here, and
VERDICT reports by these numbers.

| item | REVIEW-2 | what it requires |
|---|---|---|
| R2-1 | §1 N-1 condition (1); §5 JQ-N1-2 | correct JQ-N1 part 2 (and part 3's greedy-clique bullet); then ratification |
| R2-2 | §1 N-1 condition (2); §4.3; §7 item 4 | the judge's run checks `moments_sha256` against the sealed key |
| R2-3 | §5 JQ-R04-GATE (required, and two recommended) | say what `ALL-removable` is, its count, that K-4 is outside it; NN card-order dependence; first-run row |
| R2-4 | §5 JQ-R04-CONTENT-a | remove or balance the argument paragraph; add the B-2 lift condition |
| R2-5 | §5 JQ-R04-CONTENT-b | recompute K-4 on printed decimals; NN for 1–2 feature probes; re-mark beats |
| R2-6 | §5 JQ-B1 | establish whether any exam card can satisfy B-1; withdraw or reduce; remove the closing sentence |
| R2-7 | §5 JQ-CANTEEN-8 | a juror file: define overlap, 21 beside 135, what each answer requires, coupling to JQ-N1-3 |
| R2-8 | §5 JQ-N1-4 (recommended) | the noise sentence; exact representative lines |
| R2-9 | §5 JQ-R04-DATE-b (recommended); §4.4 | count by release day; within-set uniqueness |
| R2-10 | §5, last paragraph | neither group commissioned until its unfit parts are fixed |
| R2-11 | §4.2; §7 item 3 | the floating-point K-4 probe reaching the exam-building run |
| R2-12 | §4.1; §7 item 3 | the order-dependent NN verdicts reaching the exam-building run |
| R2-13 | §3.1 (T4 caveat); §4.4 | T4 counts by the day the card starts |
| R2-14 | §3.3 item 1 | the second run's "block above representative" and "0.013 is noise" |
| R2-15 | §3.3, last paragraph | C-4 "identical" without saying the lists differed |
| R2-16 | §3.1 (K-1 table) | two of the four "beats" are not properties of the cards |
| R2-17 | §4.5; §7 item 5 | card numbers derivable from public constants — for the exam-building run to know |
| R2-18 | §6 | the index carries each question's subject in four identifiers |
| R2-19 | §7 item 1 | R-04 not solved; a concurrent run under `exam/` |

---

## 2 · What was done, item by item

### R2-1 · JQ-N1 part 2 and part 3 — done; ratification referred

`exam-prep/third-fix/juror-questions/JQ-N1.md`. Part 2 now states that under
`cross-coin` greedy-clique counts coins, not moments, and keeps the earliest
moment of a coin; that this is a second convention; what the alternative
changes; and that the engine offers only "earliest" today, so a ruling for
"latest" needs the engine changed first. Part 3's greedy-clique bullet points
to it. The convention was read in `_collapse_lists()` and measured with the
engine's own loop, only that choice reversed
(`scripts/26_third_fix_checks.py`, run `212dd7ecffc51263`, G-5):

| definition | events, keep earliest | events, keep latest | events in one partition only |
|---|---|---|---|
| move-window | 168 | 168 | 12 |
| card-span | 125 | 125 | 30 |

REVIEW-2's own literal greedy (p1b) found 4 and 21 (card-span 125 against
124): a different implementation of the alternative, counted the same way.
Both are given to the jurors. Ratification is RULES 33–35's, not mine.

### R2-2 · the key check — done in the engine; handed forward

`scripts/15_event_collapse.py`: `chance_line()` now **requires** a keyword
argument `key_moments_sha256` and refuses unless it equals the fingerprint of
the moments the event map was made from; `moments_fingerprint()` computes it
from a plain moment list. Tried (run `212dd7ecffc51263`, G-1): the true map
with the true key is accepted (`key_check: matched`); REVIEW-2's two forged
attempts (start hours moved 1,000 h apart; one card's hour moved) are refused
against the true key; an omitted key raises `TypeError`; `None` is refused.
**Limit, measured, not hidden:** a forged map passed with its own fingerprint
is accepted — the code cannot know where the value came from. So the part
that matters is handed forward: `exam-prep/HANDED-FORWARD.md` B-2 requires
the judge's script to compute the value from the sealed key file itself,
after checking that file's SHA-256 against the fingerprint recorded when it
was sealed (RULES 9). The engine's run `bec532fa008e0e01` reproduces
`events.csv`, `collapse-summary.csv` and `shuffle-calibration.csv` of run
`756cf4ea156d92c3` byte for byte; its record carries the fingerprint of the
observation moments, `7c900a10…14f6`, equal to REVIEW-2 p4's.

### R2-3 · JQ-R04-GATE — done

`exam-prep/third-fix/juror-questions/JQ-R04-GATE.md`. Says what
`ALL-removable` is (the audit's current list minus the forced families; 44
features on `strict-flags`), that it grew 23 → 43 → 44 as channels were
found, that the granularity channel was outside it until this run, and that
nothing guarantees there is no other. The nearest-neighbour tie dependence is
stated, with the fact that the gate row has no ties on any observation set.
The first-run row is dropped, and the referral reason no longer says which
options passed earlier material (RULES 6). The table now shows the third-fix
audit on five blinded versions; all fail both attacks.

### R2-4 · JQ-R04-CONTENT part a — done

The paragraph arguing that removal would not remove the mechanism is removed;
a neutral sentence says the effect of removal is engineering and will be
measured either way. The premise now quotes B-2's lift condition (lines
224–225) and §4 item 4 (lines 667–671), notes the evidence citations of trade
counts (lines 229–234, 251), and says no floor has been stated. The table's
nearest-neighbour column is the order-free one (R2-12).

### R2-5 · JQ-R04-CONTENT part b — done; the review's re-marking partly disputed

K-4 is recomputed on the printed decimals (13 distinct values at 2 decimals,
91 at 3 — REVIEW-2's p2 C figures), and the nearest-neighbour columns are the
order-free score against its own chance line. Re-marked:

| cell | second-fix | REVIEW-2 | third-fix (order-free NN, own line) |
|---|---|---|---|
| granularity, 2 decimals, NN | 0.176471 (0.166667) beats — float | 0.143791 (0.169935) does not | **0.1946 (0.1334) beats** |
| repeat structure, 3 decimals, NN | 0.205882 (0.166667) beats — card order | mean 0.1510 below 0.1667: does not | **0.1510 (0.1401) beats** |

Both numbers the second-fix table printed were unsupported (one a float
artefact, one the card numbering), as REVIEW-2 found. But REVIEW-2's
replacement verdicts compare the order-free mean with the **index-tie-break**
statistic's chance line; the order-free statistic has its own, lower, line
(averaging over ties narrows the null). Against it both cells beat. See §6,
dispute D-1. Pair AUC beats in every cell, as before.

### R2-6 · JQ-B1 — done (withdrawn, reduced to a statement); one check handed forward

Established from the laboratory's own files (run `212dd7ecffc51263`, G-4):
B-1's frozen trigger names AVGOUSDT and NOKUSDT (line 187); both are in
`data/draw/observation-coins.txt`; TACTICS 1 draws "a different 20 coins";
`scripts/04_draw.py` draws the exam from what remains; the draw manifest
records `"observation_x_exam_overlap": []` and `"disjoint": true`. So under
the frozen trigger B-1 fires on no exam card whichever means is chosen, and
the question has no outcome to decide.
`exam-prep/third-fix/juror-questions/JQ-B1.md` is a statement, not a juror
file; the index marks it withdrawn; the closing sentence (which asked jurors
to extend a frozen trigger to a class) is not carried forward. Whether the
exam cards really contain neither contract can only be checked against the
exam set: `HANDED-FORWARD.md` A-5.

### R2-7 · JQ-CANTEEN-8 — done

`exam-prep/third-fix/juror-questions/JQ-CANTEEN-8.md`. "Overlap" is taken
from the only written definition (`data/overlap/overlap-manifest.md`: card
spans share a clock hour); the second written usage (before windows, the
canteen book's "C010 and C011 overlap by ten hours") is offered as part b,
so a "no" fixes its spacing from a definition (48 h or 24 h) and no juror
sets a number. Counts (run `212dd7ecffc51263`, G-3): of the 135 calm+calm
overlapping pairs, 21 same coin and 114 different coins; by before window 10
and 53; every same-coin overlapping pair is calm+calm. The question is
scoped to the same coin (TACTICS 2 spaces per coin) with "other" open. It
goes to the JQ-N1 jurors; the index names the coupling.

### R2-8 · JQ-N1 part 4 — done

The noise sentence is replaced by exact figures (run `212dd7ecffc51263`, G-2,
criterion K-9): for the 306-card line, two runs differ by 0.0131 or more with
probability 0.058, by 0.0196 or more 0.0018, by 0.0261 or more below 0.0001;
for the representative column the exact 1% point and the 95% range of the
reported value are added to every row (0.0160 to 0.0345 wide where n is 116 to
168); the block column's own variation is stated as not computed. K-9's
acceptance check passed: every exact 1% point equals REVIEW-2 p5's.

### R2-9 · JQ-R04-DATE part b — done

By release day: 13 names on 18 cards (third-fix audit T4, which now prints
both counts; criterion K-7's check reproduced 13/18 and 11/13). The file says
the count is within-set uniqueness, not publication frequency, and that
publication frequency is unmeasured. Parts a and c are unchanged.

### R2-10 · groups commissionable — done; commissioning referred

Every row REVIEW-2 ruled unfit is corrected (§3), so both groups — JQ-N1 with
JQ-CANTEEN-8, and JQ-R04-DATE with JQ-R04-CONTENT — and JQ-R04-GATE can be
commissioned. Commissioning is the coordinator's; ratification is the
jurors' and the referee's.

### R2-11 · the floating-point K-4 probe — done; handed forward

The probe is now the audit family `granularity-close` in
`scripts/16_identity_audit.py`, computed on the printed text with exact
decimal arithmetic (criterion K-5; acceptance check passed: 13 and 91
distinct values; pair AUC 0.596809 and 0.630049, REVIEW-2 p3 D's exact
figures). It is removable under K-2's rule and sits in the gate row.
`HANDED-FORWARD.md` A-3 replaces SECOND-FIX §8 step 3 and forbids running it
as E-3 shows.

### R2-12 · nearest neighbour on tied features — done; handed forward

`scripts/16_identity_audit.py` keeps the index-tie-break score unchanged and
adds, for every family, the tie range, the number of cards with a tied
nearest neighbour, and the **tie-free** score (exact mean over every
tie-break) with its own chance line from the same shuffles (criterion K-6;
acceptance check passed: every p3b "lowest", "highest" and "mean" reproduced
on `strict-flags`). `HANDED-FORWARD.md` A-4 forbids quoting the index verdict
alone where ties exist. What the tie-free score shows is in §4.

### R2-13 · T4 by start day — done

T4 now prints both counts; see R2-9.

### R2-14 · block versus representative — done (correction recorded)

§5, corrections C3-2 and C3-3, with the exact numbers of G-2: the second
run's "block above representative in two configurations" is not supported
(`move-window/component/cross-coin`: the exact representative 1% point is
0.6029, above block's 0.5980; `move-window/greedy-clique/any`: block's 0.5980
is inside the representative's 95% range 0.5776–0.6025). The first review's
"far below" is not supported at those readings either; it holds at
`card-span/component` (representative 0.6552 against block 0.5588 / 0.5621).
JQ-N1 part 4 carries the exact figures to the jurors.

### R2-15 · C-4 — done (correction recorded)

§5, C3-5.

### R2-16 · the K-1 table — done (correction recorded), partly disputed

§5, C3-1; §6, D-1.

### R2-17 · card numbers from public constants — handed forward as information

`HANDED-FORWARD.md` A, "for your information, not a requirement". REVIEW-2
decided nothing and neither do I: whether the exam's numbering should change
is not settled by any rule or instruction I have.

### R2-18 · subjects in the index identifiers — not done; referred to the coordinator

REVIEW-2 named it and decided nothing. I kept the identifiers: they are the
names every review, verdict and juror file uses, and my instruction asks me
to report by them; renaming them would break those references. The index's
fourth column no longer points at a canteen passage or the overlap manifest
(JQ-CANTEEN-8 now has its own file). Whether a subject in an identifier is
"content" is for the coordinator to decide.

### R2-19 · R-04 and the concurrent run — R-04 not closed; closure work done; the concurrent run is the coordinator's

R-04 is not closed (§4). What its closure depends on is in VERDICT. The work
that does not depend on any juror answer was done: the gate's feature list
gained the granularity channel (K-5), the nearest-neighbour score was made
order-free (K-6), T3 now sees ranked columns (K-11), and the engineering
route the second run named and did not try — ranking the unrounded source
values — was built and audited (K-10, §4). Whether the run working under
`exam/` may proceed is not mine; HANDED-FORWARD A-0 restates SECOND-FIX §8.

---

## 3 · The juror rows, one by one, checked against REVIEW-2's standard

REVIEW-2's standard (§5): a row is fit when (i) a juror reading only the
files its row names can answer it; (ii) every outcome it offers can follow
from the instrument or rule it is about; (iii) its wording does not lean;
(iv) it is inside RULES 33; and (v) no number is shown to a juror as measured
that the instrument does not support. I applied the same five tests to every
row I corrected. Every number in the corrected files was checked against its
named source by `scripts/28_juror_file_check.py` (run `bbb740248b0c8717`:
61 checks, 0 failed; output in `exam-prep/third-fix/checks/`), and every
`RULES.md`, `TACTICS.md` and canteen line citation was printed by the same
script and read against the file.

| row | REVIEW-2 | now | (i) | (ii) | (iii) | (iv) | (v) | result |
|---|---|---|---|---|---|---|---|---|
| JQ-N1-1 | fit | unchanged (text identical; file re-issued with the corrected parts) | — | — | — | — | — | keeps its ruling |
| JQ-N1-2 | not fit | corrected | yes: the cross-coin convention is stated in the file | yes: earliest is what the engine does; latest is offered with what it needs | yes: no reason is given for either convention | yes: a convention of definition | yes: G-5 and p1b | **fit** |
| JQ-N1-3 | fit | corrected (one sentence added, and the pointer to the calm-overlap question) | yes | yes | yes | yes | yes | **fit** |
| JQ-N1-4 | fit (recommendation) | corrected | yes | yes | yes: the noise is stated for both columns, and the block column's is stated as not computed | yes | yes: G-2 exact; E-4 | **fit** |
| JQ-CANTEEN-8 | not fit | corrected (new juror file) | yes: the definitions, the counts and the rule text are in the file | yes: both answers can be carried out; "no" fixes a spacing from a written definition | yes: each option carries one reason; the stakes are stated for both | yes: a definition and a procedure, no number chosen | yes: G-3 | **fit** |
| JQ-R04-GATE | not fit | corrected | yes | yes: the four options are unchanged and can all be graded | yes: the earlier sentence naming which options passed is gone | yes | yes: third-fix audits | **fit** |
| JQ-R04-DATE-a | fit | unchanged | — | — | — | — | — | keeps its ruling |
| JQ-R04-DATE-b | fit (recommendation) | corrected | yes | yes | yes | yes | yes: T4 by release day | **fit** |
| JQ-R04-DATE-c | fit | unchanged | — | — | — | — | — | keeps its ruling |
| JQ-R04-CONTENT-a | not fit | corrected | yes: B-2 lift condition and §4 item 4 quoted | yes | yes: the one-sided paragraph is gone; one reason for each option, as before | yes | yes: third-fix audit, order-free NN | **fit** |
| JQ-R04-CONTENT-b | not fit | corrected | yes | yes | yes | yes | yes: exact K-4, order-free NN, both against their own lines | **fit** |
| JQ-B1 | not fit | corrected by withdrawal (statement) | — | — | — | — | — | not a juror row; its statement rests on G-4 |

Two things I could not make the test show and name here: (1) "does not
lean" is a judgement; the referee and the jurors may disagree with mine.
(2) Row JQ-R04-CONTENT-b shows only measurements of the one rendering
that has been built (b1); b2 and b3 are not built, because the file promises
that only permitted renderings will be built. REVIEW-2 noted the imbalance
this creates; it remains, stated in the file ("have not been built").

---

## 4 · What the instruments show now

All on the 306 observation cards; nothing on exam cards. Audit runs in
`exam-prep/third-fix/identity/`, audit script SHA-256 `4a248f78…f4da`.

### 4.1 · The gate row, every blinded version

| set | audit run | features | nearest neighbour (line) | pair AUC (line) | residual diagnostic (time-overlap forbidden) |
|---|---|---|---|---|---|
| `raw-observation` | `4858581e2eb08704` | 56 | 0.6242 (0.1732) beats | 0.7064 (0.5127) beats | — |
| `blinded-ratio` | `12b07f79e74f0be7` | 40 | 0.4052 (0.1732) beats | 0.6155 (0.5126) beats | — |
| `blinded-rank` | `96f1d17e27b8afaf` | 47 | 0.4477 (0.1699) beats | 0.5814 (0.5132) beats | — |
| `blinded-strict` | `1f2ae3cf3a5b2044` | 44 | 0.4085 (0.1699) beats | 0.5741 (0.5136) beats | — |
| `blinded-strict-flags` | `e05144718b909704` | 44 | 0.4085 (0.1699) beats | 0.5741 (0.5136) beats | 0.3987 (0.1732), run `03bf5fc1560d1e33` |
| `blinded-strict-flags-k1` | `ded6a9caaf77d910` | 44 | 0.4346 (0.1765) beats | 0.5770 (0.5137) beats | 0.4248 (0.1765), run `7b187671811b1396` |
| `blinded-strict-flags-unrounded` | `34095384f8b94ab7` | 26 | 0.2386 (0.1765) beats | 0.5456 (0.5137) beats | 0.2255 (0.1765), run `7dd6bf1f73244a4f` |

No gate row has a card with a tied nearest neighbour, so the index and
tie-free scores are equal there.

### 4.2 · Single families: the order-free nearest neighbour changes verdicts

On `strict-flags` (run `e05144718b909704`), against its own chance line the tie-free
score beats on `trades-level`, `openint-level`, `depth-level`,
`funding-line`, `repeat-close`, `repeat-chg`, `repeat-trades`,
`repeat-openint`, `repeat-ratio`, `repeat-depth` and `granularity-close`;
the index score beat only on `repeat-volume`, `repeat-trades`,
`repeat-ratio` and `repeat-depth` (and `repeat-volume`'s tie-free score does
**not** beat: 0.1297 against 0.1298). Averaging over ties narrows the null,
which is why the order-free lines are lower (for example `trades-level`
0.1403 against 0.1667). Consequence for the R-04 standard's Level 1: on the
order-free score `depth-level` also fails it, beside `openint-level` and
`trades-level` (correction C3-11).

### 4.3 · T3 now sees the ranked `quote vol` column

On `strict-flags`: 34 of the 495 pairs that truly share an hour print three
identical consecutive rank rows, against 2,726 of the 46,170 pairs that do
not (a false-positive rate of 0.059); the same on `rank`, `strict` and the
3-decimal set; 35 against 2,910 on the K-10 set; 0 and 0 on `ratio`. That is
not an identification of the clock hour; it is recorded because the row used
to read "not printed".

### 4.4 · K-10: ranking the unrounded source values

Built: `scripts/17_blind_cards.py --rank-source unrounded`, otherwise the
`strict-flags` configuration; set
`exam-prep/third-fix/blind-proof/strict-flags-unrounded/` (run
`f8b6f4075510ae05`). Every guard of K-10 passed: every ranked cell of every
card, formatted with the card writer's own functions, gives exactly the
printed raw token (306 cards × 24 hours × 9 columns); the B-3 zero hours are
the same on 4 cards; the B-4 run hours are the same in every depth column (5
cards carry a run); `chg%` is unchanged. The default rendering is unchanged:
all 1,224 reviewed blinded cards are reproduced byte for byte.

Audited (run `34095384f8b94ab7`) against `strict-flags` (run `e05144718b909704`):

| family | `strict-flags` pair AUC (line) | unrounded pair AUC (line) | `strict-flags` tie-free NN (line) | unrounded tie-free NN (line) |
|---|---|---|---|---|
| `price-level` | 0.5035 (0.5130) | 0.5035 (0.5130) | 0.1471 (0.1797) | 0.1471 (0.1797) |
| `volatility-frozen` | 0.5426 (0.5133) beats | 0.5426 (0.5133) beats | 0.1601 (0.1765) | 0.1601 (0.1765) |
| `volume-level` | 0.4992 (0.5049) | no features left | 0.1186 (0.1285) | no features left |
| `trades-level` | 0.5295 (0.5135) beats | 0.4997 (0.5033) | 0.1541 (0.1403) beats | 0.1256 (0.1256) |
| `openint-level` | 0.5138 (0.5118) beats | no features left | 0.1420 (0.1310) beats | no features left |
| `depth-level` | 0.5044 (0.5104) | no features left | 0.1471 (0.1313) beats | no features left |
| `ratio-level` | 0.4899 (0.5136) | 0.5082 (0.5052) beats | 0.1345 (0.1648) | 0.1202 (0.1250) |
| `taker-buy` | 0.4963 (0.5143) | no features left | 0.1198 (0.1311) | no features left |
| `funding-line` | 0.5727 (0.5109) beats | 0.5727 (0.5109) beats | 0.1519 (0.1248) beats | 0.1519 (0.1248) beats |
| `p7-shape` | 0.5239 (0.5132) beats | 0.5239 (0.5132) beats | 0.1503 (0.1797) | 0.1503 (0.1797) |
| `shape-scale-free` | 0.5120 (0.5126) | 0.5144 (0.5125) beats | 0.1471 (0.1732) | 0.1373 (0.1765) |
| `repeat-close` | 0.5421 (0.5107) beats | 0.5421 (0.5107) beats | 0.1408 (0.1387) beats | 0.1408 (0.1387) beats |
| `repeat-chg` | 0.5231 (0.5129) beats | 0.5231 (0.5129) beats | 0.1429 (0.1345) beats | 0.1429 (0.1345) beats |
| `repeat-volume` | 0.5060 (0.5115) | no features left | 0.1297 (0.1298) | no features left |
| `repeat-trades` | 0.5852 (0.5127) beats | 0.5012 (0.5081) | 0.2222 (0.1623) beats | 0.1210 (0.1248) |
| `repeat-takerbuy` | 0.5027 (0.5130) | no features left | 0.1212 (0.1328) | no features left |
| `repeat-openint` | 0.6211 (0.5133) beats | 0.5081 (0.5049) beats | 0.2028 (0.1419) beats | 0.1221 (0.1285) |
| `repeat-ratio` | 0.5639 (0.5125) beats | 0.5150 (0.5098) beats | 0.1863 (0.1765) beats | 0.1220 (0.1282) |
| `repeat-depth` | 0.5351 (0.5133) beats | 0.4987 (0.5071) | 0.2147 (0.1423) beats | 0.1194 (0.1291) |
| `granularity-close` | 0.5968 (0.5132) beats | 0.5968 (0.5132) beats | 0.1946 (0.1334) beats | 0.1946 (0.1334) beats |
| `ALL` | 0.5789 (0.5137) beats | 0.5598 (0.5148) beats | 0.4281 (0.1699) beats | 0.2680 (0.1699) beats |
| `ALL-except-frozen-volatility` | 0.5784 (0.5139) beats | 0.5566 (0.5146) beats | 0.4216 (0.1732) beats | 0.2582 (0.1765) beats |
| `ALL-removable` | 0.5741 (0.5136) beats | 0.5456 (0.5137) beats | 0.4085 (0.1699) beats | 0.2386 (0.1765) beats |

Read straight: ranking the unrounded values removes most of the repeat
channel of the ranked columns (the `repeat-trades` and `repeat-depth`
families and `trades-level` no longer beat either line) and reduces the gate
row on both attacks, but **does not close it**. What is left above the lines
comes from the price column (`repeat-close`, `granularity-close`, untouched
by K-10), from repeats that exist in the source itself (`repeat-openint`,
`repeat-ratio`, by pair AUC), and, marginally and by pair AUC only, from
`ratio-level` and `shape-scale-free`. The forced families are outside the
gate row. One cost, stated: a ranked column now orders hours that the
raw card printed as equal, so the blinded card carries an order the watchers
never saw; nothing in the frozen book reads that order, and its effect on an
exam candidate is not measured.

### 4.5 · K-12: the gate row without some feature groups — NOT FOR JUROR FILES

`scripts/27_gate_sensitivity.py`, run `7f6cd821a957440e`, on the K-10 set.
Feature subsets, not renderings: no card was built.

| variant | features | nearest neighbour (line) | pair AUC (line) |
|---|---|---|---|
| (a) `ALL-removable` as audited | 26 | 0.2386 (0.1765) beats | 0.5456 (0.5137) beats |
| (b) without the price-column families | 22 | 0.1242 (0.1765) does not beat | 0.5272 (0.5136) beats |
| (c) as (b), and without the trade-count features | 17 | 0.1373 (0.1732) does not beat | 0.5299 (0.5143) beats |

This says which juror outcomes would, on today's material, combine with the
K-10 route to pass which reading of the gate. That is exactly what a juror
must not see before answering (RULES 6), and it must not be put in an
instruction to one. It is written here because the coordinator must know
that R-04's closure depends on more than juror answers: under every reading
that involves pair AUC, the gate row still fails with the price column and
the trade-count column both gone, so further engineering — not yet found —
is needed whatever the jurors rule.

---

## 5 · Corrections — what was claimed, what it is now, why

Earlier files are kept byte for byte; the ones corrected here have an
addendum appended pointing to this table. Juror files of the second-fix run
are kept unchanged and are superseded through the index.

| # | where | claimed | now | why |
|---|---|---|---|---|
| C3-1 | `second-fix/SECOND-FIX.md` §3, K-1 table; `second-fix/juror-questions/JQ-R04-CONTENT.md` part b | granularity NN at 2 decimals 0.176471 beats (line 0.166667); 23 and 126 distinct values; repeat-close NN at 3 decimals 0.205882 beats | float artefact and card-order artefact respectively; on printed decimals 13 and 91 distinct values; order-free NN 0.1946 (0.1334) and 0.1510 (0.1401), both beat | REVIEW-2 §4.1, §4.2; criteria K-5, K-6 |
| C3-2 | `second-fix/SECOND-FIX.md` §4 item 1; `VERDICT.md` second-fix dispute 1 | at move-window with event-constant answers the corrected block boundary is above the representative one in two rows | not supported: exact representative 1% point 0.6029 against block 0.5980; and block 0.5980 inside the representative's 95% range 0.5776–0.6025 | REVIEW-2 §3.3; G-2 |
| C3-3 | `second-fix/SECOND-FIX.md` §4 item 2; `second-fix/juror-questions/JQ-N1.md` part 4 | differences of about 0.013 are within Monte Carlo noise; "not evidence of anything" | right for 306-card lines (2 steps: probability 0.058); understated for the representative column, whose 95% range is 0.0160–0.0345 wide at n = 116–168 | REVIEW-2 §3.3; G-2 |
| C3-4 | `second-fix/SECOND-FIX.md` §4 item 4 | blinded sets "are not biased by this" | unbiased on average, but a single index-tie-break verdict on a tied family is a property of the card numbering; against its own line the order-free score gives a different verdict from the index score on nine families of `strict-flags` (eight newly beat, one no longer does; §4.2) | REVIEW-2 §4.1; K-6 |
| C3-5 | `second-fix/SECOND-FIX.md` §2, C-4 | "identical" | the counts are identical; the first review's list of eleven names differs from the second run's in one name (it lists American Time Use Survey, which starts on two days; the second run lists Employer Costs for Employee Compensation); the second run's list is right by its stated method | REVIEW-2 §3.3, last paragraph |
| C3-6 | `second-fix/SECOND-FIX.md` §5 row 3; `second-fix/juror-questions/JQ-R04-DATE.md` part b | 11 names on one calendar day, 13 cards | by the day the card starts; by the day the release falls 13 names, 18 cards; both are within-set uniqueness | REVIEW-2 §4.4; K-7 |
| C3-7 | `second-fix/SECOND-FIX.md` §8 step 3 | run the K-4 probe "as E-3 shows" | superseded by `HANDED-FORWARD.md` A-3 | REVIEW-2 §4.2 |
| C3-8 | `second-fix/SECOND-FIX.md` §5 row 11; `VERDICT.md` second-fix table | "forged maps are refused" | true for maps edited or relabelled after construction; a map built by `collapse()` from forged moments was accepted; now refused against the key's fingerprint, with the limit stated in R2-2 | REVIEW-2 §4.3; G-1 |
| C3-9 | `second-fix/juror-questions/JQ-R04-GATE.md` | `ALL-removable` "is every measurable feature of a card that the blinding could still remove" | it is the audit's current feature list minus the forced families; it missed a measured channel | REVIEW-2 §5 |
| C3-10 | `second-fix/juror-questions/JQ-R04-CONTENT.md` part a | "Nothing in the frozen canteen book reads the trade count" | no rule, blocker, score or exit reads a card's trade count; the book names a trade-count floor as B-2's lift condition (lines 224–225, 667–671) | REVIEW-2 §5 |
| C3-11 | `R-04-blindness.md` §5; `second-fix/SECOND-FIX.md` §5 row 2 | Level 1 "not met on two families" (`openint-level`, `trades-level`) | by pair AUC, those two; by the order-free nearest neighbour against its own line also `depth-level` | K-6, §4.2 |
| C3-12 | `second-fix/juror-questions/JQ-B1.md` | a question with three options | under the frozen trigger no option can block an exam card; withdrawn | REVIEW-2 §5; G-4 |
| C3-13 | `second-fix/SECOND-FIX.md` §4 item 3; §10 item 7 | T3 cannot see ranked columns (named, not fixed) | fixed (K-11); §4.3 | — |

---

## 6 · Where I disagree with the second review (RULES 32)

**D-1 · REVIEW-2 §4.1 and §5 (JQ-R04-CONTENT-b): the replacement verdicts.**
REVIEW-2 is right that the two "beats" the second-fix table printed were not
properties of the cards. But its own verdicts — "K-4 at 2 decimals … does not
beat" (0.143791 against 0.169935) and "`repeat-close` … tie-break mean 0.1510
below line 0.1667" — compare an order-free number with the chance line of
the **index-tie-break** statistic, or use the index statistic on a family
where 304 of 306 cards are tied. A permutation line belongs to the statistic
it was drawn for. The tie-free score's own line is lower (0.1334 and 0.1401
here), and both cells beat it. The same applies to p3b's "mean beats" column
throughout: for example `trades-level` (mean 0.1541) and `repeat-close` on
`strict-flags` (0.1408) do beat their own lines (0.1403, 0.1387). REVIEW-2's
central point — that the index verdict is a property of the numbering —
stands and is the reason for K-6.

**D-2 · REVIEW-2 §6: neutral identifiers.** Not a disagreement with a
finding: REVIEW-2 decided nothing. I did not rename, for the reasons in R2-18.

---

## 7a · What I could not do, by name

1. **Nothing was measured on exam cards**; `exam/` is closed to this run.
2. **R-04 is not closed.** The remaining pair-AUC signal (§4.4, §4.5) has no
   engineering route found yet.
3. **No juror question was answered or ratified** — not mine (RULES 33–35).
4. **The judge's script does not exist**, so whether it really reads the key
   (B-2) cannot be checked; the engine cannot tell where the value it is
   given came from (G-1, last attempt).
5. **The block-mode null's random variation is not computed** (no exact
   form; no repeated-run measurement made).
6. **How often each release is published is not measured.**
7. **The tool-less adversary is not measured**, for release names, hour
   offsets, or the finer order K-10 adds to ranked columns.
8. **Whether the second-fix juror files were already put to jurors** — I
   cannot see `LEDGER.md`.
9. **Whether the exam's source cards are numbered by coin** (REVIEW-2 §4.5) —
   unknown.
10. **The run working under `exam/`** — not inspected, not mine.
11. **REVIEW-2's statements that rest on git objects** (§2: the reviewed
    bytes of first-run files, "nothing changed after commit `87685d5`") were
    not re-verified: git history is closed to this run. The hashes of every
    file REVIEW-2 lists as found were re-verified against the files at the
    start of this run (all equal).
12. **K-10 on exam data** — the route reads the card writer's sources; it has
    been shown only for the observation pipeline (306 cards, every cell).

## 7 · Decisions I took that the instruction did not cover

1. **Folder and file names:** `exam-prep/third-fix/` for this run's working;
   `exam-prep/HANDED-FORWARD.md` at the folder's root, so the exam-building
   run and the judge's run find it next to `VERDICT.md`.
2. **Instruments changed in place** (`15`, `16`, `17`), as the second-fix run
   did, so a later run importing them gets the repaired code; every change
   is listed in each script's header; reviewed outputs untouched.
3. **`key_moments_sha256` is required**, not optional (a breaking change), so
   that a judge cannot forget it.
4. **The order-free nearest-neighbour statistic** (exact mean over
   tie-breaks, its own line) and keeping the index version beside it.
5. **`granularity-close` joins the gate row** (K-5), following K-2's rule
   and the first review's reason that a gate that cannot see a leak is not a
   gate; the second-fix run had recommended it.
6. **T4's keying of a name printed without an offset** by the card's start
   day (K-7), as REVIEW-2's p2 did.
7. **The T3 suffix fix** (K-11), and with it a second batch of every audit;
   the first batch's runs (`6e8b25a450781c63`, `f7f3e1f961a52e5d`,
   `d0abcbf4eb7fc2ca`, `c3fc7b1843bc3b06`, `11a116e2282cbe57`,
   `fff5f53e56b89b90`, `af59d44f00b6c081`; residual `950da2e6f7395aac`,
   `81d8696eeefbf26d`) are kept; their T1, T2 and T4 equal the second
   batch's on all seven card sets (checked), and only T3's `quote vol` row
   differs (on the raw cards nothing differs). The residual run of the K-10 set,
   `7dd6bf1f73244a4f`, started after the audit script had reached its final
   version, so the second batch found it already recorded and wrote nothing.
   One run of `scripts/28_juror_file_check.py` (`d24a77b82c90e1b8`, 61 checks,
   0 failed) was made before the last wording edits to two juror files; the
   record that checks the files as they now are is `bbb740248b0c8717`.
8. **Trying the K-10 route**, its design (source values from the klines and
   the card writer's caches, read-only) and its guards.
9. **The K-12 sensitivity check**, and keeping its result out of every juror
   file.
10. **Withdrawing JQ-B1** (reducing it to a statement), as REVIEW-2 allowed.
11. **JQ-CANTEEN-8's framing:** scope to the same coin with "other" open;
    the two written overlap definitions as part b; joining the JQ-N1 group.
12. **The index:** a status column; each group's rows list every file the
    group needs; the earlier index kept as a byte copy.
13. **Second-fix juror files left byte-identical** (no addendum), so the
    earlier version is exactly what was reviewed; the index is the authority.
14. **Exact representative figures in JQ-N1 part 4** (a recommendation, not
    a requirement), and both implementations' numbers in part 2.
15. **Dropping the first-run row from JQ-R04-GATE** rather than defending
    it, and removing the sentence that said which options passed it.
16. **Not building renderings b2 and b3** before jurors permit them.
17. **Addenda appended** to `SECOND-FIX.md`, `VERDICT.md`, `README.md`,
    `R-04-blindness.md`, `N-1-collapse.md` and
    `decisions-and-open-questions.md`, leading bytes unchanged.

---

## 8 · How to reproduce

- `bash exam-prep/third-fix/run-instruments.sh` (first batch: collapse
  engine and audits with the K-5…K-7 audit) and
  `bash exam-prep/third-fix/run-instruments-2.sh` (every audit with the
  final audit script); `bash exam-prep/third-fix/run-unrounded-audit.sh`
  (K-10 set, first batch). Logs beside them. Append-only; a recorded run
  writes nothing.
- `python3 scripts/17_blind_cards.py --out exam-prep/third-fix/blind-proof/strict-flags-unrounded --label strict-flags-unrounded --levels rank --btceth drop --funding flags --takerbuy rank --p7 no-scale --rank-source unrounded`
- `python3 scripts/26_third_fix_checks.py` (G-1 … G-5)
- `python3 scripts/27_gate_sensitivity.py --cards exam-prep/third-fix/blind-proof/strict-flags-unrounded/cards --truth exam-prep/third-fix/blind-proof/strict-flags-unrounded/truth-strict-flags-unrounded.csv --label blinded-strict-flags-unrounded`
- `python3 scripts/28_juror_file_check.py` (every number and line citation in
  the corrected juror files)
- Constants: `SHUFFLES = 1000`, `TOP_FRACTION = 0.01`, `SEED = 20260913`,
  imported from the instruments. No threshold was introduced.

## 9 · Fingerprints

`exam-prep/third-fix/FINGERPRINTS.md`.
