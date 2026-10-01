# Handed forward — what later runs must do

Written by Mateo · data engineer · third-fix run · 2026-10-01 (system clock,
RULES 23). Append-only: a later run adds a dated section below; it does not
edit what is here.

This file is where the run that builds the exam cards and the run that writes
the judge's script (Greta) find what the pre-exam work requires of them. It
**replaces** `exam-prep/second-fix/SECOND-FIX.md` §8, `R-04-blindness.md` §8
and `N-1-collapse.md` §8 wherever they differ; those files are kept unchanged.
Each requirement names its source. Nothing here is a trading rule, a threshold
or a score.

The juror questions these requirements wait on are indexed in
`exam-prep/JUROR-QUESTIONS.md`.

---

## A · The run that builds the exam cards

**A-0 · Do not build exam cards until R-04 is closed on the observation
cards.** (SECOND-FIX §8; still in force: R-04 is not closed, see
`exam-prep/VERDICT.md`.) Whether a run already working under `exam/` may
proceed is the coordinator's, not this file's.

**A-1 · Blinding.** Use `scripts/17_blind_cards.py` with the configuration
the laboratory settles after JQ-R04-DATE and JQ-R04-CONTENT are ratified.
Record the full configuration string, including `close_dp` and, if used,
`rank_source`. (SECOND-FIX §8 step 1; `rank_source` added by the third-fix
run, K-10.)

**A-2 · The acceptance gate.** Run `scripts/16_identity_audit.py`, third-fix
version or later (SHA-256 `4a248f78c78376c3b58ce7b02bc20af2c035e8089529449d303c70061164f4da`
or a later version whose change list says what changed), on the exam cards
with `--truth` before the answer key is sealed. Record in the exam manifest:
both gate attacks on `ALL-removable`; the tie-free nearest-neighbour score and
the number of cards with a tied nearest neighbour; every `repeat-*` family;
`granularity-close`; T3; and both T4 counts (by start day and by release
day). Grade the gate on the statistic JQ-R04-GATE ratifies, and on nothing
else. (SECOND-FIX §8 step 2; REVIEW-2 §4.1, §4.2, §4.4.)

**A-3 · The granularity probe.** It is now the audit family
`granularity-close`, computed on the printed decimal text with exact
arithmetic. **Do not** run it "as `scripts/25_instrument_checks.py` E-3
shows": E-3 subtracts parsed floats and reports a nearest-neighbour "beats"
at 2 decimals that the printed cards do not support (REVIEW-2 §4.2). This
replaces SECOND-FIX §8 step 3.

**A-4 · Nearest-neighbour verdicts on tied features.** For any family on
which `cards_with_tied_nn` is above zero, the nearest-neighbour score with
the index tie-break is a property of the card numbering (REVIEW-2 §4.1). Do
not quote its verdict alone: quote the tie-free score with its own chance
line, and the tie range.

**A-5 · B-1 cannot fire on an exam card — check that it is so.** Before
sealing the key, confirm that no exam card's contract is `AVGOUSDT` or
`NOKUSDT` (the two contracts B-1's frozen trigger names; both are observation
coins, and the draw manifest records the observation and exam lists as
disjoint). Record the check in the exam manifest. If either contract is
present, the statement `exam-prep/third-fix/juror-questions/JQ-B1.md` is void
and the question goes back to the coordinator. (REVIEW-2 §5, JQ-B1.)

**A-6 · Calm moments of one coin.** If JQ-CANTEEN-8 is ratified "no", the
exam's calm moments must be drawn so that no two of one coin overlap in the
sense ratified in its part b. Write down, before the draw, how the draw
enforces it, and report it. If it is ratified "yes", nothing changes.
(JQ-CANTEEN-8.)

**A-7 · The exam manifest.** Record the configuration string, the audit run
number, the gate figures of A-2 and every channel the audit names with its
size, so that nobody later reads "blind" as "perfectly blind".
(`R-04-blindness.md` §8 step 5.)

