# Sardine Refiner -- Session Prompts and Two-Device Protocol

> **Updated:** 2026-09-17. Three things: the OPENING prompt (paste into every new chat), the CLOSING prompt (self-QC, fix loop, final package), and the two-device protocol (Claude on the MacBook, Outlier on the recorded PC). Micro-prompts for the middle of a task are in section 4.

---

## 0. One-time setup (do once, saves minutes every task)

**Option A: claude.ai Project on the Mac (recommended if you use claude.ai).**
1. Create a Project called "Sardine Refiner".
2. Upload as project knowledge: `project_instructions.md`, `QualitySpecDoc.md`, `pipeline.md`, `tasker_orchestrator.md`, `RubricWritingGuide.md`, `JustificationGuide.md`, `ArchitectureReviewGuide.md`, `CommonErrors.md`, `PreSubmitChecklist.md`, `TaskWorksheet_Template.md`, `examples/debussy_worked_example.md`, this file.
3. Paste section 2.1 (the short project instruction) into the Project's custom instructions.
4. Every task = new chat inside the Project + the OPENING prompt. Nothing else to load.

**Option B: Claude Code on the Mac with the OneDrive folder synced.**
Claude reads the kit files by path and writes `Tasks/<task-id>.md` itself. Use the OPENING prompt variant in 2.3. This is the only option where `tools/rubric_audit.py` runs automatically.

**Photo bridge.** Phone camera + AirDrop to the Mac (or Continuity Camera). Claude transcribes photos of the PC screen. Test once: photograph a rubric list screen, drop it in, ask for a verbatim transcription.

**Ask your QM two things before the first task.** (a) May the Autoflation Link be opened in a browser on the Mac (non-recorded device)? If yes, brief text and the rubric list can be copy-pasted instead of photographed; deliverables still have to be judged on the PC. (b) Is Windows voice typing (Win+H, an OS feature, not a window) acceptable for entering text into Outlier fields on the recorded PC? If yes, you can read the Mac screen and dictate. Do not assume either; the kit works without both.

---

## 1. Two-device protocol (the rules the prompts enforce)

| Direction | Bridge | Rule |
|---|---|---|
| PC -> Mac (inputs) | Photo of the PC screen, or typed notes | Claude transcribes every photo verbatim before using it. Brief: 1-2 photos. Rubric list: scroll and photograph every screen. Deliverables: key frames or screens with the timestamp, page or panel visible. Score panel: 1 photo. |
| Mac -> PC (outputs) | Teleprompter blocks | Claude outputs short paste-ready blocks in the exact order of the Outlier fields, one screen at a time. You type across. Comparison paragraphs 60-120 words. Verdict justifications 12-25 words. |
| Existing criteria | Edit deltas | For each synthetic criterion Claude says KEEP, or CHANGE TEXT TO "...", CHANGE WEIGHT TO n, CHANGE CATEGORY TO ..., or DELETE. Full text only for NEW criteria. You retype only what changes. |
| Order of work | Draft on Mac, QC on Mac, type on PC once | Everything (comparisons, gates, rubric set, verdicts, justifications, alignment, closing QC) is finished on the Mac before the rubric phase is typed into the PC. Then click Next, photograph the score panel, reconcile on the Mac, submit. |
| Evidence | Located observations only | Claude never invents what a deliverable contains. If it needs a fact, it asks a yes/no or "what and where" question. You answer while looking at the PC. |
| Source of truth | Mac session / worksheet | The platform is a copy of the worksheet. TaskLog entry written on the Mac after submit. |

**Typing budget per task** (why the blocks are short): 3 paragraphs (~300 words) + 2 gate answers + ~30-45 criteria (only the changed or new ones in full) + ~100 one-line justifications (~2,000 words). Anything longer than that is Claude being verbose; tell it "shorter".

**What you never have to think about** (the prompts do it): which dimension a fact belongs to, weight band from the brief's wording, category choice, whether a criterion is atomic or vague, pass semantics for negatives, the coverage matrix, the arithmetic, the 17-dimension scorecard, what to fix and in what order.

---

## 2. OPENING prompt

### 2.1 Project custom instruction (paste once into the claude.ai Project settings)

```
You are the Sardine Refiner Task Orchestrator defined in tasker_orchestrator.md. The rulebook is project_instructions.md; the QC benchmark is QualitySpecDoc.md (17 dimensions, all must be [No Issues]); the step order is pipeline.md; criterion writing follows RubricWritingGuide.md and, for architecture or interior tasks, ArchitectureReviewGuide.md; justifications follow JustificationGuide.md.

Two-device setup: the contributor reads the Autoflation Link and types into Outlier on a separate, screen-recorded PC where only the Outlier page may be open. You never see the deliverables. Inputs reach you as photos of the PC screen or typed notes; transcribe every photo verbatim before using it. Return outputs as short paste-ready blocks in the exact order of the Outlier fields, one screen at a time. For existing synthetic criteria give edit deltas (KEEP / CHANGE TEXT TO / CHANGE WEIGHT TO / CHANGE CATEGORY TO / DELETE); full text only for NEW criteria. Comparison paragraphs 60-120 words; verdict justifications 12-25 words.

Never invent evidence, locations, verdicts or ratings. Ask one focused question batch at a time, in the order the PC screens appear. Labels RD, AD1, AD2 only. Pass = it happened for positive and negative criteria alike. Every claim in a justification needs a rubric. Minimum 30 criteria, maximum 100. RD must score 95% or more. No em dashes anywhere. Gate only at real decisions; do not ask "look right?".
```

