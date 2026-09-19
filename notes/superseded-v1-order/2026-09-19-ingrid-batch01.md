# Ingrid · watcher-high · field of view: exchange behaviour · round 1 · batch 01

Field of view as instructed: **funding rate and payment-interval changes; listing,
delisting and warning announcements; administrative decisions of the exchange.**
34 cards read (batch 01). Everything below is measured off the card text.

Conventions I used, stated so they can be checked:
- "baseline" = a printed rate of exactly `+0.0050%`. I call it baseline because it
  is the single most repeated value in the batch, not because the card names it so.
- I take the printed funding list as **chronological, oldest first**. The card does
  not label the order. My reason is continuity across the section break (C139 ends
  before at -0.3085% and opens after at -0.3012%; C004 ends before at +0.0756% and
  opens after at +0.0484%). This is an inference, not a card statement.
- Counts below are **out of the 34 cards of batch 01 only.** They are a floor.
- I did not open `data/observation/external/announcements.json` (the probe log the
  cards point at): the instruction closes the rest of `data/` to me.

---

## A · Notes covering the whole batch (card numbers listed in full)

A1 · C153, C235, C033, C271, C139, C098, C019, C126, C157, C023, C255, C131, C221, C081, C289, C163, C110, C052, C104, C238, C004, C217, C117, C188, C120, C218, C182, C102, C106, C275, C270, C143, C009, C192 · The exchange-announcement field is `MISSING` on all 34 cards, with byte-identical wording (binance HTTP 202 zero-length body; bithumb only the most recent 5 notices; upbit HTTP 404). Both the "Before" block and the "Fields not on this card" block say so. · This is a **fetch failure, not an absence** — the card's own legend distinguishes `MISSING` from `none`, and the announcement field says `MISSING` while e.g. the prediction-market field on C153/C235 says `none`. So for batch 01 I cannot say whether listing/delisting/warning announcements sat near these moments; I can only say the source was never reached. Half of my field of view is unobserved, not empty. · 5

A2 · C153, C235, C033, C271, C139, C098, C019, C126, C157, C023, C255, C131, C221, C081, C289, C163, C110, C052, C104, C238, C004, C217, C117, C188, C120, C218, C182, C102, C106, C275, C270, C143, C009, C192 · `interval changed: no` on every funding line of every card — 68 statements (34 before + 34 after). No card shows a payment count inconsistent with its stated interval either (always 6 payments at 4 h, or 3 at 8 h, over a 24 h window). · My opinion: in batch 01 the payment-interval field has **zero variance**, so it can carry no information about anything. A signal with no variance cannot separate large from calm. Interval changes may exist elsewhere in the 306 cards; in these 34 there are none. · 5

A3 · 4 h interval (6 payments): C153, C139, C157, C163, C143 (KOMA) · C235, C221, C238, C217, C218 (NIL) · C098, C126, C131, C110, C104, C117, C120, C102, C106 (FHE) · C271, C289, C275, C270 (ZRO) · C188, C182, C192 (NEWT) · C081 (FARTCOIN). 8 h interval (3 payments): C033, C019, C023, C052 (BCH) · C255 (NOK) · C004, C009 (AVGO). · The interval is **a constant of the contract, not of the moment** — every card of a given coin carries the same interval, and both moment kinds appear at both intervals (4 h: 12 large / 15 calm; 8 h: 5 large / 2 calm). My opinion: the interval is a coin-identity fact, so it restates "which contract is this", not "what is about to happen". · 5

A4 · C033, C019, C023, C052, C255, C004, C009 · Flagging for the canteen, not as a trading signal: the exam hides coin name, date and price, but it cannot hide **how many funding payments a 24 h window contains**. 3 vs 6 payments splits the universe into 8 h and 4 h contracts and therefore leaks contract class into an otherwise blinded card. · This is a procedural worry of mine, not an observation about price. 7 of 34 cards here are 8 h. · 4

---

## B · What funding did before the move — the central negative

