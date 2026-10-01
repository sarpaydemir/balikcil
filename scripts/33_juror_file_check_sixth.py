#!/usr/bin/env python3
"""
33_juror_file_check_sixth.py -- checks the juror files and the index the
sixth-fix run issued, acting on exam-prep/REVIEW-5.md (DATE and CONTENT
rows only).

What it does
------------
  X  Removed / pointers. In the four sixth-fix juror files (JQ-R04-DATE,
     JQ-R04-CONTENT, JQ-R04-CONTENT-d, JQ-R04-CARRIES): no run number (16
     hex digits), no `scripts/` path, no review, VERDICT, HANDED-FORWARD,
     *-FIX.md, probe, manifest file, checks/ or identity/ folder; every
     `exam-prep/` path is a juror file on that file's own reading list; the
     DATE and CONTENT files no longer carry part d, "four parts", or the
     gate's fail condition; their closing paragraphs say where the rest is
     decided (JQ-R04-CONTENT-d, other jurors).
  N  No new measured number. Every number in a sixth-fix file occurs in the
     fifth-fix DATE or CONTENT file, except the numbers in NEW_NUMBERS, each
     listed with its reason and checked by Q.
  Q  Quotes and premises. Every rule passage the two new files quote is
     found in the cited lines; the GATE file and the ratified verdict
     passages part d quotes are found in their lines; every statement the
     new files make about the audit is checked against
     scripts/29_identity_audit_exact.py, read as text and parsed with `ast`
     (not imported, not run).
  D  Part d kept. The question and the two options of the fifth-fix part d
     that the sixth-fix file says are unchanged occur in it word for word
     (whitespace-insensitive), apart from the one named rewording.
  I  Index. Every row present once; no digit outside an identifier, a path,
     a line range, a SHA-256, a rule reference, a section locator or a date;
     no reading list names a forbidden file; every listed path exists; the
     union of "What you open" over a row's group equals the row's list;
     answer-together is symmetric; JQ-R04-CARRIES and JQ-R04-CONTENT-d share
     a group with no DATE/CONTENT row; JQ-R04-GATE shown ratified; the
     order section names the groups; earlier index versions match their
     stated SHA-256.
  U  Unchanged. Every file in the run's pre-run snapshots
     (exam-prep/sixth-fix/pre-run-fingerprints.txt, and
     pre-run-scripts-fingerprints.txt for scripts/, exam_* never read) has
     the same SHA-256, except the index (re-issued; its earlier version kept
     byte for byte) and the three appended files (HANDED-FORWARD.md,
     VERDICT.md, README.md), which must start with their
     pre-run bytes. No new file outside exam-prep/sixth-fix/ except this
     script. The two files three jurors are answering now have the SHA-256
     the instruction states. scripts/__pycache__/ holds the same nine names.

Input   : the files named above (repository-relative paths).
Output  : exam-prep/sixth-fix/checks/juror-file-check-<run16>.md
          exam-prep/sixth-fix/checks/runs/<run16>.json      (append-only)
          exam-prep/sixth-fix/checks/runs/<run16>.clock     (one clock line
          appended per run; the clock is read, not guessed -- RULES 23)
          --dry: prints, writes nothing.
Run number: SHA-256 over the contents of every input, keyed by its
          repository-relative path. VERDICT.md and SIXTH-FIX.md quote this
          run number, so they are not inputs; only VERDICT.md's and
          README.md's pre-run prefixes are read (U).
Rules   : RULES 19, 23, 29, 30, 32-34. No threshold, score or trading rule
          is defined here.
Run with PYTHONDONTWRITEBYTECODE=1 and python3 -B.
"""
import ast
import datetime as dt
import hashlib
import json
import os
import re
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
EP = "exam-prep"
F5 = EP + "/fifth-fix/juror-questions/"
F6 = EP + "/sixth-fix/juror-questions/"
OUT = EP + "/sixth-fix/checks"

