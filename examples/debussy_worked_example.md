# Worked Example -- Debussy Centenary Competition (from the course, annotated)

> **Source:** course slides "Good example 1 of 3" (the brief) and "Worked example 2 of 3, 3 of 3" (ten criteria with AD1 and AD2 verdicts and justifications). The RD column was not shown on the slides. **Two negative criteria on slide 3 of 3 were graded under the OLD pass rule (Pass = flaw avoided). This file shows them corrected to the current rule (Pass = flaw happened) and explains the difference.**

---

## 1. The brief (read this first; every criterion traces back to a line here)

**Work description.** To celebrate the 100th anniversary of the death of composer Claude Debussy, a major French city has launched a competition open to all French composers. Participants are invited to submit a solo piano composition inspired by Debussy's style and musical language, while meeting the requirements opposite.

**Provided material.** The score of Debussy's "Doctor Gradus ad Parnassum", for reference, in input/score.

**Deliverables.** The music in .mp3 or .wav format.

**Requirements.**
1. The piece must be written for solo piano only.
2. It should incorporate subtle references to Debussy's "Doctor Gradus ad Parnassum", but avoid any direct repetition of its musical motifs or phrasing.
3. It is preferable for the piece to begin in C major, but it may modulate to other keys later on.
4. The tempo is at the composer's discretion.
5. The composition should broadly fit within Debussy's musical aesthetic, particularly his tonal and impressionistic approach.
6. The composer has full freedom in structuring and developing the piece.
7. The composition should be between two and four minutes in length.

### 1.1 Brief extraction (as the worksheet would hold it)

| ID | Requirement | Strength | Keyed on |
|---|---|---|---|
| R1 | Solo piano only | must | "must", "only" |
| R2 | Subtle references to Doctor Gradus | should | "should incorporate" |
| R3 | No direct repetition of its motifs or phrasing | should (negative) | "avoid any direct repetition" |
| R4 | Begins in C major | preferable | "preferable" |
| R5 | May modulate later | discretion | "may" |
| R6 | Tempo | discretion | "at the composer's discretion" |
| R7 | Fits Debussy's tonal and impressionistic aesthetic | should | "should broadly fit" |
| R8 | Structure | discretion | "full freedom" |
| R9 | Duration 2:00 to 4:00 | should | "should be between" |
| F1 | Score of Doctor Gradus in input/score | reference material | |
| D1 | .mp3 or .wav | deliverable | |

Note how the strength tags drive the weights in section 2: R1 (must) = 10, R2 (should) = 8, R4 (preferable) = 6. R6 and R8 are at the composer's discretion, so there is no tempo criterion and no structure-shape criterion; grading those would be an arbitrary choice (QC Dim 5).

---

## 2. The ten criteria from the course, with verdicts

Verdict columns for AD1 and AD2 are as shown on the slides, except rows 9 and 10 (see 2.1). The RD column is the expected result for a golden reference (not shown on the slides; RD must reach 95% or more).

