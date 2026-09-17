# Sardine Refiner -- Pre-Submit Checklist

> **Updated:** 2026-09-17 -- Initial build. Red-flag sweep in pipeline order, each line tagged with the QC dimension it protects. Every box must be checked before you click submit. Ends with the 17-row scorecard.

---

## 1. Setup and brief [Dims 7, 8, 16]

- [ ] Autoflation Link open; every value below traces to it
- [ ] RD / AD1 / AD2 labels written at the top of the worksheet and used consistently everywhere
- [ ] Brief extracted: work description, R1..Rn, S1..Sn, F1..Fn, D1..Dn, each requirement tagged must / should / preferable / discretion
- [ ] Forbidden assumptions noted (region, units, date format, spelling, regulation)
- [ ] Sufficiency test run: every referenced input present, every requirement checkable
- [ ] Each provided file's authority recorded: direct reference (follow / preserve), specific reference (use only for X), or ambiguous
- [ ] Exact vs approximate wording preserved for every numeric requirement
- [ ] Package validated: inputs match the brief; RD could have come from these inputs; no outdated or duplicate RD files mistaken for current; AD1 and AD2 files open in the requested format (or another usable editable file exists)

## 2. Deliverables experienced [Dims 1, 12]

- [ ] RD opened / played / run / scrolled to the end
- [ ] AD1 opened / played / run / scrolled to the end
- [ ] AD2 opened / played / run / scrolled to the end
- [ ] Deliverable Inventory filled: files, formats, dimensions or duration, count vs spec, editable yes/no
- [ ] Evidence Ledger has located observations for all three across the whole length or page range

## 3. Three comparisons [Dims 1, 2]

- [ ] RD vs AD1: five ratings, each with E# evidence; extremes (1, 2, 6, 7) have two or more located facts
- [ ] RD vs AD2: judged independently of AD1
- [ ] AD1 vs AD2: anchors checked (1 favours AD1, 7 favours AD2); consistent with the two RD comparisons
- [ ] Three justification paragraphs: five dimensions named each, N/A stated where relevant, brief anchored, evidence located, both deliverables compared, last sentence gives direction and cause
- [ ] Direction of each paragraph matches its five numbers
- [ ] No "the reference", "the human one", "the first model" wording; labels only

## 4. Gates [Dim 16]

- [ ] Gate 1 answered from the sufficiency test; if No, gap statement names the missing constraint / file / uncheckable requirement and the task stops here
- [ ] Gate 2 answered from the ratings, not from deference; if Yes, explanation is evidence-located and the task stops here

## 5. Criterion content (every card) [Dims 4, 5, 8, 9, 10, 17]

