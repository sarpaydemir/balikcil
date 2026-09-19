# Ingrid · watcher-high · field of view: exchange behaviour · round 1 · batch 02

Field of view: **changes in the funding rate and the payment interval; listing,
delisting and warning announcements; every administrative decision the exchange
takes.** Nothing else on the card is mine to report.

Cards read: 34 of 34 in batch 02 —
C244, C240, C233, C283, C298, C154, C282, C080, C303, C235, C257, C088, C176,
C116, C184, C135, C204, C219, C148, C143, C296, C016, C069, C224, C018, C293,
C065, C174, C046, C211, C291, C049, C022, C183.

Every count below is **out of these 34 cards only**. It is a floor, not a count
over the set.

Composition of what I read, for the reader's arithmetic: **15 large, 19 calm.**
large = C244 C283 C282 C088 C116 C184 C219 C296 C069 C018 C065 C174 C046 C049 C183
calm  = C240 C233 C298 C154 C080 C303 C235 C257 C176 C135 C204 C148 C143 C016 C224 C293 C211 C291 C022

Where I looked for each note: the **Funding** line in the Before section and in
the After section, the **Exchange announcements** line in the Before section,
and the **Fields not on this card** list, of each of the 34 cards named above.

Format: `card no · what I saw · why I think so · how sure I am (1–5)`

---

## A · Failures in my field (these are failures, not results)

C244, C240, C233, C283, C298, C154, C282, C080, C303, C235, C257, C088, C176, C116, C184, C135, C204, C219, C148, C143, C296, C016, C069, C224, C018, C293, C065, C174, C046, C211, C291, C049, C022, C183 · the **Exchange announcements** field is `MISSING` on all 34 of 34 cards, with byte-identical reason text on each: binance HTTP 202 with a zero-length body; bithumb returns only the 5 most recent notices and no paging parameter changed it; upbit HTTP 404 · opinion: this is one upstream fetch failure repeated 34 times, not 34 separate "nothings" — so listing / delisting / warning announcements are **unmeasured** in batch 02 and I can say nothing at all about them, in either direction · 5

C244 … C183 (all 34) · the `Fields not on this card` block on every card repeats the same announcement failure, and TACTICS §3 states outright that **the history of leverage limits is not on the card** · opinion: the "administrative decision" half of my field is therefore **structurally empty**, not accidentally empty — the card format as designed carries no leverage tier, no margin-tier change, no trading-halt field · 5

## B · Payment interval — every observation I have

C244, C240, C233, C283, C298, C154, C282, C080, C303, C235, C257, C088, C176, C116, C184, C135, C204, C219, C148, C143, C296, C016, C069, C224, C018, C293, C065, C174, C046, C211, C291, C049, C022, C183 · `interval changed: no` on **all 34 cards, in both the Before and the After section — 68 statements, zero changes** · opinion: the interval-change signal has **no events at all** in batch 02, so it can be neither confirmed nor refuted here; anyone scoring it from this batch is scoring an empty cell · 5

C016, C018, C022, C046, C049, C257 · interval **8 h**, 3 payments per 24-hour window, on every one of these cards (BCH ×5, NOK ×1) · —— · 5

C244, C240, C233, C283, C298, C154, C282, C080, C303, C235, C088, C176, C116, C184, C135, C204, C219, C148, C143, C296, C069, C224, C293, C065, C174, C211, C291, C183 · interval **4 h**, 6 payments per 24-hour window, on all 28 of these · opinion: interval in this batch is a **static per-coin property**, constant across every card of a given coin, never an event — so it can only ever act as a coin label, never as a timing signal · 4

C244 … C183 (all 34) · payment counts are exactly 6 (4 h coins) or exactly 3 (8 h coins) in both windows on every card; no card shows a skipped, doubled or irregular payment · opinion: no funding-schedule irregularity of any kind occurred in batch 02 · 4

## C · The base rate is a clamp, and on 12 cards it swallows the whole field

C080, C088, C176, C204, C219, C224, C065, C069, C296, C303, C211, C183 · all six Before-window payments print exactly **+0.0050%** — Binance's base funding rate (0.01% per 8 h expressed per 4 h) · opinion: when funding sits pinned on the base rate it is telling me the perp premium stayed inside the clamp band and nothing more; for these 12 cards my field is **blank**, not calm · 4

