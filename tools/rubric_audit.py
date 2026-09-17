#!/usr/bin/env python3
"""
rubric_audit.py -- deterministic self-audit for a Sardine Refiner task worksheet.

Reads the FINAL RUBRIC markdown table (section 8 of TaskWorksheet_Template.md) and,
optionally, the three comparison rating tables (section 4), then reports:

  - criteria count vs QC Dim 3 (25-100) and the course floor (30)
  - weight validity and band sanity (Dim 4)
  - category validity (six approved categories)
  - atomicity heuristics: "and", lists, slashes (Dim 9)
  - vague words and AI filler (Dim 10, Dim 17)
  - negative criteria phrased as avoidance (pass-semantics trap, Dim 12)
  - near-duplicate criteria by token overlap (Dim 6)
  - missing sources, missing or copy-pasted justifications (Dim 13)
  - RD anomalies: RD fails a positive or passes a negative (Dim 15 hints)
  - score model: P, score and percent for RD / AD1 / AD2; RD >= 95 (Dim 15)
  - alignment of totals with the 1-7 ratings (Dim 14)

Usage:
  python tools/rubric_audit.py Tasks/<task-id>.md
  python tools/rubric_audit.py Tasks/<task-id>.md --pref-rd-ad1 3.0 --pref-rd-ad2 4.4 --pref-ad1-ad2 5.2
  python tools/rubric_audit.py Tasks/<task-id>.md --min-count 30 --dup-threshold 0.6

Exit code 1 if any FAIL line is printed, else 0. Pure standard library.
"""

import argparse
import re
import sys
from itertools import combinations

APPROVED_CATEGORIES = {
    "requirements compliance": "Requirements Compliance",
    "presentation and aesthetics": "Presentation & Aesthetics",
    "presentation & aesthetics": "Presentation & Aesthetics",
    "functionality": "Functionality",
    "content correctness": "Content Correctness",
    "usability and realism": "Usability & Realism",
    "usability & realism": "Usability & Realism",
    "editability": "Editability",
}

VAGUE_WORDS = [
    "appropriate", "appropriately", "proper", "properly", "good", "clean",
    "suitable", "suitably", "reasonable", "reasonably", "correctly", "nice",
    "high quality", "high-quality", "adequate", "adequately", "professional-looking",
    "well-designed", "well designed", "looks good", "sounds good", "works well",
]

AI_FILLER = [
    "ensure", "ensures", "effectively", "seamlessly", "seamless", "robust",
    "compelling", "leverage", "leverages", "cohesive and", "in order to",
]

AVOIDANCE_STARTS = [
    "avoids", "avoid ", "does not", "doesn't", "do not", "no ", "free of",
    "without ", "is not ", "are not ", "never ", "lacks ",
]

COMPOUND_MARKERS = [" and ", " as well as ", " including ", "/", ";"]

STOPWORDS = set("""
the a an of in on at to for is are be with by from that this these those it its
or and as into than then there their they them which who whom whose what when
where while will would should could can may might must do does did done has have
had having not no nor so such very each every all any some both either neither
""".split())

PASS_WORDS = {"pass", "p", "yes", "y", "true", "1"}
FAIL_WORDS = {"fail", "f", "no", "n", "false", "0"}


def norm(s):
    return re.sub(r"\s+", " ", (s or "").strip())


def parse_verdict(v):
    v = norm(v).lower().strip("*_ ")
    if v in PASS_WORDS:
        return True
    if v in FAIL_WORDS:
        return False
    return None


def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [norm(c) for c in line.split("|")]


def is_separator(cells):
    return all(re.fullmatch(r":?-{2,}:?", c) or c == "" for c in cells) and any(c for c in cells)


def find_rubric_table(lines):
    """Return (header_cells, rows) for the first table whose header has Criterion and Weight."""
    for i, line in enumerate(lines):
        if not line.strip().startswith("|"):
            continue
        cells = split_row(line)
        low = [c.lower() for c in cells]
        if any("criterion" in c for c in low) and any("weight" in c for c in low):
            rows = []
            j = i + 1
            while j < len(lines) and lines[j].strip().startswith("|"):
                r = split_row(lines[j])
                if not is_separator(r):
                    rows.append(r)
                j += 1
            return cells, rows
    return None, []


