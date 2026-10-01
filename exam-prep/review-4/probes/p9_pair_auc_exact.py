#!/usr/bin/env python3
"""p9 · review-4 · an independent exact pair AUC for the families whose
pair-AUC figures JQ-R04-CONTENT shows. Features are taken from script 29's
card_features() and its feature selection (select/standardise only to learn
which features are used); everything after that is written here: squared
z-scored distances as exact Fractions (exact sample variance, divisor n-1;
a zero-variance feature contributes nothing), then the Mann-Whitney AUC for
"a same-coin pair is closer than a different-coin pair", ties counted 1/2,
as an exact Fraction. Compared with the audit CSV's pair_auc (6 decimals).
Reads the three card sets and their truth files, and the fourth-fix audit
CSVs. Writes nothing (prints)."""
import csv, glob, importlib.util, os, sys
from fractions import Fraction
from collections import defaultdict
ROOT = "/home/user/balikcil"
sys.path.insert(0, os.path.join(ROOT, "scripts"))
spec = importlib.util.spec_from_file_location("a29", os.path.join(ROOT, "scripts/29_identity_audit_exact.py"))
a = importlib.util.module_from_spec(spec); spec.loader.exec_module(a)
import lab_cards
SETS = {
 "strict-flags": ("exam-prep/blind-proof/strict-flags/cards", "exam-prep/blind-proof/strict-flags/truth-strict-flags.csv", "9ff0ffec3fe21ebe"),
 "strict-flags-k1": ("exam-prep/second-fix/blind-proof/strict-flags-k1/cards", "exam-prep/second-fix/blind-proof/strict-flags-k1/truth-strict-flags-k1.csv", "762815a877c19551"),
 "strict-flags-unrounded": ("exam-prep/third-fix/blind-proof/strict-flags-unrounded/cards", "exam-prep/third-fix/blind-proof/strict-flags-unrounded/truth-strict-flags-unrounded.csv", "d6557e91f9f97f7b"),
}
FAMS = {"strict-flags": ["trades-level", "repeat-trades", "repeat-close", "granularity-close"],
        "strict-flags-k1": ["repeat-close", "granularity-close"],
        "strict-flags-unrounded": ["trades-level", "repeat-trades"]}
for name, (cd, tr, run) in SETS.items():
    cd = os.path.join(ROOT, cd)
    names = sorted(f for f in os.listdir(cd) if f.endswith(".md") and f != "INDEX.md")
    cards = [lab_cards.parse_any_card(os.path.join(cd, n)) for n in names]
    truth = {r["id"]: r for r in csv.DictReader(open(os.path.join(ROOT, tr), encoding="utf-8"))}
    coins = [truth[c["card"]]["coin"] for c in cards]
    feats = [a.card_features(c) for c in cards]
    allkeys = sorted({k for f in feats for k in f})
    audit = {r["family"]: r for r in csv.DictReader(open(glob.glob(os.path.join(ROOT, "exam-prep/fourth-fix/identity/run-%s/identity-audit-*.csv" % run))[0]))}
    n = len(cards)
    for fam in FAMS[name]:
        keys = a.select({k: 1 for k in allkeys}, a.FAMILIES[fam])
        _, used = a.standardise(feats, keys)
        cols = []
        for k in used:
            xs = [Fraction(r[k]) for r in feats]
            m = sum(xs, Fraction(0)) / n
            v = sum(((x - m) ** 2 for x in xs), Fraction(0)) / (n - 1)
            if v:
                cols.append((xs, v))
        same, diff = [], []
        for i in range(n):
            for j in range(i + 1, n):
                d = sum(((xs[i] - xs[j]) ** 2 / v for xs, v in cols), Fraction(0))
                (same if coins[i] == coins[j] else diff).append(d)
        # Mann-Whitney: P(same < diff) + 1/2 P(equal), by a merged sort
        allv = sorted([(d, 0) for d in same] + [(d, 1) for d in diff])
        diff_seen = 0; num = Fraction(0); i = 0
        while i < len(allv):
            j = i
            while j < len(allv) and allv[j][0] == allv[i][0]:
                j += 1
            s = sum(1 for k in range(i, j) if allv[k][1] == 0); dd = (j - i) - s
            # each same here beats the diffs not yet seen (strictly larger), ties half
            num += s * (len(diff) - diff_seen - dd) + Fraction(s * dd, 2)
            diff_seen += dd; i = j
        auc = num / (len(same) * len(diff))
        print("%s | %s | exact AUC %.6f | audit %s | equal at 6 dp: %s" % (name, fam, float(auc), audit[fam]["pair_auc"], "%.6f" % float(auc) == "%.6f" % float(audit[fam]["pair_auc"])))
        sys.stdout.flush()