**For your information, not a requirement** (REVIEW-2 §4.5): on every
blinded observation set the card numbers `B###` are assigned by
`random.Random(20260913).shuffle` over the source order, and 20260913 is the
draw number printed in TACTICS 1. If the exam's source order carries coin or
time, anyone with tools and the public seed can undo the numbering. An exam
candidate has no tools (RULES 10). Nobody has decided whether the exam's
numbering should use a different method; that decision is not this file's.

---

## B · The run that writes the judge's script (Greta)

**B-1 · The event map.** Build it with `collapse()` from
`scripts/15_event_collapse.py` under the configuration JQ-N1 ratifies, or
with `identity_map()`, labelled, only where a rule asks for a card-level
line. Do not write a second implementation. If the ratified configuration
is greedy-clique with `cross-coin` and the jurors ruled for keeping the
**latest** moment of a coin, the engine does not offer that yet: it must be
added, checked and recorded before it is used. (N-1 §8; JQ-N1 part 2.)

**B-2 · Check the moments against the sealed key — every time.** Read the
moments (`id, coin, kind, start hour`) from the **sealed answer key file
itself**. Before using it, check its SHA-256 against the fingerprint
recorded when it was sealed (RULES 9). Compute `moments_fingerprint()` on
those moments and pass the result as `key_moments_sha256` to **every**
`chance_line()` call. The engine (third-fix version, SHA-256
`e59cecb7c8e455f5cd8625130b962ba343bc168f53699667e5ac132ddbed2fe6` or later)
refuses to run without it and refuses a map made from other moments. It
cannot tell whether the value really came from the key: passing the event
map's own fingerprint would make the check empty, and that is exactly what
this requirement forbids. Take `labels` from the same key. (REVIEW-2 §1
condition 2, §4.3.)

**B-3 · The record.** Store the whole record `chance_line()` returns, minus
the null list, next to the run number. It must show `key_check: matched` and
a `key_moments_sha256` equal to the value computed in B-2. (SECOND-FIX §8;
REVIEW-2 §4.3.)

**B-4 · Representative mode.** Pass the representatives the ratified rule
names (JQ-N1 part 4a) and, for an event holding both a `large` and a `calm`
card, the label the ratified rule gives it (part 4b). (SECOND-FIX §8.)

**B-5 · Report events, not only cards,** wherever RULES 12's 1% boundary is
quoted. (`N-1-collapse.md` §8 item 6.)

---

## C · Instruments changed by the third-fix run

| script | what changed | earlier runs |
|---|---|---|
| `scripts/15_event_collapse.py` | `chance_line()` requires `key_moments_sha256`; `moments_fingerprint()` added | run `756cf4ea156d92c3` kept; run `bec532fa008e0e01` reproduces its outputs byte for byte |
| `scripts/16_identity_audit.py` | tie-free nearest neighbour and tie range; family `granularity-close`; T4 by release day; T3 sees ranked columns | second-fix runs kept |
| `scripts/17_blind_cards.py` | `--rank-source unrounded` (default unchanged: the 1,224 reviewed cards are reproduced byte for byte) | — |
| `scripts/26_third_fix_checks.py` | new | — |

`scripts/25_instrument_checks.py` is a record of the second-fix run. Re-run
against the third-fix engine, its E-2 attempts would now be refused for want
of `key_moments_sha256`; that is expected and is not a defect of either.

---
---

# Section added by the fourth-fix run · 2026-10-01 — the complete list in force

Mateo · data engineer · fourth-fix run · appended 2026-10-01 (system clock,
RULES 23). **Nothing above this line was changed:** the first 7,206 bytes of
this file are the file as the third review found it (SHA-256
`d864fb37c769a11f60d2ce38248ef212acbaf919f62f2406c1b4b0bd625360c0`).

