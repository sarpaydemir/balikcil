# Calibration of the outside typed-choice endpoint

Run by `data-engineer` (Mateo), Mode A, 2026-09-19 23:05-23:30 UTC.
Every number below was measured by a script in `scripts/` and can be recomputed from
the artefacts in this folder. Where a number is an estimate it says so.

This report **measures an instrument**. It sets no threshold, proposes no rule, and
makes no trading judgement.

---

## 1 - The endpoint's contract, established here and not taken on trust

`scripts/19_endpoint_probe.py` sent 37 named probes; the full record, request by
request, is `probes/probe-results.json`. 21 returned HTTP 200, 14 returned HTTP 400,
2 returned HTTP 401. Nothing failed at transport level.

### 1.1 What the memo gets right

- `POST https://openrouter.ai/api/alpha/decisions`, bearer auth, the request shape in
  its section 3, and the three question types `choice`, `score`, `noul` - all confirmed.
  A fourth type is rejected with `Invalid discriminator value. Expected 'noul' |
  'choice' | 'score'` (probe 13).
- Price: **measured** at exactly $0.042 per million input tokens, output billed at
  zero. Over the 300-call item run, `input_tokens x 0.042e-6` reproduced the summed
  `cost` field to the last digit ($0.00667027).
- A chat-completions body is rejected (probe 27), as the memo says.
- `temperature` is accepted and silently ignored - no error, and the answer was
  unchanged (probe 26).
- The 32,000-token context is real. A 140,000-character state was accepted at 29,511
  input tokens (probe 35); a 200,000-character state was rejected with
  `HTTP 400: {"detail":{"error_type":"max_tokens_exceeded"}}` (probe 23).

### 1.2 What the memo gets wrong or leaves out

1. **The response carries two fields the memo's sample omits: `id` and `provider`.**
   Every 200 response has `id` of the form `gen-dec-<unix seconds>-<random>` and
   `provider: "TypeSafe"`. The embedded unix time is used in section 2 below as an
   outside time anchor.
2. **A `score` answer has a different shape from a `choice` answer, and the memo does
   not describe it.** It returns
   `{"type":"score","score":<float>,"legend":{<index>:<criterion>},"probabilities":{<index>:p},"confidence":<float>}`.
   There is no `choice` field.
3. **The returned `score` is on a 0-based index scale, not on the scale you wrote in
   your criteria.** A five-element criteria array returns a score in [0, 4]; a
   three-element array returns [0, 2]; a one-element array returns exactly 0. Anyone
   reading a five-point rating straight out of `score` is off by one. Tested identity:
   `score == sum(index x probability(index))` over all 100 score calls, maximum absolute
   gap 0.03, which the 2-decimal rounding of the returned probabilities accounts for.
