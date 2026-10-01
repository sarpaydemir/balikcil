#!/usr/bin/env python3
"""
exam_24_acquire_archive.py -- raw Binance archive data for the exam coins, the
                              part that does not depend on which moments are
                              chosen (Mode B, step 1 only).

What it does
------------
Reads the exam coin list at run time from exam/draw/exam-coins.txt (no coin
name is written in this file) and, for those coins, lists the public Binance
archive and downloads:

  * klines 1h      monthly  data/futures/um/monthly/klines/<SYM>/1h/
                   every month in MONTHS, for the exam coins and for the two
                   reference symbols TACTICS 3 names ("bitcoin and ethereum,
                   over the same hours"). Moment finding (TACTICS 2) and the
                   price / volume / trade count / taker columns (TACTICS 3)
                   come from these.
  * fundingRate    monthly  data/futures/um/monthly/fundingRate/<SYM>/
                   every month in MONTHS, exam coins only (TACTICS 3: funding
                   rate, payment interval and its changes).
  * metrics        daily    data/futures/um/daily/metrics/<SYM>/
                   every day from the first day of MONTHS[0] to the last day of
                   MONTHS[-1], exam coins only (TACTICS 3: open interest,
                   long/short ratios). The whole span is taken so that no
                   moment choice is needed to decide which days to fetch.

It does NOT download order book depth (bookDepth): TACTICS 3 says only the
moment days are downloaded, and moments do not exist yet. It only LISTS each
exam coin's bookDepth folder and records which days exist and their byte
sizes, so the later run can measure its download before starting.

Before downloading anything it measures the exact byte size of every file it
is about to fetch (from the archive's own listing) and the free disk space,
and stops if the space is not there (RULES 28).

Every zip is verified against the archive's own .CHECKSUM companion and gets a
SHA-256 (RULES 2). A file that fails to download or verify is recorded by name
with the exact error (RULES 20, 21); a file that fails verification is kept as
<name>.FAILED, never under its real name.

Input   : exam/draw/exam-coins.txt
          the public archive (addresses documented in lab_archive.py)
Output  : exam/data/klines_1h/<SYM>/<SYM>-1h-<YYYY>-<MM>.zip
          exam/data/fundingRate/<SYM>/<SYM>-fundingRate-<YYYY>-<MM>.zip
          exam/data/metrics/<SYM>/<SYM>-metrics-<YYYY>-<MM>-<DD>.zip
          exam/acquisition/archive-manifest.jsonl   append-only, one line per
                    file: source URL, checksum URL, download time, SHA-256,
                    archive SHA-256, verified flag, bytes, error
          exam/acquisition/archive-plan-<run_id>.json   listing result, exact
                    sizes, disk check, files not in the archive, bookDepth
                    availability (written once per run id; RULES 30)
          exam/acquisition/archive-inventory-<run_id>.json  every kept file
                    with its SHA-256; written only when nothing failed
          exam/acquisition/runs.jsonl   one line per attempt (append-only)
Rules   : RULES 2, 19, 20, 21, 23, 26, 27, 28, 29, 30

Run number (RULES 29): run_id = SHA-256 of (this script's bytes + the exam
coin list's bytes). The same script on the same coin list has the same number.
If a plan or inventory file already exists under this number with different
content, the script stops instead of overwriting (RULES 30).

Usage   : exam_24_acquire_archive.py --plan-only   list + size + disk check
          exam_24_acquire_archive.py               the above, then download
Re-runnable: yes. A file already present and verified is not fetched again.
No randomness in this script.
"""

import argparse
import calendar
import hashlib
import json
import os
import shutil
import sys
import threading
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lab_archive import (  # noqa: E402
    FetchError, Manifest, http_get, list_prefix, object_url, sha256_bytes,
    sha256_file, utc_now_iso,
)

