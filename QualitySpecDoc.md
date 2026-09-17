# Sardine Refiner -- Quality Spec Doc (QC Benchmark, P0)

> **Updated:** 2026-09-17 -- Initial build. The 17 dimensions below are transcribed verbatim from "QC Spec Doc - Sayfa1.pdf" (Title / QC Comments columns). Each dimension is paired with a "recipe for No Issues" drawn from the sardine_refiner course slides. This file is the benchmark. A task is 5/5 only when all 17 rows land on [No Issues].

---

## 1. How QC grades you

- The auditor re-does the task: opens the same Autoflation Link, experiences RD, AD1 and AD2, forms their own ratings, then reads your ratings, justifications, rubric edits and verdicts.
- Each of the 17 dimensions gets exactly one label: [Fail - ...], [Non-Fail - ...] or [No Issues].
- Any [Fail] = the task fails. Any [Non-Fail] = the task is not perfect. Target: 17 x [No Issues].
- Dimensions 1-2 grade your comparison work. Dimensions 3-11 grade the rubric set you submit. Dimensions 12-15 grade your verdicts and the arithmetic. Dimension 16 grades Gate 1 honesty. Dimension 17 is the catch-all.
- Several dimensions are percentage thresholds over your criteria count. Count your criteria before you submit and recompute the percentages.

---

## 2. Threshold table (quick view)

| # | Dimension | Fail when | Non-Fail when | No Issues when |
|---|---|---|---|---|
| 1 | SxS Rating - Ranking Disagreement | Severe disagreement, e.g. you rate AD1/AD2 at most 2 in 3+ dimensions and the auditor thinks at least 6, or vice versa | 2 dimensions disagree on non-adjacent buckets; or 3+ dimensions disagree on adjacent buckets | Auditor agrees with all ratings, OR any variance is subjective taste that your justification adequately supports |
| 2 | Justification - Analysis | Only states the ranking ("A is better") | Some explanation or evidence, but not all issues addressed | Very detailed: explains what the brief asks comprehensively and compares the deliverables in detail |
| 3 | Rubric Criteria - Criteria Count (25-100) | Fewer than 25 criteria | More than 100 criteria | 25 to 100 criteria (course target: at least 30) |
| 4 | Rubric Criteria - Weights | More than 10% of criteria that AD1 and/or AD2 fail are weighted Critically when they should be Slightly, or vice versa | 10% or less such criteria | No such criteria |
| 5 | Rubric Criteria - Golden-Solution Neutrality | 20% or more of criteria enforce a subjective choice with no room for equally plausible alternatives, are not comparable to RD, and are not phrased leniently | 11% to 19% | 10% or less |
| 6 | Rubric Criteria - Overlap / Redundancy | 2 or more criteria redundant or overlapping | Exactly 1 | None |
| 7 | Rubric Criteria - Coverage | Missing explicit-requirement criteria >= 10% of count; OR set skewed toward a handful of aspects; OR set too high-level (superficial checks only) | 1 to <10% explicit requirements missing; OR 1+ implicit expectations missing | Covers all explicit requests, implicit professional expectations, and expert-level nuances |
| 8 | Rubric Criteria - Relevance & Correctness | 2 or more criteria irrelevant, arbitrary, or assuming undeclared region-based constraints | Exactly 1 | Every criterion relevant, justified as a requirement, free of undeclared region assumptions |
| 9 | Rubric Criteria - Atomicity | 4+ or 10% of criteria (whichever is bigger) combine unrelated checks | 1-3 or <=9%, or a few borderline-but-defensible bundles | Mostly atomic; combined criteria only pair elements that should be evaluated together |
| 10 | Rubric Criteria - Self-contained or Vague Criteria | 4+ or 10% (whichever is bigger) vague or not self-contained | 1-3 or <=9% | All criteria evaluable on their own, self-contained within RD + inputs + brief (or professional nuance), none vague |
| 11 | Rubric Criteria - Aesthetic & Comparative Depth | Design is central but rubric has almost no aesthetic/functionality criteria, or judges aesthetics as one lump | Has them but misses key elements | Each relevant visual/auditory element graded on its own, depth proportional to how central design is |
| 12 | Rubric Grading - Verdict Accuracy (RD/AD1/AD2) | 10% or more of Pass/Fail verdicts per response incorrect | Fewer than 10% but at least 1 incorrect | Every verdict for RD, AD1 and AD2 correct |
| 13 | Rubric Criteria - Criteria Justifications | 20% or more objectively inaccurate | 11% to 19% inaccurate | All correct and aligned with their ratings, OR 10% or less inaccurate |
| 14 | Rubric Grading - Justification-Final Score Alignment | Rubric totals show a large gap that opposes the stated preference direction, well beyond a couple of percent | Modest mismatch (a couple of percent), not a reversed story | Preference ranking and rubric totals tell the same story |
| 15 | Rubric Grading - Golden Artifact Sanity (RD >= 95%) | RD scores less than 95% on the rubric | (none) | RD scores 95% or higher |
| 16 | Task Setup - Brief & Input Sufficiency | Brief and inputs severely missing, and you proceeded instead of flagging | (none) | Brief and input files sufficient to carry the task |
| 17 | All CB Generated Content - Unlisted Minor Errors | (none) | Errors not named in the rubric above that stop the task from being perfect | No unlisted errors |

