# Ingrid · watcher-high · round 1 · batch 03 · 2026-09-19

Field of view: exchange behaviour — funding rate and payment-interval changes;
listing / delisting / warning announcements; administrative decisions of the exchange.

Cards read: 34 of 34 in batch 03 (C096, C064, C299, C280, C246, C300, C125, C011,
C248, C094, C234, C243, C189, C001, C129, C149, C218, C178, C099, C227, C090, C010,
C268, C113, C132, C207, C097, C144, C198, C137, C290, C254, C159, C250).

Batch composition as measured from the cards: 18 large moments, 16 calm moments.
Coins present: FHEUSDT (7 cards), NILUSDT (8), ZROUSDT (5), NEWTUSDT (4),
KOMAUSDT (4), FARTCOINUSDT (3), AVGOUSDT (3).
All counts below are out of these 34 cards only. They are a floor, not a count over the set.

Where I looked on each card: the `Exchange announcements` line in the Before section,
the `Funding:` line in both the Before and the After section, and the
`Fields not on this card` block at the foot.

---

## A · Announcements and administrative decisions

C096, C064, C299, C280, C246, C300, C125, C011, C248, C094, C234, C243, C189, C001, C129, C149, C218, C178, C099, C227, C090, C010, C268, C113, C132, C207, C097, C144, C198, C137, C290, C254, C159, C250 · the `Exchange announcements` line reads `MISSING` on all 34 cards, with byte-identical reason text: binance HTTP 202 with a zero-length body, bithumb returns only the most recent 5 notices with no working paging, upbit HTTP 404 · my opinion: this is one upstream fetch failure repeated 34 times, not 34 findings; listing / delisting / warning announcements are therefore **unobservable** in this batch and no statement about them can be made either way · 5

C096 … C250 (all 34) · the same MISSING line is repeated verbatim in the `Fields not on this card` block of every card, naming the same three hosts · my opinion: the card generator records the failure twice, so I have two independent confirmations per card that the source failed rather than returned an empty result · 5

C096, C064, C299, C280, C246, C300, C125, C011, C248, C094, C234, C243, C189, C001, C129, C149, C218, C178, C099, C227, C090, C010, C268, C113, C132, C207, C097, C144, C198, C137, C290, C254, C159, C250 · no card carries any other administrative field — no leverage-limit change, no margin-tier change, no trading-halt or price-cap note; the only administrative quantities on the card are the funding rate and the payment interval · my opinion: two thirds of my stated field of view has no data channel on these cards at all, and this is a structural gap, not a null result · 5

---

## B · Payment interval

C096 … C250 (all 34 cards, both the Before and the After line) · every funding line ends `interval changed: no` — 68 readings, zero changes · my opinion: the payment-interval-change signal has **zero variation** in this batch, so it cannot discriminate anything here and should not be given score weight until a card is found where it reads `yes` · 5

C011, C001, C010 (AVGOUSDT) · interval 8 h, 3 payments per 24 h · all other 31 cards: interval 4 h, 6 payments per 24 h · my opinion: this is a standing contract-class setting fixed per symbol, not a decision taken inside the card window; it tells you which product you are looking at, not what is about to happen · 5

C207 (NEWTUSDT, 2026-06-24 14:00) · the Before section lists **5** payments at interval 4 h while flagging `interval changed: no`; 24 h / 4 h = 6, and the After section of the same card lists 6 · every other 4 h card in the batch lists exactly 6 before and 6 after · my opinion: either a window-alignment artefact at the edge of the 24 h span or a genuinely absent payment record; 1 card out of 34, worth a data check before anyone builds a rule on payment counts · 3

---

## C · Funding level — what it does and does not separate

C064, C299, C248, C234, C243, C218, C178, C227, C090, C268, C250 · the Before window is pinned at exactly +0.0050% on all six payments (11 cards) · of these 11, **7 are large moments and 4 are calm** (large: C064 +28.14%, C299 +29.86%, C243 +140.96%, C178 -12.90%, C227 +28.70%, C090 +21.28%, C250 +25.48% · calm: C248, C234, C218, C268) · against the batch base rate of 18 large / 16 calm this is 64% vs 53% · my opinion: a flat-at-floor funding window is **not** a calm-market tell and must not be scored as one; this is the single most common pattern in my field and it is uninformative · 4

C280, C300, C189, C207, C254, C159, C144 · the Before window contains at least one negative payment (7 cards): 4 large (C280, C207, C254, C159), 3 calm (C300, C189, C144) · my opinion: "funding turned negative" on its own is also close to the base rate and does not separate the two kinds · 4