def col_index(header, *names):
    low = [h.lower() for h in header]
    for name in names:
        for idx, h in enumerate(low):
            if h == name.lower():
                return idx
    for name in names:
        for idx, h in enumerate(low):
            if name.lower() in h:
                return idx
    return None


def parse_ratings(lines):
    """Parse the three comparison tables (Dimension | Rating) under their headings.
    Returns dict {'rd_ad1': avg, 'rd_ad2': avg, 'ad1_ad2': avg} with None where absent."""
    keys = [("rd_ad1", r"rd\s*vs\.?\s*ad1"), ("rd_ad2", r"rd\s*vs\.?\s*ad2"), ("ad1_ad2", r"ad1\s*vs\.?\s*ad2")]
    result = {k: None for k, _ in keys}
    current = None
    values = {k: [] for k, _ in keys}
    for line in lines:
        low = line.lower()
        if line.strip().startswith("#"):
            current = None
            for k, pat in keys:
                if re.search(pat, low):
                    current = k
                    break
            continue
        if current and line.strip().startswith("|"):
            cells = split_row(line)
            if len(cells) >= 2 and not is_separator(cells):
                m = re.fullmatch(r"[1-7](\.\d+)?", cells[1])
                if m:
                    values[current].append(float(cells[1]))
    for k in values:
        if values[k]:
            result[k] = sum(values[k]) / len(values[k])
    return result


def tokens(text):
    words = re.findall(r"[a-z0-9]+", text.lower())
    return set(w for w in words if w not in STOPWORDS and len(w) > 2)


def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def direction_expected(avg):
    """Return +1 if the second deliverable in the pair is expected ahead, -1 if the first, 0 if comparable."""
    if avg is None:
        return None
    if avg > 4.25:
        return 1
    if avg < 3.75:
        return -1
    return 0


