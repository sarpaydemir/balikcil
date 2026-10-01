#!/usr/bin/env python3
"""
25_instrument_checks.py -- check the instruments as changed by the second-fix
run, and measure the two things the changes need a number for.

What it does
------------
  E-1  Regression: the changed scripts/17_blind_cards.py, run in memory with
       each reviewed configuration and `--close-dp 2`, must produce every one
       of the 1,224 committed blinded cards byte for byte. (Nothing is
       written; the committed cards are only read.)
  E-2  The guards of the changed scripts/15_event_collapse.py: what
       chance_line() accepts and refuses, and what its record carries. The
       same attempts REVIEW §4.3 made, plus the new ones.
  E-3  Criterion K-4 (exam-prep/second-fix/criteria-written-before-
       measuring.md): the granularity probe on the rebased `close` -- the
       smallest non-zero difference between two printed `close` values of a
       card -- attacked with the audit's two attacks and chance lines, on the
       reviewed rendering (`strict-flags`) and on the K-1 rendering
       (`strict-flags-k1`).
  E-4  The shuffle-calibration table of the reviewed collapse run
       (`386d234b85269a21`) set against the second-fix run
       (`756cf4ea156d92c3`), column by column, with the differences counted
       here rather than by hand.

Input   : cards/ ; exam-prep/blind-proof/{ratio,rank,strict,strict-flags}/ ;
          exam-prep/second-fix/blind-proof/strict-flags-k1/ ;
          exam-prep/collapse/shuffle-calibration.csv ;
          exam-prep/collapse/run-756cf4ea156d92c3/shuffle-calibration.csv
Output  : exam-prep/second-fix/checks/instrument-checks-<run16>.md
          exam-prep/second-fix/checks/runs/<run16>.json   (append-only)

Rules implemented
-----------------
RULES 12 : 1,000 shuffles and the best 1%, imported from the audit.
RULES 19 : every number written here is counted by this script.
RULES 23 : the clock is read from the system.
RULES 29 / 30 : run number = SHA-256 of this script, the scripts it imports
           and every input; a recorded run is never rewritten.

Constants: REVIEWED_RUNS lists the four blinding run numbers the review
reproduced (REVIEW §8); their configuration strings are read from those run
records, not retyped. Every other constant is imported. No threshold, score
or trading rule is defined anywhere in this file.
"""

import csv
import datetime as dt
import hashlib
import importlib.util
import json
import os
import random
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import lab_cards  # noqa: E402

REVIEWED_RUNS = {"ratio": "ca9e460829ecdac5", "rank": "35df01d621d8da5a",
                 "strict": "a9a8f3bcd515fd62",
                 "strict-flags": "10405ae115941d40"}