DATE6 = F6 + "JQ-R04-DATE.md"
CONT6 = F6 + "JQ-R04-CONTENT.md"
D6 = F6 + "JQ-R04-CONTENT-d.md"
CAR6 = F6 + "JQ-R04-CARRIES.md"
DATE5 = F5 + "JQ-R04-DATE.md"
CONT5 = F5 + "JQ-R04-CONTENT.md"
N1_5 = F5 + "JQ-N1.md"
C8_5 = F5 + "JQ-CANTEEN-8.md"
GATE = EP + "/third-fix/juror-questions/JQ-R04-GATE.md"
VERD = "decisions/2026-10-01-jq-r04-gate/verdict.md"
AUDIT = "scripts/29_identity_audit_exact.py"
INDEX = EP + "/JUROR-QUESTIONS.md"
INDEX_COPY = EP + "/sixth-fix/JUROR-QUESTIONS-as-of-fifth-fix.md"
HF = EP + "/HANDED-FORWARD.md"
VERDICT = EP + "/VERDICT.md"
SNAP = EP + "/sixth-fix/pre-run-fingerprints.txt"
SNAP_S = EP + "/sixth-fix/pre-run-scripts-fingerprints.txt"
SELF = "scripts/33_juror_file_check_sixth.py"

# The files three jurors are answering now, with the SHA-256 the sixth-fix
# instruction states. They must not change.
JURY_NOW = {
    N1_5: "071bf434f05cfc7e83b87b7698274f609a5bf28334b956fec95e64b50709497e",
    C8_5: "944c5d85ee547e93ae55ac8d5f10dab05bc5ebe593b3de03d9b092b40aa8d396",
}
# Pre-run size of the three appended files, measured with `wc -c` before
# anything was appended to each (HANDED-FORWARD.md and VERDICT.md at
# 2026-10-01T23:03Z, README.md at 2026-10-01T23:10Z); their pre-run SHA-256 is
# taken from the snapshot, so a wrong size here fails U, it cannot pass it.
APPENDED = {HF: 28525, VERDICT: 34212, EP + "/README.md": 5937}
# The index was re-issued; its pre-run version is kept byte for byte here.
REISSUED = {INDEX: INDEX_COPY}

# Numbers allowed in a sixth-fix file although they are not in the fifth-fix
# DATE or CONTENT file. Every one is a line number of a passage quoted for
# the first time (checked by Q), a count read from the audit's code
# (checked by Q), part of an identifier, or a quoted rule figure.
NEW_NUMBERS = {
    "50": "TACTICS.md lines 50-51, quoted (Q)",
    "51": "TACTICS.md lines 50-51 / RULES.md lines 51-52, quoted (Q)",
    "52": "RULES.md lines 51-52, quoted (Q)",
    "55": "TACTICS.md lines 55-62, quoted (Q)",
    "62": "TACTICS.md lines 55-62, quoted (Q)",
    "103": "TACTICS.md lines 101-103, quoted (Q)",
    "107": "TACTICS.md lines 101-107, quoted (Q)",
    "119": "RULES.md lines 119-121, quoted (Q)",
    "121": "RULES.md lines 119-121, quoted (Q)",
    "72": "verdict line 72, quoted (Q)",
    "7": "'previous-7-day' / '7 days', TACTICS 3's own words (Q)",
    "24": "'the card's 24 hours' / '24 hours', TACTICS 3's own words (Q)",
    "33": "RULES 33, a rule reference",
    "12": "RULES 12, a rule reference",
    "-04": "identifier JQ-R04",
}

# Numbers that may disappear from the DATE / CONTENT files: section numbers
# of a review that the files no longer name (sixth-fix instruction item 3).
GONE_ALLOWED = {"3.4": "REVIEW.md section 3.4, pointer removed",
                "3.2": "REVIEW.md section 3.2, pointer removed"}

FORBIDDEN_IN_JUROR = [
    (r"\b[0-9a-f]{16}\b", "a run number"),
    (r"scripts/", "a script path"),
    (r"REVIEW", "a review"),
    (r"VERDICT", "VERDICT.md"),
    (r"HANDED", "HANDED-FORWARD.md"),
    (r"-FIX\.md", "a *-FIX.md file"),
    (r"probe", "a probe"),
    (r"blind-manifest", "a manifest file"),
    (r"/checks/", "a checks folder"),
    (r"/identity/", "an identity folder"),
    (r"JQ-R04-GATE\.md", "the GATE file, which states gate figures"),
    (r"pre-run", "a snapshot"),
    (r"criteria", "a criteria file"),
]
FORBIDDEN_IN_LIST = re.compile(
    r"REVIEW|VERDICT|HANDED|-FIX\.md|criteria|/checks/|/identity/|"
    r"/collapse/|review-|blind-proof|pre-run|R-04-blindness|N-1-collapse|"
    r"decisions-and-open")

