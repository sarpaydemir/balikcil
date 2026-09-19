# N-1 · collapse before counting

Mateo · data engineer · 2026-09-19 (system clock, RULES 23)
Run `386d234b85269a21` · `scripts/15_event_collapse.py`

---

## 1 · The problem as the canteen stated it

Sofia, canteen book §2.5, rule `N-1`:

> **Consequence: no count in any of the 40 files has been collapsed.** A
> shuffle over 306 un-collapsed cards produces a chance line that is too easy
> to beat.

Viktor, §9 item 3:

> Every count that goes to the chance line must be collapsed first. …
> TACTICS 7 already says "a moment appearing in several cards in the same hour
> counts as a single event"; nobody has done it yet, in any of the 40 files.

The rules behind it:

- `RULES.md` 13 — "Moments occurring in several coins in the same hour count as
  a single event. If the whole market moved together, that is one event."
- `TACTICS.md` 7 — "A moment appearing in several cards in the same hour counts
  as a single event."

---

## 2 · My standard for "solved"

Written before the measurements below were looked at. A reviewer can test every
line of it by re-running one named script.

1. **There is one implementation, and it is a partition.** A single
   deterministic function turns a moment list into events; the events cover
   every moment exactly once. The script checks this on every configuration and
   stops if it fails. *Test: read `collapse()` and the partition check in
   `scripts/15_event_collapse.py`; run it.*
2. **It agrees with an independent earlier measurement.** On the 306
   observation cards, the reading that matches the relation
   `scripts/14_overlap_map.py` measured must reproduce that script's counts
   exactly. *Test: §4 below, against run `12ce59e2902a0034`.*
3. **No reading is chosen by me.** Every reading of "the same hour" that the
   written rules allow is implemented and measured; the choice between them is
   put to jurors under RULES 33. *Test: §5.*
4. **A chance line cannot be computed without an event map.** The function a
   judge imports takes the events as an argument, has no card-level mode and no
   default mode, and refuses if the events do not partition the ids.
   *Test: `chance_line()` in `scripts/15_event_collapse.py`; the guard raises.*
5. **The effect of collapsing is measured, not asserted.** *Test: §6.*

**Not part of the standard, deliberately:** choosing the reading, choosing
between the two ways of using it, and settling the calm-to-calm spacing
question. Those are RULES 33 open questions, not engineering.

---

## 3 · What was built

| file | what it is |
|---|---|
| `scripts/15_event_collapse.py` | the engine and the measurement run |
| `scripts/lab_cards.py` | the shared card reader all three scripts use |
| `exam-prep/collapse/events.csv` | every card's event id under every configuration (3,366 rows) |
| `exam-prep/collapse/collapse-summary.csv` | the counts, one row per configuration |
| `exam-prep/collapse/shuffle-calibration.csv` | what collapsing does to a chance line |
| `exam-prep/collapse/collapse-manifest.md` | the run record, with fingerprints |

Three functions are the interface a later judge script imports:

```
collapse(moments, definition, resolution, scope)   -> list of events
block_shuffle_indices(events, id_order, rng)       -> one cluster-level draw
chance_line(answers, labels, events, id_order, mode) -> (observed, boundary, null)
```

`chance_line` has **no default mode and no card-level mode**. A judge who wants
an un-collapsed line has to write it himself rather than pick it off a default.

The engine takes `--moments CSV` (`id,coin,kind,start_hour_utc`), so the exam's
sealed answer key can be fed to it without this run ever seeing the key.

---

## 4 · Cross-check against an independent script

`scripts/14_overlap_map.py`, run `12ce59e2902a0034`, measured the 48-hour span
relation on the same 306 cards with completely separate code. My engine, run
`386d234b85269a21`, reproduces it:

| measured | `14_overlap_map.py` | `15_event_collapse.py` (`card-span/component/any`) |
|---|---|---|
| cards sharing no clock hour with any other | 10 | 10 events of size 1 |
| connected chains of >= 2 cards | 48 | 48 events of size >= 2 |
| largest chain | 20 cards | largest event 20 |
| start hours carrying more than one card | 15 | 15 events of size >= 2 under `start-hour` |

