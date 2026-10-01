#!/usr/bin/env python3
"""p3_index.py — review-7 probe of `exam-prep/JUROR-QUESTIONS.md`.

What it does
  1. Lists each row's identifier and status cell.
  2. Shared wording: every run of 7 consecutive words that the index shares
     with a question file it names, or with `exam-prep/USER-QUESTIONS.md`.
  3. Numbers: every number in the index (SHA-256 values removed), with the
     line it is on, so that the reviewer can say what each one is.
Input   exam-prep/JUROR-QUESTIONS.md, exam-prep/USER-QUESTIONS.md, and the
        question files under exam-prep/*/juror-questions/ that the index
        names. Nothing else.
Output  stdout only. No randomness, no threshold (7 words is a probe width,
        chosen by the reviewer and named in REVIEW-7 §8).
Run     PYTHONDONTWRITEBYTECODE=1 python3 -B exam-prep/review-7/probes/p3_index.py
"""
import os
import re
import sys

sys.dont_write_bytecode = True
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
IDX = "exam-prep/JUROR-QUESTIONS.md"
UQ = "exam-prep/USER-QUESTIONS.md"
WIDTH = 7  # probe width in words (reviewer's choice, not a threshold)


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def words(t):
    t = re.sub(r"[`*|]", " ", t)
    return re.findall(r"[A-Za-z0-9'’–-]+", t.lower())


def shingles(t):
    w = words(t)
    return {" ".join(w[i:i + WIDTH]) for i in range(len(w) - WIDTH + 1)}


def main():
    idx = read(IDX)
    print("== 1 · rows and statuses")
    for ln in idx.split("\n"):
        m = re.match(r"\| (JQ-[A-Za-z0-9-]+) \|", ln)
        if m:
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            print("%-18s %s" % (m.group(1), cells[-1][:150]))
    files = sorted(set(re.findall(
        r"exam-prep/[a-z-]+/juror-questions/JQ-[A-Za-z0-9-]+\.md", idx)))
    print("\n== 2 · shared %d-word runs" % WIDTH)
    si = shingles(idx)
    for rel in files + [UQ]:
        common = sorted(si & shingles(read(rel)))
        print("%s: %d shared runs" % (rel, len(common)))
        for c in common:
            print("    " + c)
    print("\n== 3 · numbers (SHA-256 removed)")
    for i, ln in enumerate(idx.split("\n"), 1):
        t = re.sub(r"[0-9a-f]{64}", " ", ln)
        t = re.sub(r"\d{4}-\d{2}-\d{2}", " ", t)
        nums = re.findall(r"\d[\d,.–-]*\d|\d", t)
        if nums:
            print("line %d: %s" % (i, " ".join(nums)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
