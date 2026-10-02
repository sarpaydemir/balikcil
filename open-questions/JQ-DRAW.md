# JQ-DRAW · Which moments of the exam pool become the 400 exam cards

**Identifier:** `JQ-DRAW` · **Version:** 2 · **Parts:** `JQ-DRAW-a`, `JQ-DRAW-b`,
`JQ-DRAW-c`, `JQ-DRAW-d`

This file names none of the exam coins and gives no date and no price.

---

## 1 · The point

`TACTICS.md` §6, lines 99–100, says the exam uses 400 cards prepared from the
exam coins: 200 from before a large movement and 200 from calm moments.
`TACTICS.md` §2, lines 33–44, says how the large-movement moments and the calm
moments of each of the coins are found. That procedure has been run for the
exam coins. What it found is called **the pool** below. Every moment in the pool
belongs to exactly one of the exam coins; below, each of the exam coins is
called a **symbol**, and no symbol is named.

These facts about the pool were measured. A juror is not sent to check them.

1. The pool holds more than 200 large-movement moments and more than 200 calm
   moments.
2. For each symbol, the pool holds exactly as many calm moments as
   large-movement moments.
3. No two moments in the pool share both start hour and symbol.
4. `TACTICS.md` §2 names no measure for the size of a 24-hour movement. The pool
   was found with this one: the closing price of the 24th hour, counting the
   start hour as the first, divided by the closing price of the hour just before
   the start, minus one. The size is the absolute value of that change. Measured
   instead as the change in the logarithm of the closing price over the same
   hours, the pool's large-movement moments rank differently, and the 200
   largest are not the same 200.
5. The draw number written at `TACTICS.md` line 22 has already seeded at least
   two random draws: the draw of coins in `TACTICS.md` §1, and the random choice
   of the pool's calm moments under `TACTICS.md` §2 line 42.

So in each kind the pool holds more moments than the exam needs, and something
has to decide which moments become cards. This question asks what decides it.

## 2 · What this question does not ask

- what a card shows, what is hidden from it, or how its price is converted;
- the order in which cards are given;
- how cards that share an hour are counted or scored;
- the answer key, or how it is sealed;
- how the pool was found, or the counts 400, 200 and 200.

---

## 3 · How to answer

Answer every part, each by itself, whatever you answer in the other parts. In
each part, choose one outcome. Each part is counted by itself.

Three outcomes are open in every part:

- **Settled.** The written rules already settle this. Cite the file and line it
  rests upon, and say what they require.
- **Outside.** This is outside what a juror can decide. Cite the file and line it
  rests upon, and say which limit in RULES 33 it crosses.
- **Other.** State it in full, so that it can be carried out with no further
  choice. In part a or part b, if it draws at random, it takes its seed from
  part c, and it also states how its draw is carried out and whether it comes
  before or after the other part's draw.

**Which procedures are listed.** Parts a and b each list two procedures, chosen
by one rule and no other:

- (i) the draw that gives every moment of that kind in the pool the same chance;
- (ii) the procedure that applies to the cards what `TACTICS.md` §2 says about
  choosing that kind of moment, using only counts that the written rules or
  part a supply. For large-movement moments §2 says largest first (lines
  36–38). For calm moments it says the same number as the large-movement
  moments of the same symbol, chosen at random (line 42).

Any other procedure is open under **Other**.

**Order.** In each part, the outcomes that belong to that part alone come first;
where there are two, they are in alphabetical order of their short names.
Settled, Outside and Other follow, in that order, in every part. Neither order
means anything.

### JQ-DRAW-a · the 200 large-movement cards

Which of the pool's large-movement moments become the 200 large-movement cards?

- **Even chance.** 200 moments drawn at random from all the pool's
  large-movement moments, each with the same chance. The draw is carried out as
  part d says.
- **Largest.** The 200 moments whose 24-hour change is largest in size, measured
  as in fact 4. Ties go to the earlier start hour, then to the symbol that comes
  first in alphabetical order.
- **Settled.**
- **Outside.**
- **Other.**

### JQ-DRAW-b · the 200 calm cards

Which of the pool's calm moments become the 200 calm cards?

- **Even chance.** 200 moments drawn at random from all the pool's calm moments,
  each with the same chance, without regard to part a. The draw is carried out
  as part d says.
