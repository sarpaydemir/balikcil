# Juror 3 · JQ-R04-CARRIES-a and -b

Written 2026-10-01. I did not see the other jurors' answers and did not look for them. The only thing I opened in `decisions/2026-10-01-jq-r04-carries/` is this file, which I wrote.

The two parts depend on each other in one direction. Part a's test runs on "the features that part b counts as the column's" (question file line 126). My answer to part a is the same whichever set part b names, so it does not depend on part b. Part b decides how many sets the part a test runs on, so what part a finally says about a column depends on part b. I say below where this matters.

---

## 1 · Answer

### JQ-R04-CARRIES-a

**C. On each feature set that part b counts as the column's, the column carries a measured coin signature when either attack, pair AUC or nearest neighbour, beats its own RULES 12 chance line on that set.** A result equal to its line does not beat it (question file lines 84–85). I leave alone the case the question excludes, where the two nearest-neighbour versions disagree on whether that attack beats its line (lines 93–95). Then the run stops and refers, as written.

One observation, which I do not rule on. Under C, if pair AUC beats its line on the same set, a disagreement between the two nearest-neighbour versions could not change the outcome. Whether the run must still stop in that case is for whoever handles the referral. The question text says it stops, and I do not change that.

### JQ-R04-CARRIES-b

**Other, which is option 1 and option 3 together. The column's feature sets are every audit set whose features, as the audit uses them on the card set measured, are all computed from the column's own printed values and from nothing else.** These are:
- (i) the "own features, as one set" row that option 1 describes, which the audit gains, and
- (ii) every existing family made of the column alone, as option 3 describes.

The column carries a measured coin signature when part a's test holds on any of these sets.

For the trade-count column this means:
- the own-set row: typical level, the two repeat features and the two shape features, but not the previous-7-day feature;
- `repeat-trades`;
- `trades-level`, but only on a card set where the previous-7-day feature is not used.

`shape-scale-free` is never one of this column's sets, because it holds the features of seven other columns.

Some features in a set may be unusable, meaning constant on every card or missing on a card (lines 85–87). They drop out as the audit already rules. A set left with no usable feature is not a measurement. It shows no *measured* signature, and the run must list it by name as "could not be measured", not as "no signature" (RULES 22).

**If the referee must count this against the listed options:** the necessary core of my answer is option 1, and if forced to choose a listed option I choose option 1. I never choose option 2.

---

## 2 · What it rests on

### Part a

- **RULES 12, `RULES.md` lines 51–52:** "The chance line is not invented. The answers are shuffled 1,000 times, and the real result must fall inside the best 1%." This is the laboratory's only written definition of when a measured result counts as more than chance. It applies to *a result*.
- **Question file lines 74–76:** the audit asks "by two attacks, **each compared with its own RULES 12 chance line**." So each attack is a separate result with its own line. A "measured" signature is one that a measurement shows beyond its chance line. When either attack's result falls inside its best 1%, the audit has measured a signature.
  - D would need two results, which is more than RULES 12 asks of any one result.
  - A and B would each discard one of the audit's two written measurements. No line in `RULES.md`, `TACTICS.md`, `TEAM.md`, `README.md` or the question gives a ground for preferring one attack. I looked in all of them.
- **Ratified precedent, `decisions/2026-10-01-jq-r04-gate/verdict.md` line 72:** "The gate fails if either the nearest-neighbour attack or the pair AUC attack beats its own RULES 12 chance line on the exam cards. Split: 3–0." That jury answered for the whole removable row how the same audit's same two attacks combine into "the cards tell the coin". Giving the same audit a different combining rule when the unit is one column would leave the laboratory with two inconsistent meanings of "the audit measured a coin signature". This verdict does not settle part a, because it ruled on a gate and not on a column-level definition. It does weigh directly on it.
- **Scope, RULES 33, `RULES.md` lines 119–121:** "A juror decides procedure and definition only: … never a threshold or score". C leaves both lines exactly as RULES 12 fixes them. It adds no number and changes no line. The gate verdict (lines 40–52) records that the same objection, that choosing how two lines combine sets an error rate, was raised and answered there, and ratification went ahead.

