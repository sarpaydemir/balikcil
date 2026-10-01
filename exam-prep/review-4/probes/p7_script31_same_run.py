#!/usr/bin/env python3
"""p7 · review-4 · reproduce scripts/31_juror_file_check_fourth.py under its
stated run number 4b4d4795eb488c94 WITHOUT writing anything.
Script 31's run number hashes the path of script 30's record, so a re-run with
OUT_DIR moved gets a different number. Here the script's own source is
executed with its default OUT_DIR (exam-prep/fourth-fix/checks), with two
guards: (1) `open` and `os.makedirs` refuse any write; (2) the run number is
printed before the append-only check. If the run number is the stated one,
script 31's own guard compares the recomputed record with the stored one
and exits 0 ("already recorded") only if they are equal.
Reads: scripts/31_juror_file_check_fourth.py and its inputs. Writes nothing."""
import builtins, os, sys
ROOT = "/home/user/balikcil"
path = os.path.join(ROOT, "scripts/31_juror_file_check_fourth.py")
src = open(path, encoding="utf-8").read()
marker = '    failed = [c for c in checks if not c["found"]]\n'
assert src.count(marker) == 1
src = src.replace(marker, marker + '    print("RUN16", run16, "failed", len(failed))\n')
real_open = builtins.open
def guarded_open(f, mode="r", *a, **k):
    if any(x in mode for x in "wax+"):
        raise PermissionError("p7 refuses to write: %s" % f)
    return real_open(f, mode, *a, **k)
def guarded_makedirs(*a, **k):
    if not os.path.isdir(a[0]):
        raise PermissionError("p7 refuses to create: %s" % a[0])
builtins.open = guarded_open
os.makedirs = guarded_makedirs
sys.path.insert(0, os.path.join(ROOT, "scripts"))
g = {"__name__": "__main__", "__file__": path}
try:
    exec(compile(src, path, "exec"), g)
except SystemExit as e:
    print("exit code", e.code)