4. **`noul` is not described at all, and it is not a free-text type.** It returns
   `{"type":"noul","noul":<float 0..1>}` - a bare number, with **no `confidence` and no
   `probabilities`**. Its `criteria`, if given, must be a record keyed `"true"` and
   `"false"` (probe 09's validation error names the path `criteria.true`); a record
   with any other keys is a 400. Probe 28 asked a true/false question with those keys
   and got `0.98`.
5. **The memo says "all three require `instructions`". True, but incomplete:**
   `choice` also requires `criteria` as a **record** (400 otherwise, probe 12), and
   `score` requires `criteria` as an **array** - a record is a 400 (probe 07) and
   omitting it is a 400 (probe 06).
6. **`state` is not restricted to a string.** The validation error at probe 16 names a
   union of string, record and array, and a record (probe 31) and an array (probe 32)
   were both accepted and answered.
7. **An empty `state` is not an error.** Probe 17 sent `""` and got `OTHER` back at
   confidence 0.99. There is no "I cannot answer" path: garbage in returns a confident
   answer out.
8. **A truncated JSON body is parsed leniently rather than refused.** Probe 20 sent
   `{"model":..., "state":"x", "questions": {` and got the semantic error
   `At least one question is required`, not a parse error. A body cut off in flight
   will not reliably present as malformed.
9. **Auth failures are shape-dependent.** A token not matching the provider's key
   pattern returns `401 Missing Authentication header` (probe 21) - i.e. it is treated
   as absent; no header at all returns `401 No cookie auth credentials found`
   (probe 22). A wrong-but-well-formed key returned `401 User not found.` in an earlier
   pass of this probe set.
10. **Validation errors echo the account id** in a `user_id` field. Not the API key,
    but an account identifier; it is redacted from every artefact here (see section 7).
11. **`confidence` is a deterministic function of the probabilities, at least for
    two-option questions.** Over the 100 `CARDCOUNT` calls, `confidence == top
    probability - second probability` held in 100 of 100 cases (max gap 0.01, the
    rounding). It is therefore not an extra signal on top of the distribution; it is a
    re-statement of it. For questions with more than two options no identity I tested
    reproduced it, and the definition is unpublished.
12. Unknown top-level keys are ignored, not rejected (probe 33). Question labels and
    option keys may contain spaces, punctuation and non-ASCII characters and come back
    unchanged (probes 36, 37).

---

## 2 - The answer key, and the evidence that it came first

MEMO section 4 step 2: *"Label them by hand, and write the labels down before you look
at what the model says. Order matters: labelling after seeing its answers is not a
test."*

### 2.1 Where the 100 items came from

`scripts/20_build_key.py`, seed `20260919` (written in the script, used nowhere else).

- **Source:** the 36 round-1 files `notes/2026-09-19-{amara,ingrid,kenji,lukas}-v2-batch{01..09}.md`.
- **Excluded, with reason, each reason counted:** the four `*-round2.md` files and the
  two `canteen/` files, because their text names the watchers directly and would hand
  the model the FIELD label — Amara's round-2 file names Ingrid 33 times, Kenji 36 and
  Lukas 34; `canteen/2026-09-19-viktor.md` names the four watchers 330 times between
  them and `canteen/2026-09-19-sofia.md` 273 times. Also excluded:
  `notes/superseded-v1-order/`, which its own README sets aside. The 36 round-1 v2 files
  that were used name only their own author, and that only in the header line, which the
  selection rule drops.
- **Line selection rule** (in the script's `qualifies()` docstring and copied into
  `KEY-MANIFEST.json`): a line qualifies if it is not a heading, cites at least one
  `C###` card number, is in the TACTICS section 4 note format (3 or more dot-separated
  fields, last field a single digit 1-5), and contains no laboratory member's name.
- **Pool sizes measured:** ingrid 261, kenji 357, amara 482, lukas 587 qualifying lines.
- **Draw:** 25 per author by `random.Random(20260919).sample`, then interleaved with
  `random.Random(20260920).shuffle` before ids were assigned, so neither the row order
  nor the id order of `items.jsonl` groups items by author.

Anyone who distrusts this can re-run the script and check the two digests.

### 2.2 The labels are read off the source, not judged

No item was labelled by opinion. Each label is a fact about where the line came from
or what characters are in it:

| label | what it is | menu it was tested with |
|---|---|---|
| `field_key` | the watcher file the line sits in | `FIELD`, four options, descriptions quoted verbatim from `TEAM.md` |
| `multi_key` | whether more than one distinct `C###` appears on the line | `CARDCOUNT`, two options |
| `confidence_key` | the 1-5 digit the watcher wrote as the last field | `CERTAINTY`, `score`, five-point array |

For `CERTAINTY` the digit is **stripped from the text that is sent**
(`text_no_confidence`), so the answer is not in the input.

Key distribution: FIELD 25/25/25/25 by construction; CARDCOUNT 52 SINGLE / 48 MULTI;
CERTAINTY 1x"1", 4x"2", 19x"3", 51x"4", 25x"5".

### 2.3 Four mechanisms, so the ordering is visible rather than promised

1. **The files are split.** `items.jsonl` holds `id`, `text_full`,
   `text_no_confidence` and nothing else - no author, no source file, no label.
   `key.jsonl` holds the labels and the provenance and no text. The runner refuses to
   start if `items.jsonl` carries any field outside that whitelist.
2. **The runner never opens the key.** `scripts/21_run_endpoint.py` reads
   `items.jsonl`; it reads `key.jsonl` only as bytes, to hash them, and stops if the
   digest differs from the one in `KEY-MANIFEST.json`.
3. **An outside time anchor.** Before the first item call, the build script posted the
   key's SHA-256 digest - and nothing else - to the endpoint, and stored the response.
   The endpoint's own `id` embeds its unix clock. Notarisation at provider time
   **1789859632** (2026-09-19 23:13:52 UTC); **earliest of the 300 item calls at
   1789859698**, 66 seconds later. This is an outside party's clock, not a trusted
   timestamping authority, and I say so rather than overselling it.
4. **The comparison script checks 1-3 before it computes anything** and exits if either
   the digest or the ordering fails. It passed:
   `key_digest_matches_notarised: true`, `every_call_after_notarisation: true`,
   `calls_with_no_provider_time: 0`.

`scripts/22_compare.py` is the first script in the chain that reads a label.

---

## 3 - What MEMO section 4 asks to be reported

300 calls, 100 items x 3 question sets, one question per call. **Zero failures.**

### 3.1 FIELD - four-option routing, key = which watcher wrote it

- **Agreement with key: 73 / 100.** Baseline of a uniform guess over four balanced
  classes: 25%.
- Confusion matrix (rows = key, columns = model):

| key \ model | EXCH | CROWD | OUTSIDE | PRICE |
|---|---|---|---|---|
| EXCHANGE_BEHAVIOUR | **11** | 5 | 2 | 7 |
| CROWD | 1 | **23** | 1 | 0 |
| OUTSIDE_WORLD | 0 | 0 | **17** | 8 |
| PRICE_ITSELF | 0 | 0 | 3 | **22** |

  The errors are not spread evenly: 14 of the 27 come from one class, and
  `EXCHANGE_BEHAVIOUR` recall is 11/25 = 44%. Nothing is ever mis-routed *into*
  `EXCHANGE_BEHAVIOUR` from `OUTSIDE_WORLD` or `PRICE_ITSELF`.
- **The confidence of every item it got wrong**, ascending (full list, MEMO section 4
  step 4):

  0.20, 0.27, 0.31, 0.39, 0.40, 0.50, 0.51, 0.57, 0.60, 0.61, 0.61, 0.68, 0.72, 0.72,
  0.74, 0.76, 0.77, 0.78, 0.79, 0.79, 0.85, 0.88, 0.89, **0.93, 0.96, 0.99, 1.00**

  Per-item, with the probability it gave the correct option, in
  `ANALYSIS.json -> question_sets.FIELD.confidence_of_every_wrong_item`.
- Confidence when right: min 0.32, median 0.98, mean 0.875. When wrong: min 0.20,
  median 0.72, mean 0.675. The two distributions overlap across their whole range.
- **The number MEMO section 5 records as unknown - correct answers that were also
  low-confidence - measured here:** 24 of the 73 correct answers came in below 0.90,
  15 below 0.70, 4 below 0.50.
- Escalation curve (no threshold is being chosen here; this is the distribution):

| accept at >= | accepted | accuracy on accepted | errors accepted | escalated |
|---|---|---|---|---|
| 0.50 | 91 | 0.758 | 22 | 9 |
| 0.70 | 73 | 0.795 | 15 | 27 |
| 0.80 | 62 | 0.887 | 7 | 38 |
| 0.90 | 53 | 0.925 | **4** | 47 |
| 0.95 | 50 | 0.940 | **3** | 50 |
| 0.99 | 37 | 0.946 | **2** | 63 |
| 1.00 | 30 | 0.967 | **1** | 70 |

### 3.2 CARDCOUNT - two-option mechanical property, key is certain

- **Agreement with key: 100 / 100.** Majority-class baseline 52%. No errors, so there
  is no error-confidence distribution to report.
- 42 of the 100 correct answers came in below confidence 1.00, 9 below 0.90, 2 below
  0.50. At an accept-above-0.90 rule this task would escalate 9 items, all of which
  were already right - pure cost, zero errors caught.

### 3.3 CERTAINTY - `score` type, key = the watcher's own 1-5 digit

- **Exact agreement: 37 / 100** using the modal index; 35 / 100 using the rounded
  `score`. **A constant answer of "4" scores 51 / 100.** Within plus or minus 1: 87%
  for the model, **95% for the constant "4"**. Mean absolute error 0.78.
- Confidence on this question set is low and does not separate right from wrong: mean
  0.376 when right, 0.350 when wrong; medians 0.39 and 0.34. At every threshold on the
  grid the accuracy of the accepted part stays at or below 0.44, except a single item
  above 0.95.
- Read plainly: on this task the endpoint is **worse than a constant**, and its
  confidence gives no usable handle for escalation.

### 3.4 Cost, measured

| component | calls | cost |
|---|---|---|
| probe run 1 (discarded) | 27 | $0.00016817 |
| probe run 2 (discarded) | 37 | $0.00241290 |
| probe run 3 (kept) | 37 | $0.00241290 |
| key notarisation (kept) | 1 | $0.00001583 |
| item run | 300 | $0.00667027 |
| **measured total** | **402** | **$0.01168007** |

Plus one notarisation call from a discarded first key build whose record no longer
exists: **estimate $0.0000158** (the same request shape as the kept one), giving
**$0.0116959 estimated grand total**. Both discarded probe runs are recoverable from
git objects `4604cb5` and `7080238`, which is how their cost was measured rather than
guessed.

Per calibrated item, all three questions: **$0.0000667**. Input tokens on the item run:
158,816 total, median 517 per call. Output tokens: 11,748, billed at zero.

### 3.5 Latency, wall clock

- 300 item calls, sequential: **median 0.340 s**, p90 0.438 s, **worst 0.610 s**,
  best 0.274 s, mean 0.354 s. Whole run 107.1 s for 300 calls = 0.357 s per call
  including my own overhead.
- No difference between question types worth naming: medians 0.339 (FIELD), 0.337
  (CERTAINTY), 0.342 (CARDCOUNT).
- Over all 338 kept calls including probes: median 0.338 s, p90 0.440 s, max 0.610 s.
  Rejected requests come back far faster (validation 400s about 0.05-0.07 s).
- This is consistent with the memo's 0.321 s median over 178 calls.

### 3.6 Failures

**Zero failures in the 300-call item run** - 300/300 HTTP 200, no retries, no transport
errors. The failures that did occur were all deliberate probes; each is listed in
section 1.2 with its exact error text and the request that caused it, and every one is
in `probes/probe-results.json` with its full request body.

One non-endpoint failure is recorded in section 7.

---

## 4 - The threshold - MEMO section 5 applied to these numbers

MEMO section 5 says its own threshold is **not established**, that in its run every
error came with low confidence and an "accept above 0.9, escalate below" rule would have
caught all of them, that this rests on **two** errors, and that it is a hypothesis to be
tested on your own data and not built on.

**Tested here, it does not hold.**

- On FIELD, an accept-above-0.90 rule lets **4 errors through** out of 27, including one
  at confidence **0.99** and one at confidence **1.00** where the model put probability
  **0** on the correct option. High confidence is not a guarantee of correctness on this
  task.
- The cost the memo lists as unmeasured is real: that same rule escalates **47 of 100**
  items, and 24 of those 47 were already correct.
- On CARDCOUNT the rule costs 9 needless escalations and catches nothing, because there
  is nothing to catch.
- On CERTAINTY the rule is inapplicable: only 4 items reach 0.90 at all and 3 of those 4
  are wrong.

So confidence is **informative but not sufficient** on the one task here that resembles
a judgement: mean confidence is higher when right (0.875) than when wrong (0.675), and
accuracy on the accepted part does rise monotonically with the threshold - but the
distributions overlap end to end, and errors survive at the top of the range.

**I am not setting an operating threshold for this laboratory, and I say why rather than
just declining.** Picking one is a choice that changes the numbers and that the written
rules do not settle: it trades an error rate against an escalation rate, and the written
rules contain no target for either. That is the definition of an **open question** under
RULES 33 ("a choice that changes the numbers"), it is explicitly not an engineering
call, and RULES 33 reserves it for at least three jurors in separate contexts plus a
referee. It is also the kind of number RULES 33 forbids a juror to set -
"never a threshold or score" - so on my reading a jury could rule on *whether and where*
such a component may be used, but the threshold itself would have to go to the user, as
the preamble to `RULES.md` requires for anything that changes a rule. I flag that as a
second open question rather than answering it.

---

## 5 - Where such a component could and could not be used here

Grounded in what each role is *required to produce*.

### It cannot be used for

- **The four watchers (Ingrid, Kenji, Amara, Lukas).** TACTICS section 4 fixes their
  output as `card no - what I saw - why I think so - how sure I am (1-5)`, and RULES 34
  applies the same discipline elsewhere: "A note without a card number does not count."
  The endpoint returns a label and a number and, by the memo's section 5 and by every
  response recorded here, **never a why**. It structurally cannot produce the "why I
  think so" field.
- **Sofia (canteen chair).** TEAM.md: she writes the surviving ideas as a mechanical rule
  and a score recipe, and "Cannot: invent an idea. Every rule rests on at least one
  watcher note and a card number." Choosing what the menu should even be is the work
  itself; the memo's own section 5 says that part does not get cheaper, and my FIELD
  numbers show why - the two worst-confused classes are confused because `TEAM.md` itself
  gives "the funding rate itself" to Kenji and funding *changes* to Ingrid, so the menu I
  quoted from it overlaps. A typed choice cannot notice that its menu is wrong.
- **Viktor (skeptic).** RULES 32: "An objection is made with reasoning. An unreasoned
  'no' does not count." A red stamp with no reasoning is void by rule.
- **Hana and Tomas (exam candidates).** RULES 10: "An agent sitting the exam cannot use
  tools and cannot read files. A paper where tool use is observed is void." A network
  call is tool use. TEAM.md also requires Hana and Tomas to share one definition so the
  comparison is fair; changing one of them breaks that.
- **Greta (judge).** TEAM.md: "Greta is a script, not an AI. A judge has no opinions."
  RULES 29 requires the same input to give the same number and the same result. The
  endpoint's run-to-run determinism on real items is **unmeasured** here (two repeated
  probe calls agreed; the 100 items were never re-run), and RULES 31 requires a score
  ledger with raising signals, blockers and unknowns - three prose lines the endpoint
  cannot emit.
