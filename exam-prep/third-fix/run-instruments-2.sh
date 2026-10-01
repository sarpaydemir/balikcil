#!/bin/bash
# third-fix run · second batch: every audit again with the final third-fix
# audit script (K-11, the T3 suffix fix), plus the residual diagnostic.
# Append-only by run number; re-running resumes.
# Reads : cards/, exam-prep/blind-proof/, exam-prep/second-fix/blind-proof/,
#         exam-prep/third-fix/blind-proof/
# Writes: exam-prep/third-fix/identity/
set -u
export PYTHONDONTWRITEBYTECODE=1
cd /home/user/balikcil
O=exam-prep/third-fix/identity
date -u +"start %Y-%m-%dT%H:%M:%SZ"
df -B1 --output=avail . | tail -1 | sed 's/^/free bytes /'
sha256sum scripts/16_identity_audit.py
python3 scripts/16_identity_audit.py --out $O --label raw-observation
for v in strict-flags ratio rank strict; do
  python3 scripts/16_identity_audit.py --cards exam-prep/blind-proof/$v/cards \
    --truth exam-prep/blind-proof/$v/truth-$v.csv --out $O --label blinded-$v
  date -u +"audit $v done %Y-%m-%dT%H:%M:%SZ"
done
K=exam-prep/second-fix/blind-proof/strict-flags-k1
python3 scripts/16_identity_audit.py --cards $K/cards \
  --truth $K/truth-strict-flags-k1.csv --out $O --label blinded-strict-flags-k1
U=exam-prep/third-fix/blind-proof/strict-flags-unrounded
python3 scripts/16_identity_audit.py --cards $U/cards \
  --truth $U/truth-strict-flags-unrounded.csv --out $O \
  --label blinded-strict-flags-unrounded
date -u +"audits done %Y-%m-%dT%H:%M:%SZ"
python3 scripts/18_residual_diagnostic.py --cards exam-prep/blind-proof/strict-flags/cards \
  --truth exam-prep/blind-proof/strict-flags/truth-strict-flags.csv --out $O --label blinded-strict-flags
python3 scripts/18_residual_diagnostic.py --cards $K/cards \
  --truth $K/truth-strict-flags-k1.csv --out $O --label blinded-strict-flags-k1
python3 scripts/18_residual_diagnostic.py --cards $U/cards \
  --truth $U/truth-strict-flags-unrounded.csv --out $O --label blinded-strict-flags-unrounded
date -u +"end %Y-%m-%dT%H:%M:%SZ"
