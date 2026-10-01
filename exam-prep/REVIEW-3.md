# Review 3 — the third pre-exam fix (`exam-prep/third-fix/`)

Mateo · data engineer, reviewing posture · started 2026-10-01T20:46:01Z, this
file written after 2026-10-01T21:13:39Z (system clock, RULES 23) · free disk at
start 12,415,352,832 bytes, at 21:13:39Z 12,405,506,048 bytes · nothing was
downloaded.

I did not do the work under review and was not told how it was done. Every
number below is either re-run with the third run's own scripts into
`exam-prep/review-3/rerun/`, or recomputed by a probe of my own in
`exam-prep/review-3/probes/` (code and output side by side). Where I state a
number I name the run or the probe that produced it.

**Opened:** `exam-prep/` (all; card files by script), `scripts/` (the non-`exam_`
files: read and run), `cards/` (by script), `data/overlap/` (manifest and
`pairs.csv`), `data/draw/` (`observation-coins.txt`, `draw-manifest.md` by
`grep`), `data/moments/moment-manifest.md` (head), `data/observation/` (by
script, through `17_blind_cards.py`), `canteen/2026-09-19-sofia.md` (lines
170–240, 660–675, 905–940), `RULES.md`, `TACTICS.md`. `git status` was run
twice (working-tree state only).
**Not opened:** `exam/`, `decisions/`, `instructions/`, `LEDGER.md`,
`reports/`, `external/`, `notes/`, `canteen/2026-09-19-viktor.md`, `TEAM.md`,
the root `README.md` (allowed, not needed), any `scripts/exam_*` (not read, not
run), git history (no `git log`, `git show`, `git diff`), anything outside the
Balıkçıl folder. No memory or session-log search. No bytecode cache was written
(`PYTHONDONTWRITEBYTECODE=1`; `scripts/__pycache__/` checked afterwards, no new
file).

---

## 1 · Rulings

| problem | ruling |
|---|---|
| **R-04 · is the exam blind?** | **Not solved.** I agree with the third run. The gate row (`ALL-removable`) beats its chance line on both attacks on all six blinded versions, including the new unrounded-rank version; every gate figure reproduces byte for byte (§2), and the gate row has no exactly tied nearest neighbour under exact arithmetic (q2), so the nearest-neighbour figure there does not depend on card order or on floating point. |
| **N-1 · collapse before counting** | **Solved only under three conditions.** The engine reproduces, its key check works against accidental mismatch, and under the convention the engine implements ("keep the earliest") it does exactly what JQ-N1's wording says (q1). Conditions: **(1)** JQ-N1 part 2 is corrected again where §5 says (its "keep the latest" figures are not of the wording) and the JQ-N1 group is then ratified (RULES 33–35); **(2)** the judge's script meets HANDED-FORWARD B-2 and B-3, **and** either the engine's key check is hardened or B-3 also requires the event map's fingerprint to be recomputed from the sealed key — today a forged map passes the check if the caller replaces one method on the map object (§4.2); **(3)** if "keep the latest" is ratified, it is implemented over every clock hour as the wording says, not by reversing the choice inside the engine's anchored windows, and checked against an independent literal implementation (q1 is one). |

---

## 2 · What I re-ran (the third run's own scripts, outputs in `exam-prep/review-3/rerun/`)

Command file `exam-prep/review-3/rerun.sh`, log `exam-prep/review-3/rerun.log`
(20:47:36Z → 21:00:08Z; script 28 again at 21:11:13Z, see §9 item 2). Scripts
26, 27 and 28 have no `--out`; they were imported and their `OUT_DIR` pointed at
`rerun/checks/`, so nothing was written into `exam-prep/third-fix/`.

