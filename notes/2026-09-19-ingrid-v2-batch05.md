# Ingrid · watcher-high · round 1 · batch 05 · 2026-09-19

Field of view: funding rate and its changes · funding payment interval and its
changes · listing / delisting / warning announcements · exchange administrative
decisions.

Cards read (34): C222, C190, C058, C072, C036, C265, C202, C084, C147, C111,
C206, C292, C081, C002, C023, C003, C164, C091, C267, C039, C245, C160, C104,
C173, C252, C123, C172, C237, C021, C275, C138, C085, C175, C156.

All counts below are **out of the 34 cards of batch 05 only**. They are floors,
not counts over the whole card set.

Where I looked for announcements: on each of the 34 cards, the `Exchange
announcements:` line in the **Before** section and the `Binance and Korean
exchange announcements` entry in the **Fields not on this card** section. I did
not open `data/observation/external/announcements.json`; it is outside what this
instruction lets me read.

Format: `card no · what I saw · why I think so · how sure I am (1–5)`

---

## A · Failures and what the batch cannot answer

C222, C190, C058, C072, C036, C265, C202, C084, C147, C111, C206, C292, C081, C002, C023, C003, C164, C091, C267, C039, C245, C160, C104, C173, C252, C123, C172, C237, C021, C275, C138, C085, C175, C156 · **Announcement data is MISSING on all 34 of 34 cards**, with byte-identical wording on every card: binance = HTTP 202 with a zero-length body; bithumb = only the most recent 5 notices, no paging; upbit = HTTP 404. This is `MISSING` (source unreachable), not `none` (source read, nothing there) — the card's own legend draws that distinction · This is a fetch failure, not an absence of announcements. Half of my field of view (listing / delisting / warning / administrative notices) has **no data at all** in this batch, so it cannot be judged either way here. A technical failure is not a result · 5

C222 … C156 (all 34) · **Funding payment interval never changes**: every one of the 68 funding lines (34 before + 34 after) reads `interval changed: no` · Read directly off each card · So "interval change" has **zero occurrences in 34 cards** and cannot be tested from this batch, in either direction. Anyone scoring it from batch 05 is scoring an empty cell · 5

C222 … C156 (all 34) · **No funding payment is missing anywhere**: every 4 h-interval card carries exactly 6 payments per 24 h window and every 8 h-interval card exactly 3, before and after · 6×4 = 24 and 3×8 = 24 · My opinion: this also means there is **no funding suspension, no settlement gap and no trading halt** visible in these 34 cards — the administrative events that would show up as a hole in the payment series simply are not here. That is a fact about the batch, not about the exchange · 4

---

## B · The payment interval as a standing exchange decision

C036, C023, C039, C021 (BCH) and C002, C003 (AVGO) · **8 h interval**; the other 28 cards (NIL, NEWT, FARTCOIN, OMNI, KOMA, FHE, ZRO) are all **4 h** · Read off the funding line of each card · Opinion: the interval is fixed per contract here, so within a coin it is a constant and can never separate one moment from another. Across coins it is a standing exchange classification, and in this batch it lines up with how much the coin moves: the six 8 h cards measure +1.14, +3.29, +0.91, +1.05, −0.05 and +7.72 %, while 4 h cards reach −47.62 % and +161.78 %. **This is a restatement of the coin's volatility, which price already says** — it adds nothing a volatility measure would not · 4

C002, C003 (AVGO) · **Exactly `+0.0000%` funding prints, 6 of the 12 AVGO payments** (C002 before 0.0000, 0.0000, +0.0120; C002 after +0.0238, 0.0000, 0.0000; C003 before +0.0071, 0.0000, +0.0322; C003 after +0.0147, 0.0000, +0.0388). **No other card in the batch — 0 of the other 32 — prints an exact zero**; the nearest are +0.0002 (C039) and +0.0003 (C245) · Opinion (clearly marked as opinion, and it rests on 2 cards): this looks like a contract-specific administrative rule, e.g. funding set to zero outside the underlying's trading session, rather than a market outcome. If that is what it is, funding carries no information for this contract during those windows. **2 cards is an observation, not a rule** · 3 for the measurement being real, 2 for the reason

---

## C · The `+0.0050%` clamp, and the null it produces

C222, C202, C084, C081, C091, C267, C292, C104, C252, C237 · **Before-window funding pinned at exactly `+0.0050%` for all 6 payments — 10 of 34 cards.** Of these, **4 are large moments (C202, C104, C252, C237) and 6 are calm (C222, C084, C081, C091, C267, C292)** · Read off the Before funding line. The batch base rate is 15 large / 19 calm = 44 % large; the clamped group is 4/10 = 40 % large · My reading: **flat-at-the-floor funding separates nothing.** It is present just as often before a calm moment as before a large one, so as a signal it is telling us nothing. This is a null and I am writing it down as one · 4

