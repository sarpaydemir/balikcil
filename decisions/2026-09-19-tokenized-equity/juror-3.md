# Juror 3 — open question, 2026-09-19

**Question:** does the universe definition in `TACTICS.md` section 0 admit a
contract whose underlying is a tokenized equity — a share in a listed company —
rather than a cryptocurrency?

Written without sight of any other juror's answer. I did not open
`decisions/` beyond writing this file.

---

## 1 · Answer

**Yes — as written, the definition admits it:** the only tests it states are
"Binance USDT perpetual futures contract", "traded during this period" and
"present in the archive", and it imposes no condition whatsoever on what the
contract's underlying is, so a tokenized-equity perpetual that meets those three
tests is inside the universe.

---

## 2 · What it rests on

**The defining sentence itself.** `TACTICS.md`, section 0, lines 7–11:

> - **Universe:** every Binance USDT perpetual futures contract that traded
>   during this period. The list is built from the archive
>   (`data.binance.vision`), not from today's exchange, so that coins which died
>   during the period are included too.

Three things carry the answer here, and all three are on the page:

- The noun of the definition is **contract**, not coin, not cryptocurrency, not
  token. The subject of a definition is what the definition is about.
- The quantifier is **"every"**. It is the widest word available, and it is
  followed by exactly one restrictive clause — "that traded during this period"
  — which is about *trading*, not about the underlying.
- The one purpose the sentence gives for its own construction is *inclusion*:
  build from the archive "**so that** coins which died during the period are
  included too". The stated intent of the drafting is to widen the net against
  an accident of who is listed today, not to narrow it by asset class.

A definition that wanted to exclude non-crypto underlyings had the room to say
so in that sentence and does not. I looked for such a clause in the whole of
`TACTICS.md`, the whole of `RULES.md`, the whole of `README.md` and the whole of
`TEAM.md`; there is no sentence anywhere in those four files that restricts the
universe by what the contract tracks. That is a "before saying none, say where
you looked" statement under RULES 20.

**The rule was written first, and the result is being opened second.**
`RULES.md` line 34–36:

> 6. The rule is written first, the result is opened second. A rule is not
>    changed after looking at a result. If it is changed it counts as a new
>    rule, carries the "afterwards" label, and is tested again.

The universe definition and the draw number both pre-date the draw —
`TACTICS.md` line 22: "**Draw number:** `20260913`. Written before the draw; it
does not change." The tokenized-equity character of a drawn contract is a
*result* of that draw, learned afterwards. Reading the definition now as though
it had always contained an unwritten "cryptocurrency only" clause would be
reading a new restriction into a pre-registered rule because of what the
pre-registered rule produced. RULES 6 is the laboratory's own name for why that
is not allowed. This does not make the wide reading *convenient*; it makes it
the reading the laboratory's own discipline requires.

**What the measured artefact shows** —
`/home/user/balikcil/data/observation/external/coin-names.json`, read in full,
10 entries, one per observation contract:

- Eight of the ten resolve by exact symbol match to a cryptocurrency: BCH →
  "Bitcoin Cash", ZRO → "LayerZero", FARTCOIN → "Fartcoin", FHE → "Mind
  Network", NEWT → "Newton Protocol", NIL → "Nillion", OMNI → "OmniCat", KOMA →
  "Koma Inu". All have `"error": null`.
- **AVGOUSDT** has `"error": null` and three exact-symbol hits, and every one of
  them is a wrapper around shares of one listed company:

  > `"id": "broadcom-robinhood-tokenized-stock", "name": "Broadcom • Robinhood Token"`
  > `"id": "broadcom-dinari-tokenized-stock", "name": "Broadcom (Dinari Tokenized Stock)"`
  > `"id": "broadcom-backpack-securities", "name": "Broadcom (Backpack Securities)"`

  with `"source_url": "https://api.coingecko.com/api/v3/search?query=AVGO"`.
  What this measures, stated exactly: in that source, on that endpoint, there is
  **no** entity with symbol AVGO that is a cryptocurrency — the entire exact-hit
  set is tokenized Broadcom stock. What it does **not** measure: the contract
  specification Binance settles `AVGOUSDT` against. A third-party name lookup on
  a base ticker is evidence about the ticker, not a contract spec. I am not
  entitled to more than that from this file (RULES 19).
