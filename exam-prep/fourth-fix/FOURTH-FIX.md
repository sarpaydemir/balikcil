# Fourth fix — acting on `exam-prep/REVIEW-3.md`

Mateo · data engineer · first clock read 2026-10-01T21:22:37Z, this file
written after 2026-10-01T21:45:32Z (system clock, RULES 23) · free disk at
21:22:37Z 12,401,352,704 bytes, at 21:45:32Z 12,398,252,032 bytes · nothing
was downloaded.

This file is the working of the run that acts on the third review. The
verdict, with an outcome for every item, is appended to
`exam-prep/VERDICT.md`. What later runs must do is in the section appended to
`exam-prep/HANDED-FORWARD.md` by this run, which is complete on its own. The
juror files are in `exam-prep/fourth-fix/juror-questions/`, indexed in
`exam-prep/JUROR-QUESTIONS.md`.

**Opened:** `exam-prep/` (every working file, review, verdict, index,
handed-forward file, juror file, probe and probe output I needed; card files
were read by script, and one blinded card, `B001` of the unrounded-rank set,
was printed once to see the column names); `canteen/2026-09-19-sofia.md`
(lines 100–420, 660–672, 900–945); `RULES.md`, `TACTICS.md` (whole);
`scripts/` (15, 16, 17, 26, 28, 06 in part; every file I ran or changed);
`cards/` (by script, and the header line of `C175` by `grep`).
**Not opened:** `exam/`, `decisions/`, `instructions/`, `LEDGER.md`,
`reports/`, `external/`, `notes/`, `data/` (read only by the scripts that
read it before me; none of my scripts reads it),
`canteen/2026-09-19-viktor.md`, `TEAM.md`, the root `README.md` (allowed, not
needed), any `scripts/exam_*` (not read, not run; three of their names
appeared once in a directory listing of `scripts/__pycache__/`), git history
(no `git` command was run), anything outside the Balıkçıl folder. No memory
or session-log search. No bytecode cache was written
(`PYTHONDONTWRITEBYTECODE=1`; checked afterwards).

**Not written:** `exam-prep/third-fix/juror-questions/JQ-R04-GATE.md` and
`scripts/16_identity_audit.py` (the GATE file names it as its source), nor
anything else a juror on JQ-R04-GATE is pointed at (`RULES.md`,
`TACTICS.md`).

---

## 1 · How REVIEW-3's items are numbered here

REVIEW-3 numbers its N-1 conditions (§1 (1)–(3)) and states its other
demands inside sections. Each demand gets one number here; `VERDICT.md`
reports by these numbers.

| item | REVIEW-3 | what it requires |
|---|---|---|
| R3-1 | §1 N-1 (1); §3 R2-1; §4.3; §5 JQ-N1-2 and "What must change" | correct JQ-N1 part 2's "keep the latest" figures and the sentence that invites the wrong implementation; then ratification |
| R3-2 | §1 N-1 (2); §3 R2-2; §4.2; §7 B-2, B-3 | harden the engine's key check, or make B-3 recompute the event map's fingerprint from the sealed key |
| R3-3 | §1 N-1 (3); §4.3; §7 B-1 | "keep the latest", if ratified, implemented over every clock hour and checked against a literal implementation; B-1 must name what to check against |
| R3-4 | §3 R2-5, R2-12; §4.1; §5 CONTENT-a (v), CONTENT-b; §7 A-2 gap 2; §11 item 9 | compare distances exactly (or state a tolerance); replace the figures that are not the exact tie averages |
| R3-5 | §4.4; §5 JQ-R04-CONTENT-a | state part a's premise for both built renderings, or without figures |
| R3-6 | §5, "the point no row answers" | the rank source is an open question; it belongs with JQ-R04-CONTENT unless the coordinator records why it is engineering |
| R3-7 | §3 R2-10; §5, couplings paragraph | neither coupled group can be commissioned until its unfit parts are fixed |
| R3-8 | §7 A-0 | name the standard that closes R-04, including which nearest-neighbour version Level 1 reads |
| R3-9 | §7 A-1 | an owner and a procedure for the configuration; `rank_source` is open |
| R3-10 | §5 JQ-R04-GATE; §7 A-2 gap 1 | which nearest-neighbour version grades the gate if the exam gate row has a tied nearest neighbour |
| R3-11 | §7, "the file as a whole" | one place to read what is in force; restate `R-04-blindness.md` §8 step 4 |
| R3-12 | §5 JQ-CANTEEN-8 (two minor points, "no effect on any outcome") | — (the row is fit) |
| R3-13 | §5, couplings: GATE's optional part and JQ-N1 both read RULES 13 | — (the referee "may want to check") |
| R3-14 | §6, "Recommended, not required" | leave B-1 out of the recipe-holder's exam instructions on the frozen scope |
| R3-15 | §4.5 | named, "not a review item"; decides nothing |
| R3-16 | §8 (R2-18) | identifiers carry a question's subject; undecided, the coordinator's |
| R3-17 | §10 (a) | VERDICT's third-fix point 2 (and THIRD-FIX §4.5) must not reach a GATE juror or the referee |
| R3-18 | §3 R2-16 | two verdicts sit at their line and are decided by the seed |