C104 · Before funding **flat at `+0.0050%` for all 6 payments, and the measured 24 h move was +161.78 %** — the largest move in the batch. The after window is also near the floor: +0.0050, +0.0050, +0.0050, **+0.1018**, +0.0050, +0.0050 · Read off the card; BTC in the after table stays inside ±0.5 %/h through the whole rally and ETH likewise except +2.87/−2.93 at h+19/+20, so **this was not the market moving together — it is the coin** · A single hard counterexample to "funding leads the move". Also worth someone checking: funding returning to the floor at payments 5 and 6 while the coin prints +12 %/h at h+17…+19 looks odd to me, and I flag it as something to verify rather than assert · 4 for the measurement, 2 for the oddity

C237 · Funding **flat at `+0.0050%` across all 12 payments, before *and* after**, while the measured 24 h move was **+42.62 %** · Read off both funding lines · Opinion: a 42 % move that leaves no trace in funding over 48 hours is a second counterexample of the same shape as C104 · 4

---

## D · Elevated positive funding before the moment

C147, C111, C164, C003, C160, C123, C172, C138, C156 · **At least one before-window payment ≥ +0.030% — 9 of 34 cards.** Large: C111, C003, C123, C138, C156 (5). Calm: C147, C164, C160, C172 (4). 5/9 = 56 % large against a 44 % base rate · Counted off the before funding lines · Opinion: a tilt this small on 9 cards is nothing. And it is **confounded by coin** — 6 of the 9 are KOMA or FHE · 3

C147, C164, C160, C172, C173, C138, C156 (all 7 KOMA cards) · **Within one coin, elevated funding does not separate the two kinds.** KOMA's before-window maxima: C147 +0.0835 (calm), C164 +0.0591 (calm), C172 +0.0426 (calm), C160 +0.0312 (calm), C138 +0.0697 (large), C156 +0.0695 (large), C173 +0.0190 (large) · The four highest readings are **all calm** cards · This is the cleanest thing I saw against reading elevated funding as a warning. Persistently rich funding is a **coin trait** (thin book, small cap), not a moment trait · 4

C111, C003, C123, C138, C156 · When elevated before-funding *was* followed by a large move, **the move was up every time — 5 of 5** (+40.69, +7.72, +37.58, +55.55, +27.86 %) · Read off the measured-move lines · Opinion: this is the **opposite** of the usual "crowded longs get flushed" story, which makes me distrust it as much as it interests me. 5 cards, two coins (FHE, KOMA) plus one AVGO — far too few, and it would flip if the story is really about those coins' one-way trends. **An observation resting on 5 events inside 3 coins is not a rule** · 2

C058, C202, C173 · **The three down large-moves in this batch had no elevated before-funding**: C058 max +0.0139, C202 flat at the +0.0050 floor, C173 max +0.0190 · Read off the before funding lines · Opinion: in batch 05 nothing in funding stood ahead of a fall. Note also the batch's direction base rate — **12 of 15 large moments are up**, so any direction claim made here is fighting an 80/20 prior · 3

---

## E · Negative funding before the moment

C036, C265, C206, C023, C039, C160, C021, C275, C175 · **At least one negative before-window payment — 9 of 34 cards.** Large: C265, C175 (2). Calm: C036, C206, C023, C039, C160, C021, C275 (7). 2/9 = 22 % large against a 44 % base rate · Counted off the before funding lines · Opinion: shallow negative funding leans, if anything, toward **calm** — and it is confounded, since 5 of the 9 are BCH or ZRO, the low-volatility coins of the batch · 3

C265, C275, C021, C023, C036 · **All before-window payments negative — 5 of 34 cards**, and only **1 of the 5 (C265) is a large moment**. The other four measured −2.50, +1.05, +3.29, +1.14 % · Read off the before funding lines · So "persistently negative funding" on its own is mostly a calm-moment condition here. The depth matters more than the sign · 4

C265, C175 · **Deep negative before-funding — a payment ≤ −0.030% — appears in only 2 of 34 cards, and both are large moments, both up** (C265 −0.0700 %, move +17.75 %; C175 −0.0362 %, move +11.54 %) · Read off the before funding lines and the measured-move lines. C275/C021/C023/C036 are all-negative but shallow (deepest −0.0188 %) and all calm, which is what makes the depth cut look like it is doing the work · **Two events. This is an observation, not a rule**, and I would expect it to dissolve on a larger set · 2

C265 · The spike is at **h+8: +14.43 % in one hour on 50.71M quote volume against ~0.5M in the hours before**, and at that hour **BTC +0.13 % and ETH +0.07 %** · Read off the after table · **This was not the whole market moving — it belongs to the coin.** Stating it explicitly as the rules require · 5

---

## F · Funding inside the after window is a consequence, not a lead

