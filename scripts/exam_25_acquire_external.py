#!/usr/bin/env python3
"""
exam_25_acquire_external.py -- the non-Binance sources TACTICS 3 names, for the
                               exam coins, as far as they do not depend on which
                               moments are chosen (Mode B, step 1 only).

What it does
------------
Reads the exam coin list at run time from exam/draw/exam-coins.txt (no coin
name is written in this file) and fetches, from the same documented public
addresses 08_external_sources.py uses:

  1. US release calendar: the BLS monthly release lists for CAL_MONTHS and the
     Federal Reserve FOMC calendar page. Coin- and moment-independent.
  2. Coin names: CoinGecko search on each coin's base ticker (only to find the
     Wikipedia article, exactly as 08 does).
  3. Wikipedia daily page views over the fixed span WIKI_START..WIKI_END, with
     08's acceptance rule unchanged: CoinGecko exact-symbol name -> exact
     English Wikipedia title -> the article summary must contain one of 08's
     SUBJECT_WORDS.
  4. Prediction market (Polymarket): the search answers for each coin, and the
     hourly price history of every matched market whose life overlaps the DATA
     span (first day of MONTHS[0] .. last day of MONTHS[-1]). 08 filters on the
     card span instead; the card span lies inside the data span, so this is a
     superset and needs no moment. The matching test is 08's, unchanged.
  5. Exchange announcements: the six addresses 08 probes, re-probed, raw answer
     kept. No conclusion is written here.

Every fetched body is stored raw, SHA-256 fingerprinted, with its source URL
and fetch time (RULES 2). These third-party sources publish no checksum file;
that is written next to every row. Every failure is recorded with its exact
error text (RULES 20, 21).

Code reuse: 08_external_sources.py is loaded read-only with importlib for its
parse_bls, parse_fomc, base_ticker and SUBJECT_WORDS, so the parsing and the
article-acceptance words are the same code, not a copy. 08's own fetch is not
used: it sends a contact e-mail address in its User-Agent; this script sends
lab_archive.USER_AGENT instead (decision recorded in the run report).

Input   : exam/draw/exam-coins.txt
Output  : exam/data/external/raw/...                 raw bytes as fetched
          exam/data/external/us-calendar.json        parsed, as 08 parses
          exam/data/external/coin-names.json
          exam/data/external/wikipedia.json
          exam/data/external/prediction-market.json
          exam/data/external/announcements-probe.json
          exam/acquisition/external-manifest.jsonl   append-only
          exam/acquisition/runs.jsonl                one line per attempt
Rules   : RULES 2, 19, 20, 21, 23, 26, 27, 29, 30

Run number (RULES 29): run_id = SHA-256 of (this script's bytes + 08's bytes +
the coin list's bytes). Re-runnable: a body already recorded is not fetched
again; a failed fetch is retried and appended after its failure line.
No randomness in this script.
"""

import hashlib
import importlib.util
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lab_archive import USER_AGENT, Manifest, sha256_bytes, sha256_file, utc_now_iso  # noqa: E402

SCRIPT_PATH = os.path.abspath(__file__)
SCRIPTS_DIR = os.path.dirname(SCRIPT_PATH)
ROOT = os.path.dirname(SCRIPTS_DIR)
EXT08_PATH = os.path.join(SCRIPTS_DIR, "08_external_sources.py")

_spec = importlib.util.spec_from_file_location("ext08", EXT08_PATH)
ext08 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ext08)

# ---------------------------------------------------------------- constants --
# Network behaviour: the same values 08 uses.
HTTP_TIMEOUT_S = ext08.HTTP_TIMEOUT_S
HTTP_RETRIES = ext08.HTTP_RETRIES
HTTP_BACKOFF_S = ext08.HTTP_BACKOFF_S
POLITE_SLEEP_S = ext08.POLITE_SLEEP_S

