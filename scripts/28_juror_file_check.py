#!/usr/bin/env python3
"""
28_juror_file_check.py -- check every number and every line citation in the
juror files the third-fix run corrected, against the source each file names.

What it does
------------
  N  Numbers. For each file, recomputes from the named run outputs the text
     each number must appear as, and checks that exact text is in the file.
     A failure is listed; the script exits non-zero if any check fails.
  L  Line citations. Every citation of the form "`RULES.md` line(s) …",
     "`TACTICS.md` line(s) …", "`canteen/2026-09-19-sofia.md` line(s) …" and
     "`scripts/<name>.py` lines …" is printed with the text of the cited lines,
     so a reader can compare the quotation with the file. (Whether a
     quotation is faithful is read by a person; the script only lays the two
     side by side.)

The audit runs it reads are the third-fix audit's (the run record whose
`script_sha256` equals the current scripts/16_identity_audit.py), found by
card-set label in exam-prep/third-fix/identity/runs/.

Input   : exam-prep/third-fix/juror-questions/*.md and the sources they name
Output  : exam-prep/third-fix/checks/juror-file-check-<run16>.md
          exam-prep/third-fix/checks/runs/<run16>.json   (append-only)
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
JQ = os.path.join(REPO, "exam-prep", "third-fix", "juror-questions")
IDN = os.path.join(REPO, "exam-prep", "third-fix", "identity")
OUT_DIR = os.path.join(REPO, "exam-prep", "third-fix", "checks")


def sha(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def f4(x):
    return "%.4f" % float(x)


def audit_runs():
    """label -> (run16, rows by family) for the current audit script."""
    cur = sha(os.path.join(HERE, "16_identity_audit.py"))
    out = {}
    for rec in sorted(glob.glob(os.path.join(IDN, "runs", "*.json"))):
        r = json.load(open(rec, encoding="utf-8"))
        if r.get("script_sha256") != cur or "card_set" not in r:
            continue
        csvp = os.path.join(IDN, "run-" + r["run"],
                            "identity-audit-%s.csv" % r["card_set"])
        rows = {x["family"]: x for x in csv.DictReader(open(csvp,
                                                            encoding="utf-8"))}
        out[r["card_set"]] = (r["run"], rows, r)
    return out


def main():
    started = dt.datetime.now(dt.timezone.utc)
    A = audit_runs()
    checks = []
    texts = {os.path.basename(p): open(p, encoding="utf-8").read()
             for p in sorted(glob.glob(os.path.join(JQ, "*.md")))}

    def need(fname, text, source):
        checks.append({"file": fname, "text": text, "source": source,
                       "found": text in texts[fname]})

    # ---------------- JQ-R04-GATE ------------------------------------------
    disp = [("blinded-strict-flags", "`strict-flags` (the recommended one)"),
            ("blinded-strict", "`strict`"), ("blinded-rank", "`rank`"),
            ("blinded-ratio", "`ratio`"),
            ("blinded-strict-flags-k1", "`strict-flags`, price at 3 decimals")]
    for lab, d in disp:
        run, rows, _ = A[lab]
        g = rows["ALL-removable"]
        if g["nn_beats_chance"] != "YES" or g["auc_beats_chance"] != "YES":
            raise SystemExit("gate row of %s does not beat both" % lab)
        need("JQ-R04-GATE.md",
             "| %s | `%s` | %s | %s (%s) — beats | %s (%s) — beats |"
             % (d, run, g["features_used"], f4(g["nn_same_coin_accuracy"]),
                f4(g["nn_chance_1pct"]), f4(g["pair_auc"]),
                f4(g["auc_chance_1pct"])), "audit %s, ALL-removable" % run)
        if g["cards_with_tied_nn"] != "0":
            raise SystemExit("gate row of %s has ties" % lab)
    sf_run, sf, _ = A["blinded-strict-flags"]
    need("JQ-R04-GATE.md", "blinded version, it is **44 features**"
         if sf["ALL-removable"]["features_used"] == "44" else "MISMATCH",
         "audit %s features_used" % sf_run)
    sec = {x["family"]: x for x in csv.DictReader(open(os.path.join(
        REPO, "exam-prep", "second-fix", "identity", "run-d70dd7b545bfce8a",
        "identity-audit-blinded-strict-flags.csv"), encoding="utf-8"))}
    p6 = open(os.path.join(REPO, "exam-prep", "review-2", "probes", "p6.out"),
              encoding="utf-8").read()
    m = re.search(r"first-run feature set \(every repeat-\* family excluded\)"
                  r"\s*\| (\d+) \|", p6)
    need("JQ-R04-GATE.md", "(the row went from %s to %s features)"
         % (m.group(1), sec["ALL-removable"]["features_used"]),
         "review-2 p6.out; second-fix audit d70dd7b545bfce8a")
    need("JQ-R04-GATE.md", "(43 → %s)" % sf["ALL-removable"]["features_used"],
         "audit %s" % sf_run)
    # residual diagnostic on strict-flags with the current audit
    res = None
    for rec in sorted(glob.glob(os.path.join(IDN, "runs", "*.json"))):
        r = json.load(open(rec, encoding="utf-8"))
        if r.get("label") == "blinded-strict-flags" and "rows" in r:
            h = hashlib.sha256()
            h.update(("script:" + r["script_sha256"] + "\n").encode())
            h.update(("audit:" + sha(os.path.join(
                HERE, "16_identity_audit.py")) + "\n").encode())
            truth = os.path.join(REPO, "exam-prep", "blind-proof",
                                 "strict-flags", "truth-strict-flags.csv")
            h.update(("truth:" + sha(truth) + "\n").encode())
            import lab_cards  # noqa
            d = os.path.join(REPO, "exam-prep", "blind-proof", "strict-flags",
                             "cards")
            for n in sorted(os.listdir(d)):
                if n.endswith(".md"):
                    h.update(("%s:%s\n" % (n[:-3], sha(os.path.join(d, n))))
                             .encode())
            if h.hexdigest()[:16] == r["run"]:
                res = r
    no = [x for x in res["rows"]
          if x["time_overlapping_neighbours_forbidden"] == "no"][0]
    yes = [x for x in res["rows"]
           if x["time_overlapping_neighbours_forbidden"] == "yes"][0]
    need("JQ-R04-GATE.md", "from %s to %s (line %s; residual diagnostic run\n`%s`"
         % (f4(no["nn_same_coin_accuracy"]), f4(yes["nn_same_coin_accuracy"]),
            f4(yes["chance_1pct"]), res["run"]), "residual %s" % res["run"])

    # ---------------- JQ-R04-CONTENT ---------------------------------------
    k1_run, k1, _ = A["blinded-strict-flags-k1"]
    for fam, lab in (("trades-level", "typical level of the ranked column"),
                     ("repeat-trades",
                      "how many values repeat in the column")):
        x = sf[fam]
        need("JQ-R04-CONTENT.md",
             "| %s | **%s** (%s) — beats | **%s** (%s) — beats |"
             % (lab, f4(x["pair_auc"]), f4(x["auc_chance_1pct"]),
                f4(x["nn_tie_free"]), f4(x["nn_tie_free_chance_1pct"])),
             "audit %s %s" % (sf_run, fam))
    man = open(os.path.join(REPO, "exam-prep", "second-fix", "blind-proof",
                            "strict-flags-k1",
                            "blind-manifest-strict-flags-k1.md"),
               encoding="utf-8").read()
    ties = dict(re.findall(r"^\| (\d) \| (\d+) \|$", man, re.M)[-2:])
    for dp, rows, lab in (("2", sf, "2 decimals (first run)"),
                          ("3", k1, "3 decimals (the fewest at which "
                                    "rounding makes no new repeats)")):
        rc, gr = rows["repeat-close"], rows["granularity-close"]
        need("JQ-R04-CONTENT.md",
             "| %s | %s | **%s** (%s) | **%s** (%s) | **%s** (%s) | **%s** (%s) |"
             % (lab, ties[dp], f4(rc["pair_auc"]), f4(rc["auc_chance_1pct"]),
                f4(rc["nn_tie_free"]), f4(rc["nn_tie_free_chance_1pct"]),
                f4(gr["pair_auc"]), f4(gr["auc_chance_1pct"]),
                f4(gr["nn_tie_free"]), f4(gr["nn_tie_free_chance_1pct"])),
             "audits %s / %s; k1 manifest" % (sf_run, k1_run))
        for fam in ("repeat-close", "granularity-close"):
            for col in ("auc_beats_chance", "nn_tie_free_beats_chance"):
                if rows[fam][col] != "YES":
                    raise SystemExit("%s %s %s not YES" % (dp, fam, col))
    need("JQ-R04-CONTENT.md", "audit run\n`%s`" % sf_run, "run id")
    need("JQ-R04-CONTENT.md", "`%s` (2 decimals)" % sf_run, "run id")
    need("JQ-R04-CONTENT.md", "`%s` (3 decimals)" % k1_run, "run id")

    # ---------------- JQ-R04-DATE ------------------------------------------
    t4 = A["blinded-strict-flags"][2]["t4_release_names"]
    need("JQ-R04-DATE.md", "run `%s`, T4" % sf_run, "run id")
    need("JQ-R04-DATE.md", "**%d of 306** cards print at least one US release "
         "name; **%d** distinct" % (t4["cards_printing_a_release_name"],
                                    t4["distinct_release_names"]), "T4")
    need("JQ-R04-DATE.md", "**%d** of the %d names fall on exactly one release "
         "day" % (len(t4["names_on_exactly_one_release_day_of_this_set"]),
                  t4["distinct_release_names"]), "T4")
    need("JQ-R04-DATE.md", "**%d** cards carry one of them. The %d:"
         % (t4["cards_carrying_such_a_name_by_release_day"],
            len(t4["names_on_exactly_one_release_day_of_this_set"])), "T4")
    flat = re.sub(r"\s+", " ", texts["JQ-R04-DATE.md"])
    names_ok = all(n in flat for n in
                   t4["names_on_exactly_one_release_day_of_this_set"])
    checks.append({"file": "JQ-R04-DATE.md", "text": "every one of the %d "
                   "release-day names" % len(
                       t4["names_on_exactly_one_release_day_of_this_set"]),
                   "source": "T4", "found": names_ok})
    raw2 = list(csv.DictReader(open(os.path.join(
        REPO, "exam-prep", "second-fix", "identity", "run-13d935bb5cf78346",
        "hour-linkage-raw-observation.csv"), encoding="utf-8")))
    be = [x for x in raw2 if x["columns"] == "BTC+ETH"][0]
    nonshar = int(be["pairs"]) - int(be["truly_sharing_hours"])
    need("JQ-R04-DATE.md", "**%s of the %s** card" % (be["detected_of_those"],
                                                     be["truly_sharing_hours"]),
         "raw T3 13d935bb5cf78346")
    need("JQ-R04-DATE.md", "**%s false matches among %s,%03d** pairs"
         % (be["false_positives"], nonshar // 1000, nonshar % 1000),
         "raw T3 13d935bb5cf78346")
    off = 0
    for p in glob.glob(os.path.join(REPO, "exam-prep", "blind-proof",
                                    "strict-flags", "cards", "B*.md")):
        for ln in open(p, encoding="utf-8"):
            if "US releases" in ln and "none in these hours" not in ln \
                    and re.search(r"\([-+][0-9]* h\)", ln):
                off += 1
    need("JQ-R04-DATE.md", "**%d** cards print at least one\nrelease with an "
         "hour offset" % off, "grep over strict-flags cards")

    # ---------------- JQ-N1 --------------------------------------------------
    rec26 = None
    for r in glob.glob(os.path.join(OUT_DIR, "runs", "*.json")):
        x = json.load(open(r, encoding="utf-8"))
        if "G-2" in x.get("results", {}):
            rec26 = x
    g2 = {r["config"]: r for r in rec26["results"]["G-2"]["rows"]}
    e4 = json.load(open(os.path.join(
        REPO, "exam-prep", "second-fix", "checks", "runs",
        "35925ca8acf60690.json"), encoding="utf-8"))["results"]["E-4"]["rows"]
    e4 = {(r["config"], r["predictor"]): r for r in e4}
    rows_n1 = [("none", "none/none/none", "synthetic-iid",
                "independent per card"),
               ("start-hour / any", "start-hour/component/any",
                "synthetic-iid", "independent per card"),
               ("start-hour / any", "start-hour/component/any",
                "synthetic-event-constant", "one per event"),
               ("move-window / component / any", "move-window/component/any",
                "synthetic-event-constant", "one per event"),
               ("move-window / greedy-clique / any",
                "move-window/greedy-clique/any", "synthetic-event-constant",
                "one per event"),
               ("card-span / component / any", "card-span/component/any",
                "synthetic-iid", "independent per card"),
               ("card-span / component / any", "card-span/component/any",
                "synthetic-event-constant", "one per event"),
               ("card-span / greedy-clique / any",
                "card-span/greedy-clique/any", "synthetic-event-constant",
                "one per event")]
    for lab, cfg, pred, ans in rows_n1:
        e, g = e4[(cfg, pred)], g2[cfg]
        need("JQ-N1.md", "| %s | %s | %s | %s | %s (%d) | %s | %s – %s |"
             % (lab, ans, f4(e["card"]), f4(e["block_second_fix"]),
                f4(e["representative"]), e["representative_n"],
                f4(g["representative_exact_1pct"]),
                f4(g["reported_stat_2_5pct"]), f4(g["reported_stat_97_5pct"])),
             "E-4 35925ca8acf60690; G-2 %s" % rec26["run"])
    ap = rec26["results"]["G-2"]["p_two_lines_apart_by_steps"]
    need("JQ-N1.md", "with probability %.3f" % ap["2"], "G-2")
    need("JQ-N1.md", "0.0196 or more with probability %.4f" % ap["3"], "G-2")
    if not ap["4"] < 0.0001:
        raise SystemExit("4-step probability not below 0.0001")
    need("JQ-N1.md", "0.0261 or more with probability below 0.0001", "G-2")
    need("JQ-N1.md", "steps of\n  %.4f" % rec26["results"]["G-2"]["support_step"],
         "G-2")
    widths = [g["reported_stat_97_5pct"] - g["reported_stat_2_5pct"]
              for g in g2.values() if 116 <= g["n"] <= 168]
    need("JQ-N1.md", "that range is %.4f to %.4f wide" % (min(widths),
                                                          max(widths)), "G-2")
    g5 = {r["definition"]: r for r in rec26["results"]["G-5"]}
    need("JQ-N1.md", "%d events\n    under move-window and %d under card-span"
         % (g5["move-window"]["events_in_one_partition_only"],
            g5["card-span"]["events_in_one_partition_only"]), "G-5")
    need("JQ-N1.md", "unchanged: %d and %d)"
         % (g5["move-window"]["events_keep_latest"],
            g5["card-span"]["events_keep_latest"]), "G-5")
    p1b = open(os.path.join(REPO, "exam-prep", "review-2", "probes",
                            "p1b.out"), encoding="utf-8").read()
    mm = dict((d, (a, b, c)) for d, a, b, c in re.findall(
        r"p1b (\S+?)/greedy-clique/cross-coin: events earliest-rule (\d+), "
        r"latest-rule (\d+), events not shared by both (\d+)", p1b))
    need("JQ-N1.md", "found %s and %s (card-span: %s events against\n    %s)"
         % (mm["move-window"][2], mm["card-span"][2], mm["card-span"][0],
            mm["card-span"][1]), "review-2 p1b.out")
    summ = {r["config"]: r for r in csv.DictReader(open(os.path.join(
        REPO, "exam-prep", "collapse", "run-bec532fa008e0e01",
        "collapse-summary.csv"), encoding="utf-8"))}
    lab_cfg = {"no collapse": "none/none/none"}
    for c in summ:
        if c != "none/none/none":
            d, r_, s = c.split("/")
            lab_cfg["%s / %s / %s" % (d, "–" if d == "start-hour" else r_,
                                      s)] = c
    for lab, cfg in lab_cfg.items():
        x = summ[cfg]
        vals = [x["events"], x["events_of_size_1"], x["largest_event"],
                x["events_holding_both_kinds"],
                x["events_holding_2plus_cards_of_one_coin"],
                x["largest_same_coin_count_in_one_event"]]
        row = [ln for ln in texts["JQ-N1.md"].split("\n")
               if ln.startswith("| %s |" % lab)]
        got = ([c.strip().strip("*") for c in row[0].strip("|").split("|")][1:]
               if row else None)
        checks.append({"file": "JQ-N1.md", "text": "summary row '%s' = %s"
                       % (lab, vals), "source": "collapse-summary "
                       "bec532fa008e0e01", "found": got == vals})

    # ---------------- JQ-CANTEEN-8 -------------------------------------------
    g3 = rec26["results"]["G-3"]
    sp, bw = g3["card_span"], g3["before_window"]
    for k, lab in (("calm+calm · same coin", "both calm, **same coin**"),
                   ("calm+calm · different coins", "both calm, different "
                    "coins"),
                   ("calm+large · different coins", "one calm, one large, "
                    "different coins"),
                   ("large+large · different coins", "both large, different "
                    "coins")):
        a, b = sp.get(k, 0), bw.get(k, 0)
        cell = ("**%d** | **%d**" % (a, b)) if "same" in k else ("%d | %d"
                                                                 % (a, b))
        need("JQ-CANTEEN-8.md", "| %s | %s |" % (lab, cell), "G-3")
    for k, lab in (("calm+large · same coin", "one calm, one large, same "
                    "coin"), ("large+large · same coin", "both large, same "
                              "coin")):
        need("JQ-CANTEEN-8.md", "| %s | %d | %d |"
             % (lab, sp.get(k, 0), bw.get(k, 0)), "G-3")
    tot = sum(sp.values())
    need("JQ-CANTEEN-8.md", "\"135 calm+calm overlapping pairs out of %d\""
         % tot if sp["calm+calm · same coin"] + sp[
             "calm+calm · different coins"] == 135 else "MISMATCH", "G-3")
    c1011 = [p for p in g3["same_coin_pairs"] if p["pair"] == "C010/C011"][0]
    need("JQ-CANTEEN-8.md", "their cards start %d hours apart, so their "
         "before windows\n  share %d hours and their card spans %d"
         % (c1011["start_gap_hours"], 24 - c1011["start_gap_hours"],
            c1011["shared_hours"]), "G-3")
    need("JQ-CANTEEN-8.md", "`%s` (G-3)" % rec26["run"], "run id")

    # ---------------- JQ-B1 ---------------------------------------------------
    g4 = rec26["results"]["G-4"]
    ok = (g4["contracts_named_by_trigger"] == ["AVGOUSDT", "NOKUSDT"]
          and all(g4["named_contracts_in_observation_list"].values())
          and g4["draw_manifest_disjoint_true"]
          and g4["draw_manifest_observation_x_exam_overlap_empty"])
    checks.append({"file": "JQ-B1.md", "text": "the four facts of 'What is "
                   "established'", "source": "G-4 %s" % rec26["run"],
                   "found": ok})

    # ---------------- line citations ----------------------------------------
    files = {"RULES.md": "RULES.md", "TACTICS.md": "TACTICS.md",
             "canteen/2026-09-19-sofia.md": "canteen/2026-09-19-sofia.md",
             "scripts/06_find_moments.py": "scripts/06_find_moments.py",
             "scripts/04_draw.py": "scripts/04_draw.py"}
    cache = {k: open(os.path.join(REPO, v), encoding="utf-8").read()
             .split("\n") for k, v in files.items()}
    cites = []
    pat = re.compile(r"`(RULES\.md|TACTICS\.md|canteen/2026-09-19-sofia\.md|"
                     r"scripts/06_find_moments\.py|scripts/04_draw\.py)`"
                     r"\s+lines?\s+(\d+)(?:[–-](\d+))?")
    for fname, t in texts.items():
        for m in pat.finditer(re.sub(r"\s+", " ", t)):
            f, a, b = m.group(1), int(m.group(2)), int(m.group(3) or
                                                       m.group(2))
            cites.append({"file": fname, "cites": "%s %d–%d" % (f, a, b),
                          "text": " / ".join(x.strip() for x in
                                             cache[f][a - 1:b])})

    # ---------------- write ---------------------------------------------------
    script_sha = sha(os.path.abspath(__file__))
    h = hashlib.sha256()
    h.update(("script:%s\n" % script_sha).encode())
    for fname in sorted(texts):
        h.update(("%s:%s\n" % (fname, sha(os.path.join(JQ, fname)))).encode())
    h.update(("audit:%s\n" % sha(os.path.join(HERE, "16_identity_audit.py")))
             .encode())
    h.update(("checks26:%s\n" % rec26["run"]).encode())
    run_full = h.hexdigest()
    run16 = run_full[:16]
    failed = [c for c in checks if not c["found"]]
    if "--dry" in sys.argv:
        # a dry run writes nothing: it prints what failed, for editing
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
    L = ["# Juror-file check — run `%s`" % run16, "",
         "Written by `scripts/28_juror_file_check.py` at %s (system clock)."
         % started.strftime("%Y-%m-%dT%H:%M:%SZ"), "",
         "## N · numbers: %d checks, %d failed" % (len(checks), len(failed)),
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
    sys.path.insert(0, HERE)
    main()
