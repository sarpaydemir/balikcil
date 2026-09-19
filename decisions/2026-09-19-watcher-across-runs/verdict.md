RATIFIED

## Check 1: Count

Three answers present: Juror 1, Juror 2, Juror 3.

**Result:** PASS — count requirement met.

---

## Check 2: Independence

All three answers address the question independently, having seen no other juror's work.

**On the framing in the question:** Each juror independently identified the same sentence in the instruction: "Each run starts in a fresh context: a watcher in its second run remembers nothing of its first."

- Juror 1 (lines 165–170): "states the status quo of the mechanism... not a result, a prediction or a 'pay attention to X'."
- Juror 2 (lines 178–181): "states the mechanical status quo and does not say what may be *given*, so I do not read it as a steer."
- Juror 3: Implicitly rejects it through the same reasoning applied in the answer.

All three independently recognized and rejected the same potential bias without being silently influenced by it. This confirms independence rather than compromising it. None of the three allow this framing to move their answer.

**On overlaps in phrasing:** All three cite the same foundational documents (TEAM.md 168–169, RULES.md 3, `.claude/agents/watcher-high.md` 109–110). Natural overlap in references does not constitute dependence. Their framings differ: Juror 1 emphasizes bookkeeping including "batch file" and "write target"; Juror 2 distinguishes "administrative" material including "card numbers already given"; Juror 3 frames the constraint as "scope facts." None quote or name another juror. No suspicious identical phrasing exists that cannot be explained by independent reasoning about the same documents.

**Result:** PASS — independence holds. The framing did not move any juror.

---

## Check 3: Grounding

**Juror 1:** Lines 23–92 ground the answer across TEAM.md (lines 168–170), RULES.md rule 3 (lines 15–17), TACTICS.md section 4 (line 81), `.claude/agents/watcher-high.md` (lines 67–68, 109–110, 72), RULES.md rule 7 (line 37), TACTICS.md section 5 (lines 86, 89–90), TEAM.md line 54, and `data/card-order/order-manifest.md` line 65. All quoted.

**Juror 2:** Lines 16–97 ground the answer across TEAM.md ("Agent definitions" section, structural decisions), `.claude/agents/watcher-high.md` (lines 3, 109–110, 120–121), RULES.md 3, TACTICS.md sections 4 and 5, `watcher-high.md` "Four things you must know" item 4, TEAM.md Sofia section, and `order-manifest.md`. All cited with specific lines or sections.

**Juror 3:** Lines 20–134 ground the answer across RULES.md lines 15–17, `.claude/agents/watcher-high.md` lines 3, 72, 109–110, 114–116, 120–127, TEAM.md lines 47–48, 168–169, TACTICS.md lines 81, 86–87, `data/card-order/order-manifest.md` lines 96 and 73. All quoted.

**Result:** PASS — all three answers are fully grounded with file references and line numbers.

---

## Check 4: The Outcome and Split

**Juror 1's core answer:** "A watcher in a later run may be given only the run's bookkeeping — its field of view, its round number, which batch it is reading, the batch file, and a file to write into — and **may not be given its own earlier notes, nor any summary, count, carry-over or paraphrase of them.**"

**Juror 2's core answer:** "A watcher in a later run may be given only **administrative** material about its own earlier runs — which batch it is now reading, which card numbers it has already been given, its field of view, its round number, and the path of the file it now writes to — and **may not be given the substance of its own earlier work**: not its earlier notes, not its earlier report, not a summary, recollection or carry-forward of either."

**Juror 3's core answer:** "A watcher's later run may be given only the scope facts every instruction already carries — its field of view, its round number, the cards of that batch and the file to write its notes to — and **nothing of the substance of its own earlier runs**: not its earlier notes, not a summary or digest of them, not a carried-over conclusion, hypothesis or 'keep watching X' line."

**Agreement:**
- YES to: bookkeeping/administrative/scope information (field of view, round number, batch information, write target)
- NO to: the substance of earlier work (no earlier notes, no summaries, no carry-overs, no conclusions, no prior opinions)

All three answers agree on the fundamental distinction and the direction. The nuances differ slightly (what exactly counts as bookkeeping), but the core outcome is identical across all three jurors.

**Result:** PASS — 3–0 unanimous agreement on the answer.

---

## Check 5: The Reasoned Objection (RULES 32)

**Juror 1** identifies four counter-arguments (lines 94–126): expressio unius reading of the round rule; narrower scoping of RULES 3 to old-project results only; the assumption of one watcher reading everything; and the cost of amnesia to cross-batch structure. Juror 1 examines each and concludes: "Against all four, the decisive fact remains that `TEAM.md` states the harm by name — 'A watcher accumulating opinions between runs would break the blind exam'..." Juror 1 ranks these objections as less decisive than the main ground and maintains confidence 4/5. No blocker is claimed.

**Juror 2** lays out "The honest case against" (lines 99–129): that the answer rests on one sentence about a configuration key, not an explicit document statement; that the blind exam argument may not reach a watcher who does not sit it; that the word "other" in the round rule implies one's own notes might not be barred; and the hazard of watcher self-recall restoring anchoring bias. Juror 2 does not adopt any of these as a reasoning that blocks the answer. Confidence remains 4/5.

