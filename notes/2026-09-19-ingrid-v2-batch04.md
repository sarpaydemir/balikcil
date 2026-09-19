# Ingrid · watcher-high · field: exchange behaviour · v2 batch 04 · round 1

- Date: 2026-09-19 · effort: high · model: opus
- Field of view: funding rate and payment interval and their changes; listing,
  delisting and warning announcements; administrative decisions of the exchange.
- Cards read: 34 of 34 in batch 04 — C249, C251, C196, C289, C201, C220, C306,
  C079, C059, C272, C269, C276, C108, C177, C179, C304, C112, C295, C266, C033,
  C191, C214, C258, C139, C061, C107, C103, C070, C180, C086, C024, C131, C163,
  C305.

## Where I looked (RULES 20)

On every one of the 34 cards I read: the `**Funding:**` line in the Before
section, the `**Funding:**` line in the After section, the
`**Exchange announcements:**` line in the Before section, and the
`## Fields not on this card` footer. For eight cards (C249, C251, C180, C139,
C107, C112, C196, C191, C276, C258) I also read the hourly table, in order to
check the BTC and ETH columns before making any claim about a coin-specific
versus a market-wide move. I did not read `data/observation/external/announcements.json`
(not named in my instruction); I report only what the cards themselves print
about it.

## Batch composition, as measured on the cards

21 cards are marked `Moment kind: large`, 13 `calm`. Coins: ZRO 8 cards, NEWT 7,
FARTCOIN 5, FHE 5, NIL 3, BCH 2, KOMA 2, OMNI 1, NOK 1.

## Notes

C249, C251, C196, C289, C201, C220, C306, C079, C059, C272, C269, C276, C108, C177, C179, C304, C112, C295, C266, C033, C191, C214, C258, C139, C061, C107, C103, C070, C180, C086, C024, C131, C163, C305 · The `Exchange announcements` line reads `MISSING` on all 34 of 34 cards, with the identical three-probe text: binance HTTP 202 zero-length body, bithumb only the 5 most recent notices with no paging, upbit HTTP 404. · This is a source failure, not an absence of announcements (RULES 21). Listing, delisting and warning announcements — roughly half of my field of view — cannot be observed at all from batch 04, and no note about them may be written in either direction. · 5

C249, C251, C196, C289, C201, C220, C306, C079, C059, C272, C269, C276, C108, C177, C179, C304, C112, C295, C266, C033, C191, C214, C258, C139, C061, C107, C103, C070, C180, C086, C024, C131, C163, C305 · Every one of the 68 funding lines (34 Before + 34 After) ends `interval changed: no`. The payment counts corroborate it: every 4 h card carries exactly 6 payments per 24 h window and every 8 h card exactly 3, with no mismatched count anywhere. · Two independent readings on the card agree, so I treat this as solid. The consequence is that the "funding interval change" signal has zero instances in these 34 cards and cannot be studied from them — a floor of 0, not evidence that the exchange never changes intervals. · 5

C033, C024, C258 · These three are the only 8 h-interval contracts in the batch (BCH twice, NOK once); the other 31 cards are all 4 h. The interval is constant per coin across that coin's cards. · Opinion: the 4 h/8 h split is a standing administrative classification of the contract, not a per-moment event, so in a blind exam where the coin name is hidden "interval = 4 h" would act as a proxy label for "smaller/newer altcoin". Anyone scoring funding should treat it as a coin attribute and not as a signal. · 4

C201, C306, C272, C179, C061, C180, C086, C305, C177, C214, C220, C079 · In 12 of the 34 cards the funding rate is exactly +0.0050% on all 12 payments (6 before + 6 after) — it never moves once in 48 hours. Eight of those 12 are large moments, with measured 24 h moves of +12.76, +19.25, -28.51, +11.35, -22.94, -30.89, -19.67 and +24.02 per cent. · A move of -30.89% (C180) or +24.02% (C305) passed through the contract without the funding series registering anything. Opinion: +0.0050% is the resting/default value of a 4 h contract (the interest component with the premium inside its dead band); I could not verify that mechanism from anything printed on the card, so it is opinion. Practical consequence: on such cards funding is an *unknown*, not a neutral reading, and a score recipe should record it on the unknowns line (RULES 31). · 5

C112, C276, C139, C266, C103, C163 · These six are the only cards where any Before-window funding payment reaches |rate| >= 0.05%. Three of them are large moments (C112 +0.1110%, C276 -0.0600%, C139 -0.3085%) out of 21 large cards; three are calm moments (C266 -0.1292%, C103 +0.1385%, C163 +0.0836%) out of 13 calm cards. That is 3/21 = 14% of large versus 3/13 = 23% of calm. · The signal is if anything commoner in the calm cards here. Opinion: an extreme funding reading in the 24 h before the moment did not flag a large move in this batch; on these counts it is an anti-signal or noise. 34 cards is far too few to settle it, but it is enough to say the effect is not large and obvious. · 4