---

## 3. Dimension by dimension: verbatim text + recipe for No Issues

### Dim 1 -- SxS Rating - Ranking Disagreement

**Verbatim:**
> [Fail - Major Ranking Disagreement]: You and CB have a severe disagreement, such as one marks AD1/AD2 as at most 2 in at least 3 dimensions and auditor thinks it's at least a 6 or vice versa.
> [Non-Fail - Loose Ranking Disagreement] - For 2 dimensions, you and the contributor disagree on non-adjacent buckets - For 3+ dimensions, you and the contributor disagree on adjacent buckets
> [No Issues] - You agree with all of the contributor's ratings; OR any variance is a matter of subjective taste that the justification adequately supports.

**What the auditor does:** rates all three comparisons on the five dimensions themselves, then compares to your 15 numbers.

**Recipe for No Issues:**
1. Experience every deliverable in full before rating (play the whole track, run the whole game, open every file, scroll every page).
2. Rate each dimension from evidence you can point to, not from overall impression. Log the evidence in the worksheet Evidence Ledger with a location.
3. Use extremes (1, 2, 6, 7) only when the gap is large and you can name at least two concrete pieces of evidence for it. Most honest ratings live in 3 to 5.
4. Judge RD vs AD2 independently of RD vs AD1. Do not let one alternative's score anchor the other.
5. In AD1 vs AD2, remember the anchors flip: 1 favours AD1, 7 favours AD2.
6. The escape hatch is the justification: if your rating is defensible taste, the paragraph must show the evidence and reasoning. That is what "adequately supports" means.

**Self-test:** for each of the 15 ratings, can you say "I gave X because of [evidence at location] compared with [evidence at location]"? If not, you are guessing.

### Dim 2 -- Justification - Analysis

**Verbatim:**
> [Fail - Generic Justification] The justification does not provide any explanation other than stating the ranking, ex., "A is better."
> [Non-Fail - Generic Justification] The justification provides some explanation or evidence supporting the SxS ranking, but it did not address all the issues.
> [No Issues] The justification is very detailed: it explains what the brief asks for comprehensively and compares the deliverables in detail!

**What the auditor does:** reads the three comparison paragraphs and checks that every rating is explained, that the brief's requirements are referenced, and that both deliverables are compared with located evidence.

**Recipe for No Issues:**
1. One paragraph per comparison (three total). Each covers all five dimensions by name, even the ones that do not apply ("Only one file was delivered, so multi-asset consistency does not apply.").
2. Shape every claim as: name the dimension, point to concrete evidence with a location, compare to the other deliverable, say why a client would care.
3. Open by anchoring to the brief: what was asked (format, script steps, palette, length) and whether each deliverable met it.
4. State the net result and what the gap is about ("AD1 is a little behind RD, and the gap is about design, not content").
5. Every praise or criticism in the paragraph must have a rubric criterion behind it (the course checks this closely).

**Self-test:** count the dimensions named in each paragraph (must be 5), count the located evidence points (aim for 4+), confirm the final sentence states direction and cause.

### Dim 3 -- Rubric Criteria - Criteria Count (25-100)

**Verbatim:**
> [Fail - Criteria Count] The rubric has fewer than 25 criteria.
> [Non-Fail - Criteria Count] The rubric has more than 100 criteria.
> [No Issues] The rubric contains 25 to 100 criteria.

