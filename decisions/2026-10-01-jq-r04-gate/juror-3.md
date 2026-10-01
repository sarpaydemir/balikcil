# JQ-R04-GATE · juror 3

Juror, `opus`, effort high. Written 2026-10-01. I have not seen and did not look for the other jurors' answers.

## 1 · Answer

**C:** the gate fails if **either** attack (nearest neighbour or pair AUC) beats its own RULES 12 chance line on the exam cards. The cards pass only if **neither** does.

On the optional second part: the rules do not forbid the nearest-neighbour attack from matching cards that share clock hours. RULES 13 governs how events are counted when scoring. It does not govern what a candidate can link. My answer to the main question does not depend on this part.

I set no threshold. The chance line stays exactly as RULES 12 fixes it (1,000 shuffles, best 1%), applied to each attack separately. I do not change any rule.

## 2 · What it rests on

**(a) What the gate protects is a requirement, and a requirement fails if any valid test shows it broken.**
- `RULES.md` line 41 (RULES 9): "In the exam the coin name and the date are hidden."
- `TACTICS.md` lines 101–102 (§6): "**What is hidden:** - the coin name".

The rules state this as a fact the exam must satisfy, not as a tendency to be weighed. Each attack is a separate, legitimate measurement of whether the hiding holds. The question file (lines 82–87) describes them as asking different things: nearest neighbour asks "*can a card be matched to its own coin?*", and pair AUC asks "*does similarity carry coin information on average?*" A card set can fail one of these and not the other. Option D would pass a set on which a card *can* be matched to its own coin at a rate beyond chance, as long as the average-similarity test did not also fire. That outcome is incompatible with "the coin name is hidden". The same holds the other way round for B, and A has the same gap. Only C refuses to certify cards as hidden while one of the laboratory's own measurements, at its own RULES 12 line, says they are not.

**(b) Each attack already has its own RULES 12 line, so C applies RULES 12 as written and does not invent a combined line.**
- `RULES.md` lines 51–52 (RULES 12): "The chance line is not invented. The answers are shuffled 1,000 times, and the real result must fall inside the best 1%."
- Question file lines 80–81: "The audit attacks `ALL-removable` in **two** ways, each against its own RULES 12 chance line".

Under C, every result that falls inside the best 1% of its own shuffles counts as having beaten chance, which is exactly what RULES 12 says. D adds a second condition (the *other* result must also beat its line) that no rule contains. "Both" is a joint criterion, and its false-alarm behaviour is no longer the RULES 12 1%. That makes D the reading that changes the chance line, not C. (A and B each drop a measurement the laboratory already makes and prints.)

The wording of the step fits C on its plain terms. "If `ALL-removable` beats its chance line … the gate has failed" (question file lines 56–57). When `ALL-removable` is set against two lines, each of them "its own", it beats its chance line as soon as it beats either one.

**(c) The gate is a lower bound by construction, so its two readings should not be weakened further.**
Question file lines 69–75: `ALL-removable` "is **not** 'everything about a card that could identify its coin' … Nothing guarantees that no other channel exists outside the list." A pass can only ever mean "no leak was found in what was looked at". Requiring two attacks to agree before a leak counts lowers the floor of a measurement that is already only a floor.

**(d) Reversibility. C is the reversible reading. A, B and D carry an irreversible risk.**
- `RULES.md` lines 41–42: "The answer key is sealed before the exam: its fingerprint is written into `LEDGER.md`."
- `RULES.md` lines 34–36 (RULES 6): "A rule is not changed after looking at a result. If it is changed it counts as a new rule, carries the 'afterwards' label, and is tested again."
- `TACTICS.md` line 22: "**Draw number:** `20260913`. Written before the draw; it does not change." `TACTICS.md` line 24: "**Exam:** a different 20 coins".

If C wrongly fails a blind card set, the cost is re-blinding and re-auditing before the key is sealed. Nothing is spent and the exam coins stay unused, so that error is reversible. If A, B or D wrongly passes a leaky set, the key is sealed and the exam is sat on cards whose coins can be identified. The exam coins are a one-time draw that does not change, and RULES 6 forbids changing the procedure after seeing the result. That error cannot be undone. I do not have a measured figure for the rework under C. As an **estimate**, it is one further blinding-and-audit cycle per failure, of the kind this laboratory has already run several times.

**(e) RULES 6 timing.**
`RULES.md` line 34: "The rule is written first, the result is opened second." No exam card has been measured (question file line 123). On today's observation material all four options give the same result (lines 142–145). Fixing C now satisfies RULES 6.

**Earlier verdicts.** I read all seven `decisions/2026-09-19-*/verdict.md` files: zero-trade-contracts, tokenized-equity, calm-separation, large-moment-selection, effort-level, watcher-across-runs and card-order-requirement. **None of them settles any part of this question.** None deals with the blindness audit, with combining two tests, or with the exam-card gate.

**Optional second part, and its ground.** RULES 13 (`RULES.md` lines 53–54: "Moments occurring in several coins in the same hour count as a single event. If the whole market moved together, that is one event.") is restated in `TACTICS.md` line 127, under **§7 Scoring**: "A moment appearing in several cards in the same hour counts as a single event." In both places it is a rule about how results are counted, so that one market move is not scored as many. It says nothing about whether two cards that print the same hours can be linked to each other. If two exam cards of one coin print overlapping hours, a candidate could link them through that overlap, so the overlap is itself a channel the blinding has to answer for. Forbidding the attack from seeing it would hide a real leak. The rules therefore do not support forbidding it. Whether the audit also prints the restricted version as a diagnostic is engineering, not mine to decide. I do not rely on the measured restricted figure in the question file. My answer is the same either way.