IDS = ["JQ-N1-1", "JQ-N1-2", "JQ-N1-3", "JQ-N1-4", "JQ-CANTEEN-8",
       "JQ-R04-GATE", "JQ-R04-CARRIES-a", "JQ-R04-CARRIES-b",
       "JQ-R04-DATE-a", "JQ-R04-DATE-b", "JQ-R04-DATE-c",
       "JQ-R04-CONTENT-a", "JQ-R04-CONTENT-b", "JQ-R04-CONTENT-c",
       "JQ-R04-CONTENT-d", "JQ-B1"]

EARLIER_INDEX = {
    EP + "/sixth-fix/JUROR-QUESTIONS-as-of-fifth-fix.md":
        "2e09076f475df688704f7788a33cdf77996016533fc92ffc1e0105f34237c715",
    EP + "/fifth-fix/JUROR-QUESTIONS-as-of-fourth-fix.md":
        "90c51c9e60f8c11a895b11cc6abc067504edb9e8abb11267502f56424c580dc0",
    EP + "/fourth-fix/JUROR-QUESTIONS-as-of-third-fix.md":
        "c1d3dfdeab36a40f3c2b2096b53c80d057603c3c07d1bfdeeb64f45fefa10720",
    EP + "/third-fix/JUROR-QUESTIONS-as-of-second-fix.md":
        "7020127c257b7addbae1fd6cbca0e4031accc3b28a4816980c5cd410532399d9",
}

RESULTS = []


def die(msg):
    sys.stderr.write("STOP: %s\n" % msg)
    sys.exit(2)


def p(rel):
    return os.path.join(REPO, rel)


def read(rel):
    with open(p(rel), encoding="utf-8") as fh:
        return fh.read()


def readb(rel):
    with open(p(rel), "rb") as fh:
        return fh.read()


def sha(b):
    return hashlib.sha256(b).hexdigest()


def norm(s):
    s = s.replace("**", "").replace("`", "")
    return re.sub(r"\s+", " ", s).strip()


def check(group, name, ok, detail=""):
    RESULTS.append({"group": group, "check": name, "ok": bool(ok),
                    "detail": detail})


def lines(rel, a, b):
    ls = read(rel).split("\n")
    return "\n".join(ls[a - 1:b])


def numbers(text):
    text = re.sub(r"JQ-R04", "JQ-R-04", text)
    return set(re.findall(r"-04|\d+(?:[.,]\d+)*", text))


def section(text, title):
    m = re.search(r"^## " + re.escape(title) + r"\n(.*?)(?=^## |\Z)", text,
                  re.S | re.M)
    return m.group(1) if m else ""


def paths_in(text):
    return set(re.findall(r"`((?:exam-prep|decisions|canteen)/[^`]+|"
                          r"RULES\.md|TACTICS\.md)`", text))


# --------------------------------------------------------------------- X
def check_x():
    files = {DATE6: read(DATE6), CONT6: read(CONT6), D6: read(D6),
             CAR6: read(CAR6)}
    for rel, txt in files.items():
        for pat, what in FORBIDDEN_IN_JUROR:
            hits = re.findall(pat, txt)
            check("X", "%s names no %s" % (os.path.basename(rel), what),
                  not hits, "; ".join(sorted(set(hits)))[:200])
        own = paths_in(section(txt, "What you open"))
        ep = {x for x in paths_in(txt) if x.startswith("exam-prep/")}
        check("X", "%s: every exam-prep path is on its own reading list"
              % os.path.basename(rel), ep <= own, str(sorted(ep - own)))
        others = {x for x in paths_in(txt)
                  if not x.startswith("exam-prep/")} - {
            "RULES.md", "TACTICS.md", "canteen/2026-09-19-sofia.md", VERD}
        check("X", "%s: no other path" % os.path.basename(rel), not others,
              str(sorted(others)))
    for rel in (DATE6, CONT6):
        t = norm(files[rel])
        b = os.path.basename(rel)
        for gone in ("part d", "Part d", "four parts", "all four",
                     "fail the gate", "fails the gate", "ALL-removable",
                     "either attack beats"):
            check("X", "%s: '%s' gone" % (b, gone), gone not in t)
        check("X", "%s: closing paragraph says where the rest is decided" % b,
              "decided by a separate question, JQ-R04-CONTENT-d, which other "
              "jurors answer; it is not yours to decide" in t)
    t = norm(files[CONT6])
    check("X", "CONTENT: three parts in title", "— three parts" in t)
    check("X", "CONTENT: part a names JQ-R04-CARRIES as answered before",
          "JQ-R04-CARRIES, which other jurors answer before you sit" in t)
    check("X", "CONTENT: section heading no longer defines 'carries'",
          'How "carries a coin signature" is measured' not in files[CONT6])
    check("X", "DATE: 'all three of its parts'",
          "all three of its parts" in norm(files[DATE6]))


