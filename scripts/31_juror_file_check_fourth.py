#!/usr/bin/env python3
"""
31_juror_file_check_fourth.py -- check every number and every line citation
in the juror files the fourth-fix run issued, against the source each file
names; and check that the JQ-R04-GATE file, which this run must not change,
is unchanged and still agrees with the exact audit.

What it does
------------
  N  Numbers. For each figure a file shows, recompute from the named run
     output the exact text it must appear as, and check that text is in the
     file. Passages the fourth-fix run did not change are checked to be
     byte-identical to the third-fix file (which scripts/28 checked, run
     bbb740248b0c8717, and REVIEW-3 re-checked).
  L  Line citations of RULES.md, TACTICS.md, the canteen book and
     scripts/06_find_moments.py are printed with the cited text, so a reader
     can compare quotation and file side by side.
  G  JQ-R04-GATE: its SHA-256 equals the one the coordinator's instruction
     gives, and every figure of its table equals the exact audit's gate row
     (read only; the file is not written).

Input   : exam-prep/fourth-fix/juror-questions/*.md; the third-fix juror
          files; exam-prep/third-fix/juror-questions/JQ-R04-GATE.md (read
          only); the exact-audit runs in exam-prep/fourth-fix/identity/; the
          check run of scripts/30 in exam-prep/fourth-fix/checks/runs/; the
          collapse runs; the strict-flags-k1 blinding manifest; cards/.
Output  : exam-prep/fourth-fix/checks/juror-file-check-<run16>.md
          exam-prep/fourth-fix/checks/runs/<run16>.json   (append-only)
          With --dry: nothing is written; failures are printed.

Rules implemented: RULES 19 (a number shown to a juror is a measured one),
RULES 23, RULES 29/30. No threshold, score or trading rule is defined here.
"""

import csv
import datetime as dt
import glob
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
JQ4 = os.path.join(REPO, "exam-prep", "fourth-fix", "juror-questions")
JQ3 = os.path.join(REPO, "exam-prep", "third-fix", "juror-questions")
OUT_DIR = os.path.join(REPO, "exam-prep", "fourth-fix", "checks")
GATE = os.path.join(JQ3, "JQ-R04-GATE.md")
GATE_SHA = "55e7b95c9bc4beb7eb78418ed230270661d14ed92876bb13d047d1b853f816ce"
CHECKS30 = "516027c6c9f215d6"
COLLAPSE_RUN = "a0ecf6970d86b199"
EXACT = {"blinded-strict-flags": "9ff0ffec3fe21ebe",
         "blinded-strict-flags-k1": "762815a877c19551",
         "blinded-strict-flags-unrounded": "d6557e91f9f97f7b",
         "blinded-strict": "45d062efe77c9251",
         "blinded-rank": "446adf64f8e8235c",
         "blinded-ratio": "989b8f21b23e0310"}