## 3 · The strongest case against my answer

1. **Multiplicity.** Under C, two tests each at the 1% line give a card set that really is blind up to roughly a 2% chance of failing (an **estimate** from the union bound, not measured). That is about double the "best 1%" in RULES 12, so one could say C quietly loosens RULES 12 against the cards, which is a threshold change a juror may not make. My reply is that RULES 12 defines when a *result* beats chance, and C applies it to each result unchanged. No rule sets an error rate for an acceptance gate. Still, this is a real argument. A referee could reasonably hold that any choice among A–D sets the gate's effective error rate and so comes close to a threshold.

2. **The same run's own precedent may point to D.** The question file (lines 100–102) says the first run's "Level 1" standard "required a family to fail **both** attacks". If that means "a family counts as leaking only when both attacks beat chance", then the author of the step used D for single families, and reading the pooled gate the same way is the more consistent reading of one document by one author. I cannot open that document. The sentence is ambiguous to me: a family that "fails" an attack could mean it was caught or that it escaped. If it means "a family is cleared only when it escapes both", it supports C. I do not rest on it either way. Its strongest form is a genuine case for D.

3. **Nearest neighbour is the more fragile statistic.** It is sensitive to near-copy cards with overlapping hours and, where exact ties exist, to card numbering (question file lines 89–96). Under C it can fail the gate on its own. Someone could argue the gate should not be decided by its least robust input, and that D (or A, the averaged statistic) is the sounder rule. My reply: both fragilities are measured and disclosed. Overlapping hours are a real channel (see the optional part above), and the numbering dependence vanishes where there are no ties. Fragility argues for printing the robust version as well, not for letting a leak pass.

4. **C may make the gate effectively unpassable.** The feature list grows as channels are found (lines 69–75), and every added test is another way to fail. A strict gate that can never be passed stalls the exam indefinitely. That is a real cost, but it is a cost of the blinding, not of the reading. The rules give no basis for passing cards whose coin identity is measurably recoverable.

## 4 · Confidence

**4 / 5** that C is the reading the laboratory's documents best support. No line in `RULES.md` or `TACTICS.md` literally says "either test", so the answer rests on the purpose of RULES 9, on RULES 12 applied per measurement, on the plain wording "its own chance line", and on the reversibility asymmetry. It does not rest on an explicit sentence.

**What would change my mind:**
- If `exam-prep/R-04-blindness.md` §8 (which I did not open) defines "its chance line" in that step as one named statistic. Then the step, written before the result, already chose, and RULES 6 would favour honouring it.
- If the "Level 1" rule clearly means "a family counts as leaking only when both attacks beat chance" **and** the gate is shown to have been written as an extension of Level 1. That would move me toward D.
- If a written rule were found that sets the error rate an acceptance gate must hold. Then C's roughly 2% (estimate) false-fail rate might conflict with it.

**Should a rule change?** No change. Nothing in `RULES.md` needs amending for this answer, and a rule changes only after the user is asked.

---

## Files I read
- `exam-prep/third-fix/juror-questions/JQ-R04-GATE.md` (whole)
- `RULES.md`, `TACTICS.md`, `TEAM.md`, `README.md` (whole)
- `decisions/2026-09-19-{zero-trade-contracts,tokenized-equity,calm-separation,large-moment-selection,effort-level,watcher-across-runs,card-order-requirement}/verdict.md`. I found these with one glob limited to `decisions/2026-09-19-*/verdict.md` and opened nothing else under `decisions/`.

I did not open `exam/`, any other file under `exam-prep/`, or any other file in `decisions/2026-10-01-jq-r04-gate/`.

## Assumptions the instruction did not cover
- **Which nearest-neighbour version applies if the two ever differ.** The numbering-dependent and tie-averaged versions coincide where there are no exact ties (question file lines 93–96, 138–140). If they differ on some exam-card set, my answer does not say which one is "the" nearest-neighbour score. I list this as unresolved (RULES 22). It may need its own open question.
- **What "fail both attacks" means in the Level 1 sentence.** I could not resolve it without opening a closed file, so I did not rely on it.
- **What an exam candidate can see at once.** I assumed the attacks are legitimate stand-ins for what a candidate could do with the cards (`TACTICS.md` line 110: "all get the same 400 cards"). Whether the gate measures the right thing is engineering and outside this question.

## Steers seen
- **Results in the question.** The question contains measured numbers from the observation cards (lines 128–150). RULES 3 forbids results in instructions. They are disclosed as being the same under all four options, so in my judgement they do not favour any option. I report them anyway.
- **Framing that may lean toward a stricter reading.** The corrected description stresses that `ALL-removable` is "not complete by construction" and that "Nothing guarantees that no other channel exists outside the list". That is factual, and I used it in ground (c). It does favour a strict reading, and a referee should know I relied on wording the question chose to emphasise.
- **Framing that may lean toward D.** The "Level 1 … required … both" sentence (lines 100–102) points at one option by naming a precedent for it. I treated it as an argument against my answer, not as ground.
- **The coordinator's instruction.** I saw no steer in it.
