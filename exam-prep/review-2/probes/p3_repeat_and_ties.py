#!/usr/bin/env python3
"""
p3_repeat_and_ties.py -- review-2 probe (R-04).

What it does
  A. Feature check: recomputes every `repeat-*` feature (distinct printed values,
     largest number of rows sharing one printed value) from the card TEXT with
     its own parser, and compares it with 16_identity_audit.card_features() on
     every card of `strict-flags`, `strict-flags-k1` and the raw cards.
  B. Own pair AUC: a deterministic Mann-Whitney AUC written here (no shared
     code with the audit beyond the standardised vectors) for the `repeat-*`
     families and the `ALL-removable` gate row on `strict-flags`, compared with
     the second-fix CSV (run d70dd7b545bfce8a).
  C. Nearest-neighbour tie range: for each card, the set of other cards at
     exactly the minimum distance. The NN score's lowest and highest possible
     values over every tie-break, and its mean under uniformly random
     tie-breaks -- exact, no randomness. For the gate row and every repeat
     family on `strict-flags`, and for `repeat-close` on the raw cards.
  D. K-4 granularity feature computed two ways -- float subtraction of parsed
     values (as 25_instrument_checks.py E-3 does) and exact decimal subtraction
     of the printed strings -- and attacked with the audit's own functions,
     1000 shuffles, seed 20260913, best 1%.
Input   cards/ ; exam-prep/blind-proof/strict-flags/ ;
        exam-prep/second-fix/blind-proof/strict-flags-k1/ ;
        exam-prep/second-fix/identity/run-d70dd7b545bfce8a/*.csv ;
        scripts/16_identity_audit.py, scripts/lab_cards.py (imported)
Output  stdout
Rules   RULES 12 (1000 shuffles, best 1%, imported from the audit). No
        threshold is defined here.
"""
import csv, glob, os, re, random, importlib.util, sys
from collections import defaultdict
from decimal import Decimal

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(REPO, "scripts"))
import lab_cards  # noqa
spec = importlib.util.spec_from_file_location(
    "ia", os.path.join(REPO, "scripts", "16_identity_audit.py"))
ia = importlib.util.module_from_spec(spec); spec.loader.exec_module(ia)

SETS = {
    "strict-flags": (os.path.join(REPO, "exam-prep/blind-proof/strict-flags/cards"),
                     os.path.join(REPO, "exam-prep/blind-proof/strict-flags/truth-strict-flags.csv")),
    "strict-flags-k1": (os.path.join(REPO, "exam-prep/second-fix/blind-proof/strict-flags-k1/cards"),
                        os.path.join(REPO, "exam-prep/second-fix/blind-proof/strict-flags-k1/truth-strict-flags-k1.csv")),
    "raw": (os.path.join(REPO, "cards"), None),
}

def load(label):
    d, t = SETS[label]
    names = sorted(f for f in os.listdir(d) if f.endswith(".md") and f[0] in "BC")
    cards = [lab_cards.parse_any_card(os.path.join(d, n)) for n in names]
    if t:
        tr = {r["id"]: r for r in csv.DictReader(open(t, encoding="utf-8"))}
        for c in cards:
            c["coin"] = tr[c["card"]]["coin"]
    texts = [open(os.path.join(d, n), encoding="utf-8").read() for n in names]
    return cards, texts

def text_table(text):
    sec = text.split("## Before", 1)[1].split("\n## ", 1)[0]
    lines = [l for l in sec.splitlines() if l.startswith("|")]
    head = [re.sub(r" (x|r|dev)$", "", h.strip()) for h in lines[0].strip("|").split("|")]
    rows = [[x.strip() for x in l.strip("|").split("|")] for l in lines[2:]]
    return {h: [r[i] for r in rows] for i, h in enumerate(head)}

def own_auc(vecs, coins):
    n = len(vecs)
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            d = sum((a - b) ** 2 for a, b in zip(vecs[i], vecs[j])) ** 0.5
            pairs.append((d, coins[i] == coins[j]))
    pairs.sort(key=lambda x: x[0])
    # average ranks over ties
    ranks = [0.0] * len(pairs)
    i = 0
    while i < len(pairs):
        j = i
        while j + 1 < len(pairs) and pairs[j + 1][0] == pairs[i][0]:
            j += 1
        for k in range(i, j + 1):
            ranks[k] = (i + 1 + j + 1) / 2.0
        i = j + 1
    pos = [r for r, (_, s) in zip(ranks, pairs) if s]
    n1, n0 = len(pos), len(pairs) - len(pos)
    u = sum(pos) - n1 * (n1 + 1) / 2.0
    return 1.0 - u / (n1 * n0)

def nn_tie_range(vecs, coins):
    dist = ia.pair_distances(vecs)
    lo = hi = ex = 0.0
    tied_cards = 0
    for i in range(len(vecs)):
        m = min(dist[i][j] for j in range(len(vecs)) if j != i)
        cand = [j for j in range(len(vecs)) if j != i and dist[i][j] == m]
        same = [coins[j] == coins[i] for j in cand]
        lo += all(same); hi += any(same); ex += sum(same) / len(same)
        tied_cards += len(cand) > 1
    n = len(vecs)
    nn_idx = ia.nearest_neighbours(dist)
    return lo / n, hi / n, ex / n, tied_cards, ia.nn_accuracy(nn_idx, coins)

