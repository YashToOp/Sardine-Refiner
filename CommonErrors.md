# Sardine Refiner -- Common Errors Playbook

> **Updated:** 2026-09-17 -- Initial build from the course ("the most common mistake", "rubric pointers from recent audits", "why this changed") and the 17 QC dimensions. Each error: what it is, why it matters (which QC dimension it hits), a BAD example, a GOOD pattern, tips.

## Mental model: where a task breaks

| Part | Where the defect is introduced | When you catch it |
|---|---|---|
| Part 1 - Setup and comparison | Reading the brief, experiencing deliverables, rating, gates | STEP 1-6 of pipeline.md |
| Part 2 - Criterion content | A single criterion's text, category or weight | STEP 7-8 |
| Part 3 - Rubric set composition | The set as a whole: count, coverage, overlap, depth | STEP 8 |
| Part 4 - Verdicts and justifications | Pass/Fail calls and the paragraphs under them | STEP 9 |
| Part 5 - Alignment and hygiene | Totals vs ratings, RD sanity, proofreading | STEP 10-11 |

---

## Index

**Part 1 - Setup and comparison**
1. Mixing up RD, AD1 and AD2
2. Rating before experiencing the deliverable in full
3. Assuming the human reference is best
4. Generic comparison justification
5. Justification skips a dimension
6. Extreme ratings without located evidence
7. Anchoring RD vs AD2 on RD vs AD1
8. Proceeding on an insufficient brief

**Part 2 - Criterion content**
9. Trusting synthetic rubrics as truth
10. Compound criterion ("and", lists)
11. Vague or not self-contained criterion
12. Generalised instead of the brief's exact value
13. Enforcing RD's arbitrary choice
14. Undeclared region assumption
15. Irrelevant or unsourced criterion
16. Wrong category
17. Weight band misjudged
18. "Avoids X" with a negative weight
19. AI-sounding criterion text

**Part 3 - Rubric set composition**
20. Duplicate criteria
21. Overlapping criteria
22. Explicit requirement uncovered
23. Implicit expectations and expert nuances missing
24. Aesthetics graded as one lump
25. Functionality never actually run
26. Content never recalculated
27. Editability ignored
28. Fewer than 30 (or more than 100) criteria
29. Set skewed to one category

**Part 4 - Verdicts and justifications**
30. Negative criterion graded backwards
31. Verdict copied across the three deliverables
32. Justification contradicts its verdict
33. Justification without a location
34. Claim in a comparison justification with no rubric behind it

**Part 5 - Alignment and hygiene**
35. RD scores under 95%
36. Preference direction contradicts rubric totals
37. Tuning numbers to force the story
38. Unlisted minor errors (typos, signs, labels)

**Part 6 - Reference files, subjectivity and package (from the architecture guide)**
39. Converting "approximately" into an exact rule
40. Promoting incidental or legacy file content into requirements
41. Ignoring a subjective brief term instead of decomposing it
42. Macro consistency criterion double-penalising a detailed mismatch
43. Over-atomising a dependent combination
44. Generic "matches the reference" criterion hiding several failures
45. Missing evaluation source on a multi-asset package
46. Skipping package validation (golden output, extra files, formats)
47. Inflating RD when reviewing its failures

---

## Part 1 - Setup and comparison

### Error 1: Mixing up RD, AD1 and AD2

**What it is:** a rating, justification or verdict refers to the wrong deliverable.
**Why it matters:** the course says it invalidates the whole submission. Every QC dimension inherits the mistake.
**BAD:** the AD1 vs AD2 paragraph praises "the reference's cleaner mix".
**GOOD:** worksheet rows are labelled; each paragraph starts with the label it is about; the AD1 vs AD2 paragraph never mentions RD except as the brief's bar.
**Tips:** write the three labels at the top of the worksheet; re-read the panel header before each rating; search your final text for "reference", "human", "model" and replace with labels.

### Error 2: Rating before experiencing the deliverable in full

