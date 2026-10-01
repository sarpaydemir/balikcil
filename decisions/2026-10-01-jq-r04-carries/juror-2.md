# JQ-R04-CARRIES · juror 2 · 2026-10-01

Written without seeing any other juror's answer. I opened nothing in
`decisions/2026-10-01-jq-r04-carries/` except this file, which I created.

Abbreviation: "Q" means `exam-prep/sixth-fix/juror-questions/JQ-R04-CARRIES.md`.

---

## 1 · Answer

### JQ-R04-CARRIES-a

**C.** A column carries a measured coin signature when **either** attack (pair
AUC or nearest neighbour), run on the feature set that part b assigns to the
column, beats its own RULES 12 chance line. Each line stays exactly as RULES 12
fixes it.

### JQ-R04-CARRIES-b

**Own features, as one set.** The test in part a reads every feature computed
from the column's own printed values and from nothing else, tested together as
one set. For the trade-count column that is its typical level, its two repeat
features and its two shape features. It does not include the previous-7-day
feature. The audit gains this set as a row of its own. Which features are
computed from the column is read from the audit's code, as Q lines 118–120
already require. It is not chosen.

### How the two parts depend on each other

- Part a takes the set that part b names. Under my part b there is **one** set
  per column, so C combines **two** results, each against its own line. That is
  the same structure as the ratified gate (below).
- If part b were ratified as "every family that reads the column", my answer to
  part a would still be C, but my confidence in it would drop. Under that
  reading, C would combine six results for the trade-count column (3 families ×
  2 attacks), and the case against below (several chances to beat a 1% line)
  would weigh much more heavily. I flag this. I do not change my answer
  because of it.
- The nearest-neighbour tie problem (two versions disagreeing) is not mine to
  settle. Q lines 93–95 already settle it: "the run that measures stops, and
  the point is referred." My answer does not relax that stop, even in a case
  where pair AUC alone would already decide the outcome under C.

### What I do not decide

I set no chance line, threshold, score or trading rule. I do not decide
whether a column may be left out; that is JQ-R04-CONTENT. I change no rule.

### Reversibility

The definition is applied to a measurement taken "before any exam card is used"
(Q lines 20–21). Until the blinding is frozen and the answer key sealed, it is
reversible at the cost of re-running the audit. Once exam cards have been sat
on a blinding that relied on it, reversing it means a new blinding and a new
sitting. I have not measured that cost and give no number.

---

## 2 · What it rests on

### Part a

1. **What the audit says an attack measures.** Q lines 74–76: "For a set of
   features it asks whether they tell which coin a card is, by two attacks,
   each compared with its own RULES 12 chance line". Each attack is a separate
   measurement of the same property: whether the set tells the coin. When one
   of them beats its line, the laboratory has *measured* that the set tells the
   coin. The words to be defined are "carries a **measured** coin signature".
   An attack that beats chance is such a measurement. B and A each discard a
   measurement the audit makes. D refuses to count a measurement unless a second
   one agrees.
2. **The rule the signature threatens.** `RULES.md` line 41 (RULES 9): "In the
   exam the coin name and the date are hidden." `TACTICS.md` line 102: "the
   coin name". A coin signature is a way the coin name gets out. A definition
   of "carries a signature" exists to detect that, so it should count a leak
   that either measurement detects.