---

## 2 · What was done, item by item

### R3-1 · JQ-N1 part 2 — done; ratification referred

`exam-prep/fourth-fix/juror-questions/JQ-N1.md`. Part 2 now states both
conventions symmetrically ("earliest", "latest", each with its card-number
tie-break), gives the figures of the wording — move-window 168 and 168
events, 4 in one partition only; card-span 125 and 124, 21 — and the table
row of each "latest" configuration, all from the engine and checked against
two literal implementations (R3-3). The G-5 figures (12 and 30) and the
sentence "it was run for this file with only that one choice reversed" are
gone. Part 3's pointer no longer names one convention; part 4 adds the
"latest" immovable-event counts and the fourth-fix collapse run. Correction
C4-1.

### R3-2 · the key check — done in the engine **and** handed forward

`scripts/15_event_collapse.py` (criterion K-14): `chance_line()` and
`verify_event_map()` refuse anything whose type is not exactly `EventMap`;
the moments fingerprint, the event-map fingerprint and the record are
computed by module functions (`_tuple_fingerprint()`,
`event_map_fingerprint()`), never by a method of the map; a map whose
configuration label is not what its own fields make is refused. Measured
(`scripts/30_fourth_fix_checks.py`, run `516027c6c9f215d6`, H-1): REVIEW-3
q4's attempt 0 accepted, 1–5 refused (3 and 4 were accepted before); a true
map in a subclass refused; G-1's attempts as before; a tampered label or
`same_coin_keep` refused; a plain list refused; a patched `sha256()` does
not reach the record. Because nothing inside one process stops a caller who
edits the engine's functions, B-3 now also requires the event-map
fingerprint to be recomputed from the sealed key in a separate step and by
the review of the judge's run (`HANDED-FORWARD.md`, fourth-fix section B-3).
`main()` is unchanged in what it measures: runs `721b2448f1722ccf` and
`a0ecf6970d86b199` give the three CSVs of `bec532fa008e0e01` byte for byte.

### R3-3 · "keep the latest" — done in the engine; its use handed forward

`collapse(…, same_coin_keep="latest")`, allowed only with greedy-clique and
cross-coin (criterion K-15), implemented by `_greedy_literal()`: the wording
of JQ-N1 part 2 over every clock hour. H-2: identical to REVIEW-3 q1's
`literal()` and to REVIEW-2 p1b's `greedy_latest()` on the observation
moments at both definitions, and to q1's `literal()` on all 200 of q1's
random sets at both definitions; the same literal path run with "earliest"
equals the engine's existing path everywhere. Label `…+latest`. HANDED-
FORWARD B-1 names the check and the run to repeat if the engine changes.

### R3-4 · exact comparison of distances — done (new script); figures replaced

`scripts/29_identity_audit_exact.py` (criterion K-13): a copy of
`scripts/16_identity_audit.py` in which every comparison of two distances is
exact (integers after one common scaling, then dense ranks). Script 16 is
not changed (the GATE file names it). Acceptance check passed: every figure
of REVIEW-3 q2 (tied cards, tie-free score and line, verdict) reproduced on
the three sets q2 ran; T3 and T4 byte-identical to the third-fix audit on
all seven sets; features unchanged. Run on all seven card sets (runs in §4).

The same float equality also set the **pair-AUC** ranks (distances equal in
exact arithmetic were ranked apart by rounding noise), which REVIEW-3 did
not test. Exact ranks move several pair-AUC figures in the third or fourth
decimal (largest: `granularity-close` on the 2-decimal sets, 0.596809 →
0.599532). **No "beats" verdict changed on any family of any set** (H-3: no
`*_beats_chance` cell differs). Corrections C4-2 … C4-4. The juror files
now carry the exact figures (JQ-R04-CONTENT parts a and b). HANDED-FORWARD
A-2 names script 29, so `cards_with_tied_nn` is an exact count.

