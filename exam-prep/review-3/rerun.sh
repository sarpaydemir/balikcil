#!/bin/bash
# review-3 · re-run of every third-fix instrument run, into review-3's own
# directory (never into another run's directory). Each script is append-only by
# run number, so an interrupted batch resumes by running this file again.
# Reads : cards/, data/ (overlap, draw, moments, observation caches via 17),
#         canteen/2026-09-19-sofia.md (via 26), exam-prep/ (blind-proof sets,
#         collapse, second-fix, third-fix, review-2 probes - read only).
# Writes: exam-prep/review-3/rerun/ only. No bytecode caches.
set -u
export PYTHONDONTWRITEBYTECODE=1
cd /home/user/balikcil
R=exam-prep/review-3/rerun
mkdir -p $R
date -u +"start %Y-%m-%dT%H:%M:%SZ"
df -B1 --output=avail . | tail -1 | sed 's/^/free bytes /'
sha256sum scripts/15_event_collapse.py scripts/16_identity_audit.py scripts/17_blind_cards.py \
  scripts/18_residual_diagnostic.py scripts/26_third_fix_checks.py scripts/27_gate_sensitivity.py \
  scripts/28_juror_file_check.py scripts/lab_cards.py
# 1 collapse engine
python3 scripts/15_event_collapse.py --out $R/collapse
date -u +"collapse done %Y-%m-%dT%H:%M:%SZ"
# 2 blinding: the K-10 set, and the four default sets plus K-1 (claim: reproduced byte for byte)
B="--levels rank --btceth drop --funding flags --takerbuy rank --p7 no-scale"
python3 scripts/17_blind_cards.py --out $R/blind/strict-flags-unrounded --label strict-flags-unrounded $B --rank-source unrounded
python3 scripts/17_blind_cards.py --out $R/blind/strict-flags --label strict-flags $B
python3 scripts/17_blind_cards.py --out $R/blind/strict --label strict --levels rank --btceth drop --funding summary --takerbuy rank --p7 no-scale
python3 scripts/17_blind_cards.py --out $R/blind/rank --label rank --levels rank --btceth drop --funding summary --takerbuy centred
python3 scripts/17_blind_cards.py --out $R/blind/ratio --label ratio --levels ratio --btceth drop --funding summary --takerbuy centred
python3 scripts/17_blind_cards.py --out $R/blind/strict-flags-k1 --label strict-flags-k1 $B --close-dp no-new-ties
date -u +"blinding done %Y-%m-%dT%H:%M:%SZ"
# 3 audits on the sets as the third run audited them
O=$R/identity
python3 scripts/16_identity_audit.py --out $O --label raw-observation
for v in strict-flags ratio rank strict; do
  python3 scripts/16_identity_audit.py --cards exam-prep/blind-proof/$v/cards \
    --truth exam-prep/blind-proof/$v/truth-$v.csv --out $O --label blinded-$v
  date -u +"audit $v done %Y-%m-%dT%H:%M:%SZ"
done
K=exam-prep/second-fix/blind-proof/strict-flags-k1
python3 scripts/16_identity_audit.py --cards $K/cards --truth $K/truth-strict-flags-k1.csv --out $O --label blinded-strict-flags-k1
U=exam-prep/third-fix/blind-proof/strict-flags-unrounded
python3 scripts/16_identity_audit.py --cards $U/cards --truth $U/truth-strict-flags-unrounded.csv --out $O --label blinded-strict-flags-unrounded
date -u +"audits done %Y-%m-%dT%H:%M:%SZ"
python3 scripts/18_residual_diagnostic.py --cards exam-prep/blind-proof/strict-flags/cards \
  --truth exam-prep/blind-proof/strict-flags/truth-strict-flags.csv --out $O --label blinded-strict-flags
python3 scripts/18_residual_diagnostic.py --cards $K/cards --truth $K/truth-strict-flags-k1.csv --out $O --label blinded-strict-flags-k1
python3 scripts/18_residual_diagnostic.py --cards $U/cards --truth $U/truth-strict-flags-unrounded.csv --out $O --label blinded-strict-flags-unrounded
date -u +"residual done %Y-%m-%dT%H:%M:%SZ"
# 4 checks 26, 27, 28 by import with OUT_DIR redirected (they have no --out).
#   28 reads OUT_DIR/runs for the G-2 record: it therefore reads review-3's own re-run of 26.
for s in 26_third_fix_checks 28_juror_file_check; do
python3 - "$s" "$R/checks" <<'PY'
import importlib.util, os, sys
name, out = sys.argv[1], os.path.abspath(sys.argv[2])
spec = importlib.util.spec_from_file_location(name, os.path.join("scripts", name + ".py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
m.OUT_DIR = out
sys.argv = [name]
m.main()
PY
done
python3 - "$R/checks" <<'PY'
import importlib.util, os, sys
out = os.path.abspath(sys.argv[1])
spec = importlib.util.spec_from_file_location("g27", "scripts/27_gate_sensitivity.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
m.OUT_DIR = out
U = "exam-prep/third-fix/blind-proof/strict-flags-unrounded"
sys.argv = ["27", "--cards", U + "/cards", "--truth", U + "/truth-strict-flags-unrounded.csv",
            "--label", "blinded-strict-flags-unrounded"]
m.main()
PY
date -u +"end %Y-%m-%dT%H:%M:%SZ"
# Added after the 2026-10-01T20:47Z run: script 28 failed on import there
# ("No module named 'lab_cards'": an imported spec does not put scripts/ on
# sys.path). The block below re-runs 28 alone with scripts/ on the path; it is
# the record review-3 uses for 28.
python3 - "$R/checks" <<'PY'
import importlib.util, os, sys
sys.path.insert(0, os.path.abspath("scripts"))
out = os.path.abspath(sys.argv[1])
spec = importlib.util.spec_from_file_location("jfc28", "scripts/28_juror_file_check.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
m.OUT_DIR = out
sys.argv = ["28"]
m.main()
PY
date -u +"28 done %Y-%m-%dT%H:%M:%SZ"
