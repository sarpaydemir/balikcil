#!/usr/bin/env python3
"""
exam_27_find_moments.py -- the large-movement and calm moments of the exam
                           coins (TACTICS 2), found by the very code that found
                           the observation moments.

What it does
------------
1. Self-check. Loads scripts/06_find_moments.py as a module (it is NOT modified
   and its main() is NOT called) and re-runs its procedure on the observation
   inputs exactly as 06 did: data/draw/observation-coins.txt, the hourly klines
   under data/observation/klines_1h/, seed 20260913. The rebuilt moments.csv
   must be byte-identical to data/moments/moments.csv and the rebuilt run
   number must equal the one in data/moments/moment-manifest.md. If either
   differs, the script stops: the imported procedure would not be the one that
   produced the observation moments.
2. Input check. Every hourly kline zip of every exam coin must be listed in the
   exam archive inventory (exam/acquisition/archive-inventory-*.json) with the
   same SHA-256 it has on disk. Otherwise the script stops.
3. Runs 06's find_for_symbol() and load_hourly() unchanged on the exam coins,
   with 06's KLINES_DIR pointed at exam/data/klines_1h/. Randomness is consumed
   exactly as in 06: one random.Random(SEED), one rng.sample per symbol,
   symbols in alphabetical order. Rows are written in 06's format.
4. Writes the pool report: per exam coin, by LINE NUMBER in
   exam/draw/exam-coins.txt, how many large and how many calm moments it has,
   and the totals. It chooses nothing: no moment is selected for a card here.

Coin names are read at run time from exam/draw/exam-coins.txt. No coin name is
written in this file; the pool report and the console output use line numbers.

Input   : scripts/06_find_moments.py         (imported, unchanged)
          exam/draw/exam-coins.txt
          exam/data/klines_1h/<SYM>/*.zip      (from exam_24)
          exam/acquisition/archive-inventory-*.json
          data/draw/observation-coins.txt, data/observation/klines_1h/,
          data/moments/moments.csv, data/moments/moment-manifest.md (self-check)
Output  : exam/moments/moments.csv       one row per moment, 06's columns
          exam/moments/lifetimes.json    06's per-coin notes
          exam/moments/pool-report.json  counts by coin line number, totals,
                                         measured checks, fingerprints
          exam/moments/runs.jsonl        one line per attempt, append-only,
                                         with start/finish times (system clock)
Rules   : TACTICS 2 as read by the ratified verdicts
          decisions/2026-09-19-large-moment-selection (separation applied
          during selection) and decisions/2026-09-19-calm-separation and
          2026-10-01-jq-n1-canteen-8 part a (no calm-to-calm spacing);
          RULES 19, 20, 21, 23, 29, 30.

Run number (RULES 29): computed with 06's own formula -- SHA-256 over, for each
exam coin in alphabetical order and each of its kline zips in name order, the
zip's file name followed by its SHA-256, then "seed=<SEED>". The same klines and
the same seed always give the same number and the same moments.
Records (RULES 30): moments.csv, lifetimes.json and pool-report.json contain no
clock reading; if one already exists with different content the script stops
and writes nothing. Times go only into the append-only runs.jsonl.

Randomness: seed 20260913 = 06's SEED (TACTICS 1 draw number), read from 06.
Usage    : python3 -B scripts/exam_27_find_moments.py
"""

import csv
import glob
import hashlib
import importlib.util
import io
import json
import os
import random
import re
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lab_archive import sha256_bytes, sha256_file, utc_now_iso  # noqa: E402

# ---------------------------------------------------------------- constants --
# None of the procedure's numbers live here: SEED, the 20/18/48/72/24 values and
# the period bounds are all taken from scripts/06_find_moments.py at run time.
SCRIPT_PATH = os.path.abspath(__file__)
ROOT = os.path.dirname(HERE)
SCRIPT_06 = os.path.join(HERE, "06_find_moments.py")

OBS_LIST = os.path.join(ROOT, "data", "draw", "observation-coins.txt")
OBS_KLINES = os.path.join(ROOT, "data", "observation", "klines_1h")
OBS_MOMENTS = os.path.join(ROOT, "data", "moments", "moments.csv")
OBS_MANIFEST = os.path.join(ROOT, "data", "moments", "moment-manifest.md")

