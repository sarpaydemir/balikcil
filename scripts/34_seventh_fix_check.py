#!/usr/bin/env python3
"""34_seventh_fix_check.py — checks for the seventh-fix run (exam-prep).

What it does
    Checks, by script, the claims the seventh-fix run makes about the files it
    wrote or left alone:
      S  every file in the pre-run snapshot of `exam-prep/` is unchanged, except
         the re-issued index and three appended files, whose pre-run bytes are
         still their prefix; every non-`exam_*` script and the rule and verdict
         files in the scripts snapshot are unchanged
      N  no new file under `exam-prep/` except `USER-QUESTIONS.md` and files in
         `exam-prep/seventh-fix/`; no new script except this one
      L  the three juror files a jury is using or waiting on, and the withdrawn
         JQ-R04-CONTENT-d file, have the SHA-256 the instruction / sixth-fix
         fingerprints give
      V  every earlier version of the index is where the index says, with the
         SHA-256 it says
      I  the index: every row once; each row's status; reading lists of every
         row except JQ-R04-CONTENT-d unchanged; no number that the sixth-fix
         index did not carry (SHA-256 values aside); no option or question
         sentence of any juror file
      U  `exam-prep/USER-QUESTIONS.md`: every quotation is in its cited lines
         and in the file; every number in it is on a declared list; no decimal
         figure; the four forced families are the audit's; every family prefix
         of the audit maps to a field TACTICS 3 lists
Input
    `exam-prep/` (snapshot files, index, user questions, juror files, the three
    appended files), `RULES.md`, `TACTICS.md`, the two ratified verdicts,
    `scripts/29_identity_audit_exact.py` (parsed with `ast` and read as text,
    never imported), the names (only) of files in `scripts/`. Files whose names
    begin `exam_` are never opened.
Output
    `exam-prep/seventh-fix/checks/seventh-fix-check-<run>.md` and
    `exam-prep/seventh-fix/checks/runs/<run>.json`, plus `<run>.clock` (system
    clock of the first recording). `--dry` writes nothing.
Rules implemented
    RULES 29–30: the run number is the SHA-256 (first 16 hex digits) of this
    script and of every input's bytes; records are append-only; different
    content under an existing run number stops the script. RULES 23: the clock
    is read from the system. No randomness is used (no seed needed).
Run
    PYTHONDONTWRITEBYTECODE=1 python3 -B scripts/34_seventh_fix_check.py [--dry] [--show]
    (--show prints every check, not only failures; it changes no output file)
"""
import ast
import datetime
import hashlib
import json
import os
import re
import sys

sys.dont_write_bytecode = True

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EP = "exam-prep"
SEV = "exam-prep/seventh-fix"
OUT = "exam-prep/seventh-fix/checks"

# ---- constants (each from a named source; none is a threshold) ----------
# Pre-run snapshots taken by this run at 2026-10-01T23:31Z before any write.
SNAP_EP = SEV + "/pre-run-fingerprints.txt"
SNAP_SCRIPTS = SEV + "/pre-run-scripts-fingerprints.txt"
# Files this run re-issues (whole) or appends to (prefix must be pre-run).
REISSUED = {"exam-prep/JUROR-QUESTIONS.md"}
APPENDED = {"exam-prep/VERDICT.md", "exam-prep/HANDED-FORWARD.md",
            "exam-prep/README.md"}