**Recipe for No Issues:**
1. Target at least 30 (course floor). Never submit under 25. Never exceed 100.
2. Reach the number by splitting compound criteria and by covering implicit expectations, never by padding with duplicates (that trades Dim 3 for Dim 6).
3. Count the final list on the platform counter before submitting.

### Dim 4 -- Rubric Criteria - Weights

**Verbatim:**
> [Fail - Criteria Weights] >10% of the rubric criteria that AD1 and/or AD2 fail AND are weighted as Critically Important/Detrimental when they should be Slightly Important/Detrimental or vice versa
> [Non-Fail - Criteria Weights] 10% or less criteria that AD1 and/or AD2 fail AND are weighted as Critically Important/Detrimental when they should be Slightly Important/Detrimental or vice versa
> [No Issues] There are no criteria that AD1 and/or AD2 fail AND are weighted as Critically Important/Detrimental when they should be Slightly Important/Detrimental or vice versa

**What the auditor does:** looks at every criterion an alternative fails and asks whether the weight band matches how much a client would care.

**Recipe for No Issues:**
1. Map the brief's language to bands: "must", "only", "required", a hard constraint or a dead file = Critically Important (8 to 10) or Critically Detrimental (-8 to -10). "Should", "expected", professional standard = Important (4 to 7) or Detrimental (-4 to -7). "Preferable", "nice to have", polish = Slightly Important (1 to 3) or Slightly Detrimental (-1 to -3).
2. Re-check weights specifically on the criteria that AD1 or AD2 fail. Those are the ones the auditor scrutinises.
3. A two-band jump (Critical vs Slightly) is the error the QC counts. Keep sibling criteria of similar importance in the same band.

### Dim 5 -- Rubric Criteria - Golden-Solution Neutrality

**Verbatim:**
> [Fail - Golden-Solution Neutrality] 20% or more of the criteria have major errors of this kind: they enforce subjective choices without room for equally plausible alternatives, and are neither comparable to the golden reference nor phrased leniently.
> [Non-Fail - Golden-Solution Neutrality] 11%-19% of the criteria have such errors.
> [No Issues] 10% or less of the criteria enforce an arbitrary subjective choice

**Recipe for No Issues:**
1. RD is a level to match, not a design to copy. If RD made a choice the brief never mandated (a corner radius, a key, a palette, a font), do not turn it into a criterion.
2. When quality must be judged, phrase comparatively: "The look and feel is at least as good as RD." "It works at least as well as RD."
3. Or phrase leniently with alternatives: "uses a pentatonic, whole-tone, or church-mode colour" instead of "uses the whole-tone scale at 1:00".
4. Reserve exact-value criteria for things the brief or input files actually fix (script lines, hex colours on the brand sheet, duration window, format).

### Dim 6 -- Rubric Criteria - Overlap / Redundancy

**Verbatim:**
> [Fail - Overlap / Redundancy] - 2 or more criteria are redundant or overlapping (independently assessing the same elements).
> [Non-Fail - Overlap / Redundancy]- Exactly 1 criterion is redundant or overlapping with another.
> [No Issues] - No redundant criteria is present.

**Recipe for No Issues:**
1. Duplicate = same test, different wording. Keep one, delete the other.
2. Overlap = a criterion bundles a property already scored elsewhere. Remove the bundled part.
3. After adding or splitting criteria, do a full pass over the list sorted alphabetically or by category; near-duplicates cluster.
4. Run tools/rubric_audit.py; it flags high-similarity pairs.
5. Fast overlap test: if one specific error occurred, how many criteria would fail for exactly that mistake? More than one means narrow, merge or rewrite.
6. Macro consistency criteria ("render matches model") are allowed only for proposal-level contradictions (different massing, layout logic, facade concept, version). Never fail them for a single wall, window or material mismatch that a detailed criterion already caught.

### Dim 7 -- Rubric Criteria - Coverage

**Verbatim:**
> [Fail - Missing Coverage] - The number of missing rubric criteria that correspond to the brief's explicit requirements is >=10% of the total rubric criteria count; OR the rubric set is highly skewed toward a handful of aspects and does not provide full coverage; OR the rubric set is too high-level -- it includes only superficial checks and misses the elements professionals care about.
> [Non-Fail - Missing Coverage] The number of missing rubric criteria that correspond to the brief's explicit requirements is at least 1 but less than 10% of the total rubric criteria count | 1+ implicit expectations are missing from the rubric.
> [No Issues] - The rubric covers all the explicit requests, the implicit professional expectations, and the expert-level nuances of the field (checks only a domain professional would know)!

