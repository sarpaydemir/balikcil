# Juror 1 — open question, 2026-09-19

**Question:** Does the universe definition in `TACTICS.md` section 0 admit a
contract whose underlying is a tokenized equity — a share in a listed company —
rather than a cryptocurrency?

---

## 1 · Answer

**Yes — as written, the definition admits it:** its three conditions are venue,
instrument type and having traded in the period, and the nature of the
underlying is not one of them, so a Binance USDT perpetual futures contract on a
tokenized equity that traded during the period is inside the universe.

## 2 · What it rests on

**The definition itself.** `TACTICS.md` line 7–10:

> - **Universe:** every Binance USDT perpetual futures contract that traded
>   during this period. The list is built from the archive
>   (`data.binance.vision`), not from today's exchange, so that coins which died
>   during the period are included too.

Three conditions, and only three: (a) **Binance**, (b) **USDT perpetual futures
contract**, (c) **traded during this period**. There is no fourth condition
about what the contract's price references. The sentence selects at the level of
the **contract**, not the level of the asset behind it.

**The word "contract" is the operative noun, and it is deliberate.** Grepping
`TACTICS.md` for `crypto|equit|stock|share|underlying|asset class|contract`
returns exactly one line — line 7, the universe definition. Grepping `RULES.md`
for the same pattern returns **no matches**. Neither document anywhere restricts
the asset class. Where I looked for such a restriction (RULES 20): the whole of
`RULES.md`, the whole of `TACTICS.md`, the whole of `README.md`, the whole of
`TEAM.md`, plus the greps above. I found none.

**Membership is decided by the archive, not by a judgement about the underlying.**
The same line fixes the source — "built from the archive (`data.binance.vision`),
not from today's exchange". Whether a symbol is in the universe is a question
about what is in the archive. Deciding membership by asking "what does this
contract really track?" replaces a mechanical, reproducible test with a
judgement call, which is the opposite of what that sentence is doing.

**The laboratory already counts its universe in contracts.** `README.md` line 78:

> universe was built from the archive and the draw was made (795 contracts; 10

Not "795 coins". The count of the universe is a count of contracts.

**What `coin-names.json` shows.** Reading
`data/observation/external/coin-names.json` for myself: of the ten observation
contracts, eight resolve to an exact-symbol cryptocurrency (BCH → Bitcoin Cash,
ZRO → LayerZero, FARTCOIN → Fartcoin, FHE → Mind Network, NEWT → Newton
Protocol, NIL → Nillion, OMNI → OmniCat, KOMA → Koma Inu). Two do not:

- **`AVGOUSDT`.** All three exact-symbol hits are tokenized representations of
  one listed company's shares, and none is a cryptocurrency:

  > "id": "broadcom-robinhood-tokenized-stock", "name": "Broadcom • Robinhood Token"
  > "id": "broadcom-dinari-tokenized-stock", "name": "Broadcom (Dinari Tokenized Stock)"
  > "id": "broadcom-backpack-securities", "name": "Broadcom (Backpack Securities)"

  `"error": null` — the lookup succeeded, and the CoinGecko search endpoint
  simply knows no coin with the symbol AVGO. Stated precisely, and no further:
  **the file shows that no cryptocurrency carries the ticker AVGO and that the
  ticker belongs to a listed company's tokenized shares.** It is a CoinGecko
  name lookup, not a Binance contract specification, so it is strong indirect
  evidence about the underlying, not a measurement of it. I did not read a
  Binance contract spec; none was among the files I may look at.

- **`NOKUSDT` is unresolved and I will not guess it.**

  > "error": "CoinGecko search returned 5 coins, none with symbol == NOK",
  > "name": null

  The lookup ran and returned a result — this is not a connection failure
  (RULES 20) — but it identifies nothing. NOK is the ticker of a listed company
  and also of a national currency and could be neither here. **Unknown, by
  name** (RULES 22). It does not affect my answer, because my answer is about
  what the definition admits, not about how many admitted contracts there are.

**Both are in the drawn universe, measured.** `data/draw/observation-coins.txt`
lists `AVGOUSDT` (line 9) and `NOKUSDT` (line 10). `data/universe/universe.csv`
line 91 gives `AVGOUSDT,2026-04-20,2026-08-31,134,4834698.5889,new,...,0,134,
7412049`, and line 483 gives `NOKUSDT,2026-06-01,2026-08-31,92,6870909.60965,
new,...,0,92,3729747`. Both satisfy condition (c) on the archive's own evidence.

**RULES 6 points the same way.** `RULES.md` line 34–36:

> 6. The rule is written first, the result is opened second. A rule is not
>    changed after looking at a result. If it is changed it counts as a new
>    rule, carries the "afterwards" label, and is tested again.

The universe rule and the draw number (`TACTICS.md` line 22: "**Draw number:**
`20260913`. Written before the draw; it does not change.") were fixed before
anyone looked up what AVGO was. Reading the definition today as though it had
always excluded equity underliers — rather than admitting that it did not and
that this is new knowledge — would be changing a rule after seeing a result
while denying that anything changed. Whatever is done next, the honest reading
of the rule *as written* is that it admits.

## 3 · The strongest case against my own answer

**The rest of the document is written about coins, not contracts, and a
definition is read in the company it keeps.** "Contract" appears once in
`TACTICS.md`; **"coin" appears 20 times** (measured by grep). The universe
sentence itself ends with "so that **coins** which died during the period are
included too" — the definition's own final clause glosses its subject as coins.
Section 1 says "**Coins** are split into four groups", section 2 says "The
largest 20 of the year are taken for each **coin**", `README.md` line 9 asks
"what happens while a **coin** is quiet". On that reading "contract" is merely
the technical form in which a coin is traded on Binance, and the author never
contemplated an equity underlier; the intended universe is crypto, and my
answer is a lawyer's reading that defeats the plain intent.

The methodological half of this objection is stronger still, and I think it is
the real one. The laboratory's instruments assume a market that never closes:
`TACTICS.md` line 34 "Hourly closing prices are used", line 37 "The largest 20
of the year", RULES 13 "Moments occurring in several coins in the same hour
count as a single event. If the whole market moved together, that is one event."
A share in a listed company has an underlying that trades roughly six and a half
hours a weekday and gaps over weekends, earnings dates and corporate actions —
and RULES 13's notion of "the whole market" means the crypto market, which is
not the market that moves an equity. A contract like that could manufacture
moments that the whole apparatus would misread.

Two things blunt it, and I record both rather than only the one that suits me.
First, it is an argument about **whether the instruments fit**, not about
**what the sentence says** — and the question put to me is the second. Second,
the fit is better than the objection assumes: `universe.csv` line 91 records
`AVGOUSDT` with `days_with_zero_trades` = 0 and `days_with_trades` = 134 over
2026-04-20 → 2026-08-31 (134 days), and line 483 records `NOKUSDT` with
`days_with_zero_trades` = 0 and 92 days of trades over 2026-06-01 → 2026-08-31
(92 days). The **contracts** traded every single day, weekends included. The
hourly series the cards are built from does not have the holes the objection
predicts. Nothing in `TACTICS.md` section 3's card list becomes impossible
either.

I do not think this defeats my answer, but I hold it honestly: if the
laboratory concludes it meant crypto, the text it would point to is its own word
"coins" in the very same sentence, and that is not a frivolous reading.

**Which reading is reversible.** "The definition admits it" is the **reversible**
direction: it changes nothing, the drawn lists stand, and if a later jury
narrows the universe the narrowing is simply applied then. "The definition does
not admit it" is the **irreversible and expensive** direction: it invalidates
the universe list, and the draw keyed to it, and everything built on the draw.
Cost to reverse later, **estimate, unmeasured**: a re-built universe file, a
re-run draw under an unchanged draw number, and re-downloaded data for every
replacement contract — plus the "afterwards" label and a re-test under RULES 6.
Per `TACTICS.md` line 28–30 the observation names and each list's fingerprint
are already written into `LEDGER.md`; `LEDGER.md` is closed to me, so I did not
read it and cannot say what is recorded there.

I say what the definition admits and stop there. What should be done about a
contract already drawn is not mine, and I propose nothing.

## 4 · Confidence

**4 / 5.**

Four and not five because the counter-argument in part 3 is real: the
definition's own closing clause says "coins", and I am reading the operative
noun against the document's habitual one. Four and not three because the
operative noun is the one that does the selecting, because `RULES.md` contains
no asset-class restriction at all, because the definition explicitly delegates
membership to the archive rather than to judgement, and because `README.md`
counts the universe in contracts.

**What would change my mind:**
- Any line in `RULES.md` or `TACTICS.md` restricting the underlying asset class
  that I failed to find. I searched all four root documents and the two greps
  above; if one exists, my answer is simply wrong.
- A Binance contract specification showing `AVGOUSDT` does **not** settle on a
  listed company's share price — that would dissolve the question rather than
  answer it, since then no such contract is in the universe to begin with.
- A demonstration that a card cannot be built for these contracts at all — that
  would not change what the definition *admits*, but it would make the answer
  academic, and I would say so.

**What would not change my mind:** a showing that an equity-underlier contract
is bad for the experiment. That is an argument for asking the user to change the
rule (RULES 3–4, and RULES 33 forbids me to change one). It is not a reading of
the sentence that exists.

---

### Files I read

- `/home/user/balikcil/RULES.md` (whole)
- `/home/user/balikcil/TACTICS.md` (whole)
- `/home/user/balikcil/README.md` (whole)
- `/home/user/balikcil/TEAM.md` (whole)
- `/home/user/balikcil/data/observation/external/coin-names.json` (whole)
- `/home/user/balikcil/data/draw/observation-coins.txt` (whole)
- `/home/user/balikcil/data/universe/universe.csv` (header, first rows, and the
  three rows matching AVGOUSDT / NOKUSDT / BCHUSDT)

I did not open `exam/`, `decisions/` (other than writing this file),
`LEDGER.md`, `instructions/`, `notes/`, `canteen/`, `reports/` or `scripts/`,
and nothing outside this folder. **Incident:** one grep of mine was globbed
`*.md` across the folder and matched files in `cards/`, which is closed to me;
its preview showed me three lines from card files about a Wikipedia
article-matching rule. I stopped, did not open the saved output, and re-ran the
search file by file. Those lines played no part in this answer; I record the
exposure rather than hide it.

### What I had to assume, by name

1. **That `AVGOUSDT`'s underlying is in fact Broadcom's share price.** I have a
   CoinGecko name lookup, not a Binance contract spec. My answer does not
   actually depend on this — it is a reading of the definition, and holds
   whether or not any such contract exists — but the question is only live if
   one does.
2. **That the ten entries in `coin-names.json` are the ten observation
   contracts and were fetched as recorded.** The file carries a `source_url`
   per entry and I took the fetch at face value; I did not re-fetch and could
   not, having no network tool.
3. **That `NOKUSDT` is unidentified,** not identified-as-something. I treat it
   as unknown throughout.

### Steer in the instruction

The instruction is clean on the decisive point: it states the question, names
the files, and says "**Nothing has been decided on this question.** No answer
exists to agree or disagree with", and "Read it and decide for yourself what it
shows." Pointing a juror at a file is permitted — RULES 3: "Agents are not told
what to look for, only what they may look at."

Two asymmetries I record, neither of which changed my answer:

1. **The question's own title, "tokenized equities in the universe", and the
   decision folder name `2026-09-19-tokenized-equity`, presuppose that a
   tokenized-equity contract is in the universe.** That is close to handing over
   a result. In practice it told me nothing I did not then verify myself from
   `coin-names.json`, and the presupposition is arguably unavoidable in stating
   the question at all — but a juror was told part of the finding before
   reading the file.
2. **Only one branch got a follow-up clause:** "If your answer is that such
   contracts do not belong, the remedy is a separate question for a separate
   jury". The symmetric branch is not written. A conditional written for one
   answer and not the other makes that answer the anticipated one. It is a
   scope limit rather than a prediction, so I do not call it a RULES 3 breach —
   but it is asymmetric, and I answered the other way, so it did not carry me.