COIN_LIST = os.path.join(ROOT, "exam", "draw", "exam-coins.txt")
EXAM_KLINES = os.path.join(ROOT, "exam", "data", "klines_1h")
ACQ_DIR = os.path.join(ROOT, "exam", "acquisition")
OUT_DIR = os.path.join(ROOT, "exam", "moments")
MOMENTS_CSV = os.path.join(OUT_DIR, "moments.csv")
LIFETIMES_JSON = os.path.join(OUT_DIR, "lifetimes.json")
POOL_JSON = os.path.join(OUT_DIR, "pool-report.json")
RUNS_PATH = os.path.join(OUT_DIR, "runs.jsonl")

# TACTICS 6 numbers, quoted only so the report can set the pool beside them.
# They select nothing in this script.
TACTICS6_CARDS_LARGE = 200
TACTICS6_CARDS_CALM = 200


def load_06():
    spec = importlib.util.spec_from_file_location("find_moments_06", SCRIPT_06)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def read_list(path):
    with open(path, "r", encoding="utf-8") as fh:
        return [ln.strip() for ln in fh if ln.strip()]


def run_fingerprint(m06, klines_dir, symbols):
    """06's main() formula, verbatim in effect."""
    fp = hashlib.sha256()
    files = []
    for sym in sorted(symbols):
        d = os.path.join(klines_dir, sym)
        for name in sorted(os.listdir(d)) if os.path.isdir(d) else []:
            if name.endswith(".zip"):
                p = os.path.join(d, name)
                h = sha256_file(p)
                files.append((os.path.relpath(p, ROOT), h))
                fp.update((name + h).encode())
    fp.update(("seed=%d" % m06.SEED).encode())
    return fp.hexdigest(), files


def run_procedure(m06, klines_dir, symbols):
    """06's main() loop and row format, with KLINES_DIR pointed at klines_dir."""
    m06.KLINES_DIR = klines_dir
    rng = random.Random(m06.SEED)
    all_moments, notes = [], []
    for sym in sorted(symbols):                      # fixed order: alphabetical
        bars = m06.load_hourly(sym)
        res = m06.find_for_symbol(sym, bars, rng)
        notes.append(res["note"])
        all_moments.extend(res["moments"])
    all_moments.sort(key=lambda m: (m["symbol"], m["start_ms"]))
    rows = [["moment_id", "symbol", "kind", "start_hour_utc", "start_ms",
             "move_24h_pct", "rank_in_coin"]]
    for m in all_moments:
        mid = "%s-%s-%s" % (m["symbol"], m["kind"][0].upper(),
                            m06.iso(m["start_ms"]).replace("-", "").replace(":", "").replace("Z", ""))
        rows.append([mid, m["symbol"], m["kind"], m06.iso(m["start_ms"]),
                     m["start_ms"], "%.4f" % (m["move_24h"] * 100.0),
                     m["rank_in_coin"]])
    body = io.StringIO()
    csv.writer(body, lineterminator="\n").writerows(rows)
    return all_moments, notes, body.getvalue()


def write_once(path, text):
    blob = text.encode("utf-8")
    if os.path.exists(path):
        with open(path, "rb") as fh:
            old = fh.read()
        if old == blob:
            return "identical, not rewritten"
        raise SystemExit("STOP (RULES 30): %s exists with different content "
                         "(sha256 %s vs new %s); nothing written"
                         % (os.path.relpath(path, ROOT), sha256_bytes(old), sha256_bytes(blob)))
    with open(path + ".tmp", "wb") as fh:
        fh.write(blob)
    os.replace(path + ".tmp", path)
    return "written"


def append_run(row):
    with open(RUNS_PATH, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, sort_keys=True) + "\n")
        fh.flush()
        os.fsync(fh.fileno())


