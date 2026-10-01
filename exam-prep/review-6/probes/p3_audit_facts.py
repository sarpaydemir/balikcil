#!/usr/bin/env python3
"""
p3_audit_facts.py -- review 6 probe. Checks, against the audit's code, every
statement JQ-R04-CARRIES and JQ-R04-CONTENT-d make about which features the
audit computes from which printed column, which family holds them, which
families are outside `ALL-removable`, when a feature is not used, and what
"beats" means. The audit is parsed with `ast` and read as text; it is not
imported and not run.

Input : scripts/29_identity_audit_exact.py
Output: stdout only (captured into p3_audit_facts.out).
Rules : RULES 19 (no unmeasured statement). No threshold, no randomness.
Run   : PYTHONDONTWRITEBYTECODE=1 python3 -B exam-prep/review-6/probes/p3_audit_facts.py
"""
import ast
import os
import re
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SRC = open(os.path.join(REPO, "scripts/29_identity_audit_exact.py"),
           encoding="utf-8").read()
tree = ast.parse(SRC)
G = {}
for node in tree.body:
    if isinstance(node, ast.Assign) and len(node.targets) == 1 \
            and isinstance(node.targets[0], ast.Name) \
            and node.targets[0].id in ("FAMILIES", "REPEAT_GROUP",
                                       "FORCED_FAMILIES"):
        G[node.targets[0].id] = ast.literal_eval(node.value)
FAM, RG, FORCED = G["FAMILIES"], G["REPEAT_GROUP"], G["FORCED_FAMILIES"]

bad = 0


def check(name, ok, detail=""):
    global bad
    print("%-4s %s %s" % ("ok" if ok else "FAIL", name, detail))
    bad += not ok


# feature keys written literally in card_features()
lit = set(re.findall(r'f\["([a-z0-9\-]+:[a-z0-9_]+)"\]', SRC))
check("trades-level prefixes", FAM["trades-level"] == ["trades:",
                                                       "p7:log_avg_trades"],
      str(FAM["trades-level"]))
check("one 'trades:' feature, the log of the median",
      sorted(k for k in lit if k.startswith("trades:")) ==
      ["trades:log_median_trades"]
      and 'safelog(median(col["trades"]))' in SRC)
check("p7:log_avg_trades read from the previous-7-day line",
      re.search(r'avg hourly trades.*\n.*\n\s*f\["p7:log_avg_trades"\]', SRC)
      is not None)
check("repeat-trades = rep-trades: only", FAM["repeat-trades"] ==
      ["rep-trades:"])
check("only `trades` maps to repeat group 'trades'",
      [k for k, v in RG.items() if v == "trades"] == ["trades"])
check("two repeat features per column (distinct, maxrepeat)",
      ':distinct" % (tag, name)' in SRC and ':maxrepeat" % (tag, name)' in SRC)
m = re.search(r'for name, tag in \(\(("quote vol".*?)\):\n', SRC, re.S)
shape_cols = re.findall(r'\("([^"]+)", "[a-z_]+"\)', m.group(0)) if m else []
check("shape-scale-free columns", shape_cols == [
    "quote vol", "trades", "open int", "depth -1%", "depth +1%", "L/S acct",
    "top L/S pos", "taker L/S"], str(shape_cols))
check("two shape features per column (sd_log, acf1_log)",
      'f["shape:sd_log_" + tag]' in SRC and 'f["shape:acf1_log_" + tag]' in SRC)
check("shape-scale-free = shape: only", FAM["shape-scale-free"] == ["shape:"])
others = [k for k, v in FAM.items()
          if any(p.startswith(("trades:", "rep-trades:", "shape:",
                               "p7:log_avg_trades")) for p in v)]
check("families holding any trade-count feature", sorted(others) ==
      ["repeat-trades", "shape-scale-free", "trades-level"], str(others))
check("FORCED_FAMILIES", tuple(FORCED) == ("volatility-frozen", "funding-line",
                                           "p7-shape", "repeat-chg"))
check("p7-shape = price_pct, range_pct", FAM["p7-shape"] ==
      ["p7:price_pct", "p7:range_pct"])
check("ALL-removable = every family not in FORCED_FAMILIES",
      re.search(r'\("ALL-removable",\s*sorted\(\{p for k, v in FAMILIES\.items'
                r'\(\)\s*if k not in FORCED_FAMILIES', SRC) is not None)
inside = ["btc-eth", "repeat-btceth", "trades-level", "repeat-trades",
          "shape-scale-free", "price-level", "repeat-close",
          "granularity-close", "volume-level", "openint-level", "depth-level",
          "ratio-level", "taker-buy", "repeat-volume", "repeat-takerbuy",
          "repeat-openint", "repeat-ratio", "repeat-depth"]
check("families of BTC/ETH, trades, close and the other ranked columns are "
      "all outside FORCED", not set(inside) & set(FORCED))
check("p7 features inside the row (log_avg_vol in volume-level, "
      "log_avg_trades in trades-level)",
      "p7:log_avg_vol" in FAM["volume-level"]
      and "volume-level" not in FORCED and "trades-level" not in FORCED)
check("a feature absent on any card, or constant, is dropped",
      "if any(v is None for v in vals):" in SRC
      and "if s is None or s == 0:" in SRC)
check("beats = strictly above the line",
      '"YES" if obs_nn > nn_line' in SRC and '"YES" if obs_auc > auc_line'
      in SRC and '"YES" if obs_tf > tf_line' in SRC)
print("failed %d" % bad)
sys.exit(1 if bad else 0)