# --------------------------------------------------------------------- N
def check_n():
    base = numbers(read(DATE5)) | numbers(read(CONT5))
    for rel in (DATE6, CONT6, D6, CAR6):
        txt = read(rel)
        # the run's own date line(s) and identifiers carry dates/digits
        txt2 = re.sub(r"2026-10-01", "", txt)
        new = numbers(txt2) - base
        extra = new - set(NEW_NUMBERS)
        check("N", "%s: no new number outside NEW_NUMBERS"
              % os.path.basename(rel), not extra, str(sorted(extra)))
        used = sorted(new & set(NEW_NUMBERS))
        check("N", "%s: allowed new numbers used" % os.path.basename(rel),
              True, ", ".join(used))
    # the measured figures of DATE and CONTENT are kept, not changed
    for r5, r6 in ((DATE5, DATE6), (CONT5, CONT6)):
        five = {x for x in numbers(read(r5)) if "." in x or "," in x}
        gone = {x for x in five if x not in numbers(read(r6))}
        gone -= set(GONE_ALLOWED)
        check("N", "%s: every decimal/thousands figure kept"
              % os.path.basename(r6), not gone, str(sorted(gone)))


# --------------------------------------------------------------------- Q
def quote_in(rel, a, b, quote):
    src = norm(re.sub(r"(?m)^\s*> ?", "", lines(rel, a, b)))
    frags = [f.strip(" \"'") for f in re.split(r"…|\" · \"", norm(quote))]
    frags = [f for f in frags if f]
    miss = [f for f in frags if f not in src]
    return not miss, "; ".join(miss)[:200]


