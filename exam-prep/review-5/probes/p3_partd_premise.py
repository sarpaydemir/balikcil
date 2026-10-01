#!/usr/bin/env python3
"""
p3_partd_premise.py -- REVIEW-5 probe. Independent check of the premise
sentence of JQ-R04-CONTENT part d (fifth-fix file, lines 288-290):
"In the audit as it stands, everything it computes from the bitcoin and
ethereum columns, the trade-count column, the price column and the other
ranked columns is inside the row."

How: parses scripts/29_identity_audit_exact.py with `ast` (not imported, not
run, so no bytecode is written and none of its code executes); reads
FAMILIES, FORCED_FAMILIES and REPEAT_GROUP as literals; builds the prefix
list of ALL-removable exactly as the script's construction does (every
family not in FORCED_FAMILIES). The map from printed column to feature
prefixes below is my reading of card_features() (lines 217-345 of the
script); it is written out so that it can be checked line by line.
Also prints, verbatim, the comment lines that state why each forced family
is forced (they are the instrument's own grounds).

Input : scripts/29_identity_audit_exact.py
Output: stdout (saved beside this file as p3_partd_premise.out)
No threshold, no randomness.
"""
import ast
import hashlib
import os
import sys

sys.dont_write_bytecode = True
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
AUDIT = os.path.join(ROOT, "scripts", "29_identity_audit_exact.py")

src = open(AUDIT, encoding="utf-8").read()
print("audit SHA-256", hashlib.sha256(src.encode()).hexdigest())
tree = ast.parse(src)
lit = {}
for node in tree.body:
    if isinstance(node, ast.Assign) and len(node.targets) == 1 and \
            isinstance(node.targets[0], ast.Name) and \
            node.targets[0].id in ("FAMILIES", "FORCED_FAMILIES",
                                   "REPEAT_GROUP"):
        lit[node.targets[0].id] = ast.literal_eval(node.value)
FAM, FORCED, RG = lit["FAMILIES"], lit["FORCED_FAMILIES"], lit["REPEAT_GROUP"]
removable = sorted({p for k, v in FAM.items() if k not in FORCED for p in v})
forced_p = sorted({p for k, v in FAM.items() if k in FORCED for p in v})
print("FORCED_FAMILIES", list(FORCED))
print("prefixes left out of ALL-removable", forced_p)

# My reading of card_features(): printed column -> feature prefixes it feeds.
# rep-<tag>: from REPEAT_GROUP; shape:*_<tag>; level prefixes.
SHAPE_TAG = {"quote vol": "vol", "trades": "trades", "open int": "oi",
             "depth -1%": "depth_bid", "depth +1%": "depth_ask",
             "L/S acct": "ls_acct", "top L/S pos": "top_ls",
             "taker L/S": "taker_ls"}
LEVEL = {"close": ["price:"], "quote vol": ["volume:"],
         "trades": ["trades:"], "open int": ["openint:"],
         "depth -1%": ["depth:"], "depth +1%": ["depth:"],
         "L/S acct": ["ratio:"], "top L/S pos": ["ratio:"],
         "taker L/S": ["ratio:"], "taker buy%": ["takerbuy:"],
         "BTC": ["btceth:"], "ETH": ["btceth:"]}
GRAN = {"close": ["gran-close:"]}
COLS = {"bitcoin/ethereum": ["BTC", "ETH"], "trade count": ["trades"],
        "price": ["close"],
        "other ranked": ["quote vol", "taker buy%", "open int", "L/S acct",
                         "top L/S pos", "taker L/S", "depth -1%",
                         "depth +1%"]}


def covered(prefix):
    """Is a feature with this name/prefix selected by ALL-removable?"""
    return any(prefix.startswith(p) or p.startswith(prefix)
               for p in removable)


def forced_hit(prefix):
    return [p for p in forced_p if prefix.startswith(p) or
            p.startswith(prefix)]


all_ok = True
for group, cols in COLS.items():
    for c in cols:
        feeds = list(LEVEL.get(c, [])) + list(GRAN.get(c, []))
        if c in RG:
            feeds.append("rep-%s:" % RG[c])
        if c in SHAPE_TAG:
            feeds.append("shape:")
        res = [(f, covered(f), forced_hit(f)) for f in feeds]
        ok = all(r[1] and not r[2] for r in res)
        all_ok &= ok
        print("%-17s %-12s %s %s" % (group, c, "inside" if ok else "NOT",
                                      res))
print("premise holds:", all_ok)

print("\nInstrument's stated grounds for the forced families (verbatim):")
for i, line in enumerate(src.splitlines(), 1):
    if 426 <= i <= 434:
        print("%4d  %s" % (i, line))