Two independent implementations, the same numbers.

---

## 5 · The readings, and what each counts

"The same hour" can be read three ways, and the choice changes the numbers a
great deal. All three are implemented; **I choose none of them.**

| name | what it means | where the wording comes from |
|---|---|---|
| `start-hour` | the two moments begin in the same clock hour | TACTICS 2: "A moment's start is the hour at which the 24-hour movement began" — so a moment *is* its start hour |
| `move-window` | the two 24-hour movements share a clock hour (start gap <= 23 h) | TACTICS 2: a moment is a 24-hour movement, so it "occurs" across 24 hours |
| `card-span` | the two 48-hour card spans share a clock hour (start gap <= 47 h) | the relation `14_overlap_map.py` measured; the widest reading |

Two further choices sit under them:

- **resolution.** Overlapping intervals have no unique partition into "groups
  sharing an hour". `component` = anything chained together is one event.
  `greedy-clique` = repeatedly take the clock hour covered by the most
  still-unassigned moments, ties to the earliest hour then the lowest card
  number. `greedy-clique` is **a stated convention, not an observation**, and
  it is written down so it can be disagreed with.
- **scope.** RULES 13 says "in several coins". `any` lets two moments of the
  same coin merge; `cross-coin` does not.

Measured on the 306 observation cards:

| configuration | events | events of size 1 | largest event | events holding both kinds |
|---|---|---|---|---|
| `none` (today) | 306 | 306 | 1 | 0 |
| `start-hour/component/any` | 289 | 274 | 3 | 2 |
| `start-hour/component/cross-coin` | 289 | 274 | 3 | 2 |
| `move-window/component/any` | 131 | 49 | 8 | 52 |
| `move-window/component/cross-coin` | 136 | 56 | 8 | 52 |
| `move-window/greedy-clique/any` | 161 | 68 | 6 | 49 |
| `move-window/greedy-clique/cross-coin` | 168 | 78 | 6 | 50 |
| `card-span/component/any` | **58** | 10 | 20 | 37 |
| `card-span/component/cross-coin` | 62 | 13 | 20 | 39 |
| `card-span/greedy-clique/any` | 116 | 32 | 7 | 56 |
| `card-span/greedy-clique/cross-coin` | 125 | 41 | 7 | 60 |

The last column is the one a judge has to read before anything else. **An event
holding a `large` card and a `calm` card has no single label.** Under
`start-hour` that happens twice in 289 events; under `card-span/component/any`
it happens in 37 of 58. Any scheme that replaces an event by one answer and one
label is undefined on those events unless a tie-break is written down first.

---

## 6 · What collapsing does to the chance line

RULES 12 fixes the shuffle at 1,000 draws and the line at the best 1%. The
answer vectors used here are **synthetic**, drawn from seed `20260913`, and no
rule from the canteen book is evaluated: the point is the width of the null,
which is a property of the shuffle scheme and the labels, not of any signal.

Two ways of using an event map, measured:

| way | 1% boundary, `none` | 1% boundary, `start-hour` | 1% boundary, `card-span/component/any` |
|---|---|---|---|
| **block** — keep every card, permute whole events | 0.5588 | 0.5719 | 0.5654 (iid answers) / 0.5817 (event-constant answers) |
| **representative** — one card per event, n = events | 0.5654 (n = 306) | 0.5744 (n = 289) | **0.6552** (n = 58) |

For comparison, the card-level shuffle that TACTICS 7 is run with today gives
**0.5719** on the same labels.

Read straight:

- **Cluster-level permutation on its own barely moves the line** — between
  -0.013 and +0.020 across the eleven configurations. The reason is measured
  and is in §5: the cards inside an event mostly do **not** carry the same
  label, so they are not the duplicated observations a block permutation
  corrects for.
- **Replacing each event by one card moves it a great deal**, from 0.5719 to
  0.6552 at the widest reading, because the null is then drawn over n = 58
  instead of n = 306.

So Viktor's sentence — "a shuffle over 306 un-collapsed cards will produce a
chance line that is too easy to beat" — is supported by the second row and
**not** by the first. Which of the two a judge uses is part of the open
question below, and the size of the correction depends on it.

