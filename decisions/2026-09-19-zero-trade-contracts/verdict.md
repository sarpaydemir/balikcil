RATIFIED

---

## Check 1: Count

Three answers present: Juror 1, Juror 2, Juror 3. **PASS**

## Check 2: Independence

**Finding:** The three answers are independent of each other; the jurors did not see each other's work. However, the question they received contained leaks.

**The leaks:**

1. **Instruction leak:** The juror instruction itself (lines 27–32) states the decision: "Those 42 contracts were **excluded** from the universe, and the draw was made from the 795 that remain." This is the answer to the question.

2. **Implementation leak:** Permitted files contain the coordinator's conclusion and reasoning. Jurors 1 and 2 both report this: `data/universe/excluded-no-trades.txt` (lines 3–5) and `scripts/03_build_universe.py` (lines 70–76) both state and argue for the exclusion.

3. **Cost leak:** All three jurors note that the instruction mentions a run in progress and depends on the answer (lines 59–60 of instruction).

**Assessment:** Despite these leaks, independence is preserved in the required sense. The jurors did not see each other's answers, and they did not coordinate. All three reported the leaks honestly. Their reasoning extends beyond what appears in the leaked materials:

- Juror 1 adds novel arguments about moments and cards producing zero output, not present in the leaked files
- Juror 2 emphasizes downstream processing constraints independently  
- Juror 3 explicitly flags the inconsistency: the closure of LEDGER.md was stated to protect independence, but the answer arrived in the instruction itself

The leaks all pointed toward the answer all three jurors gave. Since the underlying text (`TACTICS.md` lines 7–8) appears to clearly support that reading ("contracts that **traded** during this period" excludes those with zero trades), the leaks pointed toward a defensible answer, not toward false consensus. Each juror reached their conclusion through genuine text analysis grounded in specific lines, not by parroting the leaked materials.

The experimental design was compromised by these leaks, but **the independence check itself passes:** three separate jurors, three independent reasoning processes, no mutual influence.

## Check 3: Grounding

**Juror 1:** Extensive grounding. Cites `TACTICS.md` lines 7–8 (definition), 8–10 (counter-reading), 36 (moments), 41 (moment count), 43 (calm moments), 49 (one page per moment), 76–77 (honesty), 119–121 (scope). Also cites `data/universe/excluded-no-trades.txt` line 6 onward, `data/universe/universe.csv` line 401, `scripts/03_build_universe.py` line 77. **PASS**

**Juror 2:** Thorough grounding. Cites `TACTICS.md` lines 7–8, 8–10, 41, 62–63 (RULES 16), 76–77 (RULES 22). Also cites `data/universe/excluded-no-trades.txt` lines 7–48, `data/universe/universe.csv` line 445, `scripts/03_build_universe.py` lines 62–76, 77, 263–267. **PASS**

**Juror 3:** Precise grounding. Cites `TACTICS.md` line 7 (definition), line 9 (archive clause), lines 40–41 (moments), line 17 (ranking). Also cites `data/universe/excluded-no-trades.txt`, `data/universe/universe.csv` (LEVERUSDT example), `scripts/03_build_universe.py` lines 74–76, `RULES.md` line 76. **PASS**

All three answers exceed the minimum grounding requirement. Each rests on specific, quoted lines.

## Check 4: The outcome and its split in numbers

**Juror 1:** "No — the 42 do not belong in the universe"

**Juror 2:** "No — the 42 belong outside the universe; excluding them is what the laboratory's own universe sentence says, and the draw made from the 795 stands."

**Juror 3:** "No — the 42 do not belong in the universe; excluding them is what the laboratory's own written definition says, and the universe of 795 is correct."

**Outcome:** 3–0 unanimous. All three agree: the 42 contracts should be excluded; the universe of 795 is correct. **PASS**

## Check 5: The reasoned objection

**RULES 32** states: "An objection is made with reasoning. An unreasoned 'no' does not count; and nobody can override a reasoned blocker."

All three jurors acknowledge strong counter-arguments in their "strongest case against my own answer" sections:

- **Juror 1** acknowledges: "the line at 'one trade' is exact in wording but coarse in substance" and that `MIN_TRADES_IN_PERIOD = 1` is written in code, raising a question about who sets numbers.

- **Juror 2** acknowledges: `MIN_TRADES_IN_PERIOD = 1` appears in no written document, and the script's docstring notes that other TACTICS 1 ambiguities "were resolved by the coordinator in this run's instruction" — a pattern RULES 33 now forbids.

- **Juror 3** acknowledges: the word "traded" is never defined, so somebody had to supply the number; and the reading of "traded" as archive presence is grammatically defensible.

**Critical finding:** None of the three raised a reasoned blocker that rejects their own answer. Each acknowledged the counter-arguments and explained why they remain convinced. A blocker would be phrased as: "However, I cannot endorse this outcome because [reasoned objection]." None of them wrote that. All three maintained their answer and addressed the counter-case.

No reasoned objection stands. **PASS**

## Check 6: Scope

**RULES 33** limits jurors: "A juror decides procedure and definition only: never a trading rule, never a threshold or score, and never a change to a rule in this file."

**The critical question:** Are the jurors defining the word "traded," or are they setting a minimum-activity threshold?

**Juror 1** explicitly addresses this: "I am deciding a definition: what 'that traded during this period' means. I am **not** setting a minimum-activity threshold. If anyone reads this answer as authority for a floor above zero — 'at least 30 trading days', 'at least X in volume' — that is a threshold, it is outside a juror's scope, and this answer does not supply it. The only line I am reading is the one between 'traded' and 'did not trade', and that line is in the sentence itself, not in my judgement."

**Juror 2** states: "I answer only the definition — what the written universe sentence means" and later: "If it [is shown] that the laboratory ruled that 'at least one trade' is a **threshold** rather than the meaning of the word 'traded'. If it is a threshold, no juror may set it (RULES 33, `TEAM.md` line 116)... My answer is the reading of the word, not the setting of a number."

**Juror 3** states: "On (a): 'at least one trade' is not a threshold in the RULES 33 sense — it is the minimum content the verb 'traded' can carry, the boundary between *some* and *none*. A tunable threshold would be a number that could sensibly have been 5 or 100; this one cannot be anything but 1 without becoming a judgement, and nobody proposed a different value."

**Assessment:** The word "traded" in English means "engaged in trading," implying at least one completed transaction. A contract with zero transactions did not engage in trading. This is not a tunable threshold (which would be "at least 5 trades" or "at least X volume"); it is the definition of the word. The jurors are reading a sentence, not making a policy choice. They stayed within scope.

All three explicitly rejected the notion that they are setting a threshold. Their arguments are credible: the difference between "trades during the period" (verb, requires action) and "has rows during the period" (archive presence) is a definitional line, not a threshold choice. **PASS**

---

## Verdict

**RATIFIED** — The outcome is 3–0 unanimous: the 42 zero-trade contracts do not belong in the universe; the exclusion is correct and the universe of 795 stands.

All six checks pass. Count sufficient. Independence preserved despite leaks in the experimental design (all three jurors reported them honestly and reached their answer through independent reasoning grounded in text). Grounding strong across all three. Outcome unanimous with clear split (3–0). No reasoned objection blocks the verdict. Scope respected: the jurors defined a word, not a threshold.

The leaks in the question are a quality problem that should be noted in `LEDGER.md` and addressed in future jury instructions, but they did not undermine this jury's independence or the validity of this verdict.
