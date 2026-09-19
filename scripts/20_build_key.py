#!/usr/bin/env python3
"""
20_build_key.py — build the calibration item set and its answer key, before any
model sees an item.

WHAT IT DOES
    1. Selects 100 watcher-note lines from notes/ by a deterministic, published rule.
    2. Writes the items (text only, no labels) and the key (labels only, no text) into
       two separate files, so that the script which calls the endpoint physically
       cannot read a label.
    3. Writes a manifest carrying the SHA-256 of both files, the selection rule and
       the seed.
    4. Notarises the key's digest at the endpoint: it posts the digest — and nothing
       else — and records the response id and the provider's own timestamp. That gives
       an outside, independently issued time anchor showing the key existed before the
       first item call. It is an anchor, not a trusted timestamping authority.

INPUT
    notes/2026-09-19-{amara,ingrid,kenji,lukas}-v2-batch{01..09}.md  (36 files)
    TEAM.md — the four fields of view, quoted for the criteria text
    env OPENROUTER_API_KEY (for the notarisation call only)

OUTPUT
    external/calibration/items.jsonl        — id, source, text. NO labels.
    external/calibration/key.jsonl          — id, labels. NO text.
    external/calibration/KEY-MANIFEST.json  — digests, seed, rule, notarisation

RULES IT IMPLEMENTS
    MEMO §4 step 2 — the key is written down before the model's answers are looked at.
    RULES 23 — the clock is read from the system, and a second clock from the endpoint.
    RULES 29/30 — deterministic from its input; refuses to overwrite with new content.
    RULES 19 — every number written here is counted, not estimated.

WHAT THIS SCRIPT DOES NOT DO
    It does not interpret a note and it does not label anything by judgement. Both
    labels are read off the source: the field-of-view label is the file the line came
    from, and the self-rating is the digit the watcher wrote at the end of the line.
"""

from __future__ import annotations

import hashlib
import json
import os
import random
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

# ---------------------------------------------------------------------------
# Constants — each with its source.
# ---------------------------------------------------------------------------

# Engineering constant set by this script and written down here: the sampling seed.
SEED = 20260919

# Engineering constant: how many items, and how many per author.
# MEMO §4 step 1 says "~100 items"; four authors divide it evenly.
N_TOTAL = 100
N_PER_AUTHOR = 25

# Source: TEAM.md, the four watcher entries. The label is the author's file, and the
# text beside it is quoted from TEAM.md so no wording here is invented.
FIELD_OF_VIEW = {
    "ingrid": ("EXCHANGE_BEHAVIOUR",
               "changes in the funding rate and the payment interval; listing, delisting "
               "and warning announcements; every administrative decision the exchange takes"),
    "kenji": ("CROWD",
              "open interest, long/short ratios, the ratio of large players, taker "
              "buy/sell pressure, the funding rate itself"),
    "amara": ("OUTSIDE_WORLD",
              "Binance and Korean exchange announcements, the US release calendar, the "
              "number of people viewing the page on Wikipedia, the prediction market, the "
              "state of bitcoin and ethereum over those hours"),
    "lukas": ("PRICE_ITSELF",
              "price, volume, trade count, order book depth, volatility"),
}

# Names that must not appear inside an item, because they would hand the model the
# field-of-view label directly.
NAME_LEAK = re.compile(r"ingrid|kenji|amara|lukas|sofia|viktor|nadia|hana|tom[aá]s|greta|derya|mateo",
                       re.IGNORECASE)

CARD_RE = re.compile(r"\bC\d{3}\b")

ENDPOINT = "https://openrouter.ai/api/alpha/decisions"          # memo §3
MODEL = os.environ.get("DECISION_MODEL", "").strip() or "typesafe/jev-1.13"
KEY = os.environ.get("OPENROUTER_API_KEY", "")
TIMEOUT_S = 60

