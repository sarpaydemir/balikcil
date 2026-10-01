#!/usr/bin/env python3
"""
exam_28_acquire_bookdepth.py -- order book depth (bookDepth) for the moment
                                days of the exam coins: the archive item that
                                could only be fetched once moments existed.

What it does
------------
TACTICS 3: "order book depth (only the moment days are downloaded; the files
are large)". The rest of the exam coins' archive data was taken by exam_24
over the whole span; bookDepth was left until the moments existed.

* Moment days are computed by scripts/07_download_moment_data.py's own
  moment_days() (imported, unchanged), pointed at exam/moments/moments.csv
  (from exam_27): every UTC calendar day touched by the window
  [t0 - 24h, t0 + 23h] of any moment of that coin. All moments in the pool are
  covered; no moment is chosen here.
* Each exam coin's bookDepth folder is listed fresh from the archive; the exact
  byte size of every file to fetch comes from that listing. Free disk space is
  measured and the run stops before downloading if it does not fit (RULES 28).
  The headroom factor and floor are 07's own constants, read from 07.
* Every zip is fetched by exam_24's fetch_one() (imported, unchanged): verified
  against the archive's .CHECKSUM companion, SHA-256 recorded, a file failing
  verification kept as <name>.FAILED, never under its real name (RULES 2, 20, 21).
* After downloading, every kept file is re-hashed against the manifest and an
  inventory is written only if nothing is missing.

Coin names are read at run time from exam/draw/exam-coins.txt (via the moments
file). No coin name is written in this file; console lines use line numbers.

Input   : exam/moments/moments.csv, exam/draw/exam-coins.txt
          scripts/07_download_moment_data.py, scripts/exam_24_acquire_archive.py
          the public archive (addresses documented in lab_archive.py)
Output  : exam/data/bookDepth/<SYM>/<SYM>-bookDepth-<YYYY-MM-DD>.zip
          exam/acquisition/bookdepth-manifest.jsonl  append-only, one line per
                    file fetched (RULES 2, 30)
          exam/acquisition/bookdepth-plan-<run>.json  moment days, listing,
                    exact sizes, days absent from the archive (write-once)
          exam/acquisition/bookdepth-inventory-<run>.json  every kept file and
                    its SHA-256; written only when nothing failed (write-once)
          exam/acquisition/bookdepth-runs.jsonl  one line per attempt, with the
                    disk check and the system-clock times (append-only)
Rules   : TACTICS 3; RULES 2, 19, 20, 21, 23, 26, 27, 28, 29, 30

Run number (RULES 29): SHA-256 of (this script's bytes + exam/moments/moments.csv
bytes + exam/draw/exam-coins.txt bytes). Plan and inventory files are written
once per run number; different content under the same number stops the script.

Usage   : exam_28_acquire_bookdepth.py --plan-only   list + size + disk check
          exam_28_acquire_bookdepth.py               the above, then download
Re-runnable: yes. A file already in the manifest as verified and present on
disk is not fetched again. No randomness.
"""

import argparse
import hashlib
import importlib.util
import json
import os
import shutil
import sys
import threading
from concurrent.futures import ThreadPoolExecutor

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lab_archive import FetchError, Manifest, sha256_file, utc_now_iso  # noqa: E402

# ---------------------------------------------------------------- constants --
# Speed only; affects no number this script produces (same as exam_24).
DOWNLOAD_WORKERS = 8
PROGRESS_EVERY = 100
# Disk headroom: taken from 07 at run time (07 fetched bookDepth for the
# observation moments); not set here.

SCRIPT_PATH = os.path.abspath(__file__)
ROOT = os.path.dirname(HERE)
SCRIPT_07 = os.path.join(HERE, "07_download_moment_data.py")
SCRIPT_24 = os.path.join(HERE, "exam_24_acquire_archive.py")
COIN_LIST = os.path.join(ROOT, "exam", "draw", "exam-coins.txt")
MOMENTS_CSV = os.path.join(ROOT, "exam", "moments", "moments.csv")
DATA_DIR = os.path.join(ROOT, "exam", "data")
ACQ_DIR = os.path.join(ROOT, "exam", "acquisition")
MANIFEST_PATH = os.path.join(ACQ_DIR, "bookdepth-manifest.jsonl")
RUNS_PATH = os.path.join(ACQ_DIR, "bookdepth-runs.jsonl")


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run_id():
    h = hashlib.sha256()
    for p, tag in ((SCRIPT_PATH, b""), (MOMENTS_CSV, b"\n--moments--\n"),
                   (COIN_LIST, b"\n--coin-list--\n")):
        h.update(tag)
        with open(p, "rb") as fh:
            h.update(fh.read())
    return h.hexdigest()


