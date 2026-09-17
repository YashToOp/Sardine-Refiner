# Sardine Refiner -- Justification Guide

> **Updated:** 2026-09-17 -- Initial build. The course calls justifications "the part that matters most" and QC grades them on Dim 2 (comparison justifications) and Dim 13 (criterion justifications). This guide gives the shape, templates and language rules for both kinds, plus the two gate statements.

---

## 1. The two kinds of justification

| Kind | Where | How many | QC dimension |
|---|---|---|---|
| Comparison justification | After the five ratings in each of the three comparisons | 3 per task | Dim 2 (and Dim 1 via "adequately supports") |
| Criterion verdict justification | Under each Yes/No for RD, AD1, AD2 on every rubric card | 3 per criterion, 90+ per task | Dim 13 (and Dim 12) |

Plus two one-off statements: the Gate 1 "No" gap statement and the Gate 2 "Yes" explanation.

---

## 2. Comparison justification (one paragraph per comparison)

### 2.1 The shape

For every claim: **name the dimension -> point to concrete evidence with a location -> compare it to the other deliverable -> say why a client would care.**

Then close with the net direction and what the gap is about.

### 2.2 Template

```
[Brief anchor]: the brief asks for [format / script steps / palette / length]; [X] meets [which] and [Y] meets [which].
Realism: [X] [observed fact] at [location]; [Y] [observed fact] at [location]. [Client impact].
Design & UI/UX Quality: ...
Professionalism: ...
Coherence & Continuity: ...
Multi-Asset Consistency: ... (or: Only one file was delivered, so multi-asset consistency does not apply.)
Overall [X] is [a little behind / clearly behind / comparable to / a little ahead of] [Y], and the gap is about [design / content / function / polish], not [the other].
```

Write it as flowing prose, not a labelled list, but make sure every dimension is named.

### 2.3 Worked example (from the course, RD vs AD1)

> "AD1 follows the brief as well as RD: flat design, and all six script steps in order. The design is weaker: three scenes use the same layout, and the labels at 0:22 and 0:41 are hard to read against the green background. Only one file was delivered, so multi-asset consistency does not apply. Overall AD1 is a little behind RD, and the gap is about design, not content."

Why it passes: brief anchored (flat design, six script steps), evidence located (0:22, 0:41, three scenes), compared (as well as RD / weaker than RD), N/A dimension stated, direction and cause in the last sentence.

### 2.4 Rejected shapes (Dim 2 Fail)

- "The reference is better overall."
- "AD1 looks unprofessional."
- "Both are fine, so I gave it a 4."
- "Design is bad, colours are off."

No evidence, no comparison, no location. A reviewer cannot check any of it.

### 2.5 Rules

1. Cover all five dimensions by name. State N/A explicitly when a dimension does not apply.
2. At least one located evidence point per dimension you scored away from 4.
3. Compare, do not describe: every sentence should say something about both deliverables or say why only one is affected.
4. The direction of the paragraph must match the numbers. If four dimensions are 3 and one is 5, the paragraph says RD is slightly ahead overall and names the one area where the alternative wins.
5. Extremes need extra evidence: a 1, 2, 6 or 7 needs at least two located facts for that dimension.
6. In AD1 vs AD2, write about AD1 and AD2 only. Do not drag RD in except as the brief's bar.
7. **Every claim needs a rubric.** After writing, list each praise or criticism and map it to a criterion ID in the worksheet. Missing -> add the criterion.
8. Length: roughly 90 to 200 words. Long enough to locate evidence for five dimensions, short enough to read in a minute.

### 2.6 Dimension prompts (what to look for)

| Dimension | Ask |
|---|---|
| Realism | Does it look, sound or feel true-to-life for the medium? Timbre, lighting, texture, motion, voice, data plausibility. |
| Design & UI/UX Quality | Layout, hierarchy, legibility, spacing, colour, navigation, controls, flow. |
| Professionalism | Would a paying client accept this as finished work? Polish, correctness, absence of amateur tells. |
| Coherence & Continuity | Does it hold together from start to end? Order, consistency of style and logic, no contradictions, transitions. |
| Multi-Asset Consistency | Across files, scenes, pages or components: same palette, type, tone, naming, data. N/A if one file. |

---

## 3. Criterion verdict justification (one paragraph per verdict)

### 3.1 The shape

**Verdict -> observed fact -> location -> relation to the criterion's value or threshold.** One paragraph per verdict, not a blurb per section. The reviewer must be able to check it in seconds.

### 3.2 Template

