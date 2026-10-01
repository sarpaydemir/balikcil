# Criteria written before measuring — fourth-fix run

Mateo · data engineer · fourth-fix run · written 2026-10-01T21:23:15Z (system
clock, RULES 23), before any of the measurements they govern were run.

This file is append-only. It exists so that a reader can check that each
criterion below was fixed before its result was known. The numbering
continues the third-fix run's K-5 … K-12
(`exam-prep/third-fix/criteria-written-before-measuring.md`).

## K-13 · the audit compares distances exactly (REVIEW-3 §4.1)

A new audit script, `scripts/29_identity_audit_exact.py`, is a copy of
`scripts/16_identity_audit.py` (third-fix version, SHA-256 `4a248f78…f4da`)
with one change: every comparison between two distances is made in exact
arithmetic. `scripts/16_identity_audit.py` itself is **not changed**, because
the juror file for JQ-R04-GATE, which jurors are answering now, names it as
the source of its figures.

Definition, the one REVIEW-3 q2 used: the squared distance between two cards
over the features a family uses is Σ_k (x_ik − x_jk)² / v_k, where x is the
feature value exactly as the audit computes it (a float, taken as the exact
rational it represents) and v_k is the exact sample variance (divisor n − 1)
of feature k over the card set. This is the squared distance between the
z-scored vectors in exact arithmetic. It is computed with integers after a
common scaling, so equality and order are exact. Which features a family
uses is decided exactly as in script 16 (no change in `features_used`); a
feature whose exact variance is zero contributes zero.

From the exact distances: the tie sets, the index-tie-break nearest
neighbour (the lowest card index inside the exact tie set), the tie range,
the tie-free score and its line, and the pair ranks of the pair AUC (ties by
exact equality). Shuffles, seed, line and everything else: unchanged.

Acceptance check of the code, fixed now: on the three card sets REVIEW-3 q2
ran (`strict-flags`, the 3-decimal set, the unrounded-rank set), for every
family q2 printed, the new audit's number of cards with a tied nearest
neighbour must equal q2's "tied cards exact", and its tie-free score and
line must equal q2's at 4 decimals. T3 and T4 must be byte-identical to the
third-fix audit's hour-linkage CSV and T4 record. If any of this fails, the
code is wrong and nothing from it goes into a juror file.

Reported, whatever it shows: every family on all seven card sets, and every
cell where the new audit differs from the third-fix audit (both NN versions,
the tie range, the tied-card count, pair AUC and every verdict).

## K-14 · the engine's key check reads nothing from the object it checks (REVIEW-3 §4.2)

`scripts/15_event_collapse.py`, changed in place: `chance_line()` and
`verify_event_map()` refuse any object whose type is not exactly `EventMap`
(no subclass); `chance_line()` computes the moments fingerprint with the
module function from the map's `.moments`, and the record's
`event_map_sha256` and `moments_sha256` with module functions, never with a
method of the map. Acceptance check: of REVIEW-3 q4's attempts, 0 is
accepted and 1–5 are refused; the third-fix G-1 attempts behave as before
(true map accepted, forged maps refused, `None` refused, omitted key a
`TypeError`); `main()` gives `events.csv`, `collapse-summary.csv` and
`shuffle-calibration.csv` byte-identical to run `bec532fa008e0e01`.

## K-15 · "keep the latest" as worded (REVIEW-3 §4.3, §1 condition 3)

`collapse()` gains `same_coin_keep` ("earliest", the default, the existing
path unchanged; or "latest"), allowed only with greedy-clique and
cross-coin. "latest" is implemented from the wording, over every clock hour:
in each round, every clock hour from the earliest still-unassigned start to
the latest start plus the window is a candidate; its coverage is the number
of coins with at least one still-unassigned moment covering it; the hour
with the largest coverage wins, ties to the earliest hour; of each coin's
moments covering that hour, the latest (by start hour, then card number)
joins the event. The configuration label gains `+latest`.

Acceptance check, fixed now, against two literal implementations written by
the reviewers, not by me: on the observation moments, at move-window and
card-span, the partition must be identical to REVIEW-3 q1's `literal()`
(keep latest) and to REVIEW-2 p1b's `greedy_latest()`; on q1's 200 random
moment sets (its seed and generator) at both definitions, identical to q1's
`literal()` in every set. The same literal path run with "earliest" must
equal the engine's existing path on the observation moments and on the same
random sets. If any of this fails, the code is wrong and nothing from it
goes into a juror file.

## K-16 · what the unrounded-rank rendering changes on a card (REVIEW-3 §5, the point no row answers)

For the referred question on the rank source, counted on the 306
observation cards, pairing each card of the unrounded-rank set with its
`strict-flags` card through the truth files' `source_card`, for each ranked
column: the number of cards on which the two renderings print a different
column; and the number of hours that print a value equal to another hour's
on the raw card (the same printed token in the same column of the same
card's before table) but a different rank from it on the unrounded-rank
card. No number is chosen; the counts are reported as they come out.