- **NOKUSDT** is an unknown, not a finding. The record is
  `"error": "CoinGecko search returned 5 coins, none with symbol == NOK"`,
  `"exact_symbol_hits": []`, `"name": null`. RULES 20 —

  > 20. Before saying "none", where we looked and what error we got is written
  >     down. A connection error does not mean "no data".

  — so I record NOK as **not identified** by this artefact. I note, without
  asserting it, that NOK is the ticker of at least one listed company and also
  the ISO code of a national currency; neither is established here, and I do not
  treat NOKUSDT as either.

**The two named contracts are genuinely inside the universe and the draw** —
`/home/user/balikcil/data/universe/universe.csv`, lines 91 and 483:

> `AVGOUSDT,2026-04-20,2026-08-31,134,4834698.5889,new,...`
> `NOKUSDT,2026-06-01,2026-08-31,92,6870909.60965,new,...`

Both carry `group = new`, which is what `TACTICS.md` line 16 prescribes — "**new:**
first trade falls inside the period" — and both appear in
`/home/user/balikcil/data/draw/observation-coins.txt` (lines 9 and 10). So the
question is not hypothetical: the definition has already admitted at least one
contract (AVGOUSDT) whose ticker resolves, in the recorded lookup, exclusively to
tokenized shares. My answer is that it admitted it **correctly**, by its own
terms.

