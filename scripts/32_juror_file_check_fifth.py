#!/usr/bin/env python3
"""
32_juror_file_check_fifth.py -- checks the juror files and the index the
fifth-fix run issued, acting on exam-prep/REVIEW-4.md.

What it does
------------
  R  Rebuild. The four fifth-fix juror files are rebuilt in memory from the
     fourth-fix files by exam-prep/fifth-fix/make_fifth_fix_files.py, and
     must equal the issued files byte for byte.
  X  Removed. Every passage REVIEW-4 §2 requires removed is absent
     (whitespace-insensitive).
  N  No new number. Every number in a fifth-fix file already occurs in the
     fourth-fix file of the same name, except the line numbers of passages
     quoted for the first time (listed in NEW_NUMBERS and checked by Q).
  Q  Quotes. Every passage part d quotes is found in the cited lines of the
     cited file; the premise sentence of part d is checked against the
     audit's family table (scripts/29_identity_audit_exact.py, read as text,
     not imported or run).
  I  Index. Every row present once; the index carries no digit outside an
     identifier, a path, a line range of a reading list, a SHA-256 (or the
     word SHA-256), a rule reference, a section locator ("Part 1") or a
     date; no reading list names a forbidden file; the
     canteen book only by the line ranges the CONTENT file names; the
     union of "What you open" over a row's group equals the row's list
     (rows answered together go to the same jurors); earlier index
     versions match their stated SHA-256.
  U  Unchanged. Every file under exam-prep/ and scripts/ that the pre-run
     snapshot lists (exam_* scripts and bytecode excluded, as there) has the
     same SHA-256, except the index (re-issued; earlier version kept) and
     the three appended files, which must start with their pre-run bytes.
     No new file outside exam-prep/fifth-fix/ except this script.

Input   : the files named above (paths relative to the repository root).
Output  : exam-prep/fifth-fix/checks/juror-file-check-<run16>.md
          exam-prep/fifth-fix/checks/runs/<run16>.json   (append-only)
          --dry: prints, writes nothing.
Run number: SHA-256 over the contents of every input, keyed by its
          repository-relative path (not by absolute path, so the number does
          not depend on where the repository sits).
Rules   : RULES 19, 23, 29, 30, 32-34. No threshold, score or trading rule.
Run with PYTHONDONTWRITEBYTECODE=1 (the script also sets
sys.dont_write_bytecode before importing the builder).
"""
import datetime as dt
import hashlib
import importlib.util
import json
import os
import re
import shutil
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
EP = "exam-prep"
F4 = EP + "/fourth-fix/juror-questions/"
F5 = EP + "/fifth-fix/juror-questions/"
NAMES = ["JQ-N1.md", "JQ-CANTEEN-8.md", "JQ-R04-DATE.md", "JQ-R04-CONTENT.md"]
BUILDER = EP + "/fifth-fix/make_fifth_fix_files.py"
INDEX = EP + "/JUROR-QUESTIONS.md"
SNAP = EP + "/fifth-fix/pre-run-fingerprints.txt"
OUT = EP + "/fifth-fix/checks"
GATE = EP + "/third-fix/juror-questions/JQ-R04-GATE.md"
GATE_SHA = "55e7b95c9bc4beb7eb78418ed230270661d14ed92876bb13d047d1b853f816ce"
VERDICT_GATE = "decisions/2026-10-01-jq-r04-gate/verdict.md"
AUDIT = "scripts/29_identity_audit_exact.py"
EARLIER_INDEX = {
    EP + "/fifth-fix/JUROR-QUESTIONS-as-of-fourth-fix.md":
        "90c51c9e60f8c11a895b11cc6abc067504edb9e8abb11267502f56424c580dc0",
    EP + "/fourth-fix/JUROR-QUESTIONS-as-of-third-fix.md":
        "c1d3dfdeab36a40f3c2b2096b53c80d057603c3c07d1bfdeeb64f45fefa10720",
    EP + "/third-fix/JUROR-QUESTIONS-as-of-second-fix.md":
        "7020127c257b7addbae1fd6cbca0e4031accc3b28a4816980c5cd410532399d9",
}
# Appended files: pre-run size and SHA-256 of that prefix (read before
# appending, 2026-10-01, this run).
APPENDED = {
    EP + "/HANDED-FORWARD.md":
        (23037, "8ab30e59d2774e303199f26cff932914e980e2ff2773e7f97f0d36fbc4e8642b"),
    EP + "/VERDICT.md":
        (26243, "5ed3c26f56431a9c3705d100347f8a2c5162b01616f9200c4e6602e4aa243c4e"),
    EP + "/README.md":
        (5042, "03225075610a6844ebffe2ca18e965600cfdefb96d95e20f9233ab31175569fc"),
}
REISSUED = {INDEX}