| run | script | result |
|---|---|---|
| `bec532fa008e0e01` | `15_event_collapse.py` | same run number; `events.csv`, `collapse-summary.csv`, `shuffle-calibration.csv` byte-identical |
| `f8b6f4075510ae05` | `17_blind_cards.py --rank-source unrounded` (K-10) | same run number; every guard passed again; 306 cards and truth file byte-identical; combined fingerprint `a3adc013…a794` reproduced; run record identical apart from its clock line |
| (new numbers: the script changed) | `17_blind_cards.py`, default rank source, the configurations of `ratio`, `rank`, `strict`, `strict-flags` and the K-1 set | all 1,224 first-run cards and all 306 K-1 cards, and their truth files, byte-identical: the claim "default rendering unchanged" holds |
| `4858581e2eb08704` `12b07f79e74f0be7` `96f1d17e27b8afaf` `1f2ae3cf3a5b2044` `e05144718b909704` `ded6a9caaf77d910` `34095384f8b94ab7` | `16_identity_audit.py` (raw + six blinded sets) | same run numbers; every audit CSV and hour-linkage CSV byte-identical; reports differ only in clock, disk and output-path lines |
| `03bf5fc1560d1e33` `7b187671811b1396` `7dd6bf1f73244a4f` | `18_residual_diagnostic.py` | same run numbers; reports identical except clock/disk |
| `212dd7ecffc51263` | `26_third_fix_checks.py` | same run number; report identical except clock/disk; record identical |
| `7f6cd821a957440e` | `27_gate_sensitivity.py` | same run number; report identical except clock/disk; record identical |
| `bbb740248b0c8717` | `28_juror_file_check.py` | same run number, 61 checks, 0 failed (it read my own re-run of 26 for G-2) |

Also verified (q0): all 134 rows of `exam-prep/third-fix/FINGERPRINTS.md` match
the files; the six appended files start with exactly the bytes the third run
names, whose hashes equal `exam-prep/review-2/FINGERPRINTS.md`; the old index
copy is byte-identical to the index REVIEW-2 found; of the 91 rows of
`exam-prep/review-2/FINGERPRINTS.md`, the 10 that no longer match are exactly
the 10 files the third run declares changed; every file under `exam-prep/` and
`scripts/` modified after 20:06Z is listed in the third run's fingerprints
(except that file itself, as it says). K-11: on all seven card sets the first
and second audit batches have identical audit CSVs and differ only in the T3
`quote vol` row.

---

## 3 · The third run's outcomes against REVIEW-2's items — do they hold?

Numbering is the third run's (THIRD-FIX §1).