C112, C276, C139, C266, C103, C163 · Taking those same six extreme-Before cards, the following 24 h gave +56.18%, +23.02%, -39.29%, -3.64%, -0.51% and +2.18%. The sign of the extreme funding did not pick the direction: positive funding preceded +56.18% (C112) and also -0.51% (C103) and +2.18% (C163); negative funding preceded +23.02% (C276), -39.29% (C139) and -3.64% (C266). · Opinion: the "crowded longs pay, therefore price falls" story fails on C112, where funding sat at roughly +0.07% to +0.11% per 4 h through the entire 24 h before *and* during a +56.18% rise. Six cards, both signs, both directions plus calm. · 4

C249, C196, C112, C191, C139, C107, C266, C258, C103, C163 · These ten are the only cards where any After-window payment reaches |rate| >= 0.05%: six of the 21 large cards (29%) and four of the 13 calm cards (31%). · Opinion: a funding extreme occurring *inside* the 24 h window separates large from calm essentially not at all here. And because it sits in the After section it is invisible in the exam anyway; it could only be used live, in the money test. · 4

C107, C191 · The largest funding prints arrive after the price move, not before it. C107 (FHE, -52.36%): the -0.6905% payment is the fifth of six, i.e. roughly hour +17 on the 00/04/08/12/16/20 UTC grid, after the -15.33% hour at +12 and the -28.54% hour at +13. C191 (NEWT, +30.09%): the -0.0699% payment is the sixth, roughly hour +21, immediately after the +12.52% hour at +20. · The payment hours are my inference from the standard 4 h UTC grid and are an estimate — the card prints the rates in order but not their timestamps. Opinion: on these two cards the extreme funding print is a restatement of a price move already on the chart, so it carries no information that price does not already carry. · 4

C272, C180 · These two cards share the identical start hour, 2025-10-09 22:00 UTC (ZRO -28.51%, NEWT -30.89%). On C180's After table BTC prints -0.96 and ETH -1.75 at hour +16, and BTC -2.06 / ETH -3.26 at hour +22, with the coin's own -18.59% hour at +23. So the whole market moved: by RULES 13 these two cards are one event, not two. In my field the striking part is that both contracts' funding stayed at exactly +0.0050% for all 12 payments through it. · The biggest drawdown in the batch left literally no trace in either funding series. Opinion: funding did not react to a market-wide liquidation event on these two contracts, which makes funding useless as a warning for that class of move. Two cards, and they are one event, so this is an observation about a single event. · 4

C139 · KOMA, start 2025-10-09 10:00, -39.29%. The coin printed -15.68% at hour +0 while BTC was +0.29 and ETH +0.44 — the market was not moving, so this is a coin-specific collapse, unlike C272/C180 twelve hours later. Funding here *did* react: -0.0891% and -0.3085% in the last two Before payments, and -0.3012% in the first After payment, before flipping positive (+0.0416%). · Set against C272/C180: the one card where funding printed a large negative value at the moment of a crash is the coin-specific crash, and the market-wide crash showed nothing. Opinion: attractive, but it rests on one coin-specific card versus one market-wide event, and KOMA is anyway one of the funding-lively contracts (see the next note), so the contrast may be the contract, not the event. Observation, not a rule. · 3

C108, C112, C107, C103, C131, C139, C163, C266, C276, C196 · Whether funding moves at all is largely a property of the coin, not of the moment. All 5 FHE cards (C108, C112, C107, C103, C131), both KOMA cards (C139, C163) and the single OMNI card (C266) show funding away from the default somewhere in the Before window, on calm and large moments alike. Against that: all 3 NIL cards sit pinned at +0.0050%, all 5 FARTCOIN cards stay within |0.0209%|, 6 of 7 NEWT cards are pinned (C196 the exception), and 7 of 8 ZRO cards stay within ±0.005% (C276 the exception). · Opinion: "this contract's funding is unusual" mostly decodes to "this contract is FHE, KOMA or OMNI". Any score using funding must normalise it against the coin's own funding history, or it will simply be scoring coin identity — which in a blind exam is a hidden-label leak. · 4

C033, C024 · The two BCH cards, the only large-cap contract in the batch, hold funding inside ±0.0088% on all 6 payments across both cards, including through a +12.52% large move (C033). · Two cards. Opinion: consistent with the 8 h-interval, deep-liquidity contract having almost no basis premium, so funding carries almost no dynamic range there and cannot function as a signal for it at all. · 3

