# Second fix — acting on `exam-prep/REVIEW.md`

Mateo · data engineer · started 2026-10-01T19:00:12Z (system clock, RULES 23) ·
free disk at start: 12,576,198,656 bytes.

This file is the working of the run that acts on the review. The verdict, with
an outcome for every review item, is appended to `exam-prep/VERDICT.md`. The
questions this run refers to jurors are in `exam-prep/second-fix/juror-questions/`,
indexed for the coordinator in `exam-prep/JUROR-QUESTIONS.md`.

What I opened: `exam-prep/` (all of it), `canteen/` (Sofia's book whole; Viktor's
by headings and the R-04 and §9 passages), `RULES.md`, `TACTICS.md`, `TEAM.md`,
`README.md`, `cards/`, `scripts/`. Also `CLAUDE.md` at the root, which my
instruction did not list among the files I may look at (nor among those I may
not); I name it here rather than leave it out. I did not open `exam/`,
`decisions/`, `instructions/`, `LEDGER.md`, `reports/`, `external/`, `notes/`, or
anything outside the Balıkçıl folder, and ran no memory or session-log search.
`git log` and `git status` showed me that a concurrent run is writing under
`exam/` and adding `scripts/exam_24_*.py` / `scripts/exam_25_*.py`; I saw those
names only and opened none of them.

---

## 1 · How the review's items are numbered here

The review numbers its action items in two lists: **R-04 §3.6 items 1–3** and
**N-1 §4.5 items 1–4**. Statements elsewhere in the review that ask for an
action are referred to by their section: **§1.1** (two defects in the R-04
standard), **§1.2** (the N-1 standard lacks a shuffle test), **§2.3** (the
fingerprint recipe), **§3.1** (the Level 1 mis-summary), **§3.5(a)** (the B-4
card list), **§3.5(b)** (the "two-fifths" figure), **§4.2 last paragraph**
(Q4's jurors must know block can be degenerate), **§4.3** (the "refuses"
guard). §5 and §6 of the review are the reviewer's own limits and steer check,
not items for this run.

## 2 · Every number the items rest on, re-measured first

Before acting I re-measured each number with `scripts/24_review_checks.py`, run
`28b29921e160d204`, which loads the instruments **as reviewed** from git commit
`7735d08` (it checks their SHA-256 against REVIEW §8 and stops on a mismatch).
Output: `exam-prep/second-fix/checks/review-checks-28b29921e160d204.md`.

| review | what it says | re-measured |
|---|---|---|
| §3.1 | `trades-level` beats its pair-AUC line on `strict-flags` (0.529516 vs 0.513496), unnamed in the Level 1 sentence | same; also `openint-level` 0.513841 vs 0.511796 (C-1) |
| §3.2 | `closeset` AUC 0.5421 / 0.5107; with volatility 0.5569 / 0.5136; gate+closeset 0.5172 / 0.5141 | identical to four decimals on all four variants (C-2) |
| §3.3 | `ALL-removable` on `strict-flags`: nn 0.189542 beats 0.166667, AUC 0.504928 below 0.513011 | same (C-3) |
| §3.4 | 100 / 30 / 11 / 13; linkage 8 of 495, 15 false | identical (C-4) |
| §3.5(a) | before-window depth runs: C018 C019 C041 C058 C059; C017 after only | identical; C017 before 1/1, after 5/13 (C-5) |
| §3.5(b) | 23.7% and 85.7% | identical (C-6) |
| §4.2 | events read from two sources in 175 of 200 draws; 138 of 1,000 event-constant vectors survive | 166 of 200 and 157 of 1,000 with seed `20260913` (the review states no seed); same defect (C-7) |
| §4.4 | the same-coin table | identical, plus the row the review omits: `move-window/greedy-clique/any` 10 events, largest 2 (C-8) |
| §2.3 | recipe `sha256(concat(id ":" sha256(card) "\n"))` | reproduces all four combined fingerprints (C-9) |
| §4.3 | identity partition accepted in both modes and "reproduces the un-collapsed card-level line exactly" | accepted in both modes; representative reproduces it exactly (0.571895); **block does not** (0.558824) — same null distribution, different draws (C-10) |

## 3 · What was done, item by item

