# Juror 1 — the selection of large-movement moments (`TACTICS.md` §2)

Question answered: under §2, what procedure selects a coin's large-movement
moments, and in what order do the section's clauses operate?

Date: 2026-09-19 · role: juror (1 of 3) · read: `RULES.md`, `TACTICS.md`,
`README.md`, `TEAM.md` (whole of each). No data file, no card, no list opened.

---

## 1 · Answer

**The section prescribes one count and one separation constraint, and the
separation constraint operates *during* selection, not after it: moments are
taken largest-first, each new moment must be at least 48 hours from every
moment already taken, and the taking stops when the count is reached.** The
count is 20 for a coin that traded the whole year and, for a coin that did not,
one moment per 18 days of its lifetime. Stated as steps, implementable:

1. **Series.** Use the coin's hourly closing prices over the period
   (`TACTICS.md` §0: 2025-09-01 → 2026-08-31, and the repeat window).
2. **Candidates.** Every hour `t` in the period at which a full 24-hour
   movement can begin is one candidate moment. Its **start** is `t`; its
   movement is the change from the close at `t` to the close at `t+24h`. The
   candidate windows are rolling and overlap: `t`, `t+1h`, `t+2h` are three
   different candidates.
3. **Size.** Rank candidates by the **size of the movement regardless of sign** —
   a fall counts by the same yardstick as a rise, and both compete in one single
   ranking. There is no separate up-quota and down-quota.
4. **Quota.** `N = 20` for a coin that traded the whole year. For a coin that did
   not, `N` = its lifetime in days divided by 18.
5. **Selection (the ordering this answer turns on).** Take the largest remaining
   candidate. Add it to the list. Strike out every candidate whose start is less
   than 48 hours from that moment's start, in either direction. Repeat on what
   remains until the list holds `N` moments, or until no candidate survives.
6. **Result.** The list is the coin's large-movement moments; each is identified
   by its start hour. Calm moments are then drawn at random, as many as this list
   holds, each at least 72 hours from any large movement.

**Yield.** Under this reading a coin normally yields exactly `N` moments — the
quota is a yield, which is what lets `N` be stated as a rate ("one moment per
18 days") and lets the calm moments be "the same number". It can fall short only
if the coin's lifetime is too short to hold `N` moments 48 hours apart.

**The rejected reading, and how it differs.** The competing reading is: take the
20 largest candidates first as a fixed slice, *then* discard from within that
slice any moment that has a larger one within 48 hours, and do not refill.
Because the candidate windows are rolling and overlap hour by hour, neighbouring
candidates around one sharp episode are near-copies of each other, so the top of
the raw ranking tends to be several hours of the same few episodes. That reading
therefore yields **fewer than the quota, and can yield far fewer** — how many
fewer is a measured quantity and I have measured nothing; no data file was opened
for this question. The two readings are not a difference of detail: they differ in
how many moments exist, and so in how many cards, how many calm moments, and how
much of the year is looked at.

**What is *not* settled by §2** — named, so it is not silently assumed away.
These are gaps I had to fill to make the procedure implementable, and each fill
is my reading, not the section's words:

- (a) **Percent or absolute.** "rose or fell the most within 24 hours" does not
  say whether size is a proportional change or a change in price units. I read it
  as proportional; the section does not say so.
- (b) **Rolling or blocked windows.** §2's last line makes a moment's start an
  hour, which I read as every hour being a possible start. The section does not
  forbid reading it as fixed 24-hour blocks — under which reading the 48-hour
  clause would be doing much less work.
- (c) **Rounding of `N`** for a short-lived coin (floor, or nearest), and how
  "lifetime" is measured — first trade to last trade, or first trade to the end
  of the period.
- (d) **Full-year coins.** 20 per year and one per 18 days do not give the same
  number for a 365-day coin. The 18-day rate is written only for "a coin that did
  not trade all year", so 20 governs a full-year coin.
- (e) **48 hours between what.** I read it as between the two moments' starts,
  because §2 makes the start the moment's timestamp. Between window ends, or
  between window edges, would be a different rule.
- (f) **Ties** in movement size are not addressed. (§1 breaks ties elsewhere by
  symbol name ascending; that clause is about the draw, not about moments.)
- (g) **A literal pairwise elimination** — "strike every candidate that has a
  larger candidate within 48 hours" — is a third reading, and it is not the same
  as step 5. Where A > B > C, A within 48h of B, B within 48h of C, but A more
  than 48h from C, step 5 keeps {A, C} and the literal pairwise rule keeps {A}.
  I read step 5 as the coherent one, on the section's own words: the smaller of
  the pair "counts" no longer, and something that does not count cannot go on to
  strike out a third moment.

Within my remit: this answer sets no threshold, no score and no trading rule. The
numbers 20, 48, 18 and 72 are `TACTICS.md`'s, not mine; I have only said in what
order they operate. Nothing in `RULES.md` is changed (RULES 33). What should
happen to any list already built under either reading is not answered here.

---

## 2 · What it rests on

**`TACTICS.md` §2, lines 33–44, the whole section quoted:**

```
## 2 · Moments

- Hourly closing prices are used.
- **Large-movement moment:** the places where the coin rose or fell the most
  within 24 hours.
  - The largest 20 of the year are taken for each coin.
  - Of two moments closer than 48 hours to each other, only the larger counts.
  - For a coin that did not trade all year this count shrinks in proportion to
    its lifetime: one moment per 18 days.
- **Calm moment:** the same number as the large moments, chosen at random. At
  least 72 hours away from any large movement.
- A moment's start is the hour at which the 24-hour movement began.
```

The section states no order between its three sub-bullets. Three things inside it
decide the order for me:

1. **`TACTICS.md` line 40–41:** "For a coin that did not trade all year this
   count shrinks **in proportion to its lifetime: one moment per 18 days**."
   This states the count as a **rate of yield** — so many moments per so many
   days of life. 365 ÷ 18 is close to 20, so this clause is the 20 restated as a
   density. A rate of yield is a claim about how many moments a coin *ends up
   with*. That is true only if the separation constraint is satisfied while the
   count is being filled. If the 48-hour clause trimmed an already-taken slice of
   20, a full-year coin would end up with some unpredictable number below 20 and a
   half-year coin with some unpredictable number below 10, and the sentence "one
   moment per 18 days" would describe nothing that the procedure produces. This
   is the single strongest ground for my answer.

2. **`TACTICS.md` line 42–43:** "**Calm moment:** the same number as the large
   moments, chosen at random. At least 72 hours away from any large movement."
   Here the laboratory writes a selection with a separation constraint and a
   count in the *same breath*, and plainly means: draw until you have that many,
   each of them 72 hours clear. It is the same shape of instruction as the
   48-hour clause, and nobody would read "draw 20 at random, then throw away the
   ones too close, and keep what is left" — because then the calm list would not
   be "the same number as the large moments", which the line requires. Reading
   the 48-hour clause the same way as the 72-hour clause is the reading that
   makes the two halves of §2 agree.

3. **`TACTICS.md` line 39:** "Of two moments closer than 48 hours to each other,
   only the **larger counts**." The clause is written as a rule about what counts
   as a moment at all, not as an instruction to delete rows from a finished
   table. Its verb is definitional. And "only the larger counts" is what makes
   step 5 largest-first: the comparison that decides survival is size.

**`TACTICS.md` line 44:** "A moment's start is the hour at which the 24-hour
movement began." — grounds step 2 (a moment is identified by its start hour, and
an hour is a possible start) and step 5's measurement of the 48 hours between
starts.

