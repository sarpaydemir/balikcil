# Ingrid · watcher-high · field: exchange behaviour · round 1 · batch 06

Field of view: changes in the funding rate and the payment interval; listing,
delisting and warning announcements; every administrative decision the exchange
takes.

Cards read: 34 of 34 in batch 06 — C151, C195, C110, C052, C263, C165, C187,
C092, C027, C166, C034, C060, C051, C121, C019, C067, C017, C056, C055, C109,
C213, C089, C073, C146, C134, C194, C043, C226, C247, C050, C199, C087, C197,
C118.

Where I looked, per card: the `**Funding:**` line in the Before section, the
`**Funding:**` line in the After section, the `**Exchange announcements:**` line
in the Before section, and the `Fields not on this card` list at the foot of the
card. For five cards (C067, C043, C165, C166, C110) I also read the BTC and ETH
columns of the After table, only to say whether the whole market moved in the
same hours.

Note format: `card no · what I saw · why I think so · how sure I am (1-5)`.
All funding figures below are copied from the cards; none is estimated.
"L" = moment kind large, "c" = calm, with the card's own measured 24 h move.

---

## 1 · The two failures in my field — stated before anything else

C151, C195, C110, C052, C263, C165, C187, C092, C027, C166, C034, C060, C051, C121, C019, C067, C017, C056, C055, C109, C213, C089, C073, C146, C134, C194, C043, C226, C247, C050, C199, C087, C197, C118 · exchange announcements are MISSING on all 34 of 34 cards, with word-for-word the same reason: binance HTTP 202 with a zero-length body, bithumb returns only the most recent 5 notices with no paging, upbit HTTP 404. Both the Before-section line and the foot-of-card list say so · opinion: this is a fetch failure, not an absence — I cannot say there were no listing, delisting or warning announcements in these hours, only that no source could be read. Per RULES 20-21 this is a technical failure and is not a result · 5

C151, C195, C110, C052, C263, C165, C187, C092, C027, C166, C034, C060, C051, C121, C019, C067, C017, C056, C055, C109, C213, C089, C073, C146, C134, C194, C043, C226, C247, C050, C199, C087, C197, C118 · "interval changed: no" appears in both the Before and the After funding line of all 34 of 34 cards. The interval is a per-coin constant in this batch: 8 h / 3 payments for BCHUSDT (C052, C027, C034, C051, C019, C017, C043, C050) and for NOKUSDT (C263); 4 h / 6 payments for every other coin on these cards · opinion: within batch 06 the "payment interval and its changes" half of my field has zero variation, so it cannot separate anything here. That is a statement about these 34 cards, not about the year · 5

C151, C195, C110, C052, C263, C165, C187, C092, C027, C166, C034, C060, C051, C121, C019, C067, C017, C056, C055, C109, C213, C089, C073, C146, C134, C194, C043, C226, C247, C050, C199, C087, C197, C118 · no card carries any other administrative act — no leverage-limit change, no margin-tier change, no trading-status change. TACTICS section 3 lists "the history of leverage limits" among the things that are not on the card · opinion: so of the three parts of my field, announcements are unreadable, interval never changes, and only the funding *rate* actually carries information in batch 06. Anything I report below rests on that one part · 5

---

## 2 · The raw reading, one line per card

Written so a later count can be keyed by card number. Rate values in percent,
in payment order, as printed on the card.