**Recipe for No Issues:**
1. Build a coverage matrix before editing cards: one row per explicit requirement (numbered from the brief), one row per script line or provided file that must be used, one row per deliverable spec item (type, count, resolution, duration).
2. Add rows for implicit professional expectations by deliverable type (see RubricWritingGuide.md libraries).
3. Add rows for expert-level nuances: the things only a domain professional would flag.
4. Add rows for every failure you observed in AD1 or AD2 and for every claim in your comparison justifications.
5. Every row must point to at least one criterion ID. Empty row = write a criterion.
6. Spread across the six categories in proportion to what the brief is about. A set that is 90% Requirements Compliance for a design brief is "skewed".
7. Provided files: apply the direct-reference rule ("follow / preserve the file" makes its important content scope) or the specific-reference rule ("use the file only for X" limits coverage to X). Never promote incidental or legacy file content into requirements (ArchitectureReviewGuide.md section 2).
8. Keep exact and approximate language distinct: "300 cm" is a target, "approximately 300 cm" is a range; do not convert one into the other.
9. Subjective brief terms (photorealistic, refined, well-proportioned) are requirements too: decompose them into observable criteria rather than skipping them.

### Dim 8 -- Rubric Criteria - Relevance & Correctness

**Verbatim:**
> [Fail - Criteria Accuracy] 2 or more criteria are irrelevant to the task (no clear justification that they are a requirement), arbitrarily introduced, or assume region-based constraints the brief does not indicate
> [Non-Fail - Criteria Accuracy] Exactly 1 criterion is irrelevant, unjustified, or does not make sense given the brief
> [No Issues] Every criterion makes sense given the brief: all criteria are relevant, justified as requirements, and free of undeclared region-based assumptions.

**Recipe for No Issues:**
1. For every criterion, name its source: brief line, provided file, professional standard, or observed defect. No source = delete.
2. Do not assume a region: date formats, units, currency, spelling variant, legal or accessibility regulation, paper size, phone number format. If the brief does not state it, do not grade it.
3. Delete synthetic criteria that make no sense for the brief; removing is part of the job.

### Dim 9 -- Rubric Criteria - Atomicity

**Verbatim:**
> [Fail - Criteria Atomicity] - 4+ or 10% of the rubric (whichever is bigger) criteria combine unrelated checks together.
> [Non-Fail - Criteria Atomicity] - 1-3 or <=9% criteria bundle unrelated constraints, or a few bundles are borderline but defensible.
> [No Issues] - Criteria are mostly atomic: no criterion bundles multiple unrelated constraints; combined criteria only pair elements that should be evaluated together.

**Recipe for No Issues:**
1. One rubric, one thing to check. If the text contains "and", a list, a slash, or more than one verifiable fact, split it.
2. Allowed pairing: elements that cannot be judged apart ("each footer link opens the correct corresponding page").
3. Splitting is also how you reach 30.
4. Do not over-atomise: dependent details that only mean something as one requested combination stay together (a palette "of cool blue, indigo and dark navy" is one criterion). Split independent failure modes; a generic "matches the DWG" check hides several major failures inside one verdict and under-penalises.

### Dim 10 -- Rubric Criteria - Self-contained or Vague Criteria

**Verbatim:**
> [Fail - Self-Contained or Vague Criteria]- 4+ or 10% of the rubric (whichever is bigger) criteria are vague or not self-contained.
> [Non-Fail - Self-Contained or Vague Criteria]- 1-3 or <=9% criteria are vague or not self-contained, and neither fail condition applies.
> [No Issues]- All criteria are: 1) evaluable on their own, 2) self-contained within the RD, the inputs, and the brief, and/or 3) self-contained by professional nuance if a professional task; none require external references to evaluate, and none are vague.

**Recipe for No Issues:**
1. Replace vague words (appropriate, proper, good, clean, suitable, correct, reasonable, well) with explicit values, thresholds or named elements from the brief.
2. Every criterion must be gradable by a reviewer who has only the brief, the input files and the three deliverables in front of them.
3. Use the brief's exact terms and values, never generalised ("between 2:00 and 4:00", not "appropriate length").

### Dim 11 -- Rubric Criteria - Aesthetic & Comparative Depth