C088, C219, C065, C069, C296, C183 (large) vs C080, C176, C204, C224, C303, C211 (calm) · of those same 12 pinned-at-base cards, **6 are large moments and 6 are calm** — 6 of 15 large (40%) against 6 of 19 calm (32%) · opinion: a flat +0.0050% Before window separates nothing; this is the clearest negative result I have and it rests on 12 cards, the largest group in my batch · 4

C065, C069, C080, C088 · FARTCOIN's Before funding is pinned at +0.0050% on **4 of its 4 cards**, across moves of +21.05%, +19.80%, +4.43% and +23.20% · opinion: for this coin the funding field carried no information whatever in batch 02, whatever happened next · 4

C176, C183, C204, C211 (pinned) vs C184 (not pinned) · NEWT is pinned at base on 4 of its 5 cards · —— · 4

C135, C143, C148, C154, C174 · KOMA is the opposite case: **not one** of its 5 cards is pinned, and its Before payments swing from -0.0762% to +0.1146% · opinion: funding "informativeness" is mostly a coin property here, so any threshold rule built on absolute funding levels will really be selecting coins, not moments · 3

## D · Funding level in the Before window vs what followed

C148 (+0.1146%, calm -5.88%), C143 (+0.1067%, calm -2.09%), C154 (+0.0718%, calm -4.49%), C257 (+0.0568%, calm -1.00%) · the four cards whose largest Before payment exceeds **+0.05%** are **all four calm** · opinion: this looks like a signal and is not one — 3 of the 4 are KOMA and the fourth is NOK, so it is two coins, not four independent events; I would not carry it forward without coins outside this batch · 2

C174 · KOMA, Before payments +0.0050 +0.0198 +0.0176 +0.0434 +0.0489 +0.0244, i.e. elevated positive funding — and the moment is **large, +21.10%** · opinion: this is the one card that contradicts the line above, and one contradiction out of five is enough to stop me calling it a rule · 3

C240 · NIL, the **deepest negative Before funding in the whole batch** (-0.0108 -0.0032 -0.1030 -0.0727 -0.0451 -0.0423), and the moment is **calm: +0.74%** over 24 h · opinion: this single card is the cleanest refutation available to me of "deeply negative funding means a big move is coming" — the most extreme instance in batch 02 is a calm one · 4

C283 · ZRO, all six Before payments negative (-0.0014 … -0.0245), moment **large +43.11%** · opinion: the mirror of C240 — same Before pattern, opposite outcome; with C240 that is 2 cards pointing opposite ways · 3

C244, C283, C184, C046, C049, C018 (large) vs C240, C022 (calm) · the **last Before payment is negative** on 8 cards: 6 of 15 large (40%) against 2 of 19 calm (10.5%) · opinion: numerically the best separation in my field, but 4 of the 8 are BCH, where a negative last payment fires on 4 of its 5 cards regardless of outcome (C016 is the only BCH card with an all-positive Before window, and it is calm) — strip BCH out and it is 3 of 12 large against 1 of 17 calm, i.e. 4 cards · 2

C244 (+32.47%), C283 (+43.11%), C018 (+10.06%) up vs C184 (-13.21%), C046 (-15.65%), C049 (-9.81%) down · among the 6 large cards with a negative last Before payment the subsequent direction splits **3 up / 3 down** · opinion: whatever negative Before funding may mark, it is not direction — this is why the line above cannot become an idea on its own · 4

C240, C283, C184, C049, C046, C022 · Before windows with **4 or more of 6 payments negative** (or 2+ of 3 on the 8 h coins): 4 large, 2 calm; the 4 large split +43.11% / -13.21% / -15.65% / -9.81%, i.e. 1 up and 3 down · opinion: the 3-1 lean toward "down" is one event away from being nothing, and see the market-wide note below before anyone leans on it · 2

C184, C046, C049 · in all three of the "down" cases above, the **bitcoin and ethereum columns fell hard in the same hours** — C184 at h+18 shows BTC -2.13 / ETH -3.90 while NEWT fell -5.33; C046 at h+0 shows BTC -2.04 / ETH -3.46; C049 at h+23 shows BTC -2.27 / ETH -3.32 · opinion: **RULES 13 makes these one market event, not three coin events** — so the "down" lean in the line above is mostly a bitcoin observation wearing a funding costume, and that is the single biggest reason I hold that idea at confidence 2 · 4

## E · The After window — dramatic, and unusable

