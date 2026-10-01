#!/bin/bash
# third-fix run · re-runs the changed instruments (15, 16, and 18 through 16)
# into exam-prep/ only. Every script is append-only by run number, so an
# interrupted batch resumes by running this file again; a run already recorded
# with identical results writes nothing.
# Reads : cards/, exam-prep/blind-proof/, exam-prep/second-fix/blind-proof/
# Writes: exam-prep/collapse/ (new run directory and run record only),
#         exam-prep/third-fix/identity/
# No bytecode caches are written (PYTHONDONTWRITEBYTECODE).
set -u
export PYTHONDONTWRITEBYTECODE=1
cd /home/user/balikcil
O=exam-prep/third-fix/identity
date -u +"start %Y-%m-%dT%H:%M:%SZ"
df -B1 --output=avail . | tail -1 | sed 's/^/free bytes /'
python3 scripts/15_event_collapse.py --out exam-prep/collapse
date -u +"collapse done %Y-%m-%dT%H:%M:%SZ"
python3 scripts/16_identity_audit.py --out $O --label raw-observation
for v in strict-flags ratio rank strict; do
  python3 scripts/16_identity_audit.py --cards exam-prep/blind-proof/$v/cards \
    --truth exam-prep/blind-proof/$v/truth-$v.csv --out $O --label blinded-$v
  date -u +"audit $v done %Y-%m-%dT%H:%M:%SZ"
done
python3 scripts/16_identity_audit.py \
  --cards exam-prep/second-fix/blind-proof/strict-flags-k1/cards \
  --truth exam-prep/second-fix/blind-proof/strict-flags-k1/truth-strict-flags-k1.csv \
  --out $O --label blinded-strict-flags-k1
python3 scripts/18_residual_diagnostic.py --cards exam-prep/blind-proof/strict-flags/cards \
  --truth exam-prep/blind-proof/strict-flags/truth-strict-flags.csv --out $O --label blinded-strict-flags
python3 scripts/18_residual_diagnostic.py \
  --cards exam-prep/second-fix/blind-proof/strict-flags-k1/cards \
  --truth exam-prep/second-fix/blind-proof/strict-flags-k1/truth-strict-flags-k1.csv \
  --out $O --label blinded-strict-flags-k1
date -u +"end %Y-%m-%dT%H:%M:%SZ"
