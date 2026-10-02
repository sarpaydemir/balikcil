# JQ-DRAW · Which moments of the exam pool become the 400 exam cards

**Identifier:** `JQ-DRAW` · **Parts:** `JQ-DRAW-a`, `JQ-DRAW-b`, `JQ-DRAW-c`

This file names no exam coin and gives no date and no price. Where a coin must
be referred to at all, it is by its line number (1–20) in the laboratory's fixed
list of exam coins. A juror does not need that list.

---

## 1 · The point

`TACTICS.md` §6, lines 99–100, says the exam uses 400 cards prepared from the
exam coins: 200 from before a large movement and 200 from calm moments.
`TACTICS.md` §2 says how a coin's large-movement moments and calm moments are
found. That procedure has been run on the exam coins. What it found is called
**the pool** below.

The question cannot be posed without two measured facts about the pool:

1. The pool holds more than 200 large-movement moments and more than 200 calm
   moments.
2. Every exam coin has exactly as many calm moments in the pool as it has
   large-movement moments.

So in each kind the pool is larger than the exam needs, and something has to
decide which moments become cards. This question asks what decides it.

## 2 · What this question does not ask

- what a card shows, what is hidden on it, or how its price is converted;
- the order in which cards are given;
- how cards that share an hour are counted or scored;
- the answer key, or how it is sealed;
- how the pool itself was found.

---

## 3 · The parts

Answer every part. In each part, choose one outcome.

Two outcomes are open in every part: **"The written rules already settle
this"** and **"This is outside what a juror may decide"**. If you choose
either one, cite the file and line it rests on. If you choose "outside", also say
which limit in RULES 33 it crosses. If you choose **"Other"**, state it in full,
so that it can be carried out with no further choice.

Within each part, the outcomes with a short name are listed in alphabetical
order of that name. The order means nothing.

### JQ-DRAW-a · the 200 large-movement cards

Which of the pool's large-movement moments become the 200 large-movement cards?

- **Random.** 200 moments drawn at random from all the pool's large-movement
  moments, each with the same chance, carried out as in section 4.
- **Size.** The 200 moments whose 24-hour movement is largest in absolute size,
  measured the way `TACTICS.md` §2 measured it when it found the moment. Ties go
  to the earlier start hour, then to the lower coin line number.
- **Settled.** The written rules already settle this. Say where, and what they
  require.
- **Outside.** This is outside what a juror may decide. Say which limit it
  crosses.
- **Other.** Stated in full.

### JQ-DRAW-b · the 200 calm cards

Which of the pool's calm moments become the 200 calm cards?

- **Coin-matched.** Each exam coin gets as many calm cards as part a gives it
  large-movement cards. They are drawn at random from that coin's calm moments
  in the pool, carried out as in section 4.
- **Pool-wide.** 200 moments drawn at random from all the pool's calm moments,
  each with the same chance and independently of part a, carried out as in
  section 4.
- **Settled.** The written rules already settle this. Say where, and what they
  require.
- **Outside.** This is outside what a juror may decide. Say which limit it
  crosses.
- **Other.** Stated in full.

### JQ-DRAW-c · the seed

If your answers to parts a and b draw anything at random, what number seeds the
draw?

- **Does not arise.** Your answers to parts a and b draw nothing at random.
- **Draw number.** The draw number written at `TACTICS.md` line 22.
- **Settled.** The written rules already settle this. Say where, and what they
  require.
- **Outside.** This is outside what a juror may decide. Say which limit it
  crosses.
- **Other.** A number, stated, and where it is written before the draw.

---

## 4 · How a random draw is carried out

Every outcome above that draws at random is carried out in the same way. This
way, no outcome needs a further choice:

1. The moments of one kind are listed by start hour, ascending, and then by coin
   line number, ascending. No two moments in the pool share both.
2. The whole draw uses one generator: Python 3 `random.Random(seed)`, with the
   seed from part c.
3. If part a draws at random, its draw comes first: `sample(list, 200)` on the
   large-movement list. Part b's draw comes next. Under **Pool-wide** it is
   `sample(list, 200)` on the calm list. Under **Coin-matched** it goes coin by
   coin in ascending line number, as `sample(that coin's calm list, k)`, where
   `k` is the number of large-movement cards part a gave that coin. A coin with
   `k = 0` is skipped.