- **Jurors and the referee.** RULES 34 requires every answer to cite a file and a line,
  quoted, and TEAM.md requires a juror to write the strongest case against itself;
  RULES 35 requires the referee to say why it refuses. All three are prose obligations.
- **Derya (reporter).** Her output is Turkish prose for the user.

### It could be used for

- **My own work (data engineering), as a second opinion on a mechanical extraction that
  a script already owns.** The `CARDCOUNT` result - 100/100 on a property with a certain
  key, at $0.0000206 per item and 0.34 s - is the shape of a usable case: a regex stays
  the source of truth, the endpoint runs beside it, and **every disagreement is
  escalated**, never resolved by the endpoint. That is the only use my numbers support,
  and it is worth stating what it is worth: for anything a regex can already express,
  the regex is free, offline, certain and reproducible under RULES 29, and the endpoint
  adds only an independent second pair of eyes on the regex's blind spots. That is what
  the memo's section 7 describes its own successful test as.
- **Nothing that touches an exam card**, at any price: `exam/` is sealed and the bounds
  on this run keep it closed.

### The honest shape of the negative result

The one task here that needed reading rather than counting (FIELD) came in at 73%, with
errors at confidence 1.00. The one that needed a judgement of degree (CERTAINTY) lost to
a constant. The one that was mechanical was perfect and did not need a model. Across the
three, **the endpoint was reliable exactly where a script would have been reliable
anyway.**

