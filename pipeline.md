# Sardine Refiner -- Task Pipeline

> **Updated:** 2026-09-17 -- Initial build from the project course + QC Spec Doc.

Invoke this file at the start of every task. Follow each step in order. Do not skip steps. Every step names the QC dimension it protects (see QualitySpecDoc.md).

**Two-device execution order (SessionPrompts.md section 5).** The Outlier page lives on the recorded PC; the worksheet, the AI and the QC live on the Mac. STEP 0-2 gather inputs from the PC as photos or notes. STEP 3-6 are drafted on the Mac and typed into the PC once. STEP 7-11 (rubric set, verdicts, alignment, closing QC) are completed on the Mac BEFORE anything from the rubric phase is typed into the PC, so fixes never mean retyping. Then type once from the teleprompter, click Next, photograph the score panel, reconcile on the Mac, submit. Where a step below says "on the platform", read it as "type it into the PC from the finished Mac draft".

---

## STEP 0 -- Setup (2 min)

1. Open the Autoflation Link in a new tab. Leave it open for the whole task.
2. Copy `TaskWorksheet_Template.md` to `Tasks/<task-id>.md`. Every note, rating, justification and criterion goes there first, then gets pasted into the platform.
3. Read the CRITICAL RULES block at the top of `TaskLog.md`.
4. Write the three labels at the top of your worksheet and keep them straight for the whole task: **RD** = human reference, **AD1** = model output 1, **AD2** = model output 2. Mixing them up invalidates the submission.

---

## STEP 1 -- Absorb the brief (5-10 min) [Dims 7, 8, 16]

From the top of the Autoflation Link, extract into the worksheet:

```
Work description : job, audience, tone
Requirements     : R1, R2, R3 ... (one line each, verbatim value)
Script / copy    : S1, S2 ... (exact wording that must appear)
Provided material: F1, F2 ... (input files the work had to use)
Deliverables     : D1, D2 ... (file type, resolution, duration, count)
```

Tag every requirement with its strength, using the brief's own words:
- **must** / only / required / hard constraint -> will be Critically Important (8-10)
- **should** / expected / standard -> Important (4-7)
- **preferable** / nice to have / polish -> Slightly Important (1-3)
- **at discretion** -> not a criterion (do not grade what the brief left free)

Note anything the brief leaves open that a grader could wrongly assume (region, units, date format, spelling variant, regulation). Those are forbidden assumptions later.

**Reference-file authority (ArchitectureReviewGuide.md section 2):** for each provided file, record how strongly the brief binds the task to it. "Follow / preserve / reproduce the file" = direct reference: the file's important content becomes scope. "Use the file only for X" = specific reference: cover only X. Ambiguous = professional judgment on details that materially change the result; never promote incidental or legacy file content into requirements.

**Exact vs approximate:** keep the brief's wording. "300 cm" is an exact target. "Approximately 300 cm" is a range; do not convert it into an exact rule.

**Package validation (ArchitectureReviewGuide.md section 11, steps 1-4):**
- The input files actually present match what the brief describes.
- RD could realistically have been produced from this brief and these inputs.
- No extra or outdated RD files confuse which version is current; note which model or renders are current.
- AD1 and AD2 files open in the requested format; if not, is there another usable editable file? If no reliable evaluation source remains, the package is insufficient.

**Gate 1 preview:** if a referenced input file is missing, a constraint is unstated, a requirement cannot be checked, or package validation fails, mark it now. You will answer Gate 1 after the comparisons, but you should already know the answer.

---

## STEP 2 -- Experience all three deliverables in full (10-20 min) [Dims 1, 12]

For each of RD, AD1, AD2:
1. Open every file. Play the whole track. Watch the whole video. Run the game or dashboard and use every control. Scroll every page. Open layers or source files if delivered.
2. Record in the worksheet Deliverable Inventory: files delivered, formats, dimensions/duration, count vs D-spec, editable (layers/source) yes/no.
3. Log observations in the Evidence Ledger, one line each, with a location:

```
| E# | Deliverable | Location | Observation | Dimension / Category |
| E1 | AD1 | 0:22 | label unreadable on green background | Design / Presentation |
```

Locations: timestamps mm:ss, page or slide number, screen or section name, region of the frame, cell or line, file name.

**Do not rate anything until all three are fully experienced.** First impressions are what the rating step captures, but they must be complete impressions.

---

## STEP 3 -- Rate RD vs AD1 (5 min) [Dims 1, 2]

Five dimensions, 1-7. Low favours RD, 4 comparable, high favours AD1.

For each dimension, write the score and the E# lines that justify it:

