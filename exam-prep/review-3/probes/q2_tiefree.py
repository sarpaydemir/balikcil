#!/usr/bin/env python3
"""q2 - review-3 probe (R-04; THIRD-FIX dispute D-1; K-6).
For one blinded card set, recompute for every family and the gate row:
  - the tie sets of the nearest-neighbour attack with EXACT arithmetic
    (squared distances as Fractions of the float features over the exact
    sample variance), against the audit's float equality;
  - the tie-free score and its chance line, with the audit's own shuffle
    sequence (seed 20260913, 1,000 shuffles, 10th largest = best 1%);
  - as a diagnostic only, the share of 2,000 further shuffles (seed 1) at or above the
    observed tie-free score, to show how close a verdict sits to its line.
    2,000 and seed 1 are my own diagnostic choices; nothing is graded on them.
Input: --cards, --truth (a blinded set). Output: stdout (saved beside as .out).
Imports scripts/16_identity_audit.py for card parsing and features only.
"""
import os, sys, csv, random, importlib.util, argparse
from fractions import Fraction
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
spec = importlib.util.spec_from_file_location("ia", os.path.join(ROOT, "scripts", "16_identity_audit.py"))
ia = importlib.util.module_from_spec(spec); spec.loader.exec_module(ia)
import lab_cards
ap = argparse.ArgumentParser(); ap.add_argument("--cards"); ap.add_argument("--truth")
ap.add_argument("--families", default="")
a = ap.parse_args()
names = sorted(f for f in os.listdir(a.cards) if f.endswith(".md") and f != "INDEX.md")
cards = [lab_cards.parse_any_card(os.path.join(a.cards, n)) for n in names]
truth = {r["id"]: r for r in csv.DictReader(open(a.truth))}
for c in cards:
    c["coin"] = truth[c["card"]]["coin"]; c["start_hour_utc"] = truth[c["card"]]["start_hour_utc"]
coins = [c["coin"] for c in cards]
feats = [ia.card_features(c) for c in cards]
allkeys = sorted({k for f in feats for k in f})
specs = list(ia.FAMILIES.items())
specs.append(("ALL-removable", sorted({p for k, v in ia.FAMILIES.items() if k not in ia.FORCED_FAMILIES for p in v})))
want = set(a.families.split(",")) if a.families else None
n = len(cards)
def tf(tsets, lab):
    return sum(sum(1 for j in t if lab[j] == lab[i]) / len(t) for i, t in enumerate(tsets)) / n
def tf_fast(pairs, lab):
    return sum(w for i, j, w in pairs if lab[i] == lab[j])
print("family | features | tied cards float | tied cards exact | tie sets equal | tie-free | line (audit shuffles) | beats | share of 2,000 further shuffles >= observed")
for fam, prefixes in specs:
    if want and fam not in want: continue
    keys = ia.select({k: 1 for k in allkeys}, prefixes)
    vecs, used = ia.standardise(feats, keys)
    if not used:
        print(fam, "| 0 | no features"); continue
    # float tie sets, exactly as the audit
    d = ia.pair_distances(vecs)
    ts_float = ia.nearest_tie_sets(d)
    # exact: squared distance = sum (dx)^2 / var_k, Fractions
    raw = [[Fraction(f[k]) for k in used] for f in feats]
    var = []
    for kk in range(len(used)):
        col = [r[kk] for r in raw]; m = sum(col) / n
        var.append(sum((x - m) ** 2 for x in col) / (n - 1))
    inv = [1 / v for v in var]
    ts_exact = []
    D = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            s = Fraction(0)
            ri, rj = raw[i], raw[j]
            for kk in range(len(used)):
                dx = ri[kk] - rj[kk]
                if dx: s += dx * dx * inv[kk]
            D[i][j] = D[j][i] = s
    for i in range(n):
        best = min(D[i][j] for j in range(n) if j != i)
        ts_exact.append([j for j in range(n) if j != i and D[i][j] == best])
    same = ts_float == ts_exact
    obs = tf(ts_exact, coins)
    rng = random.Random(ia.SEED); perm = list(coins); null = []
    for _ in range(ia.SHUFFLES):
        rng.shuffle(perm); null.append(tf(ts_exact, perm))
    line = ia.quantile_top(null, ia.TOP_FRACTION)
    pairs = [(i, j, 1.0 / (n * len(t))) for i, t in enumerate(ts_exact) for j in t]
    rng2 = random.Random(1); perm = list(coins); ge = 0
    for _ in range(2000):
        rng2.shuffle(perm)
        if tf_fast(pairs, perm) >= obs - 1e-12: ge += 1
    print("%s | %d | %d | %d | %s | %.4f | %.4f | %s | %.4f" % (
        fam, len(used), sum(1 for t in ts_float if len(t) > 1), sum(1 for t in ts_exact if len(t) > 1),
        same, obs, line, "YES" if obs > line else "no", ge / 2000))
    sys.stdout.flush()
