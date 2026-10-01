RATIFIED

---

## The six checks

**1. Count:** Three answers. ✓

**2. Independence:** No quoting, echoing, or naming across answers. All three declare they saw no other juror's work. The DATE parts reach similar conclusions by different reasoning emphases. CONTENT-a diverges: Jurors 1 and 3 yes, Juror 2 no, with distinct grounds (Juror 2 objects that no document grants removal and the canteen condition violates TEAM.md; Jurors 1 and 3 permit removal when the measured signature is the trigger). ✓

**3. Grounding:** All six parts grounded in all three answers. Each cites files and line numbers: RULES.md, TACTICS.md, JQ-R04-DATE.md, JQ-R04-CONTENT.md, README.md, TEAM.md, canteen/2026-09-19-sofia.md excerpts, decisions/2026-10-01-jq-r04-gate/verdict.md. ✓

**4. Outcome and split:**

- **JQ-R04-DATE-a** (remove bitcoin/ethereum columns?): No. Split 3–0.
- **JQ-R04-DATE-b** (release names identify day?): No. Split 3–0.
- **JQ-R04-DATE-c** (offsets reveal clock hour?): No. Split 3–0.
- **JQ-R04-CONTENT-a** (remove column when nothing frozen reads it and measured signature exists?): Yes (split 2–1: Jurors 1, 3 yes; Juror 2 no).
- **JQ-R04-CONTENT-b:**
  - **b1** (actual price rebased to 100, fixed decimals): Yes. Split 3–0.
  - **b2** (computed from printed chg%, starting at 100): Yes. Split 2–1 (Jurors 2, 3 yes; Juror 1 no).
  - **b3** (no price column; chg% stays): Permitted only through CONTENT-a. Split 2–1 (Jurors 1, 3 yes-if-CONTENT-a; Juror 2 no).
- **JQ-R04-CONTENT-c** (ranked column from pre-rounding values?): No. Split 3–0.

The parts' outcomes are consistent with their stated dependencies. CONTENT-a outcome depends on CONTENT-c (which rendering the exam card would use): CONTENT-c is 3–0 no to pre-rounding, so the rendering is printed-value ranks. CONTENT-a's 2–1 yes applies when measured signature exists in that rendering. CONTENT-b's b3 outcome depends on CONTENT-a and is stated as conditional on it. CONTENT-b's b1 has a precision condition from CONTENT-c and is applied consistently across answers. ✓

**5. Reasoned objection (RULES 32):** Each juror presents the strongest case against their own answer and replies with reasoning. Juror 2 calls the CONTENT-a case "the case I find hardest to answer" and Juror 3 calls DATE-a "the case I take most seriously," but neither raises a reasoned objection that blocks their verdict. All reasoning is addressed and explained. No unreasoned veto. ✓

**6. Scope:** All three jurors declare "Rule change: none." No trading rule, threshold, score, or change to RULES.md is decided. All decisions are definitional as required by RULES 33. ✓

---

## Ratification

All six checks pass. The three jurors have provided grounded, independent, reasoned answers to a six-part open question. The outcomes are clear: five parts at 3–0, one part (CONTENT-a) at 2–1, and b2 at 2–1. No reasoned objection blocks ratification. All answers stayed within scope.

**Ratified outcomes, by part:**

- JQ-R04-DATE-a: Do RULES 9 and TACTICS 6 require removing columns that identify clock hours? **No.** The columns print no date or time. (3–0)
- JQ-R04-DATE-b: Does hiding "the date in the release calendar" cover release *names* that identify the day? **No.** It covers the printed date in that field; the name is TACTICS 3's content. (3–0)
- JQ-R04-DATE-c: Does hiding "the date and time" cover clock hour revealed by an offset plus outside knowledge of release times? **No.** It covers printed date or time; inference from public knowledge is not printed. (3–0)
- JQ-R04-CONTENT-a: May the blinding remove a TACTICS 3 field when nothing frozen reads it and it carries a measured coin signature? **Yes** — when both conditions hold: nothing the frozen canteen book reads it, and in the rendering the exam card would otherwise carry, it carries a measured coin signature as JQ-R04-CARRIES defines one. (2–1: Jurors 1, 3 yes; Juror 2 no. Juror 2 objects that no document permits removal and a canteen-dependent rule violates TEAM.md lines 70–71. Jurors 1 and 3 rest on RULES 9 and measured signature alone.)
- JQ-R04-CONTENT-b:
  - **b1** (actual price rebased to 100, fixed decimals): Permitted. (3–0)
  - **b2** (computed from printed chg%, starting from 100): Permitted. (2–1: Jurors 2, 3 yes; Juror 1 no. Juror 1 objects that b2 is not "the price itself" but a derived reconstruction, and does not permit b2 unless token-for-token identical to b1. Jurors 2 and 3 read both as valid conversions under TACTICS 6 line 104.)
  - **b3** (no price column; chg% stays): Permitted only if and as far as CONTENT-a yes. (2–1: Jurors 1, 3 yes-through-CONTENT-a; Juror 2 no. Juror 2 objects that b3 removes a TACTICS 3 field and is not permitted. Jurors 1 and 3 permit it only through the CONTENT-a permission.)
- JQ-R04-CONTENT-c: May a ranked column come from pre-rounding values, ordering hours the raw card prints as equal? **No.** The exam card is the observation card with things hidden, never with things added. Ranking from pre-rounding values adds an order the card never carried. (3–0)

The outcomes are consistent with each other and with the dependencies the questions stated.

---

## Effect on exam cards

Before any exam card is built and sealed, the outcomes permit the following:
- For the three DATE parts (a–c): the specified columns and fields stay on the exam card. The laboratory will audit which channels they provide for coin or date identification and name them in the exam manifest.
- For CONTENT-a: when a column carries a measured coin signature (tested before cards are sealed) and nothing in the frozen canteen book reads it, the column may be left out. Whether any column meets both conditions is a measurement question, not this verdict's concern.
- For CONTENT-b: b1 (actual price, fixed decimals) is permitted; b2 (computed from chg%) is permitted; b3 (omit price, keep chg%) is permitted only if CONTENT-a's conditions are met for that field.
- For CONTENT-c: ranked columns must come from the values the card prints. The rendering is ranks from printed values.

Engineering and audit follow. Nothing in this verdict changes RULES.md or any other rule.

---

## Note on the 2–1 on CONTENT-a

Juror 2's objection is reasoned and substantial: no document in RULES, TACTICS, TEAM, or README grants the blinding power to remove a field that TACTICS 3 lists, and grounding removal on whether the frozen book reads the field means building the exam around the book's ideas, which TEAM.md forbids. Jurors 1 and 3 reply that the measured signature standard (ratified in the gate verdict) is the trigger, independent of the book. Both readings are grounded and their split is a genuine disagreement on how to reconcile RULES 9 with TACTICS 3 when the method measurably fails to meet the rule. The 2–1 split stands.