NEW_ALLOWED_FILES = {"exam-prep/USER-QUESTIONS.md"}
NEW_ALLOWED_SCRIPTS = {"scripts/34_seventh_fix_check.py"}
# SHA-256 from the seventh-fix instruction (CARRIES) and
# exam-prep/sixth-fix/FINGERPRINTS.md (the other three).
LOCKED = {
    "exam-prep/sixth-fix/juror-questions/JQ-R04-CARRIES.md":
        "7532779b81422a0ef5833771a351f80fd2bfccd7968ce0c75a15698e76f0d19f",
    "exam-prep/sixth-fix/juror-questions/JQ-R04-DATE.md":
        "c053d81449411ae9cdb7d83376d74c21172409dd214360106533115e6452b42f",
    "exam-prep/sixth-fix/juror-questions/JQ-R04-CONTENT.md":
        "95d05d46c8e496e02ae63f2895661f668b332857c288c562e56cfcc2d5fdc0ab",
    "exam-prep/sixth-fix/juror-questions/JQ-R04-CONTENT-d.md":
        "963aeb9f92d69716096acfc5759999bdd9133d9aa933e0b04a0ec7684057ada1",
}
INDEX = "exam-prep/JUROR-QUESTIONS.md"
OLD_INDEX = SEV + "/JUROR-QUESTIONS-as-of-sixth-fix.md"
USERQ = "exam-prep/USER-QUESTIONS.md"
AUDIT = "scripts/29_identity_audit_exact.py"
AUDIT_SHA = "cfc4bdcb6f1ee65430ac08fad0d085ff6e83510ac4d741145aa32cde3487d03f"
JUROR_FILES = [
    "exam-prep/fifth-fix/juror-questions/JQ-N1.md",
    "exam-prep/fifth-fix/juror-questions/JQ-CANTEEN-8.md",
    "exam-prep/third-fix/juror-questions/JQ-R04-GATE.md",
    "exam-prep/third-fix/juror-questions/JQ-B1.md",
    "exam-prep/sixth-fix/juror-questions/JQ-R04-CARRIES.md",
    "exam-prep/sixth-fix/juror-questions/JQ-R04-DATE.md",
    "exam-prep/sixth-fix/juror-questions/JQ-R04-CONTENT.md",
    "exam-prep/sixth-fix/juror-questions/JQ-R04-CONTENT-d.md",
]
ROW_IDS = ["JQ-N1-1", "JQ-N1-2", "JQ-N1-3", "JQ-N1-4", "JQ-CANTEEN-8",
           "JQ-R04-GATE", "JQ-R04-CARRIES-a", "JQ-R04-CARRIES-b",
           "JQ-R04-DATE-a", "JQ-R04-DATE-b", "JQ-R04-DATE-c",
           "JQ-R04-CONTENT-a", "JQ-R04-CONTENT-b", "JQ-R04-CONTENT-c",
           "JQ-R04-CONTENT-d", "JQ-B1"]
