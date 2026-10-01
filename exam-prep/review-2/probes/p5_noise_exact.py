#!/usr/bin/env python3
"""
p5_noise_exact.py -- review-2 probe (N-1, the second-fix dispute of REVIEW §4.2).

What it does
  Under a card-level (or representative) shuffle the null distribution of
  accuracy for a 0/1 answer vector against 0/1 labels is EXACT: with n cards,
  A answers equal to 1 and L labels equal to 1, matches = n - A - L + 2X with
  X hypergeometric(n, L, A). RULES 12's line is the 10th largest of 1,000
  draws (quantile_top with fraction 0.01 in both instruments). This probe
  computes, exactly and with no randomness:
    1. the exact 1% point of the null, for the `none/none/none` synthetic-iid
       vector of 15_event_collapse.py (seed 20260913);
    2. the exact distribution of the 10th-largest-of-1,000 statistic (what the
       instrument reports), its 2.5% / 50% / 97.5% points, and the probability
       that two independent such statistics differ by 0.0131 or more;
    3. the same for every representative-column row of the second-fix
       calibration (n = number of events), so that the "block above
       representative" rows can be set against the noise of the
       representative column itself.
  The 2.5% / 97.5% points are reported as a description of spread, not as a
  test threshold.
Input   cards/ ; exam-prep/collapse/run-756cf4ea156d92c3/events.csv and
        shuffle-calibration.csv ; scripts/15_event_collapse.py (constants only)
Output  stdout
"""
import csv, os, sys, random, importlib.util
from fractions import Fraction
from math import comb
from collections import defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(REPO, "scripts"))
import lab_cards  # noqa
spec = importlib.util.spec_from_file_location(
    "ec", os.path.join(REPO, "scripts", "15_event_collapse.py"))
ec = importlib.util.module_from_spec(spec); spec.loader.exec_module(ec)
N_DRAWS, K = ec.SHUFFLES, int(round(ec.TOP_FRACTION * ec.SHUFFLES))  # 1000, 10

def null_pmf(n, A, L):
    tot = comb(n, A)
    pmf = {}
    for x in range(max(0, A + L - n), min(A, L) + 1):
        acc = Fraction(n - A - L + 2 * x, n)
        pmf[acc] = pmf.get(acc, 0) + Fraction(comb(L, x) * comb(n - L, A - x), tot)
    return dict(sorted(pmf.items()))

def kth_largest_dist(pmf):
    """P(10th largest of 1000 iid draws = v) for each support value v."""
    vals = list(pmf)
    sf = {}                         # P(draw >= v)
    run = Fraction(0)
    for v in reversed(vals):
        run += pmf[v]; sf[v] = run
    def p_at_least_k(p):            # P(Bin(N,p) >= K), float is enough here
        p = float(p)
        q = 1.0 - p
        s = 0.0
        for j in range(K):
            s += comb(N_DRAWS, j) * (p ** j) * (q ** (N_DRAWS - j))
        return 1.0 - s
    G = {v: p_at_least_k(sf[v]) for v in vals}      # P(stat >= v)
    out = {}
    for i, v in enumerate(vals):
        nxt = G[vals[i + 1]] if i + 1 < len(vals) else 0.0
        out[v] = G[v] - nxt
    return out

def pts(d):
    c, res = 0.0, {}
    for v, p in d.items():
        c += p
        for q in (0.025, 0.5, 0.975):
            if q not in res and c >= q:
                res[q] = float(v)
    return res

def p_diff_ge(d, delta):
    items = [(float(v), p) for v, p in d.items() if p > 0]
    return sum(p1 * p2 for v1, p1 in items for v2, p2 in items
               if abs(v1 - v2) >= delta - 1e-9)

def exact_top(pmf):
    run = Fraction(0)
    for v in reversed(list(pmf)):
        run += pmf[v]
        if run >= Fraction(1, 100):
            return float(v)

cards = lab_cards.load_all(os.path.join(REPO, "cards"))
by = {c["card"]: c for c in cards}
ids = sorted(by)
labels = [1 if by[c]["kind"] == "large" else 0 for c in ids]
rng = random.Random(ec.SEED)
answers = [rng.randint(0, 1) for _ in ids]
n, A, L = len(ids), sum(answers), sum(labels)
pmf = null_pmf(n, A, L)
d = kth_largest_dist(pmf)
p = pts(d)
print("none/none/none synthetic-iid: n=%d A=%d L=%d" % (n, A, L))
print("  exact 1%% point of the null: %.4f" % exact_top(pmf))
print("  reported statistic (10th largest of 1000): 2.5%% %.4f | median %.4f | 97.5%% %.4f"
      % (p[0.025], p[0.5], p[0.975]))
# the reported values are rounded to 4 decimals; the support moves in steps
# of 2/n, so "0.0131" is exactly 2 steps (0.013072), "0.0196" 3, "0.0261" 4.
step = 2.0 / n
print("  support step 2/n = %.6f" % step)
print("  distribution of the reported line:",
      ", ".join("%.4f: %.4f" % (float(v), q) for v, q in d.items() if q > 1e-4))
for k in (1, 2, 3, 4):
    print("  P(two independent reported lines differ by >= %d steps = %.4f) = %.4f"
          % (k, k * step, p_diff_ge(d, k * step)))

# representative column: answers drawn fresh per configuration in the instrument
ev = defaultdict(lambda: defaultdict(list))
for r in csv.DictReader(open(os.path.join(REPO,
        "exam-prep/collapse/run-756cf4ea156d92c3/events.csv"), encoding="utf-8")):
    ev[r["config"]][r["event_id"]].append(r["card"])
cal = list(csv.DictReader(open(os.path.join(REPO,
        "exam-prep/collapse/run-756cf4ea156d92c3/shuffle-calibration.csv"), encoding="utf-8")))
print("\nrepresentative column (exact): config | n | reported | exact 1% point | reported-statistic 2.5% / 97.5% | block reported")
seen = set()
for r in cal:
    cfg = r["config"]
    if cfg in seen:
        continue
    seen.add(cfg)
    events = list(ev[cfg].values())
    reps = [sorted(e, key=lambda c: (by[c]["start_hour_utc"], c))[0] for e in events]
    # same order the instrument uses: events in the order collapse() returns them
    em = ec.identity_map([{"id": c, "coin": by[c]["coin"], "start_dt": ec.parse_hour(by[c]["start_hour_utc"])} for c in ids]) if cfg == "none/none/none" else None
    rl = [1 if by[c]["kind"] == "large" else 0 for c in reps]
    rr = random.Random(ec.SEED)
    ra = [rr.randint(0, 1) for _ in reps]
    pm = null_pmf(len(reps), sum(ra), sum(rl))
    dd = kth_largest_dist(pm); pp = pts(dd)
    rows = [x for x in cal if x["config"] == cfg]
    print("  %s | %d | %s | %.4f | %.4f / %.4f | %s"
          % (cfg, len(reps), r["representative_shuffle_1pct_boundary"], exact_top(pm),
             pp[0.025], pp[0.975],
             " / ".join("%s %s" % (x["predictor"].replace("synthetic-", ""),
                                   x["block_shuffle_1pct_boundary"]) for x in rows)))
