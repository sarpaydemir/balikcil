# Criteria written before measuring — third-fix run

Mateo · data engineer · third-fix run · written 2026-10-01T20:11:31Z (system
clock, RULES 23), before any of the measurements they govern were run.

This file is append-only. It exists so that a reader can check that each
criterion below was fixed before its result was known. The numbering
continues the second-fix run's K-1 … K-4
(`exam-prep/second-fix/criteria-written-before-measuring.md`).

## K-5 · the granularity probe joins the audit (REVIEW-2 §4.2)

The K-4 probe — the smallest non-zero difference between two printed `close`
values of one card's before table — is computed on the **printed decimal
text**, with exact decimal arithmetic, and becomes the audit family
`granularity-close` in `scripts/16_identity_audit.py`.

Classification, by K-2's rule unchanged: a family is forced only if the
column it reads is printed unchanged because the frozen canteen book or
TACTICS requires that column unchanged. `close` is printed rebased (TACTICS 6),
not unchanged, so `granularity-close` is **removable** and sits inside `ALL`
and `ALL-removable`.

Acceptance check of the code, fixed now: on the `strict-flags` set the
feature must take 13 distinct values and on `strict-flags-k1` 91, and its
pair AUC must equal REVIEW-2's exact recomputation (p3 D: 0.596809 and
0.630049). If either differs, the code is wrong and is not used.

Whatever the gate row then shows is reported, whether or not it changes.

## K-6 · a nearest-neighbour score that does not depend on card order (REVIEW-2 §4.1)

The reviewed score (nearest neighbour, distance ties broken by the lowest card
index) stays, unchanged, in its own column, so nothing measured before
disappears. Next to it, for every family:

- **tie range** — the lowest and highest value the reviewed score can take
  over every tie-break;
- **tie-free score** — for every card, the share of its equally-nearest other
  cards that are the same coin, averaged over cards. This is the exact mean of
  the reviewed score over all tie-breaks. Its chance line is computed from the
  same 1,000 label shuffles (RULES 12), with the same statistic — not by
  comparing it with the reviewed score's line.

Acceptance check of the code, fixed now: the tie range and the tie-free score
must reproduce REVIEW-2's p3b columns "NN lowest", "NN highest" and "NN mean"
on `strict-flags` for every family p3b lists; where a family has no tied
card the three scores must be equal.

Which nearest-neighbour score a gate reads is **not** decided here. On a
family where no card has a tied nearest neighbour the two coincide.

## K-7 · release names counted by the day the release falls (REVIEW-2 §4.4)