**This section is complete.** It restates every requirement still in force
from sections A–C above, from `R-04-blindness.md` §8, `N-1-collapse.md` §8
and `second-fix/SECOND-FIX.md` §8, with the changes the third review
(`exam-prep/REVIEW-3.md` §7) required. **A later run reads this section and
nothing earlier:** a requirement written earlier and not restated here is not
in force, and section D below names each one with the reason. Each
requirement ends with its check — a question the run that must meet it can
answer yes or no — and names its source. Nothing here is a trading rule, a
threshold or a score.

---

## A · Before any exam card is built

**A-0 · R-04 must be closed first.** Do not build exam cards until a
data-engineer run has appended to `exam-prep/VERDICT.md` a section that
declares R-04 **closed** and shows, with run numbers, that every one of
A-0.1 to A-0.6 is met; and the review of that run agrees. Until then, A-0
holds. Whether a run already working under `exam/` may proceed is the
coordinator's.
*Check: does `exam-prep/VERDICT.md` carry such a section, with A-0.1 to A-0.6
each marked met with its run number, and a later review agreeing?*
(Source: SECOND-FIX §8; third-fix A-0; REVIEW-3 §7 A-0.)

The standard R-04 is closed against — `R-04-blindness.md` §2 as amended by
SECOND-FIX §7, with the two points REVIEW-3 §7 found unnamed made explicit:

- **A-0.1 · Rulings.** JQ-R04-GATE, JQ-R04-DATE-a, -b, -c and
  JQ-R04-CONTENT-a, -b, -c each have an outcome ratified under RULES 33–35
  and recorded in `LEDGER.md`.
  *Check: seven ratifications recorded, one per identifier?*
- **A-0.2 · Configuration.** The run declaring R-04 closed records one
  blinding configuration string of `scripts/17_blind_cards.py` (A-1) that
  uses only renderings the ratified outcomes of A-0.1 permit and removes or
  masks every field they require removed or masked.
  *Check: is the string recorded, and does each of its elements trace to a
  ratified outcome or to the `strict-flags` default of `R-04-blindness.md`
  §8 step 2?*
- **A-0.3 · Level 1** (`R-04-blindness.md` §2). On the 306 observation cards
  blinded with that configuration, audited with `scripts/29_identity_audit_exact.py`
  (A-2), every level family that still has features — `price-level`,
  `volume-level`, `trades-level`, `openint-level`, `depth-level`,
  `ratio-level`, `taker-buy`, `wikipedia-presence`, `btc-eth` — beats
  **none** of its three lines: pair AUC, nearest neighbour (index
  tie-break), nearest neighbour (tie-free). Level 1 says "must fail both
  attacks"; it was written before the two nearest-neighbour versions
  existed, and they can disagree (THIRD-FIX C3-11). Requiring both avoids
  choosing one. If a family beats exactly one of the two nearest-neighbour
  lines, R-04 is **not** closed on it and the disagreement goes to the
  coordinator as a possible open question (RULES 33); this file does not
  settle it.
  *Check: in the audit CSV, is `auc_beats_chance`, `nn_beats_chance` and
  `nn_tie_free_beats_chance` "no" on every one of these rows?*
- **A-0.4 · The gate** (Level 2 as `R-04-blindness.md` §8 step 3 and
  SECOND-FIX §7 apply it). On the same audit, the `ALL-removable` row does
  not fail under the statistic JQ-R04-GATE ratifies. If that statistic reads
  the nearest neighbour and `cards_with_tied_nn` on the row is above zero,
  grade the row with both nearest-neighbour versions; if they give different
  results, the gate is **not** graded and the coordinator is told (open
  question; REVIEW-3 §7 A-2 gap 1). `ALL` is reported, and its excess over
  `ALL-removable` is named as the forced residual (`R-04-blindness.md` §7),
  not graded.
  *Check: does the gate row pass under the ratified statistic, with
  `cards_with_tied_nn` = 0 or both versions agreeing?*
