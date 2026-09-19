# Ingrid · watcher-high · field: exchange behaviour · round 1 · batch 01 of 09

Field of view: funding rate and its changes; funding payment interval and its
changes; listing / delisting / warning announcements; administrative decisions
of the exchange.

Cards read: 34 of 34 in batch 01 — C167, C285, C100, C057, C077, C119, C259,
C009, C025, C153, C063, C231, C048, C279, C171, C281, C287, C102, C042, C185,
C130, C041, C044, C212, C273, C075, C203, C035, C040, C117, C053, C261, C105,
C158.

Where I looked, per card: the `Funding:` line of the **Before** section, the
`Funding:` line of the **After** section, the `Exchange announcements:` line of
the **Before** section, and the `Fields not on this card` list. Context taken
from the header (`coin`, `start hour`), the `Previous 7 days` line, the
`Moment kind` line and the `Measured 24-hour move` line.

Counts below are **out of the 34 cards of batch 01 only**. They are floors, not
counts over the 306-card set.

Batch composition I measured, for reading the counts: 17 cards marked
`Moment kind: large`, 17 marked `calm`. Nine coins: BCH 8 cards, FHE 6, ZRO 5,
KOMA 4, FARTCOIN 4, NEWT 3, NOK 2, AVGO 1, NIL 1.

Format: `card no · what I saw · why I think so · how sure I am (1-5)`

---

## A. Announcements — the source is absent, not empty

C167, C285, C100, C057, C077, C119, C259, C009, C025, C153, C063, C231, C048, C279, C171, C281, C287, C102, C042, C185, C130, C041, C044, C212, C273, C075, C203, C035, C040, C117, C053, C261, C105, C158 · all 34 cards carry the identical line "Exchange announcements: MISSING - no announcement source could be reached: binance: HTTP 202 with a zero-length body; bithumb: returns only the most recent 5 notices ... no history for the period; upbit: HTTP 404 Not Found", and the same entry repeated in "Fields not on this card" · opinion: this is a fetch failure of all three sources, not an observation that no announcement happened; two thirds of my field of view (listing, delisting, warning; any administrative decision published as a notice) therefore has zero data in batch 01 and no rule resting on announcements can be built or tested from these cards · 5

C167, C285, C100, C057, C077, C119, C259, C009, C025, C153, C063, C231, C048, C279, C171, C281, C287, C102, C042, C185, C130, C041, C044, C212, C273, C075, C203, C035, C040, C117, C053, C261, C105, C158 · the failure text is byte-identical on every card, including the probe-log path `data/observation/external/announcements.json` · opinion: the announcement fetch was run once for the whole period rather than per card, so the absence is uniform and carries no per-card meaning at all — it cannot even be used as a "data was unavailable that day" flag · 4

C167, C285, C100, C057, C077, C119, C259, C009, C025, C153, C063, C231, C048, C279, C171, C281, C287, C102, C042, C185, C130, C041, C044, C212, C273, C075, C203, C035, C040, C117, C053, C261, C105, C158 · in 0 of 34 cards did I find any other administrative item in my field — no leverage-limit change, no margin-tier change, no trading-halt note, no symbol rename, no settlement note; TACTICS section 3 already states the leverage-limit history is not on the card · opinion: within batch 01 "exchange administrative decision" reduces in practice to funding rate and funding interval, and nothing else · 5

## B. Payment interval — a stable per-contract label, with zero change events

C167, C285, C100, C057, C077, C119, C259, C009, C025, C153, C063, C231, C048, C279, C171, C281, C287, C102, C042, C185, C130, C041, C044, C212, C273, C075, C203, C035, C040, C117, C053, C261, C105, C158 · every one of the 68 funding lines (34 Before + 34 After) ends "interval changed: no"; payment counts are consistent with the stated interval in all 68 lines (6 payments at 4 h, 3 payments at 8 h), so no interval switch is hidden inside a window either · opinion: the field is present and populated, unlike the announcements field — it simply holds no event; a signal with zero events in 34 cards cannot contribute anything here, and this is an observation about the batch, not evidence that interval changes never matter · 5