def check_q():
    rq = [
        # (file, a, b, quote, which juror file)
        ("RULES.md", 34, 35, "The rule is written first, the result is "
         "opened second. A rule is not changed after looking at a result.",
         D6),
        ("RULES.md", 41, 41, "In the exam the coin name and the date are "
         "hidden.", D6),
        ("RULES.md", 51, 52, "The chance line is not invented. The answers "
         "are shuffled 1,000 times, and the real result must fall inside "
         "the best 1%.", D6),
        ("TACTICS.md", 50, 51, "the 24 hours before the start, hour by hour; "
         "plus a one-line summary of the previous 7 days.", D6),
        ("TACTICS.md", 55, 62, "price, volume, trade count, taker buy/sell "
         "pressure\" · \"open interest, long/short ratios (5-minute "
         "archive)\" · \"funding rate, payment interval and its changes\" · "
         "\"order book depth\" … \"bitcoin and ethereum, over the same "
         "hours\" · \"US release calendar (inflation, employment, rate "
         "decision)", D6),
        ("TACTICS.md", 101, 107, "the coin name\" · \"the date and time\" · "
         "\"the price itself (converted to a number starting from 100)\" · "
         "\"the coin name inside announcements\" · \"the Wikipedia number "
         "itself (given as a ratio to the coin's own average)\" · \"the date "
         "in the release calendar", D6),
        ("RULES.md", 41, 41, "In the exam the coin name and the date are "
         "hidden.", CAR6),
        ("RULES.md", 51, 52, "The chance line is not invented. The answers "
         "are shuffled 1,000 times, and the real result must fall inside "
         "the best 1%.", CAR6),
        ("RULES.md", 119, 121, "A juror decides procedure and definition "
         "only: never a trading rule, never a threshold or score, and never "
         "a change to a rule in this file.", CAR6),
        ("TACTICS.md", 50, 51, "the 24 hours before the start, hour by hour; "
         "plus a one-line summary of the previous 7 days.", CAR6),
        ("TACTICS.md", 56, 56, "price, volume, trade count, taker buy/sell "
         "pressure", CAR6),
        ("TACTICS.md", 101, 103, "the coin name\" · \"the date and time",
         CAR6),
        (GATE, 55, 57, "If ALL-removable beats its chance line on the exam "
         "cards, the cards are not blind and the gate has failed.", D6),
        (GATE, 64, 66, "ALL-removable is every feature in the audit's "
         "current list, minus the families that must stay on the card "
         "because a frozen canteen rule or TACTICS requires them.", D6),
        (VERD, 72, 72, "The gate fails if either the nearest-neighbour "
         "attack or the pair AUC attack beats its own RULES 12 chance line "
         "on the exam cards.", D6),
        (AUDIT, 431, 431, "the frozen book's S-1 reads chg% at 5.00% "
         "absolute", D6),
        (AUDIT, 432, 432, "B-5, U-2 and U-3 are answered from it", D6),
        (AUDIT, 433, 433, "TACTICS 3 puts a previous-7-day summary on the "
         "card", D6),
        (AUDIT, 434, 434, "it reads the same unchanged chg% column", D6),
        ("canteen/2026-09-19-sofia.md", 114, 118, "at least one row whose "
         "hourly close-to-close change is |5.00%| or more. Read it from the "
         "chg% column. If an exam card does not print chg%, compute it from "
         "the close column as close(h)/close(h-1) - 1", CONT6),
    ]
    for rel, a, b, q, jf in rq:
        ok, miss = quote_in(rel, a, b, q)
        check("Q", "%s lines %d-%d as quoted" % (rel, a, b), ok, miss)
        check("Q", "quote present in %s (%s %d-%d)"
              % (os.path.basename(jf), rel, a, b),
              norm(q).split("\" · \"")[0].split(" … ")[0][:60]
              in norm(read(jf)), "")
    # the audit's code, read as text and parsed with ast
    src = read(AUDIT)
    tree = ast.parse(src)
    consts = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and \
                isinstance(node.targets[0], ast.Name):
            try:
                consts[node.targets[0].id] = ast.literal_eval(node.value)
            except Exception:
                pass
    fam = consts.get("FAMILIES", {})
    forced = consts.get("FORCED_FAMILIES", ())
    check("Q", "FORCED_FAMILIES are the four part d names",
          tuple(forced) == ("volatility-frozen", "funding-line", "p7-shape",
                            "repeat-chg"), str(forced))
    check("Q", "trades-level = column level + one 7-day feature",
          fam.get("trades-level") == ["trades:", "p7:log_avg_trades"],
          str(fam.get("trades-level")))
    check("Q", "repeat-trades holds only rep-trades:",
          fam.get("repeat-trades") == ["rep-trades:"])
    check("Q", "shape-scale-free holds shape:",
          fam.get("shape-scale-free") == ["shape:"])
    m = re.search(r'for name, tag in \(\("quote vol", "vol"\),(.*?)\):\n'
                  r'\s+if not has\(name\)', src, re.S)
    shape_cols = re.findall(r'\("([^"]+)", "[a-z_]+"\)',
                            '("quote vol", "vol"),' + (m.group(1) if m else ""))
    check("Q", "shape family covers trades and seven other named columns",
          sorted(shape_cols) == sorted(["quote vol", "trades", "open int",
                                        "depth -1%", "depth +1%", "L/S acct",
                                        "top L/S pos", "taker L/S"]),
          str(shape_cols))
    trades_feats = set(re.findall(r'f\["(trades:[a-z_]+)"\]', src))
    check("Q", "one feature with prefix trades: (the median level)",
          trades_feats == {"trades:log_median_trades"} and
          'f["trades:log_median_trades"] = safelog(median(col["trades"]))'
          in src, str(trades_feats))
    check("Q", "two repeat features per column (distinct, maxrepeat)",
          '"rep-%s:%s:distinct"' in src and '"rep-%s:%s:maxrepeat"' in src)
    check("Q", "two shape features per column (sd of logs, lag-1 acf)",
          'f["shape:sd_log_" + tag]' in src and
          'f["shape:acf1_log_" + tag]' in src)
    check("Q", "a constant or missing feature is not used",
          "a key that is constant or absent" in src and
          "on any card contributes nothing" in src)
    inside = ["btc-eth", "repeat-btceth", "trades-level", "repeat-trades",
              "shape-scale-free", "price-level", "repeat-close",
              "granularity-close", "volume-level", "repeat-volume",
              "openint-level", "repeat-openint", "depth-level",
              "repeat-depth", "ratio-level", "repeat-ratio", "taker-buy",
              "repeat-takerbuy"]
    check("Q", "part d premise: every family of the named columns is "
          "inside the row", all(f in fam and f not in forced
                                for f in inside))
    check("Q", "the audit does not compute a per-column row today",
          not any(k.startswith("own-") for k in fam) and
          '("ALL-removable",' in src)
    rg = consts.get("REPEAT_GROUP", {})
    check("Q", "repeat-trades reads only the trades column",
          [k for k, v in rg.items() if v == "trades"] == ["trades"])