C151 · KOMA, L +41.49%, 4 h x6 · before +0.0318 +0.0439 +0.1044 +0.0891 +0.1056 +0.0616 · after +0.0906 +0.1238 +0.0475 +0.0725 +0.0617 +0.0066 · read straight off the card · 5
C195 · NEWT, L -18.86%, 4 h x6 · before all +0.0050 · after all +0.0050 · read straight off the card · 5
C110 · FHE, L +65.60%, 4 h x6 · before +0.0064 +0.0050 +0.0182 +0.0592 +0.0159 +0.0078 · after +0.0050 +0.0050 +0.0160 +0.0091 +0.0123 +0.0050 · read straight off the card · 5
C052 · BCH, c +1.38%, 8 h x3 · before -0.0007 -0.0013 +0.0027 · after +0.0100 +0.0100 +0.0020 · read straight off the card · 5
C263 · NOK, L +11.70%, 8 h x3 · before +0.0000 +0.0000 +0.0000 · after +0.0000 +0.0000 +0.0000 · read straight off the card · 5
C165 · KOMA, c -1.56%, 4 h x6 · before +0.0371 +0.0398 +0.0050 +0.0050 +0.0050 +0.0339 · after +0.0292 +0.0433 +0.0458 +0.0050 -0.1255 -0.0214 · read straight off the card · 5
C187 · NEWT, L -12.82%, 4 h x6 · before all +0.0050 · after all +0.0050 · read straight off the card · 5
C092 · FARTCOIN, c -2.23%, 4 h x6 · before all +0.0050 · after +0.0050 +0.0050 +0.0050 +0.0063 +0.0050 +0.0050 · read straight off the card · 5
C027 · BCH, L +13.35%, 8 h x3 · before -0.0199 -0.0007 -0.0150 · after +0.0014 -0.0042 -0.0063 · read straight off the card · 5
C166 · KOMA, L +17.55%, 4 h x6 · before +0.0050 +0.0050 +0.0050 +0.0380 +0.0816 +0.0050 · after +0.0050 +0.0149 +0.0050 +0.0395 +0.1338 +0.0716 · read straight off the card · 5
C034 · BCH, L -13.17%, 8 h x3 · before -0.0073 +0.0046 +0.0058 · after +0.0067 +0.0008 -0.0227 · read straight off the card · 5
C060 · FARTCOIN, L -19.65%, 4 h x6 · before all +0.0050 · after +0.0050 +0.0050 +0.0050 +0.0050 +0.0025 +0.0050 · read straight off the card · 5
C051 · BCH, c -1.69%, 8 h x3 · before -0.0012 +0.0045 +0.0065 · after +0.0054 -0.0007 -0.0013 · read straight off the card · 5
C121 · FHE, c +6.71%, 4 h x6 · before +0.0050 x5 then +0.0064 · after +0.0050 +0.0102 +0.0050 +0.0050 +0.0149 +0.0050 · read straight off the card · 5
C019 · BCH, L -12.53%, 8 h x3 · before +0.0100 +0.0067 -0.0006 · after +0.0040 -0.0019 -0.0048 · read straight off the card · 5
C067 · FARTCOIN, L +20.70%, 4 h x6 · before -0.0199 -0.0201 -0.0338 -0.0288 -0.0136 +0.0050 · after +0.0050 +0.0050 +0.0099 +0.0050 +0.0050 +0.0050 · read straight off the card · 5
C017 · BCH, L -12.95%, 8 h x3 · before +0.0100 +0.0100 +0.0078 · after +0.0100 +0.0100 +0.0100 · read straight off the card · 5
C056 · FARTCOIN, L -20.22%, 4 h x6 · before +0.0050 x5 then +0.0111 · after +0.0150 +0.0141 +0.0114 +0.0050 +0.0050 +0.0050 · read straight off the card · 5
C055 · FARTCOIN, c +2.60%, 4 h x6 · before all +0.0050 · after +0.0050 x4, +0.0080, +0.0050 · read straight off the card · 5
C109 · FHE, L +36.50%, 4 h x6 · before +0.0050 x4, +0.0156, +0.0050 · after +0.0073 +0.0050 +0.0075 +0.0087 +0.0343 +0.0081 · read straight off the card · 5
C213 · NEWT, L +13.09%, 4 h x6 · before all +0.0050 · after all +0.0050 · read straight off the card · 5
C089 · FARTCOIN, c +0.70%, 4 h x6 · before all +0.0050 · after all +0.0050 · read straight off the card · 5
C073 · FARTCOIN, c +2.11%, 4 h x6 · before all +0.0050 · after all +0.0050 · read straight off the card · 5
C146 · KOMA, c -1.37%, 4 h x6 · before -0.0168 +0.0050 -0.0423 +0.0050 +0.0167 +0.0050 · after +0.0050 x4, +0.0175, +0.0050 · read straight off the card · 5
C134 · FHE, c -8.39%, 4 h x6 · before all +0.0050 · after all +0.0050 · read straight off the card · 5
C194 · NEWT, L -18.02%, 4 h x6 · before all +0.0050 · after all +0.0050 · read straight off the card · 5
C043 · BCH, L -13.97%, 8 h x3 · before -0.0140 -0.0050 -0.0081 · after -0.0118 -0.0095 -0.0588 · read straight off the card · 5
C226 · NIL, L -21.59%, 4 h x6 · before all +0.0050 · after all +0.0050 · read straight off the card · 5
C247 · NIL, L -22.44%, 4 h x6 · before all +0.0050 · after +0.0050 x4, +0.0002, +0.0046 · read straight off the card · 5
C050 · BCH, c -0.65%, 8 h x3 · before -0.0155 -0.0012 +0.0045 · after +0.0065 +0.0054 -0.0007 · read straight off the card · 5
C199 · NEWT, c +1.08%, 4 h x6 · before +0.0050 +0.0050 -0.0006 +0.0043 -0.0029 -0.0033 · after +0.0010 -0.0027 -0.0096 -0.0027 +0.0050 +0.0050 · read straight off the card · 5
C087 · FARTCOIN, c +2.47%, 4 h x6 · before all +0.0050 · after -0.0012 then +0.0050 x5 · read straight off the card · 5
C197 · NEWT, c +1.21%, 4 h x6 · before -0.0049 then +0.0050 x5 · after +0.0050 x5 then +0.0013 · read straight off the card · 5
C118 · FHE, c +3.11%, 4 h x6 · before all +0.0050 · after all +0.0050 · read straight off the card · 5

