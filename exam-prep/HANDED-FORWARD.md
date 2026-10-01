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