# --------------------------------------------------------------------- D
def check_d():
    five = norm(read(CONT5)[read(CONT5).index("## Part d"):])
    six = norm(read(D6))
    m = re.search(r"- yes — (.*?) - only where no permitted rendering "
                  r"leaves it out — (.*?) - no — ", five)
    if not m:
        check("D", "fifth-fix part d options found", False)
        return
    check("D", "option 'yes' unchanged", ("yes — " + m.group(1)) in six)
    check("D", "middle option unchanged",
          ("only where no permitted rendering leaves it out — " +
           m.group(2)) in six)
    q5 = re.search(r"Question d\. (.*?)\?", five).group(1)
    q6 = re.search(r"Question d\. (.*?)\?", six).group(1)
    reworded = q5.replace("to parts a–c here",
                          "to JQ-R04-CONTENT parts a–c")
    check("D", "question d unchanged but for naming the former parts",
          reworded == q6, q6[:200])
    for para in ("Which features are computed from a field is read from the "
                 "audit's code, not chosen; the run that composes the row "
                 "records it, and that run is reviewed.",
                 "a question about a rule is the user's, not a juror's "
                 "(RULES 33)."):
        check("D", "kept: %s..." % para[:40], para in six and para in five)


# --------------------------------------------------------------------- I
def parse_index():
    rows = {}
    for ln in read(INDEX).split("\n"):
        if not ln.startswith("| JQ-"):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        rows[cells[0]] = cells
    return rows


def what_you_open(rel):
    return paths_in(section(read(rel), "What you open"))


