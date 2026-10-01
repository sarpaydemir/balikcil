#!/usr/bin/env python3
"""
p3b_tie_ranges_all.py -- review-2 probe (R-04), follow-up to p3.

What it does
  For every family the second-fix audit reports on `strict-flags` (run
  d70dd7b545bfce8a) and on `strict-flags-k1` (run 4a33cb19150e9718), and for the
  K-4 granularity feature (exact decimal version, see p3 D), it computes the
  nearest-neighbour score's lowest / highest value over every possible
  tie-break and its mean under uniformly random tie-breaks (exact, no
  randomness), and sets them beside the reported score and its chance line.
  A family's NN verdict is called "tie-dependent" here when the reported
  verdict (beats / does not beat its line) differs from the verdict the mean
  gives; no new threshold is introduced -- the line is the audit's own.
Input   exam-prep/blind-proof/strict-flags/ ; exam-prep/second-fix/blind-proof/strict-flags-k1/ ;
        the two second-fix audit CSVs ; scripts/16_identity_audit.py (imported)
Output  stdout
"""
import csv, os, sys, importlib.util
from decimal import Decimal

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(REPO, "scripts"))
import lab_cards  # noqa
spec = importlib.util.spec_from_file_location(
    "ia", os.path.join(REPO, "scripts", "16_identity_audit.py"))
ia = importlib.util.module_from_spec(spec); spec.loader.exec_module(ia)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p3_repeat_and_ties import nn_tie_range, text_table, attack  # noqa

SETS = {
    "strict-flags": ("exam-prep/blind-proof/strict-flags/cards",
                     "exam-prep/blind-proof/strict-flags/truth-strict-flags.csv",
                     "exam-prep/second-fix/identity/run-d70dd7b545bfce8a/identity-audit-blinded-strict-flags.csv"),
    "strict-flags-k1": ("exam-prep/second-fix/blind-proof/strict-flags-k1/cards",
                        "exam-prep/second-fix/blind-proof/strict-flags-k1/truth-strict-flags-k1.csv",
                        "exam-prep/second-fix/identity/run-4a33cb19150e9718/identity-audit-blinded-strict-flags-k1.csv"),
}

for label, (cd, tp, csvp) in SETS.items():
    cd, tp, csvp = (os.path.join(REPO, x) for x in (cd, tp, csvp))
    names = sorted(f for f in os.listdir(cd) if f.endswith(".md"))
    cards = [lab_cards.parse_any_card(os.path.join(cd, n)) for n in names]
    tr = {r["id"]: r for r in csv.DictReader(open(tp, encoding="utf-8"))}
    coins = [tr[c["card"]]["coin"] for c in cards]
    feats = [ia.card_features(c) for c in cards]
    allkeys = sorted({k for f in feats for k in f})
    rows = list(csv.DictReader(open(csvp, encoding="utf-8")))
    print("\n## %s" % label)
    print("family | features | NN reported | line | reported beats | NN lowest | NN highest | NN mean | mean beats | tie-dependent")
    for r in rows:
        if not r["feature_names"]:
            continue
        # keys rebuilt from the audit's own family prefixes (feature names
        # contain spaces, so the CSV's space-joined list cannot be split back)
        fam = r["family"]
        if fam == "ALL":
            prefixes = sorted({p for v in ia.FAMILIES.values() for p in v})
        elif fam == "ALL-except-frozen-volatility":
            prefixes = sorted({p for k, v in ia.FAMILIES.items()
                               if k != "volatility-frozen" for p in v})
        elif fam == "ALL-removable":
            prefixes = sorted({p for k, v in ia.FAMILIES.items()
                               if k not in ia.FORCED_FAMILIES for p in v})
        else:
            prefixes = ia.FAMILIES[fam]
        keys = ia.select({k: 1 for k in allkeys}, prefixes)
        vecs, used = ia.standardise(feats, keys)
        if len(used) != int(r["features_used"]):
            print("FEATURE COUNT MISMATCH", fam, len(used), r["features_used"])
        lo, hi, ex, tied, rep = nn_tie_range(vecs, coins)
        line = float(r["nn_chance_1pct"])
        rb, mb = rep > line, ex > line
        print("%s | %d | %.6f | %.6f | %s | %.6f | %.6f | %.6f | %s | %s"
              % (r["family"], len(used), rep, line, "YES" if rb else "no",
                 lo, hi, ex, "YES" if mb else "no",
                 "TIE-DEPENDENT" if rb != mb else ""))
    # K-4, exact decimal steps
    fd = []
    for n in names:
        t = open(os.path.join(cd, n), encoding="utf-8").read()
        dv = sorted({Decimal(x) for x in text_table(t)["close"]})
        dg = [b - a for a, b in zip(dv, dv[1:]) if b - a > 0]
        fd.append({"g": float(min(dg)) if dg else 0.0})
    vecs, used = ia.standardise(fd, ["g"])
    lo, hi, ex, tied, rep = nn_tie_range(vecs, coins)
    o_nn, nn_line, o_auc, auc_line = attack(fd, ["g"], coins)
    print("K-4 exact | 1 | %.6f | %.6f | %s | %.6f | %.6f | %.6f | %s | AUC %.6f line %.6f"
          % (rep, nn_line, "YES" if rep > nn_line else "no", lo, hi, ex,
             "YES" if ex > nn_line else "no", o_auc, auc_line))
