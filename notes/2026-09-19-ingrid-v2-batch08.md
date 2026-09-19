# Ingrid · watcher-high · field of view: exchange behaviour · round 1 · batch 08

Field of view: funding rate and payment-interval changes; listing / delisting /
warning announcements; administrative decisions of the exchange.
34 cards read (C210 C225 C169 C271 C068 C126 C205 C228 C101 C071 C115 C045 C242
C284 C133 C013 C255 C302 C229 C238 C028 C030 C124 C150 C301 C274 C168 C031 C114
C192 C012 C297 C026 C106). All counts below are out of these 34 cards only.

Format: `card no · what I saw · why I think so · how sure I am (1-5)`.

Note on a recurring value: `+0.0050%` per 4 h appears on almost every 4-hour
contract. Reading it as "the exchange's default/clamped value when the premium
is near zero" is **my opinion, not written on the card**; what the card states
is only the number.

## Part 1 - the whole-batch facts (every card checked, one by one)

C210 C225 C169 C271 C068 C126 C205 C228 C101 C071 C115 C045 C242 C284 C133 C013 C255 C302 C229 C238 C028 C030 C124 C150 C301 C274 C168 C031 C114 C192 C012 C297 C026 C106 · the **Exchange announcements** line is `MISSING` on all 34 cards, with identical wording: binance = HTTP 202 with a zero-length body, bithumb = only the 5 most recent notices so no history for the period, upbit = HTTP 404. Each card repeats it in "Fields not on this card". · I looked at the "Exchange announcements" line in the Before section and at the "Fields not on this card" block of each of the 34 files; no card carries any listing, delisting or warning text. Opinion: this is a fetch failure, not evidence that no announcement existed - half of my field of view is simply unobservable in this batch. · 5

C210 C225 C169 C271 C068 C126 C205 C228 C101 C071 C115 C045 C242 C284 C133 C013 C255 C302 C229 C238 C028 C030 C124 C150 C301 C274 C168 C031 C114 C192 C012 C297 C026 C106 · **`interval changed: no` on all 68 funding lines** (34 before + 34 after). Not one card in this batch shows a payment-interval change. · I read both funding lines of every card. Opinion: the interval field carries zero within-card information here; any rule built on "the interval changed" is untestable on this batch. · 5

C210 C225 C169 C271 C068 C126 C205 C228 C101 C071 C115 C242 C284 C133 C302 C229 C238 C124 C150 C301 C274 C168 C114 C192 C297 C106 · **interval 4 h, 6 payments per window** (26 cards); C045 C013 C255 C028 C030 C031 C012 C026 · **interval 8 h, 3 payments per window** (8 cards). The interval is constant per coin: 4 h for NEWT, NIL, KOMA, ZRO, FHE, FARTCOIN; 8 h for BCH, AVGO, NOK. · Read straight off the funding lines. Opinion: the interval is an administrative setting attached to the symbol, not an event; it separates coin types (the 8 h group here is BCH plus the two tokenised-stock symbols), so it is close to being a coin-identity label. · 5

## Part 2 - the +0.0050% baseline state and what follows it

C225 C126 C205 C228 C101 C071 C242 C133 C302 C238 C192 C106 · **all six before-window payments exactly +0.0050%** (12 of the 26 four-hour cards). Of these, 10 are calm moments (C225 -8.10%, C126 -6.79%, C205 +0.85%, C101 +1.42%, C071 +8.63%, C242 +5.78%, C133 -2.17%, C302 -2.33%, C238 +5.18%, C192 +1.53%) and **2 are large moments** (C228 -50.46%, C106 +120.84%). · Counted payment by payment on each card. Opinion: a flat baseline before the moment leans calm but does **not** rule out the two largest moves in the batch; as a blocker it would have blocked two of the biggest winners. · 4

C228 · funding stayed at **+0.0050% for all six payments of the after window too**, while the coin fell -50.46%, including -36.95% in the single hour +23. · Read both funding lines. Opinion: the crash hour sits at the very end of the window, probably after the last 4-hourly payment, so the funding field never registered the event at all - a timing artefact, not a signal. · 3

C106 · **all six before-window payments exactly +0.0050%** although the price moved +54.98% in hour -13 and -15.09% in hour -1, and the previous 7 days were +64.35%. · Compared the funding line with the hourly `chg%` column. Opinion: for this contract funding stayed pinned at baseline through violent two-way hourly moves - so the absence of a funding deviation says nothing about the absence of turmoil. Seen in 1 card. · 3

