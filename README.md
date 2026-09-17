# Sardine Refiner -- Workflow Kit

> Everything needed to produce a 5/5 sardine_refiner task: the rulebook, the step-by-step pipeline, two AI orchestrators (coach and self-check evaluator), the P0 QC benchmark, writing guides, an error playbook, a per-task worksheet, a deterministic audit script and an annotated worked example. Built 2026-09-17 from the project course (34 slides) and the QC Spec Doc (17 dimensions). Read this file first, then pick a path.

---

## What the project is (60 seconds)

Each task gives you a client **brief** and three deliverables that answered it: **RD** (human reference), **AD1** and **AD2** (two model outputs). You:

1. **Understand the job**: open the Autoflation Link, read the brief, experience all three deliverables in full.
2. **Rate three comparisons**: RD vs AD1, RD vs AD2, AD1 vs AD2, on five dimensions (Realism; Design & UI/UX Quality; Professionalism; Coherence & Continuity; Multi-Asset Consistency), 1-7 scale, one evidence-located justification paragraph each. Then two gates: is the brief sufficient, is RD worse than either alternative.
3. **Audit the rubrics** (only if both gates pass): fix the AI-generated criteria (text, category, weight), add missing ones, delete nonsense, reach 30+, then give every criterion three verdicts (RD, AD1, AD2) with a justification each. **Pass = it happened**, for positive and negative criteria alike.

QC grades every task on **17 dimensions** (QualitySpecDoc.md). One [Fail] fails the task. One [Non-Fail] means not perfect. **The goal is 17 x [No Issues].**

---

## Quick start

**Two devices (Claude on the Mac, Outlier on the recorded PC)?** Use `SessionPrompts.md`: one-time setup (claude.ai Project or Claude Code), the OPENING prompt for every new chat, the CLOSING prompt for the self-QC and fix loop, the photo-in / teleprompter-out protocol, and the 15-row sequence across the two machines. The paths below are the underlying mechanics.

### Path A: a real task, coached step by step

Open a new chat (Cursor, Claude, ChatGPT) and paste:

```
Load these into context:
1. project_instructions.md
2. QualitySpecDoc.md
3. tasker_orchestrator.md
4. RubricWritingGuide.md and JustificationGuide.md (optional but recommended)
5. ArchitectureReviewGuide.md (when the task is architecture or interior design)

Then act as the Sardine Refiner Task Orchestrator. I'll say hi.
```

Say "hi". The orchestrator walks you through brief intake, evidence logging, three comparisons, gates, rubric triage, coverage to 30+, verdicts, alignment math and a 17-row pre-flight. It cannot see your deliverables, so it asks you for observations with locations and never invents evidence.

### Path B: self-check a draft before submitting

```
Load this file as your only context:
eval_orchestrator.md

Then act as the Sardine Refiner Eval Orchestrator. I'll say hi.
```

Paste your comparisons, gate answers, rubric table, verdicts or alignment numbers. It returns the exact QC labels ([Fail - ...] / [Non-Fail - ...] / [No Issues]) per dimension with fixes.

### Path C: no AI, just the checklist

Open `pipeline.md`, copy `TaskWorksheet_Template.md` to `Tasks/<task-id>.md`, follow STEP 0 to STEP 12. Before submit, run:

```
python tools/rubric_audit.py Tasks/<task-id>.md --pref-rd-ad1 <avg> --pref-rd-ad2 <avg> --pref-ad1-ad2 <avg>
```

and walk `PreSubmitChecklist.md`.

---

## Folder map

```
Sardine-Refiner/
|
|-- README.md                      <- you are here
|-- SessionPrompts.md              <- OPENING prompt, CLOSING prompt (self-QC + fix loop), micro-prompts,
|                                     two-device protocol (photo in, teleprompter out), task sequence
|-- project_instructions.md        <- single source of truth (rules, taxonomies, workflow, scoring, glossary)
|-- QualitySpecDoc.md              <- P0: the 17 QC dimensions verbatim + recipe for [No Issues] on each + scorecard
|-- pipeline.md                    <- invoke at the start of every task; STEP 0-12 with QC dimension tags; templates
|
|-- tasker_orchestrator.md         <- AI coach system prompt (phase-gated walkthrough of one task)
|-- eval_orchestrator.md           <- AI self-check evaluator (self-contained; emits QC labels verbatim)
|
|-- RubricWritingGuide.md          <- criterion tests, phrasing patterns, vague-word table, splitting, category and
|                                     weight decision trees, deliverable-type libraries, 30-criterion poster example
|-- ArchitectureReviewGuide.md     <- domain layer from the Architecture / Interior Design guide: five quality checks,
|                                     reference-file authority, exact vs approximate, overlap borderline cases,
|                                     subjectivity decomposition, weight rules, 22-step review workflow, arch library
|-- JustificationGuide.md          <- comparison and verdict justification shapes, templates, location conventions
|-- CommonErrors.md                <- 38 numbered errors with BAD / GOOD / tips, mapped to QC dimensions
|-- PreSubmitChecklist.md          <- red-flag sweep in pipeline order + 17-row scorecard
|
|-- TaskWorksheet_Template.md      <- per-task fill file (brief extraction, evidence ledger, ratings, gates, triage,
|                                     coverage matrix, FINAL RUBRIC table, alignment, scorecard)
|-- TaskLog.md                     <- CRITICAL RULES block + per-task post-mortems
|
|-- examples/
|   |-- debussy_worked_example.md  <- the course example, annotated, negatives corrected to the current pass rule,
|                                     score math, and an expansion to 30 criteria
|-- tools/
|   |-- rubric_audit.py            <- deterministic self-audit of the worksheet (count, weights, categories, atomicity,
|                                     vague words, duplicates, RD >= 95%, alignment vs ratings)
|-- Tasks/                         <- one worksheet per task
|-- Sardine-refine sources/        <- original course photos + QC Spec Doc PDF (do not edit)
```

