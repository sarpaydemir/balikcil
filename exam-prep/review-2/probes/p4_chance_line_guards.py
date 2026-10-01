#!/usr/bin/env python3
"""
p4_chance_line_guards.py -- review-2 probe (N-1, REVIEW §4.3 / §4.5 item 4).

What it does
  Tries to obtain an un-collapsed (card-level) chance line from
  scripts/15_event_collapse.py's chance_line() while the record claims a
  collapsed configuration, by routes the second-fix run's E-2 table does not
  list:
    1. collapse() fed moments whose start hours are moved apart (forged
       moments), labelled card-span/component/any;
    2. an EventMap built directly with the class constructor;
    3. mutating an accepted EventMap's `.moments` after construction;
    4. a subclass of EventMap.
  For each: accepted or refused, and what the returned record shows
  (config, identity_partition, moments_sha256 against the true moments').
Input   cards/ via lab_cards ; scripts/15_event_collapse.py (imported)
Output  stdout
Seed    20260913 for the synthetic answer vector (the instruments' seed).
"""
import os, sys, random, importlib.util, datetime as dt

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(REPO, "scripts"))
import lab_cards  # noqa
spec = importlib.util.spec_from_file_location(
    "ec", os.path.join(REPO, "scripts", "15_event_collapse.py"))
ec = importlib.util.module_from_spec(spec); spec.loader.exec_module(ec)

cards = lab_cards.load_all(os.path.join(REPO, "cards"))
ms = [{"id": c["card"], "coin": c["coin"], "kind": c["kind"],
       "start_dt": ec.parse_hour(c["start_hour_utc"])} for c in cards]
ids = sorted(m["id"] for m in ms)
labels = [1 if {m["id"]: m for m in ms}[i]["kind"] == "large" else 0 for i in ids]
rng = random.Random(ec.SEED)
answers = [rng.randint(0, 1) for _ in ids]
true_map = ec.collapse(ms, "card-span", "component", "any")
true_msha = true_map.moments_sha256()
ident = ec.chance_line(answers, labels, ec.identity_map(ms), ids, "block")
print("reference: identity_map block boundary %.6f ; true card-span/component/any "
      "events %d, moments_sha256 %s" % (ident["boundary"], len(true_map), true_msha[:16]))

def show(name, fn):
    try:
        r = fn()
        print("%-60s ACCEPTED config=%s events=%d identity_partition=%s "
              "boundary=%.6f moments_sha256_matches_true=%s"
              % (name, r["config"], r["events"], r["identity_partition"],
                 r["boundary"], r["moments_sha256"] == true_msha))
    except Exception as e:
        print("%-60s REFUSED %s: %s" % (name, type(e).__name__, e))

# 1. forged moments: every start hour pushed 1000 h apart, coins kept
forged = [dict(m, start_dt=dt.datetime(2020, 1, 1, tzinfo=dt.timezone.utc)
               + dt.timedelta(hours=1000 * k)) for k, m in enumerate(
                   sorted(ms, key=lambda m: m["id"]))]
fm = ec.collapse(forged, "card-span", "component", "any")
show("1 forged start hours, collapse(card-span/component/any)",
     lambda: ec.chance_line(answers, labels, fm, ids, "block"))
# 1b. forged: only one card's hour moved (a partial forgery)
f2 = [dict(m) for m in ms]
f2[0]["start_dt"] = f2[0]["start_dt"] + dt.timedelta(hours=5000)
fm2 = ec.collapse(f2, "card-span", "component", "any")
show("1b one card's start hour moved, collapse(card-span/...)",
     lambda: ec.chance_line(answers, labels, fm2, ids, "block"))
# 2. constructor, identity events, collapsed label
show("2 EventMap(identity events, 'card-span','component','any', true moments)",
     lambda: ec.chance_line(answers, labels, ec.EventMap(
         [[i] for i in ids], "card-span", "component", "any", ms), ids, "block"))
# 3. mutate .moments after building a legitimate map
def mut():
    m = ec.collapse(forged, "card-span", "component", "any")
    return ec.chance_line(answers, labels, m, ids, "block")
show("3 (same as 1, built then passed)", mut)
# 4. subclass that lies about its config
class Lying(ec.EventMap):
    pass
def sub():
    m = Lying([[i] for i in ids], "none", "none", "none", ms)
    m.config = "card-span/component/any"
    return ec.chance_line(answers, labels, m, ids, "block")
show("4 subclass, identity events, .config overwritten after construction", sub)