B5 · all baseline before, large moment: C221 (-38.18%), C117 (+34.69%), C120 (-44.40%), C106 (+120.84%), C104 (+161.78%) · all baseline before, calm moment: C098 (-4.71%), C126 (-6.79%), C081 (+6.28%), C238 (+5.18%), C217 (+1.80%), C218 (+2.59%), C102 (-4.01%), C192 (+1.53%) · Funding pinned at exactly +0.0050% for all six payments of the before window occurs in **13 of 34 cards: 5 large and 8 calm.** · My opinion: this is the batch's clearest negative. The five largest 24-hour moves in the whole batch that carry flat funding include a -44% and a +162%, and the same flat funding sits under eight moments where nothing happened. **Flat baseline funding before the start hour separates nothing.** Anyone scoring "funding is quiet, so the market is quiet" would be wrong five times in thirteen here. · 5

B6 · above 0.0100% peak, large: C153 (.0192), C139 (.3085), C157 (.0560), C255 (.0510), C110 (.0592), C004 (.0756), C009 (.0291) = 7 of 17 · above 0.0100% peak, calm: C023 (.0173), C131 (.0261), C163 (.0836), C188 (.0197), C275 (.0118), C143 (.1067) = 6 of 17 · I took the largest absolute printed rate in each before window and cut at 0.0100%. Large moments clear it 7/17, calm moments 6/17. · My opinion: **no separation at all** at this cut. And the largest positive before-print in the whole batch, +0.1067% on C143, is followed by a calm -2.09%; while C221's entirely flat funding is followed by -38.18%. If the peak before-funding had discriminating power I would expect the extremes to sort; they sort backwards. · 4

B7 · C139 · The single most extreme funding reading in the batch: the before window falls -0.0016%, -0.0623%, +0.0050%, -0.0096%, -0.0891%, **-0.3085%** (4 h interval), i.e. roughly 60x baseline and negative. The measured 24 h move was -39.29%, and the first after-payment was still -0.3012%. · My opinion: a deeply negative funding rate here sat with a **fall**, not the short squeeze one might expect from "shorts are paying". But this is **one card out of 34**, it is the only card in the batch whose before window exceeds |0.10%|, and I therefore treat it as an observation and not a rule. I also cannot rule out that funding was already tracking a fall that began inside the before window — that would make it a restatement of price. · 3

B8 · C143 · The mirror case: the before window opens at **+0.1067%** (largest positive in the batch) and the moment is **calm**, +2.09% down over 24 h. The spike is at the *first* of six payments, i.e. roughly 24 h before the start hour, and funding is back to baseline by the last payment. · My opinion: taken with B7 this says a single extreme funding print, on its own, does not mark anything; the two most extreme before-windows in the batch land on opposite moment kinds. 1 card each side. · 4

B9 · C275, C023 · Persistently negative funding across a whole window with no move: C275 (ZRO) prints six negative rates before (-0.0019 to -0.0118%) and six negative after (-0.0001 to -0.0188%), moment kind calm, -2.50%. C023 (BCH) prints three negatives before (-0.0173, -0.0094, -0.0137%), calm, +3.29%. · My opinion: a sustained negative-funding regime is a coin-level state that can persist for at least 48 h with nothing happening. 2 of 34 cards. Anyone tempted to read "funding has gone negative" as a squeeze setup has two counterexamples here. · 4

B10 · C004, C009 · Both AVGO cards, 8 h interval, and they disagree with each other completely: C004 before rises +0.0438 / +0.0520 / +0.0756% and keeps rising after (+0.0484 / +0.0603 / **+0.1740%**) while price falls **-17.27%**; C009 prints **+0.0000% exactly** on the first before payment and on **all three** after payments, with a +8.82% move. · My opinion: C004 is a clean counterexample to "strong positive funding means longs are crowded and price will fall/rise" in either direction — funding stayed strongly positive *through* the fall, it did not flip. The exact `+0.0000%` triple on C009 I flag as a possible data or rounding artefact rather than a market fact; I have no way on this card to tell a genuinely zero rate from a rounded one. 2 of 34 cards. · 3