### The limit in `external/SOURCES.md`, stated rather than routed around

`external/SOURCES.md`: "**Nothing in this folder may be carried into a watcher,
canteen-chair or skeptic instruction** ... The limit binds on ideas, not only on
quotations."

This report is written into `external/calibration/`, inside that folder, so by the
letter of that sentence **its measurements cannot be carried into an instruction for
Ingrid, Kenji, Amara, Lukas, Sofia or Viktor either** - not even the operational ones,
and not by paraphrase. I did not find that this blocks a use I would otherwise have
recommended: every one of those six roles is independently excluded above on grounds
taken from `RULES.md` and `TACTICS.md`, not from the memo. But I note two things
plainly rather than working around them:

1. If anyone later wants such a component near those six roles, the route is a rule
   change agreed with the user (the preamble of `RULES.md`) or an open question under
   RULES 33 - not a paraphrase into an instruction.
2. Whether a *laboratory-produced measurement that happens to be filed in `external/`*
   is itself under that limit, or whether the limit binds only material that came from
   outside, is genuinely ambiguous in the wording. That is a wording that can be read
   two ways, which RULES 33 calls an open question. I am not deciding it.

---

## 6 - Steers I was given, reported as required

`RULES.md` 3 forbids an instruction that tells an agent what to look for. Two sentences
in my instruction carry a steer, and I report them rather than pretending they were
neutral:

1. *"Part of the memo's description of the response has already been found incomplete by
   a probe."* This told me in advance what I would find. It was accompanied by an
   instruction to establish the contract myself, which I did - the findings in section
   1.2 come from my own 37 probes and each names the probe that produced it - but the
   expectation was set before I started.
2. *"That ordering condition is the whole worth of the exercise."* A judgement about the
   method, handed down rather than reached. I acted on it; I did not test it.

The instruction deliberately did **not** restate the memo's sections 4 and 5 and sent me
to read them, which is the opposite of a steer, and worth recording as such.

Separately, the memo itself contains two steers - "`score` is probably the one you want
for observation work" (section 3) and the accept-above-0.9 observation (section 5). My
measurements contradict both: `score` lost to a constant here (section 3.3), and errors
survived above 0.9 (section 4). The first of those two memo sentences is the one
`external/SOURCES.md` names as barred from a watcher or canteen instruction.

---

## 7 - The key, and what was checked

- `OPENROUTER_API_KEY` was read from the environment only. It is in no script, no
  artefact, no log line and no part of this report. `.env` remains in `.gitignore`.
- Every string written to disk by scripts 19 and 21 passes through a `scrub()` that
  replaces the key, the key's last 12 characters, and the account id the endpoint
  echoes in validation errors.