Counts for the batch: 19 large moments (C151, C195, C110, C263, C187, C027,
C166, C034, C060, C019, C067, C017, C056, C109, C213, C194, C043, C226, C247)
and 15 calm (C052, C165, C092, C051, C121, C055, C089, C073, C146, C134, C050,
C199, C087, C197, C118).

---

## 3 · What the funding rate did and did not separate

C195, C187, C060, C213, C194, C226, C247 (large) and C092, C055, C089, C073, C134, C087, C118 (calm) · in 14 of the 34 cards every funding payment in the 24 h before is exactly +0.0050%, and the split is 7 large against 7 calm — 7 of 19 large moments (37%) and 7 of 15 calm moments (47%) · opinion: +0.0050% looks like the exchange's floor value for these contracts rather than a market price. A flat floor before the moment is at least as common before a calm hour as before a large one, so on its own it separates nothing in this batch. If a score recipe ever gives points for "funding at the floor", these 14 cards argue against it · 4

C195, C187, C060, C213, C194, C226, C247, C263, C109, C019, C017, C034, C043, C056 · in 14 of the 19 large moments the funding rate never left the band -0.0140% to +0.0156% in the 24 h before; the five that did are C151, C110, C027, C166, C067 · opinion: for roughly three quarters of the large moments in this batch, funding before them was unremarkable. Whatever caused those moves, it had not shown up in the funding rate · 4

C052, C027, C034, C051, C019, C067, C043, C050, C146, C199, C197 · 11 of 34 cards have at least one negative funding payment in the 24 h before: 5 large (C027, C034, C019, C067, C043) and 6 calm (C052, C051, C050, C146, C199, C197) — near a 50/50 split · opinion: "funding went negative" by itself does not separate large from calm here. Worse, 7 of the 11 are the same coin, BCHUSDT, where negative prints are the ordinary state (7 of the 8 BCH cards in the batch have one; only C017 does not). A threshold rule on negative funding applied across coins would in practice be selecting BCH, not selecting a condition · 4

C027, C067, C043 · 3 cards where *every* funding payment in the 24 h before is negative, and all three are large moments; no calm card in the batch has an all-negative before window · opinion: interesting but it rests on 3 cards out of 34, and the direction is not consistent — C027 +13.35%, C067 +20.70%, C043 -13.97%. Because I cannot give a direction, I am writing this as an observation and not as an idea · 2

C151, C110, C027, C166, C067 vs C195, C187, C034, C060, C019, C017, C056, C194, C043, C226, C247 · asymmetry: of the 8 large *up* moments, 5 had a before-window funding payment outside +/-0.016% (C151 +0.1056, C110 +0.0592, C027 -0.0199, C166 +0.0816, C067 -0.0338); of the 11 large *down* moments, 0 did — every one of the 11 stayed inside -0.0140% to +0.0111% · opinion: this is the only clean-looking asymmetry I found, and I distrust it. The +/-0.016% boundary was chosen *after* I had seen these 34 cards, so under RULES 6 it carries the "afterwards" label and means nothing until it is tested on cards I have not read. Three of the seven cards that trip it are the same coin (KOMA: C151, C165, C166) · 3

C151, C165, C166, C146 · all four KOMAUSDT cards in the batch have a volatile funding rate, and KOMA holds every one of the batch's four largest absolute prints: +0.1056% before and +0.1238% after on C151, +0.1338% after on C166, -0.1255% after on C165, -0.0423% before on C146 · opinion: in this batch "funding is extreme" is close to a synonym for "the coin is KOMA". Any cross-coin funding threshold needs to be normalised per coin, or it just picks out coins with thin funding markets · 4

C165 · the single largest absolute funding print in the whole batch, -0.1255% at the fifth payment of the After window, sits on a *calm* card whose measured 24 h move is -1.56%; BTC and ETH were also quiet over those hours (largest hourly moves +0.48/+0.99 and -0.43/-0.49) · opinion: a direct counterexample to "an extreme funding print marks a big move". One card, so it is a counterexample and not a rule, but it is the kind of card a recipe built on funding extremes would get wrong · 4

C110 · the largest move in the batch, +65.60%, happened with funding essentially at the exchange floor: 5 of the 6 payments in the 24 h after are +0.0160% or lower, and the before window peaked at +0.0592%. BTC and ETH moved at most +1.56% in any hour of the After window, so this was the coin's own move · opinion: a 65% rally that never showed up in the funding rate. Whatever mechanism links crowded positioning to funding did not operate here · 4