N1_VERDICT = "decisions/2026-10-01-jq-n1-canteen-8/verdict.md"
GATE_VERDICT = "decisions/2026-10-01-jq-r04-gate/verdict.md"
# Required status words per row (the true status; sources: both verdict
# files read RATIFIED; the instruction says the CARRIES jurors are answering
# now; REVIEW-6 §1; this run's withdrawal of JQ-R04-CONTENT-d).
STATUS_MUST = {
    **{r: ["**ratified**", N1_VERDICT] for r in
       ["JQ-N1-1", "JQ-N1-2", "JQ-N1-3", "JQ-N1-4", "JQ-CANTEEN-8"]},
    "JQ-R04-GATE": ["**ratified**", GATE_VERDICT],
    "JQ-R04-CARRIES-a": ["being answered", "ruled fit by the sixth review"],
    "JQ-R04-CARRIES-b": ["being answered", "ruled fit by the sixth review"],
    **{r: ["**waiting", "ruled fit by the sixth review"] for r in
       ["JQ-R04-DATE-a", "JQ-R04-DATE-b", "JQ-R04-DATE-c",
        "JQ-R04-CONTENT-a", "JQ-R04-CONTENT-b", "JQ-R04-CONTENT-c"]},
    "JQ-R04-CONTENT-d": ["**withdrawn**", "exam-prep/USER-QUESTIONS.md"],
    "JQ-B1": ["**withdrawn**"],
}
# Quotations in USER-QUESTIONS.md: (file, first line, last line, text).
QUOTES = [
    ("RULES.md", 41, 41, "In the exam the coin name and the date are hidden."),
    ("TACTICS.md", 102, 102, "the coin name"),
    ("TACTICS.md", 103, 103, "the date and time"),
    ("TACTICS.md", 104, 104,
     "the price itself (converted to a number starting from 100)"),
    ("TACTICS.md", 105, 105, "the coin name inside announcements"),
    ("TACTICS.md", 106, 106, "the Wikipedia number itself (given as a ratio "
     "to the coin's own average)"),
    ("TACTICS.md", 107, 107, "the date in the release calendar"),
    ("TACTICS.md", 56, 56, "price, volume, trade count, taker buy/sell "
     "pressure"),
    ("TACTICS.md", 61, 61, "bitcoin and ethereum, over the same hours"),
    ("RULES.md", 51, 52, "The chance line is not invented. The answers are "
     "shuffled 1,000 times, and the real result must fall inside the best "
     "1%."),
    (GATE_VERDICT, 72, 72, "The gate fails if either the nearest-neighbour "
     "attack or the pair AUC attack beats its own RULES 12 chance line on the "
     "exam cards."),
    ("exam-prep/third-fix/juror-questions/JQ-R04-GATE.md", 64, 66,
     "every feature in the audit's current list, minus the families that must "
     "stay on the card because a frozen canteen rule or TACTICS requires "
     "them"),
    ("RULES.md", 3, 4, "These rules do not change. If one must change, the "
     "user is asked first, and then it is written into `LEDGER.md`."),
    ("RULES.md", 119, 121, "A juror decides procedure and definition only: "
     "never a trading rule, never a threshold or score, and never a change to "
     "a rule in this file."),
    ("RULES.md", 34, 35, "The rule is written first, the result is opened "
     "second. A rule is not changed after looking at a result."),
    ("TACTICS.md", 94, 94, "Then the canteen book freezes"),
]
# Line citations in USER-QUESTIONS.md that point at a range, not a quotation
# (TACTICS 3's list spans 55–62; TACTICS 6's hidden list 101–107).
RANGE_CITES = [("TACTICS.md", 55, 62, "price, volume, trade count"),
               ("TACTICS.md", 101, 107, "What is hidden")]
# Every number allowed in USER-QUESTIONS.md, with its source.
ALLOWED_NUMBERS = {
    "2026", "10", "01",                  # the date of writing / verdict path
    "23",                                # RULES 23 (clock read), header
    "04",                                # in the identifiers JQ-R04-…
    "3", "4",                            # RULES.md lines 3–4; TACTICS 3
    "6", "9", "12", "33",                # rule numbers RULES 6, 9, 12, 33
    "34", "35", "41", "51", "52",        # RULES.md line numbers cited
    "119", "121",                        # RULES.md lines 119–121
    "55", "62", "101", "107",            # TACTICS.md line ranges cited
    "64", "66", "72",                    # GATE file lines, verdict line
    "94",                                # TACTICS.md line 94 (book freezes)
    "100",                               # TACTICS.md line 104 quotation
    "1,000", "1",                        # RULES 12 quotation; "U-1", part 1
    "2",                                 # part 2
    "7",                                 # TACTICS 3 "the previous 7 days"
    "24",                                # TACTICS 3 "the 24 hours"
}
# Family prefixes of the audit and the TACTICS 3 field each is computed from
# (TACTICS.md lines 50–51 and 55–62; read from `card_features()`).
PREFIX_FIELD = {
    "price:": "price (line 56)", "volatility:": "price (line 56)",
    "volume:": "volume (line 56)", "p7:log_avg_vol": "previous-7-day summary "
    "(lines 50–51)", "trades:": "trade count (line 56)",
    "p7:log_avg_trades": "previous-7-day summary (lines 50–51)",
    "openint:": "open interest (line 57)", "depth:": "order book depth "
    "(line 59)", "ratio:": "long/short ratios (line 57) and taker buy/sell "
    "pressure (line 56)", "takerbuy:": "taker buy/sell pressure (line 56)",
    "funding:": "funding rate (line 58)", "wikipedia:": "Wikipedia (line 63)",
    "p7:price_pct": "previous-7-day summary (lines 50–51)",
    "p7:range_pct": "previous-7-day summary (lines 50–51)",
    "btceth:": "bitcoin and ethereum (line 61)", "shape:": "volume, trade "
    "count, open interest, depth, ratios (lines 56–59)",
    "rep-close:": "price (line 56)", "rep-chg:": "price (line 56)",
    "rep-volume:": "volume (line 56)", "rep-trades:": "trade count (line 56)",
    "rep-takerbuy:": "taker buy/sell pressure (line 56)",
    "rep-openint:": "open interest (line 57)",
    "rep-ratio:": "long/short ratios (line 57)",
    "rep-depth:": "order book depth (line 59)",
    "rep-btceth:": "bitcoin and ethereum (line 61)",
    "gran-close:": "price (line 56)",
}
FORCED_EXPECTED = ("volatility-frozen", "funding-line", "p7-shape",
                   "repeat-chg")


