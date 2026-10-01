#!/usr/bin/env python3
"""p6 · review-4 · the ALL-removable row in the third-fix audit runs (script 16,
the runs the JQ-R04-GATE file cites) against the exact audit runs (script 29,
fourth-fix), on the five card sets the GATE file shows; every column printed.
Reads exam-prep/third-fix/identity/ and exam-prep/review-4/rerun/identity/.
Writes nothing (prints)."""
import csv, glob, os
ROOT = "/home/user/balikcil"
pairs = {"strict-flags": ("e05144718b909704", "9ff0ffec3fe21ebe"),
         "strict": ("1f2ae3cf3a5b2044", "45d062efe77c9251"),
         "rank": ("96f1d17e27b8afaf", "446adf64f8e8235c"),
         "ratio": ("12b07f79e74f0be7", "989b8f21b23e0310"),
         "strict-flags-k1": ("ded6a9caaf77d910", "762815a877c19551")}
COLS = ["features_used", "nn_same_coin_accuracy", "nn_chance_1pct", "nn_beats_chance",
        "pair_auc", "auc_chance_1pct", "auc_beats_chance", "cards_with_tied_nn",
        "nn_tie_free", "nn_tie_free_chance_1pct", "nn_tie_free_beats_chance"]
def row(folder, run):
    f = glob.glob(os.path.join(ROOT, folder, "run-" + run, "identity-audit-*.csv"))
    assert len(f) == 1, (folder, run, f)
    for r in csv.DictReader(open(f[0])):
        if r["family"] == "ALL-removable":
            return r
for s, (a, b) in pairs.items():
    ra = row("exam-prep/third-fix/identity", a); rb = row("exam-prep/review-4/rerun/identity", b)
    same = all(ra[c] == rb[c] for c in COLS)
    print(s, a, "vs", b, "identical on every column:" , same)
    print("   script 16:", [ra[c] for c in COLS])
    print("   script 29:", [rb[c] for c in COLS])