**`TACTICS.md` line 35:** "Hourly closing prices are used." — grounds step 1 and
the close-to-close construction in step 2.

**`TACTICS.md` line 36–37:** "the places where the coin **rose or fell** the most
within 24 hours" — grounds step 3: both directions are large-movement moments,
and the section writes one count for both, not a count for each.

**Supporting, from elsewhere in the same file — `TACTICS.md` line 99–100:**
"Nadia has 400 cards prepared from the exam coins: 200 before a large movement,
200 calm moments." With §1 line 24's 20 exam coins, the laboratory's own plan
requires that the exam coins between them hold at least 200 large-movement
moments. A procedure whose quota is the yield meets that comfortably and leaves
Nadia sampling down; a procedure that trims a fixed slice of 20 down to an
unknown remainder might not reach 200 at all. I flag this as an argument from
internal coherence, not as a measurement: I have not counted anything.

**On my remit — `RULES.md` line 119–121 (RULES 33):** "A juror decides procedure
and definition only: never a trading rule, never a threshold or score, and never
a change to a rule in this file." — which is why the gaps (a)–(g) above are
listed as unsettled rather than filled by decree, and why I do not touch 20, 48,
18 or 72.

**On honesty about counts — `RULES.md` line 71 (RULES 19):** "An unmeasured
number is not written down." — which is why the difference in yield between the
two readings is stated in words above and not in a number.

---

## 3 · The strongest case against my answer

Put at its strongest, against me:

**The section is a list read top to bottom, and the order of the bullets *is* the
order of operations.** "The largest 20 of the year are **taken** for each coin"
comes first and uses the verb of the act itself: the taking happens there, on the
raw ranking, and it takes twenty. The next bullet then says what happens to what
was taken: of two of *them* closer than 48 hours, only the larger counts. On this
reading the third bullet is the most natural of all: "**this count** shrinks" —
*this* count, the 20 just named, the number you take off the ranking, not the
number you end up with. My reading has to make "this count" mean a target that
the selection fills, which is a heavier load for two words to carry. An engineer
handed §2 with no further argument would very likely implement the bullets in the
order written, and it is not obvious that they would be wrong to. My reading
requires the reader to go to the third bullet, notice that "one moment per 18
days" only makes sense as a yield, and back-propagate that into the first two
bullets. That is an inference, not an instruction, and §2 nowhere writes the word
"until" or "remaining" or "each next" — the words a procedure that meant step 5
would ordinarily contain.