### R-04 §3.6 item 1 — the gate must name its statistic

Referred: `juror-questions/JQ-R04-GATE.md`. Reason: the gate sentence can be
read four ways, the readings disagree on real material (under the reviewed
audit two pass and two fail the observation cards), and I have seen those
numbers — RULES 6 is the reason the choice should not be mine. The instrument
now prints both attacks in a section of their own and says it does not decide
(`scripts/16_identity_audit.py`, "The gate rows").

### R-04 §3.6 item 2 — the `close` repeat channel: closed or named; if closed, extend the audit

Three things, in the order they were done. The criteria were written before the
measurements they govern, in `criteria-written-before-measuring.md` (K-1, K-2,
K-4), with clock times.

**(a) The audit was extended (K-2)** — for every printed column except `h`, the
number of distinct printed values and the largest number of rows sharing one
value; one family per column group. `repeat-chg` (the frozen `chg%` column) is
forced; every other `repeat-*` family is inside `ALL-removable`.

**(b) Closing by rendering was tried (K-1) and did not close it.** K-1 prints the
rebased `close` at the fewest decimals at which rounding manufactures no tie the
raw card lacks — the same principle as the first run's D-6. Result: 3 decimals
(36 cards manufacture ties at 2; 0 at 3). New blinded set
`exam-prep/second-fix/blind-proof/strict-flags-k1/` (run `151e6ccdc930d4b4`,
otherwise the `strict-flags` configuration). Audited (run `4a33cb19150e9718`):

| `close` rendering | `repeat-close` nn (line) | `repeat-close` pair AUC (line) | K-4 granularity nn (line) | K-4 granularity AUC (line) |
|---|---|---|---|---|
| 2 decimals (reviewed) | 0.160131 (0.166667) | **0.542144** (0.510666) | **0.176471** (0.166667) | **0.605430** (0.513303) |
| 3 decimals (K-1) | **0.205882** (0.166667) | **0.563626** (0.512749) | **0.215686** (0.176471) | **0.629749** (0.512369) |

At 3 decimals the manufactured ties are gone, and the raw card's own ties and
its price step (the exchange tick relative to the price) show through more
strongly; `repeat-close` at 3 decimals equals the raw cards' figure (0.5636).
The granularity probe (K-4, `checks/instrument-checks-35925ca8acf60690.md`
E-3) already beats its line at 2 decimals — **a channel nobody had named.** No
number of decimals I tried closes the column. I did **not** switch the
recommended rendering to K-1.

**(c) Named, with numbers** — above and in §4. Two renderings that would close
it (a `close` computed from the printed `chg%`, which then carries nothing
beyond `chg%`; or no `close` column) change what TACTICS 6's "the price itself
(converted to a number starting from 100)" shows. That is a definition, so it
is referred: `juror-questions/JQ-R04-CONTENT.md` part b. The exam manifest
itself cannot be written by this run (`exam/` is closed); §8 below requires the
exam-building run to record these numbers in it.

### R-04 §3.6 item 3 — the release-name date channel to jurors

Referred: `juror-questions/JQ-R04-DATE.md` part b, together with the first run's
Q-2 (part a, the clock-hour columns) and a part this run adds (part c: an hour
offset to a release with a public clock time gives the card's time of day; 99
of 306 blinded cards print at least one offset — command in §6). The audit now
counts the release-name channel on every run (T4) and tries bullet-line linkage
(T3 row `bullet:US releases`).

### N-1 §4.5 item 1 — fix or withdraw `block_shuffle_indices()`; recompute the block column

Fixed in place in `scripts/15_event_collapse.py`; the reviewed version is
withdrawn (still readable at commit `7735d08`). The replacement moves an event
only onto an event of the same size, card for card in card order — the review's
own suggested repair — and is checked on every draw. Run `756cf4ea156d92c3`,
outputs in `exam-prep/collapse/run-756cf4ea156d92c3/`; the reviewed run's
outputs in `exam-prep/collapse/` are untouched. It reproduces the review's
"true block" column exactly in all seven rows the review printed, and leaves
`events.csv`, the card-level column and the representative column byte- and
value-identical to the reviewed run (E-4). The full table is in
`checks/instrument-checks-35925ca8acf60690.md` E-4.

