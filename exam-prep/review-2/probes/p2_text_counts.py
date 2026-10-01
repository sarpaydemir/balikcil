#!/usr/bin/env python3
"""
p2_text_counts.py -- review-2 probe (R-04), own text parsing only.

What it does
  A. Release-name channel on the `strict-flags` blinded cards (JQ-R04-DATE b, c):
     cards printing a release name; distinct names; names whose cards all start
     on one calendar day (the second-fix T4 definition, by card start day); and
     the same count by RELEASE day (card start hour + printed offset), which is
     the day the name actually dates. Offsets / FOMC "no clock time" counts.
  B. K-1 (JQ-R04-CONTENT b): on the raw cards, for d = 2, 3, the number of
     cards on which rounding the rebased before-window close to d decimals
     makes two hours print the same value while the raw card printed two
     different values. Rebasing: close(h) / close(h-24) * 100.
  C. K-4: number of distinct values of "smallest non-zero step between printed
     close values" on the strict-flags and strict-flags-k1 sets.
  D. Card-number assignment: is B### -> C### the same in every blinded set,
     and is it reproduced by random.Random(20260913).shuffle over the C### order?
Input   cards/ ; exam-prep/blind-proof/*/ ; exam-prep/second-fix/blind-proof/strict-flags-k1/
Output  stdout
Rules   RULES 9 / TACTICS 6 (what is hidden). No threshold is defined here.
"""
import csv, glob, os, re, random, datetime as dt
from collections import defaultdict, Counter
from decimal import Decimal, ROUND_HALF_EVEN, ROUND_HALF_UP

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
BP = os.path.join(REPO, "exam-prep", "blind-proof")
K1 = os.path.join(REPO, "exam-prep", "second-fix", "blind-proof", "strict-flags-k1")

def truth(path):
    return {r["id"]: r for r in csv.DictReader(open(path, encoding="utf-8"))}

def before_table(text):
    sec = text.split("## Before", 1)[1].split("\n## ", 1)[0]
    lines = [l for l in sec.splitlines() if l.startswith("|")]
    head = [h.strip() for h in lines[0].strip("|").split("|")]
    rows = [[x.strip() for x in l.strip("|").split("|")] for l in lines[2:]]
    return head, rows