**Verbatim:**
> [Fail - Aesthetic Criteria] Design is central to the brief but the rubric has almost no aesthetic and/or functionality criteria when relevant, or judges aesthetics as a single lump.
> [Non-Fail - Aesthetic Criteria] The rubric has aesthetic and/or functionality criteria, when relevant, but misses key elements.
> [No Issues] The rubric grades each relevant visual/auditory element on its own, with aesthetic and or functionality depth proportional to how central design is.

**Recipe for No Issues:**
1. Never write "the design is professional" as one criterion. Break design into elements: typography legibility, hierarchy, alignment, spacing, colour harmony, contrast, imagery quality, consistency across scenes or assets, motion smoothness, mix cleanliness, and so on.
2. Judge craft, not presence: "type is legible at the delivered size" beats "type is present".
3. Scale the number of aesthetic criteria to how central design is. A poster brief needs many; a data-processing brief needs few.
4. Functionality gets the same treatment when behaviour matters: actually run or use the deliverable and write one criterion per behaviour.

### Dim 12 -- Rubric Grading - Verdict Accuracy (RD/AD1/AD2)

**Verbatim:**
> [Fail - Criteria Verdict Accuracy] 10% or more of Pass/Fail verdicts per response are incorrect
> [Non-Fail - Criteria Verdict Accuracy] Less than 10% but at least 1 of Pass/Fail verdicts per response are incorrect
> [No Issues] Every Pass/Fail verdict for RD, AD1, and AD2 is correct.

**Recipe for No Issues:**
1. Pass means "it happened", for both signs. Positive criterion: Pass = the good thing is present. Negative criterion: Pass = the flaw is present. Grading negatives backwards is the most common verdict error.
2. Judge each deliverable separately against each criterion. Never copy a verdict across the three without re-checking.
3. Locate the evidence before you click: timestamp, page, screen, region, file.
4. Where a criterion asks about a threshold, measure it (duration, count, dimensions) rather than eyeballing.

### Dim 13 -- Rubric Criteria - Criteria Justifications

**Verbatim:**
> [Fail - Criteria Justifications]: 20% or more of the criteria justifications are objectively inaccurate.
> [Non- Fail - Criteria Justifications]: 11%-19% of the criteria justifications are objectively inaccurate.
> [No Issues]: All the criteria justifications are correct and aligned with their ratings, OR only 10% or less of the justifications are objectively inaccurate.

**Recipe for No Issues:**
1. One paragraph per verdict (three per criterion), each naming the evidence and where it is.
2. The justification must agree with the verdict it sits under. "No static noodling" under a Pass on a negative criterion is a contradiction.
3. Write what you observed, not what you expected. If you did not check, do not claim.

### Dim 14 -- Rubric Grading - Justification-Final Score Alignment

**Verbatim:**
> [Fail - Justification - Final Score Alignment] The preference ranking and rubric scores are in high contrast: the rubric totals show a large gap that opposes the stated preference direction, and the difference is well beyond a couple of percent.
> [Non-Fail - Justification Alignment] There is a modest mismatch between the preference direction and the rubric totals, a couple of percent but not a reversed story.
> [No Issues] The preference ranking and rubric totals tell the same story.

**Recipe for No Issues:**
1. After all verdicts are in, compute each deliverable's rubric total (see section 4). Compare the ordering with your 1-7 ratings.
2. If you rated RD better than AD1 (mostly 1-3), RD's total must exceed AD1's. If you rated AD2 slightly better than AD1 (5) in the head-to-head, AD2's total must exceed AD1's by a modest margin, not a landslide.
3. When they disagree, find the root cause (a wrong weight, a missing criterion for something you praised, a wrong verdict, or an over-extreme rating) and fix that. Do not nudge numbers to force agreement.
4. The initial pairwise assessment may change once the rubric evidence is complete. Revising an earlier rating and its paragraph because the evidence supports a different conclusion is expected; protecting an earlier rating by tuning weights is the error.

### Dim 15 -- Rubric Grading - Golden Artifact Sanity (RD >= 95%)

**Verbatim:**
> [Fail - Golden Output Scoring] The golden output scores less than 95% on the rubric.
> [No Issues] Golden output scores 95% or higher on the rubric.

