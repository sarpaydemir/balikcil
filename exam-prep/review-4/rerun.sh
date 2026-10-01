#!/bin/bash
# review-4 · re-run every script the fourth-fix run changed or added, under
# the run numbers it states, into exam-prep/review-4/rerun/ (append-only by
# run number). Scripts 30 and 31 have no --out: they are imported and their
# OUT_DIR is pointed at exam-prep/review-4/rerun/checks/.
# Reads : cards/, exam-prep/ (blind-proof sets, probes, fourth-fix runs), scripts/
# Writes: exam-prep/review-4/rerun/
set -u
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=/home/user/balikcil/scripts
cd /home/user/balikcil
R=exam-prep/review-4/rerun
date -u +"start %Y-%m-%dT%H:%M:%SZ"
df -B1 --output=avail . | tail -1 | sed 's/^/free bytes /'
sha256sum scripts/15_event_collapse.py scripts/29_identity_audit_exact.py scripts/30_fourth_fix_checks.py scripts/31_juror_file_check_fourth.py scripts/lab_cards.py
python3 scripts/15_event_collapse.py --out $R/collapse
date -u +"collapse done %Y-%m-%dT%H:%M:%SZ"
O=$R/identity
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
date -u +"audits done %Y-%m-%dT%H:%M:%SZ"
python3 - <<'PY'
import importlib.util, os
spec = importlib.util.spec_from_file_location("s30", "scripts/30_fourth_fix_checks.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
m.OUT_DIR = os.path.abspath("exam-prep/review-4/rerun/checks")
m.main()
PY
date -u +"30 done %Y-%m-%dT%H:%M:%SZ"
python3 - <<'PY'
import importlib.util, os
spec = importlib.util.spec_from_file_location("s31", "scripts/31_juror_file_check_fourth.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
m.OUT_DIR = os.path.abspath("exam-prep/review-4/rerun/checks")
m.main()
PY
date -u +"end %Y-%m-%dT%H:%M:%SZ"