---

## 7 · The open question, written so three jurors can rule on it

Under RULES 33 an open question is never answered by one person. This is one: a
wording that can be read three ways, and a choice that changes the numbers.
**I do not answer it.** What a juror has to decide, and nothing more:

> **Q1. Which reading of RULES 13's "in the same hour" governs the count?**
> `start-hour` (289 events), `move-window` (131–168), or `card-span` (58–125).
>
> **Q2. If the reading is not `start-hour`: which resolution?** `component` or
> `greedy-clique`. They are not close: `card-span` gives 58 events under one and
> 116 under the other.
>
> **Q3. Does scope follow RULES 13's words "in several coins"** — i.e. may two
> moments of the same coin be one event, or not?
>
> **Q4. How is an event used in the count?** `representative` (one card per
> event; needs a written tie-break for the 2–60 events that hold both a `large`
> and a `calm` card, and a written rule for which card represents the event) or
> `block` (every card kept, whole events permuted).

Each of Q1–Q4 is procedure and definition, which RULES 33 puts inside a juror's
scope and outside mine. Every number a juror needs is in §5 and §6 and in
`exam-prep/collapse/collapse-summary.csv`.

**A second open question already on the books** is Sofia's §8 — may two calm
moments overlap each other? It bears on Q3 and it is not answered here either.

---

## 8 · What the judge's script must do

Written as a specification, so that "collapse" is not left to memory:

1. Read the sealed answer key as a moment list (`id,coin,kind,start_hour_utc`).
2. Call `collapse()` with the configuration the jurors ratified. Do not write a
   second implementation.
3. Check the partition (the function already stops if it is not one).
4. Compute every chance line through `chance_line()`, which will not run
   without the events.
5. Record the configuration string in the run record, next to the run number,
   so that a result can never be read without knowing which reading produced
   it.
6. Report the count of events, not only the count of cards, wherever RULES 12's
   1% boundary is quoted.

---

## 9 · What is still not done, by name

1. **The reading is not chosen** (§7). Until three jurors rule, a judge cannot
   run step 2 above. This is by design, not an omission.
2. **The tie-break for an event holding both kinds is not written.** It cannot
   be written before Q1 and Q4 are answered, because the number of such events
   is 2 under one reading and 60 under another.
3. **The exam's own event map does not exist**, and cannot: the exam moments
   live in `exam/`, which this run may not read. The engine takes them as an
   argument when the time comes.
4. **The money test is untouched.** TACTICS 8's random rival draws trades at
   random times; whether *it* needs the same treatment is not part of N-1 and
   is not measured here.

---

## 10 · Fingerprints

| file | SHA-256 |
|---|---|
| `scripts/15_event_collapse.py` | `f3de235883aac8b364aa5391c8371d50a9ecca288007f8d0bfaadadafe0ffb12` |
| `scripts/lab_cards.py` | `96b0eb01c502a40b4e76c864681763206ba627b268eedb7eb19984f81d9b928e` |
| `exam-prep/collapse/collapse-manifest.md` | `1d7a6a8e64e492ccea261ed3ea32bb3cb432a30b0c359c6d3092b493d450fc89` |
| `exam-prep/collapse/events.csv` | `7d887b831847b8838735ec0db334238cda51d9709ec6d7c97a1aa12f1faba727` |
| `exam-prep/collapse/collapse-summary.csv` | `6f3f5ce5748fc5e9d95086d07bbd6f7db9b00539b1df4445463a2df01f1400f5` |
| `exam-prep/collapse/shuffle-calibration.csv` | `145069adbb97faae4533c98bd009e7163200588942a5f57956a7eaf1981a6a66` |

A manifest carries the time it was written, so re-running a script rewrites its manifest text with a new timestamp even though the run number — the fingerprint of the inputs, RULES 29 — does not change. The run numbers are the stable identity; the hashes above identify the exact document text at the moment this file was written.

Run number `386d234b85269a21`. Two earlier run records
(`4af3b344a4898af0`, `5ba9140fe3c467fa`) are kept in
`exam-prep/collapse/runs/` as history: they are the same script at an earlier
stage of this session, superseded and not deleted (RULES 30).