# Fetch spans: the same values 08 uses (calendar months and Wikipedia span
# cover the card span of the whole period, 2025-08 lookback included).
CAL_MONTHS = ext08.CAL_MONTHS
WIKI_START = ext08.WIKI_START
WIKI_END = ext08.WIKI_END
POLY_LIMIT_PER_TYPE = ext08.POLY_LIMIT_PER_TYPE
SUBJECT_WORDS = ext08.SUBJECT_WORDS
ANNOUNCEMENT_PROBES = ext08.ANNOUNCEMENT_PROBES

# Data span for the prediction-market overlap test: the same months as
# exam_24_acquire_archive.py (2025-08 .. 2026-08), as epoch milliseconds.
DATA_SPAN_LO_MS = int(datetime(2025, 8, 1, tzinfo=timezone.utc).timestamp() * 1000)
DATA_SPAN_HI_MS = int(datetime(2026, 9, 1, tzinfo=timezone.utc).timestamp() * 1000) - 1

COIN_LIST = os.path.join(ROOT, "exam", "draw", "exam-coins.txt")
OUT_DIR = os.path.join(ROOT, "exam", "data", "external")
ACQ_DIR = os.path.join(ROOT, "exam", "acquisition")
MANIFEST_PATH = os.path.join(ACQ_DIR, "external-manifest.jsonl")
RUNS_PATH = os.path.join(ACQ_DIR, "runs.jsonl")


def run_id() -> str:
    h = hashlib.sha256()
    for p in (SCRIPT_PATH, EXT08_PATH, COIN_LIST):
        with open(p, "rb") as fh:
            h.update(fh.read())
        h.update(b"\n--\n")
    return h.hexdigest()


def fetch(url: str) -> tuple:
    """(bytes, error). Same retry policy as 08's fetch; different User-Agent."""
    last = None
    for attempt in range(HTTP_RETRIES):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT_S) as resp:
                body = resp.read()
                if resp.status == 202 and not body:
                    return None, ("HTTP 202 with a zero-length body "
                                  "(the host answered but returned nothing)")
                return body, None
        except urllib.error.HTTPError as exc:
            last = "HTTP %s %s" % (exc.code, exc.reason)
            if exc.code in (400, 401, 403, 404):
                return None, last
        except Exception as exc:  # noqa: BLE001 - recorded verbatim
            last = "%s: %s" % (type(exc).__name__, exc)
        if attempt < HTTP_RETRIES - 1:
            time.sleep(HTTP_BACKOFF_S * (2 ** attempt))
    return None, last or "unknown error"


def fetch_and_record(url: str, rel: str, manifest: Manifest) -> tuple:
    dest = os.path.join(OUT_DIR, rel)
    row = manifest.get(rel)
    if row and row.get("sha256") and os.path.exists(dest):
        if sha256_file(dest) != row["sha256"]:
            raise SystemExit("STOP (RULES 30): %s on disk differs from its manifest row" % rel)
        with open(dest, "rb") as fh:
            return fh.read(), None, False
    body, err = fetch(url)
    row = {"path": rel, "source_url": url, "downloaded_at_utc": utc_now_iso(),
           "sha256": sha256_bytes(body) if body is not None else None,
           "bytes": len(body) if body is not None else None,
           "checksum_verified": None,
           "checksum_note": "third-party source publishes no checksum file",
           "error": err}
    if body is not None:
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest + ".part", "wb") as fh:
            fh.write(body)
        os.replace(dest + ".part", dest)
    manifest.add(row)
    return body, err, True


def slug(s: str) -> str:
    return re.sub(r"\W+", "_", s)


