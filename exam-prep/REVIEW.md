# Review of `exam-prep/` — the two pre-exam fixes

Mateo · data engineer, reviewing posture · 2026-09-19T14:37:06Z (system clock,
RULES 23) · free disk at start: 15 GB

I did not do the work under review and was not told how it was done. Everything
below I opened, re-ran or recomputed myself. Where I state a number I either
re-derived it from the cards without the other run's code, or I name the
command that produced it.

What I was allowed to open: `exam-prep/`, `scripts/`, `cards/`, `data/`,
`canteen/`, `RULES.md`, `TACTICS.md`, `TEAM.md`, `README.md`. What I did not
open: `exam/`, `decisions/`, `instructions/`, `LEDGER.md`, `reports/`, and
nothing outside the Balıkçıl folder, with any tool or from the command line.
I ran no memory or session-log search.

---

## 0 · Verdict in one line each

| problem | ruling |
|---|---|
| **R-04 · is the exam blind?** | **Solved only under three conditions, stated in §3.6.** The instrument is real and reproducible and the large channels are genuinely closed. But the document's own Level 1 is not met on two families rather than one; there is a removable channel nobody named that **defeats the acceptance gate the document writes for the exam-building run**; and the acceptance gate is under-specified in a way that makes it fail on the material the run itself declares solved. |
| **N-1 · collapse before counting** | **Not solved.** `collapse()` is sound and I reproduced every cross-check number independently. But one of the three functions the judge is told to import does not do what its docstring says, the standard contains no test for it, and the `scope` option the jurors are asked to rule on does not do what the juror question says it does. |

Neither ruling rests on a disagreement about taste. Both rest on things I could
make happen at a command line.

---

## 1 · Judging the standards, before judging the work against them

Both files were asked to write down what "solved" means in a form a reviewer
could disagree with. Both did. That part was done properly and it is what made
this review possible at all: I disagree with parts of both standards below, and
I could only do that because they were written as tests rather than as
adjectives.

### 1.1 · R-04's standard (`R-04-blindness.md` §2)