**What it is:** scoring from a thumbnail, the first 20 seconds, or the first page.
**Why it matters:** Dim 1 (your ratings diverge from the auditor's), Dim 12 (verdicts wrong on things you never saw).
**BAD:** "Coherence 4" for a video whose last scene repeats the first, which you never watched.
**GOOD:** Evidence Ledger has entries across the whole duration or page range before any rating is entered.
**Tips:** play to the end; run every control; open every file; log a location for each observation.

### Error 3: Assuming the human reference is best

**What it is:** answering Gate 2 "No" or rating RD ahead out of deference.
**Why it matters:** Dim 1 and Dim 14 (your story is wrong); the course says models sometimes win and you must say so.
**BAD:** RD's audio clips at three points and AD2 is clean, but RD vs AD2 is rated 3 on Professionalism.
**GOOD:** RD vs AD2 Professionalism 5 with the three clipping timestamps named; Gate 2 considered honestly.
**Tips:** rate from evidence; if an alternative wins overall, answer Gate 2 Yes and explain.

### Error 4: Generic comparison justification

**What it is:** "A is better", "AD1 looks unprofessional", "both fine, gave it a 4".
**Why it matters:** Dim 2 Fail. Also removes your defence on Dim 1.
**BAD:** "Design is bad, colours are off."
**GOOD:** "Design & UI/UX: three scenes reuse the same layout, and the labels at 0:22 and 0:41 are unreadable against the green background; RD varies layout per scene and keeps labels on a dark band. A client would notice the repetition in a 60-second spot."
**Tips:** dimension, evidence, location, comparison, client impact. Use the template in JustificationGuide.md.

### Error 5: Justification skips a dimension

**What it is:** the paragraph covers design and content but never mentions realism or continuity.
**Why it matters:** Dim 2 Non-Fail ("did not address all the issues").
**BAD:** a 60-word paragraph about colours only.
**GOOD:** all five named, with "does not apply" stated for a single-file deliverable's multi-asset consistency.
**Tips:** count the dimension names before you paste.

### Error 6: Extreme ratings without located evidence

**What it is:** a 1, 2, 6 or 7 backed by an impression.
**Why it matters:** Dim 1 Fail is defined by extremes that the auditor sees differently.
**BAD:** "Realism 1" with "the reference just feels more real".
**GOOD:** "Realism 2: AD1's piano is an obviously synthetic patch (compare the sustain at 0:48 with RD's natural decay); AD1's reverb tail cuts at 1:10." Two located facts.
**Tips:** two located facts per extreme, or move toward the middle.

### Error 7: Anchoring RD vs AD2 on RD vs AD1

**What it is:** rating AD2 relative to AD1 instead of relative to RD.
**Why it matters:** Dim 1 (wrong numbers), Dim 14 (story inconsistent).
**BAD:** AD2 is slightly better than AD1, so it gets RD vs AD2 = 5 even though RD still beats it.
**GOOD:** RD vs AD2 judged fresh: 3. Then AD1 vs AD2 head to head: 5.
**Tips:** finish the RD vs AD1 block, clear your head, restart from the Evidence Ledger for AD2.

### Error 8: Proceeding on an insufficient brief

**What it is:** a referenced input file is missing or a requirement cannot be checked, and you answer Gate 1 Yes anyway.
**Why it matters:** Dim 16 Fail.
**BAD:** the brief says "use the palette in brand.pdf", no brand.pdf is attached, and you grade palette compliance by guessing.
**GOOD:** Gate 1 No: "Missing: brand.pdf referenced in Requirements; palette compliance cannot be judged for RD, AD1 or AD2."
**Tips:** run the sufficiency test in STEP 1 before you rate.

---

## Part 2 - Criterion content

### Error 9: Trusting synthetic rubrics as truth

**What it is:** leaving AI-generated criteria untouched.
**Why it matters:** the course makes editing an obligation; Dims 5-11 all suffer.
**BAD:** 22 synthetic criteria submitted as-is.
**GOOD:** every card triaged (keep / edit / delete) with a reason; gaps filled; count at 30+.
**Tips:** STEP 7 nine questions per card.

### Error 10: Compound criterion ("and", lists)

**What it is:** one card checks two or more things.
**Why it matters:** Dim 9. Also hides partial failures (a deliverable that does two of three gets an all-or-nothing verdict).
**BAD:** "A complete, playable full track is delivered in MP3 format and runs approximately two minutes."
**GOOD:** three criteria: complete playable file / MP3 format / duration approximately two minutes.
**Tips:** search your criteria for " and ", ", ", "/", "including".

### Error 11: Vague or not self-contained criterion

**What it is:** a grader could not decide Pass/Fail without asking you what you meant.
**Why it matters:** Dim 10.
**BAD:** "The logo is placed appropriately."
**GOOD:** "The logo appears in the top-left zone defined in layout.ai."
**Tips:** replace appropriate / proper / good / clean / suitable / reasonable / correctly / well with a value, threshold or named element.

### Error 12: Generalised instead of the brief's exact value

**What it is:** rounding the brief's requirement into a softer one.
**Why it matters:** Dim 10 and the audit pointer "Accuracy to the Brief".
**BAD:** "The composition is of a suitable length." (brief says 2 to 4 minutes)
**GOOD:** "The composition runs between 2:00 and 4:00."
**Tips:** copy values from the brief verbatim into the criterion.

### Error 13: Enforcing RD's arbitrary choice

**What it is:** turning something RD happened to do into a requirement.
**Why it matters:** Dim 5. Also drags AD scores down for no client reason.
**BAD:** "The poster uses a 12 mm corner radius on the image frame." (RD did; brief silent)
**GOOD:** "Image framing is at least as consistent as RD." or drop the criterion.
**Tips:** ask "did the brief mandate this?" If not, comparative or lenient phrasing, or delete.

### Error 14: Undeclared region assumption

**What it is:** grading on a locale convention the brief never stated.
**Why it matters:** Dim 8.
**BAD:** "Dates use MM/DD/YYYY format."
**GOOD:** "Dates use one consistent format throughout." (or delete if the brief is silent)
**Tips:** watch dates, units, currency, spelling variant, paper size, regulations.

### Error 15: Irrelevant or unsourced criterion

**What it is:** a criterion no line of the brief, no input file, no professional standard and no observed failure supports.
**Why it matters:** Dim 8.
**BAD:** "The track includes a vocal hook." (instrumental brief)
**GOOD:** deleted, with the reason logged in the triage table.
**Tips:** every criterion gets a Source column entry; blank means delete.

### Error 16: Wrong category

**What it is:** a Requirements Compliance check filed under Presentation, or an editability check under Functionality.
**Why it matters:** audit pointer "Format & Categories"; Dim 17.
**BAD:** "Source file has separate layers" under Presentation & Aesthetics.
**GOOD:** under Editability.
**Tips:** category decision tree in RubricWritingGuide.md section 5.

### Error 17: Weight band misjudged

**What it is:** a "must" at +3, or a "preferable" at +10, or a minor flaw at -9.
**Why it matters:** Dim 4, counted on the criteria AD1 or AD2 fail.
**BAD:** "The recording contains solo piano only" (brief: must) weighted 3.
**GOOD:** weighted 10. "Preferable to begin in C major" weighted 6, not 10.
**Tips:** map the brief's word to the band; keep siblings equal; re-check every AD-failed criterion.

### Error 18: "Avoids X" with a negative weight

**What it is:** a criterion phrased as the good behaviour but weighted negative, so Pass (it happened) subtracts points from a clean deliverable.
**Why it matters:** Dim 12, Dim 15 (RD gets penalised for being clean).
**BAD:** "The audio avoids clipping." weight -7.
**GOOD:** either "The audio is free of audible clipping." weight +7, or "The audio contains audible clipping." weight -7.
**Tips:** negative weight = the text describes the flaw happening.

### Error 19: AI-sounding criterion text

**What it is:** stacked adjectives and filler that no human would write on a checklist.
**Why it matters:** the course asks you to rewrite unnatural text; Dim 17.
**BAD:** "Ensure that the deliverable effectively leverages a cohesive and visually compelling colour strategy."
**GOOD:** "The palette matches the hex values in brand.pdf."
**Tips:** if it has "ensure", "effectively", "seamlessly", "robust", "compelling", rewrite.

---

## Part 3 - Rubric set composition

### Error 20: Duplicate criteria

**What it is:** same test, different wording.
**Why it matters:** Dim 6 (two or more = Fail).
**BAD:** "The track is in MP3 format." and "An MP3 file is delivered."
**GOOD:** one criterion.
**Tips:** sort the list alphabetically and by category; run tools/rubric_audit.py for similarity pairs.

### Error 21: Overlapping criteria

**What it is:** a criterion bundles a property already scored elsewhere.
**Why it matters:** Dim 6.
**BAD:** "The poster is print-ready (bleed, CMYK, embedded fonts)." alongside separate bleed, CMYK and fonts criteria.
**GOOD:** keep the three atomic ones; delete the bundle.
**Tips:** after splitting, check whether the parent still exists.

### Error 22: Explicit requirement uncovered

**What it is:** a line in the brief has no criterion.
**Why it matters:** Dim 7 (>=10% of count missing = Fail).
**BAD:** brief requires six script steps; rubric checks only "script is followed".
**GOOD:** one criterion per step present, one for order, one for wording.
**Tips:** coverage matrix rows R1..Rn each point to a criterion ID.

### Error 23: Implicit expectations and expert nuances missing

**What it is:** the set checks only what the brief spells out.
**Why it matters:** Dim 7 ("too high-level", "misses the elements professionals care about") and the course rule "if an expert would call it a mistake, write a rubric for it".
**BAD:** an audio rubric with no clipping, tempo, timbre or silence criteria.
**GOOD:** implicit expectations and nuances from the RubricWritingGuide.md library for the deliverable type.
**Tips:** ask "why do I actually prefer this one?" and write each answer down as a criterion.

### Error 24: Aesthetics graded as one lump

**What it is:** "The design looks professional" as a single criterion for a design brief.
**Why it matters:** Dim 11 Fail when design is central.
**BAD:** one aesthetics criterion at +8.
**GOOD:** typography, hierarchy, alignment, spacing, palette, contrast, imagery, consistency, each its own criterion.
**Tips:** one element per criterion; scale count to how central design is.

### Error 25: Functionality never actually run

**What it is:** Functionality criteria graded from screenshots.
**Why it matters:** Dim 12 (verdicts wrong), course rule "actually run or use the deliverable".
**BAD:** "Filters work" passed without clicking a filter.
**GOOD:** "When the Region filter is set to EU, the table shows only EU rows (tested on the Sales tab)."
**Tips:** one criterion per behaviour you personally tested.

### Error 26: Content never recalculated

**What it is:** figures accepted because they look plausible.
**Why it matters:** Dim 12, course rule "recalculate or check figures by hand".
**BAD:** "Totals are correct" passed on sight.
**GOOD:** "The Q2 total (48,210) equals the sum of the April, May and June rows in the source sheet (12,400 + 17,600 + 18,210)."
**Tips:** recompute at least the headline numbers; cite the arithmetic.

### Error 27: Editability ignored

**What it is:** no criterion about layers, live text or source files when a client would need to modify the work.
**Why it matters:** Dim 7 (implicit expectation), course rule "files must stay editable".
**BAD:** a flattened PNG poster passes every criterion.
**GOOD:** "The source file keeps type as live text." and "Elements sit on separate layers." as criteria.
**Tips:** if a client would ever edit it, add editability criteria.

### Error 28: Fewer than 30 (or more than 100) criteria

**What it is:** submitting 22 criteria because that is what the generator gave you; or 130 because you split everything twice.
**Why it matters:** Dim 3 (under 25 = Fail; over 100 = Non-Fail); course floor is 30.
**BAD:** 24 criteria.
**GOOD:** 30 to 60, reached by splitting and by covering implicit expectations.
**Tips:** expansion ladder in RubricWritingGuide.md section 9.

### Error 29: Set skewed to one category

**What it is:** 90% Requirements Compliance for a design brief.
**Why it matters:** Dim 7 ("highly skewed toward a handful of aspects").
**BAD:** 28 literal checks, 2 aesthetic checks, for a poster.
**GOOD:** categories spread in proportion to what the brief is about.
**Tips:** look at the platform's weight-by-category panel before submitting.

---

## Part 4 - Verdicts and justifications

### Error 30: Negative criterion graded backwards

**What it is:** Pass given because the flaw was avoided.
**Why it matters:** Dim 12 (wrong verdicts), Dim 15 (RD loses points for being clean), Dim 14 (story flips). The course changed the rule specifically because of this error.
**BAD:** "Contains audible clipping" (-7): AD2 clips at 1:02, marked Fail; RD is clean, marked Pass.
**GOOD:** AD2 Pass (the flaw happened, -7 applied); RD Fail (flaw absent, no penalty).
**Tips:** say it aloud before clicking: "Pass means it happened."

### Error 31: Verdict copied across the three deliverables

**What it is:** one verdict and one paragraph pasted for RD, AD1 and AD2.
**Why it matters:** Dim 12 and Dim 13.
**BAD:** "Only solo piano can be heard throughout" pasted for all three, when AD2 has a string pad at 1:40.
**GOOD:** each deliverable re-checked; AD2 Fail with the 1:40 location.
**Tips:** judge fresh; even identical evidence gets its own location line.

### Error 32: Justification contradicts its verdict

**What it is:** the paragraph describes the opposite of the verdict.
**Why it matters:** Dim 13 ("objectively inaccurate").
**BAD:** Pass on "contains static noodling" with the paragraph "no static noodling, the defect is absent".
**GOOD:** Fail with that paragraph, or Pass with "the section 1:00-1:30 has no melodic direction".
**Tips:** re-read verdict and paragraph as a pair before moving on.

### Error 33: Justification without a location

**What it is:** "the audio is clean" with no timestamp; "the layout is off" with no region.
**Why it matters:** Dim 13; the course requires "the evidence and where it is".
**BAD:** "Fails, the colours are wrong."
**GOOD:** "Fail. The headline uses #2E5AAC, which is not one of the three hex values in brand.pdf."
**Tips:** location conventions in JustificationGuide.md section 3.5.

### Error 34: Claim in a comparison justification with no rubric behind it

**What it is:** you praise the mix or criticise the spacing in a comparison paragraph, but no criterion grades it.
**Why it matters:** course rule "every claim needs a rubric, checked closely"; Dim 7.
**BAD:** paragraph says "the labels at 0:22 are unreadable"; no legibility criterion exists.
**GOOD:** criterion "On-screen labels are legible against their background" added, AD1 Fail at 0:22.
**Tips:** worksheet claim-to-criterion map; fill every row.

---

## Part 5 - Alignment and hygiene

### Error 35: RD scores under 95%

**What it is:** the golden reference fails your rubric.
**Why it matters:** Dim 15 Fail.
**BAD:** RD at 82% because five criteria enforce choices RD did not make and two negatives are graded backwards.
**GOOD:** neutralise or delete the arbitrary criteria; fix the negatives; RD at 97%.
**Tips:** compute percent(RD) with the worksheet formula or tools/rubric_audit.py.

### Error 36: Preference direction contradicts rubric totals

**What it is:** you rated AD2 ahead of AD1 (6) but AD1 out-scores AD2 on the rubric by 15 points.
**Why it matters:** Dim 14 Fail ("reversed story").
**BAD:** leaving both as they are.
**GOOD:** find the cause: a missing criterion for the thing that made AD2 better, or an over-weighted literal check AD1 happened to pass. Fix the cause.
**Tips:** STEP 10 of pipeline.md.

### Error 37: Tuning numbers to force the story

**What it is:** bumping a weight from 4 to 9 so the totals agree with your rating.
**Why it matters:** creates Dim 4 and Dim 5 errors while hiding the real Dim 14 cause.
**BAD:** "Legible labels" raised to 10 because AD1 fails it.
**GOOD:** keep the band the brief justifies; add the genuinely missing criteria; if the story still disagrees, revisit the rating.
**Tips:** every weight change needs a brief-language reason.

### Error 38: Unlisted minor errors

**What it is:** typos, a "+" where "-" was meant, a category left at the default, "AD1" where "AD2" was meant, leftover AI phrasing.
**Why it matters:** Dim 17 Non-Fail; blocks a 5/5 even when everything else is right.
**BAD:** "The poster contain a spelling errror."
**GOOD:** proofread pass; audit script clean; scorecard filled.
**Tips:** PreSubmitChecklist.md, last five minutes of every task.

---

## Part 6 - Reference files, subjectivity and package

### Error 39: Converting "approximately" into an exact rule

**What it is:** the brief says "approximately 300 cm"; the criterion demands 300 cm.
**Why it matters:** Dim 8 (unjustified requirement) and Dim 12 (wrong verdicts on deliverables that are in scale). The guide: exact language defines a target, approximate language defines a range.
**BAD:** "Ceiling height is 300 cm."
**GOOD:** "Ceiling height is in the intended scale of about 300 cm." Add a tolerance only when the brief, an input or a documented convention supports one.
**Tips:** copy the brief's qualifier into the criterion.

### Error 40: Promoting incidental or legacy file content into requirements

**What it is:** a DWG has old furniture, alternate options or annotations; the rubric demands them.
**Why it matters:** Dim 8 (arbitrarily introduced), Dim 5, and RD may fail them (Dim 15).
**BAD:** brief says "use the DWG only for room dimensions"; criterion checks that the DWG's door swings are reproduced.
**GOOD:** coverage tied to room dimensions. Ask: would the task materially change if this detail were different? If not, it is context.
**Tips:** record each provided file's authority (direct / specific / ambiguous) in the worksheet at STEP 1.

### Error 41: Ignoring a subjective brief term instead of decomposing it

**What it is:** the brief asks for a "photorealistic" render; the rubric has no realism criteria because "realistic" felt subjective.
**Why it matters:** Dim 7 (explicit requirement uncovered) and Dim 11.
**BAD:** no criterion for photorealism, or one lump "the render is photorealistic".
**GOOD:** lighting, scale and proportion, material response, shadows and reflections, secondary elements, artifacts, each its own criterion.
**Tips:** RubricWritingGuide.md section 2.11.

### Error 42: Macro consistency criterion double-penalising a detailed mismatch

**What it is:** "the render matches the model" fails because one window already failed its own criterion.
**Why it matters:** Dim 6 (same error penalised twice).
**BAD:** window mismatch fails C12 (openings) and C30 (render matches model).
**GOOD:** C30 fails only for a proposal-level contradiction (different massing, layout logic, facade concept, version).
**Tips:** decision rule: isolated mismatch = detailed criterion; proposal-level contradiction = macro criterion. Weight the macro criterion so it is not a second heavy penalty.

### Error 43: Over-atomising a dependent combination

**What it is:** "palette of cool blue, indigo and dark navy" split into three colour-existence criteria.
**Why it matters:** distorts the brief (the ask is the combined palette) and inflates the count with checks that are not independent failure modes.
**BAD:** three criteria, three points each, for one palette requirement.
**GOOD:** one criterion: "The palette is focused on cool blue, indigo and dark navy tones."
**Tips:** split independent failure modes; keep dependent details together.

### Error 44: Generic "matches the reference" criterion hiding several failures

**What it is:** one criterion "the model matches the DWG" carries footprint, walls, openings, circulation and levels.
**Why it matters:** under-penalisation (Dim 9): five major failures cost one verdict.
**BAD:** single DWG-match criterion at weight 10.
**GOOD:** separate criteria for footprint, exterior wall alignment, partitions, openings, vertical circulation, levels, site placement, where each is relevant and the brief binds the task to the file.
**Tips:** ArchitectureReviewGuide.md section 5.

### Error 45: Missing evaluation source on a multi-asset package

**What it is:** the package has a model and renders; the criterion does not say which one it is judged against, and the verdicts contradict each other.
**Why it matters:** Dim 12 and Dim 13 (verdicts and justifications inconsistent across reviewers).
**BAD:** "Openings match the reference." (in the model? in the render?)
**GOOD:** "In the 3D model, openings match the reference positions."
**Tips:** name the asset in the criterion text; the guide lists 3D model, render, plan, DWG, PDF, material presentation.

### Error 46: Skipping package validation

**What it is:** rating starts before checking that the input files match the brief, that RD could have come from those inputs, that no outdated RD files confuse the current version, and that AD1/AD2 files open.
**Why it matters:** Dim 16 (an insufficient package pushed through), Dim 12 (verdicts on the wrong version).
**BAD:** grading a legacy render as the current RD.
**GOOD:** worksheet package-validation block filled at STEP 1; Gate 1 No if no reliable evaluation source remains.
**Tips:** ArchitectureReviewGuide.md section 11, steps 1-4.

### Error 47: Inflating RD when reviewing its failures

**What it is:** RD fails a valid criterion, so the criterion is softened or deleted to lift RD.
**Why it matters:** Dim 12 and Dim 13 (wrong verdicts), and it hides a real finding.
**BAD:** deleting "openings match the reference" because RD misses one.
**GOOD:** review each RD failure: valid? weight right? rubric representing the task? Keep genuine failures. If RD genuinely underperforms, Gate 2 may be the honest answer.
**Tips:** the guide's step 16: "Do not inflate RD artificially."

---

## Pre-submission master checklist (from this playbook)

**Part 1 (8):** labels straight; everything experienced in full; RD not assumed best; three detailed justifications; five dimensions each; extremes evidenced; comparisons independent; Gate 1 honest.

**Part 2 (11):** every card triaged; atomic; self-contained; brief-exact; golden-neutral; region-neutral; sourced; categorised; banded; negatives phrased as the flaw happening; human-written.

**Part 3 (10):** no duplicates; no overlaps; explicit requirements covered; implicit and expert covered; aesthetics per element; functionality run; content recalculated; editability considered; 30-100 count; categories spread.

**Part 4 (5):** negatives graded as "flaw happened = Pass"; verdicts judged fresh x3; paragraphs match verdicts; locations everywhere; every claim has a rubric.

**Part 5 (4):** RD >= 95%; totals match ratings; no number tuning; proofread.

**Part 6 (9):** approximate kept approximate; file authority respected; subjective terms decomposed; macro criteria proposal-level only; no over-atomising; generic reference checks split; evaluation source named; package validated; RD failures reviewed without inflation.

*End of Common Errors Playbook.*
