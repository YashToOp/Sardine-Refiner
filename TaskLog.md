# Sardine Refiner -- Task Log

> **Started:** 2026-09-17. Running record of every task, what worked, what QC flagged. Read the CRITICAL RULES block before every task. Add a new entry after every submission. Update the rules block when a QC result teaches something.

---

## CRITICAL RULES -- read before starting ANY task

> Seeded from the project course and the 17-dimension QC Spec Doc. Promote a lesson here only when it cost (or nearly cost) a [No Issues] label.

### RULE 1: RD, AD1, AD2 are never mixed up
Every field on the platform refers to the three by abbreviation. One swapped label invalidates the whole submission. Write the labels at the top of the worksheet; re-read the panel header before every rating and verdict; search final text for "reference", "human", "first model", "version".

### RULE 2: Pass = it happened, for both signs
Positive criterion: Pass when the good thing is present. Negative criterion: Pass when the flaw is present. The course changed this rule because negatives were being graded backwards, penalising clean deliverables. A backwards negative hits Dim 12 (verdicts), Dim 15 (RD sanity) and Dim 14 (alignment) at once. Say it aloud before each negative verdict.

### RULE 3: Every claim needs a rubric
If a comparison paragraph praises or criticises something, a criterion must grade it. The course says this is checked closely. Keep the claim-to-criterion map in the worksheet and fill every row.

### RULE 4: 30 or more atomic criteria, never fewer than 25, never more than 100
Split on "and", lists, slashes, "including". Reach the count by splitting and by covering implicit expectations and expert nuances, never by duplicating.

### RULE 5: RD must score 95% or higher
If it does not, a criterion enforces a choice the brief never mandated, an RD verdict is wrong, or a negative is graded backwards. Compute it; do not assume it.

### RULE 6: Gates are answered honestly, and they end the task
Insufficient brief: Gate 1 No, name the gap, submit. RD worse: Gate 2 Yes, explain, submit. Both are complete, passing tasks. Pushing through an insufficient brief is a Dim 16 Fail.

### RULE 7: Every justification has a location
Timestamp, page, screen, region, file, cell. "The audio is clean" is not a justification. "No clipping heard across 0:00-2:37; peak at 1:02 stays below distortion" is.

### RULE 8: Synthetic rubrics are a starting point, not the truth
Triage every card: keep / edit / delete with a reason. Rewrite AI-sounding text. Fix category and weight. Delete nonsense.

### RULE 9: Exact terms from the brief; RD is a bar, not a template
Copy values verbatim ("between 2:00 and 4:00", the hex codes, the script lines). For quality, write "at least as good as RD". Never enforce a random RD choice the brief did not mandate.

### RULE 10: No region assumptions
Date format, units, currency, spelling variant, regulation, paper size: grade only what the brief states.

### RULE 11: Totals must tell the same story as the ratings, fixed at the root
Never tune a weight to move a total. Find the backwards negative, the non-mandated criterion, the missing criterion, the band error, or the over-extreme rating.

### RULE 12: No em dashes, no AI filler, labels only
Proofread every typed field. Dim 17 blocks a 5/5 on a typo or a wrong sign.

### RULE 13: Validate the package before rating
Inputs match the brief; RD could have come from these inputs; no outdated RD files mistaken for current; AD1 and AD2 open in the requested format. If no reliable evaluation source remains, Gate 1 is No. (Architecture guide steps 1-4.)

### RULE 14: Keep the brief's precision and the file's authority
"Approximately 300 cm" is a range, not 300 cm. "Use the DWG only for dimensions" does not make its furniture mandatory. Subjective brief words (photorealistic, refined) are requirements: decompose them into observable criteria.

### RULE 15: Your outline first, then theirs; RD failures first, never inflated
Build your own criteria outline in category order before adopting the synthetic set, then compare both directions. After clicking Next, review every RD failure first: valid, weight right, rubric representing the task. Revise a rating on evidence; never tune a weight to protect one.

---

## FORMATTING RULES FOR THIS FILE

- No em dashes anywhere. Use "--" or rewrite.
- One entry per task, newest at the bottom.
- Record numbers (count, percents, time) so the budget in pipeline.md can be calibrated.

---

## Entry template

```
## Task N: <task-id> -- <deliverable type> -- <one-line brief>

**Date:** YYYY-MM-DD
**Time taken:** __ min (brief __ / experience __ / comparisons __ / triage+coverage __ / verdicts __ / alignment+sweep __)
**Gates:** G1 = Yes/No, G2 = Yes/No (ended at gate? which?)
**Ratings (avg):** RD vs AD1 __ | RD vs AD2 __ | AD1 vs AD2 __
**Criteria:** synthetic __ -> final __ (positive __ / negative __); category spread RC/PA/FN/CC/UR/ED = __/__/__/__/__/__
**Alignment:** P __ | RD __% | AD1 __% | AD2 __%
**Audit script:** FAIL __ / WARN __ (before fixes) -> clean?
**What worked:**
-
**What was hard / surprised me:**
-
**QC result (fill in later):** labels per dimension that were not [No Issues], and why
-
**Rule promoted to CRITICAL RULES?** yes/no (which)
```

---

## Task 1: (pending)