C167, C153, C171, C158 (KOMA), C285, C279, C281, C287, C273 (ZRO), C100, C119, C102, C130, C117, C105 (FHE), C057, C077, C063, C075 (FARTCOIN), C185, C212, C203 (NEWT), C231 (NIL) all show interval 4 h; C025, C048, C042, C041, C044, C035, C040, C053 (BCH), C259, C261 (NOK), C009 (AVGO) all show interval 8 h · the interval is constant per coin across every card of that coin, spanning 2025-10-06 (C057) to 2026-08-06 (C171) — e.g. BCH is 8 h on all 8 of its cards from 2025-11-18 to 2026-08-04, FHE is 4 h on all 6 of its cards from 2025-10-17 to 2026-07-13 · opinion: the interval is a contract-level parameter the exchange set once, so it identifies the contract class rather than the moment; it will be the same value on every exam card of the same hidden coin · 5

C025, C048, C044, C261, C009 (8 h, large) vs C285, C100, C077, C153, C063, C279, C171, C281, C273, C117, C105, C158 (4 h, large) · among the 17 large moments the measured 24-hour move is 8.82%-14.36% in absolute size for all 5 on 8 h contracts, and 15.95%-103.98% for all 12 on 4 h contracts — the two ranges do not overlap in this batch; the calm moments split the same way (8 h calm: 0.23%-3.85% over C042, C041, C035, C040, C053, C259; 4 h calm: 0.50%-8.84% over C167, C057, C119, C231, C287, C102, C185, C130, C212, C075, C203) · opinion: the interval rescales what "large" means for that contract, so it is a calibration input rather than a trigger; 17 large cards is a small base and the split rests on only 5 cards on the 8 h side · 4

C212 (4 h, previous-7-day range 8.27%), C203 (4 h, 13.77%) vs C048 (8 h, 19.71%), C261 (8 h, 21.55%) · the interval label is not simply a restatement of recent realised range: two 4 h contracts show a 7-day range smaller than two 8 h contracts · opinion: the interval adds a stable contract-class fact that a single 7-day window can misstate, which is the one part of my field that is not readable off the price table · 3

C048 (BCH, 8 h, start 2026-06-14 15:00, large +13.16%) and C203 (NEWT, 4 h, start 2026-06-14 12:00, calm +1.94%) · two cards whose 24-hour windows overlap by 21 hours carry opposite moment kinds · opinion: whatever moved the market in those shared hours did not by itself decide the outcome, so this pair argues against reading either card's outcome as a whole-market event (RULES 13); I did not measure the BTC/ETH columns of these two cards, that is another watcher's field · 3

## C. The default funding value, and how often funding says nothing

C100, C077, C119, C102, C130, C063, C075, C203, C117 · in these 9 cards every one of the 6 before-window payments is exactly +0.0050%, the 4 h default; the moment that followed was large in 4 of them (C100 +103.98%, C077 +26.38%, C063 -26.31%, C117 +34.69%) and calm in 5 (C119, C102, C130, C075, C203) · opinion: 4 large / 5 calm is the batch base rate almost exactly (17/17), so "funding sitting at the default through the whole before window" tells nothing about whether a large move follows, and nothing about its direction either (2 of the 4 large ones went up, 2 down) · 4

C053 (+0.0100% +0.0100% +0.0100% before), C041 (+0.0046% +0.0100% +0.0100% before) · on the 8 h contracts the repeated value is exactly +0.0100%, twice the +0.0050% seen on 4 h contracts · opinion: the default is the interest-rate component scaled by interval, so +0.0050% at 4 h and +0.0100% at 8 h both mean "no premium"; any rule using a raw funding threshold must scale it by interval or it will read the two contract classes on different scales · 4

C077 (large, +26.38%), C117 (large, +34.69%), C261 (large, -13.33%) · in these 3 of the 17 large cards every funding payment in both the before and the after window is one identical constant (+0.0050%, +0.0050%, 0.0000% respectively) — funding did not move at all through a move of 13% to 35% · opinion: funding can be completely inert across a large move, so its absence of movement is not evidence of a calm market; the same flat state also appears in 4 calm cards (C119, C102, C130, C075) · 4

