# Sardine Refiner -- Project Instructions (Single Source of Truth)

> **Updated:** 2026-09-17 -- Initial build. Consolidated from the sardine_refiner project course (34 slides: big picture, vocabulary, workflow, 1-7 scale, five dimensions, justification rules, two gates, rubric review, categories, weights, pass semantics, rubric pointers, quality-not-rules, RD-as-bar, atomicity, checklist, Debussy worked example, 7-screen UI walkthrough, negative-criteria change note) and the QC Spec Doc (17 grading dimensions). Keep this file updated as new guidance arrives. Where the sources are silent, the rule is marked **(assumption)** and should be confirmed with your QM.

---

## 0. TL;DR (60 seconds)

**sardine_refiner** is a rubric review and preference comparison project. Every task gives you a client brief plus three deliverables that answered it: **RD** (the human-made reference), **AD1** and **AD2** (two model-made alternatives). You do three things:

1. **Understand the original job.** Open the Autoflation Link, read the brief (work description, requirements, script, provided files, deliverable spec), then experience RD, AD1 and AD2 in full.
2. **Rate three comparisons.** RD vs AD1, RD vs AD2, AD1 vs AD2. Five dimensions each on a 1-7 scale, plus one evidence-based justification paragraph per comparison. Then answer two gate questions: is the brief sufficient, and is RD worse than either alternative.
3. **Audit the rubrics** (only if both gates pass). The criteria are AI-generated and may be wrong. Fix text, weights and categories; add missing criteria; delete nonsense; then give every criterion three verdicts (RD, AD1, AD2) each with a justification. Minimum 30 criteria.

Your work is graded by QC on **17 dimensions** (QualitySpecDoc.md). Any [Fail] fails the task. Any [Non-Fail] means not perfect. The goal is 17 x [No Issues], which is a 5/5 task.

The three rules that decide most tasks: **never mix up RD/AD1/AD2**, **Pass = it happened (for positive and negative criteria alike)**, and **every claim in a justification needs a rubric behind it**.

---

## 0.1 Table of contents

1. Project overview
2. Vocabulary
3. The workflow (five stages, then rubric review)
4. Step 0: the Autoflation Link
5. Part One: preference comparison
6. The two gates
7. Part Two: rubric review
8. Scoring model and alignment
9. Deliverable-type expectations (short form)
10. The QC rubric (17 dimensions)
11. Common mistakes (quick table)
12. Glossary
13. Source documents, assumptions and open questions

---

## 1. Project overview

| Item | Value |
|---|---|
| Project name | sardine_refiner |
| Task type | Rubric Review and Preference Comparison |
| Inputs per task | Autoflation Link (brief + three deliverables + synthetic rubric set) |
| Your outputs | 15 ratings (3 comparisons x 5 dimensions), 3 comparison justifications, 2 gate answers, an edited rubric set (25-100 criteria, target 30+), 3 verdicts + 3 justifications per criterion |
| Graded by | QC Spec Doc, 17 dimensions, labels [Fail] / [Non-Fail] / [No Issues] |
| Perfect task | all 17 dimensions [No Issues] |

**What the data is for.** Your ratings, justifications and corrected rubrics become the ground truth used to compare model-generated deliverables against human professional work. A sloppy rubric or a wrong verdict poisons that ground truth, which is why QC checks verdict accuracy and RD sanity so hard.

---

## 2. Vocabulary

