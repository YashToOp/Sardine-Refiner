# Sardine Refiner -- Architecture / Interior Design Review Guide

> **Updated:** 2026-09-17 -- Consolidated from "Architectural workflow.pdf" (Sardine Refiner Review & Rubric Quality Guide, Architecture / Interior Design, 25 pages). This is the domain layer on top of pipeline.md and QualitySpecDoc.md: the five rubric quality checks with architecture examples, the relevance and weight rules, the 8-question checklist and the 22-step suggested review workflow. Section 9 (deliverable library) is the kit's own addition and is marked as such.

**Core objective (from the guide):** the brief, relevant inputs, outputs, rubric coverage, justifications, PASS/FAIL decisions, pairwise comparison and final scores should all support the same overall evaluation. The same task is checked from several different directions before submission.

---

## 1. The five rubric quality checks

| # | Check | Rule |
|---|---|---|
| 1 | Coverage | Everything important in the task must be evaluable, including the brief, relevant input information, and supported professional expectations. |
| 2 | Overlap | One independent error should not be rewarded or penalised more than once because the same issue appears in multiple criteria. |
| 3 | Subjectivity | Broad quality language is translated into observable evidence instead of being ignored or graded only by taste. |
| 4 | Atomicity | Each criterion evaluates one clear requirement or one independent failure mode whenever possible. |
| 5 | Self-Containment | A reviewer can understand and grade the criterion without guessing what it means or relying on hidden assumptions. |

---

## 2. Coverage

Coverage is broader than copying the brief into rubrics.

**Direct-reference rule.** If the brief says to follow, preserve, reproduce or apply a provided file directly, the important information in that file becomes part of the expected task scope and should be represented in the rubric set.

**Specific-reference rule.** If the brief uses an input only for a defined purpose (dimensions, layout, openings, material reference, site context), coverage focuses primarily on those referenced elements rather than every detail in the file.

**Professional judgment.** Input files can contain task-critical information not repeated word-for-word in the brief. If a detail materially affects correctness, function, safety, coordination or the ability to deliver the intended work, it may need rubric coverage. Do not promote incidental, legacy or unrelated file content into mandatory criteria without support.

### 2.1 How strongly does the brief bind the task to the reference file?

| Case | Brief wording | Coverage consequence |
|---|---|---|
| Exact file authority | "Follow the provided DWG exactly." | Major footprint, wall layout, openings, circulation cores, levels and other important DWG-defined geometry may each need separate rubric coverage. |
| Limited file authority | "Use the DWG only for room dimensions." | Do not automatically turn unrelated doors, furniture, materials, annotations or legacy geometry into mandatory requirements. |

**Coverage test:** can every important requirement from the brief, the relevant input files and the professional or domain expectations be evaluated somewhere in the final rubric set?

### 2.2 Exact vs approximate

Do not silently convert flexible language into an exact requirement.

| Case | Brief wording | How to write the criterion |
|---|---|---|
| Exact numeric requirement | "The ceiling height is 300 cm." | Treat 300 cm as a defined requirement and check the stated value directly, allowing only the measurement or file precision genuinely supported by the source. |
| Approximate numeric requirement | "The ceiling height is approximately 300 cm." | Do not convert "approximately" into an exact 300 cm rule. Evaluate reasonable alignment with the intended scale; use a numeric tolerance only when the brief, input or documented project convention supports it. |

Exact language defines a specific target. Approximate language defines an intended range or scale. The rubric preserves that distinction.

---

## 3. Overlap

Different criteria evaluate different failure modes, not the same error in different words.

**Fast overlap test:** if this specific error occurs, how many criteria would fail because of exactly the same mistake? If several would fail for the same underlying issue, narrow, merge or rewrite them.

**Good separation:** separate criteria when the conditions can fail independently and each failure has a distinct effect on task quality or compliance.

**Overlap risk:** a detailed criterion already checks a wall mismatch, and a broader "the model matches the DWG" criterion fails again because of that same wall mismatch.

**Practical rule:** one criterion per meaningful failure mode. Broad consistency checks are allowed only when they evaluate a genuinely different level of information.

### 3.1 Borderline case 1: macro-level consistency

A render-model consistency criterion can be useful because multiple deliverables should represent the same overall proposal. The risk is using it to re-penalise every wall, opening or material mismatch that already has its own detailed criterion.