T4 keeps its second-fix count (by the card's start day) and adds the count by
release day: card start hour plus the printed offset in hours. A name printed
without an offset is keyed by the card's start day, marked as such. Acceptance
check: on `strict-flags` the release-day count must reproduce REVIEW-2 p2 A
(13 names, 18 cards); the start-day count must stay 11 names, 13 cards.

## K-8 · the calm-overlap counts for JQ-CANTEEN-8 (REVIEW-2 §4.6, §5)

"Overlap" is taken from the only written definition in the laboratory's
files: `data/overlap/overlap-manifest.md`, "Window definition": "Two cards
*share a clock hour* when their 48-hour spans have at least one hour in
common." Counted from `data/overlap/pairs.csv` (run `12ce59e2902a0034`): every
overlapping pair by the two cards' kinds and by same / different coin; and,
because an exam card shows only its before window (TACTICS 6), the same
counts for pairs whose **before** windows share an hour. No spacing number is
chosen: the counts are reported for the definitions that exist.

## K-9 · the representative-column noise in JQ-N1 part 4 (REVIEW-2 §3.3, §5)

The representative null is computed exactly (hypergeometric), not by
simulation, for every row the juror table shows, using the same synthetic
answer vectors and the same representatives (earliest start hour, ties by
card number) as `scripts/15_event_collapse.py`. Acceptance check: the exact
1% points must reproduce REVIEW-2 p5's column "exact 1% point"; if they do
not, the code is wrong and nothing from it goes into a juror file.

## K-10 · ranking the unrounded source values (appended 2026-10-01T20:22:29Z)

Appended after K-5 … K-9 were measured and before any of what follows was
built or looked at. The second-fix run named, and did not try, one
engineering route against the repeat channel of the ranked columns (SECOND-FIX
§4): rank each hour's **unrounded source value** instead of the rounded value
the raw card prints, so that only genuine repeats stay equal. It does not
depend on any juror answer, so this run tries it (instruction, "what must be
true" item 4).

What is built: `scripts/17_blind_cards.py` gains `--rank-source unrounded`
(default `printed` = the existing behaviour, unchanged). With it, every column
the `rank` rendering ranks (`quote vol`, `trades`, `taker buy%`, `open int`,
`L/S acct`, `top L/S pos`, `taker L/S`, `depth -1%`, `depth +1%`) is ranked on
the value the card writer had before it rounded: the hourly klines for the
first three, the card writer's own hourly caches of the 5-minute metrics and
of the order-book depth for the rest — read, never rewritten. Every other
part of the card is unchanged. Configuration audited: `strict-flags` with only
this switch changed.

Guards, fixed now; any failure stops the script and is reported as the
result:

1. **The source is the card's source.** For every card, every hour and every
   ranked column, formatting the source value with the card writer's own
   formatting function (`scripts/09_write_cards.py`) must give exactly the
   token the raw card prints. One mismatch stops the script.
2. **B-3 survives.** The before-window hours printing an open-interest zero
   are the same on the raw and the blinded card.
3. **B-4 survives and is not manufactured.** For both depth columns, the
   before-window hours that sit in a run of three or more identical printed
   values are the same on the raw card and on the blinded card. A run the
   raw card prints only because of rounding would be lost here; if any is
   lost, the script stops, names the cards, and the route is reported as not
   available without changing what B-4 reads — a frozen rule (RULES 6) —
   and nothing further is built on it.
4. **S-1 is untouched.** `chg%` is printed unchanged (it is not ranked).

What is reported, whatever it shows: the audit of the new set with the
third-fix audit, every family, both gate attacks, and the same against
`strict-flags`. Whether the route closes the channel is read off those
numbers; no number is chosen here.

## K-11 · T3 sees a ranked column (appended 2026-10-01T20:25:42Z)

Appended before the re-run it governs. T3's `quote vol` row looked for a
column named `quote vol`, which a blinded card prints as `quote vol r`, so on
every blinded set it reported "not printed" (SECOND-FIX §4 item 3). The unit
suffix is now stripped, exactly as `card_features()` already does, and the row
is computed on the ranked column. No row is added and no other part of the
audit changes; T1, T2 and T4 must come out identical to the runs of the
version before this change (`4a248f78…` replaces `6437fcff…`), and that is
checked. Whatever T3 then shows is reported.

## K-12 · gate sensitivity on the unrounded-rank set (appended 2026-10-01T20:27:02Z)

Appended after K-10's audit was read (it beats both gate lines with smaller
margins than `strict-flags`) and before what follows was computed. Purpose:
to say, for the coordinator, whether R-04's closure could depend on juror
answers alone or also on engineering not yet found. It is a sensitivity
check of feature subsets, like REVIEW-2's p6 — **no rendering is built, and
nothing from it goes into a juror file**, so that no juror chooses a
definition by its effect (RULES 6).

On the K-10 set, with the third-fix audit's own functions and chance lines,
the gate row is recomputed (a) as audited; (b) without the families read
from the price column (`price-level`, `repeat-close`, `granularity-close`)
— what would be left if no price column were printed, which is one of the
options JQ-R04-CONTENT part b offers; (c) as (b) and also without the
trade-count column's features — what would be left if JQ-R04-CONTENT part a
were answered "yes" and the column left out. Both attacks, the tie-free
nearest neighbour, whatever they show.