- `scripts/23_manifest_and_scan.py` re-checks this after the fact over every file this
  run produced plus every script it wrote: it looks for the exact key, for any 20+
  character substring of the key, and for **anything merely shaped like a credential**
  (`sk-` style tokens, long bearer-like strings, 40+ character high-entropy runs that
  are not one of this run's own SHA-256 digests). Its verdict is in
  `MANIFEST.json -> secret_scan`.
- **A failure to report under RULES 21, not mine to hide:** the first version of
  `scripts/19_endpoint_probe.py` used a fabricated bearer token for the wrong-auth probe
  that was *shaped* like a real OpenRouter key. It was never a real credential and the
  real key was never sent in that probe, but GitHub push protection matched the pattern
  and rejected the push; the coordinator reset the commit and replaced the literal with
  `Bearer not-a-real-token-deliberately-invalid`. The probe was re-run with the new
  literal, and the endpoint's answer changed - `401 Missing Authentication header`
  instead of `401 User not found.` - which is itself the contract finding in section 1.2
  item 9.
- **Also to report:** an earlier, unredacted `probe-results.json` containing the account
  id was committed by a concurrent process at 23:09:36 UTC before I had added that
  redaction (commit `4604cb5`, since reset locally, and its content survives only as a
  loose git object). The API key was never in it - verified by scan. I added the
  account-id redaction and regenerated the artefact.

---

## 8 - Fingerprints

In `MANIFEST.json`, which carries a SHA-256 for every file in this folder including this
report. The load-bearing ones:

| file | sha256 |
|---|---|
| `items.jsonl` | `5871ab671c0bcb18c97fbafa29bfe20bc97c392e294b1efe1fadf2c0dcd79462` |
| `key.jsonl` | `2b9c95375e9bdb4ad134cd591e8dce792edd5ce1f09278abb245bb45ccf26c7f` |
| `responses.jsonl` | `2b0da346faeb4e6b19787c71b3c9f4aa7f54168bcfeb75e9a114d3e1acf4fa6d` |
| `comparison.jsonl` | `c9377461c70c2c485bc3d22bf513761cfd39c86d2bbe43f674e2689c2f93aa62` |
| `probes/probe-results.json` | `bbce3d40246f25786cbf3c6f2e66a8757bb06a8a7cf784c54415c2ea6d0a4394` |

`key.jsonl`'s digest is the one notarised at the endpoint at provider time 1789859632,
66 seconds before the first item call.

---

## 9 - Unknowns (RULES 31 - this line cannot be empty)

1. **The FIELD key is provenance, not adjudication.** It records which watcher wrote a
   line, not what the line is about. Some of the 27 disagreements are of that kind: item
   `I017` is a Kenji line whose visible subject is bitcoin and ethereum - Amara's field
   by `TEAM.md` - and the model answered `OUTSIDE_WORLD` at 0.99. Item `I058` is an
   Ingrid line that never uses the word funding. **I am not adjudicating these**; I am
   recording that the 73% is a lower bound on something and an upper bound on nothing,
   and that the error-confidence list in section 3.1 mixes two causes that this run
   cannot separate.
2. **The CERTAINTY key is one person's self-rating.** Its attainable ceiling is unknown
   and certainly below 100%.
3. **Run-to-run stability on real items is unmeasured.** Two identical probe calls gave
   the same choice; the 100 items were never re-sent. Until that is measured, nothing
   here supports a claim of reproducibility under RULES 29.
4. **The definition of `confidence` is unpublished.** Only the identities in section 1.2
   item 11 were tested; for more than two options nothing I tested reproduced it.
5. **No rate limit or throughput ceiling was probed.** All calls here were sequential;
   concurrency behaviour is unknown.
6. **One notarisation call's cost is unrecoverable** and appears in section 3.4 marked as
   an estimate.
7. **Sampling error is not quantified.** 100 items, one draw, one seed. No confidence
   interval is given on 73%, and none should be read into it.
