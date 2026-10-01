#!/bin/bash
# Runs the extended identity audit (scripts/16_identity_audit.py, second-fix
# version) on the raw observation cards and on every blinded set, then the
# residual diagnostic on the two strict-flags sets. Each run is its own
# append-only record, so an interrupted batch resumes by re-running this file:
# a set already recorded is skipped by the script itself.
set -u
cd /home/user/balikcil
O=exam-prep/second-fix/identity
date -u +"start %Y-%m-%dT%H:%M:%SZ"
python3 scripts/16_identity_audit.py --out $O --label raw-observation
for v in ratio rank strict strict-flags; do
  python3 scripts/16_identity_audit.py --cards exam-prep/blind-proof/$v/cards \
    --truth exam-prep/blind-proof/$v/truth-$v.csv --out $O --label blinded-$v
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