| Dimension | Score | Evidence (E#) |
|---|---|---|
| Realism | | |
| Design & UI/UX Quality | | |
| Professionalism | | |
| Coherence & Continuity | | |
| Multi-Asset Consistency | | (if single file: N/A, enter 4, say so) |

Rules:
- Extremes (1, 2, 6, 7) only with two or more located evidence points for a large gap.
- Then write ONE justification paragraph covering all five dimensions. Shape per claim: dimension -> evidence + location -> comparison -> why a client cares. Close with net direction and what the gap is about. Template in JustificationGuide.md.
- Every praise or criticism you write here becomes a coverage-matrix row in STEP 8.

---

## STEP 4 -- Rate RD vs AD2 (5 min) [Dims 1, 2]

Same five dimensions. Judge AD2 against RD independently of AD1. Do not let the AD1 scores anchor you. Same evidence table, same justification shape.

---

## STEP 5 -- Rate AD1 vs AD2 (5 min) [Dims 1, 2]

Head to head. **1 favours AD1, 7 favours AD2.** Re-read the anchors on the platform panel before typing. Same evidence table, same justification shape.

Sanity: if RD vs AD1 averaged 3 and RD vs AD2 averaged 5, then AD1 vs AD2 should land above 4 (AD2 ahead). If it does not, one of the three comparisons is wrong; find which.

---

## STEP 6 -- The two gates (2 min) [Dim 16]

**Gate 1: Is the task brief sufficient to evaluate and compare RD, AD1 and AD2?**
- Run the sufficiency test from STEP 1. If a gap blocks meaningful evaluation: answer **No**, write the gap statement (template below), submit, stop. That is a complete task.
- Otherwise answer **Yes**.

**Gate 2: Is RD worse than AD1 or AD2?**
- Look at STEP 3 and STEP 4. If either alternative is ahead of RD overall (ratings mostly 5-7, or decisive 6-7 on the dimensions the brief cares about): answer **Yes**, write the explanation (same evidence-located shape), submit, stop. A reference that loses to a model output is itself the finding.
- Otherwise answer **No** and continue. Never answer No out of deference to the human.

---

## STEP 7 -- Rubric triage: the synthetic criteria (15-25 min) [Dims 5, 6, 8, 9, 10]

Confirm the three guidelines on the platform (synthetic rubrics may be wrong; fill gaps; cover catchable failures). Then work the list, not the cards yet.

**7a. Copy the synthetic set out first.** Photograph every screen of the criteria list on the PC and have the synthetic criteria transcribed verbatim into the worksheet Triage Table (text, category, weight, numbered in screen order) so the set stays visible as a reference; do not edit blindly in place.

**7b. Build your own outline before reading theirs closely.** From the brief, the inputs and the Evidence Ledger, draft your own criteria list in category order: Requirements Compliance, Content Correctness, Functionality, Usability & Realism, Presentation & Aesthetics, Editability. This stops the synthetic set from anchoring you.

**7c. Compare both directions.** What is in your outline but not the synthetic set (their gap)? What is in theirs but not yours (your gap, or their nonsense)? The two sets check each other.

**7d. Triage each synthetic criterion** (keep / edit / split / delete):

For each criterion ask, in this order:
1. **Source?** Which R#, S#, F#, D#, professional standard or observed failure does it come from? None -> delete. [Dim 8]
2. **Region assumption?** Grades a locale convention the brief never declared -> delete or rewrite. [Dim 8]
3. **Atomic?** Contains "and", a list, a slash, "including", or two verifiable facts -> split. [Dim 9]
4. **Self-contained?** Contains appropriate / proper / good / clean / suitable / reasonable / correctly / well -> replace with the brief's exact value, a threshold, or a named element. [Dim 10]
5. **Golden-neutral?** Enforces a choice RD made that the brief did not mandate -> rewrite as "at least as good as RD" or list plausible alternatives. [Dim 5]
6. **Duplicate or overlap?** Same test as another card, or bundles a property scored elsewhere -> keep one, trim the other. [Dim 6]
7. **Human-readable?** Sounds AI-generated or unnatural -> rewrite plainly. [Dim 17]
8. **Category right?** One of the six; pick the one that names what you will actually check. [Dim 17]
9. **Weight right?** Band from the STEP 1 tag. Must = 8-10, should = 4-7, preferable = 1-3. Negative mirror for defects. [Dim 4]

Keep the edit reason in the table; you will reuse it if QC asks.

---

## STEP 8 -- Coverage build: reach 30+ with full coverage (15-25 min) [Dims 3, 7, 11]

Build the Coverage Matrix in the worksheet. One row per:
- explicit requirement R#, script line S#, provided file F#, deliverable spec D#
- implicit professional expectation for this deliverable type (use the library in RubricWritingGuide.md)
- expert-level nuance (what only a professional in this field would flag)
- every observed failure in the Evidence Ledger for AD1 or AD2
- every praise or criticism sentence in your three comparison justifications

Each row must point to at least one criterion ID. Empty row -> write a new criterion (atomic, self-contained, sourced, categorised, weighted).

Then check the set shape:
- Count >= 30 (never < 25, never > 100). Split compound criteria before inventing new ones.
- Categories spread in proportion to the brief. A design brief needs many Presentation & Aesthetics criteria, one per element (typography, hierarchy, spacing, colour, contrast, imagery, motion, consistency), not one lump. [Dim 11]
- Functionality criteria exist for every behaviour that matters, and you actually ran it.
- Editability criterion exists when the client would need to modify the file (layers, source, non-flattened).
- Negative criteria exist for observed defects, weighted by severity band, phrased as the bad thing happening.
- Subjective brief terms (photorealistic, refined, well-proportioned) are decomposed into observable criteria, not ignored (ArchitectureReviewGuide.md section 4).
- Dependent details stay together (a combined palette is one criterion); only independent failure modes are split. Fast overlap test on every pair: if one error occurred, how many criteria would fail for it? More than one -> merge or narrow.
- Macro consistency criteria (render matches model) are kept to proposal-level contradictions and never re-penalise a single detailed mismatch.
- Enter the final set on the platform in category order (Requirements Compliance, Content Correctness, Functionality, Usability & Realism, Presentation & Aesthetics, Editability).
- Where assets differ (3D model, render, plan, DWG, PDF, material board), state the evaluation source in the criterion text so model/render conflicts cannot arise.

---

## STEP 9 -- Verdicts and justifications, three per criterion (20-40 min) [Dims 12, 13]

Draft on the Mac first (worksheet FINAL RUBRIC table); type into the platform only after STEP 10 and STEP 11. For each criterion:

1. Apply the edited text, weight, category from STEP 7/8. For existing synthetic cards record the edit as a delta (KEEP / CHANGE TEXT TO / CHANGE WEIGHT TO / CHANGE CATEGORY TO / DELETE) so only changes get retyped; NEW criteria carry full text.
2. **RD:** verdict + one paragraph naming the evidence and where it is.
3. **AD1:** same.
4. **AD2:** same.

Rules:
- **Pass = it happened.** Positive criterion: Pass when the good thing is present. Negative criterion: Pass when the flaw is present. Never grade a negative criterion backwards.
- Judge each deliverable freshly. Do not copy a verdict or a paragraph across the three unless the evidence is genuinely identical, and even then name the location for each.
- Measure thresholds (duration, count, dimensions); do not eyeball.
- The justification must agree with the verdict above it. Re-read the pair before moving on.

Verdict justification template:
> [Pass/Fail]. [What was observed] at [location]. [How it relates to the criterion's value or threshold]. [One clause on impact if useful.]

---

## STEP 10 -- Alignment math (5 min) [Dims 14, 15]

Fill the worksheet Alignment block:

```
P            = sum of positive weights                     = ____
score(RD)    = sum of weights RD passes                    = ____   percent = ____ %  (must be >= 95)
score(AD1)   =                                             = ____   percent = ____ %
score(AD2)   =                                             = ____   percent = ____ %
```

Cross-check with the platform summary panel. Then compare with your ratings:
- RD rated ahead of AD1 (STEP 3 mostly 1-3) -> percent(RD) > percent(AD1).
- RD rated ahead of AD2 -> percent(RD) > percent(AD2).
- AD1 vs AD2 rating direction -> matches the sign of percent(AD2) - percent(AD1), with a margin proportional to how strong the rating was.

If anything disagrees, find the root cause before touching numbers: a weight in the wrong band, a criterion missing for something you praised or criticised, a wrong verdict (usually a backwards negative), or an over-extreme rating. Fix the cause, recompute.

If percent(RD) < 95: a criterion enforces something the brief never required, or an RD verdict is wrong. Fix; recompute.

**Order of work (ArchitectureReviewGuide.md steps 15-20):** click Next on the platform and read the scores; review every RD failure first (valid? weight right? rubric representing the task?); never inflate RD artificially; recheck any verdict whose justification reads the opposite way; revisit criteria that still feel subjective and make them observable or remove them; recompute; then compare with the initial ratings. If the rubric evidence genuinely supports a different conclusion than your first impression, revise the rating and its paragraph. Changing the rating on evidence is allowed; changing a weight to protect a rating is not.

---

## STEP 11 -- Closing QC on the Mac, then type, then reconcile (10 min) [Dim 17 + all]

1. Paste the CLOSING prompt (SessionPrompts.md section 3). It recomputes everything, fills the 17-row scorecard, fixes every non-[No Issues] row it can, and returns a CHANGE list, a CHECK ON PC list and the teleprompter package. If Claude Code is in use, it also runs `python tools/rubric_audit.py Tasks/<task-id>.md`.
2. Answer the CHECK ON PC items by looking at the PC; apply any resulting changes on the Mac.
3. Type the rubric phase into the PC once, from the teleprompter, in Outlier field order.
4. Click Next, photograph the score panel, send it to the Mac. Reconcile: RD failures first, no inflation. Apply final CHANGE lines on the PC.
5. Walk `PreSubmitChecklist.md` sections 8b and 9 as a last human pass. Submit only when all 17 read [No Issues].

---

## STEP 12 -- After submit (3 min)

Add an entry to `TaskLog.md`: task id, deliverable type, criteria count, RD/AD1/AD2 percents, gate answers, anything that surprised you, anything QC later flags. This is how the next task gets faster.

---

## Suggested time budget

| Stage | Share |
|---|---|
| STEP 0-2 brief + experience deliverables | 25% |
| STEP 3-6 three comparisons + gates | 15% |
| STEP 7-8 triage + coverage | 25% |
| STEP 9 verdicts + justifications | 25% |
| STEP 10-12 alignment + sweep + log | 10% |

Calibrate after your first two tasks and record actuals in TaskLog.md.

---

## REFERENCE -- Comparison justification template

```
[Dimension 1 name]: [AD/RD] [what it did] at [location]; [other deliverable] [what it did] at [location]. [Why a client cares].
[Dimension 2 name]: ...
[Dimension 3 name]: ...
[Dimension 4 name]: ...
[Dimension 5 name]: ... (or: Only one file was delivered, so multi-asset consistency does not apply.)
Overall [X] is [a little behind / ahead of / comparable to] [Y], and the gap is about [design / content / function / polish], not [the other].
```

## REFERENCE -- Criterion template

```
Text     : [One checkable statement. Exact value or named element. No "and", no list, no vague adjective.]
Category : [Requirements Compliance / Presentation & Aesthetics / Functionality / Content Correctness / Usability & Realism / Editability]
Weight   : [+8..10 must | +4..7 should | +1..3 preferable | -1..-3 minor flaw | -4..-7 serious defect | -8..-10 dealbreaker]
Source   : [R# / S# / F# / D# / professional standard / observed E#]
```

## REFERENCE -- Verdict justification template

```
[Pass/Fail]. [Observed fact] at [location]. [Relation to the criterion's value or threshold].
```

## REFERENCE -- Gate 1 "No" statement template

```
The brief is not sufficient to evaluate and compare the deliverables. Missing: [the unstated constraint / the absent input file named in the brief / the requirement that cannot be checked], which blocks judging [which requirement or dimension] for [RD / AD1 / AD2].
```

## REFERENCE -- Gate 2 "Yes" statement template

```
RD is worse than [AD1 / AD2]. On [dimension], RD [observed fact at location] while [ADx] [observed fact at location]. On [dimension], ... The brief asks for [requirement]; [ADx] meets it and RD does not. A client would prefer [ADx] because [impact].
```

---

## QUICK REFERENCE

| Item | Value |
|---|---|
| Scale | 1 RD sig. better / 2 RD better / 3 RD slightly / 4 comparable / 5 alt slightly / 6 alt better / 7 alt sig. better. AD1 vs AD2: 1 favours AD1, 7 favours AD2. |
| Dimensions | Realism; Design & UI/UX Quality; Professionalism; Coherence & Continuity; Multi-Asset Consistency |
| Gates | 1 brief sufficient? (No ends task) / 2 RD worse? (Yes ends task) |
| Categories | Requirements Compliance; Presentation & Aesthetics; Functionality; Content Correctness; Usability & Realism; Editability |
| Weights | +8..10 Critically Important / +4..7 Important / +1..3 Slightly Important / -1..-3 Slightly Detrimental / -4..-7 Detrimental / -8..-10 Critically Detrimental (architecture guide reads the bands as 8-10 / 5-7 / 5 or less; weight = impact of the criterion, not how noticeable it is) |
| Pass | It happened. Positive: good thing present. Negative: flaw present. |
| Count | 30+ (QC: 25-100) |
| RD sanity | percent(RD) >= 95 |
| Alignment | rubric totals must tell the same story as the 1-7 ratings |
| Every claim | needs a rubric |

*End of pipeline.*