def attack(feats, keys, coins):
    vecs, used = ia.standardise(feats, keys)
    dists = ia.pair_distances(vecs)
    nn_idx = ia.nearest_neighbours(dists)
    rank, tot = ia.pair_ranks(dists)
    o_nn, o_auc = ia.nn_accuracy(nn_idx, coins), ia.pair_auc(rank, tot, coins)
    rng = random.Random(ia.SEED); perm = list(coins); a, b = [], []
    for _ in range(ia.SHUFFLES):
        rng.shuffle(perm)
        a.append(ia.nn_accuracy(nn_idx, perm)); b.append(ia.pair_auc(rank, tot, perm))
    return (round(o_nn, 6), round(ia.quantile_top(a, ia.TOP_FRACTION), 6),
            round(o_auc, 6), round(ia.quantile_top(b, ia.TOP_FRACTION), 6))

def main():
    # ---------------- A
    print("A. repeat features: own text parser vs card_features()")
    for label in SETS:
        cards, texts = load(label)
        mism = 0; checked = 0
        for c, t in zip(cards, texts):
            f = ia.card_features(c)
            tab = text_table(t)
            for name, vals in tab.items():
                if name not in ia.REPEAT_GROUP:
                    continue
                g = ia.REPEAT_GROUP[name]
                dist_ = float(len(set(vals)))
                mx = float(max(vals.count(v) for v in set(vals)))
                checked += 2
                mism += f.get("rep-%s:%s:distinct" % (g, name)) != dist_
                mism += f.get("rep-%s:%s:maxrepeat" % (g, name)) != mx
        print("   %-16s features compared: %d, mismatches: %d" % (label, checked, mism))

    # ---------------- B and C on strict-flags
    cards, texts = load("strict-flags")
    coins = [c["coin"] for c in cards]
    feats = [ia.card_features(c) for c in cards]
    allkeys = sorted({k for f in feats for k in f})
    their = {r["family"]: r for r in csv.DictReader(open(os.path.join(
        REPO, "exam-prep/second-fix/identity/run-d70dd7b545bfce8a/"
              "identity-audit-blinded-strict-flags.csv"), encoding="utf-8"))}
    fams = [k for k in ia.FAMILIES if k.startswith("repeat-")]
    removable = sorted({p for k, v in ia.FAMILIES.items()
                        if k not in ia.FORCED_FAMILIES for p in v})
    print("\nB/C. strict-flags: own AUC vs CSV; NN tie range (lowest, highest, mean over random tie-breaks)")
    print("   family | features | own AUC | CSV AUC | NN as reported | NN lowest | NN highest | NN mean | cards with tied NN | CSV nn line")
    for fam in fams + ["ALL-removable"]:
        prefixes = removable if fam == "ALL-removable" else ia.FAMILIES[fam]
        keys = ia.select({k: 1 for k in allkeys}, prefixes)
        vecs, used = ia.standardise(feats, keys)
        if not used:
            print("   %s | 0 features" % fam); continue
        a = own_auc(vecs, coins)
        lo, hi, ex, tied, rep = nn_tie_range(vecs, coins)
        r = their.get(fam, {})
        print("   %s | %d | %.6f | %s | %.6f | %.6f | %.6f | %.6f | %d | %s"
              % (fam, len(used), a, r.get("pair_auc"), rep, lo, hi, ex, tied,
                 r.get("nn_chance_1pct")))

    # raw cards, repeat-close tie range (SECOND-FIX §4 item 4)
    rc, _ = load("raw")
    rcoins = [c["coin"] for c in rc]
    rfeats = [ia.card_features(c) for c in rc]
    keys = ia.select({k: 1 for k in sorted({k for f in rfeats for k in f})}, ["rep-close:"])
    vecs, used = ia.standardise(rfeats, keys)
    lo, hi, ex, tied, rep = nn_tie_range(vecs, rcoins)
    print("\n   raw cards repeat-close: NN as reported %.6f; lowest %.6f; highest %.6f; mean %.6f; tied cards %d"
          % (rep, lo, hi, ex, tied))
    k1c, _ = load("strict-flags-k1")
    k1coins = [c["coin"] for c in k1c]
    k1f = [ia.card_features(c) for c in k1c]
    keys = ia.select({k: 1 for k in sorted({k for f in k1f for k in f})}, ["rep-close:"])
    vecs, used = ia.standardise(k1f, keys)
    lo, hi, ex, tied, rep = nn_tie_range(vecs, k1coins)
    print("   k1 set repeat-close:    NN as reported %.6f; lowest %.6f; highest %.6f; mean %.6f; tied cards %d"
          % (rep, lo, hi, ex, tied))

    # ---------------- D
    print("\nD. K-4 granularity: float subtraction (as E-3) vs exact decimal subtraction")
    print("   set | version | distinct values | nn | nn line | AUC | AUC line")
    for label in ("strict-flags", "strict-flags-k1"):
        cards, texts = load(label)
        coins = [c["coin"] for c in cards]
        ff, fd = [], []
        for c, t in zip(cards, texts):
            vals = sorted(set(c["cols"]["close"]))
            gaps = [b - a for a, b in zip(vals, vals[1:]) if b - a > 0]
            ff.append({"g": min(gaps) if gaps else 0.0})
            dv = sorted({Decimal(x) for x in text_table(t)["close"]})
            dg = [b - a for a, b in zip(dv, dv[1:]) if b - a > 0]
            fd.append({"g": float(min(dg)) if dg else 0.0})
        for ver, feats_ in (("float", ff), ("exact", fd)):
            r = attack(feats_, ["g"], coins)
            print("   %s | %s | %d | %s | %s | %s | %s"
                  % (label, ver, len({f["g"] for f in feats_}), *r))

if __name__ == "__main__":
    main()