C190, C058, C072, C245, C173, C252, C138, C085 · **Before-window all positive, after-window turns negative — 8 of 34 cards.** 6 are large (C190, C058, C245, C173, C252, C138); the 2 calm ones are **C072 (−14.11 %) and C085 (−8.61 %), which are the two largest-magnitude moves among all 19 calm cards** (next are C081 +6.28 and C164 −5.28) · Counted off the two funding lines and the measured-move lines of each card · My reading: the flip tracks **size of move**, not the card's label — and since it happens *inside* the after window it is a **restatement of a price move that has already happened**. Useless as a trigger; possibly useful as a check that a rule's exit is not fighting funding · 4

C265 · After-window funding runs **−0.0319, −0.0270, −0.5868, −1.0148, −1.3683, −0.7206 %**, i.e. up to **≈274× the +0.0050 % floor in magnitude**, and the first extreme print (payment 3) lands **after** the h+8 spike, not before it · Read off the after funding line and located against the after table · Extreme funding here is the exchange's arithmetic catching up with a move that already occurred. It says nothing anyone could have traded on at the time · 4

C072 · A card **labelled `calm` whose measured 24 h move is −14.11 %**; the fall is concentrated in h+1…h+7 while BTC over the same hours prints −0.09, −0.71, +0.09, −0.30, −0.22, −0.11, −0.37 — the coin fell far more than the market · Read off the card's own Moment kind line against its own Measured 24-hour move line · Card-integrity flag rather than a field observation: **`calm` on these cards does not mean "small move"**, and any counting of my calm/large splits above inherits that. I raise it because it changes how every count in this file should be read · 4

---

## G · Funding as a cost, which is measurable and not a prediction

C111, C123, C138, C147, C164, C172, C156 vs C222, C084, C081, C091, C267, C292, C237 · **The funding cost of holding a 24 h long differs by more than 10× across cards in the same batch.** Summing the six after-window payments: C111 **+0.3578 %**, C147 +0.1781 %, C138 +0.1772 %, C164 +0.1538 %, C123 +0.1403 %, C172 +0.1253 %, C156 +0.0983 % — against **+0.0300 %** on every floor-clamped card (6 × 0.0050) · Arithmetic on the numbers printed on the cards · This matters for the money test: TACTICS 8 assumes 0.20 % round-trip in fee+slippage, and **C111's 24 h funding alone (0.3578 %) exceeds that whole assumption.** A 24 h-hold rule priced at the floor would be mispriced by up to ~0.33 % per trade on the rich cards · 5

C265 · The same sum with the sign the other way: a 24 h long in the after window would have **received ≈3.75 %** in funding (−0.0319 −0.0270 −0.5868 −1.0148 −1.3683 −0.7206) · Arithmetic on the card's after funding line · Opinion: funding is not a small correction term in the tail — on one card of 34 it is larger than most of the price move being chased. Whoever runs the money test should not treat funding as noise · 4

---

## H · Ideas (trigger · direction · exit)

**Idea 1 — deep negative funding, long.** *Trigger:* at the moment's start hour, at least one of the previous 24 h funding payments is ≤ **−0.030 %**. *Direction:* **buy**. *Exit:* close 24 h after entry, or earlier at the first funding payment that prints ≥ +0.0050 %, whichever comes first. *Evidence in batch 05:* fires on **2 of 34 cards** (C265 +17.75 %, C175 +11.54 %), both large, both up; 0 false fires. *My confidence:* **2** — two events is not evidence, the threshold was picked after looking, and it must be re-cut on cards I have not seen.

**Idea 2 — the clamp as a blocker, not a signal.** *Trigger:* all funding payments in the previous 24 h equal exactly **+0.0050 %**. *Direction:* **no position from this signal** — treat it as "funding contributes zero points", not as a reason to trade. *Exit:* n/a; it never opens a position. *Evidence in batch 05:* fires on **10 of 34 cards**, 4 large / 6 calm versus a 44 % base rate — it separates nothing. *My confidence:* **4** that it is worth writing into a score recipe as an explicit zero rather than leaving the cell blank.

**Idea 3 — funding cost gate on any 24 h-hold rule.** *Trigger:* before entering a 24 h hold, sum the coin's last six (or three) published funding payments; if the sum in the direction of the trade exceeds **+0.20 %** (the assumed round-trip cost). *Direction:* **do not take the long** — block the trade, or require the rule's expected move to clear cost + funding. *Exit:* n/a; it is a gate. *Evidence in batch 05:* would have blocked C111 (0.3578 % over 24 h) and flagged C147/C138/C164 (0.14–0.18 %). *My confidence:* **4** — this is arithmetic on printed numbers, not a forecast; the only open part is whether the trailing sum predicts the forward sum.

---

## I · What I am explicitly **not** claiming

- Nothing here is evidence. It is free observation, and it produces ideas only.
- Every count is out of **34 cards**, from **9 coins** (NIL, NEWT, FARTCOIN, BCH,
  OMNI, KOMA, FHE, ZRO, AVGO). Several of my splits are driven by one or two
  coins and would move if the coin mix moved.
- The announcement / listing / delisting / warning half of my field produced
  **no data on any card**. I did not test it and I am not reporting it as empty.
