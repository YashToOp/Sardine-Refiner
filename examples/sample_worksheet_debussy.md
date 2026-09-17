# Task Worksheet -- SAMPLE-debussy -- audio (solo piano composition)

> Filled sample of TaskWorksheet_Template.md using the course's Debussy example (10 criteria, negatives corrected to the current pass rule). Use it to see what a completed worksheet looks like and to test `tools/rubric_audit.py`. It is deliberately short of 30 criteria so the script shows the count warning.

**Labels for this task (never mix):** RD = human reference | AD1 = model output 1 | AD2 = model output 2

| Field | Value |
|---|---|
| Task id | SAMPLE-debussy |
| Date | 2026-09-17 |
| Deliverable type | audio |

---

## 1. Brief extraction (STEP 1)

| ID | Requirement (verbatim value) | Strength | Keyed on |
|---|---|---|---|
| R1 | Solo piano only | must | "must", "only" |
| R2 | Subtle references to Doctor Gradus ad Parnassum | should | "should incorporate" |
| R3 | No direct repetition of its motifs or phrasing | should | "avoid any direct repetition" |
| R4 | Begins in C major | preferable | "preferable" |
| R7 | Fits Debussy's tonal and impressionistic aesthetic | should | "should broadly fit" |
| R9 | Duration between two and four minutes | should | "should be between" |

---

## 4. Comparisons (STEP 3-5)

### 4.1 RD vs AD1

| Dimension | Rating | Evidence (E#) |
|---|---|---|
| Realism | 2 | E6 |
| Design & UI/UX Quality | 3 | E9, E10 |
| Professionalism | 3 | E6 |
| Coherence & Continuity | 2 | E9, E10 |
| Multi-Asset Consistency | 4 | N/A single file |

### 4.2 RD vs AD2

| Dimension | Rating | Evidence (E#) |
|---|---|---|
| Realism | 4 | E6b |
| Design & UI/UX Quality | 2 | E2, E3 |
| Professionalism | 2 | E7, E8 |
| Coherence & Continuity | 3 | E5 |
| Multi-Asset Consistency | 4 | N/A single file |

### 4.3 AD1 vs AD2

| Dimension | Rating | Evidence (E#) |
|---|---|---|
| Realism | 6 | E6, E6b |
| Design & UI/UX Quality | 2 | E2, E3 |
| Professionalism | 3 | E7, E8 |
| Coherence & Continuity | 3 | E5, E9 |
| Multi-Asset Consistency | 4 | N/A |

---

## 8. FINAL RUBRIC (STEP 9)

| ID | Criterion | Category | Weight | Source | RD | AD1 | AD2 | Justification RD | Justification AD1 | Justification AD2 |
|---|---|---|---|---|---|---|---|---|---|---|
| C1 | The recording contains solo piano only: no other instruments, voices, percussion or effects. | Requirements Compliance | 10 | R1 must | Pass | Pass | Pass | Pass. Only piano is heard across 0:00-3:12. | Pass. Only solo piano can be heard throughout the audio (0:00-2:48). | Pass. Only solo piano can be heard throughout the audio (0:00-2:35). |
| C2 | The piece contains a recognisable allusion to Doctor Gradus: broken chords, minimal left hand, or sixteenth notes in the right hand. | Requirements Compliance | 8 | R2 should | Pass | Pass | Fail | Pass. Right-hand sixteenths over a sparse left hand from 0:12. | Pass. Minimalistic left-hand accompaniment with sixteenth notes in the right hand from 0:05. | Fail. Some progressions evoke Debussy around 0:07-0:09, but there is no reference to Doctor Gradus. |
| C3 | The piece opens in C major. | Requirements Compliance | 6 | R4 preferable | Pass | Pass | Fail | Pass. Opening bars in C major (C, E, G). | Pass. The first bars are objectively in C major (C, E, G chords). | Fail. Starts in E-flat minor; C major never appears. |
| C4 | At least one impressionist scale colour beyond plain major or minor is used (pentatonic, whole-tone, or a church mode). | Content Correctness | 6 | R7 should | Pass | Pass | Pass | Pass. Pentatonic passage at 1:20. | Pass. Whole-tone scale around 1:00. | Pass. D Dorian at the end, around 2:28, a church mode. |
| C5 | Avoids anachronistic idioms foreign to Debussy: pop chord loops, jazz swing, regular V7-I Classical cadences. | Content Correctness | 5 | R7 should | Pass | Pass | Fail | Pass. No such idioms across the piece. | Pass. None of these anachronistic idioms are heard. | Fail. Cadences at 0:49 and 1:16 evoke the Russian school; the piece also alternates Classical, Romantic, modern and atonal writing. |
| C6 | The piano timbre is a realistic acoustic piano throughout, not an obviously synthetic or electric tone. | Usability & Realism | 7 | expert nuance | Pass | Fail | Pass | Pass. Natural sustain and decay throughout, e.g. 2:40 final chord. | Fail. Sounds like an entry-level VST, not a realistic acoustic piano (sustain at 0:48). | Pass. Definitely sounds like a realistic acoustic piano. |
| C7 | The audio is free of audible flaws: no clipping, dropouts, clicks, stuck notes or noticeable noise floor. | Usability & Realism | 7 | expert nuance | Pass | Pass | Fail | Pass. No clipping or clicks heard 0:00-3:12. | Pass. No issues of that kind can be heard in the track. | Fail. Clips slightly around 1:02, likely from right-hand chords played too harshly. |
| C8 | Leading and trailing silence do not exceed 4 seconds each, with at least 1 second of silence at the end. | Usability & Realism | 4 | expert nuance | Pass | Pass | Fail | Pass. 0.8 s lead-in, 1.6 s tail. | Pass. Leading and trailing silence stay within 4 seconds (1.1 s and 2.0 s). | Fail. There is less than 1 second of silence at the end of the audio (0.3 s). |
| C9 | The piece contains long stretches (over 10 seconds) of static noodling with no melodic or harmonic direction. | Presentation & Aesthetics | -7 | expert nuance | Fail | Pass | Fail | Fail. Melodic direction is maintained throughout; no static stretch over 10 s. | Pass. The section between 1:00 and 1:30 has no clear melodic or harmonic direction. | Fail. No static noodling; the defect is absent. |
| C10 | At least one transition between phrases or sections is not smooth: abrupt cuts or unmotivated jumps. | Presentation & Aesthetics | -7 | expert nuance | Fail | Pass | Fail | Fail. Transitions at 0:58 and 2:05 are prepared; no abrupt cut. | Pass. The transition starting at 0:41 is too abrupt; around 1:08 the section feels disjointed. | Fail. The piece is well structured; the defect is absent. |

---

## 9. Alignment (STEP 10)

P = 53. RD = 53 (100%). AD1 = 46 - 14 = 32 (60.4%). AD2 = 23 (43.4%).
