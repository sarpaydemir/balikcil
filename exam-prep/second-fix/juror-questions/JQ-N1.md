# JQ-N1 · How RULES 13's "single event" is counted — four parts, answered together

Referred by: Mateo · data engineer · second-fix run · 2026-10-01 (system clock).
This file re-issues, and replaces for juror use, the four questions first
written in `exam-prep/N-1-collapse.md` §7 (2026-09-19). Part 3 is re-worded
because its first wording offered an outcome one of its options could not
deliver; part 4 now names the block shuffle it is about. **You do not need to
open that earlier file, or anything else under `exam-prep/`.**

## What you open

- this file
- `RULES.md` (lines cited below)
- `TACTICS.md` (lines cited below)

Nothing else is needed. Every number below was counted by a script; its
source is named so that the referee can check it, but you need not open it.

## What you decide, and what you may not

You decide **procedure and definition only** (RULES 33): how the words of
RULES 13 and TACTICS 7 turn a set of moments into events, and how an event is
used when a chance line is computed. You do **not** decide a threshold, a
score, a trading rule, the number of shuffles or the 1% boundary (RULES 12
fixes those), and you do not change a rule.

Answer all four parts. Parts 1–4 are coupled (part 2 only matters for some
answers to part 1; part 3's options behave differently under part 2's
options; part 4's options behave differently under parts 1–3), so an answer
to one part that ignores the others may be impossible to carry out. If your
answers to the four parts cannot be carried out together, say so.

For each part: your answer; the file and line it rests on, quoted (RULES 34);
the strongest case against your answer; your confidence, 1–5.

"Other" is always allowed, with reasons. The options listed are the ones the
written rules' wording suggests to me; listing them is not a recommendation.

---

## The rule text

- `RULES.md` line 53–54: "Moments occurring in several coins in the same hour
  count as a single event. If the whole market moved together, that is one
  event."
- `TACTICS.md` line 127 (§7): "A moment appearing in several cards in the same
  hour counts as a single event."
- `TACTICS.md` line 44 (§2): "A moment's start is the hour at which the 24-hour
  movement began."
- `TACTICS.md` line 39 (§2): "Of two moments closer than 48 hours to each
  other, only the larger counts." (large moments of one coin)
- `TACTICS.md` line 43 (§2): calm moments are "At least 72 hours away from any
  large movement." TACTICS says nothing about two calm moments of one coin.
- `RULES.md` line 51–52 (RULES 12): "The answers are shuffled 1,000 times, and
  the real result must fall inside the best 1%."

A card shows 48 hours: the 24 hours before a moment's start and the 24 hours
after it. The exam shows only the 24 hours before.

## The scale of the choice, measured on the 306 observation cards

These are the observation cards (10 coins), not the exam cards; the exam's
event map will be computed the same way from the sealed answer key, and its
numbers will differ. They show how much the choice matters.

Source: `scripts/15_event_collapse.py`, run `756cf4ea156d92c3`,
`exam-prep/collapse/run-756cf4ea156d92c3/collapse-summary.csv`.

| reading / resolution / scope | events (from 306 cards) | events of 1 card | largest event | events holding a `large` and a `calm` card | events holding 2+ cards of the **same** coin | largest same-coin count in one event |
|---|---|---|---|---|---|---|
| no collapse | 306 | 306 | 1 | 0 | 0 | 1 |
| start-hour / – / any | 289 | 274 | 3 | 2 | 0 | 1 |
| start-hour / – / cross-coin | 289 | 274 | 3 | 2 | 0 | 1 |
| move-window / component / any | 131 | 49 | 8 | 52 | 15 | 2 |
| move-window / component / cross-coin | 136 | 56 | 8 | 52 | 10 | 2 |
| move-window / greedy-clique / any | 161 | 68 | 6 | 49 | 10 | 2 |
| move-window / greedy-clique / cross-coin | 168 | 78 | 6 | 50 | 0 | 1 |
| card-span / component / any | 58 | 10 | 20 | 37 | 25 | 5 |
| card-span / component / cross-coin | 62 | 13 | 20 | 39 | **26** | 4 |
| card-span / greedy-clique / any | 116 | 32 | 7 | 56 | 13 | 3 |
| card-span / greedy-clique / cross-coin | 125 | 41 | 7 | 60 | 0 | 1 |

---

## Part 1 · Which reading of "in the same hour"?

Two moments are "in the same hour" when:

- **start-hour** — they begin in the same clock hour. Ground: TACTICS 2 line
  44 defines a moment's start as an hour.
- **move-window** — their 24-hour movements share at least one clock hour
  (start hours at most 23 h apart). Ground: TACTICS 2 calls a moment a
  24-hour movement, so it occurs across 24 hours.
- **card-span** — their 48-hour cards share at least one clock hour (start
  hours at most 47 h apart). Ground: TACTICS 7 line 127 speaks of "a moment
  appearing in several cards in the same hour", and a card covers 48 hours.

## Part 2 · If not start-hour: how are chains resolved?

Under move-window and card-span the relation "shares an hour" is not
transitive: A may share an hour with B, and B with C, while A and C share
none. Some rule must turn it into separate events.

- **component** — anything joined by a chain is one event.
- **greedy-clique** — a stated convention, not an observation: repeatedly
  take the clock hour covered by the most still-unassigned moments, make
  those moments one event, remove them, repeat; ties go to the earliest hour,
  then the lowest card number. Every event then is a group of moments that
  all share one clock hour.

Under start-hour the relation is transitive and part 2 does not arise.

## Part 3 · May two moments of the same coin be one event? (re-worded)

RULES 13 says "in several coins"; TACTICS 7 says "in several cards".

The engine offers two scopes, and **what the second one does depends on your
answer to part 2**. The earlier wording of this question did not say so.

- **any** — two moments of one coin may be joined.
- **cross-coin** — two moments of one coin are never joined *directly*.
  - Under **greedy-clique** this means exactly what it says: no event holds
    two moments of one coin (table: 0 such events at move-window and
    card-span).
  - Under **component** it does **not**: a chain through a moment of another
    coin still puts two moments of one coin into one event. Measured:
    move-window/component/cross-coin has 10 such events; card-span/component/
    cross-coin has 26 (one holding 4 moments of one coin) — more than
    card-span/component/any's 25.

So if your answer is "two moments of one coin must never be one event", it can
be carried out with **greedy-clique** or with **start-hour** (under
start-hour no event in this card set holds two moments of one coin), but not
with **component**. If you want "never the same coin" together with
"component", say so explicitly: the engine does not offer it, and offering it
would need a further stated convention for breaking chains, which would itself
be a new open question.

A related question was referred separately by the canteen chair and is not
answered here: whether two **calm** moments of one coin may overlap at all
(`canteen/2026-09-19-sofia.md` §8). It changes how many same-coin overlaps
exist; it does not change what this part asks.

## Part 4 · How is an event used when a chance line is computed?

RULES 12 shuffles the answers 1,000 times. With events, there are two ways:

- **block** — every card is kept; whole events are moved. The implementation
  is the one in `scripts/15_event_collapse.py` as of the second-fix run
  (`block_shuffle_indices()`, SHA-256 of the script recorded in run
  `756cf4ea156d92c3`). **The earlier implementation, which the first wording
  of this question referred to, was withdrawn: it did not keep events whole.**
  The current one moves an event only onto an event of the same size, card
  for card in card order, because only then can an event keep its internal
  pattern. Consequence: **an event whose size no other event shares never
  moves.** Measured on the observation cards: 0 such events under start-hour;
  1 event (8 or 5 cards) under move-window; under card-span/component, 2
  events holding 23 cards (any) and 3 events holding 44 cards (cross-coin) of
  306; 0 under card-span/greedy-clique.
- **representative** — each event is replaced by one card; the shuffle runs
  over n = number of events. This needs two further definitions, and they
  belong to this part:
  - **4a.** Which card represents an event? (for example the earliest by
    start hour, ties by card number — that is the convention the calibration
    below used; it is not a ruling).
  - **4b.** What label does an event carry when it holds both a `large` and a
    `calm` card? (2 events under start-hour; 37–60 under the wider readings —
    see the table above.)

What the two ways do to the 1% boundary, measured with synthetic coin-flip
answers (no rule from the canteen book is evaluated). Source:
`exam-prep/second-fix/checks/instrument-checks-35925ca8acf60690.md` E-4.

| configuration | answers | card-level shuffle (no events) | block | representative (n) |
|---|---|---|---|---|
| none | independent per card | 0.5719 | 0.5588 | 0.5654 (306) |
| start-hour / any | independent per card | 0.5719 | 0.5523 | 0.5744 (289) |
| start-hour / any | one per event | 0.5654 | 0.5588 | 0.5744 (289) |
| move-window / component / any | one per event | 0.5621 | 0.5948 | 0.6031 (131) |
| move-window / greedy-clique / any | one per event | 0.5588 | 0.5980 | 0.5901 (161) |
| card-span / component / any | independent per card | 0.5719 | 0.5588 | 0.6552 (58) |
| card-span / component / any | one per event | 0.5686 | 0.5621 | 0.6552 (58) |
| card-span / greedy-clique / any | one per event | 0.5621 | 0.6013 | 0.6121 (116) |

How large random variation alone is: in the first row every event is one
card, so the block shuffle and the card-level shuffle draw from the same
distribution — and their boundaries still differ by 0.0131 (0.5588 against
0.5719). Differences of that size in this table are not evidence of anything.

---

## The strongest objection to referring this at all

That RULES 13 is clear and needs no juror. The measured spread (289 events
against 58 from the same 306 cards; across the configurations, answer types
and the two ways of part 4, the 1% boundary ranges from 0.5458 to 0.6613 in
the full table of the source file named above) is the reason it was referred: RULES 33 calls "a choice that changes the
numbers" an open question.
