#!/usr/bin/env python3
"""p5 · review-4 · compare every output of exam-prep/review-4/rerun/ with
the fourth-fix run's output of the same run number. CSVs must be
byte-identical. Markdown reports and JSON records: every differing line is
printed, so that a reader can see that only clock, disk and output-path
lines differ. Reads only inside the Balikcil folder; writes nothing."""
import filecmp, hashlib, os, difflib
ROOT = "/home/user/balikcil"
pairs = [("exam-prep/review-4/rerun/collapse", "exam-prep/fourth-fix/collapse"),
         ("exam-prep/review-4/rerun/identity", "exam-prep/fourth-fix/identity"),
         ("exam-prep/review-4/rerun/checks", "exam-prep/fourth-fix/checks")]
for mine, theirs in pairs:
    m = os.path.join(ROOT, mine); t = os.path.join(ROOT, theirs)
    if not os.path.isdir(m):
        print("MISSING rerun folder", mine); continue
    for dp, dn, fn in os.walk(m):
        for f in sorted(fn):
            pm = os.path.join(dp, f); rel = os.path.relpath(pm, m); pt = os.path.join(t, rel)
            if not os.path.exists(pt):
                print("NO COUNTERPART", os.path.join(mine, rel)); continue
            a = open(pm, "rb").read(); b = open(pt, "rb").read()
            if a == b:
                print("identical  ", os.path.join(theirs, rel)); continue
            if f.endswith(".csv") or f.endswith(".sha256"):
                print("CSV/SHA DIFFERS", os.path.join(theirs, rel)); continue
            la = a.decode().splitlines(); lb = b.decode().splitlines()
            d = [x for x in difflib.unified_diff(lb, la, lineterm="", n=0) if not x.startswith(("---", "+++", "@@"))]
            print("differs    ", os.path.join(theirs, rel), "(%d changed lines)" % len(d))
            for x in d:
                print("      ", x[:220])