def check_i():
    txt = read(INDEX)
    rows = parse_index()
    check("I", "every row present once", sorted(rows) == sorted(IDS) and
          len([l for l in txt.split("\n") if l.startswith("| JQ-")]) ==
          len(IDS), str(sorted(set(IDS) ^ set(rows))))
    t = txt
    t = re.sub(r"`[^`]*`", "", t)
    t = re.sub(r"\b[0-9a-f]{64}\b", "", t)
    t = re.sub(r"JQ-[A-Za-z0-9-]+", "", t)
    t = re.sub(r"lines \d+–\d+(?:, \d+–\d+)*(?: and \d+–\d+)?", "", t)
    t = re.sub(r"Part \d+(?: \(with \d+a and \d+b\))?", "", t)
    t = re.sub(r"RULES \d+–\d+", "", t)
    t = re.sub(r"SHA-256", "", t)
    t = re.sub(r"2026-10-01", "", t)
    t = re.sub(r"R-04", "", t)
    left = re.findall(r"\d", t)
    check("I", "no stray digit in the index", not left,
          str(sorted(set(re.findall(r".{12}\d.{6}", t))))[:300])
    for rid, cells in rows.items():
        need = cells[3]
        check("I", "%s: list names no forbidden file" % rid,
              not FORBIDDEN_IN_LIST.search(need), need[:120])
        for pth in re.findall(r"`([^`]+)`", need):
            check("I", "%s: listed file exists: %s" % (rid, pth),
                  os.path.exists(p(pth)))
    # group union
    file_of = {r: re.search(r"`([^`]+)`", c[1]).group(1)
               for r, c in rows.items() if r != "JQ-B1"}
    for rid, cells in rows.items():
        if rid in ("JQ-B1", "JQ-R04-GATE"):
            continue
        together = [] if cells[2] in ("none", "—") else \
            [x.strip() for x in cells[2].split(",")]
        group = [rid] + together
        union = set()
        for g in group:
            union |= what_you_open(file_of[g]) | {file_of[g]}
        union = {u for u in union if not u.startswith("canteen/")}
        listed = {x for x in re.findall(r"`([^`]+)`", cells[3])
                  if not x.startswith("canteen/")}
        check("I", "%s: list equals its group's 'What you open'" % rid,
              union == listed, str(sorted(union ^ listed)))
        for g in together:
            other = rows[g][2]
            check("I", "%s: answer-together symmetric with %s" % (rid, g),
                  rid in other)
    dc = {"JQ-R04-DATE-a", "JQ-R04-DATE-b", "JQ-R04-DATE-c",
          "JQ-R04-CONTENT-a", "JQ-R04-CONTENT-b", "JQ-R04-CONTENT-c"}
    for rid in ("JQ-R04-CARRIES-a", "JQ-R04-CARRIES-b", "JQ-R04-CONTENT-d"):
        tog = set(x.strip() for x in rows[rid][2].split(","))
        check("I", "%s shares no group with a DATE/CONTENT row" % rid,
              not (tog & dc))
    check("I", "JQ-R04-CONTENT-d alone", rows["JQ-R04-CONTENT-d"][2] ==
          "none")
    for rid in sorted(dc):
        check("I", "%s: waits for JQ-R04-CARRIES" % rid,
              "not to be commissioned until JQ-R04-CARRIES is ratified"
              in rows[rid][4] and
              "ratification sentence of the JQ-R04-CARRIES verdict only"
              in rows[rid][3])
        check("I", "%s: canteen by line ranges only" % rid,
              "lines 112–120, 221–225, 245–246, 268–270 and 667–671 only"
              in rows[rid][3])
    check("I", "CONTENT file announces the ratification sentence",
          "ratification sentence" in section(read(CONT6), "What you open"))
    check("I", "GATE ratified, verdict named",
          "ratified" in rows["JQ-R04-GATE"][4] and VERD in
          rows["JQ-R04-GATE"][4])
    order = section(txt, "The order in which the groups sit")
    check("I", "order section names every open group",
          all(x in order for x in ("JQ-N1", "JQ-R04-CARRIES",
                                   "JQ-R04-DATE-a", "JQ-R04-CONTENT-d")))
    for rel, h in EARLIER_INDEX.items():
        check("I", "earlier index kept: %s" % rel,
              sha(readb(rel)) == h and rel in txt and h in txt)


# --------------------------------------------------------------------- U
def check_u():
    snap = {}
    for ln in read(SNAP).split("\n"):
        if ln.strip():
            h, rel = ln.split("  ", 1)
            snap[rel] = h
    for rel, h in snap.items():
        if not os.path.exists(p(rel)):
            check("U", "still present: %s" % rel, False)
            continue
        b = readb(rel)
        if rel in REISSUED:
            check("U", "re-issued, earlier kept: %s" % rel,
                  sha(readb(REISSUED[rel])) == h)
        elif rel in APPENDED:
            check("U", "appended, prefix unchanged: %s" % rel,
                  sha(b[:APPENDED[rel]]) == h and len(b) > APPENDED[rel])
        else:
            if sha(b) != h:
                check("U", "unchanged: %s" % rel, False)
    check("U", "every other snapshot file unchanged",
          not [r for r in RESULTS if r["group"] == "U" and not r["ok"]])
    now = []
    for root, dirs, files in os.walk(p(EP)):
        for f in files:
            now.append(os.path.relpath(os.path.join(root, f), REPO))
    new = sorted(set(now) - set(snap))
    bad = [x for x in new if not x.startswith(EP + "/sixth-fix/")]
    check("U", "no new exam-prep file outside sixth-fix/", not bad, str(bad))
    ssnap = {}
    for ln in read(SNAP_S).split("\n"):
        if ln.strip():
            h, rel = ln.split("  ", 1)
            ssnap[rel] = h
    for rel, h in ssnap.items():
        if sha(readb(rel)) != h:
            check("U", "script unchanged: %s" % rel, False)
    names = sorted("scripts/" + f for f in os.listdir(p("scripts"))
                   if os.path.isfile(p("scripts/" + f))
                   and not f.startswith("exam_"))
    check("U", "only new script is this one",
          sorted(set(names) - set(ssnap)) == [SELF],
          str(sorted(set(names) ^ set(ssnap))))
    for rel, h in JURY_NOW.items():
        check("U", "jury file unchanged: %s" % rel, sha(readb(rel)) == h)
    pyc = sorted(os.listdir(p("scripts/__pycache__")))
    check("U", "scripts/__pycache__ holds nine names, none for script 29 or "
          "33", len(pyc) == 9 and not any(x.startswith(("29_", "33_"))
                                          for x in pyc), str(pyc))


