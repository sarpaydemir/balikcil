#!/usr/bin/env python3
"""p3 · review-4 · a third literal implementation of JQ-N1 part 2's
greedy-clique wording under scope cross-coin, written from the juror file's
words alone (lines 120-133), for "earliest" and "latest", at move-window
(a moment covers its start hour and the 23 after it) and card-span (the 24
before the start and the 23 after it: 48 hours). Every clock hour is a
candidate in every round (scanned at window edges; see the comment in literal()). Compares with the engine's events.csv (earliest)
and prints, for both conventions, the JQ-N1 columns plus the block-immovable
counts (an event whose size no other event shares), and the number of events
in one partition only (counted over both partitions).
Moments: card id, coin and start hour read from each raw card's header;
kind read from the engine's events.csv `none/none/none` rows (kind is not on
the card), and cross-checked that coin and start hour agree.
Reads: cards/C*.md, exam-prep/review-4/rerun/collapse/run-a0ecf6970d86b199/events.csv
Writes nothing (prints)."""
import csv, datetime as dt, os, re
from collections import Counter, defaultdict
ROOT = "/home/user/balikcil"
EV = os.path.join(ROOT, "exam-prep/review-4/rerun/collapse/run-a0ecf6970d86b199/events.csv")
rows = list(csv.DictReader(open(EV)))
kind = {}; chk = {}
for r in rows:
    if r["config"] == "none/none/none":
        kind[r["card"]] = r["kind"]; chk[r["card"]] = (r["coin"], r["start_hour_utc"])
EPOCH = dt.datetime(2020, 1, 1, tzinfo=dt.timezone.utc)
moments = []
for f in sorted(os.listdir(os.path.join(ROOT, "cards"))):
    if not re.match(r"C\d+\.md$", f):
        continue
    txt = open(os.path.join(ROOT, "cards", f), encoding="utf-8").read()
    cid = f[:-3]
    coin = re.search(r"\| coin \| `([^`]+)` \|", txt).group(1)
    sh = re.search(r"\| start hour \(UTC\) \| (\d{4}-\d\d-\d\d \d\d:\d\d) \|", txt).group(1)
    t = dt.datetime.strptime(sh, "%Y-%m-%d %H:%M").replace(tzinfo=dt.timezone.utc)
    h = int((t - EPOCH).total_seconds() // 3600)
    iso = t.strftime("%Y-%m-%dT%H:%MZ")
    assert chk[cid] == (coin, iso), (cid, chk[cid], coin, iso)
    moments.append((cid, coin, h, kind[cid]))
assert len(moments) == 306
def cardnum(cid):
    return int(cid[1:])
def literal(defn, keep):
    lo, hi = (0, 23) if defn == "move-window" else (-24, 23)
    un = {m[0]: m for m in moments}
    events = []
    while un:
        # Coverage is constant between window edges and only rises at a
        # window's first hour, so the earliest hour of largest coverage is
        # always some unassigned moment's first covered hour; scanning those
        # in increasing order is the same as scanning every clock hour.
        best = None
        for H in sorted({m[2] + lo for m in un.values()}):
            cov = {m[1] for m in un.values() if m[2] + lo <= H <= m[2] + hi}
            if best is None or len(cov) > best[0]:
                best = (len(cov), H)
        H = best[1]
        bycoin = defaultdict(list)
        for m in un.values():
            if m[2] + lo <= H <= m[2] + hi:
                bycoin[m[1]].append(m)
        ev = []
        for c, ms in bycoin.items():
            if keep == "earliest":
                pick = min(ms, key=lambda m: (m[2], cardnum(m[0])))
            else:
                pick = max(ms, key=lambda m: (m[2], cardnum(m[0])))
            ev.append(pick)
        for m in ev:
            del un[m[0]]
        events.append(frozenset(m[0] for m in ev))
    return events
info = {m[0]: m for m in moments}
def stats(evs):
    sizes = Counter(len(e) for e in evs)
    mixed = sum(1 for e in evs if {info[c][3] for c in e} >= {"large", "calm"})
    samecoin = sum(1 for e in evs if max(Counter(info[c][1] for c in e).values()) >= 2)
    lsc = max(max(Counter(info[c][1] for c in e).values()) for e in evs)
    imm = [e for e in evs if sizes[len(e)] == 1]
    return dict(events=len(evs), singles=sizes[1], largest=max(sizes), mixed=mixed,
                samecoin=samecoin, largest_same_coin=lsc, immovable_events=len(imm),
                immovable_cards=sum(len(e) for e in imm))
eng = defaultdict(lambda: defaultdict(set))
for r in rows:
    eng[r["config"]][r["event_id"]].add(r["card"])
for defn in ("move-window", "card-span"):
    E = literal(defn, "earliest"); L = literal(defn, "latest")
    cfg = "%s/greedy-clique/cross-coin" % defn
    engE = {frozenset(s) for s in eng[cfg].values()}
    print(defn, "earliest literal == engine earliest:", set(E) == engE)
    print(defn, "earliest", stats(E))
    print(defn, "latest  ", stats(L))
    print(defn, "events in one partition only:", len(set(E) ^ set(L)))