4. These mechanics are not an outcome of this question. They are fixed here only
   so that every outcome can be carried out. A juror who thinks they change the
   answer can say so under "Other".

Any combination of outcomes across parts a, b and c can be carried out together.

## 5 · What a juror needs

`RULES.md`, `TACTICS.md`, `TEAM.md`, `README.md`, and the ratified verdicts:
each `verdict.md` under `decisions/` whose first line reads `RATIFIED`. Nothing
else. Section 1 states the two facts so that no other file is needed.

## 6 · Answer form

For each part, as `TEAM.md` sets out for jurors, give:

- the outcome you choose;
- the file and line it rests on, quoted (RULES 34);
- the strongest case against your answer;
- your confidence, from 1 to 5.

---

## 7 · For the reviewer: how each standard was checked

**Answerable from what it names.** The question names `TACTICS.md` §6 lines
99–100, §2 and line 22, and RULES 33. All of them are in files a juror may read.
The only facts outside those files are the two in section 1. They are stated
here, and the juror is not sent to look for them. The mechanics in section 4 are
spelled out in full.

**Every outcome can follow.**

- *Random* and *Pool-wide* each take 200 from a list that holds more than 200
  (fact 1).
- *Size* can be carried out with no further choice. Its measure is the one §2
  already uses. In the pool, no two large-movement moments have the same size,
  so its tie rule never acts, but it is stated anyway.
- *Coin-matched* is always possible. Part a never gives a coin more
  large-movement cards than the coin has in the pool, and by fact 2 the coin has
  at least that many calm moments. Under every part-a outcome the total comes to
  200.
- *Draw number* names a number that is already written down.
- *Does not arise* covers answers that draw nothing at random.
- *Settled* and *Outside* need a citation and nothing more.
- *Other* must be stated in full.
- Every random draw follows section 4, so no outcome leaves the generator, the
  list order or the order of the draws open.
- Every combination of a, b and c can be carried out together.

**Leans toward no answer.**

- *Figures:* the only figures are the two facts in section 1, and they are given
  only as far as the question needs them ("more than 200" and "exactly as many").
- *Passages:* no passage is quoted in favour of any outcome. Lines are cited
  only to say what the question is about and where a named number is written.
- *Precedent:* no verdict is cited.
- *Order and emphasis:* within each part, outcomes are listed alphabetically by
  short name, and the file says the order means nothing. The descriptions are
  of similar length, and no case is made for or against any outcome.
- *Single concrete seed:* part c offers one concrete seed because it is the only
  number the written rules name as a draw number. Offering any other number
  would mean the question-writer inventing one. "Other" is open to a juror who
  names a different number.
- *Procedures not listed:* procedures that would need an allocation rule or a
  number that neither the written rules nor this file supplies are not listed by
  name. They remain open under "Other".

**"Settled" and "outside" offered.** Both are outcomes in every part.

**Inside RULES 33.** Each part picks a procedure for choosing among moments
that already exist. No part sets a threshold, a score or a trading rule. The
counts 200 and 200 belong to `TACTICS.md` §6, and no part asks about them. No
part changes a rule in `RULES.md`. Part c asks which already-written number
seeds a draw, or lets the juror say that question is outside their remit.

**Points at no working file.** The only files named are the four root documents
and the ratified verdicts. No script, data file, run output, review or exam-prep
file is named. The source of the two facts in section 1 is given to the
coordinator, not in this file.

**No exam coin's name, date or price.** A script scanned this file for:

- every exam coin's symbol and base name;
- date and time patterns and month names;
- decimal figures.

It found none in the listed case. Matched in other case, it found only two
ordinary English words, the preposition "on" and the verb "may". Both were read
by hand and neither refers to a coin or a date. The file contains no date and no
price.

Every digit in the file belongs to one of these:

- a section number;
- a list-item or fact number (1–4);
- a rule number (33, 34);
- a `TACTICS.md` line number (22, 99, 100);
- the card counts 400 and 200;
- "24-hour";
- "Python 3";
- the ranges 1–20 and 1–5;
- `k = 0`.