def main() -> int:
    started = utc_now_iso()
    os.makedirs(OUT_DIR, exist_ok=True)
    m06 = load_06()
    attempt = {"script": "scripts/exam_27_find_moments.py",
               "script_sha256": sha256_file(SCRIPT_PATH),
               "procedure_script": "scripts/06_find_moments.py",
               "procedure_script_sha256": sha256_file(SCRIPT_06),
               "coin_list_sha256": sha256_file(COIN_LIST),
               "started_at_utc": started}

    # -- 1. self-check against the observation moments -----------------------
    obs_syms = read_list(OBS_LIST)
    obs_fp, _ = run_fingerprint(m06, OBS_KLINES, obs_syms)
    _, _, obs_text = run_procedure(m06, OBS_KLINES, obs_syms)
    with open(OBS_MOMENTS, "rb") as fh:
        obs_disk = fh.read()
    with open(OBS_MANIFEST, "r", encoding="utf-8") as fh:
        mm = re.search(r"full input fingerprint \| `([0-9a-f]{64})`", fh.read())
    self_check = {
        "observation_moments_sha256_on_disk": sha256_bytes(obs_disk),
        "observation_moments_sha256_rebuilt": sha256_bytes(obs_text.encode("utf-8")),
        "observation_run_fingerprint_in_manifest": mm.group(1) if mm else None,
        "observation_run_fingerprint_rebuilt": obs_fp,
    }
    self_check["identical"] = (
        self_check["observation_moments_sha256_on_disk"] == self_check["observation_moments_sha256_rebuilt"]
        and self_check["observation_run_fingerprint_in_manifest"] == obs_fp)
    print("self-check:", json.dumps(self_check, indent=1), flush=True)
    attempt["self_check"] = self_check
    if not self_check["identical"]:
        attempt.update({"finished_at_utc": utc_now_iso(),
                        "outcome": "STOPPED: imported 06 procedure does not reproduce "
                                   "the observation moments"})
        append_run(attempt)
        print(attempt["outcome"])
        return 3

    # -- 2. exam kline inputs must match the acquisition inventory ------------
    coins = read_list(COIN_LIST)
    line_of = {c: i + 1 for i, c in enumerate(coins)}
    invs = sorted(glob.glob(os.path.join(ACQ_DIR, "archive-inventory-*.json")))
    if len(invs) != 1:
        raise SystemExit("STOP: expected one archive inventory, found %d" % len(invs))
    with open(invs[0], "r", encoding="utf-8") as fh:
        inv = {f["path"]: f["sha256"] for f in json.load(fh)["files"]}
    run_fp, input_files = run_fingerprint(m06, EXAM_KLINES, coins)
    bad = []
    for rel, h in input_files:
        key = os.path.relpath(os.path.join(ROOT, rel), os.path.join(ROOT, "exam", "data"))
        if inv.get(key) != h:
            bad.append({"path": rel, "disk_sha256": h, "inventory_sha256": inv.get(key)})
    for c in coins:
        want = sorted(k for k in inv if k.startswith("klines_1h/%s/" % c))
        have = sorted(os.path.relpath(os.path.join(ROOT, rel), os.path.join(ROOT, "exam", "data"))
                      for rel, _ in input_files if rel.split(os.sep)[3] == c)
        if want != have:
            bad.append({"coin_line": line_of[c], "inventory_files": len(want),
                        "disk_files": len(have)})
    attempt["input_check"] = {"inventory_file": os.path.relpath(invs[0], ROOT),
                              "inventory_sha256": sha256_file(invs[0]),
                              "kline_zips_checked": len(input_files),
                              "mismatches": bad}
    if bad:
        attempt.update({"finished_at_utc": utc_now_iso(),
                        "outcome": "STOPPED: exam kline inputs do not match the inventory"})
        append_run(attempt)
        print(json.dumps(bad, indent=1))
        return 4

    # -- 3. the procedure on the exam coins -----------------------------------
    moments, notes, text = run_procedure(m06, EXAM_KLINES, coins)
    attempt["run_fingerprint"] = run_fp
    attempt["run_number"] = run_fp[:16]

    # -- 4. pool report, by line number ---------------------------------------
    per_line = {}
    for n in notes:
        ln = line_of[n["symbol"]]
        per_line[str(ln)] = {
            "lifetime_days": n.get("lifetime_days"),
            "traded_hours_in_period": n.get("traded_hours_in_period"),
            "candidate_start_hours": n.get("candidate_start_hours"),
            "n_large_target": n.get("n_large_target", 0),
            "large": n.get("n_large_selected", 0),
            "calm_eligible_hours": n.get("calm_eligible_hours"),
            "calm": n.get("n_calm_selected", 0),
            "reason_no_moments": n.get("reason_no_moments"),
            "large_shortfall_reason": n.get("large_shortfall_reason"),
            "calm_shortfall_reason": n.get("calm_shortfall_reason"),
            "first_traded_hour_utc": n.get("first_traded_hour_utc"),
            "last_traded_hour_utc": n.get("last_traded_hour_utc"),
        }
    per_line = {k: per_line[k] for k in sorted(per_line, key=int)}
    n_large = sum(1 for m in moments if m["kind"] == "large")
    n_calm = sum(1 for m in moments if m["kind"] == "calm")

    sep48 = m06.SEPARATION_LARGE_H * m06.HOUR_MS
    calm_ts = {}
    for m in moments:
        if m["kind"] == "calm":
            calm_ts.setdefault(m["symbol"], []).append(m["start_ms"])
    close_calm_pairs = 0
    for ts in calm_ts.values():
        ts.sort()
        close_calm_pairs += sum(1 for i in range(len(ts) - 1) if ts[i + 1] - ts[i] < sep48)
    hour_groups = {}
    for m in moments:
        hour_groups.setdefault(m["start_ms"], []).append((line_of[m["symbol"]], m["kind"]))
    shared = {m06.iso(t): sorted("line %d %s" % x for x in v)
              for t, v in sorted(hour_groups.items()) if len({x[0] for x in v}) > 1}
    same_coin_same_hour = sum(1 for v in hour_groups.values()
                              if len(v) > len({x[0] for x in v}))
    distinct_start_hours = {"all": len(hour_groups),
                            "large": len({m["start_ms"] for m in moments if m["kind"] == "large"}),
                            "calm": len({m["start_ms"] for m in moments if m["kind"] == "calm"})}

    pool = {
        "run_number": run_fp[:16],
        "run_fingerprint": run_fp,
        "seed": m06.SEED,
        "procedure": "scripts/06_find_moments.py find_for_symbol + load_hourly, unchanged",
        "procedure_script_sha256": attempt["procedure_script_sha256"],
        "coin_list_sha256": attempt["coin_list_sha256"],
        "kline_zips_used": len(input_files),
        "self_check_reproduces_observation_moments": True,
        "per_coin_line": per_line,
        "totals": {"coins": len(coins), "large": n_large, "calm": n_calm,
                   "moments": n_large + n_calm,
                   "coins_with_zero_moments": sorted(int(k) for k, v in per_line.items()
                                                     if v["large"] == 0)},
        "beside_tactics_6": {"cards_large_called_for": TACTICS6_CARDS_LARGE,
                             "cards_calm_called_for": TACTICS6_CARDS_CALM,
                             "pool_large": n_large, "pool_calm": n_calm,
                             "pool_large_minus_called_for": n_large - TACTICS6_CARDS_LARGE,
                             "pool_calm_minus_called_for": n_calm - TACTICS6_CARDS_CALM},
        "measured_checks": {
            "calm_pairs_inside_one_coin_closer_than_48h": close_calm_pairs,
            "start_hours_shared_by_more_than_one_coin": len(shared),
            "start_hours_with_two_or_more_moments_of_one_coin": same_coin_same_hour,
            "distinct_start_hours": distinct_start_hours,
            "shared_start_hours": shared,
        },
        "not_done_here": "No moment was chosen for a card. How the TACTICS 6 cards "
                         "are drawn from this pool is not decided by this script.",
    }
    pool_text = json.dumps(pool, indent=1, sort_keys=True) + "\n"
    life_text = json.dumps(notes, indent=1, sort_keys=True) + "\n"

    results = {}
    # check all three first so a RULES 30 stop writes nothing
    for path, t in ((MOMENTS_CSV, text), (LIFETIMES_JSON, life_text), (POOL_JSON, pool_text)):
        if os.path.exists(path):
            with open(path, "rb") as fh:
                if fh.read() != t.encode("utf-8"):
                    attempt.update({"finished_at_utc": utc_now_iso(),
                                    "outcome": "STOPPED (RULES 30): %s exists with different content"
                                               % os.path.relpath(path, ROOT)})
                    append_run(attempt)
                    print(attempt["outcome"])
                    return 5
    for path, t in ((MOMENTS_CSV, text), (LIFETIMES_JSON, life_text), (POOL_JSON, pool_text)):
        results[os.path.relpath(path, ROOT)] = {"action": write_once(path, t),
                                                "sha256": sha256_file(path)}
    attempt.update({"finished_at_utc": utc_now_iso(), "outputs": results,
                    "totals": pool["totals"], "outcome": "complete"})
    append_run(attempt)

    for k, v in per_line.items():
        print("line %-3s lifetime %-8s large %-3s calm %-3s %s" % (
            k, v["lifetime_days"], v["large"], v["calm"],
            v["reason_no_moments"] or v["calm_shortfall_reason"]
            or v["large_shortfall_reason"] or ""), flush=True)
    print(json.dumps({"run_number": run_fp[:16], "totals": pool["totals"],
                      "outputs": results}, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
