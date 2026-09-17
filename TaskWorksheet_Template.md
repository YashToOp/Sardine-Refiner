# Task Worksheet -- <task-id> -- <deliverable type>

> Copy this file to `Tasks/<task-id>.md` at STEP 0 of pipeline.md. Fill every section in order. Paste from here into the platform. `tools/rubric_audit.py` reads section 8 (the FINAL RUBRIC table) and section 4 (ratings); keep those table headers exactly as written.

**Labels for this task (never mix):** RD = human reference | AD1 = model output 1 | AD2 = model output 2

| Field | Value |
|---|---|
| Task id | |
| Date | |
| Autoflation Link | (open in a tab; do not paste secrets here) |
| Deliverable type | audio / static design / video / web / app / data / doc / game / 3D / other |
| Time started | |

---

## 1. Brief extraction (STEP 1)

**Work description (job, audience, tone):**

**Requirements**

| ID | Requirement (verbatim value) | Strength (must / should / preferable / discretion) | Keyed on (brief wording) |
|---|---|---|---|
| R1 | | | |
| R2 | | | |
| R3 | | | |

**Script / copy that must appear**

| ID | Exact wording | Where it must appear |
|---|---|---|
| S1 | | |

**Provided material**

| ID | File | How it must be used | Present? |
|---|---|---|---|
| F1 | | | |

**Deliverables spec**

| ID | Item | Type / format | Resolution / duration | Count |
|---|---|---|---|---|
| D1 | | | | |

**Provided-file authority (direct = follow/preserve the file; specific = use only for X; ambiguous = judgment on material details):**

| File | Authority | What it binds (or is limited to) |
|---|---|---|
| F1 | | |

**Forbidden assumptions (brief is silent on):** region / units / date format / spelling variant / regulation / paper size / other:

**Package validation (architecture guide steps 1-4):**

| Check | Result | Notes |
|---|---|---|
| Input files present match what the brief describes | | |
| RD could realistically have been produced from this brief and these inputs | | |
| Extra or outdated RD files? Which model / renders are current? | | |
| AD1 file opens in the requested format (or another usable editable file exists) | | |
| AD2 file opens in the requested format (or another usable editable file exists) | | |

**Gate 1 pre-check:** every referenced file present? every requirement checkable? package valid? Notes:

---

## 2. Deliverable inventory (STEP 2)

| | RD | AD1 | AD2 |
|---|---|---|---|
| Files delivered | | | |
| Format(s) | | | |
| Dimensions / duration | | | |
| Count vs D-spec | | | |
| Editable (layers / live text / source)? | | | |
| Fully experienced (played / run / opened to the end)? | | | |

---

## 3. Evidence Ledger (STEP 2)

One line per observation. Always a location.

| E# | Deliverable | Location | Observation | Dimension / Category |
|---|---|---|---|---|
| E1 | | | | |
| E2 | | | | |
| E3 | | | | |
| E4 | | | | |
| E5 | | | | |
| E6 | | | | |
| E7 | | | | |
| E8 | | | | |

---

## 4. Comparisons (STEP 3-5)

### 4.1 RD vs AD1 (1 = RD significantly better, 4 = comparable, 7 = AD1 significantly better)