REPO = Path(__file__).resolve().parent.parent
NOTES = REPO / "notes"
OUT = REPO / "external" / "calibration"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def qualifies(line: str) -> bool:
    """The published selection rule for a note line.

    A line qualifies when all of the following hold:
      (a) it is not a heading and not blank;
      (b) it cites at least one card number of the form C###;
      (c) it is written in the note format of TACTICS §4,
          `card no · what I saw · why I think so · how sure I am (1-5)`:
          at least three ' · '-separated fields, the last of which is a single
          digit 1-5;
      (d) it contains no laboratory member's name, which would give the
          field-of-view label away.
    """
    s = line.strip()
    if not s or s.startswith("#") or s.startswith(">"):
        return False
    if not CARD_RE.search(s):
        return False
    parts = [p.strip() for p in s.split("·")]
    if len(parts) < 3:
        return False
    if not re.fullmatch(r"[1-5]", parts[-1]):
        return False
    if NAME_LEAK.search(s):
        return False
    return True


def strip_confidence(line: str) -> str:
    """Remove the trailing ' · <digit>' so the score question cannot read its own key."""
    parts = line.split("·")
    return "·".join(parts[:-1]).strip()


def collect() -> dict[str, list[dict]]:
    by_author: dict[str, list[dict]] = {a: [] for a in FIELD_OF_VIEW}
    for author in sorted(FIELD_OF_VIEW):
        for batch in range(1, 10):
            f = NOTES / f"2026-09-19-{author}-v2-batch{batch:02d}.md"
            if not f.exists():
                sys.exit(f"expected source file missing: {f}")
            for lineno, raw in enumerate(f.read_text().splitlines(), start=1):
                if qualifies(raw):
                    s = raw.strip().lstrip("- ").strip()
                    by_author[author].append(
                        {"source_file": str(f.relative_to(REPO)), "source_line": lineno, "text": s}
                    )
    return by_author


def write_append_only(path: Path, content: str) -> str:
    digest = hashlib.sha256(content.encode()).hexdigest()
    if path.exists():
        old = path.read_text()
        if old != content:
            sys.exit(f"REFUSING to overwrite {path} with different content (RULES 30).")
        return digest
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    return digest


def notarise(key_digest: str) -> dict:
    """Post the key's digest, and only the digest, to get an outside time anchor."""
    body = {
        "model": MODEL,
        "state": f"sha256:{key_digest}",
        "questions": {
            "is_hex": {
                "type": "choice",
                "instructions": "Is this string a 64-character hexadecimal digest?",
                "criteria": {"YES": "it is 64 hex characters", "NO": "it is not"},
            }
        },
    }
    t0 = time.perf_counter()
    r = requests.post(ENDPOINT, headers={"Authorization": f"Bearer {KEY}",
                                         "Content-Type": "application/json"},
                      json=body, timeout=TIMEOUT_S)
    lat = round(time.perf_counter() - t0, 4)
    rec = {"posted": f"sha256:{key_digest}", "http_status": r.status_code, "latency_s": lat,
           "local_clock_utc": now_iso()}
    try:
        j = r.json()
        rec["response"] = j
        gid = j.get("id", "")
        m = re.match(r"gen-dec-(\d+)-", gid)
        if m:
            rec["provider_unix_time"] = int(m.group(1))
            rec["provider_time_utc"] = datetime.fromtimestamp(
                int(m.group(1)), timezone.utc).isoformat(timespec="seconds")
    except Exception as e:
        rec["error"] = f"{type(e).__name__}: {e}"
        rec["response_text"] = r.text[:2000]
    return rec