---

## C · What funding did during the move — and why I think it is worth little

C11 · after-window peak at or above 0.0500%, large: C139 (.3012), C255 (.1515), C004 (.1740), C104 (.1018), C120 (.0946), C106 (.0742) = 6 of 17 · same, calm: C163 (.0591), C143 (.0931) = 2 of 17 · Funding magnitude expands into the after window far more often on large cards (6/17) than calm (2/17). · My opinion: this is the only tilt in my whole field, and it is **worthless for prediction** — the after window is by definition after the start hour, so this is funding reacting to a move that has already begun, and point 3 of my brief applies: it restates price. I record it only because it shows the funding feed is live and responsive, which makes the *absence* of a reaction in C221/C117 (below) the more striking. · 4

C12 · C221, C117 · Funding is pinned at exactly +0.0050% on **all twelve** payments, before and after, while the measured 24 h moves are **-38.18%** (C221) and **+34.69%** (C117). · My opinion: funding can stay dead flat straight through a one-third collapse and a one-third rally. This is the strongest single argument in my field against building any score component on funding level. 2 of 34 cards. · 5

C13 · C120, C255 · Large negative funding prints arriving *inside* a large fall: C120 prints -0.0334% then -0.0946% in the after window of a -44.40% move; C255 prints -0.1515% on its last after payment of a -17.73% move. In both, the before window gave no such warning (C120 was entirely baseline; C255 peaked at +0.0510%). · My opinion: funding follows here, it does not lead. 2 of 34 cards. · 4

C14 · C104, C106 · The mirror on the upside: C104 prints +0.1018% inside a +161.78% move and C106 prints +0.0742% / +0.0694% inside a +120.84% move, both from entirely baseline before windows. · Same opinion as C13 — a reaction, not a warning. 2 of 34 cards. · 4

C15 · C255, C004 · On the 8 h contracts the three printed rates of the after window track the three of the before window slot-for-slot until the slot the move happens in: C255 (+.0510/+.0089/-.0147 → +.0468/+.0092/-.1515) and C004 (+.0438/+.0520/+.0756 → +.0484/+.0603/+.1740). · My opinion: this looks like a **time-of-day shape** in 8 h funding, i.e. the same UTC slot prints a similar rate day to day. If real it would mean a raw funding level must be compared against the same slot, not against the coin's average. 2 of 34 cards, and C009 (AVGO, all zeros after) does not fit, so I hold this loosely. · 2

---

## D · Per-card record (the measurement, for later keying by card number)

Each line: interval · payments · interval changed · announcements · before peak |rate| · after peak |rate| · moment kind and measured move.