| Term | Meaning |
|---|---|
| **RD** | Reference Deliverable. The human-created professional output. The golden reference, but only after it survives Gate 2. |
| **AD1** | Alternative Deliverable 1. The first model-generated artifact. |
| **AD2** | Alternative Deliverable 2. The second model-generated artifact. |
| **Autoflation Link** | The task page. Top: the brief. Bottom: the three-part side-by-side (RD, AD1, AD2). Source of truth for every edit and justification you write. |
| **Brief** | Work description (job, audience, tone), requirements (length, format, style, palette, constraints), script or copy (exact wording that must appear), provided material (input files the work had to use), deliverables (file type, resolution, count expected). |
| **Comparison** | One of RD vs AD1, RD vs AD2, AD1 vs AD2. Each has five ratings and one justification. |
| **Dimension (rating)** | Realism, Design & UI/UX Quality, Professionalism, Coherence & Continuity, Multi-Asset Consistency. |
| **Gate** | One of two yes/no questions that decide whether the task continues to rubric review. |
| **Criterion / rubric** | One card: text, category, weight. Graded Pass/Fail for RD, AD1 and AD2, each with a justification. |
| **Category** | One of six: Requirements Compliance, Presentation & Aesthetics, Functionality, Content Correctness, Usability & Realism, Editability. |
| **Weight** | Signed integer from -10 to 10. Positive rewards a thing the deliverable should have; negative penalises a defect it should not have. |
| **Verdict** | Pass or Fail (shown as Yes/No on the platform). Pass = it happened. |
| **Synthetic rubrics** | The AI-generated starting criteria. May contain errors. Not the truth. |
| **Coverage matrix** | Your worksheet table mapping every requirement, expectation and observed failure to a criterion ID. |
| **Evidence Ledger** | Your worksheet log of observations with locations (timestamp, page, screen, region, file). |

Every question on the platform refers to the three artifacts by abbreviation. **Mixing them up invalidates the whole submission.** Never assume the human output is best; models sometimes win, and when they do you say so and explain why.

---

## 3. The workflow

### 3.1 Five stages, in this order

| Stage | Name | What you do |
|---|---|---|
| 01 | Check the Autoflation Link | Read the brief and requirements, then experience RD, AD1 and AD2 in full. |
| 02 | Rate RD vs AD1 | Five dimensions on the 1-7 scale, plus one overall justification. |
| 03 | Rate RD vs AD2 | The same five dimensions, judged independently of AD1. |
| 04 | Rate AD1 vs AD2 | The two model outputs head to head. Here 1 favours AD1 and 7 favours AD2. |
| 05 | Two gate questions | Is the brief sufficient? Is RD worse? Either one can end the task. Pass both and the rubrics open. |

### 3.2 Part Two: rubric review (reached only if both gates pass)

Confirm the three rubric guidelines, open the criteria list, then for each card: fix the text, fix the weight and category, give a verdict and a reason for RD, then AD1, then AD2. Add criteria where there are gaps. Remove criteria that make no sense. Finish with at least 30 criteria.

### 3.3 The UI, screen by screen (7 screens)

1. **Every dimension is scored three times.** Three panels (RD vs AD1, RD vs AD2, AD1 vs AD2), each "0/6 completed" (5 ratings + 1 justification). Each panel restates the dimension definition and the anchors (1 = RD is significantly better, 4 = comparable, 7 = ADx is significantly better; in the head-to-head, 1 = AD1 significantly better, 7 = AD2 significantly better).
2. **The two gate questions.** "Is the task brief sufficient to accurately evaluate and compare the deliverables (RD, AD1, and AD2)?" Yes/No. "Is the Reference Deliverable (RD) worse than any of the Alternative Deliverables (AD1 or AD2)?" Yes/No. Gate 1 No ends the task. Gate 2 Yes ends the task.
3. **Confirming the rubric guidelines.** A checkbox: rubrics are synthetic and may contain errors; add rubrics where you see gaps; if a model fails at something a rubric could catch, add it.
4. **The criteria list, then Continue.** Every criterion with weight and category; search, filter and sort exist to help you scan for duplicates and gaps; a counter shows answered/total; a summary panel shows positive vs negative point split, weight by category, and per-deliverable Yes/No point shares. Continue opens criteria one by one.
5. **Editing a criterion.** Text box, Weight (points, "relative significance to the overall rubric"), Category dropdown ("the functional or aesthetic focus area"). All three editable; adding and removing criteria is expected.
6. **A verdict and a reason, three times per criterion.** "Does the criterion pass for the Reference Deliverable (RD)?" Yes/No + Justification. Same pair for AD1 and AD2. Name the evidence and where it is: "The deliverable is in .mp3 format" works because a reviewer can check it in seconds.
7. **Final review and submit.** (Not captured in the course photos. Run PreSubmitChecklist.md before clicking.)