### 2.2 OPENING prompt for a claude.ai Project chat (paste at the start of every task)

```
New sardine_refiner task. Run the Task Orchestrator from the project knowledge (tasker_orchestrator.md, project_instructions.md, QualitySpecDoc.md, pipeline.md, RubricWritingGuide.md, JustificationGuide.md, ArchitectureReviewGuide.md, CommonErrors.md, PreSubmitChecklist.md). Two-device protocol applies: I am on the recorded PC with only Outlier open; you get photos or typed notes; you return teleprompter blocks and edit deltas.

Open a worksheet for this task in your reply, in the shape of TaskWorksheet_Template.md, with the labels RD = human reference, AD1 = model output 1, AD2 = model output 2 at the top. Keep it updated as we go; I will ask for it at the end.

Intake: ask me for everything you need to start, in ONE message, in this order, and tell me for each whether a photo or typed text is better:
1. Task id and deliverable type (audio / static design / video / web / app / data / document / game / 3D / architecture-interior / other).
2. The brief from the top of the Autoflation Link: work description, requirements, script or copy, provided material, deliverables spec.
3. Whether each provided file the brief mentions is actually present on the page.
4. What RD, AD1 and AD2 each contain: files, formats, durations or dimensions, whether they open, whether they are editable.
5. Anything already visible that looks wrong, missing or outdated in the package.

After intake: structure the brief (R#/S#/F#/D# with must / should / preferable tags and provided-file authority), run package validation and the Gate 1 pre-check, then guide me through experiencing the deliverables with targeted yes/no and what-and-where questions per deliverable type so I only answer, never decide what to look at. Then Phases 3 to 11 of the orchestrator. I will say "closing QC" when the draft is complete.
```

### 2.3 OPENING prompt for Claude Code on the Mac (kit folder synced)

```
New sardine_refiner task. Read tasker_orchestrator.md, project_instructions.md, QualitySpecDoc.md, pipeline.md, RubricWritingGuide.md, JustificationGuide.md, ArchitectureReviewGuide.md, PreSubmitChecklist.md and SessionPrompts.md from this folder, then act as the Sardine Refiner Task Orchestrator under the two-device protocol in SessionPrompts.md section 1.

Create Tasks/<task-id>.md from TaskWorksheet_Template.md as soon as I give you the task id, and keep it updated after every phase; it is the source of truth. Ask me for the intake items in one message (task id and deliverable type; brief as photo or text; provided files present or not; what RD, AD1, AD2 contain; anything visibly wrong in the package). I will drop photos of the PC screen into this chat; transcribe them verbatim into the worksheet before using them. Return outputs as teleprompter blocks in Outlier field order and edit deltas for existing criteria. When I say "closing QC", run SessionPrompts.md section 3 and run tools/rubric_audit.py on the worksheet as part of it.
```

---

## 3. CLOSING prompt (self-QC, fix loop, final package)

Paste when the draft is complete on the Mac and BEFORE typing the rubric phase into the PC. Paste it again after the platform score panel if anything changed.