# ---------------------------------------------------------------- constants --
# Months, inclusive. Period 2025-09 .. 2026-08 is TACTICS 0. 2025-08 is the
# lookback month the card's "before" section needs (TACTICS 3: 24 h before the
# start plus a 7-day summary); the same list is used by 05 and 07.
MONTHS = ["2025-08",
          "2025-09", "2025-10", "2025-11", "2025-12",
          "2026-01", "2026-02", "2026-03", "2026-04",
          "2026-05", "2026-06", "2026-07", "2026-08"]

# TACTICS 3: "bitcoin and ethereum, over the same hours". Same list as 05/09.
REFERENCE_SYMBOLS = ["BTCUSDT", "ETHUSDT"]

KLINES_1H_PREFIX = "data/futures/um/monthly/klines/%s/1h/"
FUNDING_PREFIX = "data/futures/um/monthly/fundingRate/%s/"
METRICS_PREFIX = "data/futures/um/daily/metrics/%s/"
BOOKDEPTH_PREFIX = "data/futures/um/daily/bookDepth/%s/"

# Disk guard (RULES 28). Sizes come from the archive's own listing (measured);
# the factor and floor are safety headroom only, the same values 05 uses.
DISK_HEADROOM_FACTOR = 5.0
DISK_MIN_FREE_BYTES = 200 * 1024 * 1024

# Speed only; affects no number this script produces.
DOWNLOAD_WORKERS = 8
PROGRESS_EVERY = 250

SCRIPT_PATH = os.path.abspath(__file__)
ROOT = os.path.dirname(os.path.dirname(SCRIPT_PATH))
COIN_LIST = os.path.join(ROOT, "exam", "draw", "exam-coins.txt")
DATA_DIR = os.path.join(ROOT, "exam", "data")
ACQ_DIR = os.path.join(ROOT, "exam", "acquisition")
MANIFEST_PATH = os.path.join(ACQ_DIR, "archive-manifest.jsonl")
RUNS_PATH = os.path.join(ACQ_DIR, "runs.jsonl")


# ------------------------------------------------------------------ helpers --
def read_coins() -> list:
    with open(COIN_LIST, "r", encoding="utf-8") as fh:
        return [ln.strip() for ln in fh if ln.strip()]


def run_id() -> str:
    h = hashlib.sha256()
    with open(SCRIPT_PATH, "rb") as fh:
        h.update(fh.read())
    h.update(b"\n--coin-list--\n")
    with open(COIN_LIST, "rb") as fh:
        h.update(fh.read())
    return h.hexdigest()


def all_days() -> list:
    out = []
    for ym in MONTHS:
        y, m = int(ym[:4]), int(ym[5:])
        for d in range(1, calendar.monthrange(y, m)[1] + 1):
            out.append("%04d-%02d-%02d" % (y, m, d))
    return out


def listing(prefix: str) -> dict:
    """{filename: (key, size)} of the .zip objects in one archive folder."""
    res = list_prefix(prefix)
    out = {}
    for f in res["files"]:
        name = f["key"].rsplit("/", 1)[-1]
        if name.endswith(".zip"):
            out[name] = (f["key"], f["size"])
    return out


def write_once(path: str, obj) -> None:
    """Write JSON; if the file exists with different content, stop (RULES 30)."""
    blob = (json.dumps(obj, indent=1, sort_keys=True) + "\n").encode("utf-8")
    if os.path.exists(path):
        with open(path, "rb") as fh:
            old = fh.read()
        if old == blob:
            return
        raise SystemExit("STOP (RULES 30): %s exists with different content "
                         "(sha256 %s vs new %s); refusing to overwrite"
                         % (path, sha256_bytes(old), sha256_bytes(blob)))
    with open(path + ".tmp", "wb") as fh:
        fh.write(blob)
    os.replace(path + ".tmp", path)


def append_run(row: dict) -> None:
    with open(RUNS_PATH, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, sort_keys=True) + "\n")
        fh.flush()
        os.fsync(fh.fileno())


