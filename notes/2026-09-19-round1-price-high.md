# Round 1 notes · watcher-high · field of view: price itself
# (price, volume, trade count, order book depth, volatility)
# Cards read: C001–C010. Written 2026-09-19.
#
# Numbers marked **[computed]** are arithmetic I did on figures printed on the
# card (e.g. the mean of the 24 `quote vol` cells). Numbers with no mark are
# read straight off the card. No number here is an estimate unless it says so.
#
# Format: card no · what I saw · why I think so · how sure I am (1–5)

## A · Facts about the card set itself

C001–C010 · All ten cards carry the same coin, `AVGOUSDT`. · Read from the `coin` row of each card header; ten out of ten. · 5
C001–C010 · The ten start hours run 2026-05-07 20:00 to 2026-07-16 00:00 — about ten weeks, not a year. · Read from the `start hour (UTC)` row of each header. · 5
C001–C010 · Five moments are labelled `large` (C003, C004, C005, C007, C009) and five `calm` (C001, C002, C006, C008, C010). · Read from the `Moment kind` line in each After section. · 5
C003, C004, C005 · These three are one continuous, back-to-back stretch of price, not three independent samples: C003 After ends at 492.83 and C004 Before opens at 487.39 (2 h gap); C004 After ends at 408.26 and C005 Before opens at 408.24 (adjacent). Start hours are 50 h and 48 h apart. · Read the +23 close of one card against the -24 close of the next; start hours differenced from the headers. My opinion: three of my five large moments are therefore roughly one episode, so any "4 of 5 large cards did X" count in these notes is worth far less than it looks. · 5
C004, C005 · The two start hours are exactly 48 h apart (2026-06-03 12:00 and 2026-06-05 12:00). · Differenced from the headers. My opinion, flagged as procedure not finding: TACTICS §2 drops a moment only if it is *closer than* 48 h to a larger one, so this sits exactly on the boundary — I am not calling it a fault, only recording that it is on the line. · 4
C006 · Its `Previous 7 days` line (price -16.71%, range 38.27%) is a summary of the very hours C004 and C005 cover. · C006 starts 2026-06-10, and 168 h back reaches into the 2026-06-03/06-05 crashes on C004/C005. My opinion: C006's "before" context is not independent of two other cards in the set. · 4
C001–C010 · The coin's activity regime changed by roughly 40x inside these ten weeks. `Previous 7 days · avg hourly volume` runs 47.72k (C001) → 85.83k → 153.81k → 313.19k → 960.13k → 1.95M (C006) → 415.87k → 393.34k → 390.92k → 482.53k (C010). · Read off the Previous-7-days line of each card. My opinion: any rule using an absolute volume or depth threshold will mean different things in May than in June on this one coin alone, so thresholds in my field should be ratios, never levels. · 5
C001–C010 · "Calm" does not mean "flat". The calm cards' own `Measured 24-hour move` lines are +4.19%, -0.05%, -2.51%, +0.56%, -4.87%; the large cards' are +7.72%, -17.27%, -9.70%, -8.36%, +8.82%. The largest calm (4.87%) and the smallest large (7.72%) are only about 2.9 points apart. · Read from the `Measured 24-hour move` line of all ten After sections. · 5
C001–C010 · Not a single card is missing, truncated or unreadable in my field: every card printed 24 Before rows and 24 After rows, with `close`, `chg%`, `quote vol`, `trades`, `depth -1%`, `depth +1%` filled in every row. · I checked each of the 480 rows for a `.` or `MISSING` in those six columns and found none. Before saying "none": the empty/MISSING fields on these cards (Wikipedia, prediction market, announcements) are all outside my field of view. · 5
C002, C008 · Two hours print `open int` = 0 (C002 h-14 and h-13; C008 h+10), which looks like a data gap rather than zero open interest. · Read off the table. Recording it only because I saw it while scanning; open interest is not my field and I make no claim about it. · 3

## B · Volume against the coin's own recent baseline — the one thing that came close to separating