### R3-5 · JQ-R04-CONTENT part a — done

The table shows the trade-count column in both built renderings: from the
printed values it beats both lines on both features; from the values before
rounding it beats neither (one nearest-neighbour figure equals its line,
0.1256, and is marked "does not beat"). The question now reads "in the
rendering the exam card would otherwise carry", and a paragraph says how
part c bears on it. 0.2222 (0.1623) is replaced by 0.2134 (0.1619).

### R3-6 · the rank source — referred to jurors as JQ-R04-CONTENT-c

New part c in `exam-prep/fourth-fix/juror-questions/JQ-R04-CONTENT.md`, in
the group REVIEW-3 names (with JQ-R04-DATE). It describes both ways of
ranking, the guards the second passed, and how much finer order it adds
(criterion K-16, H-4: on every one of the 306 cards at least one hour the raw
card prints as equal to another is ranked apart from it; per column from 48
cards for `quote vol` to 306 for `top L/S pos`). Options yes / no / other,
one reason each. REVIEW-3's alternative — the coordinator records a reason
why it is engineering — remains open to the coordinator; I did not take it,
because the choice changes the numbers and no written rule settles it.

### R3-7 · the coupled groups — done; commissioning is the coordinator's

Every row REVIEW-3 ruled unfit is corrected, and the new row is checked
(§3). Both coupled groups can now be commissioned: JQ-N1-1…4 with
JQ-CANTEEN-8; JQ-R04-DATE-a…c with JQ-R04-CONTENT-a…c.

### R3-8 · what closes R-04 — done (handed forward, checkable)

HANDED-FORWARD, fourth-fix section, A-0 and A-0.1 … A-0.6: rulings
recorded; one configuration recorded; Level 1 on the exact audit with **both**
nearest-neighbour versions and pair AUC (no family may beat any of the three;
a disagreement between the two nearest-neighbour versions is sent to the
coordinator, not settled here); the gate as JQ-R04-GATE ratifies it; the
clock-hour line through the ratified JQ-R04-DATE outcomes; the frozen book's
three guards. Each with a yes/no check.

### R3-9 · owner and procedure for the configuration — done (handed forward)

A-1 and A-0.2: the run that declares R-04 closed records one configuration
string built only from ratified outcomes (or the `strict-flags` default);
the exam-building run uses it byte for byte. `rank_source` waits on
JQ-R04-CONTENT-c.

### R3-10 · a tied gate row — done (handed forward, not decided)

A-0.4 and A-2: if the ratified statistic reads the nearest neighbour and the
exam gate row has a tied nearest neighbour, both versions are computed; if
they disagree the gate is not graded and the coordinator is told. I did not
choose a version: the choice changes the numbers (RULES 33), and the GATE
file may not change while jurors answer it.

### R3-11 · one place to read — done

The section appended to `HANDED-FORWARD.md` restates everything in force,
including `R-04-blindness.md` §8 step 4 (A-0.6), and its table D lists every
earlier requirement it does not restate, with the reason. A later run reads
that section only.

### R3-12 · JQ-CANTEEN-8's two minor points — done (not required)

The file had to be re-issued anyway (it points to JQ-N1, which moved). The
"overlap by ten hours" paragraph now says the figure fits any 24-hour
window, not specifically before windows, and that every such reading gives
the same spacing; the per-coin spacing is attributed to the script that
drew the moments, with its lines. Options, counts and stakes unchanged.

### R3-13 · GATE and JQ-N1 both read RULES 13 — passed to the coordinator

In `VERDICT.md`: a referee ratifying both JQ-R04-GATE's optional part and
JQ-N1 should check that the two readings of RULES 13 do not contradict each
other. Not written into the index (the index carries no content).

### R3-14 · B-1 in the exam instructions — handed forward as information

HANDED-FORWARD, fourth-fix section, "for information" item (2). REVIEW-3
recommends it and does not require it; it is not mine to require.

### R3-15 · B-1 in the money test — recorded, nothing decided

HANDED-FORWARD, fourth-fix section, "for information" item (3).

### R3-16 · subjects in identifiers — not done; still the coordinator's