Events whose size no other event shares never move: 0 under `start-hour`; 1
event (8 or 5 cards) under `move-window`; 2 events / 23 cards
(`card-span/component/any`) and 3 events / 44 cards
(`card-span/component/cross-coin`); 0 under `card-span/greedy-clique`.

### N-1 §4.5 item 2 — a standard line that tests the shuffle

Done. New line 6 of the N-1 standard (§7 below). `check_block_shuffle()` tests
permutation, single-source and event-constancy on 1,000 draws; `main()` runs it
on the review's example and on all eleven configurations before measuring, and
stops on failure; `chance_line()` checks every block draw it makes. One honest
limit: in the review's example all three events have different sizes, so the
correct shuffle never moves anything there and the example passes trivially;
the eleven real configurations are what exercise it (start-hour alone has 13
events of size 2 and 2 of size 3 that do move).

### N-1 §4.5 item 3 — re-issue Q3 with the table; Q4 names its block implementation

Done and referred: `juror-questions/JQ-N1.md` (parts 1–4, to be answered
together). Part 3 states what `cross-coin` does under each resolution and
carries the complete same-coin table; part 4 names the second-fix block
shuffle, states that the earlier one was withdrawn, gives the immovable-event
counts (review §4.2 last paragraph), and makes the two definitions
representative mode needs (which card represents an event; what label a mixed
event carries) explicit sub-parts.

### N-1 §4.5 item 4 — `chance_line()` carries its configuration

Done. `collapse()` returns an `EventMap` that carries its configuration and the
moments it was made from. `chance_line()` refuses anything else, re-derives the
map from its own moments and configuration and refuses a mismatch, and returns
a record with the configuration, the event-map fingerprint, counts, the
immovable events, the representatives' fingerprint, the shuffle constants and
the engine's SHA-256. The un-collapsed line is only available as
`identity_map()`, which labels itself `none/none/none`. Every guard was tried
(`checks/instrument-checks-35925ca8acf60690.md` E-2), including the review's
§4.3 bypass, now refused. **Limit, stated:** nothing in Python stops a caller
from writing his own shuffle without this module; the guard makes the
un-collapsed line impossible to get *from this module* without saying so.

### The other review statements

- **§1.1, first defect (standard scoped to columns):** done — the standard's
  clock-hour line now reads "field" (§7), T3 covers the release bullet, T4
  counts release names.
- **§1.1, second defect (which attack decides):** referred with item 1.
- **§1.2:** done with N-1 items 2 and 4.
- **§2.3:** done — the recipe is in §5 row 8 below and in an addendum appended
  directly after the hash table of `R-04-blindness.md`.
- **§3.1, §3.5(a), §3.5(b):** done — corrected in §5; the earlier text is kept
  and an addendum points to the correction.
- **§4.2 last paragraph:** done — `JQ-N1.md` part 4.
- **§4.3:** done with N-1 item 4; the earlier claim corrected in §5.

## 4 · What the review-required audit extension found

The review asked for distinct-value features "for every printed column" in
order to see the `close` channel. Applied to every column, they show the same
mechanism — values rounded by the raw card writer, whose repeats survive
ranking — in the ranked columns. `strict-flags`, extended audit run
`d70dd7b545bfce8a`:

| family | features | nn | line | pair AUC | line |
|---|---|---|---|---|---|
| `repeat-close` | 2 | 0.160131 | 0.166667 | **0.542144** | 0.510666 |
| `repeat-chg` (forced) | 2 | 0.101307 | 0.166667 | **0.523074** | 0.512879 |
| `repeat-volume` | 2 | **0.163399** | 0.153595 | 0.506038 | 0.511512 |
| `repeat-trades` | 2 | **0.232026** | 0.173203 | **0.585220** | 0.512746 |
| `repeat-takerbuy` | 2 | 0.124183 | 0.169935 | 0.502733 | 0.513045 |
| `repeat-openint` | 2 | 0.143791 | 0.173203 | **0.621051** | 0.513329 |
| `repeat-ratio` | 6 | **0.186275** | 0.176471 | **0.563942** | 0.512470 |
| `repeat-depth` | 4 | **0.222222** | 0.169935 | **0.535063** | 0.513320 |
| **`ALL-removable`** | 43 | **0.392157** | 0.169935 | **0.569908** | 0.513821 |

