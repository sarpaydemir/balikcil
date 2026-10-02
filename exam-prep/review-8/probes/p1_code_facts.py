#!/usr/bin/env python3
"""Review 8, probe p1 -- statements of the eighth-fix JQ-R04-CONTENT-d file
about the audit, checked against the audit's code and against card sets.

What it does: loads scripts/29_identity_audit_exact.py as a module (main() is
not run), computes card_features() on the raw observation cards and on the
four blinded observation sets under exam-prep/blind-proof/, and reports:
  (1) FORCED_FAMILIES and their feature prefixes;
  (2) every feature key, mapped to the one field it is read from (the map is
      transcribed from card_features(); a key the map cannot place is a
      FAIL);
  (3) REPEAT_GROUP's columns against the columns each set prints;
  (4) how many columns carry the rank suffix " r" in each set;
  (5) whether `wikipedia:present` is computed on cards that print no
      Wikipedia line;
  (6) the composition the file states for answer "yes" (every feature of a
      printed field moved out): which keys of ALL-removable remain, and
      whether any of them survives standardise() (constant/absent dropped).
It runs no attack, computes no chance line and measures no option's effect
on any gate result.
Input: scripts/29_identity_audit_exact.py, scripts/lab_cards.py, cards/,
exam-prep/blind-proof/*/cards/. Output: stdout only (redirected by the caller
into exam-prep/review-8/probes/p1_code_facts.out).
Constants: none of judgement. No randomness.
Run with PYTHONDONTWRITEBYTECODE=1 python3 -B.
"""
import importlib.util
import os
import re
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = HERE.rsplit(os.sep + "exam-prep" + os.sep, 1)[0]  # the Balikcil root
assert os.path.isfile(os.path.join(REPO, "RULES.md")), REPO
SCRIPTS = os.path.join(REPO, "scripts")
sys.path.insert(0, SCRIPTS)

spec = importlib.util.spec_from_file_location(
    "audit29", os.path.join(SCRIPTS, "29_identity_audit_exact.py"))
A = importlib.util.module_from_spec(spec)
spec.loader.exec_module(A)
import lab_cards  # noqa: E402

# feature-key -> field, transcribed from card_features()
SHAPE_TAG = {"vol": "quote vol", "trades": "trades", "oi": "open int",
             "depth_bid": "depth -1%", "depth_ask": "depth +1%",
             "ls_acct": "L/S acct", "top_ls": "top L/S pos",
             "taker_ls": "taker L/S"}
FIXED = {
    "price:log_median_close": "close",
    "volatility:mean_abs_chg": "chg%", "volatility:max_abs_chg": "chg%",
    "volatility:sd_chg": "chg%",
    "volume:log_median_vol": "quote vol",
    "trades:log_median_trades": "trades",
    "openint:log_median_oi": "open int",
    "depth:log_median_depth_bid": "depth -1%",
    "depth:log_median_depth_ask": "depth +1%",
    "ratio:log_median_ls_acct": "L/S acct",
    "ratio:log_median_top_ls": "top L/S pos",
    "ratio:log_median_taker_ls": "taker L/S",
    "takerbuy:mean": "taker buy%", "takerbuy:sd": "taker buy%",
    "btceth:mean_btc": "BTC", "btceth:sd_btc": "BTC",
    "btceth:mean_eth": "ETH", "btceth:sd_eth": "ETH",
    "gran-close:min_step": "close",
    "wikipedia:present": "LINE:Wikipedia page views",
}


def field_of(k):
    if k in FIXED:
        return FIXED[k]
    if k.startswith("p7:"):
        return "LINE:Previous 7 days"
    if k.startswith("funding:"):
        return "LINE:Funding"
    m = re.match(r"^shape:(sd|acf1)_log_(.+)$", k)
    if m and m.group(2) in SHAPE_TAG:
        return SHAPE_TAG[m.group(2)]
    m = re.match(r"^rep-[a-z]+:(.+):(distinct|maxrepeat)$", k)
    if m:
        return m.group(1)
    return None


def load(dirpath):
    out = []
    for fn in sorted(os.listdir(dirpath)):
        if fn.endswith(".md"):
            try:
                out.append(lab_cards.parse_any_card(os.path.join(dirpath, fn)))
            except Exception as e:  # report, never hide
                print("  could not parse %s: %s" % (fn, e))
    return out


def printed_fields(c):
    cols = {re.sub(r" (x|r|dev)$", "", k) for k in c["cols"]}
    lines = {"LINE:" + k for k in c["bullets"]}
    return cols | lines


print("== (1) FORCED_FAMILIES")
for fam in A.FORCED_FAMILIES:
    print("  %-18s %s" % (fam, A.FAMILIES[fam]))
print("== REPEAT_GROUP columns: %d -> %s" % (len(A.REPEAT_GROUP),
                                              sorted(A.REPEAT_GROUP)))

removable_prefixes = sorted({p for k, v in A.FAMILIES.items()
                             if k not in A.FORCED_FAMILIES for p in v})

sets = [("raw cards/", os.path.join(REPO, "cards"))]
for v in ("rank", "ratio", "strict", "strict-flags"):
    sets.append(("blind-proof/" + v,
                 os.path.join(REPO, "exam-prep", "blind-proof", v, "cards")))

for label, d in sets:
    cards = load(d)
    print("\n== set %s: %d cards parsed" % (label, len(cards)))
    feats = [A.card_features(c) for c in cards]
    keys = sorted({k for f in feats for k in f})
    unplaced = [k for k in keys if field_of(k) is None]
    print("  (2) feature keys: %d; placed on exactly one field: %d; "
          "UNPLACED: %s" % (len(keys), len(keys) - len(unplaced),
                            unplaced or "none"))
    colsets = sorted({tuple(c["cols"].keys()) for c in cards})
    for cs in colsets:
        base = [re.sub(r" (x|r|dev)$", "", k) for k in cs]
        extra = [k for k in base if k not in A.REPEAT_GROUP]
        ranked = [k for k in cs if k.endswith(" r")]
        print("  (3) a column header printed: %d columns; not in REPEAT_GROUP:"
              " %s" % (len(cs), extra))
        print("  (4) columns with the rank suffix ' r': %d" % len(ranked))
    no_wiki = [c for c in cards if "Wikipedia page views" not in c["bullets"]]
    wk = [f.get("wikipedia:present") for c, f in zip(cards, feats)
          if "Wikipedia page views" not in c["bullets"]]
    print("  (5) cards printing no Wikipedia line: %d; on them "
          "wikipedia:present is computed on %d, distinct values %s"
          % (len(no_wiki), sum(1 for x in wk if x is not None),
             sorted(set(x for x in wk if x is not None))))
    # (6) answer "yes" as the file states it, per card set: move out every
    # feature computed from a field the card prints
    rem_keys = A.select({k: 1 for k in keys}, removable_prefixes)
    stay = []
    for k in rem_keys:
        fld = field_of(k)
        printed_on_all = all(fld in printed_fields(c) for c in cards)
        printed_on_none = all(fld not in printed_fields(c) for c in cards)
        if printed_on_all:
            continue
        stay.append((k, fld, "printed on no card" if printed_on_none
                     else "printed on some cards only"))
    print("  (6) ALL-removable keys: %d; left after moving out every feature"
          " of a printed field: %d -> %s" % (len(rem_keys), len(stay), stay))
    if stay:
        vecs, used = A.standardise(feats, [k for k, _, _ in stay])
        print("      of these, usable after standardise(): %d -> %s"
              % (len(used), used))
