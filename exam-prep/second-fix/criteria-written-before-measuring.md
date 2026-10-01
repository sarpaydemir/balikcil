# Criteria written before measuring

Mateo · data engineer · second-fix run · written 2026-10-01T19:00:12Z (system
clock, RULES 23), before any of the measurements they govern were run.

This file is append-only. It exists so that a reader can check that each
criterion below was fixed before its result was known.

## K-1 · the rendering of the rebased `close` column (REVIEW §3.2, §3.6 item 2)

The rebased `close` column is printed at a fixed number of decimals `d`,
uniform across every card of the set being blinded.

Criterion: `d` is the smallest whole number of decimals (searched upward
from 2, the rendering under review) at which, on **no** card of the set, two
before-window hours print the same rebased `close` while the raw card printed
two different `close` values. In words: the blinding manufactures no tie that
the raw card did not already have.

Where it comes from: it is the same principle as decision D-6 of the first
run (`exam-prep/decisions-and-open-questions.md` D-6: "the smallest number
that fabricates nothing"), which the review did not dispute, applied to the
column the review found the blinding manufactures ties in. It contains no
number chosen by me: `d` is computed from the card set.

What it does not do: it does not remove ties the raw card already has (an
hour whose printed raw `close` repeats another hour's). Those are inherited
from the market and from the raw card writer, and are measured and named,
not removed.

The audit result on the re-rendered cards is reported whatever it is. If it
shows the channel open, it is reported open.

## K-2 · what the extended audit adds (REVIEW §3.6 item 2, last sentence)

For every column printed in a card's before table except `h`, two features:
the number of distinct printed values over the 24 rows, and the largest
number of rows sharing one printed value. One family per column group,
named `repeat-<group>`. Each new family is classified forced or removable by
the same rule the first run used for its families: it is forced only if the
column it reads is printed unchanged because the frozen canteen book or
TACTICS requires that column unchanged. Under that rule `repeat-chg` (the
`chg%` column, unchanged for S-1) is forced; every other `repeat-*` family is
removable.

## K-3 · the block shuffle (REVIEW §4.2, §4.5 item 1)

The replacement must satisfy the contract the withdrawn function's own
docstring states: "Whole events keep their internal pattern; only whole
events are moved." Test written before the replacement is run: (a) the
output is a permutation of card positions; (b) every event draws all its
answers from exactly one source event; (c) an answer vector that is constant
inside each event is still constant inside each event after permutation, on
every one of 1,000 draws, for every configuration and for the review's
three-event example. Any failure stops the script.

## K-4 · a granularity probe on the re-rendered `close` (appended 2026-10-01T19:08:56Z)

Appended after the collapse engine was re-run and before any blinded card was
re-rendered or audited. Printing `close` at more decimals can expose the
price step of the instrument (its tick relative to its price), which is a
coin signature of its own. One probe, reported next to the audit and **not**
added to the audit's families or its gate (K-2 fixed those): the smallest
non-zero absolute difference between two printed `close` values of the same
card, attacked with the audit's own two attacks and chance lines. It is
reported for the rendering under review and for the K-1 rendering, whatever
it shows.