- **Symbol-matched.** Each symbol gets as many calm cards as the outcome of part
  a gives it large-movement cards. They are drawn at random from that symbol's
  calm moments in the pool, each with the same chance. The draw is carried out
  as part d says.
- **Settled.**
- **Outside.**
- **Other.**

### JQ-DRAW-c · the seed

If the outcomes ratified for this question draw anything at random, what number
seeds the draw?

- **Draw number.** The draw number written at `TACTICS.md` line 22.
- **Settled.**
- **Outside.**
- **Other.** A number, stated, and where it is written before the draw.

### JQ-DRAW-d · how a random draw is carried out

If an outcome listed in part a or part b that draws at random is ratified, how
is the draw carried out?

Measured with a thousand seeds other than the draw number: with the same seed, a
draw picked different moments whenever any one of these was done differently.

- the order in which the moments are listed before the draw;
- the way the generator is used to pick;
- when both parts draw at random and part b's draw does not depend upon part
  a's, whether part a's draw or part b's draw comes first;
- under Symbol-matched, the order in which the symbols are taken.

The outcomes:

- **Section 4.** As written in section 4 of this file.
- **Settled.**
- **Outside.**
- **Other.** A procedure stated in full that covers every outcome listed in parts
  a and b that draws at random.

---

## 4 · The procedure named in JQ-DRAW-d

This procedure covers the outcomes listed in parts a and b.

1. The moments of one kind are listed by start hour, earliest first, and then by
   symbol in alphabetical order. By fact 3 this gives every moment a single
   place in the list.
2. The whole draw uses one generator, created once: Python's
   `random.Random(seed)`, with the seed from part c. The exact Python version
   is written down before the draw.
3. If part a's ratified outcome is **Even chance**, its draw comes first:
   `sample(large-movement list, 200)`. Part b's draw comes next. Under **Even
   chance** it is `sample(calm list, 200)`. Under **Symbol-matched** the symbols
   are taken in alphabetical order, and for each symbol the draw is
   `sample(that symbol's calm moments, listed as in step 1, k)`, where `k` is
   the number of large-movement cards that symbol has.
4. The generator is used for nothing else.

## 5 · What can be carried out together

- Each procedure listed in parts a and b chooses 200 moments from a list that
  holds more than 200 (fact 1).
- **Symbol-matched** needs the 200 large-movement cards that the outcome
  ratified for part a chooses. Under either procedure listed in part a it can
  always be carried out: no symbol gets more large-movement cards than it has
  large-movement moments, and by fact 2 it has as many calm moments. Under
  Settled or Other in part a, it can be carried out if that outcome chooses 200
  of the pool's large-movement moments.
- An outcome of part a or part b that draws at random needs a seed from part c.
  A listed outcome that draws at random also needs a procedure from part d.
  Parts c and d are used only if such an outcome is ratified.

These combinations **cannot** be carried out from this question alone:

- a part with no ratified outcome;
- part a or part b ratified as Outside, or as Settled or Other where that
  outcome chooses no moments;
- an outcome that draws at random, with part c ratified as Outside, or as
  Settled or Other where that outcome gives no number;
- a listed outcome that draws at random, with part d ratified as Outside, or as
  Settled or Other where that outcome gives no procedure;
- an Other in part a or part b that draws at random and does not state how its
  draw is carried out;
- **Symbol-matched**, with an outcome of part a that does not choose 200 of the
  pool's large-movement moments.

This file does not say what happens in those cases.

## 6 · What a juror needs

This file, `RULES.md`, `TACTICS.md`, `TEAM.md` and `README.md`, and the
`verdict.md` in each of these ten folders under `decisions/` (each folder's name
ends as shown):

- `-separation`
- `-requirement`
- `-level`
- `-selection`
- `-equity`
- `-runs`
- `-contracts`
- `-canteen-8`
- `-gate`
- `-carries`

Nothing else. The facts in section 1 are stated so that no other file is needed.

## 7 · Answer form

For each part, as `TEAM.md` lines 113–115 set out for jurors, give:

- the outcome you choose;
- the file and line it rests upon, quoted (RULES 34);
- the strongest case against your answer;
- your confidence, from 1 to 5.
