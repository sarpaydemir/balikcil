RATIFIED

## 1 · Count

Three answers present: juror-1.md, juror-2.md, juror-3.md. Minimum met. ✓

## 2 · Independence

All three jurors declare independence explicitly:
- Juror 1: "Written 2026-10-01 without seeing any other juror's answer. In `decisions/2026-10-01-jq-r04-carries/` I opened nothing; I only wrote this file."
- Juror 2: "Written without seeing any other juror's answer. I opened nothing in `decisions/2026-10-01-jq-r04-carries/` except this file, which I created."
- Juror 3: "Written 2026-10-01. I did not see the other jurors' answers and did not look for them. The only thing I opened in `decisions/2026-10-01-jq-r04-carries/` is this file, which I wrote."

All three arrive at answer C for part a by independent reasoning paths. Part b shows genuine disagreement: jurors 1 and 2 converge on option 1; juror 3 proposes "Other" (option 1 plus part of option 3). No verbatim echoing, no cross-reference, no coordination detected. The convergence on C reflects natural agreement when reading the same text, not collusion. ✓

## 3 · Grounding

All three answers cite files and lines explicitly:

- **Juror 1:** RULES.md lines 51–52, 41, 100–103; TACTICS.md lines 50–51, 56, 101–102; question file lines 74–76, 75–76, 17, 104–106, 112–114, 110–111, 116–117, 118–120, 34–35; `decisions/2026-10-01-jq-r04-gate/verdict.md` line 72; previous verdicts.

- **Juror 2:** RULES.md lines 41, 51–52, 71, 119–121; TACTICS.md lines 56, 101–102; question file lines 74–76, 28–30, 110–114, 104–106, 16–19, 142–143, 118–120, 34–35; `decisions/2026-10-01-jq-r04-gate/verdict.md` line 30; previous verdicts.

- **Juror 3:** RULES.md lines 51–52, 119–121, 34–35, 76–77; question file lines 74–76, 84–85, 93–95, 16–19, 112–114, 104–106, 110–111, 116–117, 118–120; TACTICS.md lines 50–51, 56; `decisions/2026-10-01-jq-r04-gate/verdict.md` line 72; previous verdicts.

All answers extensively grounded. RULES 34 satisfied. ✓

## 4 · The outcome and split for each part

### Part a: Which attack decides?

**Outcome: C.** A column carries a measured coin signature when **either** attack—pair AUC or nearest neighbour—beats its own RULES 12 chance line on the feature set that part b counts as the column's.

- Juror 1: "C. When either attack ... beats its own RULES 12 chance line."
- Juror 2: "C. When either attack ... beats its own RULES 12 chance line."
- Juror 3: "C. On each feature set ... the column carries a measured coin signature when either attack ... beats its own RULES 12 chance line on that set."

**Split: 3–0.** All three agree on C.

### Part b: Which features count as the column's?

**Outcome: Option 1 ("own features, as one set").** The test reads every feature computed from the column's own printed values and from nothing else, tested together as one set. For the trade-count column: its typical level, its two repeat features and its two shape features, not the previous-7-day feature.

- Juror 1: "own features, as one set."
- Juror 2: "Own features, as one set."
- Juror 3: "Other, which is option 1 and option 3 together" — supplementing the own-set row with every existing family made of the column alone.

Juror 3's "Other" answer is a valid option (the question permits "Other, with reasons"). Juror 3 specifies that option 1 is the "necessary core" but wishes to add pure-column families. Juror 3 provides a fallback: "if forced to choose a listed option I choose option 1." However, the primary answer given is "Other," which is materially different: it would test additional feature sets (up to three sets per trade-count column under "Other" vs. one set under option 1 alone).

**Split: 2–1.** Two jurors (1, 2) vote for option 1 (own features, as one set). One juror (3) votes for Other (option 1 plus pure-column families).

### Consistency between parts