---

## The rules that decide most tasks

| Rule | Why |
|---|---|
| RD, AD1, AD2 are never mixed up | One swapped label invalidates the whole submission |
| Pass = it happened, for both signs | Negative criteria were being graded backwards; the course changed the rule. Backwards negatives hit Dims 12, 14 and 15 at once |
| Every claim in a justification needs a rubric | Checked closely; praise or criticise something, and a criterion must grade it |
| 30+ atomic, self-contained criteria (QC: 25-100) | Split on "and", lists, slashes; exact brief values; no vague adjectives |
| RD is a bar, not a template | "At least as good as RD" for quality; never enforce a random RD choice |
| RD must score 95%+ | If not, a criterion is arbitrary, an RD verdict is wrong, or a negative is backwards |
| Gates are honest and end the task | Insufficient brief: Gate 1 No + gap statement. RD worse: Gate 2 Yes + explanation. Both are complete tasks |
| Every justification has a location | Timestamp, page, screen, region, file, cell |
| Totals must tell the same story as the ratings | Fix at the root; never tune a weight to move a total |

---

## A typical task, start to finish

1. Open the Autoflation Link. Copy the worksheet template. Extract the brief into R#/S#/F#/D# rows with must / should / preferable tags.
2. Experience RD, AD1, AD2 completely. Log every observation with a location.
3. Rate RD vs AD1, RD vs AD2 (independently), AD1 vs AD2 (1 favours AD1, 7 favours AD2). Write three paragraphs: dimension, evidence, location, comparison, client impact, direction and cause.
4. Answer the gates from evidence. If either ends the task, write the statement and submit.
5. Triage every synthetic criterion: keep / edit / split / delete, with a reason.
6. Build the coverage matrix (explicit, implicit, expert, observed failures, justification claims). Add criteria until every row is covered and the count is 30+.
7. Grade every criterion three times with located paragraphs. Say "Pass = it happened" before each negative.
8. Compute P and the RD / AD1 / AD2 percents. RD >= 95. Direction matches ratings. Fix root causes.
9. Run the audit script, walk the checklist, fill the 17-row scorecard. Submit.
10. Log the task in TaskLog.md.

Suggested budget (calibrate after two tasks): 25% brief and experience, 15% comparisons and gates, 25% triage and coverage, 25% verdicts, 10% alignment and sweep.

---

## Common mistakes (top ten)

| Mistake | Fix |
|---|---|
| "A is better" justification | Dimension, located evidence, comparison, client impact |
| Rating from the first 20 seconds | Play, run, open, scroll everything first |
| Trusting the synthetic rubrics | Triage every card; delete nonsense; fill gaps |
| "and" in a criterion | Split |
| "appropriate", "proper", "good" | Replace with the brief's value or a named element |
| Enforcing RD's arbitrary choice | "At least as good as RD" or lenient alternatives |
| Negative criterion passed because the flaw was avoided | Pass = flaw present |
| Copying one verdict across RD/AD1/AD2 | Judge fresh, locate each |
| Praising something with no rubric for it | Add the criterion |
| Nudging a weight to fix alignment | Find the backwards negative, arbitrary criterion, missing criterion, band error or over-extreme rating |

Full catalog: `CommonErrors.md`.

---

## FAQ

**Do I have to fill the worksheet?** No, but it is the fastest way to keep RD/AD1/AD2 straight, keep locations, and feed the audit script. Paste from it into the platform.

**What if a rating dimension does not apply (single file, so no multi-asset consistency)?** State N/A in the paragraph. The kit's working assumption is to enter 4 for the required field; confirm with your QM.

**How is the rubric score computed?** Working model: score = sum of weights of criteria the deliverable passes (negative passes subtract); percent = score / sum of positive weights. Confirm against the platform's summary panel on your first tasks.

**Can the AI orchestrator grade the deliverables for me?** No. It cannot see them. It structures your observations, drafts wording, checks rules and arithmetic. Verdicts come from what you saw.

**The course worked example grades negatives as Pass when the flaw is absent. Which is right?** The course's later slide "why this changed" is right: Pass = the flaw happened. See `examples/debussy_worked_example.md` for the corrected rows and the score impact.

**What do I read if I only have 15 minutes?** `project_instructions.md` section 0 (TL;DR) and `QualitySpecDoc.md` section 2 (threshold table).

---

## Sources and change log

| Date | Change |
|---|---|
| 2026-09-17 | Initial kit from the course slides (34 photos) and QC Spec Doc (17 dimensions). Assumptions flagged in project_instructions.md section 13.2. |
| 2026-09-17 | Added ArchitectureReviewGuide.md from "Architectural workflow.pdf" (25 pages) and folded its rules into pipeline, QualitySpecDoc, RubricWritingGuide, CommonErrors (Part 6), PreSubmitChecklist, worksheet, TaskLog rules 13-15 and both orchestrators. Weight-band discrepancy (course 8-10/4-7/1-3 vs guide 8-10/5-7/5 or less) flagged in project_instructions section 13.2. |

*When in doubt, the Autoflation Link and QualitySpecDoc.md win.*