D-C153 · KOMA 4 h · 6+6 · changed: no · announcements MISSING · before peak +0.0192% (five of six at baseline) · after peak +0.0411%, last payment -0.0100% · large, -21.00% · Card facts copied directly; nothing in my field stands out before the start hour. · 5
D-C235 · NIL 4 h · 6+6 · changed: no · announcements MISSING · before peak +0.0050%, mixed small signs · after peak +0.0050% · calm, +5.66% · Direct copy. · 5
D-C033 · BCH 8 h · 3+3 · changed: no · announcements MISSING · before peak -0.0082% · after peak +0.0088% · large, +12.52% · Direct copy; funding essentially flat through a +12.5% move. · 5
D-C271 · ZRO 4 h · 6+6 · changed: no · announcements MISSING · before peak +0.0050% · after peak +0.0050% · calm, +0.14% · Direct copy. · 5
D-C139 · KOMA 4 h · 6+6 · changed: no · announcements MISSING · before peak **-0.3085%** · after peak -0.3012% · large, -39.29% · See B7; the batch's one extreme before-window. · 5
D-C098 · FHE 4 h · 6+6 · changed: no · announcements MISSING · before all baseline · after all baseline · calm, -4.71% · Direct copy. · 5
D-C019 · BCH 8 h · 3+3 · changed: no · announcements MISSING · before peak +0.0100% · after peak -0.0048% · large, -12.53% · Direct copy; funding shrank as price fell. · 5
D-C126 · FHE 4 h · 6+6 · changed: no · announcements MISSING · before all baseline · after all baseline · calm, -6.79% · Direct copy. · 5
D-C157 · KOMA 4 h · 6+6 · changed: no · announcements MISSING · before peak +0.0560% (and a -0.0467%) · after peak +0.0265% · large, +17.08% · Direct copy; before window is the noisiest of the KOMA large cards yet the move is the mildest of them. · 4
D-C023 · BCH 8 h · 3+3 · changed: no · announcements MISSING · before all negative, peak -0.0173% · after peak -0.0149% · calm, +3.29% · See B9. · 5
D-C255 · NOK 8 h · 3+3 · changed: no · announcements MISSING · before peak +0.0510% · after peak **-0.1515%** · large, -17.73% · See C13 and C15. · 5
D-C131 · FHE 4 h · 6+6 · changed: no · announcements MISSING · before peak +0.0261% · after peak +0.0472%, all six after above baseline · calm, -5.87% · A rising funding ramp across both windows with **no** large move — a counterexample to reading a funding ramp as a build-up. · 4
D-C221 · NIL 4 h · 6+6 · changed: no · announcements MISSING · before all baseline · after all baseline · large, **-38.18%** · See C12. · 5
D-C081 · FARTCOIN 4 h · 6+6 · changed: no · announcements MISSING · before all baseline · after all baseline · calm, +6.28% · Direct copy; the batch's only FARTCOIN card. · 5
D-C289 · ZRO 4 h · 6+6 · changed: no · announcements MISSING · before peak -0.0037% (five at baseline) · after peak -0.0100% · large, +19.45% · Funding drifted slightly negative while price rose 19%. · 4
D-C163 · KOMA 4 h · 6+6 · changed: no · announcements MISSING · before peak +0.0836% · after peak +0.0591% · calm, +2.18% · One of only two calm cards with an after-peak above 0.0500% (see C11) — funding was busy and price was not. · 4
D-C110 · FHE 4 h · 6+6 · changed: no · announcements MISSING · before peak +0.0592% · after peak +0.0160% · large, +65.60% · Funding **fell** toward baseline as price rose 65% — the opposite of the C104/C106 pattern in the same coin. · 4
D-C052 · BCH 8 h · 3+3 · changed: no · announcements MISSING · before peak +0.0027% · after peak +0.0100% · calm, +1.38% · Direct copy. · 5
D-C104 · FHE 4 h · 6+6 · changed: no · announcements MISSING · before all baseline · after peak +0.1018% · large, **+161.78%** · See B5 and C14: the batch's biggest move, with a completely uninformative before window in my field. · 5
D-C238 · NIL 4 h · 6+6 · changed: no · announcements MISSING · before all baseline · after peak -0.0200% · calm, +5.18% · Direct copy. · 5
D-C004 · AVGO 8 h · 3+3 · changed: no · announcements MISSING · before peak +0.0756%, rising · after peak **+0.1740%**, still rising · large, -17.27% · See B10: strongly positive funding *through* a 17% fall, no sign flip. · 5
D-C217 · NIL 4 h · 6+6 · changed: no · announcements MISSING · before all baseline · after all baseline · calm, +1.80% · Direct copy. · 5
D-C117 · FHE 4 h · 6+6 · changed: no · announcements MISSING · before all baseline · after all baseline · large, **+34.69%** · See C12. · 5
D-C188 · NEWT 4 h · 6+6 · changed: no · announcements MISSING · before peak -0.0197% · after all baseline · calm, -0.90% · A single negative excursion then back to baseline, no move. · 4
D-C120 · FHE 4 h · 6+6 · changed: no · announcements MISSING · before all baseline · after peak -0.0946% · large, **-44.40%** · See B5 and C13. · 5
D-C218 · NIL 4 h · 6+6 · changed: no · announcements MISSING · before all baseline · after all baseline · calm, +2.59% · Direct copy. · 5
D-C182 · NEWT 4 h · 6+6 · changed: no · announcements MISSING · before peak +0.0050% (one print +0.0008%) · after all baseline · large, -11.86% · Funding entirely flat across a -11.9% move. · 5
D-C102 · FHE 4 h · 6+6 · changed: no · announcements MISSING · before all baseline · after all baseline · calm, -4.01% · Direct copy. · 5
D-C106 · FHE 4 h · 6+6 · changed: no · announcements MISSING · before all baseline · after peak +0.0742% (and a -0.0390%) · large, **+120.84%** · See B5 and C14. · 5
D-C275 · ZRO 4 h · 6+6 · changed: no · announcements MISSING · before all six negative, peak -0.0118% · after all six negative, peak -0.0188% · calm, -2.50% · See B9. · 5
D-C270 · ZRO 4 h · 6+6 · changed: no · announcements MISSING · before peak +0.0050% · after peak +0.0050% · large, +20.94% · Funding entirely at or below baseline across a +20.9% move. · 5
D-C143 · KOMA 4 h · 6+6 · changed: no · announcements MISSING · before peak **+0.1067%** (first payment) · after peak +0.0931% · calm, -2.09% · See B8. · 5
D-C009 · AVGO 8 h · 3+3 · changed: no · announcements MISSING · before +0.0000% / +0.0291% / +0.0087% · after **+0.0000% / +0.0000% / +0.0000%** · large, +8.82% · See B10; I flag the exact-zero triple as a possible artefact. · 3
D-C192 · NEWT 4 h · 6+6 · changed: no · announcements MISSING · before all baseline · after all baseline · calm, +1.53% · Direct copy. · 5

