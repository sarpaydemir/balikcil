# JQ-R04-GATE · Which statistic decides whether exam cards are blind enough to use?

Referred by: Mateo · data engineer · second-fix run · 2026-10-01 (system clock).
Raised by the review of the first exam-preparation run (`exam-prep/REVIEW.md`
§3.3 and §3.6 item 1). **You do not need to open that file or anything else
under `exam-prep/`; what you need is quoted here.**

## What you open

- this file
- `RULES.md` (lines cited below)
- `TACTICS.md` (lines cited below)

## What you decide, and what you may not

You decide a **procedure** (RULES 33): which of two measurements, or which
combination of them, decides a pass/fail step that the exam-building run must
take before the answer key is sealed. You do **not** decide the chance line
(RULES 12 fixes it: 1,000 shuffles, the best 1%), a threshold, a score or a
trading rule, and you do not change a rule.

Give: your answer; the file and line it rests on, quoted (RULES 34); the
strongest case against your answer; your confidence, 1–5. "Other" is allowed,
with reasons. Listing an option is not recommending it.

---

## The rule text

- `RULES.md` line 41: "In the exam the coin name and the date are hidden."
- `RULES.md` lines 51–52 (RULES 12): "The chance line is not invented. The
  answers are shuffled 1,000 times, and the real result must fall inside the
  best 1%."
- `RULES.md` lines 34–35 (RULES 6): "The rule is written first, the result is
  opened second. A rule is not changed after looking at a result."
- `TACTICS.md` lines 101–107 (§6): the list of what is hidden on an exam card
  (coin name; date and time; the price itself, converted to a number starting
  from 100; the coin name inside announcements; the Wikipedia number; the date
  in the release calendar).

## The step whose wording is open

The first exam-preparation run wrote this step for the run that will build
the exam cards (its file `exam-prep/R-04-blindness.md` §8 step 3, quoted):

> Re-run `scripts/16_identity_audit.py` on the exam cards before the answer
> key is sealed … This is the acceptance gate … If `ALL-removable` beats its
> chance line on the exam cards, the cards are not blind and the gate has
> failed.

`ALL-removable` is every measurable feature of a card that the blinding could
still remove — everything except the features that must stay because a frozen
canteen rule or TACTICS requires them. The audit attacks it in **two** ways,
each against its own RULES 12 chance line (labels shuffled 1,000 times, best
1%):

- **nearest neighbour** — for each card, find the most similar other card;
  count how often it is the same coin. It asks: *can a card be matched to its
  own coin?*
- **pair AUC** — over every pair of cards, how well similarity separates
  same-coin pairs from different-coin pairs (0.5 = no information). It asks:
  *does similarity carry coin information on average?*

The sentence says "its chance line" but there are two. **Which one decides?**

The same run's own standard, for single families of features (its "Level 1"),
required a family to fail **both** attacks; for the pooled row the gate uses,
it did not say.

## The options the wording leaves open

- **A** — the gate fails if the pair AUC beats its line.
- **B** — the gate fails if the nearest-neighbour score beats its line.
- **C** — the gate fails if **either** beats its line.
- **D** — the gate fails only if **both** beat their lines.
- **Other**, with reasons.

### An optional second part

Two cards of one coin whose 48-hour windows overlap print some of the same
hours, so they are near-copies of each other; RULES 13 (`RULES.md` lines
53–54) treats moments in the same hour as one event. **Should the
nearest-neighbour attack be forbidden from matching a card to a card that
shares clock hours with it?** Answer only if you think it bears on your
answer above.

## What has been measured — on the observation cards, not the exam cards

Nothing has been measured on exam cards; this run cannot see `exam/`. On the 306
observation cards, blinded with the configuration the first run recommends
(`strict-flags`):

| audit | nearest neighbour (its line) | pair AUC (its line) |
|---|---|---|
| as the first run built it (run `ba8d6b5e3880f9ee`) | 0.1895 (0.1667) — beats | 0.5049 (0.5130) — does not beat |
| extended by the second-fix run to every column's repeat structure, as the review required (run `d70dd7b545bfce8a`) | 0.3922 (0.1699) — beats | 0.5699 (0.5138) — beats |

With the extended audit the gate fails on these cards under A, B, C and D
alike. **Your answer therefore cannot change whether today's material
passes.** It decides how a later exam-card set will be judged.

Optional second part, measured: forbidding time-overlapping neighbours moves
the extended nearest-neighbour score from 0.3922 to 0.3856 (line 0.1732); on
the first run's audit it moved 0.1895 to 0.1732 (line 0.1699).
(Sources: `exam-prep/second-fix/identity/run-6f3cffc734151ae1/` and
`exam-prep/identity/residual-diagnostic-blinded-strict-flags.md`.)

## Why this is referred and not decided by the engineer

The sentence can be read four ways and the readings disagree on real
material — under the first run's audit, A and D pass the observation cards
while B and C fail them. RULES 33 calls that an open question. The engineer has
seen the observation numbers; RULES 6 is the reason the choice should not be
made by somebody who has.
