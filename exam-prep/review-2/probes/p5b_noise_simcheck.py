#!/usr/bin/env python3
"""
p5b_noise_simcheck.py -- sanity check of p5's exact formula, by simulation.
Draws the reported statistic (10th largest of 1,000 null draws) 4,000 times
from the exact hypergeometric null of the none/none/none synthetic-iid row
(n=306, A=148, L=153). Seed 20260913. 4,000 is a repetition count chosen for
this check only; nothing is reported from it except agreement with p5.
"""
import random, bisect, os, sys
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p5_noise_exact import null_pmf  # noqa  (runs p5's prints on import)
pmf = null_pmf(306, 148, 153)
vals = list(pmf); cum = []; s = 0.0
for v in vals:
    s += float(pmf[v]); cum.append(s)
rng = random.Random(20260913)
stat = Counter()
for _ in range(4000):
    d = sorted((vals[min(bisect.bisect_left(cum, rng.random()), len(vals) - 1)]
                for _ in range(1000)), reverse=True)
    stat[round(float(d[9]), 4)] += 1
print("\nSIMCHECK distribution of the reported line (value: share of 4000):")
for v in sorted(stat):
    print("  %.4f: %.4f" % (v, stat[v] / 4000))