- [ ] Every synthetic criterion triaged: keep / edit / delete, reason logged
- [ ] No "and", comma list, slash, "including", or second fact in any criterion (atomic)
- [ ] No appropriate / proper / good / clean / suitable / reasonable / correctly / well (self-contained)
- [ ] Brief values copied exactly (windows, formats, names, hex values)
- [ ] No criterion enforces a choice RD made that the brief did not mandate; comparative or lenient phrasing used; arbitrary-choice share <= 10%
- [ ] No undeclared region assumption
- [ ] Every criterion has a Source (R# / S# / F# / D# / professional / observed E#)
- [ ] Category is one of the six and names what is actually checked
- [ ] Weight band matches the brief's language (must 8-10, should 4-7, preferable 1-3, negative mirrors); siblings consistent
- [ ] Every negative criterion is phrased as the flaw happening (never "avoids X" at a negative weight)
- [ ] Text reads like a human wrote it; no "ensure", "effectively", "seamlessly", "robust", "compelling"

## 6. Rubric set [Dims 3, 6, 7, 11]

- [ ] Count between 30 and 100 (never under 25)
- [ ] No duplicate pair (same test, different wording)
- [ ] No overlap (a property scored twice through a bundle)
- [ ] Coverage matrix: every R#, S#, F#, D# row points to a criterion
- [ ] Implicit professional expectations for this deliverable type covered (library in RubricWritingGuide.md)
- [ ] Expert-level nuances covered (3+ checks only a professional would make)
- [ ] Every observed AD1/AD2 failure (E#) has a criterion
- [ ] Every praise or criticism in the three comparison paragraphs maps to a criterion ID
- [ ] If design is central: one aesthetic criterion per element (type, hierarchy, alignment, spacing, palette, contrast, imagery, consistency), not one lump
- [ ] If behaviour matters: one functionality criterion per behaviour you personally ran
- [ ] If figures matter: content criteria you personally recalculated
- [ ] If a client would edit the file: editability criteria (layers, live text, source)
- [ ] Categories spread in proportion to the brief (check the platform's weight-by-category panel)
- [ ] Subjective brief terms (photorealistic, refined, well-proportioned) decomposed into observable criteria, not ignored
- [ ] Fast overlap test passed: no single error would fail more than one criterion
- [ ] Macro consistency criteria limited to proposal-level contradictions; no double penalty for a detailed mismatch
- [ ] Dependent combinations kept as one criterion (no over-atomising); generic "matches the reference" checks split into independent failure modes
- [ ] Own outline built before adopting the synthetic set; both sets compared in both directions
- [ ] Final set entered in category order: Requirements Compliance, Content Correctness, Functionality, Usability & Realism, Presentation & Aesthetics, Editability
- [ ] Evaluation source named in the criterion wherever the package has several assets (model, render, plan, DWG, PDF, material board)

## 7. Verdicts and justifications [Dims 12, 13]

- [ ] Three verdicts per criterion, each judged fresh (no copy across RD, AD1, AD2)
- [ ] Pass = it happened, for both signs; every negative criterion re-read with that rule
- [ ] Three justification paragraphs per criterion, verdict word first, evidence located
- [ ] Every paragraph agrees with the verdict above it
- [ ] Thresholds measured (duration, count, size), not eyeballed
- [ ] RD verdicts consistent with RD being the golden reference (passes positives, fails negatives) unless evidence says otherwise

## 8. Alignment [Dims 14, 15]

- [ ] P, score(RD), score(AD1), score(AD2) computed in the worksheet; cross-checked with the platform panel
- [ ] percent(RD) >= 95
- [ ] Ordering of totals matches the 1-7 ratings: RD ahead where rated ahead; AD1 vs AD2 direction matches the head-to-head; margins proportional
- [ ] Any mismatch fixed at the root (weight band, missing criterion, verdict, rating), never by tuning numbers
- [ ] Scores read on the platform after clicking Next; every RD failure reviewed first (valid? weight right?) without inflating RD
- [ ] Criteria that still felt subjective made observable or removed; score check rerun after revisions
- [ ] Initial ratings revised only where the rubric evidence genuinely supports a different conclusion

## 8b. The architecture guide's eight questions (any NO means revise)

- [ ] Is every criterion atomic?
- [ ] Is every criterion self-contained?
- [ ] Is every criterion relevant?
- [ ] Is everything important covered in the rubrics?
- [ ] Are the rubrics free of duplicates and unnecessary overlap?
- [ ] Is every criterion easy to understand?
- [ ] Do PASS/FAIL verdicts match their justifications?
- [ ] Do the final scores align with the final pairwise ratings and justification?

## 9. Hygiene [Dim 17]

- [ ] `python tools/rubric_audit.py Tasks/<task-id>.md --pref-rd-ad1 <avg> --pref-rd-ad2 <avg> --pref-ad1-ad2 <avg>` run; zero FAIL lines
- [ ] Spelling and grammar pass over every typed field
- [ ] Weight signs correct (negatives for defects)
- [ ] Category dropdown set on every card (none left at default by accident)
- [ ] No em dashes, no AI filler, no leftover template placeholders
- [ ] Counter on the platform shows all criteria answered (N/N)

---

## 10. The 17-row scorecard (fill before submit)

| # | Dimension | Label I expect | Proof |
|---|---|---|---|
| 1 | Ranking Disagreement | | |
| 2 | Justification Analysis | | |
| 3 | Criteria Count | | count = |
| 4 | Weights | | AD-failed criteria checked: |
| 5 | Golden-Solution Neutrality | | arbitrary share = % |
| 6 | Overlap / Redundancy | | |
| 7 | Coverage | | uncovered rows = 0 |
| 8 | Relevance & Correctness | | |
| 9 | Atomicity | | compound = 0 |
| 10 | Self-contained / Vague | | vague = 0 |
| 11 | Aesthetic Depth | | |
| 12 | Verdict Accuracy | | |
| 13 | Criteria Justifications | | |
| 14 | Score Alignment | | RD/AD1/AD2 = / / |
| 15 | Golden Artifact Sanity | | RD = % |
| 16 | Brief & Input Sufficiency | | |
| 17 | Unlisted Minor Errors | | |

Submit only when all 17 read [No Issues]. Then log the task in TaskLog.md.

*End of Pre-Submit Checklist.*