- **A-0.5 · The clock-hour line** (`R-04-blindness.md` §2 as amended by
  SECOND-FIX §7: no printed field may identify which clock hours or which
  calendar date a card covers). Whether a field identifies them in the
  sense of the rule is what JQ-R04-DATE-a, -b and -c decide; no written
  standard gives a number for it. So: every field those ratified outcomes
  require removed or masked is absent from every blinded card, and the T3
  and T4 tables of the audit are recorded, not graded.
  *Check: is each such field absent from all 306 blinded cards (by reading
  the blinding manifest and grepping the cards), and are T3 and T4 in the
  record?*
- **A-0.6 · What the frozen book needs survives** (`R-04-blindness.md` §8
  step 4, which the third-fix section did not restate — REVIEW-3 §7):
  `scripts/17_blind_cards.py` stops if a before-window open-interest zero
  (B-3) is lost, if the largest `|chg%|` of a card moves, or if a B-4 depth
  run is lost or manufactured; with `--rank-source unrounded` it also stops
  if any ranked source value does not round to the printed raw token.
  *Check: did the blinding run complete, and does its manifest report the
  B-3 hours, the largest `|chg%|` and the B-4 runs as unchanged (on the 306
  observation cards: 4 cards with a before-window open-interest zero, 5 with
  a depth run, 306 of 306 with the largest `|chg%|` kept)?*

**A-1 · Blinding.** Build the exam cards with `scripts/17_blind_cards.py`
(never by editing `09_write_cards.py`'s output by hand), with exactly the
configuration string recorded under A-0.2 — including `close_dp` and, if
used, `rank_source`. Owner of the string: the run that declares R-04 closed;
procedure: A-0.2. The `rank_source` choice is open until JQ-R04-CONTENT-c is
ratified.
*Check: does the exam manifest's configuration string equal, byte for byte,
the one recorded under A-0.2?*
(Source: `R-04-blindness.md` §8 steps 1–2; SECOND-FIX §8 step 1; third-fix
A-1; REVIEW-3 §5, §7 A-1.)

**A-2 · The acceptance gate on the exam cards.** Before the answer key is
sealed, run `scripts/29_identity_audit_exact.py` (SHA-256
`cfc4bdcb6f1ee65430ac08fad0d085ff6e83510ac4d741145aa32cde3487d03f`, or a
later version whose header lists what changed) on the exam cards with
`--truth`. **Not** `scripts/16_identity_audit.py`: it finds ties by
floating-point equality and under-counts `cards_with_tied_nn` (REVIEW-3
§4.1). Record in the exam manifest: both gate attacks on `ALL-removable`
(index and tie-free nearest neighbour, pair AUC, each with its line); the
number of cards with a tied nearest neighbour; every `repeat-*` family;
`granularity-close`; T3; both T4 counts. Grade the gate as A-0.4 says, on
nothing else.
*Check: is the audit run's `script_sha256` the one above (or a listed later
version), was it run before the key's sealing time, and are all the listed
figures in the manifest?*
(Source: `R-04-blindness.md` §8 step 3; SECOND-FIX §8 step 2; third-fix A-2;
REVIEW-3 §7 A-2.)

**A-3 · The granularity probe** is the audit family `granularity-close`
(printed decimal text, exact arithmetic). Do not run it as
`scripts/25_instrument_checks.py` E-3 does.
*Check: is the figure in the manifest taken from the A-2 audit's
`granularity-close` row?* (Source: third-fix A-3.)

**A-4 · Nearest-neighbour verdicts on tied features.** For any family whose
`cards_with_tied_nn` is above zero, do not quote the index-tie-break verdict
alone: quote the tie-free score with its own line, and the tie range.
*Check: does every quoted nearest-neighbour verdict on such a family carry
the tie-free score, its line and the tie range?* (Source: third-fix A-4.)