---

## 4. Step 0: the Autoflation Link is your source of truth

Open it in a new tab and leave it open. Every edit and every justification you write should trace back to something on that page.

**Top of page, the task brief. What was originally requested:**
- Work description: the job, audience, and tone
- Requirements: length, format, style, palette, constraints
- Script or copy (if applicable): exact wording that must appear
- Provided material (if applicable): input files the work had to use
- Deliverables: file type, resolution, and count expected

**Bottom of page, the comparison view:** RD (human-created), AD1 (model output 1), AD2 (model output 2). View all three before writing anything. First impressions are what the rating step is meant to capture.

**Practical rule:** extract the brief into the worksheet as a numbered requirement list (R1, R2, ...) and tag each item must / should / preferable / at discretion. Those tags drive weights later.

---

## 5. Part One: preference comparison

Three comparisons (RD vs AD1, RD vs AD2, AD1 vs AD2), each scored on five dimensions, each with its own justification.

### 5.1 Reading the 1-7 scale correctly

Low numbers favour the human reference, high numbers favour the model alternative, 4 means comparable. In AD1 vs AD2 the anchors shift: 1 favours AD1 and 7 favours AD2.

| Score | Meaning (RD vs ADx) | Meaning (AD1 vs AD2) |
|---|---|---|
| 1 | Reference is significantly better | AD1 is significantly better |
| 2 | Reference is better | AD1 is better |
| 3 | Reference is slightly better | AD1 is slightly better |
| 4 | Comparable quality | Comparable quality |
| 5 | Alternative is slightly better | AD2 is slightly better |
| 6 | Alternative is better | AD2 is better |
| 7 | Alternative is significantly better | AD2 is significantly better |

### 5.2 The five rating dimensions (rate all five in each comparison)

| # | Dimension | Question |
|---|---|---|
| 1 | Realism | How realistic and believable is the output? Does it look, sound, or feel natural and true-to-life? |
| 2 | Design & UI/UX Quality | How well-designed and user-friendly is it? |
| 3 | Professionalism | Does it meet professional standards? |
| 4 | Coherence & Continuity | Is it internally consistent and logically structured? |
| 5 | Multi-Asset Consistency | Are the components consistent with each other? |

If a dimension does not apply (a single-file deliverable has no multi-asset consistency), say so in the justification. **(assumption)** Enter 4 (comparable) for that dimension since the field is required; confirm with your QM.

### 5.3 One overall justification per comparison

After the five scores, write a paragraph covering your reasoning across all of them. "It's good" or "it fails" is not an answer.

**Rejected (no evidence, no comparison, no location):**
- "The reference is better overall."
- "AD1 looks unprofessional."
- "Both are fine, so I gave it a 4."
- "Design is bad, colours are off."

**What we want:**
> "AD1 follows the brief as well as RD: flat design, and all six script steps in order. The design is weaker: three scenes use the same layout, and the labels at 0:22 and 0:41 are hard to read against the green background. Only one file was delivered, so multi-asset consistency does not apply. Overall AD1 is a little behind RD, and the gap is about design, not content."

**The shape of a good justification:** name the dimension, point to concrete evidence, compare it to the other deliverable, say why a client would care.

**Rules that QC enforces (Dim 2):** the paragraph must explain what the brief asks for comprehensively and compare the deliverables in detail. Cover all five dimensions by name. Every praise or criticism must later map to a rubric criterion.

Full templates in JustificationGuide.md.

---

## 6. The two gates

Asked after the three comparisons. Both must pass before the rubric review opens; either one ends the task after an explanation.

