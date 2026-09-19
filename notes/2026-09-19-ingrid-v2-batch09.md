# Ingrid · watcher-high · round 1 · batch 09 · field: exchange behaviour

Field of view: funding rate and payment interval and their changes; listing /
delisting / warning announcements; exchange administrative decisions.
34 cards read (C288 C014 C054 C006 C182 C161 C020 C142 C007 C122 C005 C074 C155
C294 C181 C216 C004 C232 C145 C078 C215 C286 C221 C032 C140 C262 C264 C120 C270
C083 C062 C162 C141 C278). Every count below is out of these 34 cards only.

Where I looked inside each card: the `**Funding:**` line of the Before section,
the `**Funding:**` line of the After section, the `**Exchange announcements:**`
line of the Before section, and the `## Fields not on this card` block. I also
read the BTC and ETH columns of the hour tables on C288 C014 C054 C006 C182 C161
C007 C020 C232 C181 C286 C004, to test whether a move was market-wide.

"24 h funding sum" below = the arithmetic sum of the payments printed on that
card's Funding line, in % per 24 h. It is computed by me from printed numbers,
not read off the card. Sums are comparable across 4 h and 8 h contracts because
both cover the same 24 h window.

---

## A · The announcement half of my field

C288 C014 C054 C006 C182 C161 C020 C142 C007 C122 C005 C074 C155 C294 C181 C216 C004 C232 C145 C078 C215 C286 C221 C032 C140 C262 C264 C120 C270 C083 C062 C162 C141 C278 · all 34 cards carry `Exchange announcements: MISSING`, with the same three-part reason on every card (binance: HTTP 202 with zero-length body; bithumb: only the 5 most recent notices, no paging; upbit: HTTP 404) · I read the announcements line on all 34 Before sections and the `Fields not on this card` block on all 34; not one card contains a listing, delisting or warning item · 5

C288 C014 C054 C006 C182 C161 C020 C142 C007 C122 C005 C074 C155 C294 C181 C216 C004 C232 C145 C078 C215 C286 C221 C032 C140 C262 C264 C120 C270 C083 C062 C162 C141 C278 · this is a fetch failure, not an absence: the cards say the source could not be reached, so I cannot say "there were no announcements in these hours" for any of the 34 · opinion: half of my assigned field has no data at all in this batch and any later claim about announcements must be sourced elsewhere, not from these cards · 5

## B · Payment interval

C288 C014 C054 C006 C182 C161 C020 C142 C122 C005 C074 C155 C294 C181 C216 C004 C232 C145 C078 C215 C286 C221 C032 C140 C262 C264 C120 C270 C083 C062 C162 C141 C278 · 33 of the 34 cards print `interval changed: no` · read directly from the Funding lines · 5

C007 · the one interval change in the batch: Before shows 12 payments, `interval 1/8 h`, `interval changed: yes`; After shows 3 payments, `interval 8 h`, `interval changed: no`. The 12 Before payments are +0.0000 ×4, then -0.0414 -0.0243 -0.1618, then +0.0000 ×5. The After move was -8.36% (moment kind: large) · read directly; opinion: `1/8 h` reads as two intervals inside one window, i.e. the contract paid hourly for part of the 24 h and 8-hourly for the rest, and the three large negative payments sit exactly in the switched stretch — but the card does not say which hours carried which interval, so I am not certain of that reading · 3

C007 · in the same 24 h after C007's start, BTC summed about -3.6% and ETH about -4.2% (my addition of the hourly BTC/ETH columns, estimate), while the coin fell -8.36% · so roughly half of this move is market-wide and does not belong to the coin · 4