The gate row now beats its line on **both** attacks, on every blinded variant
(nn / pair AUC: ratio 0.3824 / 0.6105, rank 0.4346 / 0.5773, strict 0.3922 /
0.5699, strict-flags 0.3922 / 0.5699, strict-flags-k1 0.4183 / 0.5720; lines
between 0.1699 and 0.1765 and between 0.5119 and 0.5138). Forbidding
time-overlapping neighbours barely moves it (0.3922 → 0.3856, line 0.1732; run
`6f3cffc734151ae1`), so it is not the overlap.

Consequence: discharging the review's three R-04 conditions does **not** leave
only the residual the first run named. **R-04 is not solved.** One engineering
route that might close the ranked-column part without removing a column —
ranking the unrounded source values rather than the rounded card text, so that
only genuine repeats (the frozen depth constants B-4 needs, the zeros B-3
needs) stay equal — exists and has **not** been tried; whether the source data
has the needed precision and whether the B-3/B-4 survivals still hold has not
been measured. It needs its own criteria written first.

Other findings, by name:

1. **Block vs representative after the repair.** With the corrected shuffle,
   block minus card-level ranges **−0.0261 to +0.0392** over the twenty
   collapsed rows (the withdrawn function: −0.0131 to +0.0196); representative
   minus card-level **+0.0025 to +0.0959**. At `move-window` with event-constant
   answers the corrected block boundary is **above** the representative one in
   two rows (0.5980 vs 0.5882; 0.5980 vs 0.5901).
2. **Monte Carlo noise.** Under `none` the block and card-level shuffles draw
   from the same distribution, yet their 1% boundaries are 0.5588 and 0.5719.
   Differences of about 0.013 between columns of the calibration table are
   therefore not evidence of anything.
3. **T3 cannot see ranked columns on blinded sets** — it looks for the column
   name `quote vol`, which a blinded card prints as `quote vol r`. Named, not
   fixed (it does not bear on any review item).
4. **The nearest-neighbour attack depends on card order when features tie.**
   It breaks distance ties by the lowest card index. With whole-number
   features (the `repeat-*` families) ties are common, so the observed score
   depends on the order of the cards. Measured: the raw cards and the K-1 set
   have identical `repeat-close` features (pair AUC 0.563626 on both), yet
   nearest neighbour is 0.075163 on the raw cards (in `C###` order) and
   0.205882 on the K-1 set (card numbers shuffled with the draw seed). Blinded
   sets, and exam cards built the same way, are in shuffled order, so their
   scores are not biased by this; raw-card nearest-neighbour scores on tied
   features are. Named, not fixed.

## 5 · Corrections — what was claimed, what it is now, why

The earlier files are kept byte for byte, with an addendum appended at the end
of each one that is corrected; their earlier SHA-256 (REVIEW §8) is recorded in
`exam-prep/second-fix/FINGERPRINTS.md`.