Part a defines when the test counts a signature (either attack beats its line). Part b defines which feature sets the test runs on. The parts are logically dependent (part a's test applies to sets named in part b) but logically consistent. Part a's outcome (C: either beats its line) is compatible with both part b outcomes (option 1 alone or option 1 plus pure families). ✓

## 5 · The reasoned objection (RULES 32)

All three jurors identify and acknowledge substantive objections:

**On part a (C):**
All three raise the threshold objection: combining two independent 1% tests creates an effective ~2% false-positive rate, potentially conflicting with RULES 12's "the best 1%."

- Juror 1: "Combining two 1% tests makes a stricter-than-written test... The gate jury met the same objection, and the referee ratified C as procedure."
- Juror 2: "Two 1% lines are not one 1% line... the objection is real." Replies with reasoning about RULES 12 and gate precedent.
- Juror 3: "Up to about 2% for the trade-count column... The threshold objection is real. It is the same one the gate jury met, and the referee ratified over it."

All three provide reasoned replies and maintain answer C. No juror claims the objection overrides their conclusion.

**On part b:**
- Juror 1: Acknowledges "Dilution" (some signatures could be hidden) and "needs new measurement" objections. Replies and maintains answer.
- Juror 2: Acknowledges "Dilution" and "new measurement unit" objections. Replies and maintains answer.
- Juror 3: Acknowledges "Unequal treatment" (different error rates for different columns), "not a listed option" (could split count), and "Option 3's case." Explicitly states: "A juror who chose option 1 for that reason has a case as good as mine." Maintains answer with reasoning.

**Verdict on objections:** All objections are real and well-reasoned. All jurors engage them with counter-reasoning and maintain their answers. Juror 3's acknowledgment that "a juror who chose option 1... has a case as good as mine" is recognition of difficulty and uncertainty, not a reasoned blocker preventing ratification. No juror claims their objection should prevent ratification. RULES 32 does not block this outcome. ✓

## 6 · Scope

RULES 33 forbids a juror to decide "a trading rule, never a threshold or score, and never a change to a rule in this file."

All three jurors:
- **Part a:** Define how the audit's two attacks combine into "carries a measured coin signature." Do not change RULES 12 lines (each attack stays at 1,000 shuffles, best 1%). Do not set a threshold or score.
- **Part b:** Define which features count as "the column's." Use features already computed from the audit's code (not invented) or explicitly named in the question. Do not set a threshold, score, or trading rule.
- **Explicitly state:** Do not decide whether a column may be left out (RULES 33, question file lines 33–35). Do not change RULES.md.

All answers decide procedure and definition only, within RULES 33 scope. ✓

**Consistency with ratified verdicts:** The prior verdict on the gate question (decisions/2026-10-01-jq-r04-gate/verdict.md, RATIFIED 3–0) decided that "The gate fails if either the nearest-neighbour attack or the pair AUC attack beats its own RULES 12 chance line." All three jurors cite this verdict for part a. The current part a outcome (C: either attack beats its line) is consistent with and supportive of the ratified gate verdict. No contradiction. ✓

---

## Ratification

All six checks pass:
1. Count: 3 answers ✓
2. Independence: All declare independence, no collusion ✓
3. Grounding: All extensively cite files and lines ✓
4. Outcome and split: Part a 3–0 (unanimous), Part b 2–1 (majority for option 1) ✓
5. Reasoned objection: All objections addressed by jurors themselves; no unaddressed blocker ✓
6. Scope: All within scope as definitions; consistent with ratified verdicts ✓

---

## Verdict

**The jury settles JQ-R04-CARRIES as follows:**

**JQ-R04-CARRIES-a:** When the test in part b identifies a column's feature sets, the column carries a measured coin signature when **either** the pair AUC attack or the nearest-neighbour attack beats its own RULES 12 chance line on that set. Split: 3–0.

**JQ-R04-CARRIES-b:** The test reads every feature computed from the column's own printed values and from nothing else, tested together as one set. For the trade-count column: its typical level, its two repeat features and its two shape features, not the previous-7-day feature. The audit gains this set as a row of its own. Split: 2–1 (majority for option 1; one juror proposes supplementing with pure-column families, both implementations possible).

Both parts can be carried out together. All grounded, independent, no reasoned blocker, all within scope.