def append_run(row):
    with open(RUNS_PATH, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, sort_keys=True) + "\n")
        fh.flush()
        os.fsync(fh.fileno())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan-only", action="store_true")
    args = ap.parse_args()

    os.makedirs(ACQ_DIR, exist_ok=True)
    m07 = load(SCRIPT_07, "moment_data_07")
    m24 = load(SCRIPT_24, "exam_acquire_24")
    if os.path.abspath(m24.DATA_DIR) != os.path.abspath(DATA_DIR):
        raise SystemExit("STOP: exam_24 DATA_DIR is not exam/data")
    m07.MOMENTS_CSV = MOMENTS_CSV

    with open(COIN_LIST, "r", encoding="utf-8") as fh:
        coins = [ln.strip() for ln in fh if ln.strip()]
    line_of = {c: i + 1 for i, c in enumerate(coins)}
    rid = run_id()
    started = utc_now_iso()
    print("run %s  started %s" % (rid[:16], started), flush=True)

    days = m07.moment_days()                      # 07's definition, unchanged
    unknown = sorted(set(days) - set(coins))
    if unknown:
        raise SystemExit("STOP: moments file holds %d symbols not on the exam list"
                         % len(unknown))

    wanted, absent, listing_errors = [], [], []
    for sym in sorted(days, key=lambda s: line_of[s]):
        prefix = m07.BOOKDEPTH_PREFIX % sym
        names = ["%s-bookDepth-%s.zip" % (sym, d) for d in days[sym]]
        try:
            have = m24.listing(prefix)
        except FetchError as exc:
            listing_errors.append({"coin_line": line_of[sym], "prefix": prefix,
                                   "error": str(exc)})
            print("line %-3s LISTING FAILED: %s" % (line_of[sym], exc), flush=True)
            continue
        for n in names:
            if n in have:
                key, size = have[n]
                wanted.append({"kind": "bookDepth", "symbol": sym, "key": key,
                               "bytes": size, "rel": "bookDepth/%s/%s" % (sym, n)})
            else:
                absent.append({"coin_line": line_of[sym], "symbol": sym, "file": n,
                               "prefix": prefix,
                               "reason": "not present in the archive folder "
                                         "(listing returned %d zips)" % len(have)})
        print("line %-3s moment days %-4d listed %d zips" % (line_of[sym], len(names), len(have)),
              flush=True)
    wanted.sort(key=lambda w: w["rel"])
    total = sum(w["bytes"] for w in wanted)

    per_line = {}
    for sym in days:
        ln = str(line_of[sym])
        per_line[ln] = {"moment_days": len(days[sym]),
                        "files_to_fetch": sum(1 for w in wanted if w["symbol"] == sym),
                        "bytes_to_fetch": sum(w["bytes"] for w in wanted if w["symbol"] == sym),
                        "days_absent_from_archive": [a["file"][len(sym) + 11:-4]
                                                     for a in absent if a["symbol"] == sym]}
    per_line = {k: per_line[k] for k in sorted(per_line, key=int)}

    usage = shutil.disk_usage(DATA_DIR)
    required = max(int(total * m07.DISK_HEADROOM_FACTOR), m07.DISK_MIN_FREE_BYTES)
    disk = {"checked_at_utc": utc_now_iso(), "path": "exam/data",
            "free_bytes": usage.free, "total_bytes": usage.total,
            "measured_download_bytes": total,
            "size_note": "not an estimate: byte sizes come from the archive's own listing",
            "required_free_bytes_with_headroom": required,
            "headroom_factor": m07.DISK_HEADROOM_FACTOR,
            "min_free_bytes": m07.DISK_MIN_FREE_BYTES,
            "headroom_source": "scripts/07_download_moment_data.py constants",
            "fits": usage.free >= required}

    plan_doc = {"run_id": rid, "moments_csv_sha256": sha256_file(MOMENTS_CSV),
                "coin_list_sha256": sha256_file(COIN_LIST),
                "moment_day_definition": "scripts/07_download_moment_data.py moment_days(): "
                                         "every UTC day touched by [t0-%dh, t0+%dh]"
                                         % (m07.CARD_BEFORE_H, m07.CARD_AFTER_H - 1),
                "files_to_fetch": len(wanted), "bytes_to_fetch": total,
                "per_coin_line": per_line, "wanted": wanted,
                "absent_from_archive": absent, "listing_errors": listing_errors}
    plan_path = os.path.join(ACQ_DIR, "bookdepth-plan-%s.json" % rid[:16])
    m24.write_once(plan_path, plan_doc)

    print(json.dumps({"files_to_fetch": len(wanted), "bytes_to_fetch": total,
                      "absent_from_archive": len(absent),
                      "listing_errors": len(listing_errors), "disk": disk}, indent=1), flush=True)

    attempt = {"run_id": rid, "script": "scripts/exam_28_acquire_bookdepth.py",
               "script_sha256": sha256_file(SCRIPT_PATH),
               "reused_sha256": {"scripts/07_download_moment_data.py": sha256_file(SCRIPT_07),
                                 "scripts/exam_24_acquire_archive.py": sha256_file(SCRIPT_24),
                                 "scripts/lab_archive.py": sha256_file(os.path.join(HERE, "lab_archive.py"))},
               "moments_csv_sha256": plan_doc["moments_csv_sha256"],
               "coin_list_sha256": plan_doc["coin_list_sha256"],
               "started_at_utc": started,
               "mode": "plan-only" if args.plan_only else "download",
               "disk_check": disk, "plan_file": os.path.relpath(plan_path, ROOT),
               "plan_sha256": sha256_file(plan_path)}

    if listing_errors:
        attempt.update({"finished_at_utc": utc_now_iso(),
                        "outcome": "STOPPED: %d folder listings failed" % len(listing_errors)})
        append_run(attempt)
        print(attempt["outcome"])
        return 3
    if not disk["fits"]:
        attempt.update({"finished_at_utc": utc_now_iso(),
                        "outcome": "STOPPED (RULES 28): free %d < required %d"
                                   % (usage.free, required)})
        append_run(attempt)
        print(attempt["outcome"])
        return 2
    if args.plan_only:
        attempt.update({"finished_at_utc": utc_now_iso(), "outcome": "plan only, nothing downloaded"})
        append_run(attempt)
        return 0

    manifest = Manifest(MANIFEST_PATH)
    lock = threading.Lock()
    counts = {"ok": 0, "skipped": 0, "failed": 0}
    failures = []
    done = [0]

    def job(item):
        res = m24.fetch_one(item, manifest, lock)
        with lock:
            counts[res["status"]] += 1
            if res["status"] == "failed":
                failures.append({"path": res["rel"], "error": res["error"]})
            done[0] += 1
            if done[0] % PROGRESS_EVERY == 0:
                print("  %d/%d  %s  %s" % (done[0], len(wanted), counts, utc_now_iso()),
                      flush=True)

    with ThreadPoolExecutor(max_workers=DOWNLOAD_WORKERS) as pool:
        list(pool.map(job, wanted))

    # -- post-check: re-hash every wanted file on disk against the manifest ---
    manifest = Manifest(MANIFEST_PATH)
    rehash_bad, inventory = [], []
    for w in wanted:
        row = manifest.get(w["rel"])
        dest = os.path.join(DATA_DIR, w["rel"])
        if not row or not row.get("checksum_verified") or not os.path.exists(dest):
            continue
        actual = sha256_file(dest)
        if actual != row["sha256"]:
            rehash_bad.append({"path": w["rel"], "manifest": row["sha256"], "disk": actual})
            continue
        inventory.append({"path": w["rel"], "sha256": actual, "bytes": os.path.getsize(dest),
                          "source_url": row["source_url"],
                          "archive_checksum_sha256": row["expected_sha256"],
                          "downloaded_at_utc": row["downloaded_at_utc"]})
    still_missing = sorted(set(w["rel"] for w in wanted) - set(i["path"] for i in inventory))
    outcome = "complete" if not still_missing and not rehash_bad else "INCOMPLETE"
    attempt.update({"finished_at_utc": utc_now_iso(), "counts_this_attempt": counts,
                    "failures_this_attempt": failures, "rehash_mismatch": rehash_bad,
                    "files_wanted": len(wanted), "files_verified_on_disk": len(inventory),
                    "files_not_verified": still_missing, "outcome": outcome})
    if outcome == "complete":
        inv_path = os.path.join(ACQ_DIR, "bookdepth-inventory-%s.json" % rid[:16])
        m24.write_once(inv_path, {"run_id": rid, "files": inventory,
                                  "total_bytes": sum(i["bytes"] for i in inventory)})
        attempt["inventory_file"] = os.path.relpath(inv_path, ROOT)
        attempt["inventory_sha256"] = sha256_file(inv_path)
    append_run(attempt)
    print(json.dumps({k: attempt[k] for k in ("finished_at_utc", "counts_this_attempt",
                                              "files_wanted", "files_verified_on_disk",
                                              "outcome")}, indent=1))
    for f in failures:
        print("FAILED (RULES 20/21): %s  %s" % (f["path"], f["error"]))
    return 0 if outcome == "complete" else 4


if __name__ == "__main__":
    raise SystemExit(main())
