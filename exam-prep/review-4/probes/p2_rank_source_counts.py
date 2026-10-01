#!/usr/bin/env python3
"""p2 · review-4 · independent recount of JQ-R04-CONTENT part c's table
(fourth-fix H-4): per ranked column, hours whose printed token on the RAW
card's before table equals another hour's token in the same column, and of
those, hours given a different rank from at least one hour they tie with on
the unrounded-rank blinded card; and the cards with such an hour.
Parses the markdown itself (does not use lab_cards or script 30).
Reads: cards/C*.md (raw), exam-prep/third-fix/blind-proof/strict-flags-unrounded/
(cards and truth). Writes nothing (prints)."""
import csv, os, re
from collections import defaultdict
ROOT = "/home/user/balikcil"
U = os.path.join(ROOT, "exam-prep/third-fix/blind-proof/strict-flags-unrounded")
COLS = ["quote vol", "trades", "taker buy%", "open int", "L/S acct",
        "top L/S pos", "taker L/S", "depth -1%", "depth +1%"]
def first_table(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    for i, l in enumerate(lines):
        if l.startswith("| h |"):
            hdr = [x.strip() for x in l.strip().strip("|").split("|")]
            rows = []
            for l2 in lines[i + 2:]:
                if not l2.startswith("|"):
                    break
                rows.append([x.strip() for x in l2.strip().strip("|").split("|")])
            return hdr, rows
    raise SystemExit("no table in " + path)
truth = list(csv.DictReader(open(os.path.join(U, "truth-strict-flags-unrounded.csv"))))
tied = defaultdict(int); apart = defaultdict(int); cards_apart = defaultdict(set)
tied_nonnum = defaultdict(int)
any_card = set()
for t in truth:
    rh, rr = first_table(os.path.join(ROOT, "cards", t["source_card"] + ".md"))
    bh, br = first_table(os.path.join(U, "cards", t["id"] + ".md"))
    assert [r[0] for r in rr] == [r[0] for r in br], t["id"]
    for col in COLS:
        ri = rh.index(col); bi = bh.index(col + " r")
        tok = [r[ri] for r in rr]; rk = [r[bi] for r in br]
        n = len(tok)
        for i in range(n):
            mates = [j for j in range(n) if j != i and tok[j] == tok[i]]
            if not mates:
                continue
            tied[col] += 1
            if not re.match(r"^[+-]?[0-9.]+[kMB]?$", tok[i]):
                tied_nonnum[col] += 1
            if any(rk[j] != rk[i] for j in mates):
                apart[col] += 1; cards_apart[col].add(t["id"]); any_card.add(t["id"])
print("| column | hours tied on the raw card | of those, ranked apart | cards with such an hour | (tied hours whose token is not a number) |")
for col in COLS:
    print("| %s | %d | %d | %d | %d |" % (col, tied[col], apart[col], len(cards_apart[col]), tied_nonnum[col]))
print("cards with at least one hour ranked apart in any column:", len(any_card), "of", len(truth))
