#!/usr/bin/env python3
"""
p1_collapse_independent.py -- review-2 probe (N-1).

What it does
  1. Reads coin, start hour and moment kind straight out of the 306 raw card
     texts with its own regexes (no lab_cards, no 15_event_collapse code).
  2. Builds every configuration of JQ-N1 with its own code:
       component     -- own union-find on |start gap| <= 0 / 23 / 47 h
       greedy-clique -- implemented LITERALLY from the JQ-N1 part 2 wording:
                        "repeatedly take the clock hour covered by the most
                        still-unassigned moments ... ties go to the earliest
                        hour, then the lowest card number", hours covered being
                        [s, s+23] (move-window) or [s-24, s+23] (card-span).
                        Under cross-coin, at most one moment per coin joins an
                        event; which one is NOT stated in JQ-N1, so this probe
                        takes the earliest (start, id) -- the convention found
                        in 15_event_collapse.py -- and says so.
  3. Compares each partition with the second-fix events.csv
     (exam-prep/collapse/run-756cf4ea156d92c3/events.csv) and recomputes every
     column of the JQ-N1 table and the immovable-event counts.
  4. Tests the repaired block_shuffle_indices() with its own checker on all
     configurations and on a constructed example where same-size events exist.
Input   cards/C###.md ; exam-prep/collapse/run-756cf4ea156d92c3/events.csv ;
        scripts/15_event_collapse.py (only block_shuffle_indices is imported)
Output  stdout (captured to exam-prep/review-2/probes/p1.out by the caller)
Rules   RULES 13 (the readings), RULES 12 (draw count 1000 = SHUFFLES, seed
        20260913 = TACTICS 1 draw number). No threshold is defined here.
"""
import csv, glob, os, re, random, datetime as dt, importlib.util
from collections import Counter, defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
SEED = 20260913          # TACTICS 1 draw number (as used by the instruments)
DRAWS = 1000             # RULES 12 shuffle count
GAPS = {"start-hour": 0, "move-window": 23, "card-span": 47}
COVER = {"move-window": (0, 23), "card-span": (-24, 23)}