### Part b

- **The words being defined:** "it carries a measured coin signature", said of "a column that TACTICS 3 puts on the card" (question file lines 16–19). The subject is the column. What a column can carry is what its own printed values carry. A feature read from another line or column is a measurement of that other thing (question file lines 144–146).
- **Why not option 2.** Question file lines 112–114: `shape-scale-free` "holds these two features for seven other columns as well (`quote vol`, `open int`, `depth -1%`, `depth +1%`, `L/S acct`, `top L/S pos`, `taker L/S`)." Under option 2, if that family beat its line, all eight columns would "carry" the signature at once, even if all of it came from, say, `open int`. A definition that cannot tell one column from another is not a definition of a *column* carrying something. The same applies, more mildly, to `trades-level`. Lines 104–106 say its previous-7-day feature is "read from the previous-7-day line, not from the column". That line is a separate item on the card (`TACTICS.md` lines 50–51: "the 24 hours before the start, hour by hour; plus a one-line summary of the previous 7 days").
- **Why not option 3 alone.** Question file lines 110–111 put two of the column's own features, "the spread of the logarithms of the column's values, and how closely each hour's logarithm follows the previous hour's", in `shape-scale-free` only. Option 3 excludes that family, so it would never test those two features for this column. A signature carried by the column's own values in those features would then go unmeasured and be reported as no signature. That is the move RULES 22 forbids (`RULES.md` lines 76–77: "'Could not be measured' never turns into 'no problem'.").
- **Why the own-set row is necessary.** Question file lines 116–117: "It does not today test a column's own features as one set apart from the families." Without that row, no existing unit tests all of this column's features and only them.
- **Why the pure families stay in, besides the own-set row.** Both attacks are similarity measures over a feature set (lines 78–82). Adding features that carry nothing can wash out the similarity that one feature carries. That is a property of how such measures behave; I have not measured it on these cards. A family made only of this column's values (e.g. `repeat-trades`, lines 107–109) is just as much a measurement of the column as the own-set row, and its units are "read from the audit's code, not chosen" (line 118). If such a measurement beats its RULES 12 line, saying the column carries no measured signature would contradict the measurement.
  - This is the same reasoning as part a and as the gate verdict: any valid measurement of the thing that beats its own line counts.
  - The criterion that picks the sets is **where the inputs come from** (only this column), not a chosen strictness.
- **The rule applies the same way to other columns.** Question file lines 118–120 say which features come from which column "is read from the audit's code … for any other column it is read the same way, and the run that measures records it". My definition uses only that record. For a column whose features all sit in mixed families, only its own-set row applies.
- **Timing, RULES 6, `RULES.md` lines 34–35:** "The rule is written first, the result is opened second." The question says the exam-card measurement happens after this definition (line 20–21: "will be measured before any exam card is used"). Defining the set now, including the new row, comes before that result.

---

## 3 · The strongest case against my answer

### Against part a (C)

The direction of caution is the opposite of the gate's. In the gate, "either" erred towards blinding more, and the gate jurors argued from that. Here, per question file lines 15–19, "carries a measured coin signature" is a condition under which a column that TACTICS 3 puts on the card (`TACTICS.md` line 56: "price, volume, trade count, taker buy/sell pressure") *may* be left out. C makes that condition true more often:
- one set judged by two 1% lines has a combined chance of a false "carries" of up to about 2% (estimate, an upper bound under independence; not measured);
- so C widens a permission to depart from a written tactic.

Someone could say:
- that D is the reading that protects the written card;
- that RULES 12's "the best 1%" should hold for the combined claim, not for each attack;
- and that a juror choosing between C and D is in substance choosing how strict the test is, which is a threshold (RULES 33).

My reply: my reason for C is what "measured" means, a result beyond its own RULES 12 line, not which side the error falls on. I deliberately do not weigh the downstream permission, because whether a column may be left out belongs to other jurors (question file lines 33–35). The threshold objection is real. It is the same one the gate jury met, and the referee ratified over it.