C125 (+0.0801% max), C113 (+0.0486%), C144 (+0.0935%), C137 (+0.0858%) · the four cards whose Before window reaches +0.0400% or more (8× the floor) split **2 large / 2 calm**, and the two large ones went in opposite directions (C125 +85.61%, C113 -41.43%) · my opinion: "hot funding precedes a fall" is not supported here — it fails on direction and it fails on separation · 4

C178, C207, C290, C159 · four of the six large **down** moves in the batch had a Before window whose highest payment was the +0.0050% floor (C178 -12.90%, C207 -11.44%, C290 -21.49% max +0.0050%, C159 -16.57% max +0.0050%) · only C099 (-48.49%, max +0.0293%) and C113 (-41.43%, max +0.0486%) had elevated funding beforehand · my opinion: most of the large falls in this batch arrived with funding sitting at its floor, i.e. with no warning at all from my field · 4

C064, C299, C227, C090, C250 · in five large up-moves of +21% to +30% the funding rate never left the +0.0050% floor across the whole 24 h **after** window either (C090's last payment +0.0085% is the only departure) · my opinion: funding is a clamped, 4-hourly quantity and a 20–30% single-day rally can pass through it without registering anything; its time resolution is poor for these events · 4

---

## D · Funding is not simply price restated

C280 (prev 7 d +15.10%, funding 5 of 6 negative), C159 (prev 7 d +28.41%, two payments at -0.0353% and -0.0649%), C254 (prev 7 d +9.06%, two negative), C137 (prev 7 d **-15.54%**, funding hot at +0.0858% and +0.0699%), C227 (prev 7 d -18.27%, funding flat at floor), C178 (prev 7 d -9.86%, funding flat at floor) · funding sign and the previous week's price direction point opposite ways in these 6 cards · my opinion: funding here is **not** a restatement of recent price — it is derived from the perp-vs-index premium, which can sit on the other side of the tape; that makes it worth carrying as a separate field even though it separated nothing in section C · 4

C137, C144, C149, C159 (KOMAUSDT, avg hourly volume on these cards 18.39k / 22.79k / 122.99k / 135.39k) · this is the thinnest coin in the batch and it holds both the batch's largest positive payment (+0.0952%, C159 after) and its largest negative before-payment (-0.0649%, C159 before), and none of its four Before windows sits at the floor · its four cards are 2 large / 2 calm · my opinion: funding **swing size is a liquidity property of the symbol, not a property of the moment**; any absolute funding threshold in a score recipe would fire mostly on the thinnest coin regardless of what follows, and should be normalised per coin or not used · 4

C218, C227, C234, C243, C248, C250 (NILUSDT) · 6 of 8 NIL cards have a Before window pinned at the floor, across 3 large and 3 calm moments including a +140.96% move (C243) · my opinion: same point from the other side — a coin can sit at the floor through everything · 4

---

## E · Single-card things I saw

C280 (ZROUSDT, 2026-01-22 17:00, large, +24.31%) · the only card in the batch in which the +0.0050% floor value never appears: 11 of its 12 listed payments are negative, deepening from +0.0021% through -0.0181% before the start and running -0.0140% to -0.0412% after it · BTC/ETH hourly moves in the after window never exceed +0.83%/+1.25%, so **the move was the coin's own, not a market-wide event** · my opinion: sustained negative funding with the perp below index while price rises 24% is the textbook crowded-short picture, but it is **1 card out of 34** and is an observation, not a rule · 3

C243 (NILUSDT, 2026-05-06, large, +140.96%) · funding in the after window went to -0.0037%, -0.0592%, -0.0275% in the middle of a +141% rally before returning to the floor · BTC/ETH hourly moves stay inside ±0.93% throughout, so this is coin-specific · my opinion: during a vertical move the premium index can invert against the direction of travel; a rule that reads "negative funding = shorts crowded" would be reading noise here · 3

C254 (NILUSDT, 2026-08-28, large, +29.19%) · holds the batch's most negative payment, -0.0598%, and it falls in the **after** window (the before window is near-flat) · BTC/ETH hourly moves inside ±0.70% · my opinion: this is contemporaneous with the move and therefore unusable as a trigger — I note it only so nobody mistakes an after-window reading for a signal · 4

C207 (NEWTUSDT, 2026-06-24, large, -11.44%) · the two last Before payments are -0.0096% and -0.0330% and the After window deepens to -0.0446% · **but** BTC fell -1.36%, -0.74%, -0.74% and ETH -1.78%, -1.76%, -1.87% over hours +1..+3, and the hour at +23 is BTC -4.85% / ETH -5.99% · my opinion: a large part of this move is market-wide and does not belong to the coin · 4

C207 (+23 h) and C300 (h-15) · both cards carry the identical market hour BTC -4.85% / ETH -5.99%; C207 starts 2026-06-24 14:00 so its +23 is 2026-06-25 13:00, and C300 starts 2026-06-26 04:00 so its h-15 is the same 2026-06-25 13:00 · my opinion: one market-wide event appearing inside two cards of this batch — under RULES 13 it must be counted once, and I flag it because it sits inside a window I am drawing a funding conclusion from · 4

C113 (FHEUSDT, 2026-01-20, large, -41.43%, previous 7 days **+370.81%**) · the Before window is elevated throughout (+0.0462%, +0.0401%, +0.0486%) and the After window falls back to +0.0050%..+0.0260% · BTC/ETH hourly moves stay inside ±1.79%, so the -41% is the coin's own · my opinion: the most extended card in the batch by prior-week move is also one of only two large cards with hot funding beforehand — suggestive, but it is 1 card and its twin C125 (hot funding, +20.70% prior week) went the other way at +85.61% · 2

C010 and C011 (AVGOUSDT, both calm, same day 2026-07-16, starts 00:00 and 14:00) · the two windows overlap by 10 hours · my opinion: these two funding readings are not independent and should count nearer to one than to two in any tally · 4

C001, C010, C011 (AVGOUSDT) · every Before payment is exactly +0.0000% (9 payments across 3 cards); the only non-zero readings anywhere are +0.0015% (C011 after) and +0.0270% (C001 after) · all three cards are calm moments with 24 h moves of -4.24%, +4.19% and -4.87% · my opinion: an 8 h / 0.0000% contract looks like a different product class whose moments are much smaller, but I saw only 3 such cards and all three were calm, so I cannot tell a property of the product from an accident of the draw · 3

---

## F · Ideas (trigger · direction · exit)

**Idea 1 — deep negative last payment (weak, rests on 2 cards).**
Trigger: on a 4 h-interval contract, the last funding payment of the 24 h before the moment is at or below -0.0300% while the earlier payments of that window were at or above the +0.0050% floor.
Direction: sell.
Exit: close 24 h after entry, or earlier at the first funding payment that comes back to +0.0050% or above, whichever is first.
Seen in C207 (-11.44%) and C159 (-16.57%), both large down moves; 2 of 34 cards. Counter-case in the same batch: C254's last before-payment is also negative (-0.0006%) and the move was +29.19% up, so the whole idea hangs on the -0.0300% threshold, which I chose after looking. Treat as an observation-shaped idea, confidence 2, and note that C207's move is partly market-wide (see section E).

**Idea 2 — a blocker, not a signal (rests on 3 cards).**
Proposed blocker: a contract with an 8 h interval and funding of exactly +0.0000% (the AVGOUSDT class here) is excluded from any funding-based rule.
Direction / exit: not applicable — this is a blocker in the RULES 31 sense, not a trade.
Seen in C001, C010, C011; 3 of 34 cards, all calm, all with 24 h moves under 5%. Three cards cannot establish it; I write it so it can be tested, not because I believe it.

**Not an idea — a "do not score" finding.**
"Before-window funding pinned at +0.0050%" fires on 11 of 34 cards and splits 7 large / 4 calm against a 18/16 base rate (section C). It has no trigger worth writing because it should carry **zero** weight in a score recipe. Same for "before-window funding contains a negative payment" (7 cards, 4 large / 3 calm).

---

## G · What I could not measure, by name

1. Listing, delisting and warning announcements — no data on any of the 34 cards; source failure, not absence (section A). Nothing in my field can be said about them.
2. Administrative decisions other than funding rate and interval — no field exists on the card for them (leverage limits, margin tiers, halts, price caps). TACTICS 3 already says the history of leverage limits is not on the card; I confirm nothing else administrative is either.
3. Payment-interval changes — the field exists and is readable, but reads `no` in all 68 readings, so it is untested rather than tested-and-null.
4. **Ordering assumption, unresolved:** the card prints the payments as `rate a b c d e f` with no timestamps and no statement of order. I have read them as oldest-to-newest. Idea 1 depends entirely on that reading. If the order is newest-first, Idea 1 inverts. This needs settling before anyone tests it.
5. **Timing assumption, unresolved:** there are no payment clock times on the card, so I cannot tell whether the last before-payment fell 10 minutes or 4 hours before the start hour. RULES 16 forbids filling at a known-in-advance moment's open price, so any funding-timed rule needs those timestamps that the card does not carry.
6. Whether the AVGOUSDT product class genuinely has smaller moments, or whether the draw simply handed me 3 calm cards for it (section E).