def die(msg):
    sys.stderr.write("STOP: %s\n" % msg)
    sys.exit(2)


def p(rel):
    return os.path.join(ROOT, rel)


def raw(rel):
    if os.path.basename(rel).startswith("exam_"):
        die("refusing to open %s" % rel)
    with open(p(rel), "rb") as fh:
        return fh.read()


def sha(b):
    return hashlib.sha256(b).hexdigest()


def norm(s):
    return re.sub(r"\s+", " ", s.replace("**", "").replace("> ", " ")).strip()


def lines_of(rel, a, b):
    return raw(rel).decode("utf-8").split("\n")[a - 1:b]


def read_snapshot(rel):
    out = {}
    for ln in raw(rel).decode("utf-8").splitlines():
        h, path = ln.split("  ", 1)
        out[path] = h
    return out


def ep_listing():
    """Every file under exam-prep/, except this run's own folder (whose files
    are named in checks below), as relative paths."""
    out = []
    for d, dirs, files in os.walk(p(EP)):
        dirs.sort()
        for f in sorted(files):
            rel = os.path.relpath(os.path.join(d, f), ROOT)
            if rel.startswith(SEV + "/"):
                continue
            out.append(rel)
    return sorted(out)


def script_names():
    return sorted("scripts/" + n for n in os.listdir(p("scripts"))
                  if os.path.isfile(p("scripts/" + n))
                  and not n.startswith("exam_"))


def index_rows(text):
    rows = {}
    for ln in text.split("\n"):
        m = re.match(r"\| (JQ-[A-Za-z0-9-]+) \|", ln)
        if m:
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            rows.setdefault(m.group(1), []).append(cells)
    return rows


def numbers(text):
    t = re.sub(r"[0-9a-f]{64}", " ", text)
    return set(re.findall(r"\d[\d,]*\d|\d", t))


def option_sentences(text):
    out = []
    for ln in text.split("\n"):
        m = re.match(r"\s*- \*\*([^*]+)\*\* — (.+)", ln)
        if m:
            out.append(norm(m.group(2))[:40])
        m = re.match(r"\*\*Question [a-z0-9]+\.\*\* (.+)", ln)
        if m:
            out.append(norm(m.group(1))[:40])
    return [o for o in out if len(o) >= 20]


