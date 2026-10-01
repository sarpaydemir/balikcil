#!/usr/bin/env python3
"""q1 - review-3 probe (N-1, JQ-N1 part 2).
(A) Do the engine's greedy-clique (windows anchored at moment starts, ties by
    anchor start then id of the first kept member) and a literal reading of
    JQ-N1 part 2's wording (every clock hour is a candidate; the hour covered by
    the most (coins/moments); ties to the earliest hour, then the lowest card
    number) give the same partition? On the observation moments and on random
    moment sets, under scope any and cross-coin, keeping the EARLIEST moment of
    a coin (what the engine does).
(B) The same for keeping the LATEST: the third run's G-5 loop (engine loop,
    one choice reversed) against the literal reading. For every event G-5
    forms, is its chosen window the earliest hour with the largest coverage?
Input: cards/ (via scripts/15_event_collapse.py's reader). Output: stdout,
saved as q1_greedy_latest.out. Seed for the random sets: 20260913 (TACTICS 1),
200 sets each; the count is a diagnostic of my own, not a rule. No threshold.
"""
import os, sys, random, importlib.util, datetime as dt
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
def load(name, file):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, "scripts", file))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
ec = load("ec", "15_event_collapse.py")
g26 = load("g26", "26_third_fix_checks.py")
import lab_cards

def literal(ms, gap, cross, keep):
    """JQ-N1 part 2 read word for word. Hours are integers (start hour index)."""
    left = sorted(ms, key=lambda m: (m["h"], m["id"]))
    events = []
    while left:
        best = None
        # Coverage only changes where a window opens (a start hour) or closes; a
        # closing never raises the count, and ties go to the earlier hour, so the
        # earliest hour with the largest coverage is always some start hour.
        for H in sorted({m["h"] for m in left}):
            cov = [m for m in left if m["h"] <= H <= m["h"] + gap]
            if not cov: continue
            if cross:
                seq = cov if keep == "earliest" else list(reversed(cov))
                seen, kept = set(), []
                for m in seq:
                    if m["coin"] in seen: continue
                    seen.add(m["coin"]); kept.append(m)
                cov = kept
            key = (-len(cov), H, min(m["id"] for m in cov))
            if best is None or key < best[0]:
                best = (key, cov)
        ids = {m["id"] for m in best[1]}
        events.append(tuple(sorted(ids)))
        left = [m for m in left if m["id"] not in ids]
    return sorted(events)

def to_engine(ms):
    t0 = dt.datetime(2025, 1, 1)
    return [{"id": m["id"], "coin": m["coin"], "start_dt": t0 + dt.timedelta(hours=m["h"])} for m in ms]

def engine(ms, gap_name, scope):
    return sorted(tuple(e) for e in ec.collapse(to_engine(ms), gap_name, "greedy-clique", scope))

def g5(ms, gap, keep):
    return sorted(tuple(e) for e in g26.greedy_cross_coin(to_engine(ms), gap, keep))

cards = lab_cards.load_all(os.path.join(ROOT, "cards"))
t0 = min(ec.parse_hour(c["start_hour_utc"]) for c in cards)
obs = [{"id": c["card"], "coin": c["coin"],
        "h": int((ec.parse_hour(c["start_hour_utc"]) - t0).total_seconds() // 3600)} for c in cards]

print("== (A) observation moments, keep earliest: engine vs literal")
for d in ("move-window", "card-span"):
    gap = ec.DEFINITIONS[d]
    for scope in ("any", "cross-coin"):
        a = engine(obs, d, scope); b = literal(obs, gap, scope == "cross-coin", "earliest")
        print(d, scope, "engine", len(a), "literal", len(b), "events in one only", len(set(a) ^ set(b)))

print("== (B) observation moments, keep latest: G-5 loop vs literal")
for d in ("move-window", "card-span"):
    gap = ec.DEFINITIONS[d]
    a = g5(obs, gap, "latest"); b = literal(obs, gap, True, "latest")
    e = g5(obs, gap, "earliest")
    print(d, "G-5 latest", len(a), "literal latest", len(b), "events in one only", len(set(a) ^ set(b)),
          "| G-5 latest vs earliest in one only", len(set(a) ^ set(e)),
          "| literal latest vs earliest in one only", len(set(b) ^ set(e)))

print("== (B2) card-span, keep latest: events in one partition only (id, coin, start hour index)")
gap = ec.DEFINITIONS["card-span"]
a = g5(obs, gap, "latest"); b = literal(obs, gap, True, "latest")
byid = {m["id"]: m for m in obs}
only_a = sorted(set(a) - set(b)); only_b = sorted(set(b) - set(a))
for e in only_a[:3]:
    print("G-5 only:", [(i, byid[i]["coin"][:4], byid[i]["h"]) for i in e])
for e in only_b[:3]:
    print("literal only:", [(i, byid[i]["coin"][:4], byid[i]["h"]) for i in e])

print("== (C) random moment sets, keep earliest: engine vs literal (200 sets x 2 definitions x 2 scopes)")
rng = random.Random(20260913)
diff = {}
for t in range(200):
    n = rng.randint(5, 25); coins = ["X", "Y", "Z", "W"][:rng.randint(2, 4)]
    ms = [{"id": "C%03d" % i, "coin": rng.choice(coins), "h": rng.randint(0, 150)} for i in range(n)]
    for d in ("move-window", "card-span"):
        gap = ec.DEFINITIONS[d]
        for scope in ("any", "cross-coin"):
            a = engine(ms, d, scope); b = literal(ms, gap, scope == "cross-coin", "earliest")
            k = (d, scope); diff.setdefault(k, 0)
            if a != b: diff[k] += 1
for k, v in sorted(diff.items()):
    print(k, "sets where engine != literal:", v, "of 200")
print("== (D) random moment sets, keep latest: G-5 vs literal")
rng = random.Random(20260913); dl = {}
for t in range(200):
    n = rng.randint(5, 25); coins = ["X", "Y", "Z", "W"][:rng.randint(2, 4)]
    ms = [{"id": "C%03d" % i, "coin": rng.choice(coins), "h": rng.randint(0, 150)} for i in range(n)]
    for d in ("move-window", "card-span"):
        gap = ec.DEFINITIONS[d]
        a = g5(ms, gap, "latest"); b = literal(ms, gap, True, "latest")
        dl.setdefault(d, 0)
        if a != b: dl[d] += 1
for k, v in sorted(dl.items()):
    print(k, "sets where G-5 latest != literal latest:", v, "of 200")