| # | Criterion | Weight | Category | Source | RD (expected) | AD1 | Justification for AD1 | AD2 | Justification for AD2 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | The recording contains solo piano only: no other instruments, voices, percussion or effects. | 10 | Requirements Compliance | R1 | Pass | Pass | Only solo piano can be heard throughout the audio. | Pass | Only solo piano can be heard throughout the audio. |
| 2 | The piece contains a recognisable allusion to Doctor Gradus: broken chords, minimal left hand, or sixteenth notes in the right hand. | 8 | Requirements Compliance | R2, F1 | Pass | Pass | Minimalistic left-hand accompaniment with sixteenth notes in the right hand. | Fail | Some progressions evoke Debussy around 0:07-0:09, but there is no reference to Doctor Gradus. |
| 3 | The piece opens in C major. | 6 | Requirements Compliance | R4 | Pass | Pass | The first bars are objectively in C major (C, E, G chords). | Fail | Starts in E-flat minor; C major never appears. |
| 4 | At least one impressionist scale colour beyond plain major/minor is used (pentatonic, whole-tone, or a church mode). | 6 | Content Correctness | R7 | Pass | Pass | Whole-tone scale around 1:00. | Pass | D Dorian at the end, around 2:28, a church mode. |
| 5 | Avoids anachronistic idioms foreign to Debussy: pop chord loops, jazz swing, regular V7-I Classical cadences. | 5 | Content Correctness | R7 | Pass | Pass | None of these anachronistic idioms are heard. | Fail | Cadences at 0:49 and 1:16 evoke the Russian school; the piece also alternates Classical, Romantic, modern and atonal writing. |
| 6 | The piano timbre is a realistic acoustic piano throughout, not an obviously synthetic or electric tone. | 7 | Usability & Realism | expert nuance | Pass | Fail | Sounds like an entry-level VST, not a realistic acoustic piano. | Pass | Definitely sounds like a realistic acoustic piano. |
| 7 | The audio is free of audible flaws: no clipping, dropouts, clicks, stuck notes or noticeable noise floor. | 7 | Usability & Realism | expert nuance | Pass | Pass | No issues of that kind can be heard in the track. | Fail | Clips slightly around 1:02, likely from right-hand chords played too harshly. |
| 8 | Leading and trailing silence do not exceed 4 seconds each, with at least 1 second of silence at the end. | 4 | Usability & Realism | expert nuance | Pass | Pass | Leading and trailing silence stay within 4 seconds. | Fail | There is less than 1 second of silence at the end of the audio. |
| 9 | The piece contains long stretches (over 10 seconds) of static noodling with no melodic or harmonic direction. | -7 | Presentation & Aesthetics | expert nuance | Fail (flaw absent) | **Pass** (flaw present) | The section between 1:00 and 1:30 has no clear melodic or harmonic direction. | **Fail** (flaw absent) | No static noodling: the defect is absent. |
| 10 | At least one transition between phrases or sections is not smooth: abrupt cuts or unmotivated jumps. | -7 | Presentation & Aesthetics | expert nuance | Fail (flaw absent) | **Pass** (flaw present) | The transition starting at 0:41 is too abrupt; around 1:08 the section feels disjointed. | **Fail** (flaw absent) | The piece is well structured: the defect is absent. |

### 2.1 The correction on rows 9 and 10

The slide shows AD1 = Fail and AD2 = Pass on both negative rows, with justifications that describe the flaw present in AD1 and absent in AD2. That is the old rule (Pass = the flaw was avoided). Under the current rule (Pass = it happened; for a negative criterion, the bad thing happened), the same justifications require AD1 = Pass and AD2 = Fail. The justification text stays exactly as written; only the verdict word flips.

The slide "This fixes a confusing, common mistake in the task" is explicit: old = "Pass = the flaw was avoided" (incorrect), new = "Pass = the flaw happened" (correct). "Pass now means the same thing for positive or negative criteria: it happened. The sign of the weight just decides if that helps or hurts the score."

### 2.2 Why the correction matters for the numbers

P (sum of positive weights) = 10 + 8 + 6 + 6 + 5 + 7 + 7 + 4 = **53**.

| | Current rule (correct) | Old rule (as on the slide) |
|---|---|---|
| AD1 positives passed | 10 + 8 + 6 + 6 + 5 + 7 + 4 = 46 | 46 |
| AD1 negatives | rows 9, 10 Pass (flaw present): -7 -7 = -14 | rows 9, 10 Fail: 0 |
| **AD1 score** | **32 / 53 = 60.4%** | 46 / 53 = 86.8% |
| AD2 positives passed | 10 + 6 + 7 = 23 | 23 |
| AD2 negatives | rows 9, 10 Fail (flaw absent): 0 | rows 9, 10 Pass: -14 |
| **AD2 score** | **23 / 53 = 43.4%** | 9 / 53 = 17.0% |
| RD (expected: all positives, no negatives) | 53 / 53 = 100% | 53 - 14 = 39 / 53 = 73.6% (RD penalised for being clean) |

Under the old rule RD would fail Dim 15 (under 95%) even though it is perfect, and AD1's noodling and abrupt transitions would cost it nothing. That is the "clean deliverables were being penalised" problem the change fixed.

**Alignment reading (Dim 14):** with the correct numbers, AD1 (60.4%) is ahead of AD2 (43.4%), so the AD1 vs AD2 head-to-head should land at 1 to 3 (AD1 better), and both RD comparisons should favour RD. If your ratings said otherwise, something in the ratings or the rubric is wrong.

---

## 3. What each criterion teaches