### Against part b ("Other": own-set row plus pure families)

1. **Unequal treatment caused by how the code is organised.** Under my answer the trade-count column gets up to three sets, each tested two ways, while a column whose features sit only in mixed families gets one. A column's chance of a false "carries" therefore depends on how the audit's code happens to group features. That is not a property of the column. Up to about 6% for the trade-count column against up to about 2% for a one-set column: estimates, upper bounds under independence, not measured.
   - Option 1 alone gives every column exactly one set and treats all columns alike.
   - That is a strong argument, and a juror who chose option 1 for that reason has a case as good as mine.
   - My counter: the extra sets are measurements of this column alone, and defining "carries" so that a pure measurement beating its line still counts as "no measured signature" seems to me worse.
2. **"Other" is not a listed option.** It adds an audit row, which the question allows only under option 1. It could split the count and leave no outcome (RULES 35: "A tie is no outcome"). That is why I gave option 1 as my fallback.
3. **Option 3's case.** The families are the units the audit was built and reviewed with, and a new row is a new instrument added at the definition stage. My reply: an added row changes nothing already measured. It is defined before any exam result. Without it, two of the column's own features go untested.

---

## 4 · Confidence and what would change my mind

- **Part a: 4 of 5.** I would change my mind if a laboratory document I may read said that a signature claim needs both attacks, or one named attack. Or if the referee held, unlike the gate verdict, that choosing between C and D is a threshold. Then my answer would become: "the rules do not settle this, and it is not a juror's to settle."
- **Part b: 3 of 5.** I hold firmly that option 2 is wrong (4 of 5 on that alone), because a definition about one column cannot be met by other columns' features. Between option 1 alone and my union of options 1 and 3, I am less sure. I would move to option 1 alone if the laboratory had a written principle that each column gets one test, or that the number of tests per column must be equal.

## Reversibility

- The definition applies to JQ-R04-CONTENT only (question file line 24). It is fully reversible until any exam card is used.
- Adding the own-set row costs one more feature set computed per column, with both attacks and their shuffles. I estimate that as small compared with the audit as it stands; not measured.
- After exam cards have been printed and sat, a definition that let a column be left out cannot be undone for that exam. That cost belongs to the other question's answer, not to this one.

---

## Files read

- `exam-prep/sixth-fix/juror-questions/JQ-R04-CARRIES.md`
- `RULES.md`, `TACTICS.md`, `TEAM.md`, `README.md`, all in full
- `decisions/2026-09-19-*/verdict.md`, all seven: zero-trade-contracts, tokenized-equity, calm-separation, large-moment-selection, effort-level, watcher-across-runs, card-order-requirement
- `decisions/2026-10-01-jq-r04-gate/verdict.md`
- `decisions/2026-10-01-jq-n1-canteen-8/verdict.md`

The one search I ran was a glob limited to `decisions/2026-09-19-*/verdict.md`. I opened nothing in `exam/`, nothing else in `exam-prep/`, and nothing else in `decisions/`.

## What I had to assume

- **The audit's mechanics are as the question describes them.** That covers families, features, attacks, the rule that unusable features are dropped, and that the column is printed as hourly ranks. I did not read the audit's code, and it was closed to me.
- **The definition was written before anyone saw the results it decides.** I do not know whether the audit has already been run on observation cards, or whether any per-family result shaped the options offered. If it has, RULES 6 is not breached by this definition, which is set before the exam-card measurement. But the referee should know I could not check this.
- **The case in which a set has no usable feature** is not covered by the question. I treated it under RULES 22.

## Steer

- I saw no steer in the coordinator's instruction: it does not restate the question and offers no preferred answer.
- In the question file, each option carries one ground of similar length. The section "What follows from the answers — not to steer" (lines 165–171) states consequences that hold whatever the answer.
- I note that the question is framed around the trade-count column and a downstream question about leaving it out (lines 15–20). That framing hints that someone expects this column to matter, but it contains no result, so I do not count it as a leak under RULES 3.
