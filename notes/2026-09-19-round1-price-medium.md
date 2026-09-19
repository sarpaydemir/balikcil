# Round 1 notes — watcher · field of view: price itself (price, volume, trade count, order book depth, volatility)

Cards read: C001–C010. Date: 2026-09-19. Round 1 (own cards only; no other watcher's notes read).

All ten cards carry the same coin, `AVGOUSDT`. Everything below is therefore one coin, ten moments.
Moment kinds as printed on the cards: large = C003, C004, C005, C007, C009 · calm = C001, C002, C006, C008, C010.

Where I write a number I took it off the card. Where I estimated (eyeballed medians), I write "estimate".

---

## A · Structure of the card set (these are measurements, not signals)

C001 · all ten cards are the same coin (`AVGOUSDT` on every card header) · read the coin line of C001–C010; no second coin appears · 5
C004 · C004's "after" window and C005's "before" window are the same hours: C004 after +23 close 408.26, C005 before h-24 close 408.24, and C004 start 2026-06-03 12:00 + 48 h = C005 start 2026-06-05 12:00 · opinion: these two cards are not independent events — the crash I read as "what happened after C004" is the same data I read as "what came before C005" · 5
C003 · C003 (start 06-01 10:00), C004 (06-03 12:00), C005 (06-05 12:00) and C006 (06-10 07:00) all fall inside 2026-06-01 → 2026-06-10, a single continuous price episode (C003 after ends 492.83; C004 before opens 487.39 two hours later; C005 before opens where C004 after closed; C006 before opens 399.87 just after C005's crash) · opinion: 3 of my 5 large cards and 1 calm card are one event, so any count like "seen in 3 large cards" here may really be one event (RULES 13) · 5
C001 · C001 is labelled "calm" yet its measured 24-hour move is +4.19%; C010 is labelled "calm" with -4.87% · opinion: "calm" on these cards means "far from a selected large moment", not "small move" — a signal that predicts a 4–5% move would still be scored wrong on these two · 4

## B · What separated large from calm, and what did not

C001–C010 · Mean absolute hourly change over the 24 before-hours (I summed the `chg%` column and divided by 24): large C003 0.30, C004 0.58, C005 0.63, C007 0.31, C009 0.57 · calm C001 0.36, C002 0.18, C006 0.72, C008 0.35, C010 0.37 · at a 0.50 cut, above = C004, C005, C009 (large) + C006 (calm) = 3 of 4 large; below = C003, C007 (large) + C001, C002, C008, C010 (calm) = 2 of 6 large · opinion: this was the best separator I could measure in my field, but it is 3-vs-1 against a 50% base rate on 10 cards of one coin, and three of the four "above" cards are the single June episode · 3
C006 · the highest before-window volatility of all ten cards (mean |hourly chg| 0.72; four hours of |chg| ≥ 2%: -2.46, -2.88, +2.51, +2.04; previous-7-day high-low range 38.27%, also the highest of the ten) sits on a card whose after is calm (-2.51%) · opinion: the top of the volatility scale does not mark a large moment — whatever edge exists in B above dies at the extreme · 4
C001–C010 · Largest single before-hour |chg%|: large C003 1.22, C004 2.00, C005 2.20, C007 1.16, C009 1.89 · calm C001 1.48, C002 1.05, C006 2.88, C008 1.50, C010 1.72 · the ranges overlap completely and the single largest value (2.88, C006) is a calm card · opinion: "one violent hour appeared in the last 24 h" carries no information here · 4
C001–C010 · Previous-7-day high-low range (printed on the card): large 11.38, 18.37, 23.12, 9.51, 6.10 · calm 7.15, 4.16, 38.27, 7.28, 11.92 · the largest (38.27, C006) and the smallest (4.16, C002) are both calm · 4
C001–C010 · Previous-7-day average hourly volume (printed): large 153.81k, 313.19k, 960.13k, 415.87k, 390.92k · calm 47.72k, 85.83k, 1.95M, 393.34k, 482.53k · calm holds both the two smallest and the largest · opinion: the coin's overall activity level does not sort the two kinds · 4
C001–C010 · Before-window high-low range as % of the window low: C003 1.80, C007 2.13, C010 2.25, C002 2.64, C009 2.74, C001 3.42, C008 3.43, C005 4.97, C004 5.98, C006 7.42 · the five narrowest hold 3 large and 2 calm, the five widest 2 large and 3 calm · opinion: "coiling / quiet before the storm" is 5 out of 10 here, i.e. nothing · 4
C001–C010 · Last-before-hour quote volume divided by the before-window median volume (medians eyeballed — **estimate**): large ≈1.3 (C003), ≈0.95 (C004), ≈0.35 (C005), ≈1.7 (C007), ≈2.4 (C009) · calm ≈3.9 (C001), ≈1.7 (C002), ≈0.6 (C006), ≈0.5 (C008), ≈0.8 (C010) · the highest ratio of all ten is a calm card · opinion: a volume flare in the final hour is not a marker · 3
C006 · a single 8.48M / 35k-trade hour at h-18, the biggest single before-hour volume in my whole set, is followed by a calm after (-2.51%); C008 likewise carries 4.17M / 15k at h-16 and is calm (+0.56%) · opinion: a huge isolated volume bar inside the before window appears in calm cards at least as often as large ones (2 calm here vs C005's 21.04M at h-23 and C009's 4.66M at h-2 on the large side — 2 vs 2) · 4

## C · Order book depth

C002 · depth-1% collapses from ~165k through the first 21 hours to 33.06k / 39.51k / 37.41k in the last three hours (a ~4–5x thinning), and the after is flat: -0.05% · 5
C008 · depth-1% falls from ~600–700k to 330k / 307k / 194k / 165k / 173k over the last five hours (~4x thinning), and the after is calm: +0.56% · 5
C001–C010 · a clear thinning of depth-1% into the start hour occurs in C001, C002, C008 (all calm) and C009 (large, 660k early → 356.85k at h-1) · opinion: 3 calm to 1 large — depth drying up before the start hour is, on these ten cards, mildly associated with the calm cards, the opposite of what I expected · 3
C007 · depth-1% roughly triples across the before window (≈230k at h-17 → 695.62k at h-1) and is followed by a large down move (-8.36%) · opinion: one card only, and C010 shows the same kind of build (554.50k at h-1 after 1.74M at h-8) with a calm after — this is an observation, not a rule · 2
C001–C010 · depth asymmetry at h-1, depth+1% ÷ depth-1%: C003 1.52, C002 1.23, C007 1.13, C009 1.11, C010 1.08, C001 1.02, C005 1.02, C004 0.93, C008 0.92, C006 0.83 · after-move for the three lowest: -2.51%, +0.56%, -17.27%; for the three highest: +7.72%, -0.05%, -8.36% · opinion: tested and no separation, either by kind or by direction · 4
C003 · single-hour depth readings jump by 3–7x with no matching price move (C003 h-21: depth-1% 49.54k vs depth+1% 335.96k; C010 h-8: depth-1% 1.74M against ~700k neighbours; C002 h-3: 173k → 33.06k in one hour; C008 h-5: 543k → 330k) · opinion: the depth column behaves like a one-off-large-resting-order reading rather than a stable state, so single-hour depth values should not be trusted as a level; seen in 4 cards · 3

## D · Direction

C001–C010 · Before-window 24 h close-to-close change (close h-1 ÷ close h-24): C001 -2.94, C002 +2.14, C003 -0.72, C004 +1.25, C005 +0.81, C006 -3.31, C007 -0.16, C008 -1.13, C009 +1.36, C010 +0.43 · the after-move carried the same sign in 3 of 10 (C006, C007, C009) and the opposite sign in 7 of 10 · opinion: the "last 24 hours continue" rival (RULES 11) scored 3/10 on my set; but 5 of the 7 reversals are calm cards where the after-move is small, so most of that 7 is not money · 4
C001–C010 · restricted to the five large cards only, the before-direction continued in 2 (C007 -0.16 → -8.36; C009 +1.36 → +8.82) and reversed in 3 (C003, C004, C005) · opinion: 2-vs-3 on five cards is indistinguishable from a coin flip · 4
C001 · the two cards whose last before-hour close is the exact low of the whole 24-hour before window (C001 close h-1 412.92 = window low; C003 close h-1 457.53 = window low) both rose afterwards, +4.19% and +7.72% · opinion: two cards is an observation, not a rule; and no card in my set closed at the exact window high, so I have no counter-test · 2
C004 · all five before-window closes sit between 0.35 and 0.89 of their window's high-low range except C001 and C003 (both 0.00): C004 0.68 → -17.27%, C005 0.35 → -9.70%, C007 0.89 → -8.36%, C009 0.69 → +8.82%, C002 0.99 → -0.05%, C006 0.42, C008 0.55, C010 0.52 · opinion: where the close sits in the before range did not order the after-direction — C007 at 0.89 fell hard and C009 at 0.69 rose hard · 4

## E · Whole-market check (RULES 13 / my definition's point 2)

C004 · the -17.27% move runs with a falling market: in the after window BTC prints -1.19, -0.88, -1.30, -1.18, -1.25, -1.85, -1.34 and ETH -1.18, -1.60, -1.22, -1.15, -1.89, -1.68 over the same hours · opinion: this large moment is at least partly a market-wide event, not this coin's own · 4
C005 · the -9.70% move likewise coincides with BTC -2.00, -2.34 and ETH -2.54, -2.59 in its first seven after-hours · opinion: same caveat as C004, and since C004's after = C005's before these two are one market episode · 4
C009 · the biggest single up hour in my set (+3.38% on 10.45M quote volume, 30k trades, at +1) happens while BTC is -0.02 and ETH -0.05 in that same hour · opinion: this large moment is specific to the coin, not the market · 4
C002 · at h-2 BTC +1.71 and ETH +3.33 while the coin prints +0.23; at C008 h-16 ETH +2.90 while the coin prints +0.18 · opinion: on these cards the coin does not track BTC/ETH hour by hour, so a BTC/ETH reading is not a usable proxy for it — but C004/C005 show it still gets dragged along in a broad sell-off · 3

## F · Ideas (three parts each — these are ideas, not evidence)

**Idea 1 — before-window volatility as a "large moment is coming" filter.**
- Trigger: at the start hour, the mean of the absolute hourly `chg%` over the preceding 24 hours is ≥ 0.50.
- Direction: none. This is a filter for *whether* a big move comes, not which way; used alone it says "take a position only when this fires", and the direction must come from somewhere else.
- Exit: 24 hours after entry, unconditionally.
- Count on my cards: fired on 4 of 10 (C004, C005, C006, C009); 3 of those 4 were large. Did not fire on C003 and C007, which were large. Base rate 50%, and three of the four firings are the one June episode.
- Restatement warning: this is computed from price alone, so it adds nothing to a reader who already has the price series — it is a summary of it, not extra information.

**Idea 2 — fade the trailing 24 hours.**
- Trigger: at the start hour, take the sign of the close-to-close change over the preceding 24 hours.
- Direction: opposite to that sign (before-move positive → sell; negative → buy).
- Exit: 24 hours after entry, unconditionally.
- Count on my cards: correct sign in 7 of 10. But restricted to the 5 large cards it is 3 right (C003, C004, C005) / 2 wrong (C007, C009), and the two wrong ones are -8.36% and +8.82% against the position. Most of the 7 comes from calm cards where the move is a fraction of a percent and would not survive the 0.20% round-trip cost of TACTICS 8.
- I am writing this mainly because it is the mirror of the RULES 11 rival, so it should be tested rather than assumed.

## G · Where I looked and found nothing (RULES 20)

- Order book depth: present as two columns (`depth -1%`, `depth +1%`) on all 24+24 rows of all ten cards. No blank or `.` cell in either depth column on any of the ten. I looked at the level, the change across the window, the last-hour value and the +1%/-1% asymmetry; only the C-section notes came out of it.
- Volatility: no volatility column exists on these cards. Everything I report as volatility I computed myself from the `chg%` column, and I have said so each time.
- Trade count: present on every row of all ten cards. I compared it with volume; the ratio (volume per trade) moved between roughly 100 and 220 in the biggest hours (C004 h-23: 2.32M/22k; C005 h-23: 21.04M/96k; C009 h-2: 4.66M/21k) and I found no ordering by moment kind. **estimate** on those per-trade figures — I divided the rounded card values.
- I did not open any card other than C001–C010, and I read no file under `exam/`, `notes/`, `canteen/`, `decisions/`, `instructions/`, `data/`, `scripts/`, `reports/` or `LEDGER.md`.