### Gate 1: Is the task brief sufficient?

- **No:** say what is missing, then submit. Name the gap: an unstated constraint, an absent input file, a requirement too vague to check.
- **Yes:** continue to Gate 2. The brief tells you enough to evaluate and compare the three deliverables.

QC Dim 16 fails you if the brief was severely insufficient and you proceeded anyway. A precisely flagged gap is a complete, passing task.

**Sufficiency test:** can you, from the brief and inputs alone, decide for each deliverable whether it did the job? Are all referenced input files actually present? Is every requirement checkable (a value, a format, a script line) or at least judgeable by professional standard? If any answer is no and it blocks meaningful evaluation, answer No.

### Gate 2: Is RD worse than AD1 or AD2?

- **Yes:** explain why, then submit. A reference that loses to a model output is itself the finding.
- **No:** continue to the rubric review.

Use your own ratings as the input: if either RD comparison came out with the alternative ahead overall (ratings mostly 5-7, or a decisive 6-7 on the dimensions the brief cares about), answer Yes and write the explanation in the same evidence-located shape as a comparison justification. Do not answer No out of deference to the human.

---

## 7. Part Two: rubric review

Reached only if RD is not worse than the alternatives. Correct the rubrics, weights and categories, then judge every criterion against all three deliverables. Four actions: edit text, fix weights and categories, pass/fail x3, add and remove.

### 7.1 The rubrics are a starting point, not the truth (three obligations)

1. **Synthetic rubrics may contain errors.** They are AI-generated and may not be easy to read or understand. Examine every rubric and edit the text, weight, or category wherever necessary.
2. **Fill the gaps you find.** If an important expectation from the brief has no rubric testing it, you must create one.
3. **Cover failures a rubric could catch.** If a model clearly fails at something no rubric covers, you must write a criterion for it.

Removing criteria is also part of the job: drop a rubric if it makes no sense.

### 7.2 Anatomy of a rubric card

Each rubric appears in its own card. Text, weight and category are all editable. Correct them, then judge the criterion against all three deliverables.

1. **Fix the rubric text.** Rewrite it if it sounds overly AI-generated, unnatural, or does not read like something a human would naturally write.
2. **Fix the weight and category.** Adjust them if the importance or the category is misjudged relative to the brief. Weight is a signed value between -10 and 10.
   - **Evaluation source.** Where the package has several assets (3D model, render, plan, DWG, PDF, material presentation), state in the criterion which asset it is judged against, so model/render conflicts cannot arise (ArchitectureReviewGuide.md step 12).
3. **Does it pass for RD?** Verdict plus a comprehensive reason on why it is passing or failing.
4. **Does it pass for AD1?** Same.
5. **Does it pass for AD2?** Same.

### 7.3 The six rubric categories

The category tells you what to check. Correct it if it is wrong.

| Category | What it means |
|---|---|
| **Requirements Compliance** | Reference files and specs provided are adhered to, and explicit instructions in the brief are followed. Check adherence to the brief literally and strictly. |
| **Presentation & Aesthetics** | Design elements, taste, and a professional look and feel for the deliverable. Judge craft, not mere presence. |
| **Functionality** | The deliverable does what it is supposed to do in any context where behaviour matters: game, dashboard, interaction. Actually run or use the deliverable, if necessary, to check its functionality. |
| **Content Correctness** | The substance of the deliverable is right. Applies when you can check for accuracy, for example in data processing and dashboards. Recalculate or check figures by hand. |
| **Usability & Realism** | Everything a paying client would expect from a fully executed project or task, including the implicit expectation of industry-grade deliverables. |
| **Editability** | Whether the deliverables are in a state that allows easy modification, component-level editing, and integration with other projects. |

### 7.4 Weight is signed importance, -10 to 10

Positive weights reward things the deliverable should have. Negative weights penalise defects it should not.

