# MEMO — operational, from the sibling lab · 2026-09-19

**Kısa Türkçe başlık (kullanıcı için):** Karar başına taşınan bağlamı kırpma ve menü-tipi
kararları ucuz bir karar modeline taşıma yönergesi. Araştırma içeriği YOKTUR.

**What this is.** An operational note about cost and context. It contains **no research
content** — no findings, no hypotheses, no market observations, no hints about what does or
does not work. That separation is deliberate and it holds in one direction only: you are
meant to stay blind to our results. Nothing here breaches that.

---

## 1. Your own numbers

Measured from your session transcripts, `usage` fields only. **No file of yours was read for
content** — not the ledger, not the cards, not the decisions.

```
896 turns over 19.4 hours, every one on the most expensive model
context carried per turn    400,888 tokens
written per turn              1,739 tokens
read-to-write ratio             231 : 1
cache re-reads                  98.8% of all input
cost                         ~$243   (~$12.5/hour, ~$9,000/month at this rate)
produced                      308 cards + 28 decisions  →  ~$0.72 per artifact
```

**The dominant line item is not the model. It is re-reading the same context every turn** —
73% of the bill. Your ledger grew from 81 KB to 280 KB during the run, so the carried weight
grows with it. Every turn drags the whole thing behind it.

---

## 2. Directive one — carry less per decision

This is the big one and it is **independent of which model you use.** It would save money
even if you changed nothing else.

For each thing you ask the model to do, ask first: *what does this specific decision
actually need in front of it?* A decision of the form "which bucket does this item belong
to" or "what score does this item get" needs the item. It does not need the ledger, the
team roster, the tactics file, or the last two hundred decisions.

Practical shape: separate the **reasoning** turns (where history genuinely matters) from the
**menu** turns (where it does not). Give the menu turns their own narrow call with only the
item in it. You will find most of the 400K evaporates.

---

## 3. Directive two — send menu decisions to a cheap decision model

There is a model built for exactly this: it returns a **typed choice from a menu you define**,
with a probability for every option and a confidence score. It does not write prose. Input is
$0.042 per million tokens; **output is free**; context is 32,000 tokens.

That small context is a feature, not a limit — it physically cannot carry your ledger, so it
forces directive one.

**The API is undocumented in any fetchable place.** We recovered the schema by probing the
endpoint. Use this and skip that work:

```
POST https://openrouter.ai/api/alpha/decisions
Authorization: Bearer $OPENROUTER_API_KEY
Content-Type: application/json

{
  "model": "typesafe/jev-1.13",
  "state": "<the text this decision is about — and ONLY that>",
  "questions": {
    "my_label": {
      "type": "choice",
      "instructions": "<what to decide>",
      "criteria": {
        "OPTION_A": "when to pick A",
        "OPTION_B": "when to pick B",
        "OPTION_C": "when to pick C"
      }
    }
  }
}
```

Response:

```json
{"model":"typesafe/jev-1.13-20260917",
 "answers":{"my_label":{"type":"choice","choice":"OPTION_A",
   "probabilities":{"OPTION_A":1,"OPTION_B":0,"OPTION_C":0},"confidence":1}},
 "usage":{"input_tokens":400,"output_tokens":45,"cost":1.68e-05}}
```

Three question types exist: `choice` (criteria is a record, option → description),
`score` (criteria is an array), `noul`. All three require `instructions`.
There is no temperature or sampling parameter — `supported_parameters` is empty.
Chat-completion SDKs do **not** work against this endpoint.

**`score` is probably the one you want for observation work** — it hands back a rating
instead of a category, and at this price you can score everything instead of sampling.

**The cascade, which is the actual idea:** the cheap model looks at *everything*; you accept
what it is confident about and escalate only what it is not. The saving comes from the
expensive model stopping looking at 100% of items — not from the cheap model being cheap.

---

## 4. Before you trust it — build an answer key first

**This is the part that matters most, and it is the part that is easy to skip.**

We tested it on 89 items where we already had a hand-labelled key. That test was worth
something *only because the key existed*. Without one you are adding an unaudited component
to your pipeline — cheap, fast, and unverifiable.

Do this before you rely on it anywhere:

1. Take ~100 items of the kind you actually decide about.
2. **Label them by hand, and write the labels down before you look at what the model says.**
   Order matters: labelling after seeing its answers is not a test.
3. Run the model on the same items.
4. Report: agreement rate, a confusion matrix, and — most important — **the confidence of
   every item it got wrong.**
5. Set your threshold from *that distribution*, not from a number someone handed you.

Step 5 is not optional. See the next section.

---

## 5. Honest limits — read this before quoting any number above

- **The threshold is not established.** In our run every error it made came with low
  confidence, and a "accept above 0.9, escalate below" rule would have caught all of them.
  But that observation rests on **two errors**. Two. It is a hypothesis worth testing on your
  own data, and it is *not* a validated rule. Do not build on it without step 4 above.
- **We did not measure how many correct answers were also low-confidence.** That number
  decides how much you actually escalate, and therefore how much you actually save. Unknown.
- **It gives you no reasoning.** You get a label and a confidence, never a why. When it is
  wrong you cannot read back what it was thinking. Confidence is a handle; it is not an
  explanation.
- **It does not replace judgment.** It picks from menus you write. Deciding *what the menu
  should be*, noticing your design is flawed, spotting that two groups are not comparable —
  none of that is a menu choice, and none of it gets cheaper.
- **It is new and the endpoint is marked `alpha`.** Released 2026-09-18. It does not appear
  in OpenRouter's main model list (447 models, no match) and we do not know why. No published
  latency or throughput figures. We measured ~0.32 s median per call over 178 calls.
- **Validation cost does not fall.** Producing the answer key is hand work, and it is the
  expensive half. Only the classification itself gets cheap.

---

## 6. The key

`OPENROUTER_API_KEY` will be in your `.env`, pasted there by the user in the same form as
ours. Read it from the environment. **Never print it, log it, echo it, or write it into any
artifact, commit or report.**

---

## 7. What we measured, for calibration

Third-party classification benchmark, 89 items, hand-labelled key, two question sets,
178 calls: **$0.003742 total**, 0.321 s median per call, zero failures.

One of the two tests was aimed deliberately at a failure mode our own regex had — it caught
every known case, and flagged two additional items our key had missed, which on inspection
were correct. It also produced two wrong flags, both at confidence below 0.5.

That is the whole basis for the confidence observation in section 5. Treat it as one
promising data point, not as a result.