COLLAPSE_RUN_REVIEWED = "386d234b85269a21"
COLLAPSE_RUN_NEW = "756cf4ea156d92c3"
OUT_DIR = os.path.join(REPO, "exam-prep", "second-fix", "checks")


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name,
                                                  os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def sha256_file(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def die(msg):
    sys.stderr.write("STOP: %s\n" % msg)
    sys.exit(1)


def main():
    started = dt.datetime.now(dt.timezone.utc)
    free_bytes = shutil.disk_usage(REPO).free
    bc = load("bc", "17_blind_cards.py")
    ec = load("ec", "15_event_collapse.py")
    ia = load("ia", "16_identity_audit.py")
    inputs = []

    def use(p):
        inputs.append((os.path.relpath(p, REPO), sha256_file(p)))
        return p

    raw = lab_cards.load_all(os.path.join(REPO, "cards"))
    R = {}

    # ---- E-1 regression -----------------------------------------------------
    e1 = []
    rng = random.Random(bc.SEED)
    order = list(range(len(raw)))
    rng.shuffle(order)
    assign = {raw[src]["card"]: "B%03d" % (i + 1)
              for i, src in enumerate(order)}
    for v, run in REVIEWED_RUNS.items():
        d = os.path.join(REPO, "exam-prep", "blind-proof", v)
        rec = json.load(open(use(os.path.join(d, "runs", run + ".json")),
                             encoding="utf-8"))
        cfg = dict(kv.split("=") for kv in rec["config"].split(";"))
        same = differ = 0
        first_diff = None
        for c in raw:
            cid = assign[c["card"]]
            text, _ = bc.build_card(c, cid, cfg["levels"], cfg["btceth"],
                                    cfg["funding"], cfg["takerbuy"], cfg["p7"],
                                    bc.CLOSE_DP_REVIEWED)
            with open(use(os.path.join(d, "cards", cid + ".md")),
                      encoding="utf-8") as fh:
                if fh.read() == text:
                    same += 1
                else:
                    differ += 1
                    first_diff = first_diff or cid
        e1.append({"variant": v, "reviewed_run": run, "config": rec["config"],
                   "identical": same, "different": differ,
                   "first_different": first_diff})
    R["E-1"] = e1

    # ---- E-2 engine guards --------------------------------------------------
    moments = [{"id": c["card"], "coin": c["coin"], "kind": c["kind"],
                "start_dt": ec.parse_hour(c["start_hour_utc"])} for c in raw]
    ids = sorted(m["id"] for m in moments)
    by = {m["id"]: m for m in moments}
    labels = [1 if by[i]["kind"] == "large" else 0 for i in ids]
    r0 = random.Random(ec.SEED)
    answers = [r0.randint(0, 1) for _ in ids]
    cs = ec.collapse(moments, "card-span", "component", "any")
    sh = ec.collapse(moments, "start-hour", "component", "any")
    e2 = []

    def attempt(name, fn):
        try:
            out = fn()
            e2.append({"attempt": name, "result": "accepted",
                       "detail": out})
        except Exception as e:      # the point is to record what is raised
            e2.append({"attempt": name, "result": type(e).__name__,
                       "detail": str(e)[:160]})

    def summary(rec):
        return {k: rec[k] for k in ("config", "mode", "events", "n_in_null",
                                    "identity_partition", "event_map_sha256")
                if k in rec} | ({"immovable_events": rec["immovable_events"],
                                 "cards_in_immovable_events":
                                     rec["cards_in_immovable_events"]}
                                if "immovable_events" in rec else {})

    attempt("events as a plain list of lists (the reviewed interface)",
            lambda: ec.chance_line(answers, labels, [list(e) for e in cs],
                                   ids, "block"))
    attempt("identity partition typed as a plain list (REVIEW §4.3 bypass)",
            lambda: ec.chance_line(answers, labels, [[i] for i in ids], ids,
                                   "block"))
    attempt("identity_map(), block",
            lambda: summary(ec.chance_line(answers, labels,
                                           ec.identity_map(moments), ids,
                                           "block")))
    attempt("a start-hour map relabelled as card-span/component/any",
            lambda: ec.chance_line(answers, labels, ec.EventMap(
                list(sh), "card-span", "component", "any", moments), ids,
                "block"))
    attempt("a card-span map with one card removed from its events",
            lambda: ec.chance_line(answers, labels, ec.EventMap(
                [e for e in cs if ids[0] not in e], "card-span", "component",
                "any", moments), ids, "block"))
    attempt("mode omitted",
            lambda: ec.chance_line(answers, labels, cs, ids))
    attempt("mode='card'",
            lambda: ec.chance_line(answers, labels, cs, ids, "card"))
    attempt("representative without `representatives`",
            lambda: ec.chance_line(answers, labels, cs, ids,
                                   "representative"))
    attempt("representative naming two cards of one event",
            lambda: ec.chance_line(answers, labels, cs, ids, "representative",
                                   representatives=[e[0] for e in cs][:-1]
                                   + [next(e for e in cs if len(e) > 1)[1]]))
    attempt("card-span/component/any, block",
            lambda: summary(ec.chance_line(answers, labels, cs, ids,
                                           "block")))
    attempt("card-span/component/any, representative (first id of each "
            "event, a test choice only)",
            lambda: summary(ec.chance_line(answers, labels, cs, ids,
                                           "representative",
                                           representatives=[e[0]
                                                            for e in cs])))

    def unpack3():
        a, b, c = ec.chance_line(answers, labels, cs, ids, "block")
        return "unpacked"
    attempt("old-style unpacking `observed, boundary, null = chance_line(...)`",
            unpack3)
    R["E-2"] = e2

    # ---- E-3 granularity probe (K-4) ---------------------------------------
    sets = {"strict-flags": os.path.join(REPO, "exam-prep", "blind-proof",
                                         "strict-flags"),
            "strict-flags-k1": os.path.join(REPO, "exam-prep", "second-fix",
                                            "blind-proof", "strict-flags-k1")}
    e3 = []
    for label, d in sets.items():
        truth = {r["id"]: r for r in csv.DictReader(open(use(os.path.join(
            d, "truth-%s.csv" % label)), encoding="utf-8"))}
        names = sorted(f for f in os.listdir(os.path.join(d, "cards"))
                       if f.endswith(".md"))
        cards = [lab_cards.parse_any_card(use(os.path.join(d, "cards", n)))
                 for n in names]
        coins = [truth[c["card"]]["coin"] for c in cards]
        feats = []
        dps = set()
        for c in cards:
            vals = sorted(set(c["cols"]["close"]))
            gaps = [b - a for a, b in zip(vals, vals[1:]) if b - a > 0]
            feats.append({"gran:min_step": min(gaps) if gaps else 0.0})
        # the printed decimals, read off the card text
        for c in cards[:1]:
            with open(c["path"], encoding="utf-8") as fh:
                for ln in fh:
                    if ln.startswith("| -24 |"):
                        dps.add(len(ln.split("|")[2].strip().split(".")[1]))
        vecs, used = ia.standardise(feats, ["gran:min_step"])
        dists = ia.pair_distances(vecs)
        nn_idx = ia.nearest_neighbours(dists)
        rank, total = ia.pair_ranks(dists)
        obs_nn = ia.nn_accuracy(nn_idx, coins)
        obs_auc = ia.pair_auc(rank, total, coins)
        rng = random.Random(ia.SEED)
        perm = list(coins)
        null_nn, null_auc = [], []
        for _ in range(ia.SHUFFLES):
            rng.shuffle(perm)
            null_nn.append(ia.nn_accuracy(nn_idx, perm))
            null_auc.append(ia.pair_auc(rank, total, perm))
        nl = ia.quantile_top(null_nn, ia.TOP_FRACTION)
        al = ia.quantile_top(null_auc, ia.TOP_FRACTION)
        e3.append({"card_set": label, "close_decimals": sorted(dps),
                   "nn": round(obs_nn, 6), "nn_line": round(nl, 6),
                   "nn_beats": obs_nn > nl,
                   "auc": round(obs_auc, 6), "auc_line": round(al, 6),
                   "auc_beats": obs_auc > al,
                   "distinct_min_step_values":
                       len({f["gran:min_step"] for f in feats})})
    R["E-3"] = e3

    # ---- E-4 calibration, reviewed vs second-fix ---------------------------
    old = {(r["config"], r["predictor"]): r for r in csv.DictReader(open(use(
        os.path.join(REPO, "exam-prep", "collapse",
                     "shuffle-calibration.csv")), encoding="utf-8"))}
    new = {(r["config"], r["predictor"]): r for r in csv.DictReader(open(use(
        os.path.join(REPO, "exam-prep", "collapse",
                     "run-" + COLLAPSE_RUN_NEW, "shuffle-calibration.csv")),
        encoding="utf-8"))}
    e4 = []
    for k in old:
        o, n = old[k], new[k]
        card = float(n["card_shuffle_1pct_boundary"])
        e4.append({"config": k[0], "predictor": k[1],
                   "card": card,
                   "block_reviewed": float(o["block_shuffle_1pct_boundary"]),
                   "block_second_fix": float(n["block_shuffle_1pct_boundary"]),
                   "representative": float(
                       n["representative_shuffle_1pct_boundary"]),
                   "representative_n": int(n["representative_n"]),
                   "card_and_representative_unchanged":
                       o["card_shuffle_1pct_boundary"]
                       == n["card_shuffle_1pct_boundary"]
                       and o["representative_shuffle_1pct_boundary"]
                       == n["representative_shuffle_1pct_boundary"]})
    collapsed = [r for r in e4 if r["config"] != "none/none/none"]
    rng_rev = [round(r["block_reviewed"] - r["card"], 6) for r in collapsed]
    rng_new = [round(r["block_second_fix"] - r["card"], 6) for r in collapsed]
    rng_rep = [round(r["representative"] - r["card"], 6) for r in collapsed]
    R["E-4"] = {"rows": e4,
                "block_minus_card_reviewed": [min(rng_rev), max(rng_rev)],
                "block_minus_card_second_fix": [min(rng_new), max(rng_new)],
                "representative_minus_card": [min(rng_rep), max(rng_rep)],
                "none_block_vs_card": [
                    r for r in e4 if r["config"] == "none/none/none"]}

    # ---- run number, write once ---------------------------------------------
    script_sha = sha256_file(os.path.abspath(__file__))
    h = hashlib.sha256()
    h.update(("script:%s\n" % script_sha).encode())
    for f in ("15_event_collapse.py", "16_identity_audit.py",
              "17_blind_cards.py", "lab_cards.py"):
        h.update(("%s:%s\n" % (f, sha256_file(os.path.join(HERE, f))))
                 .encode())
    for name, sha in sorted(set(inputs)):
        h.update(("%s:%s\n" % (name, sha)).encode())
    for c in raw:
        h.update(("%s:%s\n" % (c["card"], c["sha256"])).encode())
    run_full = h.hexdigest()
    run16 = run_full[:16]
    core = json.loads(json.dumps({"run": run16, "input_fingerprint": run_full,
                                  "script_sha256": script_sha,
                                  "results": R}, default=str))
    runs_dir = os.path.join(OUT_DIR, "runs")
    os.makedirs(runs_dir, exist_ok=True)
    rec_path = os.path.join(runs_dir, run16 + ".json")
    if os.path.exists(rec_path):
        if json.load(open(rec_path, encoding="utf-8")) != core:
            die("run record %s exists with different content (RULES 30)"
                % rec_path)
        sys.stderr.write("run %s already recorded; nothing written\n" % run16)
        return

    A = ["# Instrument checks — run `%s`" % run16, "",
         "Written by `scripts/25_instrument_checks.py`. Every number below is "
         "counted by that script.", "",
         "| field | value |", "|---|---|",
         "| run number (RULES 29) | `%s` |" % run16,
         "| full input fingerprint | `%s` |" % run_full,
         "| written at (system clock, UTC, RULES 23) | %s |"
         % started.strftime("%Y-%m-%dT%H:%M:%SZ"),
         "| free disk space at start (bytes) | %d |" % free_bytes,
         "| `scripts/25_instrument_checks.py` SHA-256 | `%s` |" % script_sha,
         "", "## E-1 · the changed blinding script reproduces every reviewed "
         "card", "",
         "| variant | reviewed run | configuration | identical | different |",
         "|---|---|---|---|---|"]
    for r in e1:
        A.append("| `%s` | `%s` | `%s` | %d | %d |"
                 % (r["variant"], r["reviewed_run"], r["config"],
                    r["identical"], r["different"]))
    A += ["", "## E-2 · what `chance_line()` accepts and refuses", "",
          "| attempt | result | detail |", "|---|---|---|"]
    for r in e2:
        A.append("| %s | %s | %s |" % (r["attempt"], r["result"],
                                       json.dumps(r["detail"], default=str)
                                       .replace("|", "/")))
    A += ["", "## E-3 · K-4, the granularity probe on the rebased `close`",
          "", "One feature: the smallest non-zero difference between two "
          "printed `close` values of a card. The audit's two attacks, 1,000 "
          "shuffles, best 1%.", "",
          "| card set | `close` decimals | distinct feature values | nn | "
          "line | beats | pair AUC | line | beats |",
          "|---|---|---|---|---|---|---|---|---|"]
    for r in e3:
        A.append("| `%s` | %s | %d | %.6f | %.6f | %s | %.6f | %.6f | %s |"
                 % (r["card_set"], r["close_decimals"],
                    r["distinct_min_step_values"], r["nn"], r["nn_line"],
                    "YES" if r["nn_beats"] else "no", r["auc"], r["auc_line"],
                    "YES" if r["auc_beats"] else "no"))
    A += ["", "## E-4 · the shuffle calibration, reviewed run `%s` against "
          "second-fix run `%s`" % (COLLAPSE_RUN_REVIEWED, COLLAPSE_RUN_NEW),
          "", "Card-level and representative columns are unchanged in every "
          "row: %s." % all(r["card_and_representative_unchanged"]
                           for r in e4), "",
          "| configuration | predictor | card-level | block, reviewed "
          "(withdrawn) | block, second-fix | representative (n) |",
          "|---|---|---|---|---|---|"]
    for r in e4:
        A.append("| `%s` | %s | %.4f | %.4f | %.4f | %.4f (%d) |"
                 % (r["config"], r["predictor"], r["card"],
                    r["block_reviewed"], r["block_second_fix"],
                    r["representative"], r["representative_n"]))
    x = R["E-4"]
    A += ["", "Over the ten collapsed configurations and both predictors "
          "(20 rows): block minus card-level, reviewed function: %+.4f to "
          "%+.4f; second-fix function: %+.4f to %+.4f; representative minus "
          "card-level: %+.4f to %+.4f."
          % (x["block_minus_card_reviewed"][0],
             x["block_minus_card_reviewed"][1],
             x["block_minus_card_second_fix"][0],
             x["block_minus_card_second_fix"][1],
             x["representative_minus_card"][0],
             x["representative_minus_card"][1]),
          "", "Reference for the size of Monte Carlo noise: under "
          "`none/none/none` every event is one card, so the block shuffle "
          "and the card-level shuffle draw from the same null distribution; "
          "their two 1%% boundaries, from the same seed, are %.4f and %.4f."
          % (x["none_block_vs_card"][0]["block_second_fix"],
             x["none_block_vs_card"][0]["card"]), ""]
    md_path = os.path.join(OUT_DIR, "instrument-checks-%s.md" % run16)
    if os.path.exists(md_path):
        die("%s exists without a run record" % md_path)
    with open(md_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(A) + "\n")
    with open(rec_path, "w", encoding="utf-8") as fh:
        json.dump(core, fh, indent=1, sort_keys=True)
        fh.write("\n")
    sys.stderr.write("run %s written\n" % run16)


if __name__ == "__main__":
    main()
