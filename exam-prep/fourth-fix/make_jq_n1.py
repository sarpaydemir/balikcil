# fourth-fix run: builds exam-prep/fourth-fix/juror-questions/JQ-N1.md from
# the third-fix file by the exact replacements below (kept so the edit is
# reproducible and reviewable). Placeholders are filled by a second step.
import sys
src = "exam-prep/third-fix/juror-questions/JQ-N1.md"
dst = "exam-prep/fourth-fix/juror-questions/JQ-N1.md"
s = open(src, encoding="utf-8").read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:70], s.count(a))
    s = s.replace(a, b)
rep("""unchanged. JQ-CANTEEN-8 is answered by the same jurors (see part 3).
""", """unchanged. JQ-CANTEEN-8 is answered by the same jurors (see part 3).
Corrected by: Mateo · fourth-fix run · 2026-10-01 (system clock) — part 2:
the figures given for keeping the **latest** moment of a coin came from a
rule other than the one worded here, and are replaced by the figures of the
wording; both conventions are now offered by the engine. Part 3's pointer to
part 2 no longer names one convention. Part 4 names the engine version that
leaves the block shuffle unchanged. The questions of parts 1, 3 and 4 are
unchanged.
""")
rep("exam-prep/third-fix/juror-questions/JQ-CANTEEN-8.md",
    "exam-prep/fourth-fix/juror-questions/JQ-CANTEEN-8.md", 2)
rep("""  - **Under scope `cross-coin` (part 3) greedy-clique counts coins, not
    moments.** The chosen hour is the one covered by the most *coins*; when
    two or more moments of one coin cover it, only the **earliest** of them
    (by start hour, then card number) joins the event, and the others stay
    unassigned for a later round. Keeping the earliest is a second
    convention, written in the engine and not in any rule. The alternative —
    keeping the latest — gives different events on the observation cards:
    with the engine's own loop and only that choice reversed, 12 events
    under move-window and 30 under card-span (counted over both partitions)
    appear in one partition and not in the other (the number of events is
    unchanged: 168 and 125); an independent implementation by the reviewer,
    counted the same way, found 4 and 21 (card-span: 125 events against
    124). Source:
    `exam-prep/third-fix/checks/third-fix-checks-212dd7ecffc51263.md` G-5;
    `exam-prep/review-2/probes/p1b.out`.
  - If you choose greedy-clique with `cross-coin`, you may rule on this
    second convention too, or say "other". The engine the judge imports
    offers only "earliest" today. "Latest" can be carried out — it was run
    for this file with only that one choice reversed (G-5) — but the engine
    would have to be given that option, and checked, before the judge could
    use it.
""", """  - **Under scope `cross-coin` (part 3) greedy-clique counts coins, not
    moments.** The chosen hour is the one covered by the most *coins*; when
    two or more moments of one coin cover it, only **one** of them joins the
    event, and the others stay unassigned for a later round. Which one is a
    second convention, written in no rule:
    - **earliest** — the earliest of them by start hour (between two of one
      coin at the same start hour, the lower card number);
    - **latest** — the latest of them by start hour (between two of one coin
      at the same start hour, the higher card number).
    In the observation cards no coin has two moments at the same start hour,
    so the card-number part of either convention is never used there.
  - The two conventions give different events on the observation cards.
    Counted with the wording above applied as it stands — every clock hour a
    candidate in every round — and checked against two literal
    implementations written independently by reviewers: under move-window
    both give **168** events, and **4** events appear in one partition and
    not in the other; under card-span "earliest" gives **125** events and
    "latest" **124**, and **21** events appear in one partition only
    (counted over both partitions). Source: `__CHECKS__`, H-2.
  - Under either convention every event is a group of moments of different
    coins that all cover one clock hour. The other columns of the table
    above, for the "latest" convention (source as above):

__LATEST_TABLE__

  - If you choose greedy-clique with `cross-coin`, rule on this second
    convention too, or say "other". The engine the judge imports offers both
    (its fourth-fix version).
""")
rep("""    card-span). Which moment of a coin joins an event when two of them
    cover the chosen hour is the second convention described in part 2
    (the earliest); it changes which events form, not whether an event can
    hold two moments of one coin.""", """    card-span). Which moment of a coin joins an event when two of them
    cover the chosen hour is the second convention described in part 2; it
    changes which events form, not whether an event can hold two moments of
    one coin.""")
rep("""`756cf4ea156d92c3`; the third-fix version leaves it unchanged, and its run
  `bec532fa008e0e01` reproduces every output of that run byte for byte).""",
"""`756cf4ea156d92c3`; the third-fix and fourth-fix versions leave it
  unchanged, and their runs `bec532fa008e0e01` and `__COLLAPSE_RUN__`
  reproduce every output of that run byte for byte).""")
open(dst, "w", encoding="utf-8").write(s)