I kept the identifiers for the reasons the third-fix run gave (THIRD-FIX
R2-18); the new row follows the same pattern (`JQ-R04-CONTENT-c`).

### R3-17 · information that must not reach a GATE juror — passed to the coordinator

In `VERDICT.md`. I wrote nothing of that kind into any file of this run: no
juror file, and no section of this file, says which reading of the gate
would pass which material.

### R3-18 · verdicts at their line — done where a juror sees one

JQ-R04-CONTENT part b now says that its repeat-structure nearest-neighbour
figure at 2 decimals (0.1408 against 0.1387) sits close to its line and can
change with the seed, citing REVIEW-3 q2. The other cell REVIEW-3 names
(`repeat-volume`, 0.1297 against 0.1298) is in no juror file.

---

## 3 · The juror rows, checked against the reviews' standard

The standard is REVIEW-2's, as REVIEW-3 applied it: (i) a juror reading only
the files its row names can answer it; (ii) every outcome it offers can
follow from the instrument or rule it is about; (iii) its wording does not
lean; (iv) it is inside RULES 33; (v) no number is shown to a juror as
measured that the instrument does not support, or that is not what the file
says it is. Every number and every quoted line of the files I issued was
checked by `scripts/31_juror_file_check_fourth.py` (run `4b4d4795eb488c94`:
59 checks, 0 failed; the cited lines printed beside each citation), and the
passages I did not change are checked byte-identical to the third-fix files.