# --------------------------------------------------------------------- plan --
def build_plan(coins: list) -> dict:
    """List every folder; return wanted files, files not in the archive, and
    listing errors. Nothing is downloaded here."""
    days = all_days()
    wanted, not_in_archive, listing_errors, bookdepth = [], [], [], {}

    def plan_folder(kind, sym, prefix, names):
        try:
            have = listing(prefix)
        except FetchError as exc:
            listing_errors.append({"kind": kind, "symbol": sym, "prefix": prefix,
                                   "error": str(exc)})
            return None
        for n in names:
            if n in have:
                key, size = have[n]
                wanted.append({"kind": kind, "symbol": sym, "key": key,
                               "bytes": size, "rel": "%s/%s/%s" % (kind, sym, n)})
            else:
                # the folder itself listed without error; this name is not in it
                not_in_archive.append({"kind": kind, "symbol": sym, "file": n,
                                       "prefix": prefix})
        return have

    for sym in coins + [s for s in REFERENCE_SYMBOLS if s not in coins]:
        is_exam = sym in coins
        have = plan_folder("klines_1h", sym, KLINES_1H_PREFIX % sym,
                           ["%s-1h-%s.zip" % (sym, m) for m in MONTHS])
        if have is not None:
            # months after MONTHS[-1] are left out: the archive keeps adding
            # them, and the plan file must not change with the calendar
            months_all = sorted(m for m in (n[len(sym) + 4:-4] for n in have)
                                if m <= MONTHS[-1])
            bookdepth.setdefault("_klines_1h_months_in_archive", {})[sym] = months_all
        if not is_exam:
            print("listed %-3s reference" % (REFERENCE_SYMBOLS.index(sym) + 1), flush=True)
            continue
        plan_folder("fundingRate", sym, FUNDING_PREFIX % sym,
                    ["%s-fundingRate-%s.zip" % (sym, m) for m in MONTHS])
        plan_folder("metrics", sym, METRICS_PREFIX % sym,
                    ["%s-metrics-%s.zip" % (sym, d) for d in days])
        # bookDepth: list only (TACTICS 3: moment days only, moments do not exist)
        try:
            bd = listing(BOOKDEPTH_PREFIX % sym)
            in_span = {n: s for n, (_k, s) in bd.items()
                       if n[len(sym) + 11:-4] in set(days)}
            bookdepth[sym] = {"prefix": BOOKDEPTH_PREFIX % sym,
                              "listed_at_utc": utc_now_iso(),
                              "days_in_span_present": len(in_span),
                              "days_in_span_total": len(days),
                              "bytes_in_span": sum(in_span.values()),
                              "first_day_in_span": min((n[len(sym) + 11:-4] for n in in_span), default=None),
                              "last_day_in_span": max((n[len(sym) + 11:-4] for n in in_span), default=None),
                              "error": None}
        except FetchError as exc:
            bookdepth[sym] = {"prefix": BOOKDEPTH_PREFIX % sym,
                              "listed_at_utc": utc_now_iso(), "error": str(exc)}
            listing_errors.append({"kind": "bookDepth(listing only)", "symbol": sym,
                                   "prefix": BOOKDEPTH_PREFIX % sym, "error": str(exc)})
        print("listed %-3s exam coin line %d" % ("", coins.index(sym) + 1), flush=True)

    wanted.sort(key=lambda w: w["rel"])
    not_in_archive.sort(key=lambda w: (w["kind"], w["symbol"], w["file"]))
    return {"wanted": wanted, "not_in_archive": not_in_archive,
            "listing_errors": listing_errors, "bookdepth_listing": bookdepth}


