#!/usr/bin/env python3
"""
exam_26_acquisition_record.py -- one fingerprinted record of the exam-coin raw
                                 data acquisition (exam_24 + exam_25).

What it does : reads the files exam_24_acquire_archive.py and
               exam_25_acquire_external.py wrote under exam/acquisition/ and
               exam/data/external/, and writes one JSON record holding:
                 - per archive kind: files and bytes verified on disk
                 - per exam coin (by line number in exam/draw/exam-coins.txt):
                   archive files kept, archive files absent from the archive,
                   bookDepth days listed (not downloaded), external results
                 - every fetch failure, by path, with its exact error
                 - what is left for after moment selection
                 - SHA-256 of every acquisition file and script
               Nothing is fetched. Nothing is interpreted.
Input        : exam/draw/exam-coins.txt, exam/acquisition/*, exam/data/external/*.json
Output       : exam/acquisition/acquisition-record-<id>.json, where <id> is the
               first 16 hex of the SHA-256 of the record's own inputs (RULES 29).
               Written once; if it exists with different content the script
               stops (RULES 30).
Rules        : RULES 2, 19, 20, 21, 22, 29, 30
No randomness. No constants that change a number.
"""

import glob
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lab_archive import sha256_file  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COIN_LIST = os.path.join(ROOT, "exam", "draw", "exam-coins.txt")
ACQ = os.path.join(ROOT, "exam", "acquisition")
EXT = os.path.join(ROOT, "exam", "data", "external")

# What this acquisition did not fetch because it needs the moments first.
# Text only; it names no coin.
DEFERRED = [
    {"item": "order book depth (bookDepth, daily archive files)",
     "why": "TACTICS 3: 'order book depth (only the moment days are downloaded; "
            "the files are large)'. Moment days do not exist yet. Folders were "
            "listed and per-day sizes recorded in the archive plan file, so the "
            "later download can be measured before it starts (RULES 28)."},
    {"item": "choice of which prediction-market histories belong on a card",
     "why": "08 keeps only markets overlapping a card span; card spans need "
            "moments. Histories were fetched for every matched market "
            "overlapping the whole data span, a superset; the card-span filter "
            "is applied later. Nothing further needs fetching for it."},
]


def jl(path):
    out = []
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                out.append(json.loads(line))
    return out