| Range | Band | Meaning |
|---|---|---|
| 8 to 10 | Critically Important | The deliverable is unacceptable without it. |
| 4 to 7 | Important | Expected in professional work; missing it hurts. |
| 1 to 3 | Slightly Important | Adds polish or value beyond the core ask. |
| -1 to -3 | Slightly Detrimental | A minor flaw a client would notice. |
| -4 to -7 | Detrimental | A serious defect, such as unprofessional practice. |
| -8 to -10 | Critically Detrimental | A dealbreaker: a constraint violated, or a dead file. |

Calibration from the brief's own words: "must" / "only" / a hard constraint = 8-10. "should" / professional expectation = 4-7. "preferable" / "nice to have" = 1-3. In the Debussy example, "solo piano only" is weight 10 and "preferable to begin in C major" is weight 6.

**Architecture guide reading of the same scale:** 8-10 most significant (critical deliverables, required file types, major required elements, openability); 5-7 important (specific geometry, colours, realism, shapes, task-specific design conditions); 5 or less minor / primarily aesthetic. The bands overlap at 4-5; the kit keeps the course bands as the platform rule. Two rules from that guide apply everywhere: the weight reflects the impact of the criterion itself, not how easy the issue is to notice or how strongly you feel about it; and the minimum rubric count is a floor, not a target, so complex tasks may need many more criteria (QC ceiling 100).

### 7.5 Pass depends on the sign of the weight

| Weight sign | Pass means |
|---|---|
| Positive | **Pass = it happened.** The deliverable did the good thing the criterion asks for. |
| Negative | **Pass = the bad thing happened.** The deliverable includes the bad thing the criterion warns about. |

**Why this changed.** Negative-weight criteria were being graded backwards. Old (incorrect): Pass = the flaw was avoided, which made it possible for clean deliverables to be penalised for following the instructions. New (correct): Pass = the flaw happened; now if a deliverable includes the flaw, it passes, and the negative weight then hurts the score. Pass now means the same thing for positive or negative criteria: it happened. The sign of the weight just decides if that helps or hurts the score.

**Warning:** the course's Debussy worked example (slide "3 of 3") shows two negative criteria graded under the old rule. Do not copy those verdicts. See examples/debussy_worked_example.md for the corrected version.

### 7.6 Rubric pointers from recent audits (apply to every rubric you touch)

| Pointer | Rule |
|---|---|
| Justifications | One paragraph per verdict, not a blurb per section. |
| Format & Categories | Match the approved category list and format spec. |
| Duplicate Criteria | Same test, different wording: keep only one. |
| Overlapping Criteria | Do not bundle properties already scored elsewhere. |
| Accuracy to the Brief | Exact terms and values, never generalised. |
| Self-Contained Criteria | Vague references need explicit values or thresholds. |
| Criteria Phrasing | Coherent and unambiguous; do not make graders guess. |
| Score Alignment | Check the rating/justification against your final scores. |

### 7.7 Check quality, not just the rules

Doing what the brief asked is only the start. A lot of what makes an output good is never written down, and you must write rubrics for those things too.

Ask yourself: "Why do I actually prefer this one? What makes it feel more professional?" Each answer you can name is a rubric you are missing. Look and feel, colours, fonts, spacing, how well it works: write them down.

The brief never says it, but as an expert you expect it:
- **Audio.** Brief: "Make a pop track for a coffee-shop ad." Says nothing about mixing or structure. You expect anyway: clean sound with no crackle, a tempo that stays steady, a clear verse and chorus. A pop track without them sounds amateur.
- **Design.** Brief: "Design a poster using this layout." Says nothing about fonts, colours or layers. You expect anyway: type you can read, colours that work together, even spacing, and the file left editable rather than flattened.

**Simple rule: if an expert would call it a mistake, write a rubric for it, even if the brief never mentions it.**

### 7.8 Use RD as the bar, but only where it matters

Look at RD closely. It shows you the quality gaps the rubrics keep missing.