```
[Pass / Fail]. [What was observed] at [location]. [How it meets or misses the criterion's value or threshold].
```

### 3.3 Examples (from the course, corrected for current pass semantics)

Positive criterion "The piece opens in C major." (weight 6)
- AD1, Pass: "The first bars are objectively in C major (C, E, G chords)."
- AD2, Fail: "Starts in E-flat minor; C major never appears."

Positive criterion "The audio is free of audible flaws: no clipping, dropouts, clicks, stuck notes or noticeable noise floor." (weight 7)
- AD1, Pass: "No issues of that kind can be heard in the track."
- AD2, Fail: "Clips slightly around 1:02, likely from right-hand chords played too harshly."

Negative criterion "The piece contains long stretches (over 10 seconds) of static noodling with no melodic or harmonic direction." (weight -7). Pass = the flaw happened.
- AD1, Pass: "The section between 1:00 and 1:30 has no clear melodic or harmonic direction, so the flaw is present."
- AD2, Fail: "No static stretch over 10 seconds is present; the piece keeps melodic direction throughout."

Requirements criterion "The track is delivered in MP3 format." (weight 9)
- RD, Pass: "File RD_final.mp3 is an MP3 (checked the file extension and playback)."

### 3.4 Rules

1. The verdict word comes first, then the evidence.
2. Always a location: timestamp (mm:ss), page or slide number, screen or section name, region of the frame, file name, cell or line.
3. The paragraph must agree with the verdict. Under a negative criterion, a Pass paragraph describes the flaw being present; a Fail paragraph describes its absence.
4. Do not copy one paragraph across RD, AD1 and AD2 unless the evidence is genuinely identical, and even then name the location for each deliverable.
5. Measure thresholds: "runs 2:37" beats "about two and a half minutes".
6. Say what you checked, not what you assume: "opened the source file; layers are flattened into one" beats "probably flattened".
7. Two or three sentences is normal. One sentence is fine when the fact is simple ("Delivered as .mp3; verified by file type.").

### 3.5 Location conventions

| Medium | Location format |
|---|---|
| Audio, video | mm:ss or mm:ss-mm:ss |
| Document, deck | page N, slide N, section title |
| Web, app | screen or page name, component name, breakpoint |
| Image, poster | region (top-left, headline, footer), element name |
| Spreadsheet | sheet name, cell or range |
| Code | file name, function name, line number |
| Multi-file | file name first, then the location inside it |

---

## 4. Gate statements

### 4.1 Gate 1 "No" (brief insufficient)

```
The brief is not sufficient to evaluate and compare the deliverables. Missing: [the unstated constraint / the input file the brief references but did not provide / the requirement that cannot be checked]. Without it, [which requirement or dimension] cannot be judged for [RD / AD1 / AD2].
```

Name the gap precisely. "The brief is vague" is not a gap statement.

### 4.2 Gate 2 "Yes" (RD is worse)

```
RD is worse than [AD1 / AD2]. On [dimension], RD [observed fact at location] while [ADx] [observed fact at location]. On [dimension], ... The brief asks for [requirement]; [ADx] meets it and RD does not. A client would prefer [ADx] because [impact].
```

Same evidence-located discipline as a comparison justification. The finding is that the reference lost; make it checkable.

---

## 5. Language rules (all justifications)

- Plain words. "used", "shows", "runs", "missing", "reads". Avoid "leverages", "showcases", "seamlessly", "robust", "comprehensive", "delve".
- No hedging where you checked: not "seems to clip", but "clips at 1:02".
- No em dashes. Use commas, periods, colons or parentheses.
- Numbers exact: durations, counts, sizes, page numbers.
- Consistent labels: RD, AD1, AD2, never "the human one", "the first model", "version B".
- One idea per sentence. A reviewer scans hundreds of these.
- Do not restate the criterion; state the evidence.

---

## 6. Self-check before submit

**Comparison justifications (x3)**
- [ ] Five dimensions named, N/A stated where relevant
- [ ] Brief anchored (what was asked, who met it)
- [ ] Every claim located
- [ ] Both deliverables compared
- [ ] Last sentence states direction and cause, matching the numbers
- [ ] Every praise or criticism mapped to a criterion ID

**Criterion justifications (x3 per criterion)**
- [ ] Verdict first
- [ ] Location present
- [ ] Agrees with the verdict (negatives: Pass = flaw present)
- [ ] Not copy-pasted across the three without re-checking
- [ ] Thresholds measured, not eyeballed

---

*End of Justification Guide.*