# Passages REVIEW-4 §2 requires removed (file -> strings).
REMOVED = {
    "JQ-N1.md": [
        "that is the convention the calibration below used",
        "What the two ways do to the 1% boundary",
        "How large random variation alone is",
        "the 1% boundary ranges from 0.5458 to 0.6613",
    ],
    "JQ-CANTEEN-8.md": [
        "TACTICS 2 puts no minimum distance between two *calm* moments. None "
        "is imposed here.",
    ],
    "JQ-R04-DATE.md": [
        "The first run removed these columns from its blinded cards and said "
        "it was acting on a reading it could not settle alone.",
    ],
    "JQ-R04-CONTENT.md": [
        "| from the values before rounding | typical level",
        "| from the values before rounding | how many values repeat",
        "none that either attack finds when it is ranked from the values "
        "before rounding",
        "If your answer to part c permits ranking from the values before "
        "rounding",
        "What the second way does to the trade-count column's measured coin "
        "signature is in part a.",
        "with its measured signature named in the exam manifest",
        "if no permitted rendering removes a channel, the channel is named in "
        "the exam manifest with its number",
    ],
}
# Numbers allowed to be new, each with the reason; each is checked by Q.
NEW_NUMBERS = {"JQ-R04-CONTENT.md": {"55": "JQ-R04-GATE.md lines 55-57",
                                     "57": "JQ-R04-GATE.md lines 55-57",
                                     "64": "JQ-R04-GATE.md lines 64-66",
                                     "66": "JQ-R04-GATE.md lines 64-66",
                                     "72": "verdict.md line 72"}}
# Part d's quotations: (file, first line, last line, quoted text).
QUOTES = [
    (GATE, 55, 57, "If `ALL-removable` beats its chance line on the exam "
                   "cards, the cards are not blind and the gate has failed."),
    (GATE, 64, 66, "`ALL-removable` is every feature in the audit's current "
                   "list, minus the families that must stay on the card "
                   "because a frozen canteen rule or TACTICS requires them."),
    (VERDICT_GATE, 72, 72, "The gate fails if either the nearest-neighbour "
                           "attack or the pair AUC attack beats its own "
                           "RULES 12 chance line on the exam cards."),
]
CANTEEN_RANGES = "lines 112–120, 221–225, 245–246, 268–270 and 667–671 only"
FORBIDDEN_IN_LISTS = [r"REVIEW", r"VERDICT", r"HANDED-FORWARD", r"-FIX\.md",
                      r"criteria", r"/checks/", r"/probes/", r"/runs/",
                      r"/identity/", r"/collapse/", r"blind-proof",
                      r"R-04-blindness", r"N-1-collapse",
                      r"decisions-and-open", r"decisions/", r"LEDGER",
                      r"/second-fix/", r"/fourth-fix/juror-questions/",
                      r"review-\d"]


def rd(rel, mode="r"):
    p = os.path.join(REPO, rel)
    if mode == "rb":
        with open(p, "rb") as fh:
            return fh.read()
    with open(p, encoding="utf-8") as fh:
        return fh.read()


def sha_b(b):
    return hashlib.sha256(b).hexdigest()


def norm(t):
    t = re.sub(r"^> ?", "", t, flags=re.M)
    t = t.replace("**", "")
    return re.sub(r"\s+", " ", t).strip()


def numbers(t):
    return set(re.findall(r"\d+", t))