```
Closing QC. Work only from this session's worksheet state. Do not ask me anything you can compute; ask me only for facts that require looking at a deliverable again, and collect those as "CHECK ON PC" questions.

1. Recount and recompute: criteria total, positive and negative counts, count per category, criteria that contain "and" / lists / slashes, criteria with vague words (appropriate, proper, good, clean, suitable, reasonable, correctly, well, nice, high quality), near-duplicate pairs, criteria with no source, criteria that enforce a choice RD made that the brief did not mandate (share of total), negative criteria phrased as avoidance, criteria whose three justifications are identical, criteria with any blank justification, justifications that contradict their verdict, comparison-paragraph claims with no criterion, dimensions missing from any comparison paragraph, extremes (1, 2, 6, 7) with fewer than two located facts, provided-file authority respected, exact vs approximate preserved, subjective brief terms decomposed, macro consistency criteria limited to proposal-level, evaluation source named where the package has several assets.
2. Compute P, score and percent for RD, AD1, AD2 (score = sum of weights of criteria passed; negative passes subtract; percent = score / P x 100). Show the arithmetic. Compare the ordering with the three rating averages.
3. Fill the 17-row scorecard from QualitySpecDoc.md section 5: for each dimension the QC label verbatim ([Fail - ...] / [Non-Fail - ...] / [No Issues]) and the proof (count, percent, criterion IDs).
4. For every row not [No Issues]: name the root cause, apply the fix yourself (rewrite the criterion, split it, delete the duplicate, add the missing criterion with category, weight and source, correct the weight band, flip the backwards negative verdict, rewrite the contradicting justification, revise the paragraph, revise a rating only if the rubric evidence supports it), and record each fix as one CHANGE line: "CHANGE C7: weight 9 -> 6 (brief says preferable; Dim 4)". Never change a weight to move a total. If a fix needs a fact you do not have, write a CHECK ON PC line instead: "CHECK ON PC C12 AD2: does the footer link open the Instagram page? (yes/no)".
5. Re-run steps 1 to 3 on the fixed state. Repeat until all 17 rows read [No Issues] or only CHECK ON PC items remain.
6. Output, in this order:
   (a) the final 17-row scorecard;
   (b) the CHANGE list grouped in Outlier order: comparisons (ratings and paragraphs), gates, criteria by ID (KEEP / CHANGE / DELETE / NEW with full text, category, weight), verdicts and justifications by ID;
   (c) the CHECK ON PC list;
   (d) the final teleprompter package for anything not yet typed into the PC, one screen at a time;
   (e) the TaskLog.md entry draft (task id, deliverable type, gates, rating averages, criteria counts, P and percents, what was hard).
7. If I then send the platform score panel (photo or numbers): reconcile it against your model, explain any difference, review every RD failure first (valid? weight right? rubric representing the task?) without inflating RD, and issue any further CHANGE lines.

Rules: labels RD / AD1 / AD2 only; Pass = it happened for both signs; no em dashes; plain words; do not soften a genuine RD failure; do not pad to reach 30 with duplicates; stop when the story is consistent across ratings, paragraphs, verdicts and totals.
```

---

## 4. Micro-prompts (mid-task, copy as needed)

| Situation | Paste |
|---|---|
| Sending a photo of the brief | `Transcribe this verbatim into the worksheet section 1, then structure it (R#/S#/F#/D#, strength tags, file authority).` |
| Sending photos of the rubric list | `Transcribe every criterion verbatim into the triage table with its category and weight, numbered C1..Cn in screen order. Then build your own outline first, compare both directions, and triage.` |
| Sending a deliverable screenshot | `This is [RD/AD1/AD2], [location]. Log observations into the Evidence Ledger and tell me what else to look at on this screen.` |
| Ready to rate | `Propose the five ratings and the paragraph for [RD vs AD1 / RD vs AD2 / AD1 vs AD2] from the ledger; mark anything you are inferring rather than observing.` |
| Gate decision | `Gates: propose answers with one-line reasons; if either ends the task, give me the statement to type.` |
| Verdict batch | `Next batch of 10 cards in teleprompter order. For each: KEEP / CHANGE / DELETE / NEW, then RD, AD1, AD2 verdict + one-line justification. Ask me only where the ledger has no fact.` |
| Too long to type | `Shorter. Paragraphs under 90 words, justifications under 20 words, no restating the criterion.` |
| Score panel photo | `Reconcile this against your totals. RD failures first. CHANGE lines only.` |
| After submit | `Write the TaskLog.md entry and list anything I should ask the QM.` |

---

## 5. Sequence of a task across the two devices

| # | Where | You do | Claude does |
|---|---|---|---|
| 1 | Mac | New chat, OPENING prompt | Asks intake in one message |
| 2 | PC | Photograph brief; note provided files, deliverable formats | |
| 3 | Mac | Drop photos, answer intake | Structures brief, validates package, Gate 1 pre-check, opens worksheet |
| 4 | PC | Experience RD, AD1, AD2 fully | Asks targeted what-and-where questions; you answer as you look |
| 5 | Mac | Approve ratings and paragraphs | Proposes 15 ratings + 3 paragraphs from the ledger |
| 6 | PC | Type the 15 ratings, 3 paragraphs, 2 gate answers | |
| 7 | PC | If both gates pass: confirm guidelines, photograph the criteria list (every screen) | |
| 8 | Mac | Drop photos | Transcribes, builds own outline, compares, triages, closes coverage to 30+ |
| 9 | Mac | Answer verdict questions per batch | Drafts 3 verdicts + 3 one-liners per criterion, edit deltas for existing cards |
| 10 | Mac | CLOSING prompt | Scorecard, fixes, CHANGE list, CHECK ON PC list, teleprompter package |
| 11 | PC | Answer CHECK ON PC items by looking; type the rubric phase once from the teleprompter | |
| 12 | PC | Click Next, photograph the score panel | |
| 13 | Mac | Drop the photo | Reconciles, RD failures first, final CHANGE lines |
| 14 | PC | Apply final changes, submit | |
| 15 | Mac | "After submit" micro-prompt | TaskLog entry, QM questions |

---

*End of Session Prompts.*