**Juror 3** presents "The honest case for 'the documents do not settle this'" (lines 136–174): that TEAM.md 168 might describe configuration, not instruction content; that a watcher's own note is not from the old project and RULES 3 targets the old project; that the round rule bars only "other watchers' notes" by name, leaving one's own silent; and that reading RULES 3 broadly stretches a wall built against one thing to hold back another. Juror 3 then states (lines 166–174): "If that case is right, the correct answer is not mine but 'the documents do not settle it, and the jury should say so.' I weighed it seriously. I do not adopt it, for two reasons..." and explains why the flat reading of RULES 3 and the expressio unius problem with allowing everything else wins over the narrower reading. Confidence remains 4/5.

None of the three jurors raised a reasoned objection that they stand behind and cannot overcome. Each considered the strongest counter-arguments, weighed them against the main grounds, and determined they are outweighed or subordinate. None declared a blocker.

**Result:** PASS — no reasoned objection stands under RULES 32.

---

## Check 6: Scope

RULES 33 confines a juror to "procedure and definition only: never a trading rule, never a threshold or score, and never a change to a rule in this file" (RULES.md).

**Juror 1:** Addresses what can be "given" to a watcher — a procedural and definitional question. States a consequence: "each run must write to its own file" as a logical necessity to keep the main rules intact (lines 69–71). This is framed as a consequence that follows from the rules, not as a new rule or threshold. Within scope.

**Juror 2:** Addresses what can be given — procedural. Acknowledges not resolving the file-naming mechanics and notes that "a separate file per run avoids the question entirely and costs nothing" (lines 145–147). Explicitly does not settle the file question. Within scope.

**Juror 3:** Addresses what can be given — procedural. Explicitly states at lines 121–124: "**Not resolved by the documents, and not mine to settle:** the file-naming and collation mechanics themselves — one file per batch versus per watcher, and who concatenates them for the canteen. That is coordinator bookkeeping, not procedure the documents fix." Explicitly stays within scope.

None of the three jurors set a threshold, score, or trading rule, or changed a rule in RULES.md.

**Result:** PASS — all three stay within scope.

---

## On the Consequence About File Location Across Runs

The instruction asks: "Each juror states something that follows from its answer about **where a watcher's notes are written across runs**. Say whether that consequence is inside the answer they were ratified on or outside it, because the coordinator will act on the difference."

**Juror 1:** States (lines 66–71, part of ground (d) and the Answer section): "each run must write to its own file. Which naming scheme is used is an engineering detail; that the runs must not share one file is the part that follows from the rules above."

This is INSIDE the answer and its grounding. Juror 1 presents it as a necessary consequence of keeping the main rules intact (the prohibition on reading earlier notes). The coordinator should treat this as part of what the ratified answer requires.

**Juror 2:** States (lines 145–147, in the Confidence section): "I did not resolve that; a separate file per run avoids the question entirely and costs nothing."

This is OUTSIDE the answer. Juror 2 explicitly says they did not resolve the file-naming question and do not claim to settle it. The statement is prudential (avoids the question) rather than procedural (what the rules require). The coordinator should treat this as explicitly unresolved by Juror 2.

**Juror 3:** States (lines 116–120 and 121–124): "The clean form is one notes file per run, named in that run's instruction as line 72 provides. **Not resolved by the documents, and not mine to settle:** the file-naming and collation mechanics themselves..."

This is PARTIALLY INSIDE and PARTIALLY OUTSIDE the answer. Juror 3 includes as a consequence of the main rules that "the notes file must not be a back door" and therefore the clean form is one notes file per run (INSIDE the answer). But Juror 3 explicitly excludes as outside their scope the actual file-naming mechanics and which agent controls them (OUTSIDE the answer). The coordinator should treat the one-file-per-run requirement as part of the ratified answer, and the naming mechanics as unresolved.

---

## Summary

All six checks pass. The outcome is 3–0 agreement on a clear and substantive procedural answer, grounded in the laboratory's written documents. No juror stepped outside scope. No reasoned objection stands. Independence holds; the framing in the question did not move any juror toward or away from their answer.

**Split: 3–0**

**Outcome:** A watcher in a later run may be given only its administrative bookkeeping (field of view, round number, batch assignment, write target) and may not be given the substance of its own earlier runs (no earlier notes, no summary or carry-over of notes, no prior conclusions or opinions). This follows from TEAM.md's statement that "a watcher accumulating opinions between runs would break the blind exam," from RULES.md rule 3's bar on instructions carrying results, and from the principle that only files named in the instruction may be read or written.

**Consequence on file location:** Juror 1 requires one notes file per run (INSIDE its answer). Juror 2 does not resolve the file question (OUTSIDE its answer). Juror 3 requires one notes file per run but leaves the naming mechanics unresolved (INSIDE for structure, OUTSIDE for implementation). The coordinator should treat the one-file-per-run requirement as a ratified consequence that follows from the main answer.

