#!/usr/bin/env python3
"""Review 8, probe p7 -- could a juror-facing file identify a coin, a date or
a price?

The exam draw (exam/draw/) is closed to this review, so the exam coins
cannot be named here. Instead every file is scanned against the WHOLE
universe the draw was made from (data/universe/universe.csv, 795 symbols;
the exam coins are a subset of it) and against the 10 observation coins
(data/draw/observation-coins.txt).

**No matched word is written anywhere.** Each hit is written as the first
12 hex digits of SHA-256(token), with file, line, column and category, so
that a reader with the file can find it and a reader without it learns
nothing.

Categories:
  SYM-FULL   a universe symbol, whole token, any case
  SYM-BASE   a universe symbol's base asset (quote currency and a leading
             1000…/1M multiplier stripped), whole token, exact upper case,
             length >= 2
  SYM-WORD   the same base asset, whole word, any case, length >= 4
  OBS        an observation coin's symbol or base, whole token, any case
  DATE       YYYY-MM-DD, or a month or weekday name; tagged "provenance"
             when its line carries "system clock" or a run/author marker
  TIME       hh:mm
  PRICE      a number with a currency sign, or with three or more decimals
Input: the files listed in FILES (juror-facing: every file in the index's
"files a juror needs" column, the canteen book by its named line ranges
only, the verdict files the eighth-fix d file cites as sources), plus the
index itself, scanned separately. Output: stdout (caller redirects to
p7_identity_scan.out). No randomness.
"""
import csv
import hashlib
import os
import re
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = HERE.rsplit(os.sep + "exam-prep" + os.sep, 1)[0]
assert os.path.isfile(os.path.join(REPO, "RULES.md"))

CANTEEN = "canteen/2026-09-19-sofia.md"
CANTEEN_RANGES = [(112, 120), (221, 225), (245, 246), (268, 270),
                  (667, 671)]  # index rows JQ-R04-DATE-a ... CONTENT-c
FILES = [
    ("juror", "exam-prep/eighth-fix/juror-questions/JQ-R04-CONTENT-d.md"),
    ("juror", "RULES.md"),
    ("juror", "TACTICS.md"),
    ("juror", "exam-prep/fifth-fix/juror-questions/JQ-N1.md"),
    ("juror", "exam-prep/fifth-fix/juror-questions/JQ-CANTEEN-8.md"),
    ("juror", "exam-prep/third-fix/juror-questions/JQ-R04-GATE.md"),
    ("juror", "exam-prep/sixth-fix/juror-questions/JQ-R04-CARRIES.md"),
    ("juror", "exam-prep/sixth-fix/juror-questions/JQ-R04-DATE.md"),
    ("juror", "exam-prep/sixth-fix/juror-questions/JQ-R04-CONTENT.md"),
    ("juror-ranges", CANTEEN),
    ("cited-by-d", "decisions/2026-10-01-jq-r04-gate/verdict.md"),
    ("cited-by-d", "decisions/2026-10-01-jq-r04-date-content/verdict.md"),
    ("cited-by-d", "decisions/2026-10-01-jq-r04-carries/verdict.md"),
    ("index", "exam-prep/JUROR-QUESTIONS.md"),
]

QUOTES = ("USDT", "USDC", "BUSD", "FDUSD")
syms = []
with open(os.path.join(REPO, "data/universe/universe.csv"),
          encoding="utf-8") as fh:
    for row in csv.DictReader(fh):
        syms.append(row["symbol"])


def base_of(s):
    b = s
    for q in QUOTES:
        if b.endswith(q):
            b = b[:-len(q)]
            break
    b = re.sub(r"^(1000000|1000|1M)", "", b)
    return b


full = {s.upper() for s in syms}
bases = {base_of(s) for s in syms if len(base_of(s)) >= 2}
obs = set()
for ln in open(os.path.join(REPO, "data/draw/observation-coins.txt"),
               encoding="utf-8"):
    t = ln.strip().split()[0] if ln.strip() else ""
    if t and not t.startswith("#"):
        obs.add(t.upper())
        obs.add(base_of(t.upper()))
print("universe symbols: %d; bases (len>=2): %d; observation tokens: %d"
      % (len(full), len(bases), len(obs)))

MONTHS = ("january february march april may june july august september "
          "october november december jan feb mar apr jun jul aug sep sept "
          "oct nov dec monday tuesday wednesday thursday friday saturday "
          "sunday").split()
PROV = re.compile(r"system clock|eighth-fix run|seventh-fix run|sixth-fix run"
                  r"|fifth-fix run|fourth-fix run|third-fix run|second-fix run"
                  r"|Mateo|RATIFIED|Written|Added|decisions/", re.I)


def h(t):
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:12]


def scan(kind, rel):
    lines = open(os.path.join(REPO, rel), encoding="utf-8").read().split("\n")
    keep = range(1, len(lines) + 1)
    if kind == "juror-ranges":
        keep = [n for a, b in CANTEEN_RANGES for n in range(a, b + 1)]
    hits = []
    for n in keep:
        ln = lines[n - 1]
        for m in re.finditer(r"[A-Za-z0-9]+", ln):
            t = m.group(0)
            if t.upper() in full:
                hits.append(("SYM-FULL", n, m.start(), t))
            elif t in bases:
                hits.append(("SYM-BASE", n, m.start(), t))
            elif len(t) >= 4 and t.upper() in bases:
                hits.append(("SYM-WORD", n, m.start(), t))
            if t.upper() in obs:
                hits.append(("OBS", n, m.start(), t))
            if t.lower() in MONTHS and not (t.lower() == "may"
                                            and t == "may"):
                hits.append(("DATE", n, m.start(), t))
        for m in re.finditer(r"\b20\d\d-\d\d-\d\d\b", ln):
            hits.append(("DATE", n, m.start(), m.group(0)))
        for m in re.finditer(r"\b\d{1,2}:\d\d\b", ln):
            hits.append(("TIME", n, m.start(), m.group(0)))
        for m in re.finditer(r"[$€]\s?\d[\d,.]*|\b\d+\.\d{3,}\b", ln):
            hits.append(("PRICE", n, m.start(), m.group(0)))
    return hits, lines


for kind, rel in FILES:
    hits, lines = scan(kind, rel)
    cats = {}
    for c, n, col, t in hits:
        tag = c
        if c in ("DATE", "TIME") and PROV.search(lines[n - 1]):
            tag = c + "/provenance"
        cats[tag] = cats.get(tag, 0) + 1
    print("\n== [%s] %s: %d hits %s" % (kind, rel, len(hits),
                                       dict(sorted(cats.items()))))
    for c, n, col, t in hits:
        tag = c
        if c in ("DATE", "TIME") and PROV.search(lines[n - 1]):
            tag = c + "/provenance"
        print("   %-17s line %4d col %3d  token-sha256:%s  len %d"
              % (tag, n, col, h(t), len(t)))
