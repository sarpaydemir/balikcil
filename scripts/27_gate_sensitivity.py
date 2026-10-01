#!/usr/bin/env python3
"""
27_gate_sensitivity.py -- criterion K-12 of exam-prep/third-fix/
criteria-written-before-measuring.md: how the acceptance-gate row moves when
feature groups are taken out of it, on one blinded card set.

What it does
------------
Reads a blinded card set and its truth file, computes the audit's features
with scripts/16_identity_audit.py's own card_features(), and recomputes the
`ALL-removable` row three ways:
  (a) as the audit builds it;
  (b) without the families read from the price column (`price-level`,
      `repeat-close`, `granularity-close`);
  (c) as (b), and without every feature read from the trade-count column
      (`trades-level`, `repeat-trades`, and the scale-free shape features of
      `trades`).
Each against its own RULES 12 chance line: pair AUC, nearest neighbour (index
tie-break) and the tie-free nearest neighbour, from the same 1,000 label
shuffles, exactly as the audit does. It builds no card and no rendering: it
answers "what would the gate row read if these features were absent", not
"what would a card without these columns read" -- a card without a column
could carry other traces of it.

Input   : --cards <folder> --truth <csv> --label <name>
Output  : exam-prep/third-fix/checks/gate-sensitivity-<label>-<run16>.md
          exam-prep/third-fix/checks/runs/<run16>.json   (append-only)

Rules implemented
-----------------
RULES 12 : 1,000 shuffles and the best 1%, imported from the audit.
RULES 19 : every number written here is counted by this script.
RULES 23 : the clock is read from the system.
RULES 29 / 30 : run number = SHA-256 of this script, the audit script and
           every input; a recorded run is never rewritten.

Constants: none of its own; SHUFFLES, TOP_FRACTION, SEED, FAMILIES and
FORCED_FAMILIES are imported from the audit. No threshold, score or trading
rule is defined anywhere in this file.
"""

import argparse
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

OUT_DIR = os.path.join(REPO, "exam-prep", "third-fix", "checks")
PRICE_FAMILIES = ("price-level", "repeat-close", "granularity-close")
TRADE_FAMILIES = ("trades-level", "repeat-trades")


def die(msg):
    sys.stderr.write("STOP: %s\n" % msg)
    sys.exit(1)


