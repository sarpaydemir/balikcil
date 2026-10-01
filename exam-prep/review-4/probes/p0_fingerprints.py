#!/usr/bin/env python3
"""p0 · review-4 · check every SHA-256 row of exam-prep/fourth-fix/FINGERPRINTS.md
against the file on disk, the stated prefixes of appended files, and list
files under exam-prep/ and scripts/ modified after the fourth run's first
clock read (2026-10-01T21:22:37Z) that the fingerprints do not list.
Reads only inside the Balikcil folder. Writes nothing (prints)."""
import hashlib, os, re, sys, datetime
ROOT = "/home/user/balikcil"
os.chdir(ROOT)
def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()
fp = open("exam-prep/fourth-fix/FINGERPRINTS.md").read()
rows = re.findall(r"^\| `([^`]+)` \| `([0-9a-f]{64})` \|$", fp, re.M)
bad = 0
for f, h in rows:
    if not os.path.exists(f):
        print("MISSING", f); bad += 1; continue
    a = sha(f)
    if a != h:
        print("DIFFERS", f, h[:12], "now", a[:12]); bad += 1
print("rows", len(rows), "differing/missing", bad)
# appended-file prefixes vs review-3 fingerprints
r3 = open("exam-prep/review-3/FINGERPRINTS.md").read()
r3rows = dict((f, h) for f, h in re.findall(r"`([^`]+)` \| `([0-9a-f]{64})`", r3))
pref = {"exam-prep/HANDED-FORWARD.md": 7206, "exam-prep/VERDICT.md": 19176,
        "exam-prep/README.md": 4375, "exam-prep/R-04-blindness.md": 21926,
        "exam-prep/N-1-collapse.md": 14545,
        "exam-prep/third-fix/THIRD-FIX.md": 37391}
for f, n in pref.items():
    b = open(f, "rb").read()[:n]
    h = hashlib.sha256(b).hexdigest()
    print("prefix", f, n, "matches review-3 record" if r3rows.get(f) == h
          else "NO MATCH (review-3 has %s)" % (r3rows.get(f, "none")[:12]), h[:12])
# files modified after the first clock read of the fourth run
t0 = datetime.datetime(2026, 10, 1, 21, 22, 37, tzinfo=datetime.timezone.utc).timestamp()
listed = set(f for f, _ in rows)
for top in ("exam-prep", "scripts"):
    for dp, dn, fn in os.walk(top):
        if "review-4" in dp:
            continue
        for x in fn:
            p = os.path.join(dp, x)
            if os.path.getmtime(p) > t0 and p not in listed:
                print("modified after 21:22:37Z, not listed:", p,
                      datetime.datetime.fromtimestamp(os.path.getmtime(p), datetime.timezone.utc).isoformat())