def main():
    dry = "--dry" in sys.argv[1:]
    os.chdir(ROOT)
    checks = []

    def check(tag, name, ok, detail=""):
        checks.append({"tag": tag, "name": name, "ok": bool(ok),
                       "detail": detail})

    inputs = {}

    def use(rel, data=None):
        b = raw(rel) if data is None else data
        inputs[rel if data is None else rel + " (prefix)"] = sha(b)
        return b

    use("scripts/34_seventh_fix_check.py")
    snap = read_snapshot(SNAP_EP)
    use(SNAP_EP)
    ssnap = read_snapshot(SNAP_SCRIPTS)
    use(SNAP_SCRIPTS)

    # S — snapshot
    changed, missing = [], []
    for rel, h in sorted(snap.items()):
        if not os.path.exists(p(rel)):
            missing.append(rel)
            continue
        if rel in APPENDED:
            continue
        b = use(rel)
        if rel in REISSUED:
            continue
        if sha(b) != h:
            changed.append(rel)
    check("S", "no file of the pre-run exam-prep snapshot is missing",
          not missing, ", ".join(missing))
    check("S", "every pre-run exam-prep file is unchanged (index and three "
          "appended files aside)", not changed, ", ".join(changed))
    for rel in sorted(APPENDED):
        whole = raw(rel)
        pre = None
        size = None
        # pre-run size: the prefix whose hash is the snapshot hash
        for n in range(len(whole), -1, -1):
            if sha(whole[:n]) == snap[rel]:
                pre, size = whole[:n], n
                break
        use(rel, pre if pre is not None else b"")
        check("S", "%s: pre-run bytes are its prefix" % rel, pre is not None,
              "prefix %s bytes" % size)
    sch = []
    for rel, h in sorted(ssnap.items()):
        if sha(use(rel)) != h:
            sch.append(rel)
    check("S", "every non-exam_ script, RULES.md, TACTICS.md and both "
          "ratified verdicts unchanged", not sch, ", ".join(sch))

    # N — new files
    listing = ep_listing()
    inputs["(listing of exam-prep/)"] = sha("\n".join(listing).encode())
    new = [r for r in listing if r not in snap]
    check("N", "no new exam-prep file outside seventh-fix/ except "
          "USER-QUESTIONS.md", set(new) <= NEW_ALLOWED_FILES, ", ".join(new))
    names = script_names()
    inputs["(names in scripts/, exam_* excluded)"] = sha(
        "\n".join(names).encode())
    newscripts = [n for n in names if n not in ssnap]
    check("N", "no new script except this one",
          set(newscripts) <= NEW_ALLOWED_SCRIPTS, ", ".join(newscripts))

    # L — locked files
    for rel, h in sorted(LOCKED.items()):
        check("L", "%s unchanged" % rel, sha(use(rel)) == h, h[:12])

    # V — earlier index versions as the index names them
    idx = use(INDEX).decode("utf-8")
    old = use(OLD_INDEX).decode("utf-8")
    pairs = re.findall(r"`(exam-prep/[^`]*JUROR-QUESTIONS-as-of-[^`]+)`"
                       r"\s*(?:\(SHA-256\s*`|\(SHA-256\n`|\(SHA-256 `)?"
                       r"\s*`?([0-9a-f]{64})?", idx)
    found = re.findall(r"`(exam-prep/[^`]+JUROR-QUESTIONS-as-of-[^`]+)`"
                       r"[^`]*?`([0-9a-f]{64})`", idx, flags=re.S)
    check("V", "the index names five earlier versions with SHA-256",
          len(found) == 5, "%d found" % len(found))
    for rel, h in found:
        check("V", "%s has the SHA-256 the index gives" % rel,
              sha(use(rel)) == h, h[:12])
    check("V", "the sixth-fix index kept byte for byte",
          sha(old.encode("utf-8")) == snap[INDEX], snap[INDEX][:12])
    del pairs

    # I — index
    rows, orows = index_rows(idx), index_rows(old)
    for r in ROW_IDS:
        check("I", "row %s appears once" % r, len(rows.get(r, [])) == 1)
    check("I", "no row the list does not name", set(rows) == set(ROW_IDS),
          ", ".join(sorted(set(rows) - set(ROW_IDS))))
    for r, musts in STATUS_MUST.items():
        st = rows[r][0][4] if r in rows else ""
        check("I", "row %s status carries %s" % (r, " + ".join(musts)),
              all(m in st for m in musts))
    for r in ROW_IDS:
        if r == "JQ-R04-CONTENT-d" or r not in rows or r not in orows:
            continue
        check("I", "row %s: file, group and reading list unchanged" % r,
              rows[r][0][:4] == orows[r][0][:4])
    newnum = numbers(idx) - numbers(old)
    check("I", "the index carries no number the sixth-fix index did not "
          "(SHA-256 values aside)", not newnum, ", ".join(sorted(newnum)))
    leaks, tested = [], 0
    for jf in JUROR_FILES:
        for o in option_sentences(use(jf).decode("utf-8")):
            tested += 1
            if o in norm(idx):
                leaks.append("%s: %s" % (jf, o))
    check("I", "no option or question sentence of any juror file in the "
          "index", not leaks and tested > 0,
          "%d sentences tested; %s" % (tested, "; ".join(leaks)))

    # U — user questions
    uq = use(USERQ).decode("utf-8")
    nuq = norm(uq)
    for rel, a, b, q in QUOTES:
        src = norm(" ".join(lines_of(rel, a, b)).replace("- ", ""))
        src2 = norm(" ".join(x.strip().lstrip("-").strip()
                             for x in lines_of(rel, a, b)))
        insrc = norm(q) in src or norm(q) in src2
        inuq = norm(q) in nuq
        cite = "%s line" % rel.split("/")[-1]
        check("U", "quotation in %s %d–%d and in USER-QUESTIONS.md: %s…"
              % (rel, a, b, q[:30]), insrc and inuq,
              "source %s; user file %s; %s" % (insrc, inuq, cite))
    for rel, a, b, probe in RANGE_CITES:
        src = norm(" ".join(lines_of(rel, a, b)))
        check("U", "cited range %s %d–%d holds %r" % (rel, a, b, probe),
              probe in src)
    nums = numbers(uq)
    extra = sorted(nums - ALLOWED_NUMBERS)
    check("U", "every number in USER-QUESTIONS.md is on the declared list",
          not extra, ", ".join(extra))
    dec = re.findall(r"\d+\.\d+", re.sub(r"[0-9a-f]{64}", " ", uq))
    check("U", "no decimal figure in USER-QUESTIONS.md", not dec,
          ", ".join(dec))
    ids = sorted(set(re.findall(r"JQ-[A-Za-z0-9-]+", uq)))
    check("U", "identifiers in USER-QUESTIONS.md limited to the withdrawn row "
          "and the GATE file path", set(ids) <= {"JQ-R04-CONTENT-d",
                                                  "JQ-R04-GATE.md",
                                                  "JQ-R04-GATE"},
          ", ".join(ids))
    for w in ("recommend", "should choose", "we suggest", "better answer"):
        hits = [m.start() for m in re.finditer(w, uq.lower())]
        allowed = (w == "recommend" and
                   uq.lower().count("nothing here recommends an answer") +
                   uq.lower().count("not recommending it") == len(hits))
        check("U", "no recommending word %r (outside the no-recommendation "
              "notice)" % w, not hits or allowed, "%d hits" % len(hits))
    asrc = use(AUDIT)
    check("U", "audit SHA-256 is the one HANDED-FORWARD names",
          sha(asrc) == AUDIT_SHA, sha(asrc)[:12])
    tree = ast.parse(asrc.decode("utf-8"))
    fam, forced = None, None
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and \
                isinstance(node.targets[0], ast.Name):
            if node.targets[0].id == "FAMILIES":
                fam = ast.literal_eval(node.value)
            if node.targets[0].id == "FORCED_FAMILIES":
                forced = ast.literal_eval(node.value)
    check("U", "FORCED_FAMILIES is the four families the user file and "
          "HANDED-FORWARD name", tuple(forced or ()) == FORCED_EXPECTED,
          repr(forced))
    prefixes = sorted({x for v in (fam or {}).values() for x in v})
    unmapped = [x for x in prefixes if x not in PREFIX_FIELD]
    check("U", "every family prefix of the audit maps to a field TACTICS 3 "
          "lists (%d prefixes)" % len(prefixes), not unmapped,
          ", ".join(unmapped))
    src_txt = asrc.decode("utf-8")
    cf = src_txt[src_txt.index("def card_features("):
                 src_txt.index("def _exact_number(")]
    keys = set(re.findall(r'f\["([a-z0-9-]+:)', cf))
    keys |= {"rep-"}  # rep-%s keys are built by format; see REPEAT_GROUP
    keys.discard("rep-")
    uncovered = [k for k in sorted(keys)
                 if not any(x.startswith(k) or k.startswith(x)
                            for x in prefixes)]
    check("U", "every feature key prefix written in card_features() is "
          "covered by a family prefix", not uncovered, ", ".join(uncovered))
    tac = raw("TACTICS.md").decode("utf-8").split("\n")
    check("U", "TACTICS.md line 63 is the Wikipedia line (for the mapping)",
          "Wikipedia" in tac[62], tac[62].strip()[:40])
    check("U", "the four forced groups are described in USER-QUESTIONS.md",
          all(s in nuq for s in (
              "the column of hourly price changes",
              "how many values repeat in that same column",
              "the funding line",
              "the price change and the high–low range printed in the "
              "one-line summary of the previous 7 days")))

    # run number and record
    blob = "\n".join("%s %s" % (k, inputs[k]) for k in sorted(inputs))
    run = sha(blob.encode())[:16]
    nfail = sum(1 for c in checks if not c["ok"])
    rep = ["# Seventh-fix check — run `%s`" % run, "",
           "Script: `scripts/34_seventh_fix_check.py`. Run number: the first "
           "16 hex digits of the SHA-256 over the sorted list of inputs and "
           "their SHA-256 below (RULES 29). %d checks, %d ok, %d failed."
           % (len(checks), len(checks) - nfail, nfail), "",
           "| tag | check | result | detail |", "|---|---|---|---|"]
    for c in checks:
        rep.append("| %s | %s | %s | %s |" % (
            c["tag"], c["name"].replace("|", "/"),
            "ok" if c["ok"] else "**FAIL**",
            c["detail"].replace("|", "/")))
    rep += ["", "## Inputs (%d)" % len(inputs), ""]
    rep += ["- `%s` `%s`" % (k, inputs[k]) for k in sorted(inputs)]
    report = ("\n".join(rep) + "\n").encode("utf-8")
    js = (json.dumps({"run": run, "checks": checks, "inputs": inputs},
                     indent=1, sort_keys=True) + "\n").encode("utf-8")
    print("run %s: %d checks, %d failed" % (run, len(checks), nfail))
    for c in checks:
        if not c["ok"] or "--show" in sys.argv[1:]:
            print("%s %s %s — %s" % ("ok  " if c["ok"] else "FAIL", c["tag"],
                                     c["name"], c["detail"]))
    if dry:
        print("--dry: nothing written")
        return 1 if nfail else 0
    os.makedirs(p(OUT + "/runs"), exist_ok=True)
    targets = [(OUT + "/seventh-fix-check-%s.md" % run, report),
               (OUT + "/runs/%s.json" % run, js)]
    for rel, data in targets:
        if os.path.exists(p(rel)):
            if raw(rel) != data:
                die("%s exists with different content (RULES 30)" % rel)
    for rel, data in targets:
        if not os.path.exists(p(rel)):
            with open(p(rel), "wb") as fh:
                fh.write(data)
    clk = OUT + "/runs/%s.clock" % run
    if not os.path.exists(p(clk)):
        now = datetime.datetime.now(datetime.timezone.utc)
        with open(p(clk), "w", encoding="utf-8") as fh:
            fh.write("first recorded %s (system clock)\n"
                     % now.strftime("%Y-%m-%dT%H:%M:%SZ"))
    print("recorded under %s" % OUT)
    return 1 if nfail else 0


if __name__ == "__main__":
    sys.exit(main())