C001 · Mean hourly quote volume over the Before window 109.2k **[computed]** against the card's 7-day baseline 47.72k = 2.29x **[computed]**. Card is calm. · Summed the 24 `quote vol` cells and divided by 24, then by the Previous-7-days average. This is the one calm card with a big volume expansion. · 4
C002 · Before-window mean volume 50.6k **[computed]** vs baseline 85.83k = 0.59x **[computed]**. Card is calm. · Same method. · 4
C003 · Before-window mean volume 341.2k **[computed]** vs baseline 153.81k = 2.22x **[computed]**. Card is large. · Same method. · 4
C004 · Before-window mean volume 1.032M **[computed]** vs baseline 313.19k = 3.30x **[computed]**. Card is large. · Same method. · 4
C005 · Before-window mean volume 4.055M **[computed]** vs baseline 960.13k = 4.22x **[computed]** — the largest expansion of the ten. Card is large. · Same method. · 4
C006 · Before-window mean volume 1.710M **[computed]** vs baseline 1.95M = 0.88x **[computed]**. Card is calm. · Same method. · 4
C007 · Before-window mean volume 299.6k **[computed]** vs baseline 415.87k = 0.72x **[computed]**. Card is LARGE — the one large moment that arrived on contracting volume. · Same method. This is the clean counterexample to the volume-expansion idea. · 4
C008 · Before-window mean volume 530.3k **[computed]** vs baseline 393.34k = 1.35x **[computed]**. Card is calm. · Same method. · 4
C009 · Before-window mean volume 838.4k **[computed]** vs baseline 390.92k = 2.14x **[computed]**. Card is large. · Same method. · 4
C010 · Before-window mean volume 284.8k **[computed]** vs baseline 482.53k = 0.59x **[computed]**. Card is calm. · Same method. · 4
C001–C010 · Taking the ten ratios together: at or above 2.0x there are 4 large (C003, C004, C005, C009) and 1 calm (C001); below 2.0x there are 1 large (C007) and 4 calm (C002, C006, C008, C010). · Counted from the ten lines above. My opinion: this is the only thing in my whole field of view that looks like it separates, and it is 8 of 10 cards on ONE coin with three of the four "hits" belonging to one continuous episode (C003/C004/C005) — so it is an observation, not a rule, and I would expect most of it to evaporate on other coins. · 3
C001–C010 · Volume expansion says nothing about direction. The four expanded large cards split 2 up (C003 +7.72%, C009 +8.82%) and 2 down (C004 -17.27%, C005 -9.70%). · Counted from the `Measured 24-hour move` lines. My opinion: this is why the volume ratio cannot become an idea on its own — RULES 8 needs a direction and I do not have one. · 4

## C · Net price drift in the before window

C001 · Before-window net move (close h-24 425.43 to close h-1 412.92) = -2.94% **[computed]**. After = +4.19%, i.e. the opposite sign. Calm. · Two closes off the table. · 4
C002 · Before net +2.14% **[computed]** (413.49 → 422.32). After = -0.05%. Calm. · Same. · 4
C003 · Before net -0.72% **[computed]** (460.87 → 457.53). After = +7.72%, opposite sign. Large. · Same. · 4
C004 · Before net +1.25% **[computed]** (487.39 → 493.47). After = -17.27%, opposite sign. Large. · Same. · 4
C005 · Before net +0.81% **[computed]** (408.24 → 411.56). After = -9.70%, opposite sign. Large. · Same. · 4
C006 · Before net -3.31% **[computed]** (399.87 → 386.62). After = -2.51%, same sign. Calm. · Same. · 4
C007 · Before net -0.16% **[computed]** (410.77 → 410.11). After = -8.36%, same sign but the before-drift is essentially nil. Large. · Same. · 4
C008 · Before net -1.13% **[computed]** (369.94 → 365.75). After = +0.56%. Calm. · Same. · 4
C009 · Before net +1.36% **[computed]** (364.58 → 369.53). After = +8.82%, same sign. Large. · Same. · 4
C010 · Before net +0.43% **[computed]** (392.03 → 393.73). After = -4.87%, opposite sign. Calm. · Same. · 4
C001–C010 · The simple rival rule of RULES 11 ("whichever direction the last 24 hours went, continue that way") gets about 3 of these 10 right (C006, C007, C009) and is wrong or flat on the other seven. · Compared the sign of each before-net above with the sign of the `Measured 24-hour move`. My opinion: on these ten cards momentum-continuation is worse than a coin flip, and since every before-net here is small (|net| ≤ 3.31%) its sign is close to noise anyway. If this holds on the exam set, the simple rule is a soft rival, which makes it easier to beat and therefore weaker evidence when we do beat it. · 3
C001–C010 · All five large moments had a quiet net drift beforehand — |before net| is 0.72, 1.25, 0.81, 0.16, 1.36 percent, all under 1.5% — while three of the five calm cards drifted more than 2% (C001 2.94, C002 2.14, C006 3.31). · Counted from the ten lines above. My opinion, and I want this read as a warning not a finding: TACTICS §2 defines a moment's start as "the hour at which the 24-hour movement began", so a quiet before-window may be built into how the moments were selected rather than being something the market does. It would be easy to mistake the selection procedure for a signal here. · 3