def main():
    # ---------------- A
    tr = truth(os.path.join(BP, "strict-flags", "truth-strict-flags.csv"))
    names_start, names_rel = defaultdict(set), defaultdict(set)
    cards_with, n_offset, n_nooffset, n_fomc = 0, 0, 0, 0
    card_names = {}
    for p in sorted(glob.glob(os.path.join(BP, "strict-flags", "cards", "B*.md"))):
        bid = os.path.basename(p)[:-3]
        t = open(p, encoding="utf-8").read()
        m = re.search(r"^- \*\*US releases:\*\* (.*)$", t, re.M)
        line = m.group(1).strip() if m else ""
        if "no clock time" in line:
            n_fomc += 1
        if not line or line.startswith("none in these hours"):
            card_names[bid] = []
            continue
        cards_with += 1
        if re.search(r"\([-+]\d+ h\)", line):
            n_offset += 1
        else:
            n_nooffset += 1
        start = dt.datetime.strptime(tr[bid]["start_hour_utc"], "%Y-%m-%dT%H:%MZ")
        nm_list = []
        for part in line.split(";"):
            part = part.strip()
            mo = re.search(r"\(([-+]\d+) h\)$", part)
            name = re.sub(r"\s*\((?:[-+]\d+ h|the calendar publishes no clock time)\)$", "", part)
            nm_list.append(name)
            names_start[name].add(start.date())
            if mo:
                names_rel[name].add((start + dt.timedelta(hours=int(mo.group(1)))).date())
            else:
                names_rel[name].add(("no-offset", start.date()))
        card_names[bid] = nm_list
    one_start = sorted(n for n, d in names_start.items() if len(d) == 1)
    one_rel = sorted(n for n, d in names_rel.items() if len(d) == 1)
    print("A. cards printing a release name:", cards_with, "of", len(card_names))
    print("   ... with at least one hour offset:", n_offset, "; without any:", n_nooffset,
          "; cards whose line says 'no clock time':", n_fomc)
    print("   distinct names:", len(names_start))
    print("   names on one START day:", len(one_start), "; cards carrying one:",
          sum(1 for v in card_names.values() if any(x in one_start for x in v)))
    for n in one_start:
        print("     -", n, sorted(str(d) for d in names_start[n]))
    print("   names on one RELEASE day (start + offset):", len(one_rel), "; cards carrying one:",
          sum(1 for v in card_names.values() if any(x in one_rel for x in v)))
    for n in one_rel:
        print("     -", n)
    print("   names in exactly one of the two lists:",
          sorted(set(one_start) ^ set(one_rel)))
    ats = [n for n in names_start if "Time Use" in n]
    for n in ats:
        print("   'Time Use' name:", n, "start days", sorted(str(d) for d in names_start[n]),
              "release days", sorted(str(d) for d in names_rel[n]))

    # ---------------- B
    print("\nB. K-1 manufactured ties (raw cards, before window)")
    raws = {}
    for p in sorted(glob.glob(os.path.join(REPO, "cards", "C*.md"))):
        head, rows = before_table(open(p, encoding="utf-8").read())
        ci = head.index("close")
        raws[os.path.basename(p)[:-3]] = [r[ci] for r in rows]
    for d in (2, 3):
        for mode, rnd in (("half-even", ROUND_HALF_EVEN), ("half-up", ROUND_HALF_UP)):
            bad = 0
            q = Decimal(1).scaleb(-d)
            for cid, vals in raws.items():
                base = Decimal(vals[0])
                pr = [(Decimal(v) / base * 100).quantize(q, rounding=rnd) for v in vals]
                hit = False
                for i in range(len(vals)):
                    for j in range(i + 1, len(vals)):
                        if pr[i] == pr[j] and Decimal(vals[i]) != Decimal(vals[j]):
                            hit = True
                bad += hit
            print("   d=%d (%s rounding): cards with a manufactured tie: %d" % (d, mode, bad))
    # python float formatting, which is what a script printing '%.*f' does
    for d in (2, 3):
        bad = 0
        for cid, vals in raws.items():
            base = float(vals[0])
            pr = ["%.*f" % (d, float(v) / base * 100) for v in vals]
            if any(pr[i] == pr[j] and float(vals[i]) != float(vals[j])
                   for i in range(24) for j in range(i + 1, 24)):
                bad += 1
        print("   d=%d (float %%-format): cards with a manufactured tie: %d" % (d, bad))

    # ---------------- C
    print("\nC. K-4 smallest non-zero step between printed close values")
    for label, d in (("strict-flags", os.path.join(BP, "strict-flags", "cards")),
                     ("strict-flags-k1", os.path.join(K1, "cards"))):
        vals = []
        for p in sorted(glob.glob(os.path.join(d, "B*.md"))):
            head, rows = before_table(open(p, encoding="utf-8").read())
            ci = head.index("close")
            xs = sorted({Decimal(r[ci]) for r in rows})
            steps = [b - a for a, b in zip(xs, xs[1:]) if b - a != 0]
            vals.append(min(steps) if steps else None)
        print("   %-16s distinct feature values: %d" % (label, len(set(vals))))

    # ---------------- D
    print("\nD. card-number assignment")
    maps = {}
    for v in ("ratio", "rank", "strict", "strict-flags"):
        maps[v] = {k: r["source_card"] for k, r in truth(os.path.join(BP, v, "truth-%s.csv" % v)).items()}
    maps["strict-flags-k1"] = {k: r["source_card"] for k, r in
                               truth(os.path.join(K1, "truth-strict-flags-k1.csv")).items()}
    ref = maps["strict-flags"]
    for v, m in maps.items():
        print("   %-16s same B->C mapping as strict-flags: %s" % (v, m == ref))
    cids = sorted(raws)
    rng = random.Random(20260913)
    order = list(range(len(cids))); rng.shuffle(order)
    derived = {"B%03d" % (i + 1): cids[s] for i, s in enumerate(order)}
    print("   mapping reproduced from the public seed and the C### order alone:", derived == ref)

if __name__ == "__main__":
    main()