3. **The chance line is untouched.** `RULES.md` lines 51–52 (RULES 12): "The
   answers are shuffled 1,000 times, and the real result must fall inside the
   best 1%." Under C each attack is judged against its own line unmodified, as
   Q lines 75–76 and 84–85 describe ("An attack **beats** its line when its
   result is above the line").
4. **Laboratory precedent. It is consistent with my answer but does not settle
   this question.** `decisions/2026-10-01-jq-r04-gate/verdict.md` line 72:
   "**The gate fails if either the nearest-neighbour attack or the pair AUC
   attack beats its own RULES 12 chance line on the exam cards.** Split: 3–0."
   That verdict also addressed the objection that choosing among A–D is a
   threshold (line 42: "an effective ~2% false-fail rate"). The referee found
   it within scope (line 64: "All three answers decide a procedure (which
   measurement(s) the gate applies) without setting thresholds"). That verdict
   is about a gate on the `ALL-removable` row (line 30), not about a single
   column, so it does **not** settle part a. But a laboratory where the gate
   finds a coin signature when either attack beats its line, while a column
   "carries" one only when both do, would hold two incompatible meanings of
   "a measured coin signature" for the same two attacks on the same exam cards.
5. **Scope.** `RULES.md` lines 119–121 (RULES 33): "A juror decides procedure
   and definition only: never a trading rule, never a threshold or score".
   Q lines 45–47 ask whether choosing among A–D is a threshold. My view is that
   it is not: no number is set, and both lines are RULES 12's. The ratified
   gate verdict (line 64) took the same view.

### Part b

1. **The thing being defined is a column.** Q lines 28–30: "what 'carries a
   measured coin signature' means when it is said of one printed column of an
   exam card". `TACTICS.md` line 56 lists "trade count" as its own item on the
   card. The question it serves (Q lines 16–19) asks about leaving out "a
   column". The unit of the claim is the column, so the unit of the
   measurement should be the column: all of its printed values, and nothing
   else.
2. **Why not "every family that reads the column".** Q lines 110–114: the
   `shape-scale-free` family "holds these two features for seven other columns
   as well (`quote vol`, `open int`, `depth -1%`, `depth +1%`, `L/S acct`,
   `top L/S pos`, `taker L/S`)". If that family beats its line, the result may
   come entirely from the other seven columns. Saying the trade-count column
   "carries" it would claim more than was measured. That conflicts with
   `RULES.md` line 71 (RULES 19): "An unmeasured number is not written down."
   The same applies to `trades-level`, which Q lines 104–106 say "also holds
   one feature read from the previous-7-day line, not from the column".
3. **Why not "only families made of the column alone".** For the trade-count
   column this reads `repeat-trades`, and `trades-level` only on some card sets
   (Q lines 156–158). It never reads the column's two shape features, because
   those sit only in a mixed family. It would therefore define the column's
   signature without part of the column. It would also make the definition
   change with which card set is measured. Q lines 118–119 say "Which features
   are computed from which column is read from the audit's code, not chosen";
   the families, by contrast, are how the audit happens to group features.
4. **One pre-declared set, tested as a whole, matches how the laboratory
   measured the gate.** `decisions/2026-10-01-jq-r04-gate/verdict.md` line 30:
   the gate is read "on the `ALL-removable` row". That is a single combined
   set, not a per-family union. Testing one set per column also keeps the
   number of chances to beat a 1% line at two per column, the same as the
   gate. That is closest to the spirit of `RULES.md` lines 34–35 (RULES 6):
   "The rule is written first, the result is opened second."
5. **The new row is computed, not chosen.** Q lines 142–143: "The audit gains
   this set as a row of its own." The set's membership follows from Q lines
   118–120. No number is introduced.

---

## 3 · The strongest case against my answer

### Against part a (C)

- **The laboratory demands "all", not "either", for a positive finding.**
  `RULES.md` line 50 (RULES 11): "A finding that cannot beat all three does not
  count as 'learned'." `TACTICS.md` lines 130–134 make the exam's passing
  condition a conjunction ("beats the chance line, **and** beats Tomás, **and**
  beats the simple rule"). "This column carries a coin signature" is itself a
  positive claim about the data. On that reading it should need D, not C, and
  C lets a single lucky attack make the claim.
- **Two 1% lines are not one 1% line.** With two chances, the probability that
  a column with no signature is declared to carry one is up to about 2%
  (estimate, union bound; not measured; lower if the attacks are correlated).
  RULES 12 says "the best 1%". A referee could hold that any choice among A–D
  sets that effective rate and so is a threshold, which Q lines 45–47 put
  outside a juror's scope.
- **The direction of the consequence.** In JQ-R04-CONTENT the condition
  "carries a measured coin signature" is one of the conditions under which a
  column that `TACTICS.md` line 56 puts on the card might be left out. C makes
  that condition hold more often than D does. So C leans toward departing from
  TACTICS 3, whereas in the gate question "either" leaned toward caution.

My reply: the attacks are not rivals to beat. They are two instruments looking
for one leak, and RULES 9 is the rule the leak would break. A leak that one
instrument finds beyond RULES 12 chance has been measured. RULES 11's "all
three" is about rivals to a claim of skill, which is a different situation.
I still count the objection as real, not as a straw man.

### Against part b (own features, as one set)

- **Dilution.** Pooling all of a column's features into one similarity can
  hide a signature that a subset carries strongly. For example, the two repeat
  features might separate coins clearly while the shape features add noise, so
  the pooled set fails to beat its line. Then the column would really carry a
  signature, which `repeat-trades` alone, a family made only of this column,
  could show, and my definition would say it does not. A defensible "Other"
  would therefore count the own-features set **or** any family made of the
  column alone. I rejected that because it adds chances to beat the line,
  which makes the strictness choice more threshold-like. But I cannot claim my
  set loses no real signal.
- **It is a new measurement unit.** Q lines 116–117: "It does not today test a
  column's own features as one set apart from the families." The families are
  what the audit measures and reports today, and option 2's ground (Q lines
  151–152) is that each of them "measures the column". My answer creates work
  and a new row. If family-level results on any card set already exist and
  have been seen by anyone, choosing a new unit now is uncomfortably close to
  RULES 6. I do not know whether such results exist (I was not allowed to look),
  and I list this as an unknown.

---

## 4 · Confidence

- **Part a: 4/5.** I would change my mind if a written laboratory rule required
  two measurements of the same property to agree before the property counts as
  measured. In RULES.md and TACTICS.md I found conjunctions only for passing
  against rivals (RULES 11, TACTICS 7). I would also change my mind if the
  referee ruled that choosing among A–D is a threshold. In that case my answer
  would become "the rules do not settle this, and it is not a juror's", and the
  same would then apply to the ratified gate verdict.
- **Part b: 3/5.** I would change my mind if the audit's code showed that the
  column's own features cannot be computed as one set on the exam cards (for
  example, if every one of them is constant or missing on some card, see Q
  lines 86–87). I would also change my mind if a laboratory document defined a
  column's signature at the family level. I found none in RULES.md, TACTICS.md,
  TEAM.md, README.md or the permitted verdicts.

---

## Files read

`exam-prep/sixth-fix/juror-questions/JQ-R04-CARRIES.md`; `RULES.md`;
`TACTICS.md`; `TEAM.md`; `README.md`;
`decisions/2026-09-19-{zero-trade-contracts,tokenized-equity,calm-separation,large-moment-selection,effort-level,watcher-across-runs,card-order-requirement}/verdict.md`;
`decisions/2026-10-01-jq-r04-gate/verdict.md`;
`decisions/2026-10-01-jq-n1-canteen-8/verdict.md`. I did not open anything in
`exam/`, and no other juror's answer.

## Assumptions, by name

- That Q's description of the audit (features, families, attacks, tie versions)
  is accurate. I could not read the audit's code.
- That "the features part b counts as the column's" in Q line 126 means the set
  is fixed before part a's attacks are run, as one row.
- Unknown: whether family-level audit results already exist and have been seen.

## Steer

I saw no steer. Q's closing section is headed "not to steer", and it states
only what the answer decides. The listed grounds for the part b options are
given for every option. The instruction points to the gate verdict as an
earlier decision. That is a relevant precedent named among all of them, not a
result about this question.