def sha256_file(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cards", required=True)
    ap.add_argument("--truth", required=True)
    ap.add_argument("--label", required=True)
    args = ap.parse_args()
    started = dt.datetime.now(dt.timezone.utc)
    free_bytes = shutil.disk_usage(REPO).free
    spec = importlib.util.spec_from_file_location(
        "ia", os.path.join(HERE, "16_identity_audit.py"))
    ia = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ia)

    truth = {r["id"]: r for r in csv.DictReader(open(args.truth,
                                                     encoding="utf-8"))}
    names = sorted(f for f in os.listdir(args.cards) if f.endswith(".md"))
    cards = [lab_cards.parse_any_card(os.path.join(args.cards, n))
             for n in names]
    coins = [truth[c["card"]]["coin"] for c in cards]
    feats = [ia.card_features(c) for c in cards]
    allkeys = sorted({k for f in feats for k in f})

    def prefixes(drop):
        return sorted({p for k, v in ia.FAMILIES.items()
                       if k not in ia.FORCED_FAMILIES and k not in drop
                       for p in v})

    variants = [
        ("(a) ALL-removable as audited", prefixes(()), False),
        ("(b) without the price-column families", prefixes(PRICE_FAMILIES),
         False),
        ("(c) as (b), and without the trade-count features",
         prefixes(PRICE_FAMILIES + TRADE_FAMILIES), True),
    ]
    rows = []
    for name, pref, drop_trades in variants:
        keys = ia.select({k: 1 for k in allkeys}, pref)
        if drop_trades:
            keys = [k for k in keys if "trades" not in k]
        vecs, used = ia.standardise(feats, keys)
        d = ia.pair_distances(vecs)
        nn = ia.nearest_neighbours(d)
        ts = ia.nearest_tie_sets(d)
        rank, tot = ia.pair_ranks(d)
        o_nn = ia.nn_accuracy(nn, coins)
        o_tf = ia.nn_tie_free(ts, coins)
        o_auc = ia.pair_auc(rank, tot, coins)
        rng = random.Random(ia.SEED)
        perm = list(coins)
        n_nn, n_tf, n_auc = [], [], []
        for _ in range(ia.SHUFFLES):
            rng.shuffle(perm)
            n_nn.append(ia.nn_accuracy(nn, perm))
            n_tf.append(ia.nn_tie_free(ts, perm))
            n_auc.append(ia.pair_auc(rank, tot, perm))
        l_nn = ia.quantile_top(n_nn, ia.TOP_FRACTION)
        l_tf = ia.quantile_top(n_tf, ia.TOP_FRACTION)
        l_auc = ia.quantile_top(n_auc, ia.TOP_FRACTION)
        rows.append({"variant": name, "features": len(used),
                     "feature_names": used,
                     "cards_with_tied_nn": sum(1 for t in ts if len(t) > 1),
                     "nn": round(o_nn, 6), "nn_line": round(l_nn, 6),
                     "nn_beats": o_nn > l_nn,
                     "nn_tie_free": round(o_tf, 6),
                     "nn_tie_free_line": round(l_tf, 6),
                     "nn_tie_free_beats": o_tf > l_tf,
                     "auc": round(o_auc, 6), "auc_line": round(l_auc, 6),
                     "auc_beats": o_auc > l_auc})

    script_sha = sha256_file(os.path.abspath(__file__))
    h = hashlib.sha256()
    h.update(("script:%s\n" % script_sha).encode())
    h.update(("audit:%s\n" % sha256_file(os.path.join(
        HERE, "16_identity_audit.py"))).encode())
    h.update(("lab_cards:%s\n" % sha256_file(os.path.join(
        HERE, "lab_cards.py"))).encode())
    h.update(("truth:%s\n" % sha256_file(args.truth)).encode())
    for c in cards:
        h.update(("%s:%s\n" % (c["card"], c["sha256"])).encode())
    run_full = h.hexdigest()
    run16 = run_full[:16]
    core = json.loads(json.dumps({
        "run": run16, "input_fingerprint": run_full, "label": args.label,
        "cards_folder": os.path.relpath(args.cards, REPO),
        "script_sha256": script_sha, "rows": rows}))
    runs_dir = os.path.join(OUT_DIR, "runs")
    os.makedirs(runs_dir, exist_ok=True)
    rec = os.path.join(runs_dir, run16 + ".json")
    if os.path.exists(rec):
        if json.load(open(rec, encoding="utf-8")) != core:
            die("run record %s exists with different content (RULES 30)"
                % rec)
        sys.stderr.write("run %s already recorded; nothing written\n" % run16)
        return
    A = ["# Gate sensitivity — card set `%s`, run `%s`" % (args.label, run16),
         "", "Written by `scripts/27_gate_sensitivity.py` (criterion K-12). "
         "Feature subsets of the gate row, not renderings: no card was "
         "built. **Not for juror files.**", "",
         "| field | value |", "|---|---|",
         "| run number (RULES 29) | `%s` |" % run16,
         "| full input fingerprint | `%s` |" % run_full,
         "| written at (system clock, UTC, RULES 23) | %s |"
         % started.strftime("%Y-%m-%dT%H:%M:%SZ"),
         "| free disk space at start (bytes) | %d |" % free_bytes,
         "| card folder | `%s` |" % os.path.relpath(args.cards, REPO),
         "| `scripts/16_identity_audit.py` SHA-256 | `%s` |"
         % sha256_file(os.path.join(HERE, "16_identity_audit.py")),
         "| `scripts/27_gate_sensitivity.py` SHA-256 | `%s` |" % script_sha,
         "", "| variant | features | cards with a tied nearest neighbour | "
         "nearest neighbour (line) | tie-free nearest neighbour (line) | "
         "pair AUC (line) |", "|---|---|---|---|---|---|"]
    for r in rows:
        A.append("| %s | %d | %d | %.6f (%.6f) %s | %.6f (%.6f) %s | "
                 "%.6f (%.6f) %s |"
                 % (r["variant"], r["features"], r["cards_with_tied_nn"],
                    r["nn"], r["nn_line"], "beats" if r["nn_beats"] else "no",
                    r["nn_tie_free"], r["nn_tie_free_line"],
                    "beats" if r["nn_tie_free_beats"] else "no",
                    r["auc"], r["auc_line"],
                    "beats" if r["auc_beats"] else "no"))
    A += ["", "Features in each variant:", ""]
    for r in rows:
        A.append("- %s: %s" % (r["variant"], ", ".join(
            "`%s`" % f for f in r["feature_names"])))
    A.append("")
    path = os.path.join(OUT_DIR, "gate-sensitivity-%s-%s.md"
                        % (args.label, run16))
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(A) + "\n")
    with open(rec, "w", encoding="utf-8") as fh:
        json.dump(core, fh, indent=1, sort_keys=True)
        fh.write("\n")
    sys.stderr.write("run %s written\n" % run16)


if __name__ == "__main__":
    main()
