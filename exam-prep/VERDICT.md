# Verdict — the two problems before the exam

Mateo · data engineer · 2026-09-19 (system clock, RULES 23)

This file says whether each problem is solved and nothing about how. The
working is in the other files of `exam-prep/`.

---

## R-04 — the exam may not be blind

**SOLVED, against the standard written below, with a residual that is measured
and named and not zero.**

The standard I set, and by which a reviewer may disagree with me:

1. No field whose absolute level is a coin's signature may identify a card's
   coin, or link two cards of the same coin, better than the RULES 12 chance
   line. **Met.**
2. No printed column may identify which clock hours a card covers.
   **Met.**
3. The pooled attack over *everything* an exam candidate can see must also sit
   at the chance line. **Not met, and it cannot be met** — the reason is a
   small number of fields that the **frozen** canteen book and TACTICS 3
   require to stay on the card. Each is named, with its measured size, in
   `exam-prep/R-04-blindness.md` §7. Removing any of them would mean changing
   a rule after the fact, which RULES 6 forbids.
4. Nothing that the frozen canteen book asks an exam candidate for may be
   destroyed. **Met, and checked by script on every card.**

Two things the reviewer should weigh before accepting this verdict:

- Everything was measured on the **306 observation cards**, because `exam/` is
  closed to this run. The acceptance gate for the exam itself is written down
  as a step the exam-building run must perform before the answer key is sealed.
  Until that step runs, R-04 is solved *on the material I was allowed to see*.
- The attacker I used is a script reading all 306 cards at once. An exam
  candidate has no tools and reads no files (RULES 10). I measured the stronger
  adversary and did not measure the weaker one.

**No change to `RULES.md` is required.** The fix implements RULES 9 more
completely than TACTICS 6 does; it does not alter RULES 9. It **does** go
beyond TACTICS 6's list of what is hidden, and every step beyond that list is
named in `exam-prep/decisions-and-open-questions.md`.

---

## N-1 — collapse before counting

**SOLVED as far as one person is allowed to solve it. The instrument exists,
is tested and is cross-checked. The last step is not mine and is named.**

The standard I set:

1. One deterministic implementation, producing a true partition, checked on
   every run. **Met.**
2. It must reproduce, on the 306 observation cards, the counts an independent
   earlier script measured for the same relation. **Met, exactly.**
3. Every reading of RULES 13's wording that the written rules allow is
   implemented and measured, and none is chosen by me. **Met.**
4. A judge cannot compute a chance line without supplying an event map.
   **Met — the function refuses.**
5. The effect of collapsing is measured, not asserted. **Met.**

**What is not done, and why it is not mine:** RULES 13's phrase "in the same
hour" can be read more than one way, and the readings do not give the same
numbers. That is a wording that can be read two ways and a choice that changes
the numbers — an **open question under RULES 33**, which says it is never
answered by one person. It is written out as four numbered questions for three
jurors in `exam-prep/N-1-collapse.md` §7, together with every measurement a
juror needs to rule. Until that ruling exists, the judge's script cannot be
pointed at a configuration.

**A juror should read §7 there, not a paraphrase of it.** I have deliberately
kept the numbers out of this file: a question handed to jurors through a
summary is a question with a thumb on it.

One thing the laboratory should know before it rules, and I state it without
numbers here for the same reason: **my measurement does not support the
strongest form of the complaint N-1 makes.** Part of the correction is large
and part of it is negligible, depending on which reading is ratified. The
measurement is in `exam-prep/N-1-collapse.md` §6.

**No change to `RULES.md` is required.**

---

## A steer in the instruction I was given

I was asked to report one if I found it. I found no result and no prediction in
the instruction. One sentence leans: it speaks of what a later run needs "to
count events correctly", which presumes the current counting is wrong. My
measurement came out mixed rather than confirming that presumption, and I have
said so above rather than let the presumption stand. Two further near-misses
and the full reasoning are in `exam-prep/decisions-and-open-questions.md` §C.

---

## Where the rest is

| file | what it holds |
|---|---|
| `exam-prep/R-04-blindness.md` | the blindness standard, the measurements, the residuals, what the exam-building run must do |
| `exam-prep/N-1-collapse.md` | the collapse standard, the readings, the open question, what the judge's script must do |
| `exam-prep/decisions-and-open-questions.md` | ten decisions I took that the instruction did not cover, five questions I refused to answer, and the steer check |
| `exam-prep/collapse/` | the event maps and the shuffle calibration, with run records |
| `exam-prep/identity/` | the audits of the raw and the blinded card sets |
| `exam-prep/blind-proof/` | four blinded copies of the 306 observation cards, one per configuration |
| `scripts/15_event_collapse.py` `16_identity_audit.py` `17_blind_cards.py` `18_residual_diagnostic.py` `lab_cards.py` | the instruments |

Nothing under `exam/` was read or written by this run.