| # | where | claimed | now | why |
|---|---|---|---|---|
| 1 | `VERDICT.md`, R-04 headline | "SOLVED, against the standard written below, with a residual that is measured and named" | **NOT SOLVED** | §4; review §3.1 and §3.3 verified (C-1, C-3) |
| 2 | `VERDICT.md` R-04 line 1; `R-04-blindness.md` §5 | Level 1 "Met" / met "except `openint-level`" | not met on two families on `strict-flags`: `openint-level` AUC 0.513841 > 0.511796 and `trades-level` 0.529516 > 0.513496 | C-1 |
| 3 | `VERDICT.md` R-04 line 2; `R-04-blindness.md` §2 | "No printed column may identify which clock hours a card covers. Met." | for columns, still met (T3); the line was scoped to columns, and bullet lines carry a date channel (13 cards with a single-day release name; 99 with an hour offset) — referred, JQ-R04-DATE | review §1.1, §3.4; C-4 |
| 4 | `R-04-blindness.md` §8 step 3 | "If `ALL-removable` beats its chance line … the gate has failed" | under-specified (two lines); referred, JQ-R04-GATE; on the extended audit it fails under every reading | review §3.3; §4 |
| 5 | `R-04-blindness.md` §7 item 5 | "About two-fifths of the excess is the overlap" | 23.7% of the excess over the null mean; 85.7% of the excess over the 1% line; on the extended audit 0.3922 → 0.3856 | C-6; run `6f3cffc734151ae1` |
| 6 | `R-04-blindness.md` §8 item 4 | depth runs on "exactly the five cards they named — C017, C018, C019, C058, C059" | C018, C019, C041, C058, C059; C017's run is in the after window only | C-5 |
| 7 | `R-04-blindness.md` §9 item 3 | "A reader working card by card is a weaker adversary than the one I used" | not true for the release-name channel, where a tool-less reader with general knowledge is the stronger adversary (unmeasured either way) | review §3.4 |
| 8 | `R-04-blindness.md` §10 | combined fingerprint = "each card's SHA-256 in card-number order, hashed" | SHA-256 over the concatenation, in card-id order, of `<id>:<SHA-256 of card file>\n` | C-9 |
| 9 | `N-1-collapse.md` §3; `15_event_collapse.py` docstring | `block_shuffle_indices` moves whole events | it did not when sizes differ; withdrawn and replaced | C-7; §3 N-1 item 1 |
| 10 | `N-1-collapse.md` §6; `decisions-and-open-questions.md` §C item 3 | "Cluster-level permutation on its own barely moves the line — between −0.013 and +0.020"; "only the representative reading moves it a lot" | corrected block: −0.0261 to +0.0392; representative +0.0025 to +0.0959; at `move-window` with event-constant answers block exceeds representative in two rows; differences near 0.013 are within Monte Carlo noise | E-4; §4 items 1–2 |
| 11 | `VERDICT.md` N-1 line 4; `N-1-collapse.md` §2 line 4 | "A judge cannot compute a chance line without supplying an event map. Met — the function refuses." | was true only in its literal wording (the identity partition passed); now plain lists are refused, the identity map exists only labelled, forged maps are refused, and the record carries the configuration | review §4.3; C-10; E-2 |
| 12 | `N-1-collapse.md` §5 and §7 Q3 | "`cross-coin` does not [let two moments of the same coin merge]" | true under `greedy-clique` only; under `component` 10 (`move-window`) and 26 (`card-span`) events hold 2+ moments of one coin | C-8; JQ-N1 part 3 |
| 13 | `VERDICT.md` N-1 headline | "SOLVED as far as one person is allowed to solve it" (the review: "Not solved") | the instrument items are done and tested; the counting cannot start until JQ-N1 is ratified | §3 |

## 6 · Commands for numbers not produced by a numbered script

- 99 of 306 `strict-flags` cards print a release with an hour offset; 1 prints
  releases without one; 9 print the FOMC entry with "(the calendar publishes no
  clock time)":
  `grep -h "US releases" exam-prep/blind-proof/strict-flags/cards/*.md | grep -v "none in these hours" | grep -c "([-+][0-9]* h)"`
  (then `grep -vc` for the second, `grep -c "no clock time"` over all for the
  third).

## 7 · The two standards, amended

Added lines are marked; nothing earlier is removed.

**R-04** (`R-04-blindness.md` §2), as amended:
- The clock-hour line reads "a card must not print a **field** — a column or a
  bullet line — that identifies which clock hours or which calendar date it
  covers" *(amended: "column" → "field")*.
- *(new)* The audit's feature list includes, for every printed column, its
  repeat structure; a family is forced only if the column it reads is printed
  unchanged because the frozen book or TACTICS requires it (K-2).
- *(new)* The gate is graded on the statistic JQ-R04-GATE ratifies; until then
  both are reported and neither is called a pass.

**N-1** (`N-1-collapse.md` §2), as amended:
- Line 4 *(amended)*: a chance line cannot be obtained from this module without
  an event map that re-derives from its own moments and configuration; the
  un-collapsed line exists only as the labelled `identity_map()`; the result
  carries the configuration and the map's fingerprint.
- Line 6 *(new)*: the block shuffle is a true block permutation — every draw a
  permutation, every event read from one source event of its size, every
  event-constant vector preserved — checked on 1,000 draws for every
  configuration on every run, and on every draw a chance line makes.