C116 · FHE, move **-69.08%**, and the After funding prints -0.0326 / **-0.3836** / -0.3387 / -0.1926 / -0.3926 — roughly 77× the base rate in magnitude, the most extreme funding reading in the batch by a wide margin; the Before window that preceded it was mildly positive (+0.0191 … +0.0050) · opinion: the extreme funding **followed** the collapse, it did not announce it — this card is the clearest demonstration in batch 02 that funding's loudest readings are a consequence of price · 5

C244, C283, C282, C116, C184, C018, C046, C049 (large) vs C240, C022, C211 (calm) · the **After-window mean funding is negative** on 8 of 15 large cards (53%) against 3 of 19 calm (16%) · opinion: real separation — but it lives entirely in the After section, and TACTICS §6 says the exam cards carry only the Before section, so **this can never be traded and can never be scored**; I record it only so nobody mistakes it for a finding later · 3

C244, C283 · in both of these **large-up** cards (+32.47%, +43.11%) the After funding ran net **negative** while price surged; in C282 (-16.71%) and C116 (-69.08%), both large-**down**, the After funding also ran negative · opinion: After-window negativity accompanies large movement of **either** sign, so it is a volatility shadow, not a direction reading · 3

C296 · ZRO, move **-19.94%**, yet the After funding stayed pinned at ~+0.0050% throughout (+0.0050 +0.0031 +0.0050 +0.0050 +0.0047 +0.0050) · opinion: a 20% fall that left the funding field completely untouched — the counter-example to the line above, on the same coin · 4

C135 · KOMA calm (+1.70%), After funding swings -0.0028 / -0.0151 / **+0.0799** / +0.0090 / +0.0050 / +0.0449 — a wider swing than several of the large cards show · opinion: funding volatility by itself does not mark a large moment; this calm card out-swings C296's large one · 3

C069 · FARTCOIN large +19.80%, Before pinned at base, After drifts up +0.0050 ×3 then +0.0076 / +0.0137 / +0.0189 · opinion: funding rising off the clamp as a rally matures — again a lagging restatement of price, readable from the price column alone · 3

## F · Is my field a restatement of price?

C116, C244, C283, C069, C296 · the funding rate on Binance is computed from the premium index, i.e. from the perp's deviation from the index price · opinion (marked as opinion, I did not measure this): the Before-window funding number is therefore close to a restatement of the perp-vs-spot basis, which is near-price information; on the 12 pinned-at-base cards (section C) it is not even that, it is only "the premium stayed inside the clamp" · 3

## G · The one idea, with all three parts

**Idea I-1** — trigger · direction · exit, all three present, offered for testing only.
- **Trigger:** at the moment's start hour, **4 or more of the 6** Before-window 4 h funding payments are negative (for an 8 h coin: 2 or more of 3).
- **Direction:** **sell** (short).
- **Exit:** close 24 h after entry, or earlier on the first funding payment that prints at or above the base rate +0.0050%, whichever comes first.
- **Cards it fires on in batch 02:** C240, C283, C184, C049, C046, C022 — **6 of 34**. Outcomes: C283 +43.11%, C184 -13.21%, C046 -15.65%, C049 -9.81%, C240 +0.74%, C022 +1.54%. Among the 4 large: 1 up, 3 down.
- **Why I am not confident:** all three "down" cases coincide with bitcoin and ethereum falling in the same hours (see section D), which RULES 13 counts as a single event; and C283 is a +43% move in the opposite direction. **Confidence 2.**

**Not an idea — deliberately left as an observation.** "Last Before payment is negative" separates large from calm better than anything else in my field (6/15 vs 2/19, section D) but the direction splits 3 up / 3 down. Without a direction it is not an idea and I am not inventing one.

## H · What I did not find, and where I looked

C244 … C183 (all 34) · **no listing announcement, no delisting announcement, no warning announcement, no trading-halt notice, no margin- or leverage-tier change, no interval change** appears anywhere in batch 02. I looked at: the `Exchange announcements` line in the Before section of each of the 34 cards; the `interval changed:` flag in the Funding line of both the Before and the After section of each of the 34 cards (68 flags); and the `Fields not on this card` list of each of the 34 cards · opinion: for the interval flag this is a genuine measured "no event" (68 readings, all "no"); for the announcements it is **`MISSING`, a fetch failure, and must not be read as "no announcement happened"** · 5
