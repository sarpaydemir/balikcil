#!/usr/bin/env python3
"""
p6_gate_sensitivity.py -- review-2 probe (R-04).

What it does
  The second-fix run's K-2 classes every `repeat-*` family except `repeat-chg`
  as removable. Three of them read columns the frozen canteen book or TACTICS
  touches: `repeat-depth` (B-4 reads runs of identical depth values),
  `repeat-openint` (B-3 reads open-interest zeros) and `repeat-close` (TACTICS 6
  puts a price column starting from 100 on the card). This probe asks whether
  the gate row's outcome depends on that classification: it recomputes the
  `ALL-removable` row with those families moved, one way and all together, to
  the forced side, with the audit's own attacks, 1000 shuffles, seed 20260913,
  best 1%. It also reports the first run's 23-feature gate row plus each single
  repeat family, to show which family moves the gate.
  It does not propose a classification; it only measures whether the outcome
  turns on one.
Input   exam-prep/blind-proof/strict-flags/ ; scripts/16_identity_audit.py
Output  stdout
"""
import csv, os, sys, importlib.util
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(REPO, "scripts"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lab_cards  # noqa
from p3_repeat_and_ties import attack  # noqa
spec = importlib.util.spec_from_file_location(
    "ia", os.path.join(REPO, "scripts", "16_identity_audit.py"))
ia = importlib.util.module_from_spec(spec); spec.loader.exec_module(ia)

cd = os.path.join(REPO, "exam-prep/blind-proof/strict-flags/cards")
tr = {r["id"]: r for r in csv.DictReader(open(os.path.join(
    REPO, "exam-prep/blind-proof/strict-flags/truth-strict-flags.csv"), encoding="utf-8"))}
names = sorted(f for f in os.listdir(cd) if f.endswith(".md"))
cards = [lab_cards.parse_any_card(os.path.join(cd, n)) for n in names]
coins = [tr[c["card"]]["coin"] for c in cards]
feats = [ia.card_features(c) for c in cards]
allkeys = {k: 1 for f in feats for k in f}

def row(label, forced):
    prefixes = sorted({p for k, v in ia.FAMILIES.items() if k not in forced for p in v})
    keys = ia.select(allkeys, prefixes)
    vecs, used = ia.standardise(feats, keys)
    nn, nnl, auc, aucl = attack(feats, keys, coins)
    print("%-62s | %2d | nn %.6f line %.6f %s | AUC %.6f line %.6f %s"
          % (label, len(used), nn, nnl, "BEATS" if nn > nnl else "no",
             auc, aucl, "BEATS" if auc > aucl else "no"))

F = set(ia.FORCED_FAMILIES)
REP = {k for k in ia.FAMILIES if k.startswith("repeat-")}
print("gate row variants on strict-flags | features | nearest neighbour | pair AUC")
row("second-fix ALL-removable (as audited)", F)
row("... with repeat-depth forced", F | {"repeat-depth"})
row("... with repeat-openint forced", F | {"repeat-openint"})
row("... with repeat-close forced", F | {"repeat-close"})
row("... with repeat-depth, -openint, -close forced", F | {"repeat-depth", "repeat-openint", "repeat-close"})
row("first-run feature set (every repeat-* family excluded)", F | REP)
for fam in sorted(REP - {"repeat-chg", "repeat-btceth"}):
    row("first-run feature set + %s only" % fam, F | (REP - {fam}))
