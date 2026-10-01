#!/usr/bin/env python3
"""q4 - review-3 probe (N-1, REVIEW-2 condition 2, HANDED-FORWARD B-2).
Attempts against chance_line()'s key check that the third run's G-1 did not try.
The key is always the fingerprint of the TRUE observation moments.
  1 one card's coin changed (hours unchanged)
  2 an extra moment added to the map's moments
  3 forged moments (one card's hour moved), the map's moments_sha256 replaced
    on the instance by a function returning the true key
  4 the same with a subclass overriding moments_sha256()
  5 forged moments, map built by collapse(), the attribute .moments of the map
    then overwritten with the true moments tuple
Input cards/ (via the engine's reader). Output stdout (saved beside as .out).
Synthetic answers: all "large" (only acceptance or refusal is read here).
"""
import os, sys, importlib.util, datetime as dt
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
spec = importlib.util.spec_from_file_location("ec", os.path.join(ROOT, "scripts", "15_event_collapse.py"))
ec = importlib.util.module_from_spec(spec); spec.loader.exec_module(ec)
import lab_cards
cards = lab_cards.load_all(os.path.join(ROOT, "cards"))
ms = [{"id": c["card"], "coin": c["coin"], "kind": c["kind"], "start_dt": ec.parse_hour(c["start_hour_utc"])} for c in cards]
ids = sorted(m["id"] for m in ms)
labels = [next(m["kind"] for m in ms if m["id"] == i) for i in ids]
answers = ["large"] * len(ids)
key = ec.moments_fingerprint(ms)
CFG = ("card-span", "component", "any")
def attempt(name, fn):
    try:
        r = fn()
        print("%-60s ACCEPTED  events %d boundary %.6f key_check %s" % (name, r["events"], r["boundary"], r["key_check"]))
    except Exception as e:
        print("%-60s refused   %s: %s" % (name, type(e).__name__, str(e)[:90]))
attempt("0 true map, true key", lambda: ec.chance_line(answers, labels, ec.collapse(ms, *CFG), ids, "block", key_moments_sha256=key))
m1 = [dict(m) for m in ms]; m1[0]["coin"] = "XUSDT"
attempt("1 one coin changed, true key", lambda: ec.chance_line(answers, labels, ec.collapse(m1, *CFG), ids, "block", key_moments_sha256=key))
m2 = [dict(m) for m in ms] + [{"id": "C999", "coin": "XUSDT", "kind": "calm", "start_dt": ms[0]["start_dt"]}]
attempt("2 extra moment, true key", lambda: ec.chance_line(answers, labels, ec.collapse(m2, *CFG), ids, "block", key_moments_sha256=key))
m3 = [dict(m) for m in ms]; m3[5]["start_dt"] = m3[5]["start_dt"] + dt.timedelta(hours=2000)
em3 = ec.collapse(m3, *CFG); em3.moments_sha256 = lambda: key
attempt("3 forged hour, instance method patched to return true key", lambda: ec.chance_line(answers, labels, em3, ids, "block", key_moments_sha256=key))
class EM(ec.EventMap):
    def moments_sha256(self): return key
src = ec.collapse(m3, *CFG)
em4 = EM(list(src), src.definition, src.resolution, src.scope, m3)
attempt("4 forged hour, subclass overriding moments_sha256()", lambda: ec.chance_line(answers, labels, em4, ids, "block", key_moments_sha256=key))
em5 = ec.collapse(m3, *CFG); em5.moments = ec.collapse(ms, *CFG).moments
attempt("5 forged hour, .moments overwritten with the true tuple", lambda: ec.chance_line(answers, labels, em5, ids, "block", key_moments_sha256=key))
print("true map events", len(ec.collapse(ms, *CFG)), "forged map events", len(ec.collapse(m3, *CFG)))
