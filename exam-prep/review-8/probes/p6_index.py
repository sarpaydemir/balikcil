#!/usr/bin/env python3
"""Review 8, probe p6 -- the re-issued index exam-prep/JUROR-QUESTIONS.md.

(a) For every table row: the status word, and, where it names a verdict
    file, whether that file exists and its first line reads RATIFIED.
(b) Every run of SEVEN consecutive words the index shares with a juror file
    it names (current versions) -- the width is a probe setting carried over
    from REVIEW-7 p3, not a threshold.
(c) Every number token in the index outside SHA-256 values, with its line.
(d) Every answer label of the d file ("no", "only where …", "yes",
    "not a juror's", "Other") -- occurrences in the index of the multi-word
    labels.
Input: the index, the juror files it names, the verdict files it names.
Output: stdout (caller redirects to p6_index.out). No randomness.
"""
import os
import re
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = HERE.rsplit(os.sep + "exam-prep" + os.sep, 1)[0]
assert os.path.isfile(os.path.join(REPO, "RULES.md"))
WIDTH = 7  # probe setting (REVIEW-7 p3), not a threshold

idx_path = os.path.join(REPO, "exam-prep", "JUROR-QUESTIONS.md")
idx = open(idx_path, encoding="utf-8").read()
lines = idx.split("\n")

print("== (a) rows and statuses")
juror_files = set()
for ln in lines:
    if not ln.startswith("| JQ-"):
        continue
    cells = [c.strip() for c in ln.strip().strip("|").split("|")]
    ident, status = cells[0], cells[-1]
    for m in re.finditer(r"`(exam-prep/[^`]+\.md)`", cells[1]):
        juror_files.add(m.group(1))
    v = re.search(r"`(decisions/[^`]+/verdict\.md)`", status)
    vtxt = ""
    if v:
        vp = os.path.join(REPO, v.group(1))
        if os.path.isfile(vp):
            first = open(vp, encoding="utf-8").readline().strip()
            vtxt = "%s exists, first line %r" % (v.group(1), first)
        else:
            vtxt = "%s MISSING" % v.group(1)
    word = re.search(r"\*\*([^*]+)\*\*", status)
    print("  %-17s %-48s %s" % (ident, word.group(1) if word else status[:48],
                                vtxt))

print("\n== (b) shared runs of %d words with each juror file named" % WIDTH)


def words(t):
    return re.findall(r"[A-Za-z0-9'’\-]+", t.lower())


iw = words(idx)
igrams = {tuple(iw[i:i + WIDTH]) for i in range(len(iw) - WIDTH + 1)}
for jf in sorted(juror_files):
    jw = words(open(os.path.join(REPO, jf), encoding="utf-8").read())
    shared = sorted({tuple(jw[i:i + WIDTH])
                     for i in range(len(jw) - WIDTH + 1)} & igrams)
    print("  %s: %d shared" % (jf, len(shared)))
    for s in shared:
        print("      " + " ".join(s))

print("\n== (c) number tokens in the index (SHA-256 hex values removed)")
noh = re.sub(r"[0-9a-f]{64}", "<sha256>", idx)
for n, ln in enumerate(noh.split("\n"), 1):
    toks = re.findall(r"(?<![A-Za-z])\d[\d,.–-]*", ln)
    if toks:
        print("  line %d: %s" % (n, toks))

print("\n== (d) multi-word answer labels of the d file in the index")
for lab in ("only where the card may not be without the field",
            "only where", "not a juror's", "not a juror"):
    print("  %r: %d" % (lab, idx.count(lab)))