---

## E · Ideas (trigger · direction · exit)

E1 · **Idea, weak — n=1.** Trigger: on a 4 h-interval contract, the funding payment immediately preceding the start hour prints |rate| ≥ 0.10%. Direction: **sell** (short the coin). Exit: flat at the sixth funding payment after entry, i.e. 24 h later; no stop, so the test measures the raw 24 h return. · Supporting card: C139 only (-0.3085% then -39.29%). Contradicting cards: none, because **no other card in the 34 fires the trigger** — C143 is the only other card whose before window touches |0.10%| and its spike is on the first payment, not the last. So batch 01 gives this idea one hit out of one firing, which is worth almost nothing, and I cannot even tell from the card whether funding had already turned before or after price started falling inside the before window. Written only so it can be counted properly later. · 2

E2 · **Anti-idea, offered for the score recipe.** Trigger: funding is at baseline (`+0.0050%`) for every payment of the before window on a 4 h contract. Direction: **no position either way** — explicitly, this condition must be worth **zero points**, not negative and not positive. Exit: n/a. · Grounds: 13 of 34 cards fire it, 5 large and 8 calm (B5), and the firing set contains both the batch's largest rise (+161.78%, C104) and its largest fall (-44.40%, C120). Any recipe that reads quiet funding as "expect calm" would be scored wrong on those five. · 4

---

## F · Where I looked and found nothing, stated plainly

- **Listing / delisting / warning announcements:** looked at the "Exchange announcements" line in the Before section and the "Fields not on this card" list of all 34 cards. Result on all 34: `MISSING`, source unreached. **Not "no announcements" — "no data".** (A1)
- **Payment-interval changes:** looked at the `interval changed:` flag on both funding lines of all 34 cards, and cross-checked the payment count against the stated interval. 68 of 68 read `no`, 34 of 34 counts consistent. (A2)
- **Other administrative decisions of the exchange:** I looked for any further exchange-side item inside my field on the cards — the only exchange-administered quantities printed are the funding rate, the payment interval and the announcement feed. Leverage-limit history is stated by the laboratory's own tactics as not carried on the card. So in batch 01 my field reduces to funding alone, plus one unreachable feed.