- SAFE: use the macro criterion to ask whether the render and model represent the same overall proposal, design version or architectural concept.
- DO NOT DOUBLE-PENALISE: do not fail the macro criterion merely because one window, one wall or one opening already failed a dedicated detailed criterion.
- FAIL THE MACRO CRITERION when the inconsistency is broad enough that the assets no longer represent the same overall proposal: materially different massing, layout logic, facade concept or project version.
- WEIGHT CAREFULLY: a macro criterion should not become a second heavy penalty for a collection of detailed errors unless the combined inconsistency itself creates a separate, meaningful failure.

**Decision rule:** an isolated mismatch belongs to the detailed criterion. A proposal-level contradiction belongs to the macro consistency criterion.

### 3.2 Borderline case 2: reference detail or requirement?

Architecture files often contain legacy geometry, alternate options, annotations, furniture, site context or details that explain the project but are not requirements for the current task.

- Brief says follow or preserve the reference: important reference-defined geometry and organisation may become mandatory.
- Brief says use the file only for a specific purpose: keep the rubric tied to that purpose.
- Brief explicitly selects certain information from the file: treat those elements as direct coverage.
- Brief is ambiguous: use professional judgment only for details that materially affect the intended result, correctness, coordination or usability.
- Never turn incidental annotations, old alternatives, decorative content or unrelated file information into requirements without support.

**Decision rule:** would the task materially change if this reference detail were different? If not, it is context, not a rubric requirement.

---

## 4. Subjectivity

Subjective requirements still need coverage: translate them into observable evidence. Words such as photorealistic, realistic, refined, high-quality, well-proportioned or visually convincing are task requirements when the brief uses them. Do not ignore them; decompose them.

**Example: "photorealistic rendering" breaks into**
- lighting quality and believable light behaviour
- architectural scale, proportion and spatial relationships
- material realism and surface response
- reflections and shadows
- realism of secondary elements where relevant (vegetation, people, vehicles, furnishings)
- visible geometry, texture, exposure or rendering defects

Each bullet is its own criterion, phrased so a reviewer can point to evidence in the render.

---

## 5. Atomicity

Atomicity prevents both over-penalisation and under-penalisation.

**Why a generic DWG check under-penalises:** "The model matches the reference DWG" hides several independent major errors inside one PASS/FAIL. If footprint, wall layout, opening positions, circulation core and level organisation are all wrong, AD1 or AD2 receives one penalty for several major reference failures.

**Better:** separate independent DWG-defined failure modes when they can fail independently: footprint, exterior wall alignment, residential partitions, retail divisions, openings, vertical circulation, levels, site placement, only where each is relevant.

**Avoid over-atomisation.** Atomic does not mean splitting every adjective or dependent detail into a separate rubric. If several elements are meaningful only as one requested relationship or combination, evaluate the combination as a whole. Example: "The colour palette is focused on cool blue, indigo and dark navy tones" is one combined-palette requirement, not three colour-existence criteria, unless the task makes those colours independently mandatory.

**Practical rule:** split independent failure modes; keep dependent details together when separating them would distort what the brief asks for.

---

## 6. Self-containment

- **Specific:** avoid "high resolution", "sufficient detail", "appropriate scale" unless the criterion says what the reviewer should look for.
- **Independent:** no criterion depends on another rubric number or hidden context; name the element and the expected condition directly.
- **Supported:** a criterion may rely on the brief, input files, Golden Output (RD) or domain-specific professional expectations, never on undeclared external assumptions.
- **Consistent verdict:** the target is that different reviewers reach the same PASS/FAIL as often as possible.

---

## 7. Relevance and weight

**Relevance test:** would the quality, correctness or compliance of the deliverable meaningfully change depending on whether this criterion passes or fails? If not, reconsider whether it belongs in the set.

| Weight | Level (this guide) | Examples |
|---|---|---|
| 8 to 10 | Most significant | Critical deliverables, required file types, major required elements, openability, other failures that strongly affect whether the task is usable or correct |
| 5 to 7 | Important | Meaningful requirements and details: specific geometry, colours, realism, shapes, task-specific design conditions |
| 5 or less | Minor / primarily aesthetic | Lower-impact details that affect polish but do not determine whether the task is fundamentally correct or usable |

