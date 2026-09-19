RATIFIED

---

## 1 · Count

Three answers: juror-1.md, juror-2.md, juror-3.md. PASS.

---

## 2 · Independence

The question's source text is TACTICS.md section 4, line 80: "Cards are given in shuffled order: large moments and calm moments interleaved."

All three jurors identified the same two readings of the colon:

- **Reading A:** The second clause is a gloss on the first; shuffling *achieves* interleaving.
- **Reading B:** The second clause is an additional constraint independent of shuffling.

The convergence is correct because the text genuinely contains this structural ambiguity. Juror 1 calls it a colon that "carries the whole sentence"; Juror 2 calls it "two clauses joined by a colon, and it does not say whether the second is a gloss on the first or an extra constraint"; Juror 3 calls it "two ways" to read the colon and explores both. Each reached the same structure independently. There is no quoting, naming, or suspicious wording overlap. This is evidence of careful independent reading, not dependency.

PASS.

---

## 3 · Grounding

- **Juror 1:** Part 2 cites TACTICS.md (lines 80, 78–79, section 2 lines 36–43, section 3 line 52), `.claude/agents/watcher-high.md` (lines 44–46), RULES.md (rule 33, lines 118–121). All quoted.
- **Juror 2:** Part 2 cites TACTICS.md (line 80, lines 78–79, line 74, line 43), `.claude/agents/watcher-high.md` (lines 52–54, lines 19–21), RULES.md (rule 33, lines 120–121). All quoted.
- **Juror 3:** Part 2 cites TACTICS.md (section 4 line 80, lines 78–79, section 2 lines 42–43, section 3 lines 51–53), `.claude/agents/watcher-high.md` (lines 51–55), RULES.md (rule 33, lines 118–121). All cited with line numbers.

PASS.

---

## 4 · The outcome and its split in numbers

**The unsettled point (identical across all three jurors):**

Whether an order in which a fair, unconstrained shuffle happens to produce a long run of one kind (many large-movement cards in a row, then many calm-moment cards) must be rejected and re-drawn, or stands because the procedure was honest.

- Juror 1: "I record the split rather than resolve it...setting that number is outside a juror's scope (RULES 33)" (lines 51–54).
- Juror 2: "Section 4 does not choose between A and B...Supplying that number is not a juror's business (RULES 33)" (lines 52–56).
- Juror 3: "Saying which one wins would require fixing a number ('how long a stretch is too long'), and RULES 33 forbids a juror to set one. So: unsettled, and it is the next open question if anyone needs it settled" (lines 77–79).

**Identical reason:** RULES 33 forbids jurors from setting a threshold or number.

**The settled requirement (unanimous across all three):**

Section 4 requires:

1. The order is a **shuffle**: a permutation produced by a randomising procedure over the whole pool of the 10 coins' cards, not an order derived from card properties (not chronological by moment start, not grouped by coin, not by card ID, not by moment type).
2. The two kinds — large-movement and calm moments — must be **mixed through one sequence, not segregated**: both kinds must be present; they may not form separate blocks ("all large then all calm"); they may not be delivered as separate groups or streams.
3. No **positional rule** for kind: a watcher must not be able to read a card's kind from its position in the sequence (strict alternation large/calm/large/calm fails this).

An order can be checked against this:
- Inspect the sequence: are both kinds present? If one is absent, **fail**.
- Check whether the sequence matches any derived order (coin ID, timestamp, kind, chronology). If yes, **fail** (not shuffled).
- Look for segregation: do all cards of one kind precede all of the other, or fall into kind-blocks? If yes, **fail**.
- Check for positional rules: does the position predict the kind? (Does every even card, every third card, every other card, etc. match a pattern?) If yes, **fail**.

An order surviving these checks satisfies the requirement. The section itself settles this much and no more.

**Split: 3–0** on the settled requirement.

---

## 5 · Reasoned objection (RULES 32)

Each juror in Part 3 identified objections to its own answer and reasoned through them:

- **Juror 1** raised four objections (colon may negate one prong, one prong is not checkable, mixing may be pointless here, strictness may already be chosen) and replied to each. None blocked the answer.
- **Juror 2** raised three (blinding is weak, one test may over-read, over-declaring ambiguity). None blocked the answer.
- **Juror 3** raised three, including: "I am using the subordinate document to settle a reading of the superior one. That is legitimate as evidence of how the laboratory has understood its own rule, but it is not authority, and a referee would be right to mark it" (`watcher-high.md`, lines 181–186).

None of these constitute a reasoned blocker under RULES 32. Each juror weighed the objection and continued.

**Marked point:** Juror 3 explicitly invites marking its use of `.claude/agents/watcher-high.md` (a document that declares itself subordinate to `RULES.md` and `TACTICS.md`, lines 28–30) to interpret the meaning of `TACTICS.md` line 80. This is noted as evidence of laboratory interpretation but not authority. It does not block ratification.

---

## 6 · Scope

All three jurors explicitly held these questions outside their scope:

- Whether any built order meets this requirement (instruction forbade showing them one).
- Whether the shuffle's seed is recorded or reproducible.
- Whether all four watchers receive the same order or four independent orders.
- A run-length or balance threshold (RULES 33: "never a threshold or score").
- Any number.
- Any change to RULES.md.

All three cited RULES 33 when explaining why they did not set a threshold. No juror decided a trading rule, a threshold, a score, or a change to `RULES.md`.

PASS.

---

## Verdict

**RATIFIED.**

Section 4 of `TACTICS.md` requires that the order in which cards reach a watcher be **a shuffled permutation of all cards of the 10 observation coins, with large-movement and calm-moment cards mixed through one sequence rather than segregated, and with no positional rule that allows the watcher to read a card's kind from its position.** The section leaves open whether a shuffle output that happens to contain a long run of one kind must be re-drawn; that is a separate open question under RULES 33.

**Split: 3–0.**

The settled requirement is actionable and sufficient to check orders against section 4's text. The three jurors correctly identified and declined to resolve an unsettled boundary case within their proper scope.