| item | third run says | holds? | how established |
|---|---|---|---|
| R2-1 · JQ-N1 part 2 | done | **does not hold in full.** The earliest-moment convention is now stated, and the engine does exactly what the wording describes under it: engine and a literal word-for-word implementation agree on the observation moments (all four greedy configurations) and on 800 random moment sets (q1 A, C). But the "keep the latest" figures given to the jurors (12 and 30 events in one partition only; "the number of events is unchanged: 168 and 125") come from G-5, which reverses the choice inside the engine's windows anchored at a moment's start. With "latest", that shortcut no longer finds the earliest hour of largest coverage the wording names: G-5 and the literal reading disagree on the observation moments (8 events at move-window, 13 at card-span) and on 156 and 172 of 200 random sets (q1 B, D). Read as worded, "latest" changes 4 and 21 events and gives **124** events at card-span, which is what REVIEW-2's p1b found; my literal implementation reproduces p1b exactly. | q1 |
| R2-2 · key check | done; handed forward | **holds, with a limit not stated.** G-1 reproduces. Other attempts: changing one card's coin and adding an extra moment are refused (q4). Replacing `moments_sha256` on the map instance, or overriding it in a subclass, makes a forged 59-event map accepted with the true key, and the record then shows `key_check: matched` with a `moments_sha256` equal to the key (q4 attempts 3–4). That is deliberate tampering, visible in the judge's code, but HANDED-FORWARD B-2's "refuses a map made from other moments" is stronger than the engine. | rerun 26, q4 |
| R2-3 · JQ-R04-GATE | done | **holds.** 23 → 43 → 44 features (first-run, second-fix, third-fix strict-flags CSVs); "no card has an exactly tied nearest neighbour" on the gate row is true under exact arithmetic (q2, three sets); the first-run row is dropped and the referral reason no longer names which reading passed. | CSVs, q2 |
| R2-4 · JQ-R04-CONTENT a | done | **holds for what REVIEW-2 asked** (argument paragraph gone; B-2 lift condition quoted, lines verified by script 28). **New defects:** see §5 (the unrounded-rank rendering is left out of the premise; one figure is not the average it is said to be). | rerun 28, q2 |
| R2-5 · JQ-R04-CONTENT b | done; review disputed (D-1) | **holds in substance.** K-4 is on the printed decimals; AUC 0.596809 / 0.630049 reproduce. Three nearest-neighbour figures differ slightly from the exact tie average they are said to be (§4.1); no verdict changes. | q2 |
| R2-6 · JQ-B1 | withdrawn | **holds** — see §6. | G-4 rerun, `scripts/04_draw.py` read |
| R2-7 · JQ-CANTEEN-8 | done | **holds.** All twelve counts reproduce from `pairs.csv` and, independently, from the card start hours (q3); C010/C011 start 14 h apart. | q3 |
| R2-8 · JQ-N1 part 4 | done | **holds.** Every figure in the part 4 table equals E-4 / G-2; G-2 reproduces; the widths 0.0160–0.0345 are right for the rows with n = 116–168. | rerun 26, tables read side by side |
| R2-9 · JQ-R04-DATE b | done | **holds.** 13 names / 18 cards by release day and 11 / 13 by start day (re-run T4); the 13 names in the juror file equal the audit record's list and REVIEW-2 p2's. | rerun 16 |
| R2-10 · groups commissionable | done | **does not hold.** Three rows are not fit (§5); neither coupled group can be commissioned. | §5 |
| R2-11 · K-4 float | done; handed forward | **holds** (`granularity-close` on printed text, exact Decimal; A-3 forbids E-3). | rerun 16 |
| R2-12 · NN on tied features | done; handed forward | **holds in part.** The tie-free score does not depend on card order. It is **not** the exact mean over every tie-break wherever two distances that are equal in exact arithmetic come out unequal in floating point: the audit finds ties by float equality after z-scoring. With exact arithmetic, tie sets differ on 5 families of `strict-flags` (`repeat-trades` 231 vs 236 tied cards; tie-free 0.2222 vs 0.2134), and on `granularity-close` on every set (q2). No verdict changes on any set I recomputed. REVIEW-2's p3b has the same float behaviour (its `repeat-trades` mean is 0.222160), so K-6's acceptance check could not catch it. | q2 |
| R2-13 · T4 | done | holds | rerun 16 |
| R2-14 · block vs representative | done | holds (G-2 = REVIEW-2 p5) | rerun 26 |
| R2-15 · C-4 | done | holds | read |
| R2-16 · K-1 table; D-1 | done; disputed | **holds; D-1 is supported.** A permutation line belongs to its own statistic. On exact tie sets, with the audit's own shuffles: `repeat-close` at 2 decimals 0.1408 against 0.1387 and at 3 decimals 0.1510 against 0.1401; `granularity-close` at 2 decimals 0.1948 against 0.1337. All three beat (q2). REVIEW-2's "does not beat" compared these averages with the line of the index-tie-break statistic. Two verdicts sit at the line: `repeat-close` (2 decimals) is beyond it in 0.65% of 2,000 further shuffles, and `repeat-volume` (0.1297 against 0.1298, "does not beat") in 0.90%. Both are decided by the fixed seed, not by a margin. | q2 |
| R2-17 · public-seed numbering | information | holds | read |
| R2-18 · subjects in identifiers | not done; referred | an acceptable referral; still open (§8) | read |
| R2-19 · R-04 | not closed | holds | rerun 16, 27 |

---

## 4 · Findings of my own probes

### 4.1 · Ties are found by floating-point equality (q2)

`nearest_tie_sets()` in `scripts/16_identity_audit.py` keeps every card with
`row[j] == best` on float distances computed from z-scored floats. Two pairs
whose squared distances are equal in exact arithmetic (for example the same
integer differences at different base values) can differ in the last bit and
not be counted as tied. With squared distances computed as exact fractions over
the exact sample variance:

| set | family | tied cards, audit / exact | tie-free, audit (line) | tie-free, exact (line) |
|---|---|---|---|---|
| `strict-flags` | `repeat-trades` | 231 / 236 | 0.2222 (0.1623) | 0.2134 (0.1619) |
| `strict-flags` | `granularity-close` | 304 / 304 (sets differ) | 0.1946 (0.1334) | 0.1948 (0.1337) |
| 3-decimal set | `granularity-close` | 256 / 257 | 0.2545 (0.1547) | 0.2525 (0.1567) |
| `strict-flags` | `repeat-takerbuy`, `repeat-openint`, `repeat-ratio` | sets differ | 0.1212 (0.1328), 0.2028 (0.1419), 0.1863 (0.1765) | 0.1212 (0.1327), 0.2028 (0.1427), 0.1863 (0.1765) |

