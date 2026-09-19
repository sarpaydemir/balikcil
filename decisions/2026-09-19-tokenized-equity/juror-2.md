# Juror 2 — open question of 2026-09-19: does the universe definition admit a tokenized equity?

**Question as put to me:** `TACTICS.md` section 0 defines this laboratory's
universe. Does that definition admit a contract whose underlying is a tokenized
equity — a share in a listed company — rather than a cryptocurrency?

**Scope:** procedure and definition only. I say what the definition admits and
stop. I set no threshold, no score, no trading rule, and I propose no remedy
(RULES 33; instruction's "What is not yours to answer").

---

## 1 · Answer

**Yes — as written, the definition admits it:** section 0 tests only that a
thing is a Binance USDT perpetual futures contract and that it traded during
the period, and neither test says anything about what the contract's underlying
is.

## 2 · What it rests on

**The definition itself.** `TACTICS.md`, section "0 · Period and universe",
lines 7–10:

> - **Universe:** every Binance USDT perpetual futures contract that traded
>   during this period. The list is built from the archive
>   (`data.binance.vision`), not from today's exchange, so that coins which died
>   during the period are included too.

Two conditions, joined: *(a)* Binance USDT perpetual futures contract, *(b)*
traded during the period. Both are properties of the **contract and its trading
record**, not of the asset the contract references. The qualifier "every" is
inclusive and is not narrowed anywhere in the sentence. The second sentence
narrows only the **source** (archive, not today's exchange) and does so in order
to *widen* membership ("so that coins which died during the period are included
too"), not to restrict it.

**Nothing elsewhere in the four governing documents conditions membership on the
underlying.** Before writing "none" (RULES 20), here is where I looked: the full
text of `RULES.md` (146 lines), `TACTICS.md` (174 lines), `README.md` (84
lines), `TEAM.md` (174 lines). No line in any of the four makes universe
membership depend on the underlying being a cryptocurrency, a token, or
anything else. The only membership criteria I found anywhere are the two in
section 0 above, plus the group-assignment criteria in `TACTICS.md` section 1,
which are likewise purely mechanical — line 15:

> - **new:** first trade falls inside the period.

That is a date test on the trading record. It admits any contract whose first
trade falls inside the period.

**The laboratory's own counting unit is the contract.** `README.md`, line 79:

> First run `2026-09-18`: the universe was built from the archive and the draw
> was made (795 contracts; 10 observation · 20 exam · 765 money test).

The lab counted its universe in **contracts**, consistent with section 0's
wording.

**Why the timing of the reading matters — RULES 6**, lines 34–36:

> 6. The rule is written first, the result is opened second. A rule is not
>    changed after looking at a result. If it is changed it counts as a new
>    rule, carries the "afterwards" label, and is tested again.

The universe definition and the draw number (`TACTICS.md` line 22: "**Draw
number:** `20260913`. Written before the draw; it does not change.") were fixed
before the draw was opened. Reading an asset-class restriction *into* section 0
now, after seeing which contracts came out, is exactly the move RULES 6
forbids: it would be a narrower rule, and by RULES 6's own terms it would be a
**new** rule carrying the "afterwards" label — not a reading of the existing
one. So the honest answer to "what does the definition admit" cannot be shaped
by what the draw produced.

**What `coin-names.json` shows, and what it does not.**
`data/observation/external/coin-names.json` is a per-contract lookup against
`https://api.coingecko.com/api/v3/search`, with each record carrying its
`source_url`, its `exact_symbol_hits`, its `name` and its `error`.

- **AVGOUSDT** (`base_ticker` `"AVGO"`, `"error": null`): every exact-symbol hit
  is a tokenized wrapper of the same listed company —
  `"broadcom-robinhood-tokenized-stock"` / `"Broadcom • Robinhood Token"`,
  `"broadcom-dinari-tokenized-stock"` / `"Broadcom (Dinari Tokenized Stock)"`,
  and `"broadcom-backpack-securities"` / `"Broadcom (Backpack Securities)"`.
  There is **no** hit on that ticker that is an ordinary cryptocurrency. This is
  strong evidence that at least one drawn contract references a listed
  company's shares rather than a coin. It is **evidence, not a specification**:
  a third-party search endpoint is not Binance's own contract definition, and I
  was not given a Binance-sourced spec to confirm it. I record that as an
  unknown by name (RULES 22).
- **NOKUSDT** carries `"name": null` and
  `"error": "CoinGecko search returned 5 coins, none with symbol == NOK"`, with
  `"exact_symbol_hits": []`. This is a **successful lookup with a negative
  result**, not a connection failure — the endpoint answered with five coins and
  none matched. Per RULES 20 ("A connection error does not mean 'no data'"), the
  distinction is recorded correctly in the file. But the record identifies
  NOKUSDT as **nothing at all**. It does not establish that NOKUSDT's underlying
  is a tokenized equity; absence of a CoinGecko coin on that ticker is not a
  positive identification. Anyone who treats this record as a second confirmed
  instance is writing an unmeasured claim (RULES 19).
- The remaining eight records resolve to ordinary crypto assets (Bitcoin Cash,
  LayerZero, Fartcoin, Mind Network, Newton Protocol, Nillion, OmniCat, Koma
  Inu). `OMNIUSDT` resolves ambiguously — five exact-symbol hits, the file
  picking `"OmniCat"` — which is a naming problem, not an asset-class one, and
  is not the question I was asked.

**Measured, from `data/universe/universe.csv` (header line 1, rows as quoted):**

    AVGOUSDT,2026-04-20,2026-08-31,134,4834698.5889,new,2026-04-20,...
    NOKUSDT,2026-06-01,2026-08-31,92,6870909.60965,new,2026-06-01,...

Both carry `group` = `new`, and both are in `data/draw/observation-coins.txt`.
The other eight drawn contracts carry `large` (BCHUSDT, FARTCOINUSDT, ZROUSDT),
`mid` (FHEUSDT, NEWTUSDT, NILUSDT) and `small` (OMNIUSDT, KOMAUSDT), which
matches `TACTICS.md` line 23 ("**Observation:** 10 coins (3 large · 3 mid · 2
small · 2 new)"). So AVGOUSDT and NOKUSDT occupy **both** of the two `new`
slots. I state this as a measured fact about the drawn set; what follows from it
is not mine to say.

## 3 · The strongest case against my answer

It is a real case, and it is the purposive one.

**The definition calls its own members "coins" — inside the defining
sentence.** `TACTICS.md` line 9: "so that **coins** which died during the period
are included too." The author, in the act of defining the universe, named its
inhabitants coins. That is not a stray word elsewhere in the document; it is in
the definition. On this reading "contract" in the first clause is doing narrow
work — distinguishing a *perpetual future* from spot, and USDT-margined from
coin-margined — and is not an asset-class-neutral choice at all. "USDT perpetual
futures contract" is one noun phrase naming an instrument type; reading
"contract" as a deliberate widening beyond crypto reads intent into a phrase
that had another job.

**The rest of the corpus is written on a crypto premise, consistently.**
`TACTICS.md` line 19 ("ranked by its median daily trading volume ... over the
period"), line 40 ("For a **coin** that did not trade all year"), line 61
("**bitcoin and ethereum**, over the same hours" — a crypto benchmark placed on
*every* card), line 100 ("the **coin** name"); `RULES.md` line 41 ("In the exam
the **coin** name and the date are hidden"); `README.md` line 32 ("**Coins** are
picked by lot"), line 9 ("what happens while a **coin** is quiet"). A reader
asking "what did this laboratory think it was studying" gets one answer from a
dozen places.

**One rule's machinery arguably assumes a single market.** `RULES.md` lines
53–54:

> 13. Moments occurring in several coins in the same hour count as a single
>     event. If the whole market moved together, that is one event.

"The whole market" is calibrated on the thing the other members share. A
contract whose underlying moves with the equity market, on equity trading hours,
is not co-moving with the crypto members, so this de-duplication rule behaves
differently for it. That is a genuine argument that the corpus assumed a
homogeneous universe.

**Why I still answer yes.** These citations show what the author most likely
*expected*, not what the rule *says*. "Coin" is used throughout as the ordinary
word for a universe member — it is descriptive, not a second membership test,
and it never appears in the form "only if". The laboratory's whole method is
built on preferring the written criterion to the remembered intention (RULES 6;
RULES 8's insistence that an idea without all three written parts "is not an
idea, because it cannot be tested"). If an unwritten asset-class premise can
silently narrow a written definition after the draw, then the definition was
never the thing doing the work. I also note honestly that the counter-case is
strong enough that it should not be waved away: the right characterisation is
**the definition admits it, and probably did so unintentionally** — those are
two different findings and only the first is mine to make.

**Reversible vs irreversible.** "Admits" is the reversible reading: it leaves
the drawn set as it stands, and a later jury can still narrow the universe
prospectively. "Does not admit" is the costlier reading, because it disturbs
artefacts the rules declare fixed — the draw number ("it does not change",
`TACTICS.md` line 22) and the append-only record (RULES 30: "Records are
append-only"). I give no figure for that cost because I have measured none
(RULES 19), and the remedy is a separate jury's question, not mine.

## 4 · Confidence

**4 of 5.**

Four and not five because the counter-case in part 3 is real: the word "coin"
sits inside the defining sentence itself, and I may be reading a phrase
("contract") as a choice when it was a convention.

**What would change my mind:**

- Any line in `RULES.md`, `TACTICS.md`, `README.md` or `TEAM.md` that conditions
  universe membership on the underlying — I read all four in full and found
  none, but I read them today, at one sitting.
- A document in the laboratory that defines "coin" as a *term of art* with a
  membership test attached, rather than as the ordinary word for a universe
  member.
- Evidence that section 0's word "contract" was written to mean "instrument
  type" explicitly and to say nothing about breadth.

**What would *not* change my mind:** anything about how many such contracts were
drawn, or what it would cost to act either way. Those bear on the remedy, not on
what the definition admits, and RULES 6 makes consequences an illegitimate input
to reading a rule written beforehand.

---

## Files I read

- `/home/user/balikcil/RULES.md` (full)
- `/home/user/balikcil/TACTICS.md` (full)
- `/home/user/balikcil/README.md` (full)
- `/home/user/balikcil/TEAM.md` (full)
- `/home/user/balikcil/data/observation/external/coin-names.json` (full)
- `/home/user/balikcil/data/draw/observation-coins.txt` (full)
- `/home/user/balikcil/data/universe/universe.csv` (header plus the ten drawn
  rows, by search; not read in full)

I opened no file in `exam/`, none in `decisions/`, and nothing outside
`/home/user/balikcil`. I saw no other juror's answer.

## What I had to assume

1. **That "tokenized equity" needs no definition from the corpus.** Neither
   `RULES.md` nor `TACTICS.md` defines the term. I took the instruction's own
   gloss — "a share in a listed company" — as the working meaning.
2. **That CoinGecko's exact-symbol hits are a fair identification of AVGO.** The
   file records the endpoint, the query and the result, satisfying RULES 2 and
   27, but a third-party search is not Binance's contract specification. Flagged
   above as an unknown.
3. **That the question asks what the definition *admits*, not what it *should*
   admit.** The second is a rule change and is closed to me (RULES 33).
4. **That `universe.csv`'s `group` column is the draw's group assignment**
   described at `TACTICS.md` lines 14–21. The file carries no data dictionary; I
   inferred it from the column values matching the four group names.

## Steer seen in the instruction

I report one, at the threshold (RULES 3: an instruction "contains no result, no
prediction, and no 'pay attention to X' steer"):

- **"The definition is written in terms of contracts."** This sentence is true
  of the file, but it is the single observation that decides the question, handed
  to me before I opened the file. A neutral framing would have stopped at
  "`TACTICS.md` section 0 defines this laboratory's universe." I record it so the
  referee can weigh it; I did read section 0 in full and the case in part 3 is
  built from the words the steer left out, but I cannot certify that being told
  this first had no effect on me.
- **Lesser, and probably unavoidable:** being pointed at `coin-names.json`, which
  contains the Broadcom tokenized-stock hits, is direction-setting in that the
  evidence is one-sided by nature. I do not think this could have been avoided
  without withholding the evidence entirely.

**To the instruction's credit**, it carried an explicit anti-steer — "Nothing has
been decided on this question. No answer exists to agree or disagree with, and no
work has been done either way" — and an explicit scope fence around the remedy.
Both worked on me: I had no prior answer to anchor to.
