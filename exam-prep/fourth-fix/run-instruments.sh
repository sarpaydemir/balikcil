#!/bin/bash
# fourth-fix run · the changed engine (scripts/15, K-14/K-15) on the
# observation cards, and the exact audit (scripts/29, K-13) on all seven card
# sets. Append-only by run number; re-running resumes (a recorded run writes
# nothing).
# Reads : cards/, exam-prep/blind-proof/, exam-prep/second-fix/blind-proof/,
#         exam-prep/third-fix/blind-proof/, scripts/
# Writes: exam-prep/fourth-fix/collapse/, exam-prep/fourth-fix/identity/
set -u
export PYTHONDONTWRITEBYTECODE=1
cd /home/user/balikcil
date -u +"start %Y-%m-%dT%H:%M:%SZ"
df -B1 --output=avail . | tail -1 | sed 's/^/free bytes /'
sha256sum scripts/15_event_collapse.py scripts/29_identity_audit_exact.py scripts/lab_cards.py
python3 scripts/15_event_collapse.py --out exam-prep/fourth-fix/collapse
date -u +"collapse done %Y-%m-%dT%H:%M:%SZ"
O=exam-prep/fourth-fix/identity
python3 scripts/29_identity_audit_exact.py --out $O --label raw-observation
date -u +"audit raw done %Y-%m-%dT%H:%M:%SZ"
for v in strict-flags ratio rank strict; do
  python3 scripts/29_identity_audit_exact.py --cards exam-prep/blind-proof/$v/cards \
    --truth exam-prep/blind-proof/$v/truth-$v.csv --out $O --label blinded-$v
  date -u +"audit $v done %Y-%m-%dT%H:%M:%SZ"
done
K=exam-prep/second-fix/blind-proof/strict-flags-k1
python3 scripts/29_identity_audit_exact.py --cards $K/cards \
  --truth $K/truth-strict-flags-k1.csv --out $O --label blinded-strict-flags-k1
date -u +"audit k1 done %Y-%m-%dT%H:%M:%SZ"
U=exam-prep/third-fix/blind-proof/strict-flags-unrounded
python3 scripts/29_identity_audit_exact.py --cards $U/cards \
  --truth $U/truth-strict-flags-unrounded.csv --out $O \
  --label blinded-strict-flags-unrounded
date -u +"end %Y-%m-%dT%H:%M:%SZ"