Testable: yes, all four lines. Level 1 names the families and the two attacks;
Level 2 names the pooled rows; the third line ("a channel may only be closed if
closing it does not destroy something the frozen canteen book asks for") names
§7 as its test; the clock-hour line names the T3 table.

**One defect in the standard itself, and it is the defect that hid a channel.**
The clock-hour line reads:

> A card must not print a **column** that identifies which clock hours it
> covers.

and the T3 instrument tests exactly four column sets (`BTC`+`ETH`, `chg%`,
`close`, `quote vol`). A standard scoped to columns cannot see a channel that
lives in a bullet line, and one does — §3.4 below. A standard you can satisfy
while the thing it is about is still true is a weak standard.

**A second defect.** Level 1 is a per-family test and Level 2 a pooled test,
but neither says *which of the two attacks* decides a row. This is harmless in
§5, where both are printed — and not harmless in §8 step 3, which turns one row
into a pass/fail gate without saying which attack it is graded on. §3.3 below.

### 1.2 · N-1's standard (`N-1-collapse.md` §2)

Testable: yes, five lines, each naming a script or a section. Line 2 (agreement
with an independent earlier script) is the strongest thing in either file,
because it is a genuine external check rather than a self-consistency check.

**The defect in this standard is what it leaves out.** All five lines are about
`collapse()` and about the measurement. **Not one line of the standard tests
`block_shuffle_indices()`** — which is one of the three functions §3 of that
file hands to a later judge, and which produces the "block" column of the §6
table that `VERDICT.md` leans on. A standard that does not test one of its own
three deliverables is incomplete, and the untested deliverable is the one that
is broken (§4.2).

Line 4 ("A judge cannot compute a chance line without supplying an event map")
is true as written and much weaker than it sounds. §4.3.

---

## 2 · What I verified as sound

These are not reported numbers I accepted. Each is something I re-ran or
recomputed.

**2.1 · Every fingerprint in `FINGERPRINTS.md` verifies.** All 60 rows, files
present, SHA-256 matching. Nothing in the folder has moved since 14:19:30Z.

**2.2 · All four blinded card sets rebuild bit-for-bit, with the same run
numbers.** I rebuilt each variant into a scratch directory and `diff -r`'d the
306 cards and the truth file against the committed copies. Identical, and the
run numbers came out `ca9e460829ecdac5`, `35df01d621d8da5a`,
`a9a8f3bcd515fd62`, `10405ae115941d40` — the four the document claims. RULES 29
holds in fact.

**2.3 · The combined card fingerprints in §10 reproduce.** They are not
reproducible from the prose ("each card's SHA-256 in card-number order,
hashed") — the actual recipe is `sha256(concat("B###:" + sha256(card) + "\n"))`
and I had to read `scripts/17_blind_cards.py` line 639 to find it. With that
recipe all four match. **Minor documentation gap: the recipe should be written
next to the hashes**, otherwise a later reviewer will conclude they do not
verify.

**2.4 · All five identity audits reproduce.** Raw plus four blinded sets, CSV
and hour-linkage table byte-identical, run numbers `3c090e41041104e0`,
`b8230e324e0c03e6`, `3b1cb7d540d11283`, `23502d75682cc455`,
`ba8d6b5e3880f9ee`. The residual diagnostic reproduces too
(`ca8b0bc394468298`), modulo the manifest timestamp, which the document already
explains.

**2.5 · Every number in the §3 and §5 tables of `R-04-blindness.md` is a
faithful transcription of the CSVs.** I reprinted the CSVs and compared row by
row. No number was rounded in a flattering direction.

**2.6 · The append-only guards are real.** I pointed the blinding script at an
existing output directory with a different configuration. It stopped:

```
STOP: .../cards/B253.md already exists with different text
      (RULES 30: records are append-only, never overwritten)
```

**2.7 · The blinded cards contain no year, no month name, no ticker, no
`Polymarket`, no `Bitcoin Cash`, no coin name, and no `Moment kind` line.**
Checked by grep over all 1,224 blinded card files. The three bullet lines that
still contain the words *Wikipedia*, *After* and *coin* are the uniform "Fields
not on this card" footer, identical on all 306 cards of a variant, so they
carry nothing. The date-stripper's stop-guard is not decorative: the masking
worked on every card.

**2.8 · The collapse engine reproduces exactly** (`386d234b85269a21`;
`events.csv`, `collapse-summary.csv`, `shuffle-calibration.csv` all identical),
the partition check passes on all 11 configurations, and the manifest matches
its own `.sha256` sidecar.

**2.9 · I reproduced the whole §4 cross-check without touching either
script.** Reading coin and start hour straight out of the 306 card headers and
running my own union-find:

| quantity | `14_overlap_map.py` | `15_event_collapse.py` | **my own code** |
|---|---|---|---|
| 48-hour-span components | 58 | 58 | **58** |
| of size 1 | 10 | 10 | **10** |
| of size ≥ 2 | 48 | 48 | **48** |
| largest | 20 | 20 | **20** |
| distinct start hours | — | 289 | **289** |
| start hours with > 1 card | 15 | 15 | **15** |
| pairs within 47 h | 495 | 495 | **495** |

Three independent implementations, the same numbers. N-1's standard line 2 is
met and I am satisfied it is met for the right reason.

**2.10 · The B-3 claim of §8 item 4 is exactly right, including the subtle
part.** Before-window open-interest zeros: C002, C259, C263, C264 — four cards.
C008's zero sits at `h+10`, in the after window, which an exam card does not
show. I confirmed the offset directly. That is careful work.

---

## 3 · R-04 — what is wrong

### 3.1 · Level 1 is not met, on two families, and only one of them is named in the sentence that declares it met

`R-04-blindness.md` §5 says:

> **Level 1 of my standard is met** by `strict` and `strict-flags`: every
> level-carrying family is at or below its chance line on both attacks, except
> `openint-level` …

and `VERDICT.md` turns that into a flat **"Met."**

§2 defines a level-carrying family's test as: it "must fail **both** attacks".
On `strict-flags`, from the run's own CSV:

| family | pair AUC | its chance line | beats? |
|---|---|---|---|
| `openint-level` | 0.513841 | 0.511796 | **YES** (named) |
| `trades-level` | **0.529516** | **0.513496** | **YES (not named in that sentence)** |

`trades-level` is in Level 1's own list ("price, volume, **trades**, open
interest, depth, …"), it beats its chance line by eight times the margin
`openint-level` does, and the sentence that declares Level 1 met does not
mention it.

This is not concealment — §7 item 4 and open question Q-5 name the trades
channel and give the number 0.529. It is a **mis-summary**, and it is the
summary that `VERDICT.md` carries and that anyone downstream will read. The
correct statement is: *Level 1 is met on every level-carrying family except two,
both named, both small, one of them (`trades`) closable by a live choice rather
than by a frozen rule.*

### 3.2 · A removable channel nobody named, and it is the largest one left

The audit's feature list asks each column for its **level** and its
**scale-free shape**. It never asks a column how many distinct values it takes.
For `trades` the document worked this out by hand (§7 item 4, the tie structure
survives ranking) but never carried the thought to any other column.

I carried it to `close`. Two features — the number of distinct printed `close`
values in a card's 24 rows, and the largest number of rows sharing one value —
attacked with the audit's own machinery, its own 1,000 shuffles, its own seed,
its own 1% boundary:

| feature set | card set | nearest neighbour | its line | pair AUC | its line |
|---|---|---|---|---|---|
| `closeset` (2 features) | `strict-flags` | 0.1601 | 0.1667 | **0.5421** | 0.5107 |
| `closeset` (2 features) | `ratio` / `rank` / `strict` | 0.1601 | 0.1667 | **0.5421** | 0.5107 |
| `volatility-frozen` (the audit's) | `strict-flags` | 0.1601 | 0.1765 | 0.5426 | 0.5133 |
| `volatility-frozen` + `closeset` | `strict-flags` | **0.1830** | 0.1732 | **0.5569** | 0.5136 |

Two numbers off a column the document reports as closed (`price-level` 0.5035,
below its line) get within 0.0005 of the whole frozen-volatility family, and
combined with it beat **both** attacks — which the frozen family alone does not
do.

**Why it matters more than its size.** This channel is *removable*. It is not
inherited from a frozen canteen rule; it is manufactured by the blinding's own
rendering decision. Printing every card's rebased price to the same fixed
number of decimals means a quiet card's column collapses onto far fewer
distinct printed values than a lively one's, and that is a coin signature. It
is not even a restatement of `chg%`: on 185 of 306 cards the distinct-value
count is *lower* than `chg%` alone predicts, because the rebasing rounds
genuinely different prices onto the same printed value.

I did not decide how to close it. Closing it is a rendering choice and it is
not mine; naming it is.

### 3.3 · The acceptance gate is under-specified, and it fails on the material the run declares solved

`R-04-blindness.md` §8 step 3:

> If `ALL-removable` beats its chance line on the exam cards, the cards are not
> blind and the gate has failed.

`ALL-removable` is reported in two tables — pair AUC and nearest neighbour —
and on the observation cards, under the recommended configuration:

| attack | observed | chance line | beats? |
|---|---|---|---|
| pair AUC | 0.504928 | 0.513011 | no |
| nearest neighbour | **0.189542** | **0.166667** | **YES** |

The document's own §5 nearest-neighbour table prints that row with the star
that means "beats its own chance line". So **the gate, read literally, already
fails on the 306 cards the run declares solved.** Either the gate means "pair
AUC only" — in which case it must say so — or it means both, in which case
`strict-flags` does not pass its own gate.

This is not a quibble about wording. It is a pass/fail switch handed to a later
run with no statement of which of two printed numbers throws it.

And it gets worse when §3.2 is folded in. Adding the two `closeset` features to
the gate's own feature set:

| gate statistic, `strict-flags` | as the audit computes it | with the two unnamed features |
|---|---|---|
| `ALL-removable` pair AUC | 0.5049 (line 0.5130) — **passes** | **0.5172 (line 0.5141) — fails** |
| `ALL-removable` nearest neighbour | 0.1895 (line 0.1667) — fails | 0.2451 (line 0.1732) — fails |

The gate passes on pair AUC only because the script that grades it does not
look for the channel. A gate graded by an instrument that cannot see the leak
is not a gate.

### 3.4 · An unnamed date channel, in a bullet rather than a column

`RULES.md` 9 hides the date. §6 closes the column that fingerprinted the clock
hour and measures what it closed — good work, zero false positives in 46,170
pairs, honestly reported. The standard then stops, because it is written about
columns.

The US release bullet survives on the blinded card, with the calendar date
stripped and the relative offset kept (which is what TACTICS 6 asks for, and
D-8 is a reasonable reading of it). Measured on the 306 blinded cards:

- **100 of 306** print at least one US release name.
- **30** distinct release names appear.
- **11 of those 30 names occur on exactly one calendar day** in this card set —
  annual and one-off series: *Census of Fatal Occupational Injuries*, *American
  Time Use Survey*, *Total Factor Productivity*, *Summer Youth Labor Force*,
  *Work Experience of the Population (Annual)*, *Employer-Reported Workplace
  Injuries and Illnesses (Annual)*, *Productivity by State*, *Labor Force
  Characteristics of Foreign-born Workers*, *Usual Weekly Earnings*, *Labor
  Market Experience…*, *Productivity and Costs by Industry: Wholesale and
  Retail*. **13 cards carry one of them.**
- As a card-to-card *linkage* attack it is weak: exact-match on the bullet ties
  8 of the 495 truly-overlapping pairs, with 15 false positives in 46,170. That
  is why T3 would not have caught it even if T3 had been pointed at bullets.

The point is not linkage. The point is that these are **publicly documented
release calendars**, and an exam candidate carrying nothing but general
knowledge can read *Census of Fatal Occupational Injuries (-14 h)* and date the
card to a day and an hour. This is the one place where §9 item 3's disclaimer —
"the attacks here are scripts over 306 cards at once; a reader working card by
card is a weaker adversary" — is **wrong in direction.** For this channel the
tool-less reader is the *stronger* adversary, and it is the only adversary the
exam actually has (RULES 10).

I am not saying the line must go; TACTICS 3 puts it on the card and TACTICS 6
only hides the date in it. I am saying it is a date channel, it is not named
anywhere in `exam-prep/`, and the run's own standard is phrased so that it
could not have been found.

### 3.5 · Two factual errors in the working

**(a) The B-4 parenthetical in §8 item 4 is wrong.** It says:

> 5 carry a depth run of 3 or more raw and blinded … The depth count is 5,
> **exactly the five cards they named** — C017, C018, C019, C058, C059.

Counted over the before window — which is the only window an exam card shows,
and which the same paragraph applies correctly to B-3 — the five cards are
**C018, C019, C041, C058, C059**. C017's frozen depth run is entirely in the
*after* window (before-window longest run: 1 on both depth columns; after
window: 5 and 13). C041 has a before-window run of exactly 3, on both depth
columns — and the canteen book itself notes it, at Sofia §675: "C041's across
h-13, h-12, h-11".

The count of 5 is right. The claim of set-identity was asserted, not tested,
in the middle of a passage arguing that the frozen book's blockers survive. It
is the same before/after correction the author got right one sentence earlier
for B-3 and did not apply here.

Practical effect on the instrument: none — the guard in `17_blind_cards.py`
counts cards, not identities. Effect on a reader: a juror reading that sentence
would believe C017 carries B-4 into the exam. It does not.

**(b) "About two-fifths of the excess is the overlap" (§7 item 5) is not a
measured number.** From the run record `ca8b0bc394468298`:

| forbidden | nn | line | null mean |
|---|---|---|---|
| no | 0.189542 | 0.166667 | 0.119444 |
| yes | 0.173203 | 0.169935 | 0.119686 |

Excess over the null mean falls 0.070098 → 0.053517, a reduction of **23.7%**.
Excess over the 1% line falls 0.022875 → 0.003268, a reduction of **85.7%**.
Two-fifths is neither. RULES 19: an unmeasured number is not written down.

### 3.6 · Ruling on R-04

**Solved only under conditions.** The conditions, in the order they must be
discharged:

1. **The acceptance gate of §8 step 3 must name its statistic** — which of the
   two attacks, on which row — before any exam card is built. As written it
   fails on the observation cards.
2. **The `close` repeat-structure channel (§3.2) must be either closed or
   named with its number in the exam manifest.** It is removable, it is
   manufactured by the blinding, and it flips the gate. If it is closed, the
   audit's feature list must be extended to include distinct-value counts for
   every printed column, or the gate still cannot see it.
3. **The release-name channel (§3.4) must be put to jurors, not left
   unmentioned.** It is a reading of RULES 9 against TACTICS 3 and TACTICS 6,
   which is juror territory, exactly as the document's own Q-2 is.

With those three discharged, what remains is what the document already says
honestly: Level 2 is not reachable, the residual is named and measured, and
nothing has been measured on exam cards yet. I have no quarrel with any of
that.

**On the referrals.** Q-2 (is a printed field that identifies the clock hour a
breach of RULES 9?), Q-4 (may B-1 be applied inside the exam?) and Q-5 (should
the `trades` column be printed at all?) are all definition-and-procedure
questions that change what a card shows. Referring them is **right under RULES
33, not a dodge** — and in each case the run built both configurations rather
than referring the question and then quietly shipping its preference, which is
the honest form of a referral. D-1 states its own least-confident decision
plainly and names the cost. That is the correct behaviour and I want it on the
record alongside the failures above.

---

## 4 · N-1 — what is wrong

### 4.1 · What is right

`collapse()` is a true partition on all 11 configurations, deterministic,
reproducible bit-for-bit, and cross-checked against two independent
implementations (§2.9). §5 implements every reading the wording allows and
chooses none. §6's measurement is reproducible. The refusal to choose the
reading is correct under RULES 33.

### 4.2 · `block_shuffle_indices()` does not permute events

Its docstring:

> Whole events keep their internal pattern; only whole events are moved.

It does not, whenever events differ in size — which is every configuration here
except `none`. `slots` is the concatenation of event position-lists in original
order and `donors` the same in shuffled order; `zip` pairs them index by index,
so an event of size 3 sitting next to an event of size 1 draws its three
answers from across an event boundary.

Demonstrated, not argued. Events `[[c0,c1,c2],[c3],[c4,c5]]`:

- In **175 of 200** draws at least one event read its answers from more than
  one source event.
- With an answer vector that is constant inside each event, only **138 of
  1,000** permuted vectors were still event-constant. A true block permutation
  gives 1,000 of 1,000.

Why this matters more than a docstring bug:

- It is **one of the three functions `N-1-collapse.md` §3 hands to a later
  judge**, and §8 step 4 instructs that judge to compute every chance line
  through it. A wrong null is a wrong pass/fail on the exam.
- The `block` row of §6 — the measurement `VERDICT.md` uses to say "my
  measurement does not support the strongest form of the complaint N-1 makes" —
  is computed with it.
- N-1's own standard has no line that tests it (§1.2).

**How much does the correction move the answer?** I implemented a block
permutation that does keep events whole (permuting only among events of the
same size, so the internal pattern is preserved exactly) and reran the
calibration:

| configuration | predictor | card-level 1% | **shipped "block"** | **true block** |
|---|---|---|---|---|
| `none` | iid | 0.5719 | 0.5588 | 0.5588 |
| `start-hour/component/any` | iid | 0.5719 | 0.5719 | 0.5523 |
| `start-hour/component/any` | event-constant | 0.5654 | 0.5654 | 0.5588 |
| `move-window/component/any` | event-constant | 0.5621 | 0.5817 | **0.5948** |
| `card-span/component/any` | iid | 0.5719 | 0.5654 | 0.5588 |
| `card-span/component/any` | event-constant | 0.5686 | 0.5817 | 0.5621 |
| `card-span/greedy-clique/any` | event-constant | 0.5621 | 0.5817 | **0.6013** |

So: **the bug is real and the §6 conclusion survives it.** Corrected boundaries
move by at most about +0.02 and stay far below what the `representative`
reading does (up to 0.6552). The document's mixed finding — cluster permutation
alone barely moves the line, replacing an event by one card moves it a lot —
holds after correction. I state that plainly because the run was honest enough
to publish a result that cut against the problem it was handed, and it would be
wrong to let a code defect discredit a conclusion the defect does not change.

It is still not shippable. And note a second thing the table shows: at the
widest readings a *correct* block permutation is nearly degenerate, because an
event whose size is unique cannot move at all — 2 of the 58 events under
`card-span/component/any`, with sizes running 1…20. Whoever rules on Q4 needs
to know that `block` is not merely the milder option; at some readings it is
barely an option.

### 4.3 · The "it refuses" guard is a speed bump

Standard line 4: "A judge cannot compute a chance line without supplying an
event map. **Met — the function refuses.**"

I tried to break it. It holds where it claims to:

| attempt | result |
|---|---|
| `mode` omitted | `TypeError: missing 1 required positional argument: 'mode'` |
| `events=None` | `TypeError` |
| events missing a card | `ValueError: the events do not partition id_order exactly` |
| events with a duplicated card | `ValueError: … do not partition …` |
| `mode="card"` | `ValueError: mode must be 'block' or 'representative'` |
| `representative` with events of size > 1 | `ValueError: … needs one card per event` |
| `collapse(..., definition="none")` | `ValueError: unknown definition 'none'` |
| **`events=[[c] for c in id_order]`** | **accepted, both modes; reproduces the un-collapsed card-level line exactly** |

The identity partition is a legal partition, and it undoes the collapse. The
claim is true in the sense that a judge must *type* the bypass rather than
inherit it from a default, which is worth something. It is not true in the
sense a reader of `VERDICT.md` will take it.

**And nothing enforces the rest.** `chance_line()` does not return, record or
hash the configuration it was given. §8 step 5 tells the judge to write the
configuration into the run record; that is an instruction to a person, not a
property of the instrument. Given RULES 29–30 and how much of the rest of this
folder *is* enforced in code, this is the one place where the discipline is
asked for rather than imposed. A chance line published without the event map
that made it is not reproducible, and nothing stops it.

### 4.4 · `scope=cross-coin` does not do what the juror question says it does

`N-1-collapse.md` §5:

> **scope.** … `any` lets two moments of the same coin merge; `cross-coin` does
> not.

and juror question Q3:

> Does scope follow RULES 13's words "in several coins" — i.e. may two moments
> of the same coin be one event, or not?

Under `component` resolution it does not, because a component is a transitive
closure: A and C of the same coin land in one event whenever both are joinable
to some B of another coin. Counted from the run's own `events.csv`:

| configuration | events | events holding 2+ cards of the **same** coin | largest same-coin count in one event |
|---|---|---|---|
| `start-hour/component/any` | 289 | 0 | — |
| `start-hour/component/cross-coin` | 289 | 0 | — |
| `move-window/component/any` | 131 | 15 | 2 |
| `move-window/component/cross-coin` | 136 | 10 | 2 |
| `card-span/component/any` | 58 | 25 | 5 |
| **`card-span/component/cross-coin`** | 62 | **26** | **4** |
| `card-span/greedy-clique/any` | 116 | 13 | 3 |
| `move-window/greedy-clique/cross-coin` | 168 | **0** | — |
| `card-span/greedy-clique/cross-coin` | 125 | **0** | — |

Read the two bold rows together. Under `greedy-clique`, `cross-coin` delivers
exactly what its name says: zero. Under `component` it delivers **more**
same-coin events than `any` does — 26 of 62 against 25 of 58 — because
forbidding the direct edge reshapes the components without preventing the
chain.

So a juror who reads Q3, rules "RULES 13 says *in several coins*, so
cross-coin", and pairs it with Q2's `component` gets 26 events out of 62
holding two or more moments of the same coin, one of them holding four. The
question as written cannot produce the outcome it offers. **Q3 must be
re-issued** with the coupling to Q2 stated, or the engine must make
`component`+`cross-coin` mean what the sentence says.

This is the residual I was looking for. It is not a rounding error in a
number; it is an option that is mislabelled in the document three jurors are
about to rule from, on the one axis RULES 13 states in words.

### 4.5 · Ruling on N-1

**Not solved.** Standards 1, 2, 3 and 5 are met and I verified each of them
independently. Standard 4 is met only in its literal wording. The standard
itself is missing a line, and the deliverable that line would have tested is
broken.

To close it:

1. **`block_shuffle_indices()` must be fixed or withdrawn**, and the §6 `block`
   column recomputed with whatever replaces it. The measurement conclusion does
   not change (§4.2) but the published number must be the one the method
   claims.
2. **The standard must gain a line that tests the shuffle**, not only the
   partition. The test is one paragraph: permute an event-constant answer
   vector and assert it is still event-constant.
3. **Q3 must be re-issued** to the jurors with §4.4's table attached, and Q4
   must say which block implementation it is ruling on.
4. **`chance_line()` should carry its configuration into what it returns**, so
   that §8 step 5 is a property of the instrument rather than a request.

**On the referral itself: it is right, not a dodge.** RULES 33 defines an open
question as "a wording that can be read two ways … a choice that changes the
numbers", and Q1–Q4 are exactly that: 289 events against 58 is not a detail. A
juror's scope under RULES 33 is "procedure and definition only", and all four
are procedure and definition. RULES 34 requires an answer to cite a file and a
line, and §5 gives a juror the wording, the citation and the count for every
reading. The run also declined to put a thumb on it by keeping the numbers out
of `VERDICT.md` — and then, separately, published the one measurement that cuts
*against* the problem it was handed rather than burying it. That is the right
shape for a referral. The defect is in the wording of Q3, not in the decision
to refer.

---

## 5 · Things I could not do, by name

1. **I could not measure anything on exam cards.** `exam/` is closed to me for
   the same reason it was closed to the run under review. Every number in this
   review is from the 306 observation cards and 10 coins.
2. **I could not verify the claim "nothing under `exam/` was read".** Verifying
   it would require reading `exam/`. I neither confirm nor deny it; I state
   that it is unverified by me.
3. **I did not measure the weak adversary either.** §3.4 argues that a
   tool-less reader with general knowledge can date some cards. I did not run
   that experiment — it needs a model sitting the task, not a script — and I
   have not written a number for it. What I measured is the count of cards
   carrying a once-a-year release name: 13 of 306.
4. **I did not rebuild the raw cards.** `09_write_cards.py` and everything
   upstream of it I read but did not re-run; the data downloads are outside
   this review's scope.
5. **I did not check whether the exam draw is balanced across coins.** §9 item
   4 names it as not-mine; it is not mine either.

---

## 6 · The steer check on my own instruction

I was told to report a steer if I found one. I found one, and it is sharper
than the near-misses the run under review reported in its own §C.

> **Look for what is not there.** A residual it named is honest; a residual it
> did not name is **the thing you are here for.**

This tells me what I will find before I look. A reviewer told that unnamed
residuals are "the thing you are here for" is under pressure to produce one
whether or not one exists, and a produced residual is worth nothing.

I record what I did about it rather than only that I noticed it. Everything in
§3.2, §3.4, §4.2 and §4.4 is a measurement I can hand over with the code that
made it, against the chance line the laboratory already fixed in RULES 12, on
files anyone can re-run. None of it is an opinion about whether something
"feels" leaky. And §2 is nine paragraphs of things I tried to break and could
not — which is what the instruction's framing would have squeezed out of a less
careful reviewer.

A second, milder one:

> say whether that referral is right or whether it is a dodge

Two options, one of them loaded, offered for a question whose answer might be
neither. My answer is "right" for both files, stated in §3.6 and §4.5 with the
rule numbers it rests on.

I also record, without treating it as a steer: I was told the coordinator "has
leaked instruction content fifteen times … and cannot be trusted with the
method." That is a statement about another agent, not about my verdict, and it
shaped only *where* I wrote things — method in this file, verdict in the report
— which is what it was for.

---

## 7 · How to reproduce this review

Everything in §2 is a re-run of a committed script; the commands are the ones in
`R-04-blindness.md` §8 and `N-1-collapse.md` §3. The four probes that produced
new numbers are below in full, so that nothing here rests on my word. Each uses
the laboratory's own constants — `SHUFFLES = 1000`, `TOP_FRACTION = 0.01`,
`SEED = 20260913` — by importing them from `scripts/16_identity_audit.py` and
`scripts/15_event_collapse.py` rather than restating them. I invented no
threshold and no number.

**Probe 1 — the `close` repeat-structure channel (§3.2).** Import
`16_identity_audit.py`, take `ia.card_features(c)` unchanged, add two keys, and
run the module's own `standardise` / `pair_distances` / `nearest_neighbours` /
`pair_ranks` / `pair_auc` / `quantile_top` against `random.Random(ia.SEED)`:

```python
f['closeset:distinct']  = float(len(set(col['close'])))
f['closeset:maxrepeat'] = float(max(sum(1 for x in col['close'] if x == v)
                                    for v in set(col['close'])))
```

Families compared: `["volatility:"]`, `["closeset:"]`,
`["volatility:","closeset:"]`, the audit's `ALL-removable` prefix list, and
that list plus `["closeset:"]`.

**Probe 2 — the release-name date channel (§3.4).** Read the
`- **US releases:**` bullet from each blinded card; strip the trailing
`(-N h)` and `(the calendar publishes no clock time)` from each
semicolon-separated part to get the release name; map each name to the set of
distinct calendar days its cards start on, taken from the variant's truth file.
Count names whose day-set has size 1. The linkage figures come from the same
`|gap| <= 47 h` relation `16_identity_audit.py`'s T3 uses.

**Probe 3 — the block shuffle (§4.2).** Two parts. First, the direct
assertion, on `events = [[c0,c1,c2],[c3],[c4,c5]]`: for each draw of
`ec.block_shuffle_indices`, check whether every event's donors come from a
single source event, and separately whether an event-constant answer vector is
still event-constant after permutation. Second, a replacement that permutes
only among events of the same size:

```python
def strat_block(events, id_order, rng):
    bysize = collections.defaultdict(list)
    for k, ev in enumerate(events):
        bysize[len(ev)].append(k)
    mapping = {}
    for sz, ks in bysize.items():
        tgt = list(ks); rng.shuffle(tgt)
        for a, b in zip(ks, tgt):
            mapping[a] = b
    out = [None] * len(id_order)
    for k, ev in enumerate(events):
        src = events[mapping[k]]
        for a, b in zip(sorted(ev,  key=lambda c: pos[c]),
                        sorted(src, key=lambda c: pos[c])):
            out[pos[a]] = pos[b]
    return out
```

dropped into `15_event_collapse.py`'s own calibration loop in place of
`block_shuffle_indices`, with its synthetic answer vectors and its seed
unchanged.

**Probe 4 — the scope table (§4.4).** No new code: group
`exam-prep/collapse/events.csv` by `config` and `event_id` and count events
whose `coin` column repeats.

**The independent cross-check (§2.9)** reads `| coin |` and
`| start hour (UTC) |` straight out of the 306 card headers with a regex and
runs its own union-find on `|gap| <= 47 h`, touching neither
`14_overlap_map.py` nor `15_event_collapse.py`.

---

## 8 · Fingerprints of what I reviewed

Taken at 2026-09-19T14:37:06Z, after every re-run above. These are the file
states this review refers to.

| file | SHA-256 |
|---|---|
| `exam-prep/VERDICT.md` | `c5bd5532615ee28fc3016ba2cc07246b428c5d19dcb8b580df5d5752ccb96cf0` |
| `exam-prep/R-04-blindness.md` | `c20f9c5b6ea5ed6900eade6f844b01b2fca06db98dd9862dbda239d4e4b731d7` |
| `exam-prep/N-1-collapse.md` | `28baee9ca7928755fed3c2a860eb05a8111cf4a543c46c349b17a9422fa9899b` |
| `exam-prep/decisions-and-open-questions.md` | `9abd49462f5c33d912250f101822934b4028be85cf02c95328e506b672db4538` |
| `exam-prep/README.md` | `d315670d9b6cfc66f9e9551d54ba4c7a82dcef46cb307cfeba586b8ac66fcd3f` |
| `exam-prep/FINGERPRINTS.md` | all 60 listed rows re-verified, all matching |
| `scripts/lab_cards.py` | `96b0eb01c502a40b4e76c864681763206ba627b268eedb7eb19984f81d9b928e` |
| `scripts/15_event_collapse.py` | `f3de235883aac8b364aa5391c8371d50a9ecca288007f8d0bfaadadafe0ffb12` |
| `scripts/16_identity_audit.py` | `4c4928b84ff9b484995058c2dd4e5b043af1491b60f314e1a0f418dd90e4a371` |
| `scripts/17_blind_cards.py` | `ee064204016f110d18ceb4feda2c6f6f8c3c78ce97a0cf7d3f34e225f86f9515` |
| `scripts/18_residual_diagnostic.py` | `52ebb0a115656fad7341ec22db1d98859b48a09788e1c306118ff472ecda2015` |

Run numbers I reproduced from scratch: `386d234b85269a21` (collapse),
`3c090e41041104e0` `b8230e324e0c03e6` `3b1cb7d540d11283` `23502d75682cc455`
`ba8d6b5e3880f9ee` (audits), `ca9e460829ecdac5` `35df01d621d8da5a`
`a9a8f3bcd515fd62` `10405ae115941d40` (blinding), `ca8b0bc394468298` (residual
diagnostic). Combined blinded-card fingerprints: `ratio`
`021bdfbbb08bad12080090ffe02287246d143e1a0a9c617120fccaea9fb604e2`, `rank`
`00a428658914e43da1e1372c08844488dd6bcec69bfa192a280668efdcbc3a14`, `strict`
`fb9b83059a6682098a6de41848e8ac9d89ebb207719986b07333fa8346d653f4`,
`strict-flags`
`49dc65c3af35a57ba7acf77bb1696a94272b7f2451e7b7e2fe05a2dcb631e8f6`. All
matching.

I wrote this file and nothing else. I created and modified nothing under
`exam/`, `scripts/`, `cards/`, `data/`, `canteen/`, or anywhere else in the
laboratory; my probes ran from the session scratchpad outside the repository.
