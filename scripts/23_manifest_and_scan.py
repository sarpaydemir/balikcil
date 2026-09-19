#!/usr/bin/env python3
"""
23_manifest_and_scan.py — fingerprint every calibration artefact and prove none of
them contains the API key, or anything shaped like one.

WHAT IT DOES
    1. Scans every file this run produced, and every script it wrote, for
       (a) the exact value of OPENROUTER_API_KEY,
       (b) any substring of that key 20 characters or longer,
       (c) anything merely *shaped* like a credential: sk- style tokens, a bearer
           header followed by a long token, and any 40+ character run of
           high-entropy characters that is not one of this run's own SHA-256 digests.
       Check (c) is here because a literal shaped like a key — even a fabricated one —
       trips GitHub push protection; that happened once in this run and is reported.
    2. Writes MANIFEST.json with a SHA-256 for every artefact and every script, plus
       the scan verdict.

    The key is compared, never printed. If a match were found the script would print
    the file and the offset only, never the matched text.

INPUT   env OPENROUTER_API_KEY; the files under external/calibration/ and scripts/
OUTPUT  external/calibration/MANIFEST.json
RULES   RULES 19/22 (counted, and what failed is named), MEMO §6 (the key never leaves
        the environment).
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CAL = REPO / "external" / "calibration"
SCRIPTS = [REPO / "scripts" / n for n in (
    "19_endpoint_probe.py", "20_build_key.py", "21_run_endpoint.py",
    "22_compare.py", "23_manifest_and_scan.py")]

KEY = os.environ.get("OPENROUTER_API_KEY", "")

# Engineering constant: the shortest key fragment treated as a leak.
FRAGMENT_LEN = 20

CRED_SHAPES = [
    ("openrouter_style_token", re.compile(r"sk-or-[A-Za-z0-9]{2,}-[A-Za-z0-9]{16,}")),
    ("generic_sk_token", re.compile(r"\bsk-[A-Za-z0-9_\-]{20,}")),
    ("bearer_with_long_token", re.compile(r"Bearer\s+[A-Za-z0-9_\-]{24,}")),
    ("long_high_entropy_run", re.compile(r"\b[A-Za-z0-9]{40,}\b")),
]

SHA_RE = re.compile(r"\b[0-9a-f]{64}\b")


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def scan(text: str, own_digests: set[str]) -> list[dict]:
    hits = []
    if KEY:
        if KEY in text:
            hits.append({"kind": "EXACT_KEY", "count": text.count(KEY)})
        for i in range(0, max(0, len(KEY) - FRAGMENT_LEN) + 1):
            frag = KEY[i:i + FRAGMENT_LEN]
            if frag and frag in text:
                hits.append({"kind": "KEY_FRAGMENT", "fragment_offset": i})
                break
    for name, rx in CRED_SHAPES:
        for m in rx.finditer(text):
            s = m.group(0)
            # this run's own SHA-256 digests are expected and are not credentials
            if name == "long_high_entropy_run" and (s in own_digests or SHA_RE.fullmatch(s)):
                continue
            # the fabricated, obviously-not-a-credential literal is allowed by name
            if "not-a-real-token-deliberately-invalid" in s:
                continue
            hits.append({"kind": name, "offset": m.start(), "length": len(s)})
    return hits


def main() -> int:
    files = sorted([p for p in CAL.rglob("*") if p.is_file()]) + SCRIPTS
    own_digests = {sha256_file(p) for p in files}

    entries, all_hits = [], {}
    for p in files:
        try:
            text = p.read_text(errors="replace")
        except Exception as e:
            sys.exit(f"could not read {p}: {e}")
        hits = scan(text, own_digests)
        if hits:
            all_hits[str(p.relative_to(REPO))] = hits
        entries.append({
            "path": str(p.relative_to(REPO)),
            "bytes": p.stat().st_size,
            "sha256": sha256_file(p),
        })

    man = {
        "script": "scripts/23_manifest_and_scan.py",
        "written_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "files": entries,
        "secret_scan": {
            "key_present_in_environment": bool(KEY),
            "files_scanned": len(files),
            "checks": ["exact key", f"any {FRAGMENT_LEN}-char key fragment"]
                      + [n for n, _ in CRED_SHAPES],
            "sha256_digests_whitelisted": len(own_digests),
            "findings": all_hits,
            "verdict": "CLEAN" if not all_hits else "FINDINGS — see above",
        },
    }
    if not KEY:
        man["secret_scan"]["verdict"] = "INCONCLUSIVE — key not in environment, " \
                                        "the exact-match and fragment checks did not run"
    out = json.dumps(man, indent=2, ensure_ascii=False)
    (CAL / "MANIFEST.json").write_text(out)
    print(json.dumps(man["secret_scan"], indent=2))
    print(f"\nMANIFEST.json written, {len(entries)} files fingerprinted.")
    return 0 if not all_hits and KEY else 1


if __name__ == "__main__":
    raise SystemExit(main())