| Do | Don't | Remember |
|---|---|---|
| Use RD as the bar. Write the rubric as a comparison: "The look and feel is at least as good as RD." "It works at least as well as RD." You do not have to list every detail; RD sets the level. | Copy random details. If RD happens to use a certain corner angle, colour or key, do not ask the model to copy it unless the task really needs it. | Files must stay editable. A flat file can look fine and still be useless. A drawing usually keeps the background and each part on its own layer; if the model merges it all into one layer, the file is much harder to work with. Ask for layers or source files when that matters. |

**RD is a level to match, not a design to copy.**

### 7.9 One rubric, one thing to check (the most common mistake)

If a rubric has "and", a list, or more than one thing to check, split it.

| Mixed together | Split apart |
|---|---|
| "A complete, playable full track is delivered in MP3 format and runs approximately two minutes." | The delivered track is a complete, playable audio file. / The track is delivered in MP3 format. / The track's duration is approximately two minutes. |
| "Footer links to the clinic's social media correctly: Instagram, LinkedIn, and YouTube." | The footer contains a link to the clinic's Instagram page. / ... LinkedIn page. / ... YouTube channel. / Each link opens the correct corresponding page. |

Splitting big rubrics is also how you reach 30: smaller rubrics are better, and there are more of them.

### 7.10 Two things to get right before you submit

1. **At least 30 rubrics.** You must reach a minimum of 30 criteria. Too few usually means your rubrics are too big; split them apart. (QC hard limits: fewer than 25 fails, more than 100 is a non-fail.)
2. **Justifications: this is the part that matters most.** Make them detailed: say what each output did, where it did well or badly, and why that matters. Be specific; a short, vague justification is the fastest way to fail review. **Every claim needs a rubric:** if you praise or criticise something in a justification, there must be a rubric that covers it. If there is none, add one. This is checked closely.

---

## 8. Scoring model and alignment

The platform totals the weights. The formula is not printed in the course; this working model reproduces the panel's logic closely enough to self-check. **(assumption)** Confirm against the platform's summary panel on your first tasks.

```
P          = sum of positive weights
score(D)   = sum of weights of every criterion that D passes
             (positive passes add, negative passes subtract)
percent(D) = score(D) / P x 100
```

- **Golden artifact sanity (Dim 15):** percent(RD) must be 95 or higher. If it is not, a criterion is enforcing something the brief did not require, a verdict on RD is wrong, or a negative criterion is graded backwards.
- **Alignment (Dim 14):** the ordering of percent(RD), percent(AD1), percent(AD2) must agree with your 1-7 ratings. RD rated better than AD1 means percent(RD) > percent(AD1). AD2 rated 5 over AD1 means percent(AD2) is modestly above percent(AD1). A reversed story is a Fail.
- When the numbers disagree with the ratings, fix the root cause (weight, missing criterion, verdict, or an over-extreme rating). Never tune numbers to force the story.

---

## 9. Deliverable-type expectations (short form)

The full libraries live in RubricWritingGuide.md. Use them to write the implicit-expectation and expert-nuance criteria that QC Dim 7 and Dim 11 demand.

| Deliverable type | An expert expects, even if the brief is silent |
|---|---|
| Audio / music | no clipping or dropouts, steady tempo, clear structure, realistic instrument timbre, controlled leading and trailing silence, consistent loudness, requested format and duration |
| Static design (poster, logo, social) | legible type at delivered size, clear hierarchy, consistent alignment and spacing, harmonious colours with adequate contrast, correct dimensions and resolution, script copy verbatim, editable layers or source |
| Video / animation | requested resolution and duration, scenes in script order, readable on-screen text held long enough, audio in sync, smooth transitions, consistent style across scenes, no black frames |
| Web / UI / dashboard | loads without errors, links and controls work, responsive, readable, correct data and labelled charts, no placeholder text, accessible contrast, editable source |
| Game / interactive | runs, controls respond, win and lose states work, no crashes, instructions present, consistent assets |
| Document / deck / report | requested structure and length, correct figures, clean spelling and grammar, consistent formatting, editable format |
| Data / spreadsheet / code | formulas correct and totals reconcile, units stated, no hard-coded values where formulas belong, runs without error, documented |
| Architecture / interior (model, renders, plans) | files open, current version only, units and scale right, reference-file geometry matched to the extent the brief binds it (footprint, walls, openings, circulation, levels, site), stated dimensions exact or approximate as worded, render realism decomposed (light, scale, materials, shadows, secondary elements, artifacts), assets represent one proposal, editable layered model. Full library in ArchitectureReviewGuide.md section 9 |