def write_json(name: str, obj) -> None:
    path = os.path.join(OUT_DIR, name)
    with open(path + ".tmp", "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=1, sort_keys=True)
    os.replace(path + ".tmp", path)


def main() -> int:
    os.makedirs(os.path.join(OUT_DIR, "raw"), exist_ok=True)
    os.makedirs(ACQ_DIR, exist_ok=True)
    rid = run_id()
    started = utc_now_iso()
    with open(COIN_LIST, "r", encoding="utf-8") as fh:
        coins = [ln.strip() for ln in fh if ln.strip()]
    manifest = Manifest(MANIFEST_PATH)
    print("run_id %s started %s coins %d" % (rid, started, len(coins)), flush=True)
    failures = []

    def get(url, rel):
        body, err, fresh = fetch_and_record(url, rel, manifest)
        if fresh:
            time.sleep(POLITE_SLEEP_S)
        if err:
            failures.append({"path": rel, "url": url, "error": err})
        return body, err

    # ------------------------------------------------------- 1 US calendar --
    print("[1/5] US release calendar", flush=True)
    releases, cal_errors = [], []
    for y, m in CAL_MONTHS:
        url = "https://www.bls.gov/schedule/%d/%02d_sched_list.htm" % (y, m)
        body, err = get(url, "raw/bls/%d-%02d.html" % (y, m))
        if err:
            cal_errors.append({"source": "BLS", "url": url, "error": err})
            continue
        rows = ext08.parse_bls(body.decode("utf-8", "replace"))
        if not rows:
            cal_errors.append({"source": "BLS", "url": url,
                               "error": "page fetched (%d bytes) but no release-list "
                                        "table row parsed" % len(body)})
        releases.extend(rows)
    fomc_url = "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"
    body, err = get(fomc_url, "raw/fomc/fomccalendars.html")
    if err:
        cal_errors.append({"source": "Federal Reserve", "url": fomc_url, "error": err})
    else:
        rows = ext08.parse_fomc(body.decode("utf-8", "replace"))
        if not rows:
            cal_errors.append({"source": "Federal Reserve", "url": fomc_url,
                               "error": "page fetched (%d bytes) but no meeting block "
                                        "parsed" % len(body)})
        releases.extend(rows)
    releases.sort(key=lambda e: (e["local_date"], e.get("local_time_et") or ""))
    write_json("us-calendar.json", {"errors": cal_errors, "count": len(releases),
                                    "releases": releases})
    print("      %d releases, %d errors" % (len(releases), len(cal_errors)), flush=True)

    # -------------------------------------------------------- 2 coin names --
    print("[2/5] coin names", flush=True)
    names = {}
    for sym in coins:
        base = ext08.base_ticker(sym)
        url = "https://api.coingecko.com/api/v3/search?query=%s" % urllib.parse.quote(base)
        body, err = get(url, "raw/coingecko/%s.json" % slug(base))
        entry = {"symbol": sym, "base_ticker": base, "source_url": url, "error": err,
                 "name": None, "exact_symbol_hits": []}
        if body is not None:
            try:
                found = json.loads(body).get("coins", [])
                hits = [c for c in found if (c.get("symbol") or "").upper() == base.upper()]
                entry["exact_symbol_hits"] = [{"id": c["id"], "name": c["name"],
                                               "rank": c.get("market_cap_rank")}
                                              for c in hits[:5]]
                if hits:
                    entry["name"] = hits[0]["name"]
                else:
                    entry["error"] = ("CoinGecko search returned %d coins, none with "
                                      "symbol == %s" % (len(found), base))
            except Exception as exc:  # noqa: BLE001
                entry["error"] = "could not parse CoinGecko answer: %s" % exc
        names[sym] = entry
    write_json("coin-names.json", names)

    # --------------------------------------------------------- 3 Wikipedia --
    print("[3/5] Wikipedia pageviews", flush=True)
    wiki = {}
    for sym in coins:
        cand = names[sym].get("name")
        entry = {"symbol": sym, "article": None, "daily": {}, "tried": [], "error": None,
                 "source_url": None,
                 "rule": "08's rule: CoinGecko exact-symbol name -> exact Wikipedia "
                         "title -> summary must mention one of %s" % sorted(SUBJECT_WORDS)}
        if not cand:
            entry["error"] = ("no CoinGecko coin name for this symbol (%s), so there is "
                              "no name to look up on Wikipedia" % names[sym].get("error"))
            wiki[sym] = entry
            continue
        surl = ("https://en.wikipedia.org/w/api.php?action=query&list=search"
                "&srsearch=%s&srlimit=5&format=json" % urllib.parse.quote(cand))
        body, err = get(surl, "raw/wikipedia/search-%s.json" % slug(cand))
        if err:
            entry["tried"].append({"query": cand, "error": err})
            entry["error"] = "Wikipedia search failed: %s" % err
            wiki[sym] = entry
            continue
        titles = [h["title"] for h in json.loads(body).get("query", {}).get("search", [])]
        match = next((t for t in titles if t.lower() == cand.lower()), None)
        tried = {"query": cand, "top_hits": titles[:5], "exact_title_match": match,
                 "subject_check": None}
        entry["tried"].append(tried)
        if match:
            surl2 = ("https://en.wikipedia.org/api/rest_v1/page/summary/%s"
                     % urllib.parse.quote(match.replace(" ", "_"), safe=""))
            body2, err2 = get(surl2, "raw/wikipedia/summary-%s.json" % slug(match))
            if err2:
                tried["subject_check"] = "summary fetch failed: %s" % err2
            else:
                blob = json.loads(body2)
                text = ("%s %s" % (blob.get("description") or "",
                                   blob.get("extract") or "")).lower()
                hit = sorted(w for w in SUBJECT_WORDS if w in text)
                tried["subject_check"] = {"words_found": hit,
                                          "description": blob.get("description")}
                if hit:
                    entry["article"] = match
        if entry["article"] is None:
            entry["error"] = ("no English Wikipedia article passed 08's rule; see 'tried'")
            wiki[sym] = entry
            continue
        art = urllib.parse.quote(entry["article"].replace(" ", "_"), safe="")
        purl = ("https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/"
                "en.wikipedia/all-access/user/%s/daily/%s/%s" % (art, WIKI_START, WIKI_END))
        entry["source_url"] = purl
        body, err = get(purl, "raw/wikipedia/views-%s.json" % slug(entry["article"]))
        if err:
            entry["error"] = "pageview API: %s" % err
        else:
            for it in json.loads(body).get("items", []):
                entry["daily"][it["timestamp"][:8]] = it["views"]
        wiki[sym] = entry
    write_json("wikipedia.json", wiki)

    # ------------------------------------------------- 4 prediction market --
    print("[4/5] prediction market", flush=True)
    poly = {}
    for sym in coins:
        base = ext08.base_ticker(sym)
        queries = [q for q in [names[sym].get("name"), base] if q]
        entry = {"symbol": sym, "queries": queries, "errors": [], "markets_seen": 0,
                 "markets_matched": [], "series": {},
                 "overlap_span": "data span 2025-08-01T00:00Z .. 2026-08-31T23:59:59Z"}
        seen = {}
        for q in queries:
            url = ("https://gamma-api.polymarket.com/public-search?q=%s&limit_per_type=%d"
                   % (urllib.parse.quote(q), POLY_LIMIT_PER_TYPE))
            body, err = get(url, "raw/polymarket/search-%s.json" % slug(q))
            if err:
                entry["errors"].append({"query": q, "error": err})
                continue
            for ev in json.loads(body).get("events", []) or []:
                for mk in ev.get("markets", []) or []:
                    seen[mk.get("slug") or mk.get("id")] = (ev, mk)
        entry["markets_seen"] = len(seen)
        needles = [base.lower()] + [n.lower() for n in [names[sym].get("name")] if n]
        for mslug, (ev, mk) in sorted(seen.items(), key=lambda kv: str(kv[0])):
            text = ("%s %s" % (ev.get("title", ""), mk.get("question", ""))).lower()
            toks = set(re.split(r"[^a-z0-9]+", text))
            if not (any(n in toks for n in needles)
                    or any(n in text for n in needles if " " in n)):
                continue
            s_d, e_d = mk.get("startDate"), mk.get("endDate")
            rec = {"slug": mslug, "question": mk.get("question"), "event": ev.get("title"),
                   "startDate": s_d, "endDate": e_d, "outcomes": mk.get("outcomes"),
                   "overlaps_data_span": None}
            try:
                s_ms = int(datetime.fromisoformat(s_d.replace("Z", "+00:00")).timestamp() * 1000) if s_d else None
                e_ms = int(datetime.fromisoformat(e_d.replace("Z", "+00:00")).timestamp() * 1000) if e_d else None
                rec["overlaps_data_span"] = bool(s_ms is not None and e_ms is not None
                                                 and s_ms <= DATA_SPAN_HI_MS
                                                 and e_ms >= DATA_SPAN_LO_MS)
            except Exception as exc:  # noqa: BLE001
                entry["errors"].append({"slug": mslug, "error": "date parse: %s" % exc})
            entry["markets_matched"].append(rec)
            if not rec["overlaps_data_span"]:
                continue
            try:
                tid = json.loads(mk.get("clobTokenIds") or "[]")[0]
            except Exception:  # noqa: BLE001
                tid = None
            if not tid:
                entry["errors"].append({"slug": mslug, "error": "market has no clobTokenIds"})
                continue
            hurl = ("https://clob.polymarket.com/prices-history?market=%s"
                    "&interval=max&fidelity=60" % tid)
            body, err = get(hurl, "raw/polymarket/history-%s.json" % slug(str(mslug)))
            if err:
                entry["errors"].append({"slug": mslug, "error": "price history: %s" % err})
                continue
            hist = json.loads(body).get("history", [])
            entry["series"][mslug] = {"points": len(hist),
                                      "hourly": {int(p["t"]) * 1000: p["p"] for p in hist}}
        poly[sym] = entry
        print("      line %2d seen %3d matched %2d overlapping %2d" % (
            coins.index(sym) + 1, entry["markets_seen"], len(entry["markets_matched"]),
            sum(1 for r in entry["markets_matched"] if r["overlaps_data_span"])), flush=True)
    write_json("prediction-market.json", poly)

    # ------------------------------------------------------ 5 announcements --
    print("[5/5] announcement probes", flush=True)
    probes = []
    for exchange, label, url in ANNOUNCEMENT_PROBES:
        body, err = get(url, "raw/announcements/%s.txt" % slug(label))
        rec = {"exchange": exchange, "label": label, "url": url, "error": err,
               "bytes": None if body is None else len(body)}
        if body is not None:
            try:
                parsed = json.loads(body)
                rec["json_type"] = type(parsed).__name__
                if isinstance(parsed, list):
                    rec["items_returned"] = len(parsed)
                    if parsed and isinstance(parsed[0], dict):
                        dates = sorted(str(p.get("published_at", "")) for p in parsed)
                        rec["oldest_published_at"] = dates[0]
                        rec["newest_published_at"] = dates[-1]
            except Exception:  # noqa: BLE001
                rec["json_type"] = None
        probes.append(rec)
        print("      %-40s %s" % (label, err or ("%s bytes" % rec["bytes"])), flush=True)
    write_json("announcements-probe.json", {"probes": probes})

    finished = utc_now_iso()
    attempt = {"run_id": rid, "script": "scripts/exam_25_acquire_external.py",
               "script_sha256": sha256_file(SCRIPT_PATH),
               "reused_module_sha256": {"scripts/08_external_sources.py": sha256_file(EXT08_PATH)},
               "coin_list_sha256": sha256_file(COIN_LIST),
               "started_at_utc": started, "finished_at_utc": finished,
               "fetch_failures_this_attempt": failures,
               "derived_files_sha256": {n: sha256_file(os.path.join(OUT_DIR, n)) for n in (
                   "us-calendar.json", "coin-names.json", "wikipedia.json",
                   "prediction-market.json", "announcements-probe.json")}}
    with open(RUNS_PATH, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(attempt, sort_keys=True) + "\n")
        fh.flush()
        os.fsync(fh.fileno())
    print("finished %s  fetch failures %d" % (finished, len(failures)), flush=True)
    for f in failures:
        print("  FAILED %s  %s" % (f["path"], f["error"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