def main():
    dry = "--dry" in sys.argv[1:]
    clock = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    inputs = [DATE6, CONT6, D6, CAR6, DATE5, CONT5, N1_5, C8_5, GATE, VERD,
              AUDIT, INDEX, INDEX_COPY, HF, SNAP, SNAP_S, SELF, "RULES.md",
              "TACTICS.md", "canteen/2026-09-19-sofia.md"] + \
        sorted(EARLIER_INDEX)
    h = hashlib.sha256()
    for rel in sorted(set(inputs)):
        h.update(rel.encode() + b"\0" + readb(rel) + b"\0")
    h.update(b"VERDICT-prefix\0" + readb(VERDICT)[:APPENDED[VERDICT]])
    h.update(b"README-prefix\0" + readb(EP + "/README.md")[:APPENDED[EP + "/README.md"]])
    run_full = h.hexdigest()
    run16 = run_full[:16]

    check_x()
    check_n()
    check_q()
    check_d()
    check_i()
    check_u()

    n_ok = sum(r["ok"] for r in RESULTS)
    n_fail = len(RESULTS) - n_ok
    rep = ["# Juror-file check, sixth-fix run — run %s" % run16, "",
           "Script: `%s`. Run number: first 16 hex digits of SHA-256 over "
           "the inputs (`%s`). %d checks, %d ok, %d failed." %
           (SELF, run_full, len(RESULTS), n_ok, n_fail), "",
           "| group | check | result | detail |", "|---|---|---|---|"]
    for r in RESULTS:
        rep.append("| %s | %s | %s | %s |" % (
            r["group"], r["check"].replace("|", "/"),
            "ok" if r["ok"] else "**FAIL**",
            r["detail"].replace("|", "/").replace("\n", " ")))
    rep.append("")
    report = "\n".join(rep)
    rec = json.dumps({"run": run16, "run_full": run_full,
                      "inputs": sorted(set(inputs)) + ["VERDICT.md prefix",
                                                       "README.md prefix"],
                      "checks": len(RESULTS), "ok": n_ok, "failed": n_fail,
                      "results": RESULTS}, indent=1, sort_keys=True) + "\n"
    print("run %s  checks %d  ok %d  failed %d  clock %s" %
          (run16, len(RESULTS), n_ok, n_fail, clock))
    for r in RESULTS:
        if not r["ok"]:
            print("FAIL  %s  %s  %s" % (r["group"], r["check"], r["detail"]))
    if dry:
        return 0 if n_fail == 0 else 1
    os.makedirs(p(OUT + "/runs"), exist_ok=True)
    for rel, content in ((OUT + "/juror-file-check-%s.md" % run16, report),
                         (OUT + "/runs/%s.json" % run16, rec)):
        if os.path.exists(p(rel)):
            if read(rel) != content:
                die("%s exists with different content (RULES 30)" % rel)
        else:
            with open(p(rel), "w", encoding="utf-8") as fh:
                fh.write(content)
    with open(p(OUT + "/runs/%s.clock" % run16), "a", encoding="utf-8") as fh:
        fh.write("%s  checks %d  failed %d\n" % (clock, len(RESULTS), n_fail))
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
