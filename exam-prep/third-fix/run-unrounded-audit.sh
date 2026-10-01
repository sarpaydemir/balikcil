#!/bin/bash
# third-fix run · K-10: audit the unrounded-rank blinded set with the third-fix
# audit, and the residual diagnostic. Append-only; re-running resumes.
# Reads : exam-prep/third-fix/blind-proof/strict-flags-unrounded/
# Writes: exam-prep/third-fix/identity/
set -u
export PYTHONDONTWRITEBYTECODE=1
cd /home/user/balikcil
S=exam-prep/third-fix/blind-proof/strict-flags-unrounded
date -u +"start %Y-%m-%dT%H:%M:%SZ"
python3 scripts/16_identity_audit.py --cards $S/cards \
  --truth $S/truth-strict-flags-unrounded.csv \
  --out exam-prep/third-fix/identity --label blinded-strict-flags-unrounded
python3 scripts/18_residual_diagnostic.py --cards $S/cards \
  --truth $S/truth-strict-flags-unrounded.csv \
  --out exam-prep/third-fix/identity --label blinded-strict-flags-unrounded
date -u +"end %Y-%m-%dT%H:%M:%SZ"
