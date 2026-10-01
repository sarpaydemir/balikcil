#!/usr/bin/env python3
"""p1 · review-4 · is the tie-free nearest-neighbour verdict exact?

scripts/29_identity_audit_exact.py compares DISTANCES exactly, but sums the
tie-free score (nn_tie_free) in floating point, for the observed labels and
for each of the 1,000 shuffles, and compares obs > line in floating point.
Two labelings whose tie-free scores are equal in exact arithmetic can differ
in the last bit. This probe recomputes, for the families the juror files
quote, the observed tie-free score and all 1,000 null values as exact
fractions (same tie sets, same RNG, same seed, same shuffles as script 29),
the line as script 29 defines it (10th largest of 1,000: quantile_top), and:
  - the float verdict (script 29's), the exact verdict
  - how many null values are >= / > the observed value, exactly.
Constants: SHUFFLES, TOP_FRACTION, SEED imported from script 29.
Reads: the three card sets named below and their truth files; scripts/.
Writes nothing (prints)."""
import csv, importlib.util, os, random, sys
from fractions import Fraction
ROOT = "/home/user/balikcil"
sys.path.insert(0, os.path.join(ROOT, "scripts"))
spec = importlib.util.spec_from_file_location("a29", os.path.join(ROOT, "scripts/29_identity_audit_exact.py"))
a = importlib.util.module_from_spec(spec); spec.loader.exec_module(a)
import lab_cards
SETS = {
 "strict-flags": ("exam-prep/blind-proof/strict-flags/cards", "exam-prep/blind-proof/strict-flags/truth-strict-flags.csv"),
 "strict-flags-k1": ("exam-prep/second-fix/blind-proof/strict-flags-k1/cards", "exam-prep/second-fix/blind-proof/strict-flags-k1/truth-strict-flags-k1.csv"),
 "strict-flags-unrounded": ("exam-prep/third-fix/blind-proof/strict-flags-unrounded/cards", "exam-prep/third-fix/blind-proof/strict-flags-unrounded/truth-strict-flags-unrounded.csv"),
}
FAMS = sys.argv[1:] or ["trades-level", "repeat-trades", "repeat-close", "granularity-close", "ALL-removable"]
def tf_exact(tsets, labels):
    s = Fraction(0)
    for i, t in enumerate(tsets):
        s += Fraction(sum(1 for j in t if labels[j] == labels[i]), len(t))
    return s / len(labels)
for name, (cd, tr) in SETS.items():
    cd = os.path.join(ROOT, cd); tr = os.path.join(ROOT, tr)
    names = sorted(f for f in os.listdir(cd) if f.endswith(".md") and f != "INDEX.md")
    cards = [lab_cards.parse_any_card(os.path.join(cd, n)) for n in names]
    truth = {r["id"]: r for r in csv.DictReader(open(tr, encoding="utf-8"))}
    for c in cards:
        t = truth[c["card"]]; c["coin"] = t["coin"]; c["start_hour_utc"] = t["start_hour_utc"]
    coins = [c["coin"] for c in cards]
    feats = [a.card_features(c) for c in cards]
    allkeys = sorted({k for f in feats for k in f})
    specs = dict(a.FAMILIES)
    specs["ALL-removable"] = sorted({p for k, v in a.FAMILIES.items() if k not in a.FORCED_FAMILIES for p in v})
    for fam in FAMS:
        keys = a.select({k: 1 for k in allkeys}, specs[fam])
        vecs, used = a.standardise(feats, keys)
        if not used:
            print(name, fam, "no features"); continue
        d = a.exact_distance_codes(feats, used)
        ts = a.nearest_tie_sets(d)
        obs_f = a.nn_tie_free(ts, coins); obs_x = tf_exact(ts, coins)
        rng = random.Random(a.SEED); perm = list(coins)
        nf, nx = [], []
        for _ in range(a.SHUFFLES):
            rng.shuffle(perm)
            nf.append(a.nn_tie_free(ts, perm)); nx.append(tf_exact(ts, perm))
        line_f = a.quantile_top(nf, a.TOP_FRACTION); line_x = a.quantile_top(nx, a.TOP_FRACTION)
        ge = sum(1 for v in nx if v >= obs_x); gt = sum(1 for v in nx if v > obs_x)
        print("%s | %s | obs float %.9f exact %.9f | line float %.9f exact %.9f | float beats %s | exact beats %s | nulls >= obs %d, > obs %d (of %d)"
              % (name, fam, obs_f, float(obs_x), line_f, float(line_x), obs_f > line_f, obs_x > line_x, ge, gt, a.SHUFFLES))
        sys.stdout.flush()