## Part 3 - deviation of funding from the baseline, before the moment

C169 C115 C229 C124 C150 C274 C168 C114 · on 4-hour contracts, **at least one before-window payment deviates from +0.0050% by 0.010 percentage points or more**, and all 8 are large moments (largest deviations: C229 -0.0723, C168 +0.0809, C169 +0.0556, C150 -0.0481, C115 -0.0366, C124 +0.0398, C274 -0.0252, C114 -0.0123). · I computed |rate - 0.0050| for each of the six payments on all 26 four-hour cards. Among the 14 calm four-hour cards only **C210** reaches this threshold (-0.0584); the other 13 stay within 0.004 pp of baseline (C271 max 0.0037, C301 0.0039, C297 0.0004, rest exactly 0). So the split within this batch is 8 of 12 large vs 1 of 14 calm. Opinion: the clearest separation I found, but it rests on 26 cards from 6 coins and the deviating cards are also the coins with the wildest prior 7-day prices (KOMA +186%/+62%, FHE -46%/-42%/+17%), so it may be a restatement of prior volatility that price alone already shows. · 3

C169 C115 C229 C124 C150 C274 C168 C114 · within those same 8 large cards the **sign of the deviation carries no direction**: positive-deviation cards went -51.75% (C169), +34.70% (C124), -16.54% (C150), +135.21% (C168); negative-deviation cards went +46.39% (C115), -25.02% (C229), +26.15% (C274), -34.22% (C114). Two up, two down in each group. · Compared the deviation sign with the measured 24-hour move on each card. Opinion: any rule using funding sign as a buy/sell direction has no support here; at best this is a "something is coming" flag with no arrow. · 4

C210 · a calm card (+0.69% over 24 h) whose before window opens with **-0.0584%**, the second-largest negative before-window payment in the batch, then returns to +0.0050%. · Read off the funding line. Opinion: this is the counterexample to the previous note - deep negative funding also appears before a moment where nothing happened. One card, but it is enough to stop "large negative funding means a move is coming" from being written as a rule. · 4

C115 C284 C229 C150 C168 C114 C026 C031 C255 C210 C030 · the before window contains **both a positive and a negative payment** (a sign flip inside 24 h): 9 of the 17 large cards (C115 C284 C229 C150 C168 C114 C026 C031 C255) against 2 of the 17 calm cards (C210, C030). · Counted signs payment by payment on all 34 cards. Opinion: same family as the deviation note above and largely the same cards, so it is not independent evidence; I record it because a sign flip is easier to compute than a deviation threshold. · 3

C168 · the widest before-window spread in the batch: **+0.0494 / +0.0050 / -0.0468 / +0.0050 / +0.0698 / +0.0809** - a range of 0.1277 pp across six payments - ahead of a +135.21% move. · Read off the funding line. Opinion: funding was being thrown around in both directions in the hours before the largest up-move I saw; one card only, so an observation, not a rule. · 3

C045 C028 C274 · **every before-window payment negative**: C045 (-0.0328 -0.0728 -0.0645, large, -15.23%), C274 (-0.0010 -0.0101 -0.0252 -0.0174 -0.0112 -0.0017, large, +26.15%), C028 (-0.0056 -0.0082 -0.0172, calm, -5.41%). · Read off the funding lines. Opinion: 2 large and 1 calm, and the two large ones went in opposite directions - too thin and too contradictory for anything but an observation. · 4

C169 · the only card where **all six before-window payments sit far above baseline** (+0.0345 +0.0556 +0.0408 +0.0451 +0.0500 +0.0408), followed by -51.75%. · Read off the funding line; no other card in the batch has a fully elevated positive before window. Opinion: suggestive of crowded longs paying to stay long before a collapse, but it is a single card. · 3

## Part 4 - funding in the after window (is it a restatement of price?)

C124 C106 C274 C255 C114 C229 · the after-window funding moves with the realised price: C124 rises monotonically (+0.0126 -> +0.0593) as price rises +34.70%; C106 spikes to +0.0742/+0.0694 during +120.84%; C274 goes **more negative** (-0.0519 first payment) while price rises +26.15%; C255 ends at **-0.1515%**, the largest absolute funding value anywhere in the batch, inside a -17.73% fall; C114 (-34.22%) ends at -0.0537; C229 (-25.02%) ends -0.0127 / -0.0429. · Compared each after-window funding line with the card's measured move. Opinion: after-window funding is downstream of the move - price already says it - so it is useful for costing a trade (RULES 14) but not as a signal. · 4