C258 · NOK, 8 h interval, prints funding of exactly +0.0000% for two Before payments and two After payments (Before +0.0000% +0.0000% +0.0020%; After +0.0000% +0.0522% +0.0000%). Exact zeros appear on no other card in the batch. · Opinion: an exact 0.0000% is unlikely to be a market reading and looks like an administrative setting specific to this contract (the card also notes CoinGecko returned no coin whose symbol equals `NOK`). One card only; I flag it as a data oddity worth a second pair of eyes rather than as a signal. · 3

C249 · NIL, +27.84%, a coin-specific rise (BTC and ETH stay inside roughly ±1.3% across the whole After window). Funding runs +0.0050% +0.0050% then turns negative: -0.0029%, -0.0256%, -0.0527%, -0.0399%. Price at the third payment (roughly hour +9 on the UTC grid, an estimate) was 0.03728 and closed the window at 0.04597, a further +23%. · Opinion: funding turning negative while the coin is rising hard is counter-intuitive and is the one pattern in my field that looked like it might lead rather than lag. One card, with an inferred payment schedule. · 3

C276 · ZRO, +23.02%, with funding negative on all 6 Before payments (-0.0490 to -0.0600%) and negative on all 6 After payments. But the largest hour of the rise (+8.36% at hour +21) came with BTC +1.78 and ETH +3.87, so the final leg of this move was market-wide, not the coin's own. · Recorded because my definition requires it: part of this card's move does not belong to the coin. The funding reading itself was negative throughout and so did not change at the moment that mattered. · 4

C059, C070, C191, C289, C295, C304 · A single off-default payment inside an otherwise pinned Before window (C059 -0.0209%, C070 +0.0001%, C191 -0.0007%, C289 -0.0037%, C295 +0.0015% and +0.0046%, C304 +0.0031%) was followed by +22.72%, +21.85%, +30.09%, +19.45%, +1.02% (calm) and -5.45% (calm). · Four large and two calm out of six, against a batch base rate of 21 large in 34 (62%). Opinion: a single small funding wobble says nothing; I list it so the count exists rather than because I think it is a signal. · 3

## Idea (three parts, as required)

I have one idea that meets the trigger/direction/exit test. It is weak and I say
so.

- **Trigger:** on a 4 h-interval contract, a funding payment prints below
  -0.030% while the coin's trailing 24 h price change is >= +15%.
- **Direction:** buy (open or hold long).
- **Exit:** 24 h after entry, or at the first funding payment that prints
  >= +0.0050%, whichever comes first.
- **Rests on:** C249 (prints -0.0256% then -0.0527%; price 0.03728 at the first
  qualifying payment, 0.04597 at the window close, +23%), C196 (-0.1649% print;
  price 0.07538 to 0.08341 over the remaining 3 h, +10.7%), C191 (-0.0699%
  print; price 0.1227 to 0.1284 over the remaining 2 h, +4.6%).
- **What is wrong with it:** 3 cards out of 34. The payment hours are my
  inference from the 00/04/08/12/16/20 UTC grid and are an **estimate** — the
  cards print rates in order but not timestamps, so the trigger time is not
  measured. In C196 the funding was already negative before the window, so the
  trigger would have fired much earlier there. All three instances sit in the
  After section, which the exam never shows, so this can only ever be tested in
  the money test, not in the exam. No calm card in batch 04 produced the trigger,
  so I have no false-positive count at all. Confidence 2.

## Things I deliberately did not write as ideas

- "Funding pinned at +0.0050% before the moment." 14 of 34 cards have a Before
  window entirely at the default: 10 large (C249, C251, C201, C306, C272, C179,
  C061, C180, C086, C305) and 4 calm (C220, C079, C177, C214). 10/14 = 71%
  against a batch base rate of 21/34 = 62%. Too close to the base rate, and it
  is plainly present in calm moments, so I give no trigger.
- "Negative funding before the moment predicts direction." Killed by the cards:
  C276 -> +23.02%, C196 -> +24.09%, C139 -> -39.29%, C107 -> -52.36%,
  C266 -> calm -3.64%. Two up, two down, one calm.

## Failures and unresolved items (RULES 22)

1. Exchange announcements: unreadable on all 34 cards (source failure, three
   probes named on the card). Listing, delisting and warning announcements were
   not observed and no conclusion about them may be drawn from batch 04.
2. Funding payment timestamps are not printed on the cards, only the ordered
   rates. Any statement I make about *when within the window* a payment landed is
   an estimate from the standard UTC grid, and is marked as such above.
3. No card in batch 04 records an interval change, so the interval-change signal
   is untested, not disproven.
4. No card in batch 04 records any other administrative decision (leverage-limit
   changes, margin-tier changes, contract settlement). TACTICS section 3 states
   leverage-limit history is not on the card, so this part of my field has no
   data source at all in this design.
5. I did not read the BTC/ETH columns of C059, whose start hour (2025-10-12
   14:00) falls near the market-wide event of C272/C180, so I make no
   co-movement claim about it.
