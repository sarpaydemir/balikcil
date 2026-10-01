#!/usr/bin/env python3
"""q3 - review-3 probe (JQ-CANTEEN-8 table). Recount, from data/overlap/pairs.csv
and independently from the card start hours, every overlapping pair by kinds and
same/different coin, for card spans (start gap <= 47 h) and before windows
(start gap <= 23 h; before = t0-24h..t0-1h per data/overlap/overlap-manifest.md).
Also C010/C011's gap. Input: data/overlap/pairs.csv, cards/. Output: stdout."""
import csv, os, sys, itertools, datetime as dt
from collections import Counter
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts")); import lab_cards
rows = list(csv.DictReader(open(os.path.join(ROOT, "data/overlap/pairs.csv"))))
def key(r):
    k = "+".join(sorted([r["kind_a"], r["kind_b"]]))
    return (k, "same" if r["same_coin"] == "yes" else "diff")
span = Counter(key(r) for r in rows)
before = Counter(key(r) for r in rows if int(r["start_gap_hours"]) <= 23)
print("pairs.csv rows", len(rows))
for k in sorted(set(span) | set(before)):
    print(k, "card spans", span[k], "before windows", before[k])
cards = lab_cards.load_all(os.path.join(ROOT, "cards"))
def ph(s):
    s = s.replace("Z", "");  s = s + ":00" if len(s) == 16 else s
    return dt.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S")
ms = [(c["card"], c["coin"], c["kind"], ph(c["start_hour_utc"])) for c in cards]
sp = Counter(); bf = Counter()
for a, b in itertools.combinations(ms, 2):
    g = abs((a[3] - b[3]).total_seconds()) / 3600
    k = ("+".join(sorted([a[2], b[2]])), "same" if a[1] == b[1] else "diff")
    if g <= 47: sp[k] += 1
    if g <= 23: bf[k] += 1
print("from card start hours:")
for k in sorted(set(sp) | set(bf)):
    print(k, "card spans", sp[k], "before windows", bf[k])
by = {m[0]: m for m in ms}
print("C010-C011 start gap h", abs((by["C010"][3] - by["C011"][3]).total_seconds()) / 3600, by["C010"][1:3], by["C011"][1:3])