---

## 10. The QC rubric (17 dimensions)

Full verbatim text, thresholds and recipes are in QualitySpecDoc.md. Summary:

| # | Dimension | Fail | Non-Fail | No Issues |
|---|---|---|---|---|
| 1 | SxS Rating - Ranking Disagreement | severe disagreement (<=2 vs >=6 on 3+ dims) | non-adjacent buckets on 2 dims, or adjacent on 3+ | agree, or variance is supported taste |
| 2 | Justification - Analysis | ranking only | partial explanation | very detailed, brief explained, compared in detail |
| 3 | Criteria Count | <25 | >100 | 25-100 |
| 4 | Weights | >10% of AD-failed criteria two bands off | <=10% | none |
| 5 | Golden-Solution Neutrality | >=20% arbitrary | 11-19% | <=10% |
| 6 | Overlap / Redundancy | 2+ | exactly 1 | none |
| 7 | Coverage | >=10% explicit missing, skewed, or superficial | 1 to <10% explicit missing, or implicit missing | explicit + implicit + expert nuance covered |
| 8 | Relevance & Correctness | 2+ irrelevant/arbitrary/region-assuming | exactly 1 | all relevant, justified, region-neutral |
| 9 | Atomicity | 4+ or 10% compound | 1-3 or <=9% | atomic |
| 10 | Self-contained / Vague | 4+ or 10% | 1-3 or <=9% | all self-contained |
| 11 | Aesthetic & Comparative Depth | design central but lumped or absent | misses key elements | per-element, proportional |
| 12 | Verdict Accuracy | >=10% wrong | >=1 but <10% wrong | all correct |
| 13 | Criteria Justifications | >=20% inaccurate | 11-19% | <=10% inaccurate |
| 14 | Justification-Final Score Alignment | reversed story | a couple of percent off | same story |
| 15 | Golden Artifact Sanity | RD <95% | (none) | RD >=95% |
| 16 | Brief & Input Sufficiency | insufficient and proceeded | (none) | sufficient |
| 17 | Unlisted Minor Errors | (none) | unlisted errors exist | none |

---

## 11. Common mistakes (quick table)

Full catalog with BAD/GOOD examples in CommonErrors.md.

| Mistake | Why it fails | Fix |
|---|---|---|
| Mixing up RD, AD1, AD2 in any field | Invalidates the whole submission | Label every worksheet row; re-read labels before each verdict |
| Rating without experiencing the whole deliverable | Wrong ratings, wrong verdicts (Dims 1, 12) | Play, run, open, scroll everything; log evidence with locations |
| "A is better" justification | Dim 2 Fail | Name dimension, evidence, location, comparison, client impact |
| Trusting the synthetic rubrics | Dims 5-11 | Edit every card; delete nonsense; add gaps |
| "and" in a criterion | Dim 9 | Split into one check each |
| "appropriate", "proper", "good" in a criterion | Dim 10 | Replace with the brief's exact value or a named element |
| Enforcing RD's arbitrary choices | Dim 5 | "at least as good as RD" or lenient alternatives |
| Grading a negative criterion as Pass when the flaw is absent | Dim 12, Dim 15 | Pass = the flaw happened |
| Praising something in a justification with no rubric for it | Course rule "every claim needs a rubric" | Add the criterion |
| Fewer than 30 criteria | Course floor (QC fails <25) | Split compound criteria, cover implicit expectations |
| Preference direction contradicts rubric totals | Dim 14 | Find the root cause; fix weight, verdict, or missing criterion |
| Proceeding on an insufficient brief | Dim 16 Fail | Answer Gate 1 No, name the gap, submit |