# ----------------------------------------------------------------- download --
def fetch_one(item: dict, manifest: Manifest, lock: threading.Lock) -> dict:
    dest = os.path.join(DATA_DIR, item["rel"])
    with lock:
        if manifest.has_verified(item["rel"]) and os.path.exists(dest):
            return {"status": "skipped", "rel": item["rel"]}
    zip_url = object_url(item["key"])
    sum_url = zip_url + ".CHECKSUM"
    row = {"path": item["rel"], "kind": item["kind"], "symbol": item["symbol"],
           "source_url": zip_url, "checksum_url": sum_url,
           "listed_bytes": item["bytes"], "bytes": None,
           "downloaded_at_utc": None, "sha256": None, "expected_sha256": None,
           "checksum_verified": False, "error": None}
    try:
        blob = http_get(zip_url)
    except FetchError as exc:
        row["downloaded_at_utc"] = utc_now_iso()
        row["error"] = "zip fetch failed: %s" % exc
        with lock:
            manifest.add(row)
        return {"status": "failed", "rel": item["rel"], "error": row["error"]}
    row["downloaded_at_utc"] = utc_now_iso()
    row["sha256"] = sha256_bytes(blob)
    row["bytes"] = len(blob)
    try:
        row["expected_sha256"] = http_get(sum_url).decode("utf-8", "replace").split()[0].lower()
    except FetchError as exc:
        row["error"] = "checksum fetch failed: %s" % exc
    except IndexError:
        row["error"] = "checksum file was empty"
    if row["expected_sha256"]:
        row["checksum_verified"] = row["sha256"] == row["expected_sha256"]
        if not row["checksum_verified"]:
            row["error"] = "CHECKSUM MISMATCH: computed %s, archive says %s" % (
                row["sha256"], row["expected_sha256"])
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    out = dest if row["checksum_verified"] else dest + ".FAILED"
    with open(out + ".part", "wb") as fh:
        fh.write(blob)
    os.replace(out + ".part", out)
    with lock:
        manifest.add(row)
    if row["checksum_verified"]:
        return {"status": "ok", "rel": item["rel"]}
    return {"status": "failed", "rel": item["rel"], "error": row["error"]}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan-only", action="store_true")
    args = ap.parse_args()

    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(ACQ_DIR, exist_ok=True)
    coins = read_coins()
    rid = run_id()
    started = utc_now_iso()
    print("run_id %s  started %s  coins %d" % (rid, started, len(coins)), flush=True)

    plan = build_plan(coins)
    wanted = plan["wanted"]
    total = sum(w["bytes"] for w in wanted)
    by_kind = {}
    for w in wanted:
        e = by_kind.setdefault(w["kind"], {"files": 0, "bytes": 0})
        e["files"] += 1
        e["bytes"] += w["bytes"]

    usage = shutil.disk_usage(DATA_DIR)
    required = max(int(total * DISK_HEADROOM_FACTOR), DISK_MIN_FREE_BYTES)
    disk = {"checked_at_utc": utc_now_iso(), "path": "exam/data",
            "free_bytes": usage.free, "total_bytes": usage.total,
            "measured_download_bytes": total,
            "size_note": "not an estimate: byte sizes come from the archive's own listing",
            "required_free_bytes_with_headroom": required,
            "headroom_factor": DISK_HEADROOM_FACTOR, "fits": usage.free >= required}

    # The plan file holds only what the listing returned (no clock, no disk
    # figure), so the same archive state gives the same file (RULES 29/30).
    plan_doc = {"run_id": rid, "months": MONTHS,
                "metrics_days": [all_days()[0], all_days()[-1]],
                "coin_list_sha256": sha256_file(COIN_LIST),
                "reference_symbols": REFERENCE_SYMBOLS,
                "files_to_fetch": len(wanted), "bytes_to_fetch": total,
                "by_kind": by_kind, "wanted": wanted,
                "not_in_archive": plan["not_in_archive"],
                "listing_errors": plan["listing_errors"],
                "bookdepth_listing_only": {k: v for k, v in plan["bookdepth_listing"].items()
                                           if not k.startswith("_")},
                "klines_1h_months_in_archive": plan["bookdepth_listing"].get(
                    "_klines_1h_months_in_archive", {})}
    for sym, rec in plan_doc["bookdepth_listing_only"].items():
        rec.pop("listed_at_utc", None)
    plan_path = os.path.join(ACQ_DIR, "archive-plan-%s.json" % rid[:16])
    write_once(plan_path, plan_doc)

    print(json.dumps({"by_kind": by_kind, "disk": disk,
                      "not_in_archive": len(plan["not_in_archive"]),
                      "listing_errors": len(plan["listing_errors"])}, indent=1), flush=True)

    attempt = {"run_id": rid, "script": "scripts/exam_24_acquire_archive.py",
               "script_sha256": sha256_file(SCRIPT_PATH),
               "coin_list_sha256": sha256_file(COIN_LIST),
               "started_at_utc": started, "mode": "plan-only" if args.plan_only else "download",
               "disk_check": disk, "plan_file": os.path.relpath(plan_path, ROOT),
               "plan_sha256": sha256_file(plan_path)}

    if plan["listing_errors"]:
        attempt.update({"finished_at_utc": utc_now_iso(), "outcome":
                        "STOPPED: %d folder listings failed; see plan file" % len(plan["listing_errors"])})
        append_run(attempt)
        print("STOP: listing errors (RULES 20/21); nothing downloaded")
        return 3
    if not disk["fits"]:
        attempt.update({"finished_at_utc": utc_now_iso(),
                        "outcome": "STOPPED (RULES 28): free %d < required %d" % (usage.free, required)})
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
        res = fetch_one(item, manifest, lock)
        with lock:
            counts[res["status"]] += 1
            if res["status"] == "failed":
                failures.append({"path": res["rel"], "error": res["error"]})
            done[0] += 1
            if done[0] % PROGRESS_EVERY == 0:
                print("  %d/%d  %s  %s" % (done[0], len(wanted), counts, utc_now_iso()), flush=True)

    with ThreadPoolExecutor(max_workers=DOWNLOAD_WORKERS) as pool:
        list(pool.map(job, wanted))

    # -- post-check: every wanted file on disk re-hashed against the manifest --
    manifest = Manifest(MANIFEST_PATH)
    rehash_bad = []
    inventory = []
    for w in wanted:
        row = manifest.get(w["rel"])
        dest = os.path.join(DATA_DIR, w["rel"])
        if not row or not row.get("checksum_verified") or not os.path.exists(dest):
            continue
        actual = sha256_file(dest)
        if actual != row["sha256"]:
            rehash_bad.append({"path": w["rel"], "manifest": row["sha256"], "disk": actual})
            continue
        inventory.append({"path": w["rel"], "sha256": actual,
                          "bytes": os.path.getsize(dest), "source_url": row["source_url"],
                          "archive_checksum_sha256": row["expected_sha256"]})
    still_missing = sorted(set(w["rel"] for w in wanted) - set(i["path"] for i in inventory))

    outcome = "complete" if not still_missing and not rehash_bad else "INCOMPLETE"
    attempt.update({"finished_at_utc": utc_now_iso(), "counts_this_attempt": counts,
                    "failures_this_attempt": failures, "rehash_mismatch": rehash_bad,
                    "files_wanted": len(wanted), "files_verified_on_disk": len(inventory),
                    "files_not_verified": still_missing, "outcome": outcome})
    if outcome == "complete":
        inv_path = os.path.join(ACQ_DIR, "archive-inventory-%s.json" % rid[:16])
        write_once(inv_path, {"run_id": rid, "files": inventory,
                              "total_bytes": sum(i["bytes"] for i in inventory)})
        attempt["inventory_file"] = os.path.relpath(inv_path, ROOT)
        attempt["inventory_sha256"] = sha256_file(inv_path)
    append_run(attempt)
    print(json.dumps({k: attempt[k] for k in ("finished_at_utc", "counts_this_attempt",
                                              "files_wanted", "files_verified_on_disk",
                                              "outcome")}, indent=1))
    if failures:
        print("FAILED FILES (RULES 20/21):")
        for f in failures:
            print("  %s  %s" % (f["path"], f["error"]))
    return 0 if outcome == "complete" else 4


if __name__ == "__main__":
    raise SystemExit(main())
