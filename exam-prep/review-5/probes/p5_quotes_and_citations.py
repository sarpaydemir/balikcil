#!/usr/bin/env python3
"""
p5_quotes_and_citations.py -- REVIEW-5 probe.
(1) The three passages JQ-R04-CONTENT part d quotes, checked against the
    cited lines (markdown emphasis and whitespace removed on both sides).
(2) Every canteen line range cited in the four fifth-fix juror files, set
    against the canteen ranges each index row gives a juror.
Input : the four fifth-fix juror files, exam-prep/JUROR-QUESTIONS.md,
        exam-prep/third-fix/juror-questions/JQ-R04-GATE.md,
        decisions/2026-10-01-jq-r04-gate/verdict.md
Output: stdout (saved as p5_quotes_and_citations.out). No threshold.
"""
import os
import re
import sys

sys.dont_write_bytecode = True
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))


def rd(rel):
    return open(os.path.join(ROOT, rel), encoding="utf-8").read()


def norm(s):
    # blockquote markers at line starts are layout, not text
    s = re.sub(r"(?m)^\s*>\s?", "", s)
    s = s.replace("**", "").replace("`", "")
    return re.sub(r"\s+", " ", s).strip()


def lines(rel, a, b):
    return "\n".join(rd(rel).splitlines()[a - 1:b])


Q = [("exam-prep/third-fix/juror-questions/JQ-R04-GATE.md", 55, 57,
      "If `ALL-removable` beats its chance line on the exam cards, the cards "
      "are not blind and the gate has failed."),
     ("exam-prep/third-fix/juror-questions/JQ-R04-GATE.md", 64, 66,
      "`ALL-removable` is **every feature in the audit's current list**, "
      "minus the families that must stay on the card because a frozen "
      "canteen rule or TACTICS requires them."),
     ("decisions/2026-10-01-jq-r04-gate/verdict.md", 72, 72,
      "The gate fails if either the nearest-neighbour attack or the pair AUC "
      "attack beats its own RULES 12 chance line on the exam cards.")]
content = norm(rd("exam-prep/fifth-fix/juror-questions/JQ-R04-CONTENT.md"))
for rel, a, b, q in Q:
    src = norm(lines(rel, a, b))
    print("quote %s %d-%d: in source lines %s; in part d %s"
          % (rel, a, b, norm(q) in src, norm(q) in content))

print()
FILES = ["JQ-N1.md", "JQ-CANTEEN-8.md", "JQ-R04-DATE.md",
         "JQ-R04-CONTENT.md"]
cite = re.compile(r"(?:lines?|line)\s+(\d+)(?:\s*[–-]\s*(\d+))?")
for f in FILES:
    txt = rd("exam-prep/fifth-fix/juror-questions/" + f)
    found = set()
    paras = re.split(r"\n\s*\n", txt)
    for p in paras:
        # a canteen citation: the paragraph/bullet names the canteen book or
        # a canteen rule id, and a line number follows
        if "canteen" not in p and not re.search(r"\b(S-1|B-[0-9]|§8)\b", p):
            continue
        for m in cite.finditer(p):
            pre = p[max(0, m.start() - 160):m.start()]
            if ("RULES.md" in pre[-60:] or "TACTICS" in pre[-60:]
                    or "scripts/" in pre[-80:]):
                continue
            found.add((int(m.group(1)), int(m.group(2) or m.group(1))))
    print("%-18s canteen-looking line citations: %s" % (f, sorted(found)))

idx = rd("exam-prep/JUROR-QUESTIONS.md")
print()
for row in idx.splitlines():
    if row.startswith("| JQ-"):
        cells = [c.strip() for c in row.split("|")]
        rngs = re.findall(r"lines ([^|]*?) only", cells[4])
        print("%-18s canteen on list: %s" % (cells[1], rngs or "none"))
