#!/usr/bin/env python3
"""
22_compare.py — compare the endpoint's answers against the answer key.

This is the first script in the chain that reads a label. 20_build_key.py wrote the
key and notarised its digest; 21_run_endpoint.py made every call without being able to
see a label. This script opens both and puts them side by side.

WHAT IT DOES
    1. Checks the ordering condition of MEMO §4 mechanically: the key file still hashes
       to the digest that was notarised, and every single call carries a provider
       timestamp later than that notarisation. If either fails it stops, because the
       comparison would then be worthless.
    2. Writes a per-item comparison row for every item and question set.
    3. Reports, per question set: agreement rate against the key and against the
       base-rate baseline, the confusion matrix, the confidence of every item it got
       wrong, and the confidence distribution of the items it got right.
    4. Walks an accept/escalate threshold across the measured confidence range and
       reports, at each threshold, how much is accepted, how accurate the accepted
       part is, how many errors slip through, and how much is escalated. This is the
       distribution MEMO §4 step 5 asks to be read off, and nothing here sets a
       threshold.

INPUT
    external/calibration/key.jsonl, responses.jsonl, KEY-MANIFEST.json, RUN-MANIFEST.json

OUTPUT
    external/calibration/comparison.jsonl   — one row per (item, question set)
    external/calibration/ANALYSIS.json      — every number quoted in the report

RULES IT IMPLEMENTS
    RULES 19 — every number here is computed from a file, none estimated.
    RULES 22 — what could not be measured is named in the output, not dropped.
    RULES 29/30 — deterministic from its input; refuses to overwrite different content.
    RULES 31 — the unknowns line is filled in and cannot be empty.
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CAL = REPO / "external" / "calibration"

# Engineering constant: the thresholds the escalation curve is walked at. They are
# report grid points, not an operating threshold for this laboratory.
GRID = [0.50, 0.60, 0.70, 0.80, 0.85, 0.90, 0.95, 0.99, 1.00]


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def write_append_only(path: Path, content: str) -> str:
    d = hashlib.sha256(content.encode()).hexdigest()
    if path.exists() and path.read_text() != content:
        sys.exit(f"REFUSING to overwrite {path} with different content (RULES 30).")
    path.write_text(content)
    return d


def main() -> int:
    key_man = json.loads((CAL / "KEY-MANIFEST.json").read_text())
    run_man = json.loads((CAL / "RUN-MANIFEST.json").read_text())
    key = {json.loads(l)["id"]: json.loads(l)
           for l in (CAL / "key.jsonl").read_text().splitlines() if l.strip()}
    rows = [json.loads(l) for l in (CAL / "responses.jsonl").read_text().splitlines() if l.strip()]

    # ---- 1. the ordering condition, checked and not promised ----------------------
    order_checks = {}
    key_now = sha256_file(CAL / "key.jsonl")
    order_checks["key_digest_matches_notarised"] = (key_now == key_man["key_sha256"])
    notary_t = key_man["notarisation"].get("provider_unix_time")
    call_times = [r["provider_unix_time"] for r in rows if r.get("provider_unix_time")]
    order_checks["notarisation_provider_unix_time"] = notary_t
    order_checks["earliest_call_provider_unix_time"] = min(call_times) if call_times else None
    order_checks["calls_with_no_provider_time"] = sum(
        1 for r in rows if not r.get("provider_unix_time"))
    order_checks["every_call_after_notarisation"] = bool(
        call_times and notary_t and min(call_times) > notary_t)
    order_checks["seconds_between_notarisation_and_first_call"] = (
        min(call_times) - notary_t if call_times and notary_t else None)
    if not (order_checks["key_digest_matches_notarised"]
            and order_checks["every_call_after_notarisation"]):
        sys.exit(f"ORDERING CONDITION FAILED: {json.dumps(order_checks, indent=2)}\n"
                 f"MEMO §4 makes the comparison worthless in that case. Stopping.")

    # ---- 2. per-item comparison ---------------------------------------------------
    comp = []
    for r in rows:
        if r["http_status"] != 200:
            comp.append({"item_id": r["item_id"], "question_set": r["question_set"],
                         "failed": True, "http_status": r["http_status"]})
            continue
        ans = r["response"]["answers"]
        label = next(iter(ans))
        a = ans[label]
        k = key[r["item_id"]]
        row = {"item_id": r["item_id"], "question_set": r["question_set"],
               "latency_s": r["latency_s"], "cost": r["response"]["usage"]["cost"],
               "input_tokens": r["response"]["usage"]["input_tokens"]}
        if r["question_set"] == "FIELD":
            row.update(truth=k["field_key"], model=a["choice"],
                       confidence=a["confidence"], probabilities=a["probabilities"],
                       p_of_truth=a["probabilities"].get(k["field_key"]))
            row["correct"] = row["model"] == row["truth"]
        elif r["question_set"] == "CARDCOUNT":
            row.update(truth=k["multi_key"], model=a["choice"],
                       confidence=a["confidence"], probabilities=a["probabilities"],
                       p_of_truth=a["probabilities"].get(k["multi_key"]))
            row["correct"] = row["model"] == row["truth"]
        else:  # CERTAINTY, a score question
            probs = a["probabilities"]
            argmax_idx = max(probs, key=lambda i: probs[i])
            row.update(truth=k["confidence_key"],
                       model_argmax=int(argmax_idx) + 1,          # 0-based index -> 1..5
                       model_rounded=int(round(a["score"])) + 1,
                       raw_score=a["score"], confidence=a["confidence"],
                       probabilities=probs,
                       p_of_truth=probs.get(str(k["confidence_key"] - 1)))
            row["model"] = row["model_argmax"]
            row["correct"] = row["model_argmax"] == row["truth"]
            row["within_one"] = abs(row["model_argmax"] - row["truth"]) <= 1
            row["abs_error_argmax"] = abs(row["model_argmax"] - row["truth"])
            row["abs_error_rounded"] = abs(row["model_rounded"] - row["truth"])
        comp.append(row)

    comp_text = "\n".join(json.dumps(c, ensure_ascii=False, sort_keys=True) for c in comp) + "\n"
    comp_sha = write_append_only(CAL / "comparison.jsonl", comp_text)

    # ---- 3. per question set statistics --------------------------------------------
    out = {"script": "scripts/22_compare.py",
           "ordering_check": order_checks,
           "inputs": {"key_sha256": key_now,
                      "items_sha256": run_man["items_sha256"],
                      "responses_sha256": sha256_file(CAL / "responses.jsonl"),
                      "comparison_sha256": comp_sha},
           "question_sets": {}}

    for qs in ["FIELD", "CARDCOUNT", "CERTAINTY"]:
        sel = [c for c in comp if c["question_set"] == qs and not c.get("failed")]
        n = len(sel)
        ncorrect = sum(1 for c in sel if c["correct"])
        truth_counts = Counter(str(c["truth"]) for c in sel)
        majority = max(truth_counts.values()) / n
        cm = defaultdict(lambda: defaultdict(int))
        for c in sel:
            cm[str(c["truth"])][str(c["model"])] += 1
        wrong = [{"item_id": c["item_id"], "truth": c["truth"], "model": c["model"],
                  "confidence": c["confidence"], "p_of_truth": c["p_of_truth"]}
                 for c in sel if not c["correct"]]
        right_conf = sorted(c["confidence"] for c in sel if c["correct"])
        wrong_conf = sorted(c["confidence"] for c in sel if not c["correct"])

        def q(v, p):
            if not v:
                return None
            i = min(len(v) - 1, max(0, int(round(p * (len(v) - 1)))))
            return v[i]

        curve = []
        for t in GRID:
            acc = [c for c in sel if c["confidence"] >= t]
            esc = [c for c in sel if c["confidence"] < t]
            curve.append({
                "threshold": t,
                "accepted": len(acc),
                "accepted_share": round(len(acc) / n, 4),
                "accuracy_on_accepted": round(sum(1 for c in acc if c["correct"]) / len(acc), 4) if acc else None,
                "errors_accepted": sum(1 for c in acc if not c["correct"]),
                "escalated": len(esc),
                "accuracy_on_escalated": round(sum(1 for c in esc if c["correct"]) / len(esc), 4) if esc else None,
            })

        d = {
            "n": n,
            "agreement_with_key": round(ncorrect / n, 4),
            "n_correct": ncorrect,
            "n_wrong": n - ncorrect,
            "key_class_counts": dict(truth_counts),
            "baseline_always_majority_class": round(majority, 4),
            "baseline_uniform_guess": round(1 / len(truth_counts), 4),
            "confusion_matrix_truth_x_model": {k: dict(v) for k, v in cm.items()},
            "confidence_of_every_wrong_item": sorted(wrong, key=lambda w: w["confidence"]),
            "confidence_right": {
                "min": right_conf[0] if right_conf else None,
                "p10": q(right_conf, 0.10), "median": q(right_conf, 0.50),
                "p90": q(right_conf, 0.90),
                "max": right_conf[-1] if right_conf else None,
                "mean": round(sum(right_conf) / len(right_conf), 4) if right_conf else None,
            },
            "confidence_wrong": {
                "min": wrong_conf[0] if wrong_conf else None,
                "median": q(wrong_conf, 0.50),
                "max": wrong_conf[-1] if wrong_conf else None,
                "mean": round(sum(wrong_conf) / len(wrong_conf), 4) if wrong_conf else None,
            },
            "correct_but_low_confidence": {
                f"below_{t}": sum(1 for c in sel if c["correct"] and c["confidence"] < t)
                for t in [0.5, 0.7, 0.9, 0.95, 1.0]
            },
            "escalation_curve": curve,
            "latency_s": {
                "median": sorted(c["latency_s"] for c in sel)[n // 2],
                "max": max(c["latency_s"] for c in sel),
            },
            "cost_usd": round(sum(c["cost"] for c in sel), 8),
        }
        if qs == "CERTAINTY":
            d["exact_match_argmax"] = d["agreement_with_key"]
            d["exact_match_rounded_score"] = round(
                sum(1 for c in sel if c["model_rounded"] == c["truth"]) / n, 4)
            d["within_one_argmax"] = round(sum(1 for c in sel if c["within_one"]) / n, 4)
            d["mean_abs_error_argmax"] = round(
                sum(c["abs_error_argmax"] for c in sel) / n, 4)
            d["mean_abs_error_rounded"] = round(
                sum(c["abs_error_rounded"] for c in sel) / n, 4)
            d["baseline_always_4_exact"] = round(truth_counts.get("4", 0) / n, 4)
            d["baseline_always_4_within_one"] = round(
                sum(1 for c in sel if abs(4 - c["truth"]) <= 1) / n, 4)
        out["question_sets"][qs] = d

    # ---- 4. what the confidence number actually is ----------------------------------
    # Tested, not assumed: does confidence equal (top probability - second probability)?
    checks = {"binary_confidence_equals_top_minus_second": {"tested": 0, "matched": 0,
                                                            "max_abs_gap": 0.0},
              "score_equals_expected_index": {"tested": 0, "max_abs_gap": 0.0}}
    for c in comp:
        if c.get("failed"):
            continue
        p = sorted(c["probabilities"].values(), reverse=True)
        if len(p) == 2:
            checks["binary_confidence_equals_top_minus_second"]["tested"] += 1
            gap = abs(c["confidence"] - (p[0] - p[1]))
            checks["binary_confidence_equals_top_minus_second"]["max_abs_gap"] = max(
                checks["binary_confidence_equals_top_minus_second"]["max_abs_gap"], round(gap, 4))
            if gap <= 0.011:      # the probabilities come back rounded to 2 decimals
                checks["binary_confidence_equals_top_minus_second"]["matched"] += 1
        if c["question_set"] == "CERTAINTY":
            ev = sum(int(i) * v for i, v in c["probabilities"].items())
            checks["score_equals_expected_index"]["tested"] += 1
            checks["score_equals_expected_index"]["max_abs_gap"] = max(
                checks["score_equals_expected_index"]["max_abs_gap"],
                round(abs(ev - c["raw_score"]), 4))
    out["contract_identities_tested"] = checks

    # ---- 5. totals -------------------------------------------------------------------
    all_lat = sorted(c["latency_s"] for c in comp if not c.get("failed"))
    out["totals"] = {
        "calls": len(comp),
        "calls_failed": sum(1 for c in comp if c.get("failed")),
        "cost_usd_items_only": round(sum(c["cost"] for c in comp if not c.get("failed")), 8),
        "latency_s_median": all_lat[len(all_lat) // 2],
        "latency_s_max": all_lat[-1],
        "latency_s_min": all_lat[0],
        "latency_s_p90": all_lat[int(0.9 * (len(all_lat) - 1))],
    }
    out["unknowns"] = [
        "The FIELD key is the file a note was written in, not an adjudication of what "
        "the note is about. A watcher writing outside their own field of view produces "
        "a disagreement that this run cannot attribute to the model or to the key.",
        "The CERTAINTY key is one observer's self-rating. Its attainable ceiling is "
        "unknown and is not 100%.",
        "No second run of the same items was made, so the endpoint's run-to-run "
        "stability on these items is unmeasured; only two repeated probe calls were made.",
        "The confidence number's definition is not published. Only the identities "
        "reported under contract_identities_tested were checked.",
    ]

    txt = json.dumps(out, indent=2, ensure_ascii=False)
    sha = write_append_only(CAL / "ANALYSIS.json", txt)
    print(json.dumps({k: v for k, v in out.items() if k != "question_sets"}, indent=2))
    for qs, d in out["question_sets"].items():
        print(f"\n=== {qs} ===")
        print(json.dumps({k: v for k, v in d.items()
                          if k not in ("escalation_curve", "confidence_of_every_wrong_item")},
                         indent=2))
    print(f"\nANALYSIS.json sha256={sha}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