Two further points against me. First, **my coherence argument from the calm
moments cuts both ways**: the calm clause says "the same number as the large
moments", which is well defined whatever the large list turns out to hold — under
the bullet-order reading it simply means "as many calm moments as large moments
survived", and the section stays consistent. Second, **the exam arithmetic can be
read against me too**: 200 large-movement cards spread over 20 exam coins is ten
per coin on average, which sits *below* a quota of 20 and would fit a procedure
that yields fewer than its nominal count rather more neatly than one that yields
20 apiece and needs Nadia to discard the surplus. I do not think this is decisive
— §2's count shrinks for short-lived coins, §1 line 24 puts four new coins in the
exam, and nothing says every moment becomes a card — but it is real evidence
pointing the other way and I will not dress it down.

**Where that leaves the honest position.** §2 does not state the order in so many
words, and both readings can be built out of its sentences. I do not think that
makes the section a tie: only one of the two readings lets line 40–41 describe
anything real, and that clause is in the section, on the page, as binding as the
bullets above it. But a juror reading only lines 38–39 would land on the other
reading without doing anything wrong, and the referee should know that my answer
is a reading of the section as a whole rather than a quotation of a sentence that
settles it. If the referee's standard is "settled by the words themselves,
sentence by sentence", then the correct answer is **the text does not settle the
order**, and the fix is for the user to be asked to write one sentence into
`TACTICS.md` — not for me to legislate it.

**Reversibility.** Both readings are reversible in principle but not at equal
cost. If the laboratory implements the quota-is-yield reading and later reverses
it, the surplus moments are simply dropped — cheap, and the smaller list is a
subset of the larger one. If it implements the trim-a-slice reading and later
reverses it, every additional moment has to be found and every card for it
written and, if watchers have already read the short list, the reading of the
short list is not evidence about the moments that were missing. The asymmetry is
that the yield reading's list **contains** the other list's list; the reverse is
not true. Anything already read by a watcher is the part that does not come back:
a watcher's eyes cannot be un-run (`TACTICS.md` §4, `RULES.md` 7).

---

## 4 · Confidence, and what would change my mind

**Confidence: 3 of 5.**

3 and not higher because the order of operations is genuinely not written in §2,
and the plain bullet order reads against me; my answer rests on an inference from
line 40–41 rather than on a sentence that states the order. 3 and not lower
because that inference is not a delicate one — a count written as a rate per 18
days is a statement about how many moments a coin has, and only one of the two
procedures makes it true.

I am **confident to 4–5** about the parts of the procedure that are not about
clause order: hourly closes, rolling 24-hour windows started at any hour, one
ranking for rises and falls together, moments timestamped by their start, the
quota of 20 pro-rated at one per 18 days, and the calm rule.

**What would change my mind:**

- A sentence in `TACTICS.md` or `RULES.md` I did not read that states the order,
  or that describes the large-moment list as "up to 20" / "at most 20". I read
  both files whole and found none; the closest is `TACTICS.md` line 99–100,
  discussed above.
- A showing that the 18-day rate is arithmetic coincidence rather than a
  restatement of 20 per year — e.g. if 18 days had been chosen for some separate
  reason written down elsewhere in the laboratory's documents. I would want to
  see that in writing.
- A showing that the 24-hour windows are meant to be non-overlapping blocks
  (gap (b)). If windows do not overlap, the 48-hour clause removes far less, the
  two readings converge, and the order of the clauses stops mattering much.
- A measurement — which I am not the person to make and did not make — showing
  that the trim-a-slice reading in fact yields something close to 20 on real
  coins. That would remove my "line 40–41 would describe nothing" argument, and
  with it most of my confidence.

Nothing about *which list has already been built*, or what it cost, would change
my mind, and I was careful not to look for one.

---

## Note on the instruction (RULES 3)

The instruction was scrupulous about not characterising §2 and explicitly
permitted "the text does not settle this". Three sentences in it nevertheless
carry information I did not have from the files:

1. "If the procedures it admits differ **in how many moments they yield**, say
   that too" — this names the axis on which the readings differ before the juror
   has opened the file. It told me to look at counts. I would like to think I
   would have got there anyway, since the yield difference is the whole of the
   matter, but I cannot prove that and I report it.
2. "What should happen to **any list already produced** is a separate question" —
   this discloses that a list exists and that its validity is in doubt. It does
   not say under which reading it was built, so it does not point at an answer,
   but it does tell the juror that one answer will be the expensive one.
3. "this laboratory has learned that handing a juror an artefact built under one
   reading pulls toward that reading" — the same disclosure, restated.

None of these tells me which reading is correct, so I do not think the jury was
steered to an answer; but (1) is a steer toward a feature of the answer, and the
referee should weigh it.

## Wall

I read only `RULES.md`, `TACTICS.md`, `README.md` and `TEAM.md`, each by its
full absolute path, each read whole. I opened no folder listing, ran no glob, no
search and no command line. I did not open `exam/`, `decisions/` (including the
other files in the folder this file is written to), `LEDGER.md`,
`instructions/`, `notes/`, `canteen/`, `cards/`, `reports/`, `scripts/` or
`data/`, and nothing outside `/home/user/balikcil`. I saw no other juror's
answer. This file is the only thing I wrote.