**Band discrepancy to know about.** The project course defines the positive bands as 8-10 Critically Important, 4-7 Important, 1-3 Slightly Important. This guide describes 8-10, 5-7 and 5 or less. Both agree on 8-10. Weight 4 and 5 sit in the overlap. The kit keeps the course bands as the platform rule and uses this guide's descriptions to pick within a band; confirm with your QM if a QC result turns on a 4 or 5.

**Weight check:** the weight reflects the impact of the criterion itself, not how easy the issue is to notice or how strongly you personally feel about it.

**Rubric count:** the minimum is a floor, not a target. Complex architecture tasks may legitimately need many more criteria when independent failure modes require separate coverage (QC ceiling stays at 100).

---

## 8. Initial pairwise evaluation (the five dimensions, architecture reading)

Build an independent first impression before the final rubric set.

| # | Dimension | Architecture reading |
|---|---|---|
| 1 | Realism | How believable and professionally produced the deliverable feels. |
| 2 | Design and UI/UX Quality | Overall design craft, composition, visual quality, and usability where applicable. |
| 3 | Professionalism | Polished, free of significant errors or artifacts, ready for the intended client review. |
| 4 | Coherence and Continuity | Internally consistent and logically structured, without contradictions. |
| 5 | Multi-Asset Consistency | The delivered assets and components (model, renders, plans, material boards) share a consistent proposal, style and quality level. |

**Important:** the initial assessment can change after the rubric evidence is complete. The final preference ranking and final rubric scores should tell a consistent story. Revising an earlier rating because the rubric evidence supports a different conclusion is allowed and expected; tuning weights to protect an earlier rating is not.

---

## 9. Architecture / interior deliverable library (kit addition, not from the guide)

Use with RubricWritingGuide.md section 9 (expansion ladder). Rewrite in the brief's exact terms; keep only what the brief, inputs or professional judgment support.

**Package and files**
- Every requested deliverable file is present (3D model, renders, plans, sections, elevations, material board) in the requested format
- Each file opens without errors in the stated tool; no missing references, textures or linked files
- The model file is the current version (no outdated or duplicate versions left in the package unless the brief asks for options)
- Units and scale match the brief or the reference file
- Layers, groups or components are named and organised (Editability)
- Geometry is not merged into a single flattened object when a working model was requested (Editability)

**Reference-file compliance (only to the extent the brief binds the task to the file)**
- Building footprint matches the reference within the supported precision
- Exterior wall alignment matches the reference
- Interior partitions match the reference (residential, retail, service zones as relevant)
- Door and window openings are in the referenced positions and sizes
- Vertical circulation (stairs, lifts, cores) is in the referenced position
- Level count and level heights match the reference
- Site placement and orientation match the reference
- Room dimensions match the reference (when the brief limits authority to dimensions)

**Explicit design requirements**
- Stated dimensions (ceiling height, room sizes, spans) match: exact when stated exactly, reasonable alignment when stated approximately
- Requested materials and finishes appear where specified
- Requested palette is present as the combined palette the brief describes
- Requested furniture, fixtures or equipment are present and placed as described
- Requested style, era or concept is legible in the result

**Render realism (decomposed)**
- Lighting is believable for the stated time of day and light sources
- Scale and proportion of spaces, openings and furniture are correct
- Materials respond to light plausibly (reflection, roughness, texture scale)
- Shadows and reflections are consistent with the light setup
- Secondary elements (vegetation, people, vehicles, props) are realistic where present
- No visible geometry gaps, z-fighting, texture stretching, exposure blowouts or noise artifacts
- Camera views match the requested views and framing

**Coordination and coherence**
- Renders represent the same overall proposal as the model (macro criterion; never a second penalty for a single detailed mismatch)
- Plans, sections and elevations agree with the model
- Material board matches the materials used in the model and renders
- Annotations and dimensions in drawings are consistent with the geometry

**Function and usability**
- Circulation is continuous (doors open, corridors connect, stairs land on floors)
- Openings are placed usably (no window behind a full-height cabinet unless designed)
- Clearances plausible for the room's use where the brief or standards require it