## D · Volatility in the before window — did not separate

C001 · Largest single-hour |chg%| in the Before window = 1.48% (h-7). Calm. · Scanned the 24 `chg%` cells. · 4
C002 · Largest single-hour |chg%| = 1.05% (h-4). Calm. · Same. · 4
C003 · Largest single-hour |chg%| = 1.22% (h-10). Large. · Same. · 4
C004 · Largest single-hour |chg%| = 2.00% (h-14). Large. · Same. · 4
C005 · Largest single-hour |chg%| = 2.20% (h-19). Large. · Same. · 4
C006 · Largest single-hour |chg%| = 2.88% (h-16), the highest of all ten Before windows, with -2.46%, -2.88%, +2.51%, +2.04% in four consecutive hours. The card is CALM (after -2.51%). · Same. My opinion: this is the single cleanest kill in my field — the most violent before-window in the set was followed by the quietest kind of outcome. · 4
C007 · Largest single-hour |chg%| = 1.16% (h-15), and the first nine hours of the window never exceed 0.21%. The card is LARGE (after -8.36%). · Same. My opinion: the second kill — the calmest-looking before-window of the five large cards produced an 8% fall. · 4
C008 · Largest single-hour |chg%| = 1.50% (h-13). Calm. · Same. · 4
C009 · Largest single-hour |chg%| = 1.89% (h-4). Large. · Same. · 4
C010 · Largest single-hour |chg%| = 1.72% (h-10). Calm. · Same. · 4
C001–C010 · Ranked, the ten peak-hour volatilities interleave completely: calm values 1.05, 1.48, 1.50, 1.72, 2.88 against large values 1.16, 1.22, 1.89, 2.00, 2.20. The highest belongs to a calm card and the lowest-but-one to a large card. · Sorted the ten lines above. My opinion: realised volatility in the 24 h before a moment does not separate large from calm on these cards, and I would not carry it into the canteen as a raising signal. · 4
C001–C010 · The card's `Previous 7 days · high-low range` does not separate either: calm 7.15, 4.16, 38.27, 7.28, 11.92 against large 11.38, 18.37, 23.12, 9.51, 6.10. The widest range in the set (38.27%, C006) is calm and the narrowest (6.10%, C009) is large. · Read off the Previous-7-days line of all ten cards. · 4

## E · Order book depth