The gate row has no ties either way on `strict-flags`, the 3-decimal set and
the unrounded-rank set. On every family I recomputed, every verdict is the
same. The fix is to compare distances exactly (squared distances as exact
fractions, as q2 does) or to state a tolerance and where it comes from. The
count `cards_with_tied_nn` that HANDED-FORWARD A-2 requires in the exam manifest
is an under-count until then.

### 4.2 · The key check reads a method of the object it checks (q4)

`chance_line()` compares the key with `events.moments_sha256()`, a method of
the map passed in. `verify_event_map()` accepts subclasses. Replacing that
method on the instance, or overriding it in a subclass, lets a map built from
forged moments through with the true key. Overwriting `.moments` with the true
moments is refused, because the re-derivation no longer matches. Two small
changes would close this: compute the fingerprint inside `chance_line()` with
`moments_fingerprint()` from `events.moments`, and refuse any type other than
`EventMap` itself. Otherwise B-3 should require the checker to recompute
`event_map_sha256` from the sealed key with `collapse()` and compare it with the
record.

### 4.3 · "Keep the latest" is two different algorithms (q1)

Under "earliest", the engine's shortcut (it tries only windows whose left edge
is a moment's start, and breaks ties by that start and then by the id of the
first kept member) is equivalent to the wording (every clock hour, ties to the
earliest hour, then the lowest card number). I found no counter-example in
800 random sets. Under "latest" it is not. Keeping the latest moment of a coin
can drop the moment that anchored the window. The event then corresponds to a
later hour than the earliest hour of largest coverage. Example (card-span,
q1 B2): G-5 joins KOMA's moment at start index 7308 with AVGO 7287 and FART
7265, while the wording joins KOMA's 7293 (the only KOMA moment covering the
earliest hour of largest coverage). JQ-N1 part 2 gives the jurors both sets of
figures as two implementations "counted the same way" of one convention. They
are two conventions. HANDED-FORWARD B-1 says a "latest" option "must be added,
checked and recorded", but names nothing to check it against.

### 4.4 · The unrounded-rank rendering removes the trade-count column's measured signature (re-run, q2)