def main():
    dry = "--dry" in sys.argv
    checks = []

    def ck(cid, ok, detail):
        checks.append({"id": cid, "ok": bool(ok), "detail": detail})

    # ---- R · rebuild ------------------------------------------------------
    spec = importlib.util.spec_from_file_location(
        "make_fifth", os.path.join(REPO, BUILDER))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for n in NAMES:
        d = mod.Doc(rd(F4 + n))
        mod.EDITS[n](d)
        ck("R " + n, d.s == rd(F5 + n),
           "rebuilt from %s by the builder equals the issued file" % (F4 + n))

    # ---- X · removed passages --------------------------------------------
    for n, items in REMOVED.items():
        t5, t4 = norm(rd(F5 + n)), norm(rd(F4 + n))
        for s in items:
            ns = norm(s)
            ck("X " + n, ns in t4 and ns not in t5,
               "present in fourth-fix, absent in fifth-fix: %r" % s[:70])

    # ---- N · no new number -----------------------------------------------
    for n in NAMES:
        new = numbers(rd(F5 + n)) - numbers(rd(F4 + n))
        allowed = set(NEW_NUMBERS.get(n, {}))
        ck("N " + n, new <= allowed,
           "numbers not in the fourth-fix file: %s (allowed: %s)"
           % (sorted(new), sorted(allowed)))

    # ---- Q · quotations and the part d premise ----------------------------
    content5 = norm(rd(F5 + "JQ-R04-CONTENT.md"))
    for f, a, b, q in QUOTES:
        lines = rd(f).split("\n")[a - 1:b]
        ck("Q quote", norm(q) in norm("\n".join(lines)) and
           norm(q) in content5,
           "%s lines %d-%d contain the quotation, and part d carries it: %r"
           % (f, a, b, q[:60]))
    src = rd(AUDIT)
    m = re.search(r"FORCED_FAMILIES = \(([^)]*)\)", src)
    forced = re.findall(r'"([^"]+)"', m.group(1)) if m else []
    ck("Q forced list", forced == ["volatility-frozen", "funding-line",
                                   "p7-shape", "repeat-chg"],
       "FORCED_FAMILIES in %s: %s" % (AUDIT, forced))
    fam_block = src[src.index("FAMILIES = {"):src.index("}", src.index(
        "FAMILIES = {"))]
    fam = dict(re.findall(r'"([^"]+)":\s*\[([^\]]*)\]', fam_block))
    forced_prefixes = sorted(p for k in forced for p in
                             re.findall(r'"([^"]+)"', fam.get(k, "")))
    ck("Q forced prefixes", forced_prefixes ==
       ["funding:", "p7:price_pct", "p7:range_pct", "rep-chg:",
        "volatility:"],
       "feature prefixes left out of ALL-removable: %s" % forced_prefixes)
    rg = re.search(r"REPEAT_GROUP = \{(.*?)\}", src, re.S).group(1)
    chg_cols = [c for c, g in re.findall(r'"([^"]+)":\s*"([^"]+)"', rg)
                if g == "chg"]
    ck("Q rep-chg reads", chg_cols == ["chg%"],
       "columns feeding rep-chg: %s" % chg_cols)
    vol_src = re.findall(r'^\s*(ch = .*)$', src, re.M)
    ck("Q volatility reads", any('chg%' in v for v in vol_src),
       "volatility features are computed from: %s" % vol_src)
    p7_lines = [l.strip() for l in src.split("\n")
                if "p7:price_pct" in l or "p7:range_pct" in l]
    fund_lines = [l.strip() for l in src.split("\n") if '"funding:' in l]
    ck("Q p7/funding read no column",
       not any(re.search(r'col\[', l) for l in p7_lines + fund_lines),
       "the p7-shape and funding-line feature lines read no table column")
    ck("Q premise sentence",
       norm("everything it computes from the bitcoin and ethereum columns, "
            "the trade-count column, the price column and the other ranked "
            "columns is inside the row.") in content5,
       "part d's premise sentence is the one these checks support")

    # ---- I · index ---------------------------------------------------------
    idx = rd(INDEX)
    ids = ["JQ-N1-1", "JQ-N1-2", "JQ-N1-3", "JQ-N1-4", "JQ-CANTEEN-8",
           "JQ-R04-GATE", "JQ-R04-DATE-a", "JQ-R04-DATE-b", "JQ-R04-DATE-c",
           "JQ-R04-CONTENT-a", "JQ-R04-CONTENT-b", "JQ-R04-CONTENT-c",
           "JQ-R04-CONTENT-d", "JQ-B1"]
    rows = {}
    for line in idx.split("\n"):
        if line.startswith("| JQ-"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            rows.setdefault(cells[0], []).append(cells)
    ck("I rows", sorted(rows) == sorted(ids) and
       all(len(v) == 1 for v in rows.values()),
       "rows: %s" % sorted(rows))
    stripped = idx
    stripped = re.sub(r"`[^`]*`", "", stripped)            # paths, hashes
    stripped = re.sub(r"JQ-[A-Z0-9-]+[a-d]?", "", stripped)  # identifiers
    stripped = re.sub(r"RULES \d+(–\d+)?", "", stripped)
    stripped = re.sub(r"\d{4}-\d{2}-\d{2}", "", stripped)
    stripped = stripped.replace(CANTEEN_RANGES, "")
    stripped = stripped.replace("SHA-256", "")
    # section locators of the second column ("Part 1", "with 4a and 4b")
    stripped = re.sub(r"Part \d( \(with \da and \db\))?", "", stripped)
    stray = re.findall(r".{0,30}\d.{0,30}", stripped)
    ck("I no numbers", not stray, "digits outside allowed contexts: %s" % stray)
    gate_row = rows.get("JQ-R04-GATE", [[""] * 5])[0]
    ck("I GATE status", "ratified" in gate_row[4] and VERDICT_GATE in
       gate_row[4], "GATE row status: %s" % gate_row[4])
    for rid, cells in sorted(rows.items()):
        lst = cells[0][3]
        bad = [p for p in FORBIDDEN_IN_LISTS if re.search(p, lst)]
        ck("I list " + rid, not bad, "forbidden patterns in list: %s" % bad)
        if "canteen/" in lst:
            ck("I canteen " + rid, CANTEEN_RANGES in lst,
               "canteen given only by line ranges")
    m = re.search(r"`canteen/2026-09-19-sofia.md` lines (\d+)–(\d+) .*?lines "
                  r"(\d+)–(\d+) .*?lines (\d+)–(\d+) .*?lines (\d+)–(\d+) "
                  r".*?lines (\d+)–(\d+)", rd(F5 + "JQ-R04-CONTENT.md"), re.S)
    got = ("lines %s–%s, %s–%s, %s–%s, %s–%s and %s–%s only"
           % m.groups()) if m else None
    ck("I canteen ranges = CONTENT's", got == CANTEEN_RANGES,
       "CONTENT 'What you open' ranges: %s" % got)

    def opens(rel):
        t = rd(rel)
        sec = t[t.index("## What you open"):t.index("## What you decide")]
        found = set(re.findall(r"`([^`]+\.md)`", sec))
        if "- this file" in sec:
            found.add(rel)
        return found
    # Rows answered together go to the same jurors, so a row's list is
    # compared with the union of "What you open" over its group's files
    # (the index says so in its header).
    def target_of(rid):
        return re.findall(r"`([^`]+\.md)`", rows[rid][0][1])[0]
    for rid, cells in sorted(rows.items()):
        if rid in ("JQ-B1",):
            continue
        listed = set(re.findall(r"`([^`]+\.md)`", cells[0][3]))
        group = [rid] + [g.strip() for g in cells[0][2].split(",")
                         if g.strip() in rows]
        union = set()
        for g in group:
            union |= opens(target_of(g))
        ck("I opens " + rid, union == listed,
           "group's 'What you open' %s vs row %s"
           % (sorted(union), sorted(listed)))
    for rel, want in EARLIER_INDEX.items():
        ck("I earlier " + rel, sha_b(rd(rel, "rb")) == want,
           "SHA-256 equals the one the index states")
    ck("I GATE file unchanged", sha_b(rd(GATE, "rb")) == GATE_SHA,
       "JQ-R04-GATE.md SHA-256 %s" % GATE_SHA[:12])

    # ---- U · nothing earlier changed --------------------------------------
    snap = {}
    for line in rd(SNAP).split("\n"):
        if line.strip():
            h, p = line.split(None, 1)
            snap[p.strip()] = h
    changed = []
    for p, h in sorted(snap.items()):
        if p in REISSUED:
            continue
        b = rd(p, "rb")
        if p in APPENDED:
            size, ph = APPENDED[p]
            ok = sha_b(b[:size]) == ph == h and len(b) >= size
            ck("U appended " + p, ok,
               "first %d bytes hash to the pre-run SHA-256" % size)
        elif sha_b(b) != h:
            changed.append(p)
    ck("U unchanged", not changed, "files changed since the snapshot: %s"
       % changed)
    now = []
    for top in (EP, "scripts"):
        for dp, dn, fn in os.walk(os.path.join(REPO, top)):
            for f in fn:
                rel = os.path.relpath(os.path.join(dp, f), REPO)
                if (rel.startswith(EP + "/fifth-fix/") or f.endswith(".pyc")
                        or f.startswith("exam_")):
                    continue
                if rel not in snap:
                    now.append(rel)
    ck("U new files", sorted(now) == ["scripts/32_juror_file_check_fifth.py"],
       "new files outside exam-prep/fifth-fix/: %s" % sorted(now))

    # ---- run number, record -------------------------------------------------
    h = hashlib.sha256()
    inputs = ([F4 + n for n in NAMES] + [F5 + n for n in NAMES] +
              [BUILDER, INDEX, SNAP, GATE, VERDICT_GATE, AUDIT,
               "scripts/32_juror_file_check_fifth.py"] +
              sorted(EARLIER_INDEX))
    for rel in inputs:
        h.update(("%s:%s\n" % (rel, sha_b(rd(rel, "rb")))).encode())
    for rel, (size, ph) in sorted(APPENDED.items()):
        h.update(("%s:prefix:%d:%s\n" % (rel, size, ph)).encode())
    run_full = h.hexdigest()
    run16 = run_full[:16]
    failed = [c for c in checks if not c["ok"]]
    for c in checks:
        print("%s  %-40s %s" % ("ok  " if c["ok"] else "FAIL", c["id"],
                                c["detail"][:150]))
    print("run %s: %d checks, %d failed" % (run16, len(checks), len(failed)))
    if dry:
        sys.exit(1 if failed else 0)
    core = {"run": run16, "input_fingerprint": run_full,
            "inputs": {rel: sha_b(rd(rel, "rb")) for rel in inputs},
            "checks": checks, "failed": len(failed)}
    os.makedirs(os.path.join(REPO, OUT, "runs"), exist_ok=True)
    rec = os.path.join(REPO, OUT, "runs", run16 + ".json")
    body = json.dumps(core, indent=1, sort_keys=True, ensure_ascii=False)
    if os.path.exists(rec):
        with open(rec, encoding="utf-8") as fh:
            old = fh.read()
        if old != body:
            sys.exit("STOP: run %s already recorded with different content "
                     "(RULES 30)" % run16)
        sys.stderr.write("run %s already recorded\n" % run16)
        sys.exit(1 if failed else 0)
    with open(rec, "w", encoding="utf-8") as fh:
        fh.write(body)
    clock = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    free = shutil.disk_usage(REPO).free
    L = ["# Juror-file check (fifth-fix) — run `%s`" % run16, "",
         "Clock (system, RULES 23): %s · free disk %d bytes · input "
         "fingerprint `%s`" % (clock, free, run_full), "",
         "%d checks, %d failed." % (len(checks), len(failed)), "",
         "| result | check | detail |", "|---|---|---|"]
    for c in checks:
        L.append("| %s | %s | %s |" % ("ok" if c["ok"] else "**FAIL**",
                                       c["id"], c["detail"].replace("|", "/")))
    with open(os.path.join(REPO, OUT, "juror-file-check-%s.md" % run16), "w",
              encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