def main() -> int:
    if not KEY:
        sys.exit("OPENROUTER_API_KEY is not in the environment.")
    OUT.mkdir(parents=True, exist_ok=True)

    by_author = collect()
    counts = {a: len(v) for a, v in by_author.items()}
    print("qualifying lines per author:", counts)
    for a, n in counts.items():
        if n < N_PER_AUTHOR:
            sys.exit(f"author {a} has only {n} qualifying lines, fewer than {N_PER_AUTHOR}")

    rng = random.Random(SEED)
    drawn = []
    for author in sorted(FIELD_OF_VIEW):           # deterministic author order
        pool = by_author[author]                   # already in (file, line) order
        chosen = sorted(rng.sample(range(len(pool)), N_PER_AUTHOR))
        for j in chosen:
            drawn.append((author, pool[j]))

    # Interleave the four authors before assigning ids, so that neither the id order
    # nor the row order of items.jsonl groups the items by their field-of-view label.
    rng2 = random.Random(SEED + 1)
    rng2.shuffle(drawn)

    items, keyrows = [], []
    for idx, (author, rec) in enumerate(drawn, start=1):
        iid = f"I{idx:03d}"
        conf = int(rec["text"].split("·")[-1].strip())
        cards = sorted(set(CARD_RE.findall(rec["text"])))
        # items.jsonl holds the id and the text and nothing else: no author, no file,
        # no label, nothing from which a label could be reconstructed.
        items.append({
            "id": iid,
            "text_full": rec["text"],
            "text_no_confidence": strip_confidence(rec["text"]),
        })
        # provenance lives with the key, which is the file an auditor rebuilds from.
        keyrows.append({
            "id": iid,
            "source_file": rec["source_file"],
            "source_line": rec["source_line"],
            "field_key": FIELD_OF_VIEW[author][0],
            "field_key_basis": "the file the line was taken from",
            "multi_key": "MULTI" if len(cards) > 1 else "SINGLE",
            "multi_key_basis": f"{len(cards)} distinct C### numbers on the line",
            "confidence_key": conf,
            "confidence_key_basis": "the digit the watcher wrote as the last field",
        })

    items_text = "\n".join(json.dumps(r, ensure_ascii=False, sort_keys=True) for r in items) + "\n"
    key_text = "\n".join(json.dumps(r, ensure_ascii=False, sort_keys=True)
                         for r in sorted(keyrows, key=lambda r: r["id"])) + "\n"

    items_sha = write_append_only(OUT / "items.jsonl", items_text)
    key_sha = write_append_only(OUT / "key.jsonl", key_text)

    dist = {}
    for r in keyrows:
        dist.setdefault("field", {}).setdefault(r["field_key"], 0)
        dist["field"][r["field_key"]] += 1
        dist.setdefault("multi", {}).setdefault(r["multi_key"], 0)
        dist["multi"][r["multi_key"]] += 1
        dist.setdefault("confidence", {}).setdefault(str(r["confidence_key"]), 0)
        dist["confidence"][str(r["confidence_key"])] += 1

    manifest = {
        "script": "scripts/20_build_key.py",
        "built_utc": now_iso(),
        "seed": SEED,
        "n_items": len(items),
        "n_per_author": N_PER_AUTHOR,
        "sources": sorted({r["source_file"] for r in keyrows}),
        "selection_rule": qualifies.__doc__,
        "qualifying_pool_per_author": counts,
        "label_bases": {
            "field_key": "the watcher file the line came from; TEAM.md defines the four "
                         "fields of view and the criteria text is quoted from it",
            "multi_key": "regex count of distinct C### numbers on the line",
            "confidence_key": "the 1-5 digit the watcher wrote as the last field; it is "
                              "removed from text_no_confidence before that item is sent",
        },
        "key_distribution": dist,
        "items_sha256": items_sha,
        "key_sha256": key_sha,
        "note": "items.jsonl carries the id and the text only — no author, no source "
                "file, no label. key.jsonl carries the labels and the provenance. "
                "The run script reads items.jsonl only.",
    }
    manifest["notarisation"] = notarise(key_sha)

    man_text = json.dumps(manifest, indent=2, ensure_ascii=False)
    man_sha = write_append_only(OUT / "KEY-MANIFEST.json", man_text)

    print(f"items.jsonl        sha256={items_sha}")
    print(f"key.jsonl          sha256={key_sha}")
    print(f"KEY-MANIFEST.json  sha256={man_sha}")
    print("key distribution:", json.dumps(dist))
    print("notarised at provider time:", manifest["notarisation"].get("provider_time_utc"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