On the K-10 set, neither trade-count family beats either line: `trades-level`
pair AUC 0.4997 (line 0.5033) and tie-free NN 0.1256 (line 0.1256, equal, so
not above it); `repeat-trades` 0.5012 (0.5081) and 0.1210 (0.1248). JQ-R04-CONTENT
part a asks its question on the condition that the column "carries a measured
coin signature". It shows only the `strict-flags` rendering, where it does. The
juror files were finished at 20:37–20:38Z. The K-10 audit that shows this had
been recorded at 20:25:45Z (run `af59d44f00b6c081`; its CSV is identical to
`34095384f8b94ab7`'s).

### 4.5 · B-1 fires in neither test

`scripts/04_draw.py` builds the money-test set as every coin not drawn for
observation or exam (lines 120–127), so it excludes the observation coins too.
AVGOUSDT and NOKUSDT are observation coins. Under its frozen trigger, B-1
therefore blocks nothing in the money test either. JQ-B1's statement says only
that in the money test B-1 "is a plain symbol exclusion". This is not a review
item. I name it and decide nothing; it bears on the frozen book, not on R-04 or
N-1.

---

## 5 · The juror rows, row by row (REVIEW-2's standard)

The standard is REVIEW-2's, unchanged. A row is **fit** when:

- (i) a juror reading only the files its row names can answer it;
- (ii) every outcome it offers can follow from the instrument or rule it is
  about;
- (iii) its wording does not lean;
- (iv) it is inside RULES 33;
- (v) no number is shown to a juror as measured that the instrument does not
  support, or that is not what the file says it is.

| row | ruling | why |
|---|---|---|
| JQ-N1-1 | **fit** | unchanged; table reproduces (`events.csv` byte-identical) |
| JQ-N1-2 | **not fit** | (ii) and (v): the "keep the latest" outcome is given figures (12 / 30 events; "the number of events is unchanged: 168 and 125") from an algorithm that does not implement the wording (§4.3); as worded, "latest" gives 4 / 21 and 124 events at card-span. "It was run for this file with only that one choice reversed" invites a later run to implement it the same wrong way. |
| JQ-N1-3 | **fit** | counts reproduce; its greedy-clique bullet only points to part 2 and states nothing about "latest" |
| JQ-N1-4 | **fit** | every figure equals E-4 / G-2; G-2 reproduces; the noise statements are right |
| JQ-CANTEEN-8 | **fit** | counts reproduce two ways (q3); options balanced; no number chosen by a juror. Minor, no effect on any outcome: the canteen's "overlap by ten hours" is equally true of the two before windows, the two after windows and the two 24-hour movements (any two 24-hour windows 14 h apart share 10 h), so "the canteen book also uses overlap in this sense [before windows]" over-reads it; the spacing that option implies (24 h) is the same whichever is meant. Also minor: line 38 ("for each coin") supports a per-coin count, and the per-coin spacing is the draw script's reading of lines 39 and 43; the file presents that reading as TACTICS' own but leaves "other" open |
| JQ-R04-GATE | **fit** | every figure reproduces; no ties on the gate row under exact arithmetic; options unchanged and balanced; the earlier result is withheld. One gap belongs to HANDED-FORWARD, not to the question (§7, A-2) |
| JQ-R04-DATE-a | **fit** | unchanged; 243 / 495 and 0 / 46,170 reproduce |
| JQ-R04-DATE-b | **fit** | 100 / 30 / 13 / 18 and the 13 names reproduce |
| JQ-R04-DATE-c | **fit** | unchanged; 99 reproduces |
| JQ-R04-CONTENT-a | **not fit** | (iii) and (i): the question is conditioned on the column carrying a measured signature. It shows only a rendering where it does, and leaves out the built and audited rendering where it does not (§4.4). (v): its "how many values repeat" nearest-neighbour figure 0.2222 (0.1623) is not the tie average it is said to be; that average is 0.2134 (0.1619), still beats (§4.1) |
| JQ-R04-CONTENT-b | **not fit** (minor) | (v) only: two of its nearest-neighbour figures are not the tie average the file says they are: 2 decimals 0.1946 (0.1334), exactly 0.1948 (0.1337); 3 decimals 0.2545 (0.1547), exactly 0.2525 (0.1567). No verdict changes; the fix is to replace the figures |

### What must change

- **JQ-N1-2.** Replace the G-5 figures with the figures of the wording (q1 B or
  REVIEW-2 p1b: 4 and 21 events in one partition only; 168 and 124 events). Or
  give both and say plainly that the engine's loop with the choice reversed is
  a different rule, which the jurors are not being asked about. Remove "it was
  run for this file with only that one choice reversed".
- **JQ-R04-CONTENT-a.** State the premise for both built renderings of the
  ranked columns (`strict-flags`: the column carries a measured signature;
  unrounded-rank: neither trade-count family beats either line), or give no
  figures and state the premise without them. Replace 0.2222 (0.1623) with the
  exact tie average once the audit is fixed (§4.1).
- **JQ-R04-CONTENT-b.** Replace the two granularity nearest-neighbour figures
  with the exact tie averages once the audit is fixed.
- **The point no row answers.** The unrounded-rank rendering computes a
  printed column from finer values than the raw card prints. The exam card
  would then carry an order the watchers never saw (the third run's own
  THIRD-FIX §4.4 names this cost). No written rule settles whether that is
  permitted, and it changes the numbers. HANDED-FORWARD A-1 leaves
  `rank_source` to "the laboratory". By RULES 33 this is an open question. It
  belongs with JQ-R04-CONTENT ("may the blinding … recompute a field"), unless
  the coordinator records a reason why it is engineering.

Because the N-1 parts and the DATE/CONTENT parts are answered together,
**neither coupled group can be commissioned until its unfit parts are fixed.**
JQ-R04-GATE stands alone and is fit.

### The couplings

- **JQ-N1-1…4 with JQ-CANTEEN-8 — right.** CANTEEN-8's answer changes how many
  same-coin overlaps part 3 governs, and both use the same span arithmetic.
- **JQ-R04-DATE-a…c with JQ-R04-CONTENT-a, b — right.** Both groups read RULES 9
  against TACTICS 3 and 6. The rank-source question above belongs here if it is
  referred.
- **JQ-R04-GATE alone — right, and should stay alone.** Jurors who choose the
  gate statistic should not also choose the renderings it will grade.
  Coupling them would let one set of jurors pick definitions by their combined
  effect, which THIRD-FIX §4.5 itself warns against. One cross-reference, not a
  coupling: GATE's optional second part cites RULES 13. If both rows are
  answered, the referee may want to check that the two readings of RULES 13 do
  not contradict each other.

---

## 6 · The withdrawn row — JQ-B1

**The withdrawal is justified, and it leaves no point the written rules do not
settle.**

- The frozen trigger names two contracts (canteen line 187), both observation
  coins. The exam is drawn from the rest, and the draw manifest records
  `"disjoint": true` and an empty overlap (G-4 re-run; `scripts/04_draw.py`
  read). So B-1 cannot fire on an exam card.
- The question the canteen chair recorded is conditional. The frozen book
  already scopes B-1 to the money test ("it applies in the money test only",
  lines 205–212). The chair refers the question to jurors only "if the
  laboratory wants a different answer" (lines 935–939). So the written rules
  settle the exam case.
- Treating the trigger as a class would be a new rule (RULES 6), as the
  statement says.

**Recommended, not required.** The statement's reasoning that "the candidate …
would block … none" holds only if a candidate applies B-1 correctly; a
candidate cannot see the contract. The stronger ground is the frozen scope at
lines 205–212, which the statement cites only for the money test. Whatever run
writes the exam instructions for the recipe-holding candidate should leave B-1
out on that ground. Also see §4.5.

---

## 7 · What the third run handed forward — can the run that must meet it check, yes or no, that it has?

| requirement | checkable yes/no? | what is missing |
|---|---|---|
| A-0 | **no** | "until R-04 is closed": no test is named. It should say which standard closes R-04: `R-04-blindness.md` §2's Level 1 and Level 2, the clock-hour row, and the gate statistic JQ-R04-GATE ratifies. Level 1 itself now reads differently by index or by tie-free nearest neighbour (C3-11), so the version must be named too |
| A-1 | **no** | "the configuration the laboratory settles": no owner and no procedure; it includes the `rank_source` choice, which is an open point (§5) |
| A-2 | **yes, with two gaps** | (1) If the exam gate row has a tied nearest neighbour, "the statistic JQ-R04-GATE ratifies" does not say which nearest-neighbour version grades. (2) `cards_with_tied_nn` from the named audit version under-counts ties (§4.1) |
| A-3, A-4, A-5, A-7 | yes | — |
| A-6 | yes, if the exam's calm moments are drawn after the ruling | whether they already were is not visible to me (`exam/` closed) |
| B-1 | **yes for "earliest"; no for "latest"** | "added, checked and recorded" names no reference to check against; the only reversal in the repository (G-5) is not the wording (§4.3) |
| B-2, B-3 | yes, by reading the judge's code and record | B-3 does not catch the tampering in §4.2; add the recomputation of `event_map_sha256` from the key, or harden the engine |
| B-4, B-5 | yes | — |
| the file as a whole | **partly** | It "replaces … wherever they differ" three older §8s, so a later run must compare four files to know what is in force. `R-04-blindness.md` §8 step 4 (check that the B-3 zeros, the largest `|chg%|` and the B-4 runs survive) is not restated, but it is still in force |

---

## 8 · Does `exam-prep/JUROR-QUESTIONS.md` carry the content of a question?

It carries **no wording, no options and no numbers** of any question. Its only
numbers are the SHA-256 of the earlier index and the rule numbers "RULES 33–35".
Its part labels ("Part 4 (with 4a and 4b)", "parts a and b") show a file's
structure, not its options. As REVIEW-2 found, the identifiers still carry each
question's **subject** (GATE, DATE, CONTENT, CANTEEN-8). The JQ-CANTEEN-8
identifier names the canteen section whose text is that question's wording.
The rows no longer point at that passage. The third run referred this to the
coordinator (R2-18). It is still undecided, and it is not mine to decide.

---

## 9 · Decisions I took that the instruction did not cover

1. **Probes and the re-run live in `exam-prep/review-3/`**, as the instruction
   requires; scripts 26–28 were run by import with `OUT_DIR` redirected.
2. **Script 28 failed in the first batch** (`ModuleNotFoundError: lab_cards`).
   An imported spec does not put `scripts/` on the import path. A block was
   appended to `rerun.sh`, marked as added after the run, and 28 was re-run
   alone. The failure was mine, not the script's.
3. **The default renderings were re-built**, not only K-10, to test the claim
   that 1,224 reviewed cards are unchanged.
4. **The reference for "keep the latest"** is a literal reading of JQ-N1's
   wording (every clock hour a candidate). It is restricted to start hours,
   which cannot change the result, as q1's comment explains. A juror could
   read the wording another way; I report what the wording says, not which
   convention is right.
5. **Exact ties** are computed with squared distances as fractions over the
   exact sample variance. That is my definition of "exactly equally similar".
6. **Diagnostic counts of my own**: 200 random moment sets (seed 20260913) in
   q1; 2,000 further shuffles (seed 1) in q2. Nothing is graded on them.
7. **The fitness test (v)** also counts a figure that is not what the file
   says it is, even when no verdict changes. Under that reading,
   JQ-R04-CONTENT-b is not fit. Without it, CONTENT-b would be fit and
   CONTENT-a would still be not fit, on the omission.
8. **Two of my `pkill -f` commands matched their own shell** (exit 144). One
   stopped a superseded probe attempt and one stopped a wait loop. No output
   file was affected: every `.out` was written by a later, completed run.

---

## 10 · Steer check

My instruction contains no result, no prediction and no verdict. "For each row
whose status is 'withdrawn', if any" presumes nothing. The git status supplied at
start showed only commit subjects of the form "work: …" and "ledger: …", which
carry no result. I ran no `git log`.

Two things in the third run's files concern the coordinator rather than any
ruling:
(a) VERDICT.md's third-fix section, "What R-04's closure depends on" point 2,
says which group of gate readings fails on all material measured so far. That
is the result-before-rule information which the juror file withholds from the
jurors under RULES 6. It must not reach a GATE juror or the referee.
(b) The same section's steer paragraph reports something the third run saw in
commit subjects that it believes may concern the user. I did not look into it.

---

## 11 · What I could not do, by name

1. **Nothing measured on exam cards**; `exam/` is closed.
2. **Whether the third run read nothing under `exam/`** — not verifiable without
   reading `exam/`.
3. **Whether the exam's calm moments are already drawn** (A-6), and **whether
   the sealed key will carry `id, coin, start hour`** (B-2) — under `exam/`.
4. **Whether any juror file was already commissioned** — `LEDGER.md` is closed.
5. **REVIEW-2's git-based statements** were not re-verified (git history closed).
6. **The block-mode null's variation** — not computed (no exact form).
7. **Publication frequency of release names; what a tool-less candidate
   knows** — not measured.
8. **REVIEW-2's own probes were not re-run.** I only read p1b and p3b, and
   their outputs, to compare.
9. **The audit's float tie issue on families I did not recompute** (raw cards,
   `ratio`, `rank`, `strict`) — not measured.

---

## 12 · How to reproduce

- `bash exam-prep/review-3/rerun.sh` — every third-fix run into
  `exam-prep/review-3/rerun/` (append-only by run number).
- `python3 exam-prep/review-3/probes/<name>.py`, outputs in the `.out` files
  beside them: q0 (fingerprints), q1 (greedy-clique: engine, literal wording,
  G-5), q2 (exact tie sets and tie-free lines; run with `--cards`/`--truth`,
  three outputs), q3 (calm-overlap counts), q4 (key-check attempts).
- Constants used: `SHUFFLES = 1000`, `TOP_FRACTION = 0.01`, `SEED = 20260913`,
  imported from the instruments; no threshold was introduced.

## 13 · Fingerprints

SHA-256 of every file I wrote, and of the reviewed files as I found them, are in
`exam-prep/review-3/FINGERPRINTS.md`. This file's own SHA-256 is in my report to
the coordinator.

I wrote this file and `exam-prep/review-3/`, and nothing else. I edited no other
run's file and nothing under `exam/`, `scripts/`, `cards/`, `data/` or
`canteen/`.