def read_cards():
    out = []
    for p in sorted(glob.glob(os.path.join(REPO, "cards", "C*.md"))):
        t = open(p, encoding="utf-8").read()
        cid = os.path.basename(p)[:-3]
        coin = re.search(r"^\| coin \| `([A-Z0-9]+)` \|", t, re.M).group(1)
        sh = re.search(r"^\| start hour \(UTC\) \| (\d{4}-\d\d-\d\d \d\d:\d\d) \|",
                       t, re.M).group(1)
        kind = re.search(r"^- \*\*Moment kind:\*\* (\w+)", t, re.M).group(1)
        s = dt.datetime.strptime(sh, "%Y-%m-%d %H:%M")
        out.append({"id": cid, "coin": coin, "kind": kind,
                    "h": int(s.timestamp() // 3600)})
    return out

def component(ms, gap, cross):
    par = {m["id"]: m["id"] for m in ms}
    def f(x):
        while par[x] != x:
            x = par[x]
        return x
    for a in ms:
        for b in ms:
            if a["id"] < b["id"] and abs(a["h"] - b["h"]) <= gap:
                if cross and a["coin"] == b["coin"]:
                    continue
                ra, rb = f(a["id"]), f(b["id"])
                if ra != rb:
                    par[max(ra, rb)] = min(ra, rb)
    g = defaultdict(list)
    for m in ms:
        g[f(m["id"])].append(m["id"])
    return sorted(sorted(v) for v in g.values())

def greedy_literal(ms, definition, cross):
    lo_off, hi_off = COVER[definition]
    left = sorted(ms, key=lambda m: (m["h"], m["id"]))
    events = []
    while left:
        hmin = min(m["h"] for m in left) + lo_off
        hmax = max(m["h"] for m in left) + hi_off
        best = None
        for H in range(hmin, hmax + 1):
            cov = [m for m in left if m["h"] + lo_off <= H <= m["h"] + hi_off]
            if cross:
                seen, keep = set(), []
                for m in cov:                      # earliest (start, id) first
                    if m["coin"] not in seen:
                        seen.add(m["coin"]); keep.append(m)
                cov = keep
            if not cov:
                continue
            key = (-len(cov), H, min(m["id"] for m in cov))
            if best is None or key < best[0]:
                best = (key, cov)
        ids = {m["id"] for m in best[1]}
        events.append(sorted(ids))
        left = [m for m in left if m["id"] not in ids]
    return sorted(events)

def table_row(events, by):
    sizes = Counter(len(e) for e in events)
    same = [max(Counter(by[c]["coin"] for c in e).values()) for e in events]
    return {"events": len(events), "size1": sizes.get(1, 0),
            "largest": max(len(e) for e in events),
            "both_kinds": sum(1 for e in events
                              if len({by[c]["kind"] for c in e}) > 1),
            "same_coin_events": sum(1 for x in same if x >= 2),
            "largest_same_coin": max(same),
            "immovable_events": sum(1 for e in events if sizes[len(e)] == 1),
            "immovable_cards": sum(len(e) for e in events if sizes[len(e)] == 1),
            "size_hist": dict(sorted(sizes.items()))}

def main():
    ms = read_cards()
    by = {m["id"]: m for m in ms}
    print("cards read:", len(ms), " kinds:", dict(Counter(m["kind"] for m in ms)))
    ev = defaultdict(lambda: defaultdict(list))
    with open(os.path.join(REPO, "exam-prep/collapse/run-756cf4ea156d92c3/events.csv")) as fh:
        for r in csv.DictReader(fh):
            ev[r["config"]][r["event_id"]].append(r["card"])
    theirs = {cfg: sorted(sorted(v) for v in d.values()) for cfg, d in ev.items()}
    mine = {"none/none/none": sorted([m["id"]] for m in ms)}
    for d in GAPS:
        for res in (["component"] if d == "start-hour" else ["component", "greedy-clique"]):
            for sc in ("any", "cross-coin"):
                cfg = "%s/%s/%s" % (d, res, sc)
                if res == "component":
                    mine[cfg] = component(ms, GAPS[d], sc == "cross-coin")
                else:
                    mine[cfg] = greedy_literal(ms, d, sc == "cross-coin")
    print("\n## partitions: own code vs second-fix events.csv")
    for cfg in sorted(mine):
        print("%-40s identical=%s" % (cfg, mine[cfg] == theirs.get(cfg)))
    print("\n## JQ-N1 table columns, own code")
    for cfg in sorted(mine):
        print(cfg, table_row(mine[cfg], by))

    # ---- block shuffle, repaired version, own checker -------------------
    spec = importlib.util.spec_from_file_location(
        "ec", os.path.join(REPO, "scripts", "15_event_collapse.py"))
    ec = importlib.util.module_from_spec(spec); spec.loader.exec_module(ec)
    def own_check(events, id_order, draws, seed):
        pos = {c: i for i, c in enumerate(id_order)}
        owner = {pos[c]: k for k, e in enumerate(events) for c in e}
        rng = random.Random(seed)
        moved = 0
        for _ in range(draws):
            idx = ec.block_shuffle_indices(events, id_order, rng)
            assert sorted(idx) == list(range(len(id_order))), "not a permutation"
            for k, e in enumerate(events):
                src = {owner[idx[pos[c]]] for c in e}
                assert len(src) == 1, "multi-source event"
                s = src.pop()
                assert len(events[s]) == len(e), "size mismatch"
                if s != k:
                    moved += 1
        return moved
    print("\n## block shuffle (repaired) -- own checker, %d draws, seed %d" % (DRAWS, SEED))
    for cfg in sorted(mine):
        ids = sorted(by)
        moved = own_check(mine[cfg], ids, DRAWS, SEED)
        print("%-40s passed; event-moves over all draws: %d" % (cfg, moved))
    # constructed example in which same-size events exist, so the shuffle
    # must actually move them (the review's example cannot move anything)
    ex = [["a0", "a1", "a2"], ["b0", "b1", "b2"], ["c0"], ["d0"], ["e0", "e1"],
          ["f0", "f1"]]
    ids = sorted(c for e in ex for c in e)
    moved = own_check(ex, ids, DRAWS, SEED)
    print("constructed example (sizes 3,3,1,1,2,2): passed; event-moves:", moved,
          "of", DRAWS * len(ex), "event-draws")

if __name__ == "__main__":
    main()