---

## 12. Glossary

| Term | Meaning |
|---|---|
| CB | Contributor (you). |
| QC / auditor | The reviewer who grades your task on the 17 dimensions. |
| QM | Quality manager / project lead you escalate questions to. |
| SxS | Side by side: the preference comparison of two deliverables. |
| Bucket (Dim 1) | A band of the 1-7 scale used by QC to measure disagreement. Not defined in the sources; treat 1-2, 3, 4, 5, 6-7 as the safe reading **(assumption)**. |
| Golden reference / golden output | RD after it passes Gate 2. Must score >=95% on the rubric. |
| Critically / Important / Slightly | The three positive weight bands (8-10, 4-7, 1-3) and their negative mirrors. |
| Explicit requirement | A line in the brief that states a checkable demand. |
| Implicit expectation | A professional standard a paying client assumes without stating. |
| Expert nuance | A check only a domain professional would know to make. |
| Region-based assumption | Grading on a locale convention (units, date format, regulation, spelling) the brief never declared. Forbidden. |

---

## 13. Source documents, assumptions and open questions

### 13.1 Sources (in "Sardine-refine sources/")

| File | Content |
|---|---|
| QC Spec Doc - Sayfa1.pdf | 17 QC dimensions with Fail / Non-Fail / No Issues text (P0 benchmark) |
| WhatsApp Image ... 6.28.41 PM to 6.29.47 PM (34 photos) | Project course slides: overview, vocabulary, Step 0, five-stage workflow, Part One (scale, dimensions, justification), two gates, Part Two (obligations, card anatomy, categories, weights, pass semantics, pointers, quality-not-rules, RD as bar, atomicity, checklist), Debussy worked example (brief + 10 criteria), UI walkthrough screens 1-6 of 7, "why this changed" note on negative criteria |
| Architectural workflow.pdf (25 pages) | Review & Rubric Quality Guide, Architecture / Interior Design: five rubric quality checks with architecture examples, direct vs specific reference coverage, exact vs approximate, overlap tests and two borderline cases, subjectivity decomposition, atomicity in both directions, self-containment, relevance and weight, pairwise dimensions, 8-question checklist, 22-step review workflow. Consolidated in ArchitectureReviewGuide.md |

### 13.2 Assumptions made in this kit (confirm with QM)

1. Rating for a non-applicable dimension: enter 4 and state N/A in the justification.
2. Scoring formula: score = sum of passed weights; percent = score / sum of positive weights.
3. Dim 1 buckets: 1-2, 3, 4, 5, 6-7.
4. UI walkthrough screen 7 of 7 (final review/submit) was not in the photos.
5. Course says "at least 30"; QC says 25-100. The kit enforces 30 as the floor; the architecture guide adds that the floor is not a target.
6. Weight bands: course says 8-10 / 4-7 / 1-3; architecture guide says 8-10 / 5-7 / 5 or less. Kit uses the course bands; weights 4 and 5 are the ambiguous zone.
7. The platform's "evaluation source" (3D model, render, plan, DWG, PDF, material presentation) is described in the architecture guide as something to "add"; whether it is a separate field or part of the criterion text was not shown. The kit puts it in the criterion text until confirmed.

### 13.3 Open questions

- Does the platform panel's "Yes %" for RD equal the percent(RD) used for the >=95% check, or is it a count share?
- Is there a time limit per task? (Not stated; pipeline.md carries a suggested budget.)
- Are there deliverable-type specific guidance docs beyond the course?

---

*End of project instructions. When in doubt, the Autoflation Link and QualitySpecDoc.md win.*