C002 · The `depth -1%` column collapses in the last hours before the start: 136.02k at h-7 → 33.06k at h-3, and it stays between 33k and 39k for the final three hours — about 27% of its h-7 level **[computed]**. The card is CALM (after -0.05%). · Read the depth column down the Before table. · 4
C008 · The same pattern, larger: `depth -1%` 755.16k at h-7 → 172.97k at h-1, about 23% of its h-7 level **[computed]**, falling for six straight hours. The card is CALM (after +0.56%). · Same method. · 4
C002, C008 · These are the only two clear pre-start depth collapses in the ten cards, and both precede calm moments. · I scanned the last six Before rows of all ten depth columns; no other card falls by more than about a third. My opinion: if a depth collapse means anything here, it points away from a large move, not towards one. Two cards is two cards — this is an observation resting on two events. · 3
C003, C004, C005, C007, C009 · None of the five large moments shows a depth collapse into the start hour. At h-1 the `depth -1%` values are 169.92k, 327.63k, 837.59k, 695.62k and 356.85k, each within about a third of that card's own preceding hours. · Read the final Before rows. · 3
C007 · `depth -1%` roughly 2.6x higher in the back half of the window than the front: mean 249.3k over h-24..h-16 against 656.8k over h-12..h-1 **[computed]**. Large, down -8.36%. · Means computed from the column. · 4
C003 · `depth -1%` roughly 1.95x higher in the back half: 83.1k over h-24..h-16 against 161.8k over h-11..h-1 **[computed]**. Large, up +7.72%. · Same method. · 4
C009 · `depth -1%` roughly 0.61x, i.e. it FELL by about 39% across the window: 516.9k over h-24..h-16 against 314.8k over h-11..h-1 **[computed]**. Large, up +8.82%. · Same method. · 4
C010 · `depth -1%` roughly 1.53x, a clear rise across the window: 530.3k over h-24..h-16 against 813.0k over h-11..h-1 **[computed]**. CALM. · Same method. · 4
C003, C004, C005, C007, C009, C010 · The direction of depth change across the before window is inconsistent: the five large cards give 1.95x, 1.10x, 1.17x, 2.64x and 0.61x, and a calm card (C010) gives 1.53x, sitting in the middle of them. · Computed the same front-half/back-half means for every card. My opinion: rising or falling depth over the before window carries no separation I can see, and I would rather report that plainly than keep hunting for a cut point that fits ten cards. · 3

## F · Trade count and terminal-hour volume — restatements and non-signals

C001–C010 · Trade count moves with quote volume almost everywhere on these cards, so the `trades` column is largely a restatement of the `quote vol` column. Peak before-window trade counts are C001 5k, C002 3k, C003 13k, C004 22k, C005 96k, C006 35k, C007 8k, C008 15k, C009 21k, C010 12k — large 13/22/96/8/21 against calm 5/3/35/15/12, heavily overlapping. · Read the `trades` column; the hour with the highest trades is the hour with the highest volume on every card I checked. My opinion: this is point 3 of my brief — a signal that only restates something already in the volume column should not be scored twice. · 3
C001–C010 · Volume in the final hour before the start, as a ratio to that card's own before-window mean, does not separate: C001 1.40 calm, C002 0.66 calm, C003 0.90 large, C004 0.95 large, C005 0.22 large, C006 0.18 calm, C007 1.44 large, C008 0.19 calm, C009 0.80 large, C010 0.16 calm **[all computed]**. · Divided the h-1 `quote vol` by my computed window mean. My opinion: the three lowest values are calm (C010, C006, C008) but a large card (C005, 0.22) sits right beside them, so there is no usable cut. · 2
C001, C009 · These are the only two cards where an hour inside the last three before the start prints at least 3x the window's mean volume: C001 h-2 = 925.37k against a 109.2k mean (8.5x **[computed]**, that hour closed -0.55%) and C009 h-2 = 4.66M against an 838.4k mean (5.6x **[computed]**, that hour closed +1.50% on 21k trades). Both cards then went up over the following 24 h (+4.19% and +8.82%). · Scanned the last three Before rows of every card against my computed means. · 3

## G · Did the whole market move at the same time? (point 2 of my brief)

