#!/bin/bash
# review-2 · re-run of every second-fix instrument run, into review-2's own
# directory (never into another run's directory). Each script is append-only by
# run number, so an interrupted batch resumes by running this file again.
# Reads: cards/, exam-prep/blind-proof/, exam-prep/second-fix/blind-proof/,
#        exam-prep/collapse/, exam-prep/identity/, git objects of this repo.
# Writes: exam-prep/review-2/rerun/ only.
set -u
# Added after the 2026-10-01T19:38Z run: that run let Python write two
# bytecode caches into scripts/__pycache__/ (24_ and 25_), which review-2 then
# deleted; this line keeps a re-run from writing outside exam-prep/review-2/.
export PYTHONDONTWRITEBYTECODE=1
cd /home/user/balikcil
R=exam-prep/review-2/rerun
date -u +"start %Y-%m-%dT%H:%M:%SZ"
df -B1 --output=avail . | tail -1 | sed 's/^/free bytes /'
python3 scripts/15_event_collapse.py --out $R/collapse
python3 scripts/17_blind_cards.py --out $R/blind-k1 --label strict-flags-k1 \
  --levels rank --btceth drop --funding flags --takerbuy rank --p7 no-scale \
  --close-dp no-new-ties
python3 scripts/16_identity_audit.py --out $R/identity --label raw-observation
for v in ratio rank strict strict-flags; do
  python3 scripts/16_identity_audit.py --cards exam-prep/blind-proof/$v/cards \
    --truth exam-prep/blind-proof/$v/truth-$v.csv --out $R/identity --label blinded-$v
done
python3 scripts/16_identity_audit.py \
  --cards exam-prep/second-fix/blind-proof/strict-flags-k1/cards \
  --truth exam-prep/second-fix/blind-proof/strict-flags-k1/truth-strict-flags-k1.csv \
  --out $R/identity --label blinded-strict-flags-k1
python3 scripts/18_residual_diagnostic.py --cards exam-prep/blind-proof/strict-flags/cards \
  --truth exam-prep/blind-proof/strict-flags/truth-strict-flags.csv --out $R/identity --label blinded-strict-flags
python3 scripts/18_residual_diagnostic.py \
  --cards exam-prep/second-fix/blind-proof/strict-flags-k1/cards \
  --truth exam-prep/second-fix/blind-proof/strict-flags-k1/truth-strict-flags-k1.csv \
  --out $R/identity --label blinded-strict-flags-k1
for s in 24_review_checks 25_instrument_checks; do
python3 - "$s" "$R/checks" <<'PY'
import importlib.util, os, sys
name, out = sys.argv[1], os.path.abspath(sys.argv[2])
spec = importlib.util.spec_from_file_location(name, os.path.join("scripts", name + ".py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
m.OUT_DIR = out          # redirect: never write into exam-prep/second-fix/checks
m.main()
PY
done
date -u +"end %Y-%m-%dT%H:%M:%SZ"