| Dimension | Rating | Evidence (E#) |
|---|---|---|
| Realism | | |
| Design & UI/UX Quality | | |
| Professionalism | | |
| Coherence & Continuity | | |
| Multi-Asset Consistency | | |

**Justification (one paragraph, five dimensions named, located, compared, direction + cause):**

### 4.2 RD vs AD2 (judged independently of AD1)

| Dimension | Rating | Evidence (E#) |
|---|---|---|
| Realism | | |
| Design & UI/UX Quality | | |
| Professionalism | | |
| Coherence & Continuity | | |
| Multi-Asset Consistency | | |

**Justification:**

### 4.3 AD1 vs AD2 (1 = AD1 significantly better, 7 = AD2 significantly better)

| Dimension | Rating | Evidence (E#) |
|---|---|---|
| Realism | | |
| Design & UI/UX Quality | | |
| Professionalism | | |
| Coherence & Continuity | | |
| Multi-Asset Consistency | | |

**Justification:**

**Consistency check:** RD vs AD1 avg = ___ ; RD vs AD2 avg = ___ ; AD1 vs AD2 avg = ___ ; consistent? ___

---

## 5. Gates (STEP 6)

| Gate | Answer | Statement (if the task ends here) |
|---|---|---|
| Gate 1: brief sufficient? | Yes / No | |
| Gate 2: RD worse than AD1 or AD2? | Yes / No | |

---

## 6. Rubric build (STEP 7)

### 6.1 My own outline first (from brief + inputs + ledger, in category order)

| # | Criterion (draft) | Category | Weight | Source | Matches a synthetic criterion? (ID or none) |
|---|---|---|---|---|---|
| O1 | | Requirements Compliance | | | |
| O2 | | Content Correctness | | | |
| O3 | | Functionality | | | |
| O4 | | Usability & Realism | | | |
| O5 | | Presentation & Aesthetics | | | |
| O6 | | Editability | | | |

### 6.2 Triage of synthetic criteria (copied out, not edited in place)

| ID | Original text | Action (keep / edit / split / delete) | New text | Category | Weight | Reason (QC dim) |
|---|---|---|---|---|---|---|
| C1 | | | | | | |
| C2 | | | | | | |
| C3 | | | | | | |

**Both-direction gap check:** in my outline but not synthetic: ___ | in synthetic but not my outline (keep or nonsense?): ___

---

## 7. Coverage matrix (STEP 8)

| Row type | Row | Criterion ID(s) | Covered? |
|---|---|---|---|
| Explicit R# | R1 | | |
| Explicit R# | R2 | | |
| Script S# | S1 | | |
| Provided F# | F1 | | |
| Deliverable D# | D1 | | |
| Implicit expectation | | | |
| Implicit expectation | | | |
| Expert nuance | | | |
| Expert nuance | | | |
| Observed failure | E# | | |
| Justification claim | "..." (from 4.1 / 4.2 / 4.3) | | |

**Claim-to-criterion map (every praise or criticism in section 4):**

| Claim (quote) | Comparison | Criterion ID |
|---|---|---|
| | | |

**Shape check:** count ___ (30-100) | positive ___ | negative ___ | categories: RC ___ PA ___ FN ___ CC ___ UR ___ ED ___ | arbitrary-choice share ___% (<=10) | aesthetics per element? ___ | functionality run? ___ | editability covered? ___

---

## 8. FINAL RUBRIC (STEP 9) -- keep this header row exactly for the audit script

Verdicts: Pass or Fail (Yes/No also accepted). Pass = it happened (positive: good thing present; negative: flaw present). Multi-asset packages: start the criterion with the evaluation source ("In the 3D model, ..."; "In the exterior render, ..."). Enter on the platform in category order: Requirements Compliance, Content Correctness, Functionality, Usability & Realism, Presentation & Aesthetics, Editability.

| ID | Criterion | Category | Weight | Source | RD | AD1 | AD2 | Justification RD | Justification AD1 | Justification AD2 |
|---|---|---|---|---|---|---|---|---|---|---|
| C1 | | | | | | | | | | |
| C2 | | | | | | | | | | |
| C3 | | | | | | | | | | |
| C4 | | | | | | | | | | |
| C5 | | | | | | | | | | |
| C6 | | | | | | | | | | |
| C7 | | | | | | | | | | |
| C8 | | | | | | | | | | |
| C9 | | | | | | | | | | |
| C10 | | | | | | | | | | |
| C11 | | | | | | | | | | |
| C12 | | | | | | | | | | |
| C13 | | | | | | | | | | |
| C14 | | | | | | | | | | |
| C15 | | | | | | | | | | |
| C16 | | | | | | | | | | |
| C17 | | | | | | | | | | |
| C18 | | | | | | | | | | |
| C19 | | | | | | | | | | |
| C20 | | | | | | | | | | |
| C21 | | | | | | | | | | |
| C22 | | | | | | | | | | |
| C23 | | | | | | | | | | |
| C24 | | | | | | | | | | |
| C25 | | | | | | | | | | |
| C26 | | | | | | | | | | |
| C27 | | | | | | | | | | |
| C28 | | | | | | | | | | |
| C29 | | | | | | | | | | |
| C30 | | | | | | | | | | |

(Add rows as needed. Delete empty rows before running the script.)

---

## 9. Alignment (STEP 10)

```
P            = sum of positive weights                    = ____
score(RD)    = sum of weights RD passes                   = ____   percent(RD)  = ____ %   (>= 95 required)
score(AD1)   =                                            = ____   percent(AD1) = ____ %
score(AD2)   =                                            = ____   percent(AD2) = ____ %
Platform panel numbers (for cross-check)                  : RD ____  AD1 ____  AD2 ____
```

| Check | Expected from ratings | Actual from totals | OK? |
|---|---|---|---|
| RD vs AD1 | | | |
| RD vs AD2 | | | |
| AD1 vs AD2 | | | |

**If mismatch, root cause and fix:**

---

## 10. Pre-submit scorecard (STEP 11)

Run: `python tools/rubric_audit.py Tasks/<task-id>.md --pref-rd-ad1 <avg> --pref-rd-ad2 <avg> --pref-ad1-ad2 <avg>`

| # | Dimension | Label | Proof |
|---|---|---|---|
| 1 | Ranking Disagreement | | |
| 2 | Justification Analysis | | |
| 3 | Criteria Count | | |
| 4 | Weights | | |
| 5 | Golden-Solution Neutrality | | |
| 6 | Overlap / Redundancy | | |
| 7 | Coverage | | |
| 8 | Relevance & Correctness | | |
| 9 | Atomicity | | |
| 10 | Self-contained / Vague | | |
| 11 | Aesthetic Depth | | |
| 12 | Verdict Accuracy | | |
| 13 | Criteria Justifications | | |
| 14 | Score Alignment | | |
| 15 | Golden Artifact Sanity | | |
| 16 | Brief & Input Sufficiency | | |
| 17 | Unlisted Minor Errors | | |

**Submitted at:** ___ **Time taken:** ___

---

## 11. Post-task notes (STEP 12, copy to TaskLog.md)

- What surprised me:
- What took longest:
- What QC said (fill in later):