def sha(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def f4(x):
    return "%.4f" % float(x)


def audit(label):
    run = EXACT[label]
    p = os.path.join(REPO, "exam-prep", "fourth-fix", "identity",
                     "run-" + run, "identity-audit-%s.csv" % label)
    return run, {x["family"]: x for x in csv.DictReader(open(p))}, p


def span(text, start, end=None):
    i = text.index(start)
    j = text.index(end, i) if end else len(text)
    return text[i:j]


def main():
    started = dt.datetime.now(dt.timezone.utc)
    inputs = []
    texts = {os.path.basename(p): open(p, encoding="utf-8").read()
             for p in sorted(glob.glob(os.path.join(JQ4, "*.md")))}
    old = {os.path.basename(p): open(p, encoding="utf-8").read()
           for p in sorted(glob.glob(os.path.join(JQ3, "*.md")))}
    checks = []

    def ws(x):
        return re.sub(r"\s+", " ", x)

    def need(fname, text, source):
        # compared with runs of white space (line breaks) collapsed
        checks.append({"file": fname, "text": text, "source": source,
                       "found": ws(text) in ws(texts[fname])})

    def same(fname, start, end, why):
        a = span(texts[fname], start, end)
        b = span(old[fname], start, end)
        checks.append({"file": fname, "text": "passage from %r%s is "
                       "byte-identical to the third-fix file"
                       % (start[:40], (" to %r" % end[:30]) if end else ""),
                       "source": why, "found": a == b})

    rec30p = os.path.join(OUT_DIR, "runs", CHECKS30 + ".json")
    inputs.append(rec30p)
    r30 = json.load(open(rec30p, encoding="utf-8"))["results"]

    # ================= JQ-N1 ================================================
    F = "JQ-N1.md"
    obs = r30["H-2"]["observation"]
    mw, cs = obs["move-window"], obs["card-span"]
    if not r30["H-2"]["accepted"]:
        raise SystemExit("H-2 not accepted")
    need(F, "under move-window\n    both give **%d** events, and **%d** events"
         % (mw["engine_latest_events"],
            mw["events_in_one_partition_only_latest_vs_earliest"])
         if mw["engine_latest_events"] == mw["engine_earliest_events"]
         else "MISMATCH", "30 H-2")
    need(F, "under card-span \"earliest\" gives **%d** events and\n"
         "    \"latest\" **%d**, and **%d** events appear in one partition only"
         % (cs["engine_earliest_events"], cs["engine_latest_events"],
            cs["events_in_one_partition_only_latest_vs_earliest"]), "30 H-2")
    for d, lab in (("move-window", mw), ("card-span", cs)):
        t = lab["table_row"]
        need(F, "| %s / greedy-clique / cross-coin, keep latest | %d | %d | "
             "%d | %d | %d | %d |" % (
                 d, t["events"], t["events_of_1_card"], t["largest_event"],
                 t["events_holding_both_kinds"],
                 t["events_holding_2plus_cards_of_one_coin"],
                 t["largest_same_coin_count"]), "30 H-2 table row")
    need(F, "1 event (%d cards) under move-window, 0 under card-span"
         % mw["table_row"]["block_cards_in_immovable_events"]
         if (mw["table_row"]["block_immovable_events"] == 1
             and cs["table_row"]["block_immovable_events"] == 0)
         else "MISMATCH", "30 H-2 table row")
    need(F, "In the observation cards no coin has two moments at the same "
         "start hour," if r30["H-5"]["coin_start_hours_with_2plus_moments"]
         == 0 else "MISMATCH", "30 H-5")
    need(F, "fourth-fix-checks-%s.md" % CHECKS30, "run id")
    # the collapse run reproduces 756cf4ea156d92c3 byte for byte
    ok = True
    for f in ("events.csv", "collapse-summary.csv", "shuffle-calibration.csv"):
        a = os.path.join(REPO, "exam-prep", "fourth-fix", "collapse",
                         "run-" + COLLAPSE_RUN, f)
        b = os.path.join(REPO, "exam-prep", "collapse",
                         "run-756cf4ea156d92c3", f)
        inputs += [a, b]
        ok = ok and sha(a) == sha(b)
    need(F, "`%s`\n  reproduce every output of that run byte for byte"
         % COLLAPSE_RUN if ok else "MISMATCH", "cmp of the three CSVs")
    # the scale table and the main summary rows (unchanged passage)
    same(F, "## The scale of the choice", "## Part 1",
         "third-fix text; table = run 756cf4ea156d92c3")
    sm = {r["config"]: r for r in csv.DictReader(open(os.path.join(
        REPO, "exam-prep", "fourth-fix", "collapse", "run-" + COLLAPSE_RUN,
        "collapse-summary.csv")))}
    for cfg, r in sm.items():
        lab = "no collapse" if cfg == "none/none/none" else " / ".join(
            ("–" if x == "component" and cfg.startswith("start-hour")
             else x) for x in cfg.split("/"))
        cells = [r["events"], r["events_of_size_1"], r["largest_event"],
                 r["events_holding_both_kinds"],
                 r["events_holding_2plus_cards_of_one_coin"],
                 r["largest_same_coin_count_in_one_event"]]
        row = [ln for ln in texts[F].split("\n")
               if ln.startswith("| %s |" % lab)]
        got = ([c.strip().strip("*") for c in row[0].strip("|").split("|")]
               [1:] if row else None)
        checks.append({"file": F, "text": "summary row '%s' = %s"
                       % (lab, cells), "source": "collapse-summary %s"
                       % COLLAPSE_RUN, "found": got == cells})
    same(F, "## Part 1", "## Part 2", "third-fix text")
    same(F, "What the two ways do to the 1% boundary",
         "## The strongest objection", "third-fix text (E-4, G-2)")
    same(F, "## The strongest objection", None, "third-fix text")

    # ================= JQ-R04-CONTENT =======================================
    F = "JQ-R04-CONTENT.md"
    runS, S, pS = audit("blinded-strict-flags")
    runK, K, pK = audit("blinded-strict-flags-k1")
    runU, U, pU = audit("blinded-strict-flags-unrounded")
    inputs += [pS, pK, pU]

    def verdict(x, col):
        return "beats" if x[col] == "YES" else "does not beat"
    for rows, rlab in ((S, "from the printed values"),
                       (U, "from the values before rounding")):
        for fam, flab in (("trades-level", "typical level of the ranked "
                           "column"), ("repeat-trades", "how many values "
                                       "repeat in the column")):
            x = rows[fam]
            b = rows is S
            a1 = "**%s**" % f4(x["pair_auc"]) if b else f4(x["pair_auc"])
            n1 = "**%s**" % f4(x["nn_tie_free"]) if b else f4(
                x["nn_tie_free"])
            need(F, "| %s | %s | %s (%s) — %s | %s (%s) — %s |" % (
                rlab, flab, a1, f4(x["auc_chance_1pct"]),
                verdict(x, "auc_beats_chance"), n1,
                f4(x["nn_tie_free_chance_1pct"]),
                verdict(x, "nn_tie_free_beats_chance")),
                 "exact audit %s" % (runS if b else runU))
    need(F, "audit run\n  `%s`)" % runS, "run id")
    need(F, "audit run `%s`)" % runU, "run id")
    man = open(os.path.join(REPO, "exam-prep", "second-fix", "blind-proof",
                            "strict-flags-k1",
                            "blind-manifest-strict-flags-k1.md")).read()
    inputs.append(os.path.join(REPO, "exam-prep", "second-fix",
                               "blind-proof", "strict-flags-k1",
                               "blind-manifest-strict-flags-k1.md"))
    rb = span(man, "## The decimals of the rebased `close`")
    m2 = re.search(r"^\| 2 \| (\d+) \|", rb, re.M)
    m3 = re.search(r"^\| 3 \| (\d+) \|", rb, re.M)
    for rows, lab, n in ((S, "2 decimals (first run)", m2.group(1)),
                         (K, "3 decimals (the fewest at which rounding makes "
                          "no new repeats)", m3.group(1))):
        rc, gc = rows["repeat-close"], rows["granularity-close"]
        for x, c in ((rc, "auc_beats_chance"), (rc, "nn_tie_free_beats_chance"),
                     (gc, "auc_beats_chance"), (gc, "nn_tie_free_beats_chance")):
            if x[c] != "YES":
                raise SystemExit("part b: a bold figure does not beat")
        need(F, "| %s | %s | **%s** (%s) | **%s** (%s) | **%s** (%s) | "
             "**%s** (%s) |" % (lab, n, f4(rc["pair_auc"]),
                                f4(rc["auc_chance_1pct"]),
                                f4(rc["nn_tie_free"]),
                                f4(rc["nn_tie_free_chance_1pct"]),
                                f4(gc["pair_auc"]), f4(gc["auc_chance_1pct"]),
                                f4(gc["nn_tie_free"]),
                                f4(gc["nn_tie_free_chance_1pct"])),
             "exact audit; k1 manifest")
    need(F, "decimals, %s against %s;" % (
        f4(S["repeat-close"]["nn_tie_free"]),
        f4(S["repeat-close"]["nn_tie_free_chance_1pct"])), "exact audit")
    need(F, "audit runs `%s` (2 decimals) and\n`%s` (3 decimals)"
         % (runS, runK), "run ids")
    h4 = r30["H-4"]
    for col, r in h4["by_column"].items():
        need(F, "| `%s` | %s | %s | %s |" % (
            col, format(r["hours_tied_on_raw_card"], ","),
            format(r["hours_tied_on_raw_card_ranked_apart"], ","),
            r["cards_with_an_hour_ranked_apart"]), "30 H-4")
    need(F, "Every one of the %d cards has at least one such hour"
         % h4["cards"] if h4["total"]["cards_with_any_hour_ranked_apart"]
         == h4["cards"] else "MISMATCH", "30 H-4")
    need(F, "run\n`%s`, H-4" % CHECKS30, "run id")
    q2 = open(os.path.join(REPO, "exam-prep", "review-3", "probes",
                           "q2_tiefree_strict-flags.out")).read()
    mq = re.search(r"^repeat-close \|.*\| ([\d.]+)$", q2, re.M)
    checks.append({"file": F, "text": "q2: share of further shuffles at or "
                   "above the observed repeat-close score is below the 1%% "
                   "boundary's share and near it (%s)" % mq.group(1),
                   "source": "review-3 q2_tiefree_strict-flags.out",
                   "found": 0.0 < float(mq.group(1)) < 0.01})
    same(F, "What the frozen canteen book does with the trade count",
         "**Question a.**", "third-fix text")

    # ================= JQ-R04-DATE ==========================================
    F = "JQ-R04-DATE.md"
    same(F, "## What you decide", "These three parts should be answered",
         "third-fix text")
    same(F, "For each part: your answer", None, "third-fix text")

    # ================= JQ-CANTEEN-8 =========================================
    F = "JQ-CANTEEN-8.md"
    same(F, "## What you decide", "Answer together with JQ-N1",
         "third-fix text")
    same(F, "## What has been measured", "The canteen chair's figure",
         "third-fix text; counts = 26 G-3, REVIEW-3 q3")
    same(F, "## Part a", None, "third-fix text")
    import importlib.util  # noqa: E402
    sys.path.insert(0, HERE)
    import lab_cards  # noqa: E402
    cards = {c["card"]: c for c in lab_cards.load_all(os.path.join(REPO,
                                                                   "cards"))}

    def hrs(c):
        s = c["start_hour_utc"].replace("Z", "")
        s = s + ":00" if len(s) == 16 else s
        return dt.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S")
    gap = int((hrs(cards["C011"]) - hrs(cards["C010"])).total_seconds()
              // 3600)
    need(F, "Their cards\nstart %d hours apart, so their before windows "
         "share %d hours" % (abs(gap), 24 - abs(gap)), "cards C010, C011")
    need(F, "while their card spans share %d" % (48 - abs(gap)),
         "cards C010, C011")

    # ================= G · the GATE file, read only =========================
    gsha = sha(GATE)
    checks.append({"file": "JQ-R04-GATE.md (third-fix, not written)",
                   "text": "SHA-256 %s" % GATE_SHA, "source": "instruction",
                   "found": gsha == GATE_SHA})
    gtext = open(GATE, encoding="utf-8").read()
    for lab, d in (("blinded-strict-flags", "`strict-flags` (the recommended "
                    "one)"), ("blinded-strict", "`strict`"),
                   ("blinded-rank", "`rank`"), ("blinded-ratio", "`ratio`"),
                   ("blinded-strict-flags-k1", "`strict-flags`, price at 3 "
                    "decimals")):
        _, rows, p = audit(lab)
        inputs.append(p)
        g = rows["ALL-removable"]
        txt = "| %s | `" % d
        row = [ln for ln in gtext.split("\n") if ln.startswith(txt)][0]
        want = "| %s (%s) — beats | %s (%s) — beats |" % (
            f4(g["nn_same_coin_accuracy"]), f4(g["nn_chance_1pct"]),
            f4(g["pair_auc"]), f4(g["auc_chance_1pct"]))
        checks.append({"file": "JQ-R04-GATE.md (third-fix, not written)",
                       "text": "%s: the GATE row's figures equal the exact "
                       "audit's %s; features %s; tied cards %s" % (
                           lab, want, g["features_used"],
                           g["cards_with_tied_nn"]),
                       "source": "exact audit %s" % EXACT[lab],
                       "found": row.endswith(" %s | %s" % (
                           g["features_used"], want.lstrip("| ")))
                       and g["cards_with_tied_nn"] == "0"
                       and g["nn_tie_free"] == g["nn_same_coin_accuracy"]})

    # ================= L · line citations ===================================
    files = ("RULES.md", "TACTICS.md", "canteen/2026-09-19-sofia.md",
             "scripts/06_find_moments.py")
    cache = {f: open(os.path.join(REPO, f), encoding="utf-8").read()
             .split("\n") for f in files}
    pat = re.compile(r"`(RULES\.md|TACTICS\.md|canteen/2026-09-19-sofia\.md|"
                     r"scripts/06_find_moments\.py)`[^`]*?\blines?\s+(\d+)"
                     r"(?:[–-](\d+))?((?:(?:,| and) \d+(?:[–-]\d+)?)*)")
    cites = []
    for fname, t in texts.items():
        flat = re.sub(r"\s+", " ", t)
        for m in pat.finditer(flat):
            f = m.group(1)
            spans = [(int(m.group(2)), int(m.group(3) or m.group(2)))]
            for mm in re.finditer(r"(\d+)(?:[–-](\d+))?", m.group(4) or ""):
                spans.append((int(mm.group(1)), int(mm.group(2) or
                                                     mm.group(1))))
            for a, b in spans:
                cites.append({"file": fname, "cites": "%s %d–%d" % (f, a, b),
                              "text": " / ".join(x.strip() for x in
                                                 cache[f][a - 1:b])})
        # bare "lines N–M" after a canteen quotation in the same file
        for m in re.finditer(r"\(lines (\d+)[–-](\d+)", flat):
            a, b = int(m.group(1)), int(m.group(2))
            cites.append({"file": fname, "cites": "canteen (bare) %d–%d"
                          % (a, b), "text": " / ".join(
                              x.strip() for x in cache[
                                  "canteen/2026-09-19-sofia.md"][a - 1:b])})

    # ================= write ================================================
    script_sha = sha(os.path.abspath(__file__))
    h = hashlib.sha256()
    h.update(("script:%s\n" % script_sha).encode())
    for fname in sorted(texts):
        h.update(("%s:%s\n" % (fname, sha(os.path.join(JQ4, fname))))
                 .encode())
    h.update(("gate:%s\n" % gsha).encode())
    for p in sorted(set(inputs)):
        h.update(("%s:%s\n" % (os.path.relpath(p, REPO), sha(p))).encode())
    run_full = h.hexdigest()
    run16 = run_full[:16]
    failed = [c for c in checks if not c["found"]]
    if "--dry" in sys.argv:
        for c in failed:
            print("FAILED", c["file"], "|", c["text"], "|", c["source"])
        print("%d checks, %d failed (dry run, nothing written)"
              % (len(checks), len(failed)))
        return
    core = {"run": run16, "input_fingerprint": run_full,
            "script_sha256": script_sha, "checks": checks,
            "failed": len(failed), "citations": cites}
    os.makedirs(os.path.join(OUT_DIR, "runs"), exist_ok=True)
    rec = os.path.join(OUT_DIR, "runs", run16 + ".json")
    if os.path.exists(rec):
        if json.load(open(rec, encoding="utf-8")) != json.loads(
                json.dumps(core)):
            sys.stderr.write("STOP: %s exists with different content\n" % rec)
            sys.exit(1)
        sys.stderr.write("run %s already recorded\n" % run16)
        sys.exit(1 if failed else 0)
    L = ["# Juror-file check (fourth-fix) — run `%s`" % run16, "",
         "Written by `scripts/31_juror_file_check_fourth.py` at %s (system "
         "clock)." % started.strftime("%Y-%m-%dT%H:%M:%SZ"), "",
         "## N and G · numbers: %d checks, %d failed" % (len(checks),
                                                          len(failed)),
         "", "| file | expected text (as recomputed) | source | found |",
         "|---|---|---|---|"]
    for c in checks:
        L.append("| %s | %s | %s | %s |"
                 % (c["file"], c["text"].replace("|", "/").replace("\n", " "),
                    c["source"], "yes" if c["found"] else "**NO**"))
    L += ["", "## L · line citations, with the cited text", "",
          "| juror file | cites | text of the cited lines |", "|---|---|---|"]
    for c in cites:
        L.append("| %s | %s | %s |" % (c["file"], c["cites"],
                                       c["text"].replace("|", "/")))
    L.append("")
    with open(os.path.join(OUT_DIR, "juror-file-check-%s.md" % run16), "w",
              encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    with open(rec, "w", encoding="utf-8") as fh:
        json.dump(core, fh, indent=1, sort_keys=True)
        fh.write("\n")
    sys.stderr.write("run %s: %d checks, %d failed\n"
                     % (run16, len(checks), len(failed)))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
