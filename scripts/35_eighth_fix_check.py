#!/usr/bin/env python3
"""35_eighth_fix_check.py — checks for the eighth-fix run (exam-prep).

What it does
    Checks, by script, the claims the eighth-fix run makes about the files it
    wrote or left alone:
      S  every file in the pre-run snapshot of `exam-prep/` is unchanged,
         except the re-issued index, `USER-QUESTIONS.md` (one inserted block;
         removing it gives the pre-run bytes) and three appended files (their
         pre-run bytes are still their prefix); every non-`exam_*` script in
         the scripts snapshot is unchanged
      N  no new file under `exam-prep/` outside `exam-prep/eighth-fix/`; no
         new script except this one
      L  the four sixth-fix juror files and the four ratified verdicts have
         the SHA-256 recorded at the start of this run
      V  every earlier version of the index is where the index says, with the
         SHA-256 it says; the byte copies of the seventh-fix index and user
         file equal the pre-run snapshot
      I  the index: every row once; each row's true status, with its verdict
         file where ratified; each named verdict file exists and reads
         RATIFIED; reading lists unchanged except JQ-R04-CONTENT-d's; no
         number the seventh-fix index did not carry (SHA-256 values aside);
         no option or question sentence of any juror file, the new one
         included
      D  the new JQ-R04-CONTENT-d juror file: reading list; every quotation in
         its cited lines and in the file; nothing of a verdict beyond the
         outcome (no split, no juror reasoning); no path into `exam-prep/`,
         no review, user-question, working-file or withdrawal mention; no
         ground of the four forced families; every number on a declared
         list; no decimal figure; no recommending word; its five answers;
         its four stops, and the same four in HANDED-FORWARD; its
         statements about the audit true of the code (forced families,
         inside-set fields, one field per feature, nothing from the release
         line or announcements, the empty-set message)
      U  `USER-QUESTIONS.md` carries the superseded block once and U-1's text
         unchanged
      H  the HANDED-FORWARD eighth-fix section has A-0.1, A-0.4 step 1,
         A-0.9 and C-5, each with a check line
Input
    `exam-prep/` (snapshot files, index, user questions, juror files, the
    prefixes of the appended files), `RULES.md`, `TACTICS.md`, the four
    ratified verdicts, `scripts/29_identity_audit_exact.py` (parsed with
    `ast` and read as text, never imported), the names (only) of files in
    `scripts/`. Files whose names begin `exam_` are never opened.
Output
    `exam-prep/eighth-fix/checks/eighth-fix-check-<run>.md` and
    `exam-prep/eighth-fix/checks/runs/<run>.json`, plus `<run>.clock` (system
    clock of the first recording). `--dry` writes nothing.
Rules implemented
    RULES 29–30: the run number is the SHA-256 (first 16 hex digits) of this
    script and of every input's bytes; records are append-only; different
    content under an existing run number stops the script. RULES 23: the
    clock is read from the system. No randomness is used (no seed needed).
Run
    PYTHONDONTWRITEBYTECODE=1 python3 -B scripts/35_eighth_fix_check.py [--dry] [--show]
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
EIG = "exam-prep/eighth-fix"
OUT = "exam-prep/eighth-fix/checks"

# ---- constants (each from a named source; none is a threshold) ----------
# Pre-run snapshots taken by this run at 2026-10-02T00:04:30Z, before any write.
SNAP_EP = EIG + "/pre-run-fingerprints.txt"
SNAP_SCRIPTS = EIG + "/pre-run-scripts-fingerprints.txt"
INDEX = "exam-prep/JUROR-QUESTIONS.md"
USERQ = "exam-prep/USER-QUESTIONS.md"
HF = "exam-prep/HANDED-FORWARD.md"
APPENDED = {"exam-prep/VERDICT.md", HF, "exam-prep/README.md"}
OLD_INDEX = EIG + "/JUROR-QUESTIONS-as-of-seventh-fix.md"
OLD_USERQ = EIG + "/USER-QUESTIONS-as-of-seventh-fix.md"
NEWD = EIG + "/juror-questions/JQ-R04-CONTENT-d.md"
NEW_ALLOWED_SCRIPTS = {"scripts/35_eighth_fix_check.py"}
GATE_V = "decisions/2026-10-01-jq-r04-gate/verdict.md"
N1_V = "decisions/2026-10-01-jq-n1-canteen-8/verdict.md"
CAR_V = "decisions/2026-10-01-jq-r04-carries/verdict.md"
DC_V = "decisions/2026-10-01-jq-r04-date-content/verdict.md"
# SHA-256 read by this run at 2026-10-02T00:05Z (sha256sum), before any write.
LOCKED = {
    "exam-prep/sixth-fix/juror-questions/JQ-R04-CARRIES.md":
        "7532779b81422a0ef5833771a351f80fd2bfccd7968ce0c75a15698e76f0d19f",
    "exam-prep/sixth-fix/juror-questions/JQ-R04-DATE.md":
        "c053d81449411ae9cdb7d83376d74c21172409dd214360106533115e6452b42f",
    "exam-prep/sixth-fix/juror-questions/JQ-R04-CONTENT.md":
        "95d05d46c8e496e02ae63f2895661f668b332857c288c562e56cfcc2d5fdc0ab",
    "exam-prep/sixth-fix/juror-questions/JQ-R04-CONTENT-d.md":
        "963aeb9f92d69716096acfc5759999bdd9133d9aa933e0b04a0ec7684057ada1",
    GATE_V: "2c0bfd3defa8a70009b096675b4d65417c512b7490700434738ebbc6b8058e2d",
    N1_V: "aa15ac0dbaaefec007dfb9890189e4f1a24fa949fcfece1fb7efce4459573305",
    CAR_V: "514a8d45038d3d7ad2feba3479c58d6e1da8e50358c799203f35b22cc246050a",
    DC_V: "d465a0d37366c10249eea2492f5a27b23f4c4eaf7811f2a4b0aa7873132fb769",
}
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
    NEWD,
]
ROW_IDS = ["JQ-N1-1", "JQ-N1-2", "JQ-N1-3", "JQ-N1-4", "JQ-CANTEEN-8",
           "JQ-R04-GATE", "JQ-R04-CARRIES-a", "JQ-R04-CARRIES-b",
           "JQ-R04-DATE-a", "JQ-R04-DATE-b", "JQ-R04-DATE-c",
           "JQ-R04-CONTENT-a", "JQ-R04-CONTENT-b", "JQ-R04-CONTENT-c",
           "JQ-R04-CONTENT-d", "JQ-B1"]
# True status of each row (sources: the four verdict files read RATIFIED;
# the new d file is written by this run and not reviewed; JQ-B1 withdrawn).
STATUS_MUST = {
    **{r: ["**ratified**", N1_V] for r in
       ["JQ-N1-1", "JQ-N1-2", "JQ-N1-3", "JQ-N1-4", "JQ-CANTEEN-8"]},
    "JQ-R04-GATE": ["**ratified**", GATE_V],
    "JQ-R04-CARRIES-a": ["**ratified**", CAR_V],
    "JQ-R04-CARRIES-b": ["**ratified**", CAR_V],
    **{r: ["**ratified**", DC_V] for r in
       ["JQ-R04-DATE-a", "JQ-R04-DATE-b", "JQ-R04-DATE-c",
        "JQ-R04-CONTENT-a", "JQ-R04-CONTENT-b", "JQ-R04-CONTENT-c"]},
    "JQ-R04-CONTENT-d": ["**written — not yet reviewed, not commissioned**",
                         "kept unchanged as a record"],
    "JQ-B1": ["**withdrawn**"],
}
D_ROW_LIST = ["`%s`" % NEWD, "`RULES.md`", "`TACTICS.md`"]
# Quotations in the new d file: (file, first line, last line, text).
QUOTES = [
    ("RULES.md", 41, 41, "In the exam the coin name and the date are hidden."),
    ("RULES.md", 51, 52, "The chance line is not invented. The answers are "
     "shuffled 1,000 times, and the real result must fall inside the best "
     "1%."),
    ("RULES.md", 119, 121, "A juror decides procedure and definition only: "
     "never a trading rule, never a threshold or score, and never a change to "
     "a rule in this file."),
    ("TACTICS.md", 50, 51, "the 24 hours before the start, hour by hour; plus "
     "a one-line summary of the previous 7 days."),
    ("TACTICS.md", 56, 56, "price, volume, trade count, taker buy/sell "
     "pressure"),
    ("TACTICS.md", 57, 57, "open interest, long/short ratios (5-minute "
     "archive)"),
    ("TACTICS.md", 58, 58, "funding rate, payment interval and its changes"),
    ("TACTICS.md", 61, 61, "bitcoin and ethereum, over the same hours"),
    ("TACTICS.md", 63, 63, "number of people viewing the page on Wikipedia "
     "(daily)"),
    ("TACTICS.md", 102, 102, "the coin name"),
    ("TACTICS.md", 103, 103, "the date and time"),
    ("TACTICS.md", 104, 104,
     "the price itself (converted to a number starting from 100)"),
    ("TACTICS.md", 105, 105, "the coin name inside announcements"),
    ("TACTICS.md", 106, 106, "the Wikipedia number itself (given as a ratio "
     "to the coin's own average)"),
    ("TACTICS.md", 107, 107, "the date in the release calendar"),
    ("TACTICS.md", 94, 94, "Then the canteen book freezes"),
    ("exam-prep/third-fix/juror-questions/JQ-R04-GATE.md", 55, 57,
     "If `ALL-removable` beats its chance line on the exam cards, the cards "
     "are not blind and the gate has failed."),
    ("exam-prep/third-fix/juror-questions/JQ-R04-GATE.md", 64, 66,
     "every feature in the audit's current list, minus the families that must "
     "stay on the card because a frozen canteen rule or TACTICS requires "
     "them"),
    (GATE_V, 72, 72, "The gate fails if either the nearest-neighbour attack "
     "or the pair AUC attack beats its own RULES 12 chance line on the exam "
     "cards."),
    (DC_V, 39, 39, "Do RULES 9 and TACTICS 6 require removing columns that "
     "identify clock hours? No."),
    (DC_V, 40, 40, "Does hiding \"the date in the release calendar\" cover "
     "release *names* that identify the day? No."),
    (DC_V, 41, 41, "Does hiding \"the date and time\" cover clock hour "
     "revealed by an offset plus outside knowledge of release times? No."),
    (DC_V, 42, 42, "May the blinding remove a TACTICS 3 field when nothing "
     "frozen reads it and it carries a measured coin signature? Yes — when "
     "both conditions hold: nothing the frozen canteen book reads it, and in "
     "the rendering the exam card would otherwise carry, it carries a "
     "measured coin signature as JQ-R04-CARRIES defines one."),
    (DC_V, 44, 44, "b1 (actual price rebased to 100, fixed decimals): "
     "Permitted."),
    (DC_V, 45, 45, "b2 (computed from printed chg%, starting from 100): "
     "Permitted."),
    (DC_V, 46, 46, "b3 (no price column; chg% stays): Permitted only if and "
     "as far as CONTENT-a yes."),
    (DC_V, 47, 47, "May a ranked column come from pre-rounding values, "
     "ordering hours the raw card prints as equal? No."),
    (CAR_V, 107, 107, "When the test in part b identifies a column's feature "
     "sets, the column carries a measured coin signature when either the "
     "pair AUC attack or the nearest-neighbour attack beats its own RULES 12 "
     "chance line on that set."),
    (CAR_V, 109, 109, "The test reads every feature computed from the "
     "column's own printed values and from nothing else, tested together as "
     "one set."),
]
# Cited ranges that are not a single quotation.
RANGE_CITES = [("TACTICS.md", 55, 64, "What is on the card"),
               ("TACTICS.md", 101, 107, "What is hidden")]
# Words that must not appear in the new d file (pointers to working files,
# reviews, the user route's file, the withdrawal; verdict reasoning; the
# grounds the audit gives for its forced families — REVIEW-6 §2.2).
FORBIDDEN = ["REVIEW", "VERDICT.md", "HANDED-FORWARD", "USER-QUESTIONS",
             "U-1", "seventh", "sixth", "withdrawn", "third-fix", "(3–0)",
             "(2–1", "Juror 1", "Juror 2", "Juror 3", "TEAM.md", "objects",
             "S-1 reads", "B-5, U-2 and U-3", "puts a previous-7-day summary",
             "reads the same unchanged", "FORCED_FAMILIES",
             "volatility-frozen", "p7-shape", "funding-line", "repeat-chg",
             "recommended"]
# Every number allowed in the new d file, with its source.
ALLOWED_NUMBERS = {
    "2026", "10", "01", "02",            # dates of writing; verdict paths
    "04",                                # identifiers JQ-R04-…
    "3", "6", "9", "12", "33", "34",     # rule / TACTICS section numbers
    "35",                                # RULES 35 (referee, scope)
    "41", "51", "52", "119", "121",      # RULES.md lines cited
    "50", "55", "64", "94", "101", "107",  # TACTICS.md lines cited
    "5",                                 # "5-minute archive" (TACTICS 57)
    "72", "39", "47", "109",             # verdict lines cited
    "100",                               # TACTICS 104 and CONTENT-b quotes
    "1,000", "1",                        # RULES 12 quotation; "1–5"; stop 1
    "24",                                # TACTICS 3 "the 24 hours"
    "7",                                 # TACTICS 3 "the previous 7 days"
    "2", "4",                            # stop numbers 2 and 4
}
# The fields each family prefix of the audit is computed from
# (read from `card_features()` and `REPEAT_GROUP`).
FORCED_EXPECTED = ("volatility-frozen", "funding-line", "p7-shape",
                   "repeat-chg")
INSIDE_FIELD = {
    "price:": "close", "volume:": "quote vol", "p7:log_avg_vol": "p7 line",
    "trades:": "trades", "p7:log_avg_trades": "p7 line",
    "openint:": "open int", "depth:": "depth", "ratio:": "ratio columns",
    "takerbuy:": "taker buy%", "wikipedia:": "Wikipedia line",
    "btceth:": "BTC/ETH", "shape:": "the eight level columns",
    "rep-close:": "close", "rep-volume:": "quote vol",
    "rep-trades:": "trades", "rep-takerbuy:": "taker buy%",
    "rep-openint:": "open int", "rep-ratio:": "ratio columns",
    "rep-depth:": "depth", "rep-btceth:": "BTC/ETH",
    "gran-close:": "close",
}
FORCED_FIELD = {"volatility:": "chg%", "rep-chg:": "chg%",
                "funding:": "funding line", "p7:price_pct": "p7 line",
                "p7:range_pct": "p7 line"}
# The bullet lines card_features() may read (all others are not read).
BULLETS_READ = {"Previous 7 days", "Funding", "Wikipedia page views"}
ANSWERS = ["- **no** —", "- **only where the card may not be without the "
           "field** —", "- **yes** —", "- **not a juror's** —",
           "- **Other**, with reasons."]
STOPS_D = ["if the set holds no feature on the exam cards",
           "computes a feature from a field whose\n   features leave the set "
           "and from one whose features stay",
           "until the\n   measurement and the record that answer rests on are "
           "complete",
           "if a ratified \"Other\" cannot be carried out as written"]
STOPS_HF = ["(i) the empty row of 1b",
            "(ii) a feature computed from a field whose features leave the row "
            "and\n    from one whose features stay",
            "(iii) under \"only where\", while (a) or\n    (b) is not complete",
            "(iv) a ratified \"Other\"\n    that cannot be carried out as "
            "written"]
BLOCK_BEGIN = "<!-- eighth-fix status block: begin -->"
BLOCK_END = "<!-- eighth-fix status block: end -->"


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
    s = s.replace("**", "").replace("> ", " ")
    return re.sub(r"\s+", " ", s).strip()


def lines_of(rel, a, b):
    return raw(rel).decode("utf-8").split("\n")[a - 1:b]


def read_snapshot(rel):
    out = {}
    for ln in raw(rel).decode("utf-8").splitlines():
        h, path = ln.split("  ", 1)
        out[path] = h
    return out


def ep_listing():
    out = []
    for d, dirs, files in os.walk(p(EP)):
        dirs.sort()
        for f in sorted(files):
            rel = os.path.relpath(os.path.join(d, f), ROOT)
            if rel.startswith(EIG + "/"):
                continue
            out.append(rel)
    return sorted(out)


def script_names():
    # dotfiles (`scripts/.gitkeep`) are not scripts; the pre-run snapshot,
    # made with `ls`, does not list them either
    return sorted("scripts/" + n for n in os.listdir(p("scripts"))
                  if os.path.isfile(p("scripts/" + n))
                  and not n.startswith("exam_") and not n.startswith("."))


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


def section(text, head):
    i = text.index(head)
    j = text.find("\n## ", i + len(head))
    return text[i:j if j >= 0 else len(text)]


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

    use("scripts/35_eighth_fix_check.py")
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
        if rel in (INDEX, USERQ):
            continue
        if sha(b) != h:
            changed.append(rel)
    check("S", "no file of the pre-run exam-prep snapshot is missing",
          not missing, ", ".join(missing))
    check("S", "every pre-run exam-prep file unchanged (index, user file and "
          "three appended files aside)", not changed, ", ".join(changed))
    for rel in sorted(APPENDED):
        whole = raw(rel)
        pre, size = None, None
        for n in range(len(whole), -1, -1):
            if sha(whole[:n]) == snap[rel]:
                pre, size = whole[:n], n
                break
        use(rel, pre if pre is not None else b"")
        check("S", "%s: pre-run bytes are its prefix" % rel, pre is not None,
              "prefix %s bytes" % size)
    sch = [rel for rel, h in sorted(ssnap.items()) if sha(use(rel)) != h]
    check("S", "every non-exam_ script in the snapshot unchanged", not sch,
          ", ".join(sch))

    # N — new files
    listing = ep_listing()
    inputs["(listing of exam-prep/, eighth-fix/ excluded)"] = sha(
        "\n".join(listing).encode())
    new = [r for r in listing if r not in snap]
    check("N", "no new exam-prep file outside eighth-fix/", not new,
          ", ".join(new))
    names = script_names()
    inputs["(names in scripts/, exam_* excluded)"] = sha(
        "\n".join(names).encode())
    newscripts = [n for n in names if n not in ssnap]
    check("N", "no new script except this one",
          set(newscripts) <= NEW_ALLOWED_SCRIPTS, ", ".join(newscripts))

    # L — locked files
    for rel, h in sorted(LOCKED.items()):
        check("L", "%s unchanged" % rel, sha(use(rel)) == h, h[:12])

    # V — earlier versions
    idx = use(INDEX).decode("utf-8")
    old = use(OLD_INDEX).decode("utf-8")
    found = re.findall(r"`(exam-prep/[^`]+JUROR-QUESTIONS-as-of-[^`]+)`"
                       r"[^`]*?`([0-9a-f]{64})`", idx, flags=re.S)
    check("V", "the index names six earlier versions with SHA-256",
          len(found) == 6, "%d found" % len(found))
    for rel, h in found:
        check("V", "%s has the SHA-256 the index gives" % rel,
              sha(use(rel)) == h, h[:12])
    check("V", "the seventh-fix index kept byte for byte",
          sha(old.encode("utf-8")) == snap[INDEX], snap[INDEX][:12])
    olduq = use(OLD_USERQ)
    check("V", "the seventh-fix USER-QUESTIONS.md kept byte for byte",
          sha(olduq) == snap[USERQ], snap[USERQ][:12])

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
    for v in (GATE_V, N1_V, CAR_V, DC_V):
        first = use(v).decode("utf-8").split("\n")[0].strip()
        check("I", "%s exists and its first line reads RATIFIED" % v,
              first == "RATIFIED", first)
    for r in ROW_IDS:
        if r == "JQ-R04-CONTENT-d" or r not in rows or r not in orows:
            continue
        check("I", "row %s: file, group and reading list unchanged" % r,
              rows[r][0][:4] == orows[r][0][:4])
    drow = rows.get("JQ-R04-CONTENT-d", [[""] * 5])[0]
    check("I", "row JQ-R04-CONTENT-d reads the new file, sits alone, and "
          "lists only the new file, RULES.md and TACTICS.md",
          drow[1].startswith("`%s`" % NEWD) and drow[2] == "none" and
          [x.strip() for x in drow[3].split(",")] == D_ROW_LIST, drow[3])
    # a run date (YYYY-MM-DD) and a HANDED-FORWARD item id (A-0.1) are
    # provenance and pointers, not numbers of a question; both are stripped
    def qnums(t):
        t = re.sub(r"\d{4}-\d{2}-\d{2}", " ", t)
        t = re.sub(r"\bA-\d+\.\d+\b", " ", t)
        return numbers(t)
    newnum = qnums(idx) - qnums(old)
    check("I", "the index carries no number the seventh-fix index did not "
          "(SHA-256 values, run dates and HANDED-FORWARD item ids aside)",
          not newnum, ", ".join(sorted(newnum)))
    leaks, tested = [], 0
    nidx = norm(idx)
    for jf in JUROR_FILES:
        for o in option_sentences(use(jf).decode("utf-8")):
            tested += 1
            if o in nidx:
                leaks.append("%s: %s" % (jf, o))
    check("I", "no option or question sentence of any juror file in the "
          "index", not leaks and tested > 0,
          "%d sentences tested; %s" % (tested, "; ".join(leaks)))
    for lab in ("only where", "not a juror", "may not be without"):
        check("I", "the index carries the answer label %r no more often "
              "than the seventh-fix index did (%d)" % (lab, old.count(lab)),
              idx.count(lab) <= old.count(lab), "%d" % idx.count(lab))

    # D — the new juror file
    d = use(NEWD).decode("utf-8")
    nd = norm(d)
    opened = section(d, "## What you open")
    listed = re.findall(r"^- (.+)$", opened, flags=re.M)
    check("D", "reading list is this file, RULES.md and TACTICS.md",
          listed == ["this file", "`RULES.md` (lines cited below)",
                     "`TACTICS.md` (lines cited below)"], repr(listed))
    for rel, a, b, q in QUOTES:
        srcl = lines_of(rel, a, b)
        src = norm(" ".join(x.strip().lstrip("-").strip() for x in srcl))
        insrc = norm(q) in src
        ind = norm(q) in nd
        check("D", "quotation %s %d–%d in source and in the d file: %s…"
              % (rel.split("/")[-1], a, b, q[:28]), insrc and ind,
              "source %s; d file %s" % (insrc, ind))
    for rel, a, b, probe in RANGE_CITES:
        srcl = raw(rel).decode("utf-8").split("\n")
        hit = any(probe in x for x in srcl[a - 2:a])
        check("D", "cited range %s %d–%d starts at %r" % (rel, a, b, probe),
              hit)
    tac = raw("TACTICS.md").decode("utf-8").split("\n")
    check("D", "TACTICS.md line 64 is the last item of the on-card list",
          tac[63].startswith("- ") and tac[64].strip() == "",
          tac[63].strip()[:40])
    hits = [w for w in FORBIDDEN if w in d]
    check("D", "no pointer, verdict reasoning, split or forced-family ground",
          not hits, ", ".join(hits))
    paths = re.findall(r"exam-prep/[A-Za-z0-9]", d)
    check("D", "no path into exam-prep/", not paths, ", ".join(paths))
    nums = numbers(d)
    extra = sorted(nums - ALLOWED_NUMBERS)
    check("D", "every number in the d file is on the declared list",
          not extra, ", ".join(extra))
    dec = re.findall(r"\d+\.\d+", d)
    check("D", "no decimal figure in the d file", not dec, ", ".join(dec))
    for w in ("recommend", "should choose", "we suggest", "better answer",
              "prefer"):
        n = d.lower().count(w)
        allowed = w == "recommend" and n == d.lower().count(
            "not recommending it")
        check("D", "no recommending word %r (outside the standard notice)"
              % w, n == 0 or allowed, "%d hits" % n)
    for a in ANSWERS:
        check("D", "answer offered: %s" % a, d.count(a) == 1)
    mech = section(d, "## What each answer does")
    for lab in ("**no:**", "**only where the card may not be without the "
                "field:**", "**yes:**", "**not a juror's:**"):
        check("D", "mechanical consequence given for %s" % lab, lab in mech)
    for s_ in STOPS_D:
        check("D", "stop named in the d file: %s…" % s_[:30].replace(
            "\n", " "), s_ in d)
    for v, n_ in ((DC_V, (39, 47)), (CAR_V, (107, 109)), (GATE_V, (72, 72))):
        check("D", "verdict cited by path and line: %s" % v.split("/")[1],
              v in d)
    check("D", "the four rows of split marks are not quoted",
          "3–0" not in d and "2–1" not in d)

    asrc = use(AUDIT)
    check("D", "audit SHA-256 is the one HANDED-FORWARD names",
          sha(asrc) == AUDIT_SHA, sha(asrc)[:12])
    stxt = asrc.decode("utf-8")
    tree = ast.parse(stxt)
    fam, forced, rgroup = None, None, None
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and \
                isinstance(node.targets[0], ast.Name):
            nm = node.targets[0].id
            if nm == "FAMILIES":
                fam = ast.literal_eval(node.value)
            if nm == "FORCED_FAMILIES":
                forced = ast.literal_eval(node.value)
            if nm == "REPEAT_GROUP":
                rgroup = ast.literal_eval(node.value)
    check("D", "FORCED_FAMILIES is the four families the d file describes",
          tuple(forced or ()) == FORCED_EXPECTED, repr(forced))
    fpre = sorted({x for k in FORCED_EXPECTED for x in fam[k]})
    check("D", "forced prefixes are chg% (three features and repeats), the "
          "funding line and two previous-7-day figures",
          set(fpre) == set(FORCED_FIELD), ", ".join(fpre))
    ipre = sorted({x for k, v in fam.items() if k not in FORCED_EXPECTED
                   for x in v})
    check("D", "every inside-set prefix maps to a field the d file names "
          "(%d prefixes)" % len(ipre), set(ipre) == set(INSIDE_FIELD),
          ", ".join(sorted(set(ipre) ^ set(INSIDE_FIELD))))
    check("D", "REPEAT_GROUP names thirteen columns (A-0.9)",
          len(rgroup or {}) == 13, ", ".join(sorted(rgroup or {})))
    cf = stxt[stxt.index("def card_features("):stxt.index("def _exact_number(")]
    bl = set(re.findall(r'b\.get\("([^"]+)"', cf))
    check("D", "card_features() reads only the previous-7-day, funding and "
          "Wikipedia lines (nothing from the release line or "
          "announcements)", bl == BULLETS_READ, ", ".join(sorted(bl)))
    # one field per feature: each assignment f[...] sits under one column
    # test or one bullet, and the loops build each key from one column name
    keys = re.findall(r'f\["([^"]+)"\]', cf)
    multi = [k for k in keys if k.count(":") != 1]
    loops_ok = ('f["shape:sd_log_" + tag]' in cf and
                'f["shape:acf1_log_" + tag]' in cf and
                'xs = col[name]' in cf and
                'vals = [repr(x) for x in col[name]]' in cf)
    check("D", "each feature is computed from one field (fixed keys carry "
          "one prefix; shape and repeat keys are built per column)",
          not multi and loops_ok, ", ".join(multi))
    check("D", "the audit's empty-set message is the one the d file quotes",
          "no features left after blinding" in stxt and
          "no features left after blinding" in d)

    # U — user questions
    uq = use(USERQ)
    utxt = uq.decode("utf-8")
    i0, i1 = utxt.find(BLOCK_BEGIN), utxt.find(BLOCK_END)
    ok = utxt.count(BLOCK_BEGIN) == 1 and utxt.count(BLOCK_END) == 1 and \
        0 < i0 < i1
    removed = None
    if ok:
        blk = utxt[i0 - 1:i1 + len(BLOCK_END) + 1]
        removed = utxt.replace(blk, "", 1).encode("utf-8")
    check("U", "one status block; removing it gives the seventh-fix bytes",
          ok and removed == olduq, "")
    check("U", "the block says superseded", ok and "superseded" in
          utxt[i0:i1])

    # H — HANDED-FORWARD eighth-fix section
    hf = raw(HF).decode("utf-8")
    k = hf.find("# Section added by the eighth-fix run")
    sec = hf[k:] if k >= 0 else ""
    use(HF + " (eighth-fix section)", sec.encode("utf-8"))
    for item in ("**A-0.1 · Rulings**", "**A-0.4, step 1 · The row**",
                 "**A-0.9 · What the frozen canteen book reads**",
                 "**C-5 · Files that must not reach a juror or a referee**"):
        j = sec.find(item)
        nxt = sec.find("\n- **", j + 1)
        body = sec[j:nxt if nxt > 0 else len(sec)]
        check("H", "%s present with a check line" % item.strip("*"),
              j >= 0 and "*Check" in body)
    for s_ in STOPS_HF:
        check("H", "stop in HANDED-FORWARD 1c: %s…" % s_[:24].replace(
            "\n", " "), s_ in sec)

    # run number and record
    blob = "\n".join("%s %s" % (k_, inputs[k_]) for k_ in sorted(inputs))
    run = sha(blob.encode())[:16]
    nfail = sum(1 for c in checks if not c["ok"])
    rep = ["# Eighth-fix check — run `%s`" % run, "",
           "Script: `scripts/35_eighth_fix_check.py`. Run number: the first "
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
    rep += ["- `%s` `%s`" % (k_, inputs[k_]) for k_ in sorted(inputs)]
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
    targets = [(OUT + "/eighth-fix-check-%s.md" % run, report),
               (OUT + "/runs/%s.json" % run, js)]
    for rel, data in targets:
        if os.path.exists(p(rel)) and raw(rel) != data:
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