C151, C110 · in the two largest up moves of the batch the mean funding rate in the 24 h after was *lower* than in the 24 h before (C151 +0.0727% -> +0.0671%; C110 +0.0188% -> +0.0087%; both means computed by me from the printed payments) · opinion: this cuts against the naive expectation that a big rally drags funding up with it. Two cards only · 3

C151, C110, C166, C027, C067, C109, C034, C060, C019, C017, C056, C043, C247 · comparing mean funding after against mean funding before on the 13 large moments where funding actually varies, the change agrees in sign with the direction of the move in 9 and disagrees in 4 (disagreeing: C151, C110, C017, C056) · opinion: even as a *restatement* of the move it is a loose one. And the After funding is not usable as a signal anyway, because it is contemporaneous with the price it would be describing — this is the "if price already says it, it has no value" case, and here price does not even say it cleanly · 4

C263 · funding printed as exactly +0.0000% for all three payments before and all three after, on an 8 h interval, with a large +11.70% move. This is the only card of the 34 where the rate is 0.0000% rather than the +0.0050% floor, and the contract is thin (previous 7 days: avg hourly volume 191.74k, avg hourly trades 618) · opinion: reads like a different funding configuration on this contract rather than a market state. I could not check the listing date, because the announcement source is MISSING on this card as on all the others. One card — an observation only · 2

C043 · the deepest negative funding sequence in the After window of any card: -0.0118, -0.0095, -0.0588, on a large -13.97% move; BTC and ETH were quiet through those hours (worst hourly prints BTC -0.68, ETH -2.24, while BCH fell -3.14% in one hour with BTC at -0.12) · opinion: funding chasing the price down on a move that belongs to the coin, not to the market. It arrives with the move, not before it: the before window was only -0.0140 -0.0050 -0.0081 · 4

C067 · the clearest "sustained negative funding then a rally" card: all six before payments negative (-0.0199 -0.0201 -0.0338 -0.0288 -0.0136), then +20.70%, with funding snapping back to the +0.0050% floor afterwards; BTC and ETH moved at most +1.17%/+2.02% in any hour of the After window, so this was the coin's own move · opinion: the single most suggestive card in my field. It is one card. C043, with the same all-negative setup, went the other way · 3

---

## 4 · Idea (three parts), written so it can be killed

**Idea 1.**
- **Trigger:** at any moment start, at least one funding payment in the preceding 24 h with an absolute rate above 0.016% — that is, funding clearly off the +0.0050% floor, in either sign.
- **Direction:** buy.
- **Exit:** close 24 h after entry, unconditionally.
- **Seen in:** 7 of the 34 cards of batch 06 — C151, C110, C027, C166, C067 (all large, all up: +41.49%, +65.60%, +13.35%, +17.55%, +20.70%) and C165, C146 (both calm, small down drift: -1.56%, -1.37%). No large *down* moment in the batch trips the trigger.
- **Why I think it might be something (opinion):** the trigger fires on funding being *active* in either direction, not on its sign, so it behaves more like a measure of how contested positioning is than like a positioning level. C166 argues it is not simply a restatement of recent price: its previous-7-day line reads +0.00% price change, yet its before window carried a +0.0816% payment.
- **Why I mostly think it is not (opinion):** 7 cards. The 0.016% boundary was picked after reading the cards, so it is an "afterwards" rule under RULES 6. Three of the seven cards are KOMAUSDT, and KOMA has the noisiest funding of any coin in the batch, so the trigger may be selecting a coin rather than a condition. The two calm cards that trip it would both be losing trades.
- **How sure I am: 2.**

I have no second idea. The other things above are observations, because I could
not supply a direction for them.

---

## 5 · Where I looked before saying "none"

- Listing, delisting and warning announcements: looked at the `**Exchange
  announcements:**` line in the Before section and at the `Fields not on this
  card` list of every one of the 34 cards. All 34 say MISSING with the same
  three probe failures. I did **not** open
  `data/observation/external/announcements.json` — it is outside what this
  instruction lets me read.
- Payment-interval changes: looked at the `interval changed:` clause of both
  funding lines on all 34 cards. All 68 read "no".
- Other administrative decisions (leverage limits, margin tiers, trading
  status): no such field exists on any of the 34 cards; TACTICS section 3 says
  the history of leverage limits is not on the card. So this is "not on the
  card", not "nothing happened".

## 6 · Not verified

- My definition asks me to stop if `watcher` and `watcher-high` differ other
  than in effort, name and description. I could not check: the other definition
  file is not among the files this instruction permits me to read, so I did not
  open it.