| # | Lesson |
|---|---|
| 1 | "must ... only" in the brief = weight 10. The text lists what "only" excludes (instruments, voices, percussion, effects) so it is self-contained. Category is Requirements Compliance because the brief states it literally. |
| 2 | "should incorporate" = 8. The brief's vague "subtle references" is made checkable by naming what an allusion to Doctor Gradus looks like (broken chords, minimal left hand, sixteenths). The "or" lists alternatives, which is lenient phrasing (Dim 5), not a compound check. |
| 3 | "preferable" = 6, not 10. Weight follows the brief's word. Justification cites the evidence (C, E, G chords) and, for the fail, the actual key. |
| 4 | The aesthetic requirement (R7) is turned into a checkable musical fact with lenient alternatives (pentatonic, whole-tone, church mode). Located: "around 1:00", "around 2:28". |
| 5 | Positive weight with "avoids ..." phrasing is fine: Pass = it happened = the piece avoids them. Do not put this text under a negative weight. |
| 6 | Expert nuance the brief never states: a competition entry for solo piano must sound like a piano. Realism criterion, Usability & Realism category, weight 7 (a client would send it back). |
| 7 | Expert nuance: technical cleanliness. Located fail: "around 1:02", with a likely cause. |
| 8 | Expert nuance with exact thresholds (4 seconds, 1 second), so it is self-contained and measurable. Weight 4: a client would complain, not reject. |
| 9 | Negative criterion phrased as the flaw happening ("contains long stretches ..."), with a threshold (over 10 seconds). Pass when present. |
| 10 | Negative criterion, same pattern, located ("0:41", "around 1:08"). |

Across the set: every criterion is one check; every justification has a location or a checkable musical fact; weights follow the brief's language; two negatives out of ten (20%); RD scores 100%.

---

## 4. Reaching 30 for this brief (illustrative expansion)

The course example stops at ten. A submittable set needs at least 30. Climbing the expansion ladder (RubricWritingGuide.md section 9) for this brief would add, for example:

**Deliverable spec and explicit requirements**
- 11. The file is delivered in .mp3 or .wav format. (Requirements Compliance, 9, D1)
- 12. The file plays from start to end without errors. (Functionality, 9, D1)
- 13. The piece runs between 2:00 and 4:00. (Requirements Compliance, 8, R9)
- 14. The piece contains a direct quotation of a Doctor Gradus motif or phrase. (Requirements Compliance, -8, R3) [negative: Pass = the quotation is present]
- 15. The piece modulates to at least one key other than the opening key. (Content Correctness, 2, R5; slightly important because it is permitted, not required; consider dropping as discretion)

**Debussy aesthetic (R7), as checkable musical facts, leniently phrased**
- 16. Parallel chord planing or extended (7th, 9th, added-note) harmonies are used at least once. (Content Correctness, 5)
- 17. Tonal centres are established without relying on regular functional V7-I cadences. (Content Correctness, 5)
- 18. Dynamics vary across the piece (at least one clearly soft and one clearly loud passage). (Presentation & Aesthetics, 4)
- 19. Pedalling or sustain creates blended harmonic washes rather than dry, detached chords throughout. (Presentation & Aesthetics, 4)

**Audio craft (implicit professional expectations)**
- 20. Note velocities vary naturally (not a fixed velocity across the piece). (Usability & Realism, 5)
- 21. The stereo image is balanced with no channel noticeably louder. (Usability & Realism, 3)
- 22. Loudness is consistent across sections with no abrupt level jumps. (Usability & Realism, 4)
- 23. The final note or chord decays naturally rather than being cut off. (Usability & Realism, 5)
- 24. The tempo is consistent within phrases unless the change is clearly expressive. (Presentation & Aesthetics, 4; tempo itself is at discretion, steadiness is a craft expectation)

**Structure and coherence (structure is free, coherence is expected)**
- 25. The piece has a recognisable beginning, development and ending. (Presentation & Aesthetics, 5)
- 26. Material introduced early returns or is developed later at least once. (Presentation & Aesthetics, 4)
- 27. The overall musicality is at least as convincing as RD. (Presentation & Aesthetics, 5; comparative, golden-neutral)

**Observed-failure negatives (write only if seen in AD1 or AD2)**
- 28. The recording contains a non-piano sound (voice, percussion, effect). (Requirements Compliance, -10)
- 29. The recording contains an audible loop or copy-pasted repeated section. (Presentation & Aesthetics, -6)
- 30. The recording ends with an abrupt cut before the final note decays. (Usability & Realism, -5)

Shape: 30 criteria, 25 positive, 5 negative (17%); categories spread across Requirements Compliance, Content Correctness, Presentation & Aesthetics, Usability & Realism, Functionality; one comparative criterion (3%); nothing grades tempo choice or structure shape, which the brief left free.

---

*End of worked example.*