**Typical negatives (Pass = the flaw is present)**
- The package contains an outdated or duplicate model version presented as current
- The model contains merged geometry that prevents component-level editing
- The render contains a visible rendering artifact (gap, z-fighting, texture stretching)
- A reference-defined opening is missing from the model
- A deliverable file fails to open in the stated tool

---

## 10. Checklist before submission (the guide's eight questions)

If any answer is NO, revise before submitting.

1. Is every criterion atomic?
2. Is every criterion self-contained?
3. Is every criterion relevant?
4. Is everything important covered in the rubrics?
5. Are the rubrics free of duplicates and unnecessary overlap?
6. Is every criterion easy to understand?
7. Do PASS/FAIL verdicts match their justifications?
8. Do the final scores align with the final pairwise ratings and justification?

---

## 11. Suggested review workflow (22 steps, from the guide)

Mapped to pipeline.md steps in brackets.

**Part 1: validate the task package** [pipeline STEP 1-2]
1. Read the brief first. Check the input file referenced in the brief. Confirm the actual input matches what the brief describes and decide whether any mismatch prevents reliable completion or evaluation.
2. Check the Golden Output (RD) against the brief and inputs. Could RD realistically have been produced from this brief and these inputs? Use domain judgment; focus on meaningful reference or alignment problems.
3. Check for extra or outdated Golden Output files. Decide whether extra files affect the task; identify which model or renders represent the current version; ignore or remove legacy files when appropriate.
4. Check the required AD1 / AD2 file formats. If the requested format does not work, check whether another usable editable file exists. If no reliable evaluation source remains, the package may be insufficient (Gate 1).

**Part 2: initial comparison and rubric build** [STEP 3-7]
5. Complete the initial pairwise evaluations: RD vs AD1, RD vs AD2, AD1 vs AD2, before building the final rubric set.
6. Check whether RD is really the best option. If RD does not outperform the alternatives, reconsider the initial judgment. Evidence-based; no subjective preference.
7. Copy the synthetic rubrics into a blank document. Keep the synthetic set visible as a reference rather than editing it blindly in place.
8. Build your own simple rubric outline first, from the brief and inputs, in category order: Requirements Compliance, Content Correctness, Functionality, Usability & Realism, Presentation & Aesthetics, Editability.

**Part 3: finalise the rubric set and evaluation sources** [STEP 7-8]
9. Compare your rubrics with the synthetic set. Identify missing coverage in both directions; the two sets check each other.
10. Create the final rubric set. Close important coverage gaps, remove unnecessary overlap, keep criteria objective, atomic, relevant and self-contained.
11. Enter the final set into the task, in the category order above.
12. Add the correct evaluation source where needed: 3D model, render, plan, DWG, PDF, material presentation. This prevents model/render conflicts.

**Part 4: justifications and first score check** [STEP 9-10]
13. Start writing the justifications. Keep initial PASS/FAIL observations in a separate document so findings are not lost while editing the rubric set.
14. Flag subjective justifications. If a judgment feels subjective, flag it and return later; rewrite the criterion or justification around observable evidence.
15. Run the first score check. Once the rubric set is complete, click Next and inspect the scores. If RD is unexpectedly low, investigate before continuing.
16. Review RD failures first. Check whether each RD failure is valid, whether the weight is appropriate, and whether the rubric set represents the task correctly. Do not inflate RD artificially.

**Part 5: validate verdicts and reconcile** [STEP 10]
17. Check PASS/FAIL consistency. Every justification matches its score; negative justification + PASS or positive justification + FAIL triggers a recheck.
18. Revisit subjective criteria. Make them more objective; if a criterion cannot be defended objectively and is not supported by the task, remove it.
19. Run the score check again after all revisions.
20. Compare the final scores with the initial evaluation (RD vs AD1, RD vs AD2, AD1 vs AD2). They should tell a consistent story. Revise the earlier judgment if the rubric evidence supports a different conclusion.

**Part 6: final uncertainty check** [STEP 11]
21. Recheck everything you are still unsure about. Return to any criterion, file, justification or comparison where doubts remain.
22. Submit only when the task feels internally consistent: brief, inputs, outputs, rubric coverage, justifications, PASS/FAIL decisions, pairwise comparison and final scores support the same overall evaluation.

---

*End of Architecture / Interior Design Review Guide.*