C100 · price rose +103.98% over the after window yet 5 of the 6 after-payments are the +0.0050% default and only the last prints +0.0195% · opinion: funding reacts late — the card's own after table shows the bulk of the move in the final hours — so funding is a lagging measure of a move that price has already shown; this is the clearest single case in the batch of funding adding nothing price had not already said · 5

C259 · every before-payment is exactly 0.0000% and the after window carries 0.0000%, +0.0650%, 0.0000% · opinion: an exactly-zero print is a different state from the +0.0100% 8 h default and looks like the exchange publishing a zero rate on this contract rather than a computed near-zero premium · 3

C261, C259 (NOK), C009 (AVGO) · exact 0.0000% prints occur only on these 2 coins (3 cards): NOK is 0.0000% on all 12 payments across both cards, AVGO is 0.0000% on the first before-payment and on all 3 after-payments · opinion: these two symbols match equity tickers and behave unlike the crypto perps in the batch; whatever the cause, on NOK the funding field carried no information whatsoever, before or after, including across the -13.33% large move of C261 · 3

## D. Funding level before the moment — what it did and did not separate

C279 (before sum -0.0693%, after +19.62%), C273 (-0.0608%, +15.95%), C044 (-0.0853%, -14.36%), C185 (-0.1776%, calm -0.50%) · these are the only 4 cards of 34 whose before-window funding payments sum to -0.05% or lower; 3 of the 4 are large moments but the directions split 2 up / 1 down, and the single most negative card in the whole batch (C185) is a calm one · opinion: persistently negative funding is weakly associated with a large move here but says nothing about direction, and 4 cards is far too few to call it anything but an observation · 3

C171 (before sum +0.1141%, after -17.43%), C105 (+0.1280%, +50.56%), C158 (+0.0905%, +25.93%) · these are the 3 cards whose before-window funding sums to +0.09% or more; all 3 are large moments, but the move went down in 1 and up in 2 · opinion: the popular reading "crowded longs pay funding, therefore price falls" holds in 1 of these 3 cards in batch 01; I would not carry it forward as a direction rule on this evidence · 3

C167 · a single before-window payment of +0.0686%, about 13.7x the 4 h default, on a moment marked calm (+3.14%) · opinion: this is the cleanest counter-example in the batch to reading a funding spike as a warning of a large move, and it matters precisely because nothing happened afterwards · 4

C167, C105, C171, C158, C044, C185 · these 6 cards contain at least one before-window payment of absolute size 0.030% or more; 4 are large (C105, C171, C158, C044) and 2 are calm (C167, C185) · opinion: 4 of 6 against a batch base rate of 17 of 34 is a lift I would not trust at n=6; write it down as a candidate to be counted properly across the whole set, not as a finding · 3

C281 (before +0.0044 ... -0.0061, large -19.29%), C048 (+0.0071 +0.0041 -0.0082, large +13.16%), C212 (-0.0089 -0.0194 then four +0.0050%, calm -4.64%), C273 (+0.0019 then five negative, large +15.95%), C025 (-0.0036 +0.0024 -0.0003, large -10.44%), C042 (-0.0008 +0.0094 +0.0028, calm -0.23%), C035 (-0.0006 +0.0037 +0.0071, calm -0.36%), C231 (-0.0067 then five positive, calm -1.84%) · I looked for a sign flip inside the before window (first payment and last payment of opposite sign) as a trigger: it occurs in these 8 cards, 4 large and 4 calm, and among the large ones the subsequent direction goes both ways · opinion: no pattern; recording it so nobody spends the same hours again · 3

## E. Funding in the after window — mostly a lagging echo of price

C285, C100, C025, C063, C171, C281, C273, C105, C158 (funding sum moved the same way as price) vs C009, C153, C048, C279, C044 (opposite way) vs C077, C117, C261 (no change at all) · across the 17 large cards I compared the sign of [sum of after-window payments minus sum of before-window payments] with the sign of the measured 24-hour move: same sign in 9, opposite in 5, unchanged in 3 · opinion: 9 of 17 is close to a coin flip, so funding does not even reliably restate the direction of a move that has already happened; this weakens any recipe that uses funding as a confirmation signal · 4

