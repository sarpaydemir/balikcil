# Review 8 — the eighth pre-exam run and its juror file (`exam-prep/eighth-fix/`)

Mateo · data engineer, reviewing posture · first clock read
2026-10-02T00:20:30Z, this file written after 2026-10-02T00:37:58Z (system
clock, RULES 23) · free disk 11,474,120,704 bytes at 00:20:30Z,
11,470,434,304 bytes at 00:37:58Z · nothing was downloaded.

I did not do the work under review and was not told how it was done.
Criteria, fixed before opening anything in `exam-prep/eighth-fix/`, the
eighth-fix sections of `HANDED-FORWARD.md` and `VERDICT.md`, and
`USER-QUESTIONS.md`, and before any check or probe:
`exam-prep/review-8/criteria-written-before-ruling.md`. Probes and their
outputs side by side: `exam-prep/review-8/probes/`.

**This file discusses what the answers of a juror question do. It must not
reach a juror or a referee** (HANDED-FORWARD eighth-fix C-5, "nothing under
`exam-prep/` that the row does not name"; RULES 6).

**Opened:** `RULES.md`, `TACTICS.md`, `TEAM.md`; the four verdicts my
instruction names (`verdict.md` only); `exam-prep/` — `README.md`,
`JUROR-QUESTIONS.md`, `REVIEW-7.md`, REVIEW-6 lines 1–195, REVIEW-5 lines
125–165, REVIEW-3 lines 176–245, REVIEW-2 lines 226–303, the headings of
REVIEW, REVIEW-2 … -6, the criteria files of review-4 … review-7; the whole
eighth-fix folder except the two `pre-run-*` files and the check report
`.md` (the `.json` was read by script); `HANDED-FORWARD.md` lines 1–30,
140–260, 405–844; `VERDICT.md` lines 945–1071; `USER-QUESTIONS.md` by
`diff` and headings; the withdrawn sixth-fix d file by `diff`;
`third-fix/juror-questions/JQ-R04-GATE.md` lines 50–70;
`scripts/29_identity_audit_exact.py` lines 217–472 and 700–770 plus a
`grep`; `scripts/lab_cards.py` lines 216–260; `scripts/35_eighth_fix_check.py`
lines 1–80, 300–330, 373–381, 615–630; a blinded card and a raw card (table
headers and bullet lines); `data/universe/universe.csv` and
`data/draw/observation-coins.txt` (read by probe p7 only; the second shown
on screen masked). Two tool outputs were too large and were saved by the
harness to a file outside this folder; I did not open either and re-ran
the reads with a narrower scope.
**Not opened:** `exam/`; `open-questions/`; any `scripts/exam_*` (not read,
not run; their names appear in a listing of `scripts/` and of
`scripts/__pycache__/`); in `decisions/`, anything but the four `verdict.md`
files (the folder names were listed once at the start); `instructions/`,
`LEDGER.md`, `reports/`, `external/`, `notes/`; `canteen/` (allowed; not
needed — probe p7 read only the line ranges the index names); `CLAUDE.md`;
git history (no log, show or diff; one `git status --porcelain exam-prep`
at the end, working tree only — it showed most of my `review-8/` files
already tracked, so an automatic commit I did not make picked them up
while I worked); anything outside the Balıkçıl folder. No memory or session-log search.

---

## 1 · Item 1 — `JQ-R04-CONTENT-d`: **not fit**

| test (criteria file) | result |
|---|---|
| (i) answerable from its list | passes, with the blemishes of §2.4 |
| (ii) determinacy | **fails** — §2.1, §2.2 |
| (iii)/(vi) no lean, matching weight | **fails** (judgement, stated as such) — §2.3 |
| (iv) RULES 33 | **contested**, as REVIEW-5 §4, REVIEW-6 §3, REVIEW-7 §1 left it; the file now offers the scope answer and names the referee's scope check. Not a ground of my ruling |
| (v) true | 30 of 30 quotations found in the file and in their cited lines (p2); the four outside groups, the inside list and "one field per feature" true of the code (p1: 71, 62, 62, 60, 59 feature keys on the five card sets, each placed on exactly one field); two statements not true as written (§2.4 items 1–2); one premise stated as fact that is a reading (§2.1) |
| completeness | passes: five answers including "Other" and the scope answer |
| coupling | passes: it sits alone; the renderings it grades are ratified, so its jurors cannot choose them together with the graded set |
| deletion | REVIEW-6 §2.2's L2 ground is gone and nothing points at it (cured); the sixth-fix sentence that explained the audit's grouping word is gone while the word remains in the quoted definition and in the question (§2.4 item 4) |
| reading list | passes: the file, `RULES.md`, `TACTICS.md`; verdict paths are cited as sources with "you do not need to open"; C-5 forbids giving them |
| contradiction with the four verdicts | §3: none with three; with DATE/CONTENT, **contested** on one passage |
| earlier findings on part d | REVIEW-5 §4 (ii): cured (fixed list). REVIEW-6 §2.1: narrowed, not cured (§2.1, §2.2 below are what is left of it). REVIEW-6 §2.2: cured. REVIEW-7's U-1 faults read as tests: title, results path, stale point, rule section — cured; "an unconditional claim that is conditional" recurs once (§2.4 item 1); empty set — given an outcome, but its trigger is narrower than the audit's message (§5, A-0.4 1b) |

What must change, by section (the fault, not the fix):

- **"What each answer does to the graded set — mechanically"**, the bullet
  of the second answer, and the second answer's own text under **"The
  question"** — §2.1.
- **"What other jurors ratified"**, and the second answer's bullets — §2.2.
- **"What each answer does to the graded set — mechanically"**, the bullets
  of the second and third answers taken together — §2.3.

### 2.1 · A reading stated as a fact, that changes the numbers

The mechanics section says the CARRIES test "is written for a column; no
ratified outcome gives one for a line of the card", so under the second
answer the features of the previous-7-day line and of the Wikipedia line
leave the set. The ratified CONTENT-a outcome (DATE/CONTENT verdict line 42,
quoted in the file) speaks of "a TACTICS 3 field" that "carries a measured
coin signature as JQ-R04-CARRIES defines one". A field includes a line
(the file's own definition, lines 68–71). So a second reading is available:
the CARRIES test applied to a line's own printed values. Under it, a line
that carries a signature and that the frozen book does not read is
removable, and if printed is graded. Under the file's reading it is never
graded. The features at stake are those the file itself lists inside the
set from those two lines (two from the previous-7-day line, one from the
Wikipedia line; p1).

This is a wording that can be read two ways (RULES G, line 113). The file
settles it in its mechanics, while its own "What you decide" section tells
jurors that what "carries a measured coin signature" means is not theirs
(lines 24–25). The eighth run lists it as its own decision (EIGHTH-FIX §7
item 3: "lines of the card (no ratified test) leave the set rather than
stop the run"; "the jurors who ratify this answer ratify its text"). The
jurors do ratify the text, but the text presents the point as following
from the outcomes, not as part of what the answer asks them to accept. A
juror is led to a belief — that no ratified outcome reaches a line — that
one reading of a ratified outcome contradicts. **Fails (ii)/(v).**

### 2.2 · A passage of a ratified verdict left out, that changes the numbers

The DATE/CONTENT verdict's "Effect on exam cards" (line 56) says that for
the three DATE parts "the specified columns and fields stay on the exam
card". The file quotes the outcome sentences (lines 39–47) "up to each
answer" and not line 56. The second answer turns on whether "the ratified
outcomes give no permission to leave out" a field. For the two reference
columns the DATE-a part is about, line 56 read as "must stay" makes them
fields with no permission to leave out (so their features leave the set);
read as "may stay", CONTENT-a's conditions decide (so they are graded when
both hold). The file and HANDED-FORWARD A-0.4 step 1 take the second
reading without saying so. The eighth run names this gap in EIGHTH-FIX §3
and §6 item 4 and in its VERDICT section ("For the coordinator" item 3) —
beside the question, not in it. A juror who picks the second answer cannot
know that what it does to two columns depends on a passage they are not
shown. **Fails (ii)**; under §3 it is also the contested contradiction.

### 2.3 · Matching weight between the second and third answers (judgement)

For the third answer the file states the consequence that matters: the set
holds no feature, and an empty set is stop 1, "not graded". For the second
answer it states which columns are graded — those the A-0.7 measurement
says carry a signature and the A-0.9 record marks as unread — but not what
follows from that, which is as mechanical:

- if the blinding leaves out every column it is permitted to leave out
  (CONTENT-a), the set is empty: the same stop 1 as the third answer;
- if exactly one such column is printed, the graded set is that column's
  own feature set, measured on the same cards with the same attacks and
  seed as the A-0.7 measurement that found it carries a signature
  (`29_identity_audit_exact.py`: `standardise`, the per-row
  `random.Random(SEED)`), so the gate fails by construction;
- only with two or more such columns printed is the result not fixed in
  advance.

So under the second answer the gate never grades a column that has not
already been measured to carry a signature. The file shows the stop for
one answer and not for the other, which reaches it whenever the permission
is used. A juror comparing the two is shown a gate that does not run under
one and is left to infer that the other runs only on channels already
known to fail it. REVIEW-7 F4 asked that consequences be stated with
matching weight. **I rule this a fault; it is a judgement, and another
reviewer could weigh it as a blemish.** It does not change my ruling on
its own: §2.1 and §2.2 are enough.

### 2.4 · Blemishes, noted, not ruled

1. **The third answer's sentence** "every feature the audit computes is
   computed from a field the card prints" is not true on a rendering that
   prints no Wikipedia line: `card_features()` computes the Wikipedia
   presence feature on every card (0.0 when the line is absent). On all four
   blinded observation sets, 306 of 306 cards print no Wikipedia line and
   the feature is computed on all 306, value 0.0 (p1 (5), (6)). The composed
   set then holds one feature, constant, which `standardise()` drops, and
   the audit prints "no features left after blinding". The practical
   outcome is the message the file names, but the file's trigger ("if the
   set holds no feature") is not met as written. In HANDED-FORWARD it is a
   checkability gap (§5).
2. **"nine columns are printed as each hour's rank"** — true of the
   `strict` and `strict-flags` blinded sets (9), not of `rank` (8) or
   `ratio` (0) (p1 (4)). Unqualified in the file.
3. **Lines 69–70** read "a line of the card (the for example …" — a word
   is missing or extra.
4. **The grouping word** of the quoted definition and of the question is
   not explained; the file says "groups" for the four outside groups.
   Two of the audit's families span a column and the previous-7-day line
   (`volume-level`, `trades-level`, lines 406–407 of the audit); the
   question's per-field framing splits them. The question and A-0.4 both
   act per feature, so this changes nothing determinate; a juror could
   still read "families" as whole families.
5. **"with its size"** (lines 106 and 247) is not explained.
6. **Lines 32–33** ("answered no other question about how exam cards are
   blinded") — whether a juror of JQ-R04-GATE may sit is read differently
   by the index and by HANDED-FORWARD (§5, A-0.1).
7. **A gap the A-0.9 record exposes.** The question asks only about the
   "TACTICS requires" limb of the definition (the ellipsis at line 178 cuts
   "a frozen canteen rule or"). Under the first answer only the four
   outside groups leave, whatever the new A-0.9 record says the frozen book
   reads. If that record marks a column outside the four groups as read,
   the definition's other limb could take it out, and the first answer
   keeps it graded. The question neither puts nor names this. The
   first answer is determinate (a fixed list), so this is not a fault under
   (ii). It is a gap, and it changes the numbers only if the record marks
   such a column.

## 3 · Contradiction with the four ratified verdicts

- **JQ-R04-GATE** (line 72 quoted exactly, p2): none. Under the third
  answer the rule never has a set to apply to. The verdict is silent on an
  empty set: a gap, not a contradiction.
- **JQ-N1 / JQ-CANTEEN-8**: none. The file reads nothing of RULES 13. A gap,
  not created by this file and already noted by REVIEW-6 §4: whether the
  ratified "each event counts once in the shuffle" reaches the identity
  audit's chance lines is not said anywhere I may read.
- **JQ-R04-CARRIES** (lines 107, 109 quoted exactly): none. §2.1 concerns
  how far CONTENT-a carries the CARRIES definition, not the definition.
- **JQ-R04-DATE / CONTENT**: **contested.** On the "must stay" reading of
  line 56, the file's second answer and A-0.4 step 1 treat the two
  reference columns as fields the outcomes permit to be left out, which
  that reading does not allow: two readings that cannot both be applied
  to the same exam cards. On the "may stay" reading there is none. The
  eighth run calls this a gap (EIGHTH-FIX §3); it is a gap or a
  contradiction depending on a reading nobody has settled (§2.2).

## 4 · Item 2 — the eighth run's own choices

From EIGHTH-FIX §7 and what the files show. "Changes the numbers" as fixed
in my criteria.

| choice | changes the numbers? | where it sits |
|---|---|---|
| §7.1 numbering REVIEW-7's items | no | — |
| §7.2 answer texts reworded | yes (they compose the set) | in the question — passes |
| §7.3 the second answer counts a field as permitted out only where both conditions are on record; lines leave | **yes** | in the question's mechanics, **stated as a consequence, not as part of the answer** (§2.1) |
| §7.4 A-0.9 added (thirteen columns, no lines); A-0.7 extended to every printed column under the second answer | yes, through condition (b) | the record is named in the question (lines 167–170); its column-only scope follows §7.3 and sits beside |
| §7.5 empty set read as "not graded — stop" for every answer | yes (not graded vs failed) | in the question (stop 1) — passes; its trigger is narrower than the audit's message (§2.4 item 1) |
| §7.6 outcome sentences cut before splits and reasons | **yes**, through what the cut leaves out (line 56) | the line-56 reading **sits beside** (EIGHTH-FIX §3, §6.4; VERDICT "For the coordinator" 3) (§2.2) |
| §7.7 U-1 marked by an inserted block | no | — |
| §7.8 a ratified scope answer sends the question to the user | no (routing) | in the question (lines 222–224) — passes |
| §7.9 `canteen/` not opened | no | — |
| §7.10 script 35 strips dates and item ids; excludes dotfiles | no | — |
| not listed by the run: the first answer ignores the A-0.9 record for the definition's canteen limb | yes, only if the record marks a column outside the four groups as read | neither in nor beside (§2.4 item 7) |

## 5 · Item 3 — handed forward (eighth-fix section, `HANDED-FORWARD.md` lines 685–844)

| item | checkable yes/no | can be met by a run allowed to meet it |
|---|---|---|
| **A-0.1** (lines 711–744) | yes | yes. Note: item 2 and the check exclude only the CARRIES and DATE/CONTENT juror sets; the index's d row (line 77) says "another R-04 group" without defining it; the juror file says "no other question about how exam cards are blinded". Whether a JQ-R04-GATE juror may sit on d is answered differently by the three; a commission can meet A-0.1 and still be read as breaking the other two |
| **A-0.4 step 1** with 1b, 1c, header, check (lines 746–798) | **no**, in three places: (1) **1b** fires when "the composed row holds no feature"; the audit prints "no features left after blinding" also when the row holds features that are all constant or absent — shown for the third answer on all four blinded sets (p1 (6)): a run must judge whether 1b applies; (2) **1c (iii)** stops "while (a) or (b) is not complete for every column the card prints"; every card set prints an hour-offset column that is not among A-0.9's thirteen and has no feature (p1 (3)); read literally the stop fires on every run under the second answer; (3) **the header** must name "the part of the ratified outcome that moves" each feature; for the two reference columns under the second answer that depends on the line-56 reading (§2.2) | **no, as written.** The fourth-fix A-0 (lines 158–165, in force: "every other item stays in force word for word") forbids building any exam card until a run shows A-0.1 to A-0.6 met. A-0.4 is graded "on the exam cards" (fifth-fix, lines 432–434), and step 1 needs the A-0.7 measurement "on the exam cards" on record before the row is composed (lines 760–763) and an empty-row test "on the exam cards" (lines 778–779). No run can show A-0.4 met before an exam card exists, and none may build one before it is shown. The sequence is the fifth fix's; the eighth's step 1 depends on it and no earlier review named it |
| **A-0.9** (lines 800–819) | yes, with one judgement left to the review it names ("unclear"); where the list is delivered is not named | **the record: yes** — a run that may read the frozen book exists (a Mode C run names the frozen rule file; a review). **The delivery: contested.** The last sentence hands the exam-building run "the list: each column's name and 'read', 'not read' or 'referred'". That run is Nadia's (Mode B). `TEAM.md` lines 70–71 bar her from the canteen "So that she does not build the exam around the ideas"; lines 172–174: "so that run never sees the ideas". The list is taken from the book and is used to decide what an exam card keeps. By the letter she reads no canteen; by the stated reason she would. The ratified CONTENT-a outcome carries the same tension (its verdict records the objection, "Note on the 2–1"). Not for me to settle; the item cannot be met without someone deciding it |
| **C-5** (lines 823–844) | yes | yes |

## 6 · Item 4 — the index (`exam-prep/JUROR-QUESTIONS.md`): **true; carries no wording, option or number of a question**

- Every row's status matches the files (p6 (a)): fourteen rows "ratified",
  each naming a verdict file that exists and reads RATIFIED; the d row
  "written — not yet reviewed, not commissioned" (true until this review);
  JQ-B1 withdrawn. Script 35's I and V checks agree (p4).
- The order section (lines 39–59) is true. Its precedent sentence ("every
  juror file ratified so far had first been ruled fit by a review") is
  true: GATE by REVIEW-3, the JQ-N1 group by REVIEW-5, CARRIES and
  DATE/CONTENT by REVIEW-6.
- Shared seven-word runs with any juror file: only provenance lines (p6
  (b)). Numbers: dates, rule numbers, part numbers, canteen line ranges and
  SHA-256 values (p6 (c)).
- Notes, not faults: one answer label of the d file occurs once in the
  index, in a preamble sentence (line 36) present in earlier versions and
  not about d (p6 (d)); "another R-04 group" (line 77) is not defined in
  the index (§5, A-0.1).

## 7 · Item 5 — could a juror-facing file identify an exam coin, a date or a price: **no**

Probe p7 scanned the d file, `RULES.md`, `TACTICS.md`, every juror file the
index names, the canteen book by its named line ranges only, the three
verdicts the d file cites, and the index, against all 795 symbols of the
universe the draw was made from (so it covers the exam coins without my
knowing them), the observation coins, date and time patterns, month and
weekday names, and price-like numbers. **Matched tokens are written only as
SHA-256 prefixes, with file, line and category; no matched word is written
in any file of this review.** Every hit was inspected on screen: ordinary
English words, a modal verb, rule and line numbers, a feature-set name, run
and verdict-folder dates, the study period of TACTICS 0, and (in two
ratified files) figures measured on observation cards. None names a
symbol, a date tied to a card, or a price level. The observation-coin
category had no hit in any file.

## 8 · Reproduction (outputs in `exam-prep/review-8/probes/`)

| what | result |
|---|---|
| p1 — the file's statements about the audit, on raw and four blinded sets | §1 (v), §2.4, §5 |
| p2 — quotations | 30 checked, 0 failed (one first-run failure was my probe not stripping `>` block-quote markers; fixed in the probe, not in any input) |
| p3 — `eighth-fix/FINGERPRINTS.md` | 22 of 22 SHA-256 match (`sha256sum -c`) |
| p4 — `scripts/35_eighth_fix_check.py --dry --show` | run `af9256c4692d40db`: 160 checks, 159 ok, 1 FAIL — "no new exam-prep file outside eighth-fix/", which lists only my own `review-8/` files. Nothing written |
| p5 — the recorded run `5d0fd28862ba755b`'s inputs | 4,571 file inputs and 4 prefix or section inputs hash as recorded; the run number differs only through the two listing inputs |
| p6 — the index | §6 |
| p7 — identification scan | §7 |
| audit SHA-256 | `cfc4bdcb…d03f`, as HANDED-FORWARD names |

Every run used `PYTHONDONTWRITEBYTECODE=1` and `python3 -B`;
`scripts/__pycache__/` held the same nine names before and after; no cache
under `exam-prep/review-8/`. p1 computes features only: it runs no attack,
no chance line and no option effect.

## 9 · What I could not do, by name

1. **The exam draw.** `exam/` is closed, so item 5 is tested against the
   whole universe, not the twenty exam symbols, and not against coin names
   that differ from their symbols.
2. **Nothing measured on exam cards.** p1 uses observation cards; whether
   exam cards print a Wikipedia line, which decides §2.4 item 1 there, I
   cannot see.
3. **Which columns the frozen book reads** — not determined (A-0.9's
   record); so whether §2.4 item 7 bites is unknown.
4. **`LEDGER.md`** — whether the four ratifications are recorded.
5. **The eighth run's instruction** — closed; "not covered by its
   instruction" is taken from EIGHTH-FIX §7 and the files.
6. **The canteen book** beyond probe p7's named ranges — not opened.
7. **§2.3 and the A-0.9 delivery** are judgements on text; another
   reviewer, a referee or the user may weigh them differently.

## 10 · Decisions I took that the instruction did not cover

1. **Hashing matched tokens** in p7 so that no matched word is written in
   any file, including files that never reach a juror.
2. **Scanning against the whole universe** (`data/universe/universe.csv`)
   in place of the exam draw I may not open.
3. **Treating the fourth-fix A-0 as in force** for item 3, because the
   eighth-fix section says every item not replaced stays in force word for
   word.
4. **Ruling §2.3 a fault** while saying it does not decide the row.
5. **Counting the hour-offset column as "a column the card prints"** for
   the literal reading in §5; it is a column of the table, though not a
   TACTICS 3 field.
6. **Probe width of seven words** in p6, carried over from REVIEW-7; a probe
   setting, not a threshold.
7. **Reading the GATE juror file lines 50–70 and the audit's code** to check
   quotations and statements; both are inside what I may read.

## 11 · Steer check

My instruction gives no verdict and predicts no finding. Named, mildly: the
model-choice reason ("a fault in a juror file can only be caught here")
puts weight on finding faults; my rulings rest on the cited text and the
probes. "Neither has the coordinator" (been told how the work was done) is
information. The git status supplied at the start listed, untracked, this
review's instruction and an instruction named for an exam-draw question;
`scripts/` holds a script whose name begins `exam_` and refers to a draw
question (name only; not read). If a run builds exam cards while R-04 is
unclosed, the sequence in HANDED-FORWARD A-0 breaks; I cannot tell from a
name.

## 12 · Fingerprints

`exam-prep/review-8/FINGERPRINTS.md`. This file's own SHA-256 is in my
report to the coordinator. I wrote only this file and `exam-prep/review-8/`.
No commit.