def main() -> int:
    with open(COIN_LIST, "r", encoding="utf-8") as fh:
        coins = [ln.strip() for ln in fh if ln.strip()]
    line_of = {c: i + 1 for i, c in enumerate(coins)}

    plans = sorted(glob.glob(os.path.join(ACQ, "archive-plan-*.json")))
    invs = sorted(glob.glob(os.path.join(ACQ, "archive-inventory-*.json")))
    if len(plans) != 1 or len(invs) != 1:
        raise SystemExit("STOP: expected exactly one archive plan and one inventory, "
                         "found %d and %d" % (len(plans), len(invs)))
    plan = json.load(open(plans[0], encoding="utf-8"))
    inv = json.load(open(invs[0], encoding="utf-8"))
    arch_rows = jl(os.path.join(ACQ, "archive-manifest.jsonl"))
    ext_rows = jl(os.path.join(ACQ, "external-manifest.jsonl"))
    runs = jl(os.path.join(ACQ, "runs.jsonl"))

    inputs = [COIN_LIST, plans[0], invs[0],
              os.path.join(ACQ, "archive-manifest.jsonl"),
              os.path.join(ACQ, "external-manifest.jsonl"),
              os.path.join(ACQ, "runs.jsonl")] + \
        [os.path.join(EXT, n) for n in ("us-calendar.json", "coin-names.json",
                                        "wikipedia.json", "prediction-market.json",
                                        "announcements-probe.json")] + \
        sorted(glob.glob(os.path.join(ROOT, "scripts", "exam_2[456]_*.py"))) + \
        [os.path.join(ROOT, "scripts", "lab_archive.py"),
         os.path.join(ROOT, "scripts", "08_external_sources.py")]
    fps = {os.path.relpath(p, ROOT): sha256_file(p) for p in inputs}
    rid = hashlib.sha256(json.dumps(fps, sort_keys=True).encode()).hexdigest()

    # ---- archive -----------------------------------------------------------
    by_kind = {}
    per_line = {i + 1: {"archive_files_kept": {}, "archive_files_absent": {},
                        "bookdepth_listing": None} for i in range(len(coins))}
    for f in inv["files"]:
        kind, sym = f["path"].split("/")[:2]
        e = by_kind.setdefault(kind, {"files": 0, "bytes": 0})
        e["files"] += 1
        e["bytes"] += f["bytes"]
        if sym in line_of:
            d = per_line[line_of[sym]]["archive_files_kept"]
            d[kind] = d.get(kind, 0) + 1
    for m in plan["not_in_archive"]:
        d = per_line[line_of[m["symbol"]]]["archive_files_absent"]
        cut = {"klines_1h": 4, "fundingRate": 13, "metrics": 9}[m["kind"]]
        d.setdefault(m["kind"], []).append(m["file"][len(m["symbol"]) + cut:-4])
    for sym, rec in plan["bookdepth_listing_only"].items():
        per_line[line_of[sym]]["bookdepth_listing"] = rec
    arch_fail = [r for r in arch_rows if not r.get("checksum_verified")]

    # ---- external ----------------------------------------------------------
    names = json.load(open(os.path.join(EXT, "coin-names.json"), encoding="utf-8"))
    wiki = json.load(open(os.path.join(EXT, "wikipedia.json"), encoding="utf-8"))
    poly = json.load(open(os.path.join(EXT, "prediction-market.json"), encoding="utf-8"))
    cal = json.load(open(os.path.join(EXT, "us-calendar.json"), encoding="utf-8"))
    ann = json.load(open(os.path.join(EXT, "announcements-probe.json"), encoding="utf-8"))
    for sym, ln in line_of.items():
        w, p = wiki[sym], poly[sym]
        per_line[ln]["external"] = {
            "coin_name_found": names[sym]["name"] is not None,
            "coin_name_error": names[sym]["error"],
            "wikipedia_article_accepted": w["article"] is not None,
            "wikipedia_daily_points": len(w["daily"]),
            "wikipedia_error": w["error"],
            "polymarket_markets_seen": p["markets_seen"],
            "polymarket_markets_matched": len(p["markets_matched"]),
            "polymarket_matched_overlapping_data_span":
                sum(1 for r in p["markets_matched"] if r.get("overlaps_data_span")),
            "polymarket_histories_fetched": len(p["series"]),
            "polymarket_errors": p["errors"],
        }
    # a failure line stays in the manifest even after a later retry succeeded;
    # the latest row per path decides whether it is still failed
    latest = {}
    for r in ext_rows:
        latest[r["path"]] = r
    ext_fail_now = [{"path": r["path"], "source_url": r["source_url"],
                     "error": r["error"], "at": r["downloaded_at_utc"]}
                    for r in latest.values() if r.get("sha256") is None]
    ext_ok = [r for r in latest.values() if r.get("sha256")]

    record = {
        "record_id": rid,
        "inputs_sha256": fps,
        "coin_count": len(coins),
        "archive": {"by_kind_verified_on_disk": by_kind,
                    "total_files": len(inv["files"]), "total_bytes": inv["total_bytes"],
                    "manifest_rows": len(arch_rows),
                    "rows_not_verified": [{"path": r["path"], "error": r["error"]}
                                          for r in arch_fail],
                    "listing_errors": plan["listing_errors"],
                    "files_absent_from_archive_total": len(plan["not_in_archive"]),
                    "months": plan["months"], "metrics_days": plan["metrics_days"],
                    "reference_symbols_klines_1h": plan["reference_symbols"]},
        "external": {"files_kept": len(ext_ok),
                     "bytes_kept": sum(r["bytes"] for r in ext_ok if r.get("bytes")),
                     "paths_still_failed": ext_fail_now,
                     "us_calendar_releases_parsed": cal["count"],
                     "us_calendar_sources_parsed": sorted(set(r["source"] for r in cal["releases"])),
                     "us_calendar_errors": cal["errors"],
                     "announcement_probes": ann["probes"]},
        "per_coin_line": per_line,
        "deferred_until_moments": DEFERRED,
        "attempts": [{k: r.get(k) for k in ("run_id", "script", "mode", "started_at_utc",
                                             "finished_at_utc", "outcome")} for r in runs],
    }
    out = os.path.join(ACQ, "acquisition-record-%s.json" % rid[:16])
    blob = (json.dumps(record, indent=1, sort_keys=True) + "\n").encode("utf-8")
    if os.path.exists(out):
        if open(out, "rb").read() != blob:
            raise SystemExit("STOP (RULES 30): %s exists with different content" % out)
    else:
        with open(out + ".tmp", "wb") as fh:
            fh.write(blob)
        os.replace(out + ".tmp", out)
    print(os.path.relpath(out, ROOT), hashlib.sha256(blob).hexdigest())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
