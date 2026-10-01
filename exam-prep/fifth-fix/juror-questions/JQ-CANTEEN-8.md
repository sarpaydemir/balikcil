# JQ-CANTEEN-8 · May two calm moments of one coin overlap? — two parts

Referred by: the canteen chair, who recorded it and did not answer it
(`canteen/2026-09-19-sofia.md` §8, lines 918–933). Written out as a juror
file by: Mateo · data engineer · third-fix run · 2026-10-01 (system clock).
Corrected by: Mateo · fourth-fix run · 2026-10-01 (system clock) — two
statements about the written texts are made exact (where the per-coin
spacing is written, and what the canteen book's "overlap by ten hours" fits);
the options, the counts and the stakes are unchanged; JQ-N1 has a new place.
Corrected by: Mateo · fifth-fix run · 2026-10-01 (system clock) — one
quotation of a script comment is removed from the rule texts; it is not
needed to answer (fourth review). Nothing else changed; JQ-N1
has a new place.
**You do not need to open the canteen book, or anything under `exam-prep/`
except JQ-N1, which you answer too; what you need is quoted here.**

## What you open

- this file
- `exam-prep/fifth-fix/juror-questions/JQ-N1.md` (answered by you too)
- `RULES.md` (lines cited below)
- `TACTICS.md` (lines cited below)

## What you decide, and what you may not

You decide a **definition and a procedure** (RULES 33): whether TACTICS 2's
moment selection allows two calm moments of one coin to overlap, and, if it
does not, which written definition of "overlap" applies. You do **not**
choose a number of hours: every spacing below follows from a definition that
is already written, and if you think none of them applies, say "other" and
why. You do not decide a threshold, a score or a trading rule, and you do not
change a rule.

Answer together with JQ-N1 (`exam-prep/fifth-fix/juror-questions/JQ-N1.md`),
by the same jurors: its part 3 asks whether two moments of one coin may be
counted as one event, and the number of such pairs depends on your answer
here.

For each part: your answer; the file and line it rests on, quoted (RULES 34);
the strongest case against your answer; your confidence, 1–5. "Other" is
allowed, with reasons. Listing an option is not recommending it.

---

## The text

- `TACTICS.md` lines 38–39 (§2): "The largest 20 of the year are taken for
  each coin." · "Of two moments closer than 48 hours to each other, only the
  larger counts."
- `TACTICS.md` lines 42–43 (§2): "**Calm moment:** the same number as the
  large moments, chosen at random. At least 72 hours away from any large
  movement."
- `TACTICS.md` line 44 (§2): "A moment's start is the hour at which the
  24-hour movement began."
- `TACTICS.md` lines 50–53 (§3): "**Before:** the 24 hours before the start,
  hour by hour …" · "**After:** the 24 hours after the start. Shown only in
  free observation, never in the exam."
- `RULES.md` lines 53–54 (RULES 13): "Moments occurring in several coins in
  the same hour count as a single event. If the whole market moved together,
  that is one event."
- The canteen chair's question, `canteen/2026-09-19-sofia.md` lines 920–922:
  "**May two calm moments overlap each other?** TACTICS 2 spaces large
  moments 48 hours apart and keeps calm moments 72 hours from a large one,
  but says **nothing** about calm-to-calm."

TACTICS 2 takes its moments **per coin** (line 38: "The largest 20 of the
year are taken for each coin"), and the script that drew the moments applies
the spacings of lines 39 and 43 within each coin (`scripts/06_find_moments.py`,
function `find_for_symbol`, lines 136 and 178–199); that is the reading of
TACTICS 2 the moments were drawn under. Moments of
**different** coins that share hours are what RULES 13 governs, and how they
are counted is JQ-N1. This question is therefore about calm moments of the
**same** coin. If you read the question as also covering different coins,
answer "other" and say so.

## What "overlap" can mean — two written definitions

- **card spans** — the two cards' 48-hour spans (24 hours before the start
  and 24 after) share at least one clock hour; equivalently, the two start
  hours are at most 47 hours apart. This is the definition written in the
  laboratory's overlap measurement (`data/overlap/overlap-manifest.md`,
  "Window definition": "Two cards *share a clock hour* when their 48-hour
  spans have at least one hour in common"), and it is the one behind the
  count the canteen chair quotes.
- **before windows** — the two cards' 24-hour before windows share at least
  one clock hour; equivalently, the two start hours are at most 23 hours
  apart. This is the part an exam card shows (TACTICS 3 lines 50–53).

The canteen book gives one overlap in hours: "C010 and C011 overlap by ten
hours" (lines 203–204; again in §8, line 926: "10 h overlap"). Their cards
start 14 hours apart, so their before windows share 10 hours — and so do
their after windows and their two 24-hour movements, since any two 24-hour
windows 14 hours apart share 10 hours — while their card spans share 34. The
book's figure therefore fits a 24-hour window without saying which one; it
does not fit card spans. Every 24-hour reading gives the same spacing as
"before windows" below.

## What has been measured — on the 306 observation cards, not the exam cards

Source: `data/overlap/pairs.csv` (run `12ce59e2902a0034`), counted by
`scripts/26_third_fix_checks.py`, run `212dd7ecffc51263` (G-3). Nothing has
been measured on exam cards.

| the two moments | card spans share an hour | before windows share an hour |
|---|---|---|
| both calm, **same coin** | **21** | **10** |
| both calm, different coins | 114 | 53 |
| one calm, one large, different coins | 206 | 97 |
| both large, different coins | 154 | 101 |
| one calm, one large, same coin | 0 | 0 |
| both large, same coin | 0 | 0 |

The canteen chair's figure, "135 calm+calm overlapping pairs out of 495", is
the first two rows of the card-span column added together: 21 same-coin and
114 different-coin pairs. Every same-coin overlapping pair in the set is a
pair of calm moments; the last two rows are zero because the moments were
drawn with TACTICS 2's spacings applied within each coin (48 hours between
large moments, 72 hours between a calm and a large one), which leaves no room
for them.

## Part a · May two calm moments of the same coin overlap?

- **yes** — TACTICS 2 sets no calm-to-calm spacing, and a rule that is not
  written is not applied.
- **no** — two moments that share hours are not two observations; TACTICS 2
  spaces every other pair of one coin's moments, and calm moments are no
  exception.
- **Other**, with reasons.

## Part b · Only if part a is "no": which overlap?

- **card spans** — calm moments of one coin must start at least 48 hours
  apart (the 21 pairs above would not be allowed).
- **before windows** — calm moments of one coin must start at least 24 hours
  apart (the 10 pairs above would not be allowed).
- **Other**, with reasons.

---

## What follows from the answers, so you can see the stakes — not to steer

- **"yes"**: nothing changes in how calm moments are drawn. Overlapping calm
  cards of one coin remain, and how they are counted is decided by JQ-N1.
- **"no"**: the exam's calm moments must be drawn so that no two of one coin
  overlap in the sense chosen in part b. How the draw achieves that (for
  example, drawing again when a draw breaks it) is engineering; it will be
  written down before the draw and reported, and it involves no number of
  its own. This question does not ask what to do about the 306 observation
  cards already written; they are the material the counts above come from.

Neither answer changes `RULES.md`.