| row | REVIEW-3 | now | (i) | (ii) | (iii) | (iv) | (v) | result |
|---|---|---|---|---|---|---|---|---|
| JQ-N1-1 | fit | unchanged (text identical; the file is re-issued) | — | — | — | — | — | keeps its ruling |
| JQ-N1-2 | not fit | corrected | yes: both conventions defined in the file | yes: the engine offers both, checked against two literal implementations (H-2) | yes: neither convention is given a reason; listed in parallel | yes: a definition | yes: engine figures = q1 = p1b; G-5's figures gone | **fit** |
| JQ-N1-3 | fit | corrected (one phrase: no longer names one convention) | yes | yes | yes | yes | yes | **fit** |
| JQ-N1-4 | fit | corrected (engine version; the "latest" immovable counts) | yes | yes | yes | yes | yes: H-2 table row; collapse run reproduces 756cf4ea… byte for byte | **fit** |
| JQ-CANTEEN-8 | fit (two minor points) | corrected (the two minor points; JQ-N1's place) | yes | yes | yes: the over-reading of "overlap by ten hours" removed | yes | yes: counts byte-identical; 14 / 10 / 34 h recomputed from the cards | **fit** |
| JQ-R04-GATE | fit | **unchanged — not touched** | — | — | — | — | every figure equals the exact audit's gate row, with 0 tied cards on all five sets (check G of run `4b4d4795eb488c94`) | keeps its ruling |
| JQ-R04-DATE-a | fit | unchanged (text identical; re-issued with JQ-R04-CONTENT's new place) | — | — | — | — | — | keeps its ruling |
| JQ-R04-DATE-b | fit | unchanged (as a) | — | — | — | — | — | keeps its ruling |
| JQ-R04-DATE-c | fit | unchanged (as a) | — | — | — | — | — | keeps its ruling |
| JQ-R04-CONTENT-a | not fit | corrected | yes: both renderings, with figures | yes | yes: the premise is shown where it holds and where it does not; one reason per option, unchanged | yes | yes: exact audit | **fit** |
| JQ-R04-CONTENT-b | not fit (minor) | corrected | yes | yes | yes: one near-line verdict now said to be near its line | yes | yes: exact audit, all six figures per row (the pair-AUC figures also moved, C4-3) | **fit** |
| JQ-R04-CONTENT-c | — | **added** | yes: both renderings, the guards and the counts are in the file; the canteen lines are quoted | yes: both renderings are built and pass their guards | yes as far as I can judge: one reason per option; the cost (the finer order) and the effect on the trade-count signature are both stated | yes: what a blinding may do with a TACTICS 3 field; no number is chosen | yes: H-4, checked by 31 | **fit** (my judgement; untested by a review) |
| JQ-B1 | withdrawal justified | unchanged (withdrawn) | — | — | — | — | — | not a juror row |

Two limits, named: "does not lean" is a judgement, and part c is new, so no
reviewer has applied the standard to it yet.

---

## 4 · What the instruments show now

All on the 306 observation cards; nothing on exam cards.

**The exact audit** (`scripts/29_identity_audit_exact.py`, SHA-256
`cfc4bdcb…d03f`), runs in `exam-prep/fourth-fix/identity/`: raw
`9777f422fd2d2b41`, `ratio` `989b8f21b23e0310`, `rank` `446adf64f8e8235c`,
`strict` `45d062efe77c9251`, `strict-flags` `9ff0ffec3fe21ebe`, 3-decimal
set `762815a877c19551`, unrounded-rank set `d6557e91f9f97f7b`. Against the
third-fix audit, cells differ on every set (9 to 39 per set; listed in H-3),
in the nearest-neighbour tie counts and tie-free scores of families with
whole-number features and in pair AUC; **no verdict differs**. The gate row
has no tied nearest neighbour on any set, and its figures are those of the
third-fix audit, so R-04's state is unchanged: the gate row beats both lines
on every blinded set. R-04 is **not solved**.

**The engine** (`scripts/15_event_collapse.py`, SHA-256 `002bb406…e4f6`):
key check H-1 all as required; "latest" H-2 accepted; outputs of `main()`
unchanged.

**The rank source** (H-4): see R3-6.

---

## 5 · Corrections — what was claimed, what it is now, why

Earlier files are kept byte for byte; addenda appended to `THIRD-FIX.md`,
`R-04-blindness.md` and `N-1-collapse.md` point here.

| # | where | claimed | now | why |
|---|---|---|---|---|
| C4-1 | `third-fix/juror-questions/JQ-N1.md` part 2; `THIRD-FIX.md` R2-1 table | "keep the latest": 12 and 30 events in one partition only, 168 and 125 events, "counted the same way" as p1b's 4 and 21 | G-5 is a different rule; the wording gives 4 and 21, and 168 and 124 events | REVIEW-3 §4.3, q1; H-2 |
| C4-2 | `third-fix/juror-questions/JQ-R04-CONTENT.md` parts a, b; `THIRD-FIX.md` §4.4 table | nearest-neighbour tie-free figures of families with whole-number features, e.g. `repeat-trades` 0.2222 (0.1623), `granularity-close` 0.1946 (0.1334), 3-decimal 0.2545 (0.1547) | exact: 0.2134 (0.1619), 0.1948 (0.1337), 0.2525 (0.1567); every cell in H-3; no verdict changes | REVIEW-3 §4.1, q2; K-13 |
| C4-3 | `third-fix/criteria-written-before-measuring.md` K-5 and `THIRD-FIX.md` R2-11 (acceptance "pair AUC 0.596809 and 0.630049, REVIEW-2 p3 D's exact figures"); `third-fix/juror-questions/JQ-R04-CONTENT.md` part b pair-AUC figures | `granularity-close` pair AUC 0.5968 and 0.6300; repeat structure of `close` 0.5421 and 0.5636; part a's repeat structure of the trade count 0.5852 (0.5127) | the features were exact but the distances were ranked in floating point; with exact ranks 0.5995 (0.5130), 0.6303 (0.5123), 0.5416 (0.5108), 0.5639 (0.5128), 0.5853 (0.5128); all still beat | found by this run (H-3), beyond REVIEW-3 §4.1 |
| C4-4 | `third-fix/THIRD-FIX.md` R2-12 "the exact mean over every tie-break"; `scripts/16_identity_audit.py` header item 7 | the tie-free score is the exact mean over every tie-break | it is, over the ties the float comparison finds; exact ties are found by script 29 | REVIEW-3 §4.1 |
| C4-5 | `HANDED-FORWARD.md` third-fix B-2 | "The engine … refuses a map made from other moments" | true only against accidental mismatch until the fourth-fix engine; now also against a patched method or a subclass (H-1); a caller editing the engine's functions is caught only by B-3's recomputation | REVIEW-3 §4.2, q4 |
| C4-6 | `third-fix/juror-questions/JQ-CANTEEN-8.md` | "The canteen book also uses overlap in this sense [before windows]"; TACTICS 2 "sets its spacing per coin (line 38)" | the book's ten hours fit any 24-hour window; line 38 takes the moments per coin, and the per-coin spacing is the drawing script's reading of lines 39 and 43 | REVIEW-3 §5 |

---

## 6 · Where I disagree with the third review (RULES 32)

No disagreement. One extension: REVIEW-3 §3 (R2-5, R2-11) records that the
`granularity-close` pair-AUC figures 0.596809 / 0.630049 "reproduce". They
reproduce the computation, which ranked distances in floating point; the
exact ranking gives 0.599532 / 0.630346 (C4-3). The review's own §4.1 is the
reason, applied to the second attack.

---

## 7 · What I could not do, by name

1. **Nothing was measured on exam cards**; `exam/` is closed to this run.
2. **R-04 is not solved.** No engineering was found in this run that closes
   the gate row; none was tried beyond what is reported.
3. **No juror question was answered or ratified** — not mine (RULES 33–35).
4. **The judge's script does not exist**, so B-2 and B-3 cannot be checked
   against it.
5. **`scripts/18_residual_diagnostic.py` and `scripts/27_gate_sensitivity.py`
   were not moved to exact comparison**; they still import script 16.
   Their gate rows have no ties in either arithmetic; other uses are not
   checked.
6. **The block-mode null's random variation** — still not computed.
7. **What a tool-less candidate can use** — release names, hour offsets,
   and now the finer order of the unrounded rank — not measured.
8. **Whether the GATE jurors' commission included anything beyond the GATE
   file** (for example `VERDICT.md`) — not visible to me (`LEDGER.md` and
   `instructions/` are closed).
9. **The CANTEEN-8 citation of `scripts/06_find_moments.py` lines 136 and
   178–199** is not printed by script 31 (its pattern does not match a
   citation with a function name between file and lines); I read those
   lines myself.

## 8 · Decisions I took that the instruction did not cover

1. **Numbering REVIEW-3's items** R3-1 … R3-18 (§1).
2. **A new audit script instead of changing script 16**, because the GATE
   file, which jurors are answering, names script 16 as its source.
3. **Exact pair-AUC ranks** as well as exact ties: the review asked for the
   ties; the same comparison decides the ranks, and leaving it in floating
   point would have left a known float artefact in a juror figure.
4. **Implementing "latest" now**, before any ruling, rather than only
   handing it forward: it makes the juror figures the engine's own and
   removes a practical asymmetry between the two conventions.
5. **"Latest"'s card-number tie-break** (the higher card number) — the
   mirror of "earliest", and what both reference implementations do; it is
   never used on the observation moments (H-5: 0).
6. **Hardening the engine and also requiring B-3's recomputation**; REVIEW-3
   asked for either.
7. **Level 1 read with both nearest-neighbour versions**, and a tied gate
   row graded with both, a disagreement going to the coordinator — rather
   than choosing a version (HANDED-FORWARD A-0.3, A-0.4).
8. **The clock-hour line made checkable through the ratified JQ-R04-DATE
   outcomes**, with T3/T4 recorded and not graded, because no written
   standard gives a number (A-0.5).
9. **The owner of the configuration string** is the run that declares R-04
   closed (A-0.2, A-1).
10. **Correcting JQ-CANTEEN-8's two minor points**, which the review did not
    require, because the file had to be re-issued for JQ-N1's new place.
11. **Adding one sentence to JQ-R04-CONTENT part b** about the near-line
    verdict (R3-18), without the diagnostic's number.
12. **Re-issuing JQ-R04-DATE** only to change the place of JQ-R04-CONTENT;
    its three parts are word for word unchanged.
13. **A second collapse run** after a last change to the engine's hour index
    (`721b2448f1722ccf` kept as history; `a0ecf6970d86b199` is the final
    engine's), recorded in the run log as added by hand.
14. **The JQ-N1 file was built by recorded replacements**
    (`exam-prep/fourth-fix/make_jq_n1.py`, then three placeholders filled),
    so the change from the third-fix file is reviewable.

---

## 9 · How to reproduce

- `bash exam-prep/fourth-fix/run-instruments.sh` — the collapse engine and
  the exact audit on all seven sets (append-only; a recorded run writes
  nothing); then `python3 scripts/15_event_collapse.py --out
  exam-prep/fourth-fix/collapse` with the final engine (see the note at the
  end of `run-instruments.log`).
- `python3 scripts/30_fourth_fix_checks.py` — H-1 … H-5.
- `python3 scripts/31_juror_file_check_fourth.py` — the juror files.
- Constants: `SHUFFLES = 1000`, `TOP_FRACTION = 0.01`, `SEED = 20260913`,
  imported from the instruments; q1's 200 random sets and seed are q1's. No
  threshold was introduced.

## 10 · Fingerprints

`exam-prep/fourth-fix/FINGERPRINTS.md`.
