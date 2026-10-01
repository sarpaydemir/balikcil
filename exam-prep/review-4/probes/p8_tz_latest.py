#!/usr/bin/env python3
"""p8 · review-4 · does the engine's "latest" path (or the default path)
depend on the machine's time zone? Runs collapse() on the observation
moments (read from the raw card headers, start hours as aware UTC datetimes)
for both greedy cross-coin configurations, earliest and latest, and prints
the event-map fingerprints. Run it under several TZ settings and compare.
Reads cards/C*.md and scripts/15_event_collapse.py. Writes nothing."""
import datetime as dt, importlib.util, os, re, sys, time
ROOT = "/home/user/balikcil"
sys.path.insert(0, os.path.join(ROOT, "scripts"))
spec = importlib.util.spec_from_file_location("e15", os.path.join(ROOT, "scripts/15_event_collapse.py"))
e = importlib.util.module_from_spec(spec); spec.loader.exec_module(e)
ms = []
for f in sorted(os.listdir(os.path.join(ROOT, "cards"))):
    if not re.match(r"C\d+\.md$", f):
        continue
    t = open(os.path.join(ROOT, "cards", f), encoding="utf-8").read()
    coin = re.search(r"\| coin \| `([^`]+)` \|", t).group(1)
    sh = re.search(r"\| start hour \(UTC\) \| (\d{4}-\d\d-\d\d \d\d:\d\d) \|", t).group(1)
    ms.append({"id": f[:-3], "coin": coin, "start_dt": e.parse_hour(sh.replace(" ", "T"))})
out = []
for d in ("move-window", "card-span"):
    for k in ("earliest", "latest"):
        em = e.collapse(ms, d, "greedy-clique", "cross-coin", same_coin_keep=k)
        out.append("%s/%s %d %s" % (d, k, len(em), e.event_map_fingerprint(em)[:16]))
print("TZ=%s" % os.environ.get("TZ"), time.tzname, "|", " | ".join(out))