**Recipe for No Issues:**
1. RD passed Gate 2, so it is the golden reference. It should pass nearly every positive criterion and fail nearly every negative one.
2. If RD scores under 95%, either a criterion enforces something the brief never required (fix Dim 5 or 8), or a verdict on RD is wrong (fix Dim 12), or a negative criterion is being graded backwards.
3. Compute the number; do not assume it. On the platform, click Next after the rubric set is complete and read the scores.
4. Review RD failures first: is each one valid, is the weight right, is the rubric representing the task? Do not inflate RD artificially; a genuine RD failure stays a failure.

### Dim 16 -- Task Setup - Brief & Input Sufficiency

**Verbatim:**
> [Fail - Brief & Input Sufficiency] The input side (details in the brief and input files) is severely missing to realistically carry along the task, and the contributor proceeded anyway instead of flagging it.
> [No Issues] The brief and input files are sufficient to realistically carry along the task!

**Recipe for No Issues:**
1. Answer Gate 1 honestly. If a required input file is absent, a constraint is unstated, or a requirement is too vague to check, answer No, name the gap precisely, submit, stop.
2. Do not push through a broken brief to reach the rubric stage. A correctly flagged gap is a complete task.

### Dim 17 -- All CB Generated Content - Unlisted Minor Errors

**Verbatim:**
> [Non-Fail - Unlisted Minor Errors] There are errors in the task that are not explicitly mentioned in the grading rubrics but prevent the task from being perfect.
> [No Issues] There are no unlisted errors that you feel degrade the quality of the task

**Recipe for No Issues:**
1. Proofread everything you typed: spelling, RD/AD1/AD2 labels, weight signs, category names, leftover AI phrasing in edited criteria.
2. Check criteria read like a human wrote them (the course explicitly asks for this).
3. Run the PreSubmitChecklist.md sweep and tools/rubric_audit.py.

---

## 4. Working score model (for Dims 14 and 15)

The platform computes totals; the exact formula is not printed in the course. Use this model to self-check, then confirm against the platform summary panel (it shows positive vs negative point split and per-deliverable Yes/No point shares).

```
P            = sum of all positive weights (the maximum any deliverable can earn)
score(D)     = sum of weights of criteria D passes
               (positive criteria passed add their weight;
                negative criteria passed subtract, because the weight is negative)
percent(D)   = score(D) / P * 100

Dim 15 check : percent(RD) >= 95
Dim 14 check : ordering of percent(RD), percent(AD1), percent(AD2)
               matches the direction of your 1-7 ratings
```

Worked numbers (from examples/debussy_worked_example.md, 10 criteria): P = 53. AD1 = 32 (60.4%). AD2 = 23 (43.4%). So the AD1 vs AD2 head-to-head must lean toward AD1 (a rating of 1 to 3), and both RD comparisons must favour RD.

---

## 5. Self-audit scorecard (copy into the worksheet before submit)

| # | Dimension | My label | Evidence / count |
|---|---|---|---|
| 1 | Ranking Disagreement | | extremes used: __ / 15; each backed by 2+ located evidence points? |
| 2 | Justification Analysis | | 3 paragraphs, 5 dims each, located evidence count: __ |
| 3 | Criteria Count | | count = __ (25-100, target 30+) |
| 4 | Weights | | criteria AD1/AD2 fail = __; any two-band mismatch? |
| 5 | Golden-Solution Neutrality | | arbitrary-choice criteria = __ / __ = __% (<=10%) |
| 6 | Overlap / Redundancy | | duplicate pairs = 0 |
| 7 | Coverage | | matrix rows uncovered = 0; categories spread |
| 8 | Relevance & Correctness | | every criterion has a source; region assumptions = 0 |
| 9 | Atomicity | | compound criteria = __ (0 target) |
| 10 | Self-contained / Vague | | vague criteria = __ (0 target) |
| 11 | Aesthetic Depth | | design central? per-element aesthetic criteria = __ |
| 12 | Verdict Accuracy | | negatives graded as "flaw happened = Pass"? all three re-checked? |
| 13 | Criteria Justifications | | 3 per criterion, each with a location, each matching verdict |
| 14 | Score Alignment | | percent RD/AD1/AD2 = __/__/__; matches ratings? |
| 15 | Golden Artifact Sanity | | percent(RD) = __ (>=95) |
| 16 | Brief & Input Sufficiency | | Gate 1 answered honestly; gaps named if No |
| 17 | Unlisted Minor Errors | | proofread pass done; audit script clean |

**Verdict:** PASS only when all 17 rows read [No Issues].

---

*End of Quality Spec Doc.*