**Reversible and irreversible readings.** The wide reading ("admits") is the
reversible one: a contract that is in can be set aside later, and what is lost is
the observation work already spent on it. The narrow reading ("does not admit")
is the costly one, because it does not merely drop a name — it changes the
population that `TACTICS.md` section 1 ranks and cuts: "ranked by its median
daily trading volume (`quote_volume`) over the period and cut into **three groups
of equal size**". Remove contracts from the population and the group totals and
cut values move, so the output of a draw whose number "does not change" no longer
reproduces. My estimate of the cost, and it is an **estimate**: the full draw and
every list derived from it. I state this only as a property of the two readings.
**What to do about a contract already drawn is not my question and I propose
nothing about it** (instruction, and RULES 33 on a juror's scope).

---

## 3 · The strongest case against my own answer

Put at its best, and I think it is genuinely strong:

**Every other sentence in the laboratory says "coin", and a definition is read in
the document that contains it.** The word "contract" appears in section 0 and
then essentially vanishes. `TACTICS.md` line 14: "Coins are split into four
groups". Line 17: "a new coin is not also ranked by volume". Line 23:
"**Observation:** 10 coins". Line 29: "the names of the **10 observation
coins**". Line 40: "For a coin that did not trade all year this count shrinks in
proportion to its lifetime". `RULES.md` line 41: "In the exam the coin name and
the date are hidden." Line 53: "Moments occurring in several coins in the same
hour". `README.md` line 32: "Coins are picked by lot". And the file naming
follows: the drawn list is literally `observation-coins.txt`. On this reading,
"contract" in section 0 is a *technical description of where the list comes
from* — the archive indexes contracts — while "coin" is the laboratory's word
for **what a universe member is**, and section 0's own tail already slips into
it: "so that **coins** which died during the period are included too", in the
very sentence being construed. A drafter who wrote "coins" inside the defining
sentence plainly had cryptocurrencies in mind.

The purposive limb is stronger still. `README.md` lines 8–10 says the laboratory
watches "what happens while a coin is quiet, what happens before a sharp move,
what the exchange is doing meanwhile, what is happening in the world", and the
card in `TACTICS.md` section 3 is built for crypto: "bitcoin and ethereum, over
the same hours", "number of people viewing the page on Wikipedia (daily)", "the
price of the relevant prediction market, if any". A share in a listed company has
a price driver the card cannot see at all — the company's earnings, its sector,
the equity session clock, the fact that the underlying market closes at night and
at weekends while the perpetual does not. A watcher told to explain a sharp move
in such a contract is being asked to read a card with the cause removed from it,
and `TEAM.md` gives no watcher an equities field of view: Ingrid has exchange
behaviour, Kenji the crowd, Amara "the outside world" (announcements, US release
calendar, Wikipedia, prediction market, bitcoin and ethereum), Lukas price
itself. Under RULES 13 — "If the whole market moved together, that is one event"
— one may even argue the equity-linked contracts are a different market whose
co-movement the machinery is not built to detect.

**Why I still answer as I do.** That case argues persuasively that including such
contracts is *unwise*, and it may well be right about that. It does not show that
the written definition *excludes* them, and those are different questions. Mine
is the second. "Every Binance USDT perpetual futures contract that traded during
this period" is not ambiguous about its test; it is silent about the underlying,
and silence in a rule written before the result is not a hidden clause — under
RULES 6 it is a gap, and filling a gap after seeing the result is a **new** rule,
"carries the 'afterwards' label, and is tested again". A juror may not write that
rule: RULES 33 — "A juror decides procedure and definition only: never a trading
rule, never a threshold or score, and never a change to a rule in this file."
So the honest finding is: the definition admits these contracts, and whether it
*should* is a different question for a different body.

I also record, because it cuts against tidiness, that I could not identify
NOKUSDT at all from the permitted artefact. If the class of contracts at issue
turns out to include a currency-linked contract as well as an equity-linked one,
the question put to this jury does not cover it, and I have not answered it.

---

## 4 · Confidence

**4 of 5.**

Four and not five because the drafting is genuinely split: the defining noun is
"contract" and almost every other noun in the laboratory is "coin", and I can
read the mind of the drafter as having meant crypto. I am confident about what
the text *admits*; I am not confident the drafter foresaw this case, and I think
it likely they did not.

**What would change my mind:**

- A sentence anywhere in `RULES.md`, `TACTICS.md`, `README.md` or `TEAM.md`
  restricting the universe by asset class or by underlying, that I failed to
  find. I read all four in full; a quoted line would overturn me immediately.
- Evidence that `data.binance.vision` files these symbols under a product
  family that is *not* USDT perpetual futures — that would fail the definition's
  own first test on its own terms, with no reinterpretation needed, and my
  answer would become "no" for AVGOUSDT without any rule changing.
- A pre-2026-09-19 record showing the universe definition was written with the
  narrow meaning stated. That would be evidence about the rule as written rather
  than a change to it, and RULES 6 would then cut the other way. I could not look
  for this: `LEDGER.md` and `instructions/` are closed to me for this question.

**What would not change my mind:** a demonstration that such contracts are bad to
observe. I accept that argument may be correct and it does not bear on what the
sentence admits.

---

## Files I read

- `/home/user/balikcil/RULES.md` (whole)
- `/home/user/balikcil/TACTICS.md` (whole)
- `/home/user/balikcil/README.md` (whole)
- `/home/user/balikcil/TEAM.md` (whole)
- `/home/user/balikcil/data/observation/external/coin-names.json` (whole, 10 entries)
- `/home/user/balikcil/data/draw/observation-coins.txt` (whole, 10 lines)
- `/home/user/balikcil/data/universe/universe.csv` (header, first rows, and the
  rows for AVGOUSDT, NOKUSDT, BCHUSDT, FARTCOINUSDT by search — not the whole
  file)

Not opened: `exam/`, `decisions/` (other than writing this file), `LEDGER.md`,
`instructions/`, `notes/`, `canteen/`, `cards/`, `reports/`, `scripts/`, and
nothing outside `/home/user/balikcil`. I saw no other juror's answer.

## Assumptions the instruction did not cover, by name

1. **"Tokenized equity" was not defined for me beyond "a share in a listed
   company".** I took it to mean: a contract whose price is intended to track
   the shares of a company listed on a stock exchange, however the tracking is
   implemented. Nothing in my answer depends on the implementation.
2. **I treated `coin-names.json` as a name lookup, not as a contract
   specification.** It records a CoinGecko search on a base ticker; it is
   evidence about what entities share that ticker, and I did not let it stand
   for what Binance settles the contract against.
3. **I assumed `universe.csv` is the artefact `TACTICS.md` section 0 describes**
   ("built from the archive"). The file itself carries no provenance header
   saying so; I was given it under that description and its columns
   (`first_day_archive`, `last_month_in_archive`) are consistent with it.
4. **I read "traded during this period" as satisfied by the `days_with_trades`
   column** being greater than zero inside the period, which is how both named
   rows read.