**A-5 · B-1 cannot fire on an exam card — check that it is so.** Before
sealing the key, confirm that no exam card's contract is `AVGOUSDT` or
`NOKUSDT`, and record the check in the exam manifest. If either is present,
the statement `exam-prep/third-fix/juror-questions/JQ-B1.md` is void and the
question goes back to the coordinator.
*Check: is the check recorded, with the answer "neither present"?*
(Source: third-fix A-5.)

**A-6 · Calm moments of one coin.** If JQ-CANTEEN-8 is ratified "no", the
exam's calm moments are drawn so that no two of one coin overlap in the sense
ratified in its part b; how the draw enforces it is written down before the
draw and reported. If "yes", nothing changes.
*Check: under "no", is the method written before the draw (by its
timestamp), and does a count of same-coin calm pairs at the ratified spacing
give 0?* (Source: third-fix A-6.)

**A-7 · The exam manifest** records the configuration string, the audit run
number, the figures of A-2, and every channel the audit names with its size
— including the forced residuals of `R-04-blindness.md` §7 — so that nobody
later reads "blind" as "perfectly blind".
*Check: are these items in the manifest?* (Source: `R-04-blindness.md` §8
step 5; third-fix A-7.)

**For information, not a requirement.** (1) The card numbers `B###` of every
blinded observation set are assigned by `random.Random(20260913).shuffle`
over the source order, and 20260913 is printed in TACTICS 1; if the exam's
source order carries coin or time, anyone with tools and the public seed can
undo the numbering. Nobody has decided whether that matters for the exam
(REVIEW-2 §4.5). (2) REVIEW-3 §6 recommends, without requiring, that the run
writing the exam instructions for the recipe-holding candidate leave B-1 out
on the frozen scope of `canteen/2026-09-19-sofia.md` lines 205–212 ("it
applies in the money test only"). (3) Under its frozen trigger B-1 blocks
nothing in the money test either: the money-test set excludes the
observation coins (`scripts/04_draw.py` lines 120–127; REVIEW-3 §4.5). This
bears on the frozen book, not on R-04 or N-1, and is not decided here.

---

## B · The run that writes the judge's script (Greta)

**B-1 · The event map.** Build it with `collapse()` from
`scripts/15_event_collapse.py` (SHA-256
`002bb40639dee684fd4b7c653d2db45ec2c4527ade38d565e765619a9eebf4e6` or a
later version whose header lists what changed) under the configuration
JQ-N1 ratifies — including `same_coin_keep="latest"` if the jurors ruled for
keeping the latest moment of a coin under greedy-clique with cross-coin — or
with `identity_map()`, labelled, only where a rule asks for a card-level
line. Do not write a second implementation. "Latest" is in the engine since
the fourth-fix run and was checked against two literal implementations
(`scripts/30_fourth_fix_checks.py`, run `516027c6c9f215d6`, H-2). If the
engine has changed since, re-run that check before using it.
*Check: does the run record's `config` equal the ratified configuration
(ending in `+latest` exactly when "latest" was ratified), and, if the
engine's SHA-256 differs from the one above, does a re-run of
`scripts/30_fourth_fix_checks.py` report H-2 accepted?*
(Source: `N-1-collapse.md` §8 steps 1–3; third-fix B-1; REVIEW-3 §1
condition 3, §7 B-1.)

**B-2 · Check the moments against the sealed key — every time.** Read the
moments (`id, coin, kind, start hour`) from the **sealed answer key file
itself**; first check its SHA-256 against the fingerprint recorded when it
was sealed (RULES 9). Compute `moments_fingerprint()` on those moments and
pass it as `key_moments_sha256` to **every** `chance_line()` call. Take
`labels` from the same key. Passing the event map's own fingerprint would
make the check empty and is forbidden.
*Check: in the judge's code, is `key_moments_sha256` computed only from the
moments read out of the key file, after that file's hash check?*
(Source: third-fix B-2; REVIEW-2 §4.3.)

**B-3 · The record, and an independent recomputation.** Store the whole
record `chance_line()` returns, minus the null list, next to the run number;
it must show `key_check: matched`, a `key_moments_sha256` equal to B-2's
value, and the configuration string. Then, separately, recompute the event
map's fingerprint from the sealed key alone: read the key's moments, call
`collapse()` with the recorded configuration, compute
`event_map_fingerprint()` on the result, and compare it with the record's
`event_map_sha256`. The judge's script does this in a step that reads only
the key file and the record; the review of the judge's run repeats it. The
engine refuses forged maps, subclasses and patched methods (H-1 of run
`516027c6c9f215d6`), but no check inside one process can stop a caller who
edits the engine's own functions; this recomputation is what catches that.
*Check: does the record show `key_check: matched` and the configuration, and
does the separate recomputation give the record's `event_map_sha256`?*
(Source: `N-1-collapse.md` §8 steps 4–5; SECOND-FIX §8; third-fix B-3;
REVIEW-3 §1 condition 2, §4.2, §7 B-2/B-3.)

**B-4 · Representative mode.** Pass the representatives the ratified rule
names (JQ-N1 part 4a) and, for an event holding both a `large` and a `calm`
card, the label the ratified rule gives it (part 4b).
*Check: are the representatives and the mixed-event labels those of the
ratified rule, and is `representatives_sha256` in the record?*
(Source: SECOND-FIX §8; third-fix B-4.)

**B-5 · Report events, not only cards,** wherever RULES 12's 1% boundary is
quoted.
*Check: does every quoted boundary carry its event count?*
(Source: `N-1-collapse.md` §8 step 6; third-fix B-5.)

---

## C · Instruments changed or added by the fourth-fix run

| script | what changed | earlier runs |
|---|---|---|
| `scripts/15_event_collapse.py` (`002bb406…e4f6`) | `chance_line()` and `verify_event_map()` refuse anything but exactly `EventMap`; every fingerprint is computed by module functions; `same_coin_keep="latest"` added (literal, every clock hour) | run `bec532fa008e0e01` kept; runs `721b2448f1722ccf` and `a0ecf6970d86b199` reproduce its three CSVs byte for byte |
| `scripts/29_identity_audit_exact.py` (`cfc4bdcb…d03f`) | new: a copy of `16_identity_audit.py` that compares distances exactly | — |
| `scripts/16_identity_audit.py` | **not changed** (the JQ-R04-GATE file names it as a source while jurors answer it); its tie counts are float-based and its runs remain what they are | — |
| `scripts/30_fourth_fix_checks.py`, `scripts/31_juror_file_check_fourth.py` | new | — |

`scripts/18_residual_diagnostic.py` and `scripts/27_gate_sensitivity.py`
still import `16_identity_audit.py`, so they compare distances in floating
point. On every gate row measured no card has a tied nearest neighbour under
either arithmetic; for any other use they would need the exact comparison
first.

---

## D · Earlier requirements not restated, and why

| earlier requirement | why it is not restated |
|---|---|
| `R-04-blindness.md` §8 step 2 ("use `strict-flags` unless the laboratory rules otherwise") | replaced by A-1 / A-0.2: the configuration is the one recorded by the run that closes R-04; `strict-flags` remains the default it starts from |
| `R-04-blindness.md` §8 step 3's single sentence ("if `ALL-removable` beats its chance line … the gate has failed") | replaced by A-0.4 and A-2 (which line decides is JQ-R04-GATE) |
| SECOND-FIX §8 step 3 (run the K-4 probe as E-3 shows) | replaced by A-3 (third-fix A-3 already did) |
| third-fix A-2's "`scripts/16_identity_audit.py`, third-fix version or later" | replaced by A-2: the exact audit, because the third-fix audit under-counts ties |
| `N-1-collapse.md` §8 steps 1–6, SECOND-FIX §8 (judge), third-fix B-1 … B-5 | restated in B-1 … B-5 |
| `R-04-blindness.md` §8 steps 1, 4, 5; third-fix A-0, A-1, A-3 … A-7 | restated in A-0 … A-7 |
