#!/usr/bin/env python3
"""
21_run_endpoint.py — put the 100 calibration items to the outside decision endpoint.

WHAT IT DOES
    For each item in external/calibration/items.jsonl it makes three calls, one per
    question set, and appends the whole response to a JSONL file as it goes. It
    measures wall-clock latency per call and records the usage block, so that cost is
    counted and never estimated.

    It cannot see the answer key. It reads items.jsonl, which holds only id and text,
    and it refuses to start unless key.jsonl still hashes to the digest recorded in
    KEY-MANIFEST.json — the digest that was notarised at the endpoint before the first
    item call. It reads key.jsonl's bytes to hash them and never parses them.

INPUT
    external/calibration/items.jsonl        (id, text_full, text_no_confidence)
    external/calibration/KEY-MANIFEST.json  (the digest to check against)
    env OPENROUTER_API_KEY, env DECISION_MODEL

OUTPUT
    external/calibration/responses.jsonl    — one record per call, appended live
    external/calibration/RUN-MANIFEST.json  — totals, written when the run completes

RULES IT IMPLEMENTS
    MEMO §4 step 3 — run the model on the same items, after the key exists.
    RULES 19 — cost and latency are measured from the response, never estimated.
    RULES 20/21 — a failed call is written down with its exact error and counted as a
                  failure, not silently dropped.
    RULES 23 — the clock is read, from the system and from the provider's own id.
    RULES 26 — the run checkpoints after every call and can be resumed.
    RULES 30 — responses.jsonl is append-only; a pair already answered is never
               re-asked and never overwritten.
    MEMO §6 — the key is read from the environment and scrubbed from everything written.

THE QUESTION SETS
    FIELD      choice, four options. The option descriptions are quoted verbatim from
               TEAM.md's four watcher entries. Input: text_full.
    CERTAINTY  score, five-point array. Input: text_no_confidence — the watcher's own
               1-5 digit is stripped out, so the answer is not in the text.
    CARDCOUNT  choice, two options. A mechanical property of the same text, used as a
               control: its key is certain, so the attainable ceiling is 100%.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

ENDPOINT = "https://openrouter.ai/api/alpha/decisions"       # memo §3
MODEL = os.environ.get("DECISION_MODEL", "").strip() or "typesafe/jev-1.13"
KEY = os.environ.get("OPENROUTER_API_KEY", "")

# Engineering constants set here and written down:
TIMEOUT_S = 60          # a call that has not answered in 60 s counts as a failure
MAX_RETRIES = 3         # transport-level retries; every attempt is recorded
RETRY_SLEEP_S = 2.0

REPO = Path(__file__).resolve().parent.parent
CAL = REPO / "external" / "calibration"
ITEMS = CAL / "items.jsonl"
KEYFILE = CAL / "key.jsonl"
MANIFEST = CAL / "KEY-MANIFEST.json"
RESPONSES = CAL / "responses.jsonl"

# --- the menus -------------------------------------------------------------------
# FIELD option descriptions are quoted from TEAM.md, one per watcher entry.
FIELD_CRITERIA = {
    "EXCHANGE_BEHAVIOUR":
        "changes in the funding rate and the payment interval; listing, delisting and "
        "warning announcements; every administrative decision the exchange takes",
    "CROWD":
        "open interest, long/short ratios, the ratio of large players, taker buy/sell "
        "pressure, the funding rate itself",
    "OUTSIDE_WORLD":
        "Binance and Korean exchange announcements, the US release calendar, the number "
        "of people viewing the page on Wikipedia, the prediction market, the state of "
        "bitcoin and ethereum over those hours",
    "PRICE_ITSELF":
        "price, volume, trade count, order book depth, volatility",
}

QUESTION_SETS = {
    "FIELD": {
        "text_field": "text_full",
        "question": {
            "field_of_view": {
                "type": "choice",
                "instructions": (
                    "This is one observation note written by one of four observers, each "
                    "of whom was told to look at one thing only. Which observer's field "
                    "of view does this note belong to?"
                ),
                "criteria": FIELD_CRITERIA,
            }
        },
        "answer_label": "field_of_view",
    },
    "CERTAINTY": {
        "text_field": "text_no_confidence",
        "question": {
            "certainty": {
                "type": "score",
                "instructions": (
                    "The observer who wrote this note rated how sure of it they were, on "
                    "a scale of 1 to 5, and that rating has been removed from the text. "
                    "Which rating did they give it?"
                ),
                "criteria": [
                    "1 - the observer marked it as their least sure kind of note",
                    "2",
                    "3",
                    "4",
                    "5 - the observer marked it as their most sure kind of note",
                ],
            }
        },
        "answer_label": "certainty",
    },
    "CARDCOUNT": {
        "text_field": "text_full",
        "question": {
            "card_count": {
                "type": "choice",
                "instructions": (
                    "Card numbers in this note are written in the form C followed by "
                    "three digits, for example C042. How many different card numbers "
                    "does this note cite?"
                ),
                "criteria": {
                    "SINGLE": "exactly one different card number appears in the note",
                    "MULTI": "two or more different card numbers appear in the note",
                },
            }
        },
        "answer_label": "card_count",
    },
}


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def scrub(text: str) -> str:
    if not text:
        return text
    out = text
    if KEY:
        out = out.replace(KEY, "<REDACTED:OPENROUTER_API_KEY>")
        if len(KEY) > 12:
            out = out.replace(KEY[-12:], "<REDACTED-TAIL>")
    out = re.sub(r'"user_id"\s*:\s*"[^"]*"', '"user_id": "<REDACTED:ACCOUNT_ID>"', out)
    out = re.sub(r"user_[A-Za-z0-9]{16,}", "<REDACTED:ACCOUNT_ID>", out)
    return out


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def load_items() -> list[dict]:
    items = [json.loads(l) for l in ITEMS.read_text().splitlines() if l.strip()]
    allowed = {"id", "text_full", "text_no_confidence"}
    for it in items:
        extra = set(it) - allowed
        if extra:
            sys.exit(f"items.jsonl carries unexpected field(s) {extra} — a label could "
                     f"leak into the run. Stopping.")
    return items


def already_done() -> set[tuple[str, str]]:
    done = set()
    if RESPONSES.exists():
        for line in RESPONSES.read_text().splitlines():
            if not line.strip():
                continue
            r = json.loads(line)
            if r.get("http_status") == 200:
                done.add((r["item_id"], r["question_set"]))
    return done


def call(state: str, question: dict) -> dict:
    body = {"model": MODEL, "state": state, "questions": question}
    attempts = []
    for attempt in range(1, MAX_RETRIES + 1):
        t0 = time.perf_counter()
        try:
            r = requests.post(
                ENDPOINT,
                headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
                json=body, timeout=TIMEOUT_S)
            lat = round(time.perf_counter() - t0, 4)
            rec = {"attempt": attempt, "latency_s": lat, "http_status": r.status_code}
            try:
                rec["response"] = r.json()
            except Exception:
                rec["response"] = None
                rec["response_text"] = r.text[:2000]
            attempts.append(rec)
            if r.status_code == 200:
                return {"attempts": attempts, **rec}
            if r.status_code < 500 and r.status_code != 429:
                return {"attempts": attempts, **rec}      # a 4xx will not fix itself
        except Exception as e:
            lat = round(time.perf_counter() - t0, 4)
            attempts.append({"attempt": attempt, "latency_s": lat, "http_status": None,
                             "transport_error": f"{type(e).__name__}: {e}"})
        if attempt < MAX_RETRIES:
            time.sleep(RETRY_SLEEP_S)
    return {"attempts": attempts, **attempts[-1]}


def main() -> int:
    if not KEY:
        sys.exit("OPENROUTER_API_KEY is not in the environment. Nothing was sent.")
    if not ITEMS.exists() or not MANIFEST.exists():
        sys.exit("items.jsonl or KEY-MANIFEST.json missing — run 20_build_key.py first.")

    man = json.loads(MANIFEST.read_text())
    key_now = sha256_file(KEYFILE)          # bytes hashed; the file is never parsed here
    if key_now != man["key_sha256"]:
        sys.exit(f"key.jsonl has changed since it was notarised "
                 f"(manifest {man['key_sha256']}, now {key_now}). Refusing to run: the "
                 f"ordering condition of MEMO §4 would no longer hold.")

    items = load_items()
    done = already_done()
    todo = [(it, qname) for it in items for qname in QUESTION_SETS
            if (it["id"], qname) not in done]
    print(f"{len(items)} items x {len(QUESTION_SETS)} question sets = "
          f"{len(items)*len(QUESTION_SETS)} calls; {len(done)} already done; "
          f"{len(todo)} to make")

    started = now_iso()
    t_start = time.perf_counter()
    n_ok = n_fail = 0
    with RESPONSES.open("a") as fh:
        for i, (it, qname) in enumerate(todo, start=1):
            qs = QUESTION_SETS[qname]
            state = it[qs["text_field"]]
            out = call(state, qs["question"])
            gid = ((out.get("response") or {}).get("id") or "")
            m = re.match(r"gen-dec-(\d+)-", gid)
            rec = {
                "item_id": it["id"],
                "question_set": qname,
                "sent_at_utc": now_iso(),
                "state_sha256": hashlib.sha256(state.encode()).hexdigest(),
                "state_chars": len(state),
                "http_status": out.get("http_status"),
                "latency_s": out.get("latency_s"),
                "attempts": len(out["attempts"]),
                "response": out.get("response"),
                "response_text": out.get("response_text"),
                "transport_error": out.get("transport_error"),
                "attempt_detail": out["attempts"] if len(out["attempts"]) > 1 else None,
                "provider_unix_time": int(m.group(1)) if m else None,
            }
            fh.write(scrub(json.dumps(rec, ensure_ascii=False)) + "\n")
            fh.flush()
            if rec["http_status"] == 200:
                n_ok += 1
            else:
                n_fail += 1
                print(f"  FAILURE {it['id']}/{qname}: http={rec['http_status']} "
                      f"{scrub(json.dumps(rec.get('response') or rec.get('transport_error')))[:300]}")
            if i % 25 == 0:
                print(f"  {i}/{len(todo)} calls, {round(time.perf_counter()-t_start,1)}s elapsed")

    # totals over the whole responses file, not just this pass
    rows = [json.loads(l) for l in RESPONSES.read_text().splitlines() if l.strip()]
    ok = [r for r in rows if r["http_status"] == 200]
    cost = sum(r["response"]["usage"]["cost"] for r in ok)
    lat = sorted(r["latency_s"] for r in rows)
    run_man = {
        "script": "scripts/21_run_endpoint.py",
        "started_utc": started,
        "finished_utc": now_iso(),
        "endpoint": ENDPOINT,
        "model_requested": MODEL,
        "model_served": ok[0]["response"]["model"] if ok else None,
        "items_sha256": sha256_file(ITEMS),
        "key_sha256_at_run_time": key_now,
        "calls_total": len(rows),
        "calls_ok": len(ok),
        "calls_failed": len(rows) - len(ok),
        "cost_usd_measured": round(cost, 8),
        "input_tokens_total": sum(r["response"]["usage"]["input_tokens"] for r in ok),
        "output_tokens_total": sum(r["response"]["usage"]["output_tokens"] for r in ok),
        "latency_s_median": lat[len(lat)//2] if lat else None,
        "latency_s_max": lat[-1] if lat else None,
        "wall_clock_s_this_pass": round(time.perf_counter() - t_start, 1),
        "responses_sha256": sha256_file(RESPONSES),
    }
    (CAL / "RUN-MANIFEST.json").write_text(
        scrub(json.dumps(run_man, indent=2, ensure_ascii=False)))
    print(json.dumps(run_man, indent=2))
    return 0 if run_man["calls_failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
