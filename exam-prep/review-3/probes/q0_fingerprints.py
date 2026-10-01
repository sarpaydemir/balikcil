#!/usr/bin/env python3
"""q0 - verify every SHA-256 row of exam-prep/third-fix/FINGERPRINTS.md against the
file as found; verify the prefix claims for appended files; verify the combined
card fingerprint of the K-10 set. Input: the files named. Output: stdout (saved
beside as q0_fingerprints.out). Rule: RULES 29-30 (records verifiable). Reads only
inside the Balikcil folder (paths are relative to the repository root)."""
import hashlib, re, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
os.chdir(ROOT)
def sha(p, n=None):
    b = open(p, "rb").read()
    if n is not None: b = b[:n]
    return hashlib.sha256(b).hexdigest()
txt = open("exam-prep/third-fix/FINGERPRINTS.md").read()
ok = bad = 0
for line in txt.splitlines():
    m = re.match(r"\| `([^`]+)` \| `([0-9a-f]{64})` \|(?: `([0-9a-f]{64})` \|)?", line)
    if not m: continue
    p, h = m.group(1), m.group(2)
    if not os.path.exists(p):
        print("MISSING", p); bad += 1; continue
    got = sha(p)
    if got == h: ok += 1
    else: bad += 1; print("DIFFERS", p, "listed", h[:12], "now", got[:12])
print("rows matched", ok, "rows not matched", bad)
# prefix claims
for p, n, h in [("exam-prep/VERDICT.md",12256,"d83c2b85fe8548634193fa60d8c98e090559b7211f6066b21727a4482835fab5"),
                ("exam-prep/README.md",3605,"c704496b8234ac6d397ad50f7ea9f8d064dbc41ba5500b7d80173e9125f9d375"),
                ("exam-prep/R-04-blindness.md",21283,"64cde9b7f197143361fee1b061913304ac51814f1f9d302c852828ccbd316354"),
                ("exam-prep/N-1-collapse.md",13980,"7dee08bd1e53e0f20c2c992f784241361b5df6716fbeff1f9ee637f64727c50e"),
                ("exam-prep/decisions-and-open-questions.md",10029,"6d7f31814538b65795fc9d3afd06b90f5aa383d69af2a5b9b7619a7df6692801"),
                ("exam-prep/second-fix/SECOND-FIX.md",25076,"40cc4b7601f33b9066747e408a1e76624c15b4d34422dc41e800ffce5a3494a7")]:
    print("prefix", p, n, "equal" if sha(p, n) == h else "NOT EQUAL")
print("JQ index old copy", sha("exam-prep/third-fix/JUROR-QUESTIONS-as-of-second-fix.md") == "7020127c257b7addbae1fd6cbca0e4031accc3b28a4816980c5cd410532399d9")
# combined card fingerprint
d = "exam-prep/third-fix/blind-proof/strict-flags-unrounded/cards"
names = sorted(os.listdir(d))
s = "".join(f"{os.path.splitext(n)[0]}:{sha(os.path.join(d,n))}\n" for n in names)
print("K-10 cards", len(names), "combined", hashlib.sha256(s.encode()).hexdigest())
# REVIEW-2 own file and review-2 fingerprints untouched
for p in ["exam-prep/REVIEW-2.md","exam-prep/REVIEW.md","exam-prep/review-2/FINGERPRINTS.md"]:
    print(p, sha(p))
