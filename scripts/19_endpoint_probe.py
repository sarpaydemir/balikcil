#!/usr/bin/env python3
"""
19_endpoint_probe.py — establish the contract of the outside typed-choice endpoint.

WHAT IT DOES
    Sends a fixed, named list of probe requests to the decision endpoint described in
    external/2026-09-19-MEMO-cheap-decisions.md and records, for every probe, the HTTP
    status, the full response body, the wall-clock latency and the request that caused it.
    It asserts nothing about what the answers should be: it only records the shape of
    what comes back, including for malformed input.

INPUT
    env OPENROUTER_API_KEY  — the bearer token. Read from the environment only.
    env DECISION_MODEL      — the model id. Falls back to the memo's literal id.
    (no file in this laboratory is read)

OUTPUT
    external/calibration/probes/probe-results.json  — one record per probe
    external/calibration/probes/probe-results.md    — the same, human readable

RULES IT IMPLEMENTS
    RULES 19 — every latency/cost figure written here is measured, never estimated.
    RULES 20 — a failure is recorded with its exact error text, never as "nothing there".
    RULES 21 — a technical failure is reported as a failure.
    RULES 23 — timestamps come from the system clock.
    RULES 30 — append-only: the script refuses to overwrite an existing output file
               whose content would differ.
    MEMO §6 — the key is read from the environment and is scrubbed from every byte
              written to disk.

SAFETY
    Every string written to disk passes through scrub(), which replaces the key value
    with "<REDACTED:OPENROUTER_API_KEY>". Request headers are never recorded.
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

# ---------------------------------------------------------------------------
# Constants. Every one of these has a written source.
# ---------------------------------------------------------------------------

# Source: external/2026-09-19-MEMO-cheap-decisions.md §3 (the request shape block).
ENDPOINT = "https://openrouter.ai/api/alpha/decisions"

# Source: external/2026-09-19-MEMO-cheap-decisions.md §3 ("model": "typesafe/jev-1.13").
# Overridden by the DECISION_MODEL environment variable if the user set one.
MODEL_FALLBACK = "typesafe/jev-1.13"

# Engineering constant, set by this script, not taken from any result:
# a probe that has not answered in 60 s is recorded as a timeout.
TIMEOUT_S = 60

REPO = Path(__file__).resolve().parent.parent
OUT_DIR = REPO / "external" / "calibration" / "probes"

KEY = os.environ.get("OPENROUTER_API_KEY", "")
MODEL = os.environ.get("DECISION_MODEL", "").strip() or MODEL_FALLBACK


def scrub(text: str) -> str:
    """Remove the key — and the account id the endpoint echoes — on the way to disk.

    The account id is not the key and no rule names it. It is redacted because these
    artefacts are committed to git; the decision is recorded in the run report.
    """
    if not text:
        return text
    out = text
    if KEY:
        out = out.replace(KEY, "<REDACTED:OPENROUTER_API_KEY>")
        # also the bare token after a "Bearer " prefix, in case of re-encoding
        if len(KEY) > 12:
            out = out.replace(KEY[-12:], "<REDACTED-TAIL>")
    out = re.sub(r'"user_id"\s*:\s*"[^"]*"', '"user_id": "<REDACTED:ACCOUNT_ID>"', out)
    out = re.sub(r"user_[A-Za-z0-9]{16,}", "<REDACTED:ACCOUNT_ID>", out)
    return out


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


# ---------------------------------------------------------------------------
# The probes. Each is (name, purpose, body, headers_override).
# body may be a dict (sent as JSON) or a str (sent as a raw body, for malformed tests).
# ---------------------------------------------------------------------------

STATE = (
    "The funding line on this note reads +0.0100% with an 8 hour interval and "
    "the interval-changed flag set to no."
)

CHOICE_Q = {
    "field": {
        "type": "choice",
        "instructions": "Which single field does this sentence describe?",
        "criteria": {
            "FUNDING": "the sentence is about the funding rate or its payment interval",
            "PRICE": "the sentence is about price, volume or volatility",
            "OTHER": "neither of the above",
        },
    }
}


def probes() -> list[dict]:
    p: list[dict] = []

    def add(name, purpose, body, headers=None):
        p.append({"name": name, "purpose": purpose, "body": body, "headers": headers})

    # --- 1. the memo's own shape, verbatim -------------------------------------
    add("01_choice_memo_shape",
        "the exact request shape printed in the memo, three options",
        {"model": MODEL, "state": STATE, "questions": CHOICE_Q})

    # --- 2. does choice scale with the option count? ---------------------------
    add("02_choice_two_options",
        "choice with two options",
        {"model": MODEL, "state": STATE, "questions": {
            "yesno": {"type": "choice",
                      "instructions": "Does this sentence mention a funding interval?",
                      "criteria": {"YES": "it does", "NO": "it does not"}}}})

    add("03_choice_six_options",
        "choice with six options",
        {"model": MODEL, "state": STATE, "questions": {
            "bucket": {"type": "choice",
                       "instructions": "Pick the closest topic.",
                       "criteria": {f"OPT_{i}": f"description number {i}" for i in range(1, 7)}}}})

    # --- 3. score: criteria as an array, per the memo --------------------------
    add("04_score_array_criteria",
        "score type, criteria given as an array as the memo states",
        {"model": MODEL, "state": STATE, "questions": {
            "certainty": {"type": "score",
                          "instructions": "Rate how certain the writer of this sentence sounds, 1 to 5.",
                          "criteria": ["1 = very unsure", "2", "3", "4", "5 = completely certain"]}}})

    add("05_score_two_point_array",
        "score type with a two-element criteria array, to see what range comes back",
        {"model": MODEL, "state": STATE, "questions": {
            "certainty": {"type": "score",
                          "instructions": "Rate certainty.",
                          "criteria": ["low", "high"]}}})

    add("06_score_no_criteria",
        "score type with instructions but no criteria at all",
        {"model": MODEL, "state": STATE, "questions": {
            "certainty": {"type": "score", "instructions": "Rate certainty from 1 to 5."}}})

    add("07_score_record_criteria",
        "score type given a record instead of an array (deliberate type mismatch)",
        {"model": MODEL, "state": STATE, "questions": {
            "certainty": {"type": "score", "instructions": "Rate certainty.",
                          "criteria": {"LOW": "unsure", "HIGH": "sure"}}}})

    # --- 4. the third type, which the memo names but does not describe ---------
    add("08_noul_bare",
        "the 'noul' type with instructions only",
        {"model": MODEL, "state": STATE, "questions": {
            "thing": {"type": "noul", "instructions": "Name the single field this sentence is about."}}})

    add("09_noul_with_criteria",
        "the 'noul' type with a criteria record attached",
        {"model": MODEL, "state": STATE, "questions": {
            "thing": {"type": "noul", "instructions": "Name the field.",
                      "criteria": {"A": "one", "B": "two"}}}})

    # --- 5. several questions in one call --------------------------------------
    add("10_two_questions_one_call",
        "two questions of different types in a single request",
        {"model": MODEL, "state": STATE, "questions": {
            "field": CHOICE_Q["field"],
            "certainty": {"type": "score", "instructions": "Rate certainty 1-5.",
                          "criteria": ["1", "2", "3", "4", "5"]}}})

    # --- 6. malformed input -----------------------------------------------------
    add("11_choice_no_instructions",
        "choice with criteria but no instructions field",
        {"model": MODEL, "state": STATE, "questions": {
            "field": {"type": "choice",
                      "criteria": {"A": "one", "B": "two"}}}})

    add("12_choice_no_criteria",
        "choice with instructions but no criteria",
        {"model": MODEL, "state": STATE, "questions": {
            "field": {"type": "choice", "instructions": "Pick one."}}})

    add("13_unknown_type",
        "a question type that does not exist",
        {"model": MODEL, "state": STATE, "questions": {
            "field": {"type": "banana", "instructions": "Pick one.",
                      "criteria": {"A": "one", "B": "two"}}}})

    add("14_no_questions_key",
        "state present, questions key absent",
        {"model": MODEL, "state": STATE})

    add("15_empty_questions",
        "questions present but empty",
        {"model": MODEL, "state": STATE, "questions": {}})

    add("16_no_state",
        "questions present, state absent",
        {"model": MODEL, "questions": CHOICE_Q})

    add("17_empty_state",
        "state present but the empty string",
        {"model": MODEL, "state": "", "questions": CHOICE_Q})

    add("18_no_model",
        "model key absent",
        {"state": STATE, "questions": CHOICE_Q})

    add("19_bad_model",
        "a model id that should not exist",
        {"model": "typesafe/jev-0.0-does-not-exist", "state": STATE, "questions": CHOICE_Q})

    add("20_malformed_json",
        "a body that is not valid JSON",
        '{"model": "' + MODEL + '", "state": "x", "questions": {')

    add("21_bad_auth",
        "a syntactically plausible but wrong bearer token (the real key is NOT sent)",
        {"model": MODEL, "state": STATE, "questions": CHOICE_Q},
        {"Authorization": "Bearer not-a-real-token-deliberately-invalid"})

    add("22_no_auth",
        "no Authorization header at all",
        {"model": MODEL, "state": STATE, "questions": CHOICE_Q},
        {"__drop_auth__": "1"})

    # --- 7. the 32,000 token context limit --------------------------------------
    # ~4 chars per token is the usual rough ratio; 200,000 chars is far past 32k tokens.
    add("23_oversize_state",
        "a state far larger than the stated 32,000 token context",
        {"model": MODEL, "state": ("the funding rate moved. " * 8700)[:200000],
         "questions": CHOICE_Q})

    # --- 8. repeatability: same request twice ------------------------------------
    add("24_repeat_a",
        "identical to probe 01, first of two, to see whether the answer is deterministic",
        {"model": MODEL, "state": STATE, "questions": CHOICE_Q})
    add("25_repeat_b",
        "identical to probe 01, second of two",
        {"model": MODEL, "state": STATE, "questions": CHOICE_Q})

    # --- 9. a parameter the memo says does not exist ------------------------------
    add("26_temperature_param",
        "a temperature parameter, which the memo says is unsupported",
        {"model": MODEL, "state": STATE, "questions": CHOICE_Q, "temperature": 0.9})

    # --- 10. does it accept a chat-completions body at all? -----------------------
    add("27_chat_completion_body",
        "an OpenAI chat-completions body posted to this endpoint",
        {"model": MODEL, "messages": [{"role": "user", "content": "hello"}]})

    # --- 11. follow-ups, written after reading the first round of probes ----------
    # probe 09's validation error pointed at criteria.true / criteria.false, so noul
    # looks like a two-sided question rather than a free-text one.
    add("28_noul_true_false_criteria",
        "noul with a criteria record keyed 'true' and 'false', as probe 09's error implied",
        {"model": MODEL, "state": STATE, "questions": {
            "thing": {"type": "noul",
                      "instructions": "Is this sentence about the funding field?",
                      "criteria": {"true": "it is about funding",
                                   "false": "it is about something else"}}}})

    add("29_score_three_point_array",
        "score with a three-element array, to pin the scale the returned score sits on",
        {"model": MODEL, "state": STATE, "questions": {
            "certainty": {"type": "score", "instructions": "Rate certainty.",
                          "criteria": ["low", "medium", "high"]}}})

    add("30_score_one_point_array",
        "score with a one-element array",
        {"model": MODEL, "state": STATE, "questions": {
            "certainty": {"type": "score", "instructions": "Rate certainty.",
                          "criteria": ["only"]}}})

    # probe 16's union error said state may be string | record | array.
    add("31_state_as_record",
        "state given as a record rather than a string",
        {"model": MODEL, "state": {"funding": "+0.0100%", "interval_h": 8,
                                   "interval_changed": False},
         "questions": CHOICE_Q})

    add("32_state_as_array",
        "state given as an array rather than a string",
        {"model": MODEL, "state": ["funding +0.0100%", "interval 8 h", "changed: no"],
         "questions": CHOICE_Q})

    add("33_unknown_top_level_key",
        "an unknown top-level key, to see whether unknown keys are rejected or ignored",
        {"model": MODEL, "state": STATE, "questions": CHOICE_Q,
         "this_key_does_not_exist": {"nested": [1, 2, 3]}})

    # bracket the context limit: probe 23 (200,000 chars) failed with max_tokens_exceeded.
    add("34_large_state_100k_chars",
        "a state of 100,000 characters, to bracket the context limit from below",
        {"model": MODEL, "state": ("the funding rate moved. " * 4350)[:100000],
         "questions": CHOICE_Q})

    add("35_large_state_140k_chars",
        "a state of 140,000 characters, to bracket the context limit from above",
        {"model": MODEL, "state": ("the funding rate moved. " * 6100)[:140000],
         "questions": CHOICE_Q})

    add("36_label_odd_characters",
        "a question label containing a space, a dot and a non-ascii character",
        {"model": MODEL, "state": STATE, "questions": {
            "my label.1 ö": {"type": "choice", "instructions": "Pick one.",
                             "criteria": {"A": "one", "B": "two"}}}})

    add("37_option_keys_with_spaces",
        "choice option keys containing spaces and punctuation",
        {"model": MODEL, "state": STATE, "questions": {
            "field": {"type": "choice", "instructions": "Pick one.",
                      "criteria": {"funding / interval": "about funding",
                                   "price & volume": "about price"}}}})

    return p


def run_probe(pr: dict) -> dict:
    headers = {"Content-Type": "application/json"}
    if not (pr["headers"] or {}).get("__drop_auth__"):
        headers["Authorization"] = (pr["headers"] or {}).get("Authorization", f"Bearer {KEY}")
    rec: dict = {
        "name": pr["name"],
        "purpose": pr["purpose"],
        "sent_at_utc": now_iso(),
        "request_body": pr["body"] if isinstance(pr["body"], str) else json.loads(json.dumps(pr["body"])),
        "auth": "real-key" if headers.get("Authorization", "").endswith(KEY) and KEY else
                ("absent" if "Authorization" not in headers else "deliberately-wrong-key"),
    }
    # keep the record small for the oversize probe
    if isinstance(pr["body"], dict) and isinstance(pr["body"].get("state"), str) and len(pr["body"]["state"]) > 400:
        rec["request_body"] = dict(rec["request_body"])
        rec["request_body"]["state"] = (
            f"<{len(pr['body']['state'])} chars elided; begins: "
            f"{pr['body']['state'][:60]!r}>"
        )
    t0 = time.perf_counter()
    try:
        if isinstance(pr["body"], str):
            r = requests.post(ENDPOINT, headers=headers, data=pr["body"].encode(), timeout=TIMEOUT_S)
        else:
            r = requests.post(ENDPOINT, headers=headers, json=pr["body"], timeout=TIMEOUT_S)
        rec["latency_s"] = round(time.perf_counter() - t0, 4)
        rec["http_status"] = r.status_code
        rec["response_headers_subset"] = {
            k: v for k, v in r.headers.items()
            if k.lower() in {"content-type", "x-request-id", "retry-after", "server"}
        }
        body = r.text
        rec["response_text_len"] = len(body)
        try:
            rec["response_json"] = json.loads(body)
        except Exception:
            rec["response_json"] = None
            rec["response_text"] = body[:4000]
    except Exception as e:  # network-level failure is a result to record, not to hide
        rec["latency_s"] = round(time.perf_counter() - t0, 4)
        rec["http_status"] = None
        rec["transport_error"] = f"{type(e).__name__}: {e}"
    return rec


def write_append_only(path: Path, content: str) -> str:
    """RULES 30: never overwrite an existing file with different content."""
    digest = hashlib.sha256(content.encode()).hexdigest()
    if path.exists():
        old = path.read_text()
        if old != content:
            sys.exit(f"REFUSING to overwrite {path} with different content (RULES 30). "
                     f"existing sha256={hashlib.sha256(old.encode()).hexdigest()} new={digest}")
        return digest
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    return digest


def main() -> int:
    if not KEY:
        sys.exit("OPENROUTER_API_KEY is not in the environment. Nothing was sent.")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    started = now_iso()
    records = []
    for pr in probes():
        rec = run_probe(pr)
        records.append(rec)
        print(f"  {rec['name']:28s} http={rec.get('http_status')} "
              f"{rec.get('latency_s')}s "
              f"{'TRANSPORT-ERROR' if 'transport_error' in rec else ''}")

    out = {
        "script": "scripts/19_endpoint_probe.py",
        "endpoint": ENDPOINT,
        "model_requested": MODEL,
        "started_utc": started,
        "finished_utc": now_iso(),
        "probe_count": len(records),
        "probes": records,
    }
    text = scrub(json.dumps(out, indent=2, ensure_ascii=False, sort_keys=False))
    digest = write_append_only(OUT_DIR / "probe-results.json", text)
    print(f"\nwrote {OUT_DIR/'probe-results.json'}  sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