## 8 · What the next runs must do (replaces `R-04-blindness.md` §8 and `N-1-collapse.md` §8 where they differ)

**The exam-building run** must not build exam cards until R-04 is solved on
observation cards; today it is not (§4). When it does:
1. Use `scripts/17_blind_cards.py` with the configuration the laboratory
   settles after JQ-R04-DATE and JQ-R04-CONTENT; record the full configuration
   string, including `close_dp`.
2. Run `scripts/16_identity_audit.py` (second-fix version or later) on the exam
   cards with `--truth` before sealing the key; record both gate attacks, every
   `repeat-*` family, T3 and T4 in the exam manifest, and grade the gate on the
   statistic JQ-R04-GATE ratifies.
3. Run the K-4 granularity probe (`scripts/25_instrument_checks.py` E-3 shows
   how) and record it; it is not in the gate's feature list (§10 item 3).

**The judge's script** must: build the event map with `collapse()` under the
ratified JQ-N1 configuration (or `identity_map()`, labelled, only where a rule
asks for a card-level line); call `chance_line()` and store its whole record,
minus the null list, next to the run number; in representative mode pass the
representatives chosen by the ratified rule and, for an event holding both
kinds, the label the ratified rule gives it.

## 9 · Decisions I took that the instruction did not cover

1. **Numbering** of review items as in §1.
2. **Earlier files kept byte for byte, with appended addenda**, rather than
   rewritten, so every earlier claim stays readable and verifiable against
   REVIEW §8 by its leading bytes.
3. **Instruments changed in place** (`15`, `16`, `17`, `18`) rather than copied
   to new names, so that a later run importing them gets the repaired code;
   every change is listed in each script's header; outputs go to new
   per-run directories, and the reviewed outputs are untouched.
4. **K-1** as the closing criterion for `close` (from the first run's D-6), and
   then **not adopting it** after it measured worse.
5. **K-2's classification**: only `repeat-chg` forced; `repeat-depth` and
   `repeat-openint` removable although B-4/B-3 need some of their repeats —
   the same treatment the first run gave `openint-level`.
6. **K-4's probe definition** (smallest non-zero step between printed `close`
   values), and keeping it out of the gate in this run.
7. **Seed `20260913`** for C-7's draws; the review gives none.
8. **`chance_line()` now returns a dict, and representative mode takes the full
   map plus representatives** — a breaking change; old-style unpacking now
   raises instead of silently misreading (E-2).
9. **Part c of JQ-R04-DATE** (hour offsets → time of day) raised by me, not the
   review.
10. **Including JQ-B1 and the canteen's calm-overlap question (Sofia §8) in the
    juror index**, because both are open under RULES 33 and both bear on exam
    construction; I cannot see `LEDGER.md`, so I cannot tell whether either was
    already put to jurors.
11. **Grouping**: JQ-N1's four parts together; JQ-R04-DATE's three and
    JQ-R04-CONTENT's two parts together.

## 10 · What I did not do, by name

1. **R-04 is not solved.** The ranked-column repeat channel (§4) is open; the
   engineering route named there is untried.
2. **The `close` channel is not closed**; closing it needs JQ-R04-CONTENT part b.
3. **The K-4 granularity channel is not in the gate's feature list.** I bound
   myself in K-4, before measuring, not to add it in this run. I recommend the
   next run add it, for the review's own §3.3 reason (a gate that cannot see a
   leak is not a gate); on today's material it would not change the gate's
   outcome, which already fails.
4. **Nothing was measured on exam cards**; `exam/` is closed to this run.
5. **The tool-less adversary is not measured** — neither for release names nor
   for hour offsets.
6. **The exam manifest was not written** (it lives under `exam/`); §8 requires
   it.
7. **T3's blind spot for ranked columns** (§4 item 3) and the
   nearest-neighbour tie-order dependence (§4 item 4) are not fixed.
8. **Whether JQ-B1 or the canteen's calm-overlap question has already been
   answered** could not be checked (`LEDGER.md` closed).
9. **The concurrent run's files** (`exam/acquisition/`, `scripts/exam_24_*`,
   `scripts/exam_25_*`) were not opened; my own new scripts are numbered `24_`
   and `25_`, which sit next to theirs by number — no file collides, but the
   numbering can confuse a reader.