def main():
    ap = argparse.ArgumentParser(description="Sardine Refiner rubric self-audit")
    ap.add_argument("worksheet")
    ap.add_argument("--pref-rd-ad1", type=float, default=None, help="average of the 5 RD vs AD1 ratings")
    ap.add_argument("--pref-rd-ad2", type=float, default=None, help="average of the 5 RD vs AD2 ratings")
    ap.add_argument("--pref-ad1-ad2", type=float, default=None, help="average of the 5 AD1 vs AD2 ratings")
    ap.add_argument("--min-count", type=int, default=30)
    ap.add_argument("--dup-threshold", type=float, default=0.6)
    args = ap.parse_args()

    try:
        with open(args.worksheet, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
    except OSError as e:
        print("FAIL  cannot read worksheet: %s" % e)
        return 1

    header, rows = find_rubric_table(lines)
    if header is None:
        print("FAIL  no rubric table found (need a markdown table whose header contains 'Criterion' and 'Weight')")
        return 1

    ci = {
        "id": col_index(header, "ID"),
        "text": col_index(header, "Criterion"),
        "cat": col_index(header, "Category"),
        "w": col_index(header, "Weight"),
        "src": col_index(header, "Source"),
        "rd": col_index(header, "RD"),
        "ad1": col_index(header, "AD1"),
        "ad2": col_index(header, "AD2"),
        "jrd": col_index(header, "Justification RD", "J-RD"),
        "jad1": col_index(header, "Justification AD1", "J-AD1"),
        "jad2": col_index(header, "Justification AD2", "J-AD2"),
    }

    def cell(row, key):
        idx = ci.get(key)
        if idx is None or idx >= len(row):
            return ""
        return row[idx]

    crits = []
    for r in rows:
        text = cell(r, "text")
        if not text:
            continue
        crits.append({
            "id": cell(r, "id") or ("row%d" % (len(crits) + 1)),
            "text": text,
            "cat": cell(r, "cat"),
            "w_raw": cell(r, "w"),
            "src": cell(r, "src"),
            "rd": parse_verdict(cell(r, "rd")),
            "ad1": parse_verdict(cell(r, "ad1")),
            "ad2": parse_verdict(cell(r, "ad2")),
            "jrd": cell(r, "jrd"),
            "jad1": cell(r, "jad1"),
            "jad2": cell(r, "jad2"),
        })

    fails, nonfails, warns, infos = [], [], [], []
    n = len(crits)

    # ---- Dim 3: count
    if n < 25:
        fails.append("Dim 3  criteria count = %d (< 25) [Fail - Criteria Count]" % n)
    elif n > 100:
        nonfails.append("Dim 3  criteria count = %d (> 100) [Non-Fail - Criteria Count]" % n)
    elif n < args.min_count:
        warns.append("Dim 3  criteria count = %d, below the course floor of %d; split compounds or cover implicit expectations" % (n, args.min_count))
    else:
        infos.append("Dim 3  criteria count = %d (ok)" % n)

    # ---- per-criterion checks
    pos_pool = 0
    scores = {"rd": 0, "ad1": 0, "ad2": 0}
    cat_counts = {}
    n_pos = n_neg = 0
    compound = vague = ai = 0
    comparative = 0
    for c in crits:
        cid = c["id"]
        text = c["text"]
        low = " " + text.lower() + " "

        # weight
        try:
            w = int(float(c["w_raw"]))
        except ValueError:
            w = None
        c["w"] = w
        if w is None:
            fails.append("%s  weight '%s' is not a number" % (cid, c["w_raw"]))
        elif w == 0 or w < -10 or w > 10:
            fails.append("%s  weight %d outside -10..10 or zero; excluded from scoring until fixed" % (cid, w))
            w = None
            c["w"] = None
        else:
            if w > 0:
                n_pos += 1
                pos_pool += w
            else:
                n_neg += 1

        # category
        cat_key = c["cat"].lower().replace("&", "and").replace("  ", " ").strip()
        cat_key = cat_key.replace(" and ", " and ")
        canon = APPROVED_CATEGORIES.get(cat_key) or APPROVED_CATEGORIES.get(c["cat"].lower().strip())
        if not c["cat"]:
            fails.append("%s  category blank" % cid)
        elif canon is None:
            fails.append("%s  category '%s' not one of the six approved categories" % (cid, c["cat"]))
        else:
            cat_counts[canon] = cat_counts.get(canon, 0) + 1

        # atomicity heuristics (Dim 9)
        # a colon usually introduces examples of ONE check ("no other instruments: voices, percussion...");
        # only the part before the colon is tested for list-like structure
        before_colon = text.split(":")[0] if ":" in text else text
        markers = [m for m in COMPOUND_MARKERS if m in (" " + before_colon.lower() + " ")]
        comma_list = len(re.findall(r",", before_colon)) >= 2
        # allow the lenient "A, B, or C" alternatives pattern only if it contains " or "
        if markers or (comma_list and " or " not in low):
            compound += 1
            warns.append("%s  possible compound criterion (%s): '%s'" % (
                cid, ", ".join(m.strip() or "list" for m in markers) or "comma list", text[:90]))

        # vague words (Dim 10)
        hits = [v for v in VAGUE_WORDS if re.search(r"\b" + re.escape(v) + r"\b", low)]
        if hits:
            vague += 1
            warns.append("%s  vague wording (%s); replace with a value, threshold or named element" % (cid, ", ".join(hits)))

        # AI filler (Dim 17)
        fhits = [v for v in AI_FILLER if re.search(r"\b" + re.escape(v.strip()) + r"\b", low)]
        if fhits:
            ai += 1
            warns.append("%s  AI-sounding wording (%s); rewrite plainly" % (cid, ", ".join(fhits)))

        # negative phrased as avoidance (pass-semantics trap): look at how the sentence opens
        if w is not None and w < 0:
            opening = re.match(
                r"^\s*(the\s+\w+(\s+\w+)?\s+)?(avoids?|does\s+not|doesn't|has\s+no|have\s+no|contains\s+no|is\s+free\s+of|are\s+free\s+of|without|never|lacks?|no\s+\w+\s+(is|are)\s+present)\b",
                low.strip())
            if opening:
                warns.append("%s  negative weight but phrased as avoidance/absence; negative criteria must describe the flaw happening (Pass = flaw present)" % cid)

        # comparative phrasing (golden-neutral, informational)
        if "at least as" in low and " rd" in low:
            comparative += 1

        # source
        if not c["src"]:
            warns.append("%s  no Source recorded (R#/S#/F#/D#/professional/observed E#)" % cid)
        else:
            s = c["src"].lower()
            if w is not None and "preferable" in s and abs(w) >= 8:
                warns.append("%s  source says 'preferable' but weight %d is Critical; expected 1..3 (Dim 4)" % (cid, w))
            if w is not None and re.search(r"\bmust\b", s) and abs(w) <= 3:
                warns.append("%s  source says 'must' but weight %d is Slightly; expected 8..10 (Dim 4)" % (cid, w))

        # verdicts and scoring
        for d in ("rd", "ad1", "ad2"):
            v = c[d]
            if v is None:
                warns.append("%s  %s verdict blank or unreadable (use Pass/Fail)" % (cid, d.upper()))
            elif w is not None and v:
                scores[d] += w

        # RD anomalies (Dim 15 hints)
        if w is not None:
            if w > 0 and c["rd"] is False:
                infos.append("%s  RD FAILS a positive criterion (weight %d); double-check, this costs RD points" % (cid, w))
            if w < 0 and c["rd"] is True:
                infos.append("%s  RD PASSES a negative criterion (weight %d, flaw present in RD); double-check" % (cid, w))

        # justifications (Dim 13)
        js = [c["jrd"], c["jad1"], c["jad2"]]
        blanks = [d for d, j in zip(("RD", "AD1", "AD2"), js) if not j]
        if blanks:
            warns.append("%s  justification blank for %s" % (cid, ", ".join(blanks)))
        elif len(set(js)) == 1:
            warns.append("%s  identical justification pasted for RD, AD1 and AD2; add a per-deliverable location" % cid)
        for d, j in zip(("RD", "AD1", "AD2"), js):
            if j and not re.match(r"^\W*(pass|fail|yes|no)\b", j.lower()):
                infos.append("%s  %s justification does not start with the verdict word" % (cid, d))
        # verdict/justification sign sanity for negatives
        if w is not None and w < 0:
            for d, j, v in zip(("RD", "AD1", "AD2"), js, (c["rd"], c["ad1"], c["ad2"])):
                jl = j.lower()
                if v is True and re.search(r"\b(absent|not present|no such|none|free of|avoid)", jl):
                    warns.append("%s  %s marked Pass on a negative criterion but justification reads like the flaw is absent (backwards?)" % (cid, d))
                if v is False and re.search(r"\b(present|contains|found|occurs|at \d)", jl) and "absent" not in jl and "no " not in jl:
                    infos.append("%s  %s marked Fail on a negative criterion; confirm the justification describes the flaw being absent" % (cid, d))

    # ---- Dim 9 / Dim 10 thresholds
    thr = max(4, int(0.10 * n + 0.999)) if n else 4
    if compound >= thr:
        fails.append("Dim 9  %d possible compound criteria (>= max(4, 10%% of %d)) [Fail - Criteria Atomicity]; review the WARN lines" % (compound, n))
    elif compound:
        nonfails.append("Dim 9  %d possible compound criteria; fix to reach [No Issues]" % compound)
    if vague >= thr:
        fails.append("Dim 10 %d vague criteria (>= max(4, 10%% of %d)) [Fail - Self-Contained or Vague Criteria]" % (vague, n))
    elif vague:
        nonfails.append("Dim 10 %d vague criteria; fix to reach [No Issues]" % vague)

    # ---- Dim 6: near-duplicates
    toks = {c["id"]: tokens(c["text"]) for c in crits}
    dup_pairs = []
    for a, b in combinations(crits, 2):
        j = jaccard(toks[a["id"]], toks[b["id"]])
        if j >= args.dup_threshold:
            dup_pairs.append((a["id"], b["id"], j))
    if len(dup_pairs) >= 2:
        fails.append("Dim 6  %d near-duplicate pairs [Fail - Overlap / Redundancy]: %s" % (
            len(dup_pairs), "; ".join("%s~%s (%.2f)" % p for p in dup_pairs)))
    elif len(dup_pairs) == 1:
        nonfails.append("Dim 6  1 near-duplicate pair: %s~%s (%.2f)" % dup_pairs[0])

    # ---- category spread, sign mix
    infos.append("Categories: " + ", ".join("%s=%d" % (k, v) for k, v in sorted(cat_counts.items())) if cat_counts else "Categories: none parsed")
    infos.append("Positive criteria = %d, negative = %d, comparative ('at least as ... RD') = %d" % (n_pos, n_neg, comparative))
    if n and cat_counts:
        top = max(cat_counts.values())
        if top / n > 0.8:
            warns.append("Dim 7  %.0f%% of criteria sit in one category; set may be skewed" % (100.0 * top / n))

    # ---- Dim 15 / Dim 14: scores and alignment
    pct = {}
    if pos_pool > 0:
        for d in ("rd", "ad1", "ad2"):
            pct[d] = 100.0 * scores[d] / pos_pool
        infos.append("Score model: P=%d | RD %d pts = %.1f%% | AD1 %d pts = %.1f%% | AD2 %d pts = %.1f%%" % (
            pos_pool, scores["rd"], pct["rd"], scores["ad1"], pct["ad1"], scores["ad2"], pct["ad2"]))
        if pct["rd"] < 95:
            fails.append("Dim 15 RD scores %.1f%% (< 95) [Fail - Golden Output Scoring]; check RD anomalies above" % pct["rd"])
        else:
            infos.append("Dim 15 RD >= 95% (ok)")
    else:
        fails.append("Dim 15 no positive weights parsed; cannot compute scores")

    parsed = parse_ratings(lines)
    prefs = {
        "rd_ad1": args.pref_rd_ad1 if args.pref_rd_ad1 is not None else parsed["rd_ad1"],
        "rd_ad2": args.pref_rd_ad2 if args.pref_rd_ad2 is not None else parsed["rd_ad2"],
        "ad1_ad2": args.pref_ad1_ad2 if args.pref_ad1_ad2 is not None else parsed["ad1_ad2"],
    }
    if pct:
        pairs = [("rd_ad1", "rd", "ad1"), ("rd_ad2", "rd", "ad2"), ("ad1_ad2", "ad1", "ad2")]
        for key, first, second in pairs:
            avg = prefs[key]
            if avg is None:
                infos.append("Dim 14 %s: no rating average supplied or parsed; skipped" % key)
                continue
            exp = direction_expected(avg)
            gap = pct[second] - pct[first]  # positive = second ahead
            label = "%s (avg %.2f)" % (key, avg)
            if exp == 1 and gap < -2:
                fails.append("Dim 14 %s: rating says %s ahead but totals put %s ahead by %.1f pts [Fail - Justification - Final Score Alignment]" % (label, second.upper(), first.upper(), -gap))
            elif exp == -1 and gap > 2:
                fails.append("Dim 14 %s: rating says %s ahead but totals put %s ahead by %.1f pts [Fail - Justification - Final Score Alignment]" % (label, first.upper(), second.upper(), gap))
            elif exp == 1 and gap <= 2:
                nonfails.append("Dim 14 %s: rating favours %s but totals are only %.1f pts apart (or lean the other way) [Non-Fail - Justification Alignment]" % (label, second.upper(), abs(gap)))
            elif exp == -1 and gap >= -2:
                nonfails.append("Dim 14 %s: rating favours %s but totals are only %.1f pts apart (or lean the other way) [Non-Fail - Justification Alignment]" % (label, first.upper(), abs(gap)))
            elif exp == 0 and abs(gap) > 5:
                nonfails.append("Dim 14 %s: rating says comparable but totals differ by %.1f pts" % (label, abs(gap)))
            else:
                infos.append("Dim 14 %s: consistent (gap %.1f pts)" % (label, gap))

    # ---- report
    print("=" * 78)
    print("Sardine Refiner rubric audit: %s" % args.worksheet)
    print("criteria parsed: %d" % n)
    print("=" * 78)
    for tag, bucket in (("FAIL", fails), ("NONFAIL", nonfails), ("WARN", warns), ("INFO", infos)):
        if bucket:
            print("\n[%s] (%d)" % (tag, len(bucket)))
            for line in bucket:
                print("  %-7s %s" % (tag, line))
    print("\n" + "=" * 78)
    if fails:
        print("RESULT: %d FAIL line(s). Do not submit until these are cleared." % len(fails))
        return 1
    if nonfails:
        print("RESULT: no FAIL, but %d NONFAIL line(s) would block a 5/5." % len(nonfails))
        return 0
    print("RESULT: clean on the deterministic checks. Now run PreSubmitChecklist.md for the judgement checks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