C288 C294 C286 C270 C278 C182 C181 C161 C142 C155 C145 C140 C162 C141 C122 C120 C074 C078 C083 C062 C216 C232 C215 C221 · all 24 of these cards print `interval 4 h`; C054 C020 C032 C014 C006 C007 C005 C004 C262 C264 all print `interval 8 h` (C007's Before excepted, see above) · read directly · 5

C054 C020 C032 C014 C006 C007 C005 C004 C262 C264 vs the 24 above · the interval is constant per coin across every card of that coin, so in this batch the interval is a static contract attribute, not a time-varying quantity · opinion: it therefore cannot be a signal on its own, and the single exception C007 is the only place where it carries information at all · 4

C288 C294 C286 C270 C278 C182 C181 C161 C142 C155 C145 C140 C162 C141 C122 C120 C074 C078 C083 C062 C216 C232 C215 C221 C054 C020 C032 C014 C006 C007 C005 C004 C262 C264 · the interval, combined with the coin's habitual funding level, groups the cards by coin perfectly in this batch (4 h + values clustered on +0.0050%; 8 h + values clustered on +0.0000% or +0.0100%) · opinion, flagged for whoever builds the exam: since the exam hides the coin name, a reader could still cluster exam cards by coin from the funding interval alone — this is a de-anonymisation channel in my field and someone should check it · 4

## C · The modal funding value, and what it does not separate

C074 C216 C215 C221 C083 C062 C120 C278 · 8 cards where every one of the six Before payments is exactly +0.0050% — perfectly flat funding for the whole 24 h before the moment · read directly · 5

C074 C216 C215 C083 C278 (calm) vs C221 C062 C120 (large) · of those 8 flat-at-+0.0050% cards, 5 are calm moments and 3 are large; and the 3 large ones include the two biggest moves in the whole batch, C120 at -44.40% and C221 at -38.18% · opinion: completely featureless funding precedes calm moments and the batch's most violent moments alike, so flatness separates nothing here · 4

C221 · a -38.18% move over 24 h with the After funding still exactly +0.0050% at all six payments — funding did not react to the move at all · read directly; opinion: whatever clamp or index-tracking produces +0.0050% held right through a 38% collapse, which limits how much funding can ever say about this kind of move · 4

C142 C182 C270 C294 C232 C278 · values strictly between 0% and +0.0050% do occur on 4 h contracts (+0.0004, +0.0008, +0.0010/+0.0039/+0.0040, +0.0016, +0.0025, +0.0030/+0.0046) · read directly · so +0.0050% is the modal value, not a hard floor — I looked for sub-0.0050% values before saying this · 4

C014 C006 C007 C005 C262 C264 · payments of exactly +0.0000% appear only on the two 8 h contracts AVGOUSDT and NOKUSDT, on 6 cards; C006 and C264 are calm, C014 C007 C005 C262 are large · read directly · opinion: a zero funding rate is a property of those contracts, not a state of the market, and it appears on both kinds of moment so it separates nothing · 4

## D · Level of funding before the moment

C162 (+0.2517) C004 (+0.1714) C161 (+0.1161) C140 (+0.1049) · the four highest 24 h Before funding sums in the batch · two are calm (C162 +2.57%, C161 +6.78%) and two are large, and the two large ones went in opposite directions (C004 -17.27%, C140 +41.47%) · my sums from printed payments · so a high funding bill before a moment did not tell me either that a move was coming or which way · 4

C161 C142 C155 C145 C140 C162 C141 · three of the four highest Before sums, and five of the top eight, are the same coin (KOMAUSDT) · opinion: "funding is high" in this batch mostly identifies the coin rather than the moment, so any rule using an absolute funding level would really be a coin filter in disguise; it would have to be normalised per coin first · 4

C141 · the largest 24 h funding sum anywhere in the batch is +0.4883% — and it is in the After window of a **calm** card that moved +2.97% (payments +0.0502 +0.1008 +0.1445 +0.0514 +0.0305 +0.1109) · my sum from printed payments · opinion: this is the cleanest single counter-example to "extreme funding means something is happening to the price" · 4

C161 C145 C162 C007 · the four cards whose Before window contains a single payment at least ten times the contract's modal value (+0.0703, +0.0527, +0.0792, -0.1618) · three of those four are calm moments; only C007 is large · my threshold, applied to printed payments · opinion: a one-off funding spike before the moment is, in this batch, more often a calm-moment feature than a large-moment one · 3

## E · Sign of funding before the moment

C288 (-0.0037) C020 (-0.0364) C181 (-0.0360) C232 (-0.0890) C007 (-0.2275) C286 (-0.1680) · the six cards whose 24 h Before funding sum is negative · my sums from printed payments · 5

C288 C020 C181 C232 C007 (large) vs C286 (calm) · a negative Before funding sum appears in 5 of the 18 large cards and 1 of the 16 calm cards in this batch · counted over all 34 · opinion: the contrast (28% vs 6%) is the most interesting thing in my field this batch, but it catches only 5 of 18 large moments, so it is a low-recall hint at best · 3

C288 (+14.64%) C020 (+11.00%) C181 (+12.47%) C232 (+24.44%) vs C007 (-8.36%) C286 (-7.40%) · of those six negative-funding cards, four went up and two went down · in the same batch 20 of 34 cards moved up, so 4/6 = 67% against a 59% base rate is almost nothing · direction is not established by this; I am writing the base rate down precisely so nobody reads 4-out-of-6 as a result · 3

C181 · in C181's 24 h after the start, ETH summed about +9.1% and BTC about +3.4% (my addition of the hourly columns, estimate) while NEWTUSDT rose +12.47% · so most of this card's up-move is market-wide and does not belong to the coin — this weakens it as an example of "negative funding then up" · 4

C020 · in C020's 24 h after the start, BTC summed about +1.4% and ETH about +3.0% (estimate) while BCHUSDT rose +11.00% · the coin clearly outran the market here, so this one is coin-specific · 4

C232 · in C232's 24 h after the start, BTC summed about +0.3% and ETH about +0.8% (estimate) while NILUSDT rose +24.44% · the market was flat; this move belongs to the coin · 4

C288 · in C288's 24 h after the start, BTC summed about +4.4% and ETH about +6.0% (estimate) while ZROUSDT rose +14.64% · the market rose too, so part of this move is not the coin's · 4

C286 · the clearest counter-example: the most persistently negative Before funding of any calm card (all six payments negative, sum -0.1680) and the coin then fell -7.40% while BTC was about +1.0% (estimate) · read directly plus my sum · opinion: negative funding here preceded a fall against a flat market, i.e. exactly the opposite of the other five · 4

C032 · counted as positive (+0.0104) but it contains one payment of -0.0003%, which is noise at this scale · noted so that a later script using "any negative payment" instead of "negative sum" does not pick up a different card set · 3

## F · Funding during the move — measured, but not usable as a trigger

C232 · the last payment of the After window is -0.3576%, roughly 70× the contract's modal +0.0050%, and it lands in the same hours as the +6.53% / +8.67% / +2.48% up-leg at h+19..h+22 · read directly from the Funding line and the hour table · opinion: shorts paying that hard is a description of the squeeze, not a warning of it — it is printed after the move and cannot be a trigger · 5

C120 · the After window turns negative mid-way (-0.0334, -0.0946) during a -44.40% fall, having been flat at +0.0050% throughout the Before window · read directly · same caveat: this is a reaction, not a lead · 4

C004 · funding is positive and rising in both windows (Before +0.0438 +0.0520 +0.0756, After +0.0484 +0.0603 +0.1740) while the price falls -17.27% · read directly · opinion: funding rising through a crash is the opposite of the usual "crowded longs get flushed and funding collapses" story, and I have no explanation from my field alone · 3

C004 · in C004's 24 h after the start, BTC summed about -6.7% and ETH about -4.4% (estimate) while AVGOUSDT fell -17.27% · the market fell too; part of this move is not the coin's · 4

C232 C120 C221 · the three most extreme moves in the batch by size (+24.44%, -44.40%, -38.18%) produced, respectively, a huge funding blow-out, a moderate one, and none at all · counted over the three · opinion: funding's reaction to a large move is not reliable even after the fact, let alone before it · 4

## G · A duplication I have to report

C161 C162 · these two KOMAUSDT cards start 15 hours apart (2026-07-03 11:00 and 2026-07-04 02:00) and their funding sequences overlap exactly: C162's six Before payments are the last two of C161's Before plus the first four of C161's After, and C162's first two After payments are C161's last two · read directly by lining up the two Funding lines · both are calm, so counting them as two independent calm observations double-counts one stretch of hours · 5

C161 C162 · `TACTICS.md` §2 says "Of two moments closer than 48 hours to each other, only the larger counts" and separately that a calm moment must be "At least 72 hours away from any large movement" — neither sentence requires two *calm* moments to be apart from each other, so this pair is legal as written · opinion: this looks like a gap in the written rule rather than a mistake in card-making, and it is for the canteen or a juror to settle, not for me · 4

C004 C005 · these two AVGOUSDT cards start exactly 48 hours apart (2026-06-03 12:00 and 2026-06-05 12:00), both large. 48 h is not "closer than 48 hours", so they are legal; their windows abut but do not overlap and their funding lines share no payment · checked by lining up start hours and funding lines · noted only so nobody flags it later as the same problem as C161/C162 · 4

## H · An artifact I do not want mistaken for a signal

C054 C020 C032 C014 C006 C007 C005 C004 C262 C264 · 8 of the 10 cards on 8 h contracts are large moments, against 10 of the 24 cards on 4 h contracts · counted over all 34 · this is a property of how this batch was cut, not of the interval: cards per coin are drawn large-and-calm in pairs across the whole set, and my 34 cards see only a slice of each coin (AVGOUSDT arrives here as 4 large and 1 calm) · so nobody should read "8 h interval → more likely large" out of my numbers · 5

---

## Ideas (three parts each). None of these is evidence.

**Idea 1 — negative funding bill before the moment**
- Trigger: summed published funding payments over the 24 h before the moment < 0% (interval unchanged).
- Direction: buy.
- Exit: close 24 h after entry, fixed horizon, no stop.
- Seen in: 6 of 34 cards — C288 C020 C181 C232 C007 C286. Outcomes +14.64, +11.00, +12.47, +24.44, -8.36, -7.40.
- Against it: 4/6 up vs a 20/34 = 59% base rate in this batch; C181's move is mostly ETH beta; C286 is a clean counter-example; C007 is half market-wide. Worth testing as a *large-vs-calm* separator (5/18 large, 1/16 calm) rather than as a direction rule.
- My confidence: 2.

**Idea 2 — payment-interval change in the before window**
- Trigger: the before window reports `interval changed: yes`.
- Direction: sell.
- Exit: close 24 h after entry.
- Seen in: 1 of 34 cards — C007, which moved -8.36%.
- Against it: n = 1, and BTC/ETH fell about 3.6%/4.2% in the same hours, so a good part of that -8.36% is not the coin's. This is an observation, not a rule; I write it in three parts only so it is testable when more cards exist.
- My confidence: 1.

## Things I could not do, named

- Listing / delisting / warning announcements and any other exchange administrative decision: **no data on any of the 34 cards.** Source unreachable (binance HTTP 202 empty body; bithumb 5 most recent notices only; upbit HTTP 404). This is a technical failure, not a finding of "nothing happened" (RULES 20, 21).
- The probe log the cards point to (`data/observation/external/announcements.json`) is outside what this instruction lets me open, so I could not check whether any window was ever successfully covered.
- C007's `interval 1/8 h`: the card does not say which hours were on 1 h and which on 8 h, so I could not place the three large negative payments against the interval switch. Unresolved.
- BTC/ETH co-movement was checked by adding hourly percentage columns by eye on 12 cards only (listed at the top); those sums are estimates and are labelled as such. I did not check the other 22 cards for market-wide co-movement.