C105 · funding rises monotonically through the after window, +0.0050 +0.0050 +0.0394 +0.0422 +0.0526 +0.0614, alongside +50.56% · opinion: this is the one card where funding behaves like the textbook picture of a perp-led rally, and it is a single card · 4

C279 · funding is negative on all 6 before payments and deepens to -0.0322 -0.0342 -0.0265 -0.0181 -0.0245 -0.0054 through the after window while price rises +19.62%; C273 and C285 (same coin) also rise with funding staying negative · opinion: in these three ZRO cards the perp stayed at a discount through a large rally, which is the opposite of the usual picture and suggests the rally was not perp-led; it is one coin, so I write it as a coin-level quirk, not a rule · 3

C158 · a single after-window payment of +0.1691%, the largest absolute funding value anywhere in batch 01, on a +25.93% move · opinion: worth recording as the batch maximum so later counts have a scale reference · 4

C063 · funding flips from a flat +0.0050% before to -0.0011 +0.0050 -0.0017 -0.0149 -0.0236 -0.0149 after, alongside -26.31% · opinion: funding followed the price down rather than leading it, consistent with the lag seen in C100 · 4

C044 · the most negative 8 h before-window in the batch (-0.0310 -0.0317 -0.0226) stayed negative and deepened (-0.0151 -0.0195 -0.0305) while price fell -14.36% · opinion: this is the card that breaks "negative funding means the squeeze goes up"; keep it beside C279 and C273 when the direction question is counted · 4

## F. Ideas (trigger · direction · exit) and things that are only observations

IDEA-1 · trigger: the sum of the funding payments in the 24 h before the start hour is <= -0.05% (persistent discount), on a contract of either interval · direction: buy · exit: close 24 h after entry, or earlier at the first funding payment that prints >= the contract default (+0.0050% at 4 h, +0.0100% at 8 h) · in-batch record, stated so it is not mistaken for evidence: fires on 4 of 34 cards — C279 +19.62%, C273 +15.95%, C044 -14.36%, C185 -0.50% · 2

IDEA-2 · trigger: a 4 h-interval contract where at least one before-window payment is >= +0.030% AND the before-window sum is >= +0.09% · direction: sell · exit: close 24 h after entry, or earlier at the first payment that prints back at the +0.0050% default · in-batch record: fires on 3 of 34 cards — C171 -17.43% (correct), C158 +25.93% (wrong), C105 +50.56% (wrong), i.e. 1 of 3 · 1

OBSERVATION, not an idea (no direction, so it cannot be a trade) · C025, C048, C044, C261, C009 vs C285, C100, C077, C153, C063, C279, C171, C281, C273, C117, C105, C158 · read the funding interval off the card (3 payments per 24 h = 8 h, 6 = 4 h) and use it to set the size threshold at which a move counts as "large" for that contract: in batch 01 no 8 h card exceeded 14.36% and no 4 h large card fell below 15.95% · opinion: this is the single most useful thing my field produced in this batch and it is a calibration, not a signal · 4

## G. What I could not do

- I could not evaluate listing / delisting / warning announcements on any card: the source line is MISSING on all 34 (section A). This is a technical failure, not a result (RULES 21), and not a statement that no announcement occurred in these hours.
- I could not evaluate payment-interval changes as a signal: the field is present and populated on all 34 cards and records "no" every time (section B). Zero events, so no rule can be scored either way.
- I did not read the hourly price, volume, open-interest, long/short, depth, Wikipedia or prediction-market fields as subjects of a note; they are other watchers' fields. Where I needed context I used only the header, the `Previous 7 days` line, the `Moment kind` line and the `Measured 24-hour move` line.
- I did not measure the BTC and ETH columns, so where the whole-market question arises (RULES 13) I have flagged it rather than answered it — see the C048/C203 note in section B.
