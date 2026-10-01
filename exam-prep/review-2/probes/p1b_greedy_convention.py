#!/usr/bin/env python3
"""
p1b_greedy_convention.py -- review-2 probe (N-1, JQ-N1 parts 2-3).
Does the per-coin choice that greedy-clique + cross-coin makes, and that JQ-N1
does not state, change the events? Same literal greedy as p1, but when two
moments of one coin cover the chosen hour the LATEST (start, id) is kept
instead of the earliest. Counts only; no threshold.
Input cards/ (via p1's reader). Output stdout (saved as p1b.out).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import p1_collapse_independent as p
ms = p.read_cards(); by = {m['id']: m for m in ms}
def greedy_latest(ms, definition):
    lo_off, hi_off = p.COVER[definition]
    left = sorted(ms, key=lambda m: (m['h'], m['id'])); events = []
    while left:
        best = None
        for H in range(min(m['h'] for m in left) + lo_off, max(m['h'] for m in left) + hi_off + 1):
            cov = [m for m in left if m['h'] + lo_off <= H <= m['h'] + hi_off]
            seen, keep = set(), []
            for m in reversed(cov):
                if m['coin'] not in seen:
                    seen.add(m['coin']); keep.append(m)
            if not keep:
                continue
            key = (-len(keep), H, min(m['id'] for m in keep))
            if best is None or key < best[0]:
                best = (key, keep)
        ids = {m['id'] for m in best[1]}; events.append(sorted(ids))
        left = [m for m in left if m['id'] not in ids]
    return sorted(events)
for d in ('move-window', 'card-span'):
    a = p.greedy_literal(ms, d, True); b = greedy_latest(ms, d)
    sa = {tuple(e) for e in a}; sb = {tuple(e) for e in b}
    print('p1b %s/greedy-clique/cross-coin: events earliest-rule %d, latest-rule %d, events not shared by both %d; table row earliest %s; latest %s'
          % (d, len(a), len(b), len(sa ^ sb), p.table_row(a, by)['both_kinds'], p.table_row(b, by)['both_kinds']))