C003 · Coin +7.72% over the After window while the `BTC` column sums to about -4.86% and `ETH` to a similar negative **[computed]**. The coin rose hard while bitcoin fell. · Added the 24 `BTC` cells of the After table. My opinion: this move is the coin's own, not a market event. · 4
C009 · Coin +8.82% while the `BTC` column sums to about +0.79% **[computed]**. The single biggest hour, +1 at +3.38%, printed with BTC at -0.02%. · Same method. My opinion: coin's own move. · 4
C005 · Coin -9.70% while `BTC` sums to about -1.75% **[computed]**. The biggest hour, +14 at -4.34%, printed with BTC at -0.18%. · Same method. My opinion: mostly the coin's own, with a mild market tailwind. · 4
C007 · Coin -8.36% while `BTC` sums to about -4.52% **[computed]** — same direction, coin roughly 1.8x the size. · Same method. My opinion: a meaningful share of this one is market-wide, so under RULES 13 thinking it is partly one event with whatever bitcoin was doing. Flagging it explicitly so nobody credits the whole 8.36% to a coin-level signal. · 4
C004 · Coin -17.27% while `BTC` sums to about -6.89% **[computed]** — same direction, coin roughly 2.5x. But the two hours that did most of the damage, +8 (-5.09%) and +9 (-7.74%), printed with BTC at -0.70% and +1.18%: bitcoin was flat-to-up during the coin's worst hour. · Same method, then read the two rows individually. My opinion: the backdrop was a down market, the crash itself was not. · 4
C003, C004, C005, C007, C009 · Summing up the five large moments: two ran against or independent of bitcoin (C003, C009), one was mostly its own with a mild market drift (C005), and two ran with a falling market at roughly 1.8–2.5x its size (C004, C007). · From the five lines above. My opinion: the large moments on this coin are mostly coin-level, but C004 and C007 should not be counted as fully independent evidence. · 3

## H · Ideas and blocker candidates

C001, C009 · **IDEA (complete, but thin).** Trigger: in the last 3 hours of the before window, one hour prints quote volume of at least 3x the mean hourly quote volume of that same 24-hour window. Direction: buy. Exit: close the position 24 hours after entry, or immediately on a 4% adverse move from entry, whichever comes first. · Fires on exactly 2 of my 10 cards (C001 8.5x, C009 5.6x **[computed]**) and both rose over the next 24 h (+4.19%, +8.82%). I am writing all three parts so it can be tested, but two cards on one coin is not evidence, I have no mechanism to offer, and one of the two (C001) is a calm-labelled card — so a fair test must ask whether this only ever catches mild drift. · 2
C002, C008 · **BLOCKER CANDIDATE — direction deliberately absent.** Trigger: `depth -1%` in the final before-window hour is 40% or less of its value 6 hours earlier. Proposed effect: suppress any "large move expected" score; do not trade. Exit: not applicable, it opens nothing. · Fires on 2 of 10 cards and both are calm. I am NOT calling this an idea: it has no buy/sell direction, so under RULES 8 it does not qualify, and I say so rather than inventing a direction to fill the slot. · 3
C002, C006, C007, C010 · **BLOCKER CANDIDATE — direction deliberately absent.** Trigger: before-window mean hourly quote volume is 0.9x or less of the card's printed 7-day average hourly volume. Proposed effect: suppress any "large move expected" score. · Fires on 4 of 10 cards, 3 calm and 1 large (C007, which fell 8.36% on 0.72x volume). One in four is a miss, and the miss is an 8% move — expensive. Recorded so Viktor has something concrete to attack. · 2
C001–C010 · **OBSERVATION, NOT AN IDEA — the missing part is direction.** Before-window volume at or above 2.0x the 7-day baseline, combined with a before-window net drift of under 1.5%, picks out C003, C004, C005 and C009 — four of the five large moments and none of the five calm ones (the filter's second clause is what drops the calm false positive C001, whose drift was -2.94%). · Combined sections B and C above. I have a trigger and I could write an exit, but the four hits split 2 up and 2 down, so I have no direction and this is therefore not an idea. Three of the four hits are the single continuous C003/C004/C005 episode, which makes "four of five" nearer to "two episodes of two". · 3