C169 C115 C301 C297 C271 · funding **collapses back to the +0.0050% baseline in the after window** after a non-baseline before window: C169 (+0.0345..+0.0556 -> +0.0243 then baseline), C115 (down to -0.0366 -> all six at baseline), C301/C297/C271 (small deviations -> all baseline). · Read both funding lines of each. Opinion: the deviation is short-lived in most cards; a rule that waits for funding to "confirm" after the start hour would usually find nothing left to see. · 3

## Part 5 - the 8-hour group

C013 C012 · AVGO: funding is **exactly +0.0000% for all three before-window payments on both cards**, and C012's after window is 0.0000% as well; C013 is a **large** moment (+7.91%) and C012 a **calm** one (-1.52%). C013's after window shows a single +0.0069%. · Read off the funding lines of both AVGO cards. Opinion: on this contract the funding field is flat zero and therefore separates nothing - a large move arrived with the funding field completely still. 2 of 2 AVGO cards. · 5

C045 C028 C030 C031 C026 · BCH (5 cards): before-window funding is negative and deep on one large card (C045 min -0.0728, -15.23%), negative but shallow on one calm card (C028 min -0.0172, -5.41%), near zero and mixed on a calm card (C030 +0.0051 -0.0052 -0.0000, -0.33%) and on a large card (C031 -0.0037 +0.0094 +0.0024, -12.50%), and mixed on another large card (C026 +0.0048 -0.0232 -0.0016, +22.83%). · Read all five funding lines. Opinion: inside the one coin where I have five cards, before-window funding does not separate large from calm - C031 is a -12.50% move preceded by an unremarkable funding line. · 4

C255 · NOK: before window +0.0510 +0.0089 -0.0147 (8 h), after window +0.0468 +0.0092 **-0.1515**, around a -17.73% move; the card also records 106 missing hours in the previous-7-day line. · Read off the funding lines and the 7-day summary line. Opinion: the -0.1515% is by far the largest payment in the batch and lands inside the fall, i.e. after the fact; with only one NOK card I can say nothing about repetition. · 4

## Part 6 - whole-market caveats (RULES 13)

C031 C045 C068 C026 · in these cards the BTC and ETH columns move hard in the same direction as the coin during the after window (C031: BTC -1.55/-1.82, ETH -3.46/-3.20 inside a -12.50% fall; C045: BTC -1.16, ETH -1.41 at +23 inside -15.23%; C068: BTC -1.75/-1.74, ETH -3.33/-1.61 inside -21.02%; C026: BTC +2.39, ETH +2.13 inside +22.83%). In three of these four (C031, C068, C026) the before-window funding line was at or very near baseline. · Read the BTC and ETH columns alongside the funding lines. Opinion: these look like market-wide events rather than coin events, and my field of view showed nothing before them - which is what I would expect if the cause was not coin-specific. · 4

## Part 7 - ideas and non-ideas

**Not an idea (direction missing, so it cannot be tested as a trade).** Trigger: on a 4-hour contract, at least one of the six funding payments in the previous 24 h differs from +0.0050% by >= 0.010 pp. Direction: **none** - the sign of the deviation gave 2 up / 2 down in each sign group (C169 C124 C150 C168 positive; C115 C229 C274 C114 negative). Exit: n/a. I am writing it down as an observation, not an idea, exactly because the direction part is missing (RULES 8). If it is used at all it can only be a "large movement is more likely" raising signal for the exam's separation question, worth little on its own: 8 of 12 large vs 1 of 14 calm, in one batch, 6 coins.

**Blocker candidate (three parts, but the third is degenerate).** Trigger: on a 4-hour contract, all six funding payments of the previous 24 h are exactly +0.0050%. Direction: **open no directional position** (blocker, not a trade). Exit: the blocker lapses as soon as one payment leaves baseline. Counterexamples inside this batch that must be carried with it: **C228 (-50.46%) and C106 (+120.84%)**, both of which had a perfectly flat baseline before the moment. 12 cards carried this state, 10 calm and 2 large.

**Nothing at all can be written about announcements.** Listing, delisting, warning and every other administrative decision are unobservable in all 34 cards (see Part 1). I did not "find no announcements"; the source could not be read.
