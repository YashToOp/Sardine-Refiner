# Sardine Refiner -- Rubric Writing Guide

> **Updated:** 2026-09-17 -- Initial build. How to fix, split, write and weight criteria so the set passes QC Dims 3-11, plus deliverable-type libraries for the implicit expectations and expert nuances that Dim 7 and Dim 11 demand. Used in pipeline.md STEP 7 and STEP 8.

---

## 1. What a good criterion looks like

Every criterion you keep, edit or add must pass all seven:

| # | Test | Fails if |
|---|---|---|
| 1 | **One check** | Text contains "and", a comma list, a slash, "including", "as well as", or two facts a grader could disagree on separately |
| 2 | **Exact** | Uses a vague adjective (appropriate, proper, good, clean, suitable, reasonable, correctly, well, nice, high quality) instead of a value, threshold or named element |
| 3 | **Self-contained** | A grader with only the brief, the inputs and the three deliverables could not decide Pass/Fail without asking you |
| 4 | **Sourced** | You cannot name where it comes from: a brief line (R#), script line (S#), provided file (F#), deliverable spec (D#), a professional standard, or an observed failure (E#) |
| 5 | **Golden-neutral** | It enforces a choice RD made that the brief never mandated, with no room for equally plausible alternatives |
| 6 | **Region-neutral** | It assumes a locale convention (units, date format, currency, spelling variant, regulation, paper size) the brief never declared |
| 7 | **Human-written** | It reads like generated text: stacked adjectives, "ensure that", "in order to", "effectively", "seamlessly", "robust" |

Then assign a category (one of six) and a weight band (from the brief's language).

---

## 2. Phrasing patterns

### 2.1 Literal requirement (Requirements Compliance, from R#, S#, D#)

```
The [deliverable] [is / contains / uses] [exact value from the brief].
```
- The track is delivered in MP3 format.
- The poster is sized 420 x 594 mm (A2 portrait).
- The headline reads "Summer Nights Market" exactly as written in the copy deck.
- The video runs between 0:55 and 1:05.

### 2.2 Comparative, RD as the bar (golden-neutral quality checks)

```
The [element] is at least as [quality] as RD.
```
- The typographic hierarchy is at least as clear as RD.
- The mix clarity is at least as good as RD.
- The dashboard loads and filters at least as smoothly as RD.

Use when quality must be judged and the brief gives no number. RD sets the level; you do not list every detail.

### 2.3 Lenient alternatives (golden-neutral where several choices are valid)

```
The [element] uses [A], [B], or [C].
```
- At least one impressionist scale colour beyond plain major or minor is used (pentatonic, whole-tone, or a church mode).
- The call to action uses a button, a link, or a QR code.

### 2.4 Threshold or window

```
[Measure] is between [x] and [y]. / [Measure] does not exceed [x].
```
- Leading silence does not exceed 4 seconds.
- Body text is set at 9 pt or larger.
- Contrast between body text and background is 4.5:1 or higher.

### 2.5 Presence and craft, split

Presence is cheap (Slightly Important). Craft is what the client pays for (Important).
- A footer with contact details is present. (+2)
- The footer contact details are legible at the delivered size. (+5)

### 2.6 Negative criterion (defect present = Pass)

```
The [deliverable] contains [defect], [observable detail].
```
- The audio contains audible clipping.
- The video contains at least one black frame between scenes.
- The layout contains text that runs off the page edge.
- The piece contains a stretch longer than 10 seconds with no melodic or harmonic direction.

Phrase the bad thing as happening. Under the current rule, Pass on a negative criterion means the flaw is present and the negative weight then hurts the score. Never write "avoids X" with a negative weight; either write "avoids X" with a positive weight, or "contains X" with a negative weight.

### 2.7 Per-element aesthetics (Presentation & Aesthetics)

Never "the design is professional". One criterion per element:
- Type is legible at the delivered size.
- Heading, subheading and body form a clear hierarchy.
- Elements align to a consistent grid.
- Spacing between elements is even.
- The colour palette is harmonious and matches the brand sheet.
- Text-to-background contrast is sufficient to read at a glance.
- Imagery is sharp with no visible pixelation or artefacts.
- The style is consistent across all scenes / pages / assets.

### 2.8 Functionality (run it)

```
When [action], [expected behaviour] occurs.
```
- When the "Reset" button is clicked, all filters clear.
- When the player collides with a wall, movement stops without the character clipping through.
- Each footer link opens the correct corresponding page.

### 2.9 Content correctness (recalculate it)

```
[Figure / statement] equals [value derived from the inputs].
```
- The Q2 total in the summary tile equals the sum of the April, May and June rows in the source sheet.
- The percentage in the caption matches the underlying count divided by the total.

### 2.10 Editability

- The source file is delivered with elements on separate layers, not flattened.
- Text remains live (editable) rather than outlined or rasterised.
- The project file opens in the stated tool without missing-asset warnings.
- Components are grouped and named so a designer can modify them.

### 2.11 Decomposing a subjective brief term (do not ignore it)

When the brief says photorealistic, refined, high-quality, well-proportioned or visually convincing, the word is a requirement. Break it into observable criteria:

```
"Photorealistic rendering" ->
  Lighting is believable for the stated time of day and sources.
  Scale and proportion of spaces, openings and furniture are correct.
  Materials respond to light plausibly (reflection, roughness, texture scale).
  Shadows and reflections are consistent with the light setup.
  Secondary elements (vegetation, people, props) are realistic where present.
  No visible geometry gaps, texture stretching, exposure blowouts or noise.
```

### 2.12 Exact vs approximate values

Keep the brief's own precision. "The ceiling height is 300 cm" becomes "Ceiling height is 300 cm (within the precision the file supports)". "The ceiling height is approximately 300 cm" becomes "Ceiling height is in the intended scale of about 300 cm"; add a numeric tolerance only when the brief, an input or a documented project convention supports one. Never quietly convert approximate into exact.

### 2.13 Evaluation source

When the package holds several assets (3D model, render, plan, DWG, PDF, material board), say which one the criterion is judged against: "In the 3D model, ...", "In the exterior render, ...". This prevents model/render conflicts in the verdicts.

### 2.14 Macro consistency (multi-asset)

"The renders represent the same overall proposal as the model (massing, layout logic, facade concept, version)." Fail it only for a proposal-level contradiction. A single window or wall mismatch belongs to its detailed criterion, never to the macro one as a second penalty.

---

## 3. Vague word replacement table

| Vague | Replace with |
|---|---|
| appropriate length | between [x] and [y] (the brief's window) |
| proper format | delivered as [format from brief] |
| good quality audio | free of audible clipping / dropouts / clicks |
| clean design | elements aligned to a consistent grid; spacing even |
| readable | legible at the delivered size; contrast 4.5:1 or higher |
| correct colours | uses the palette hex values from [brand file] |
| professional tone | no spelling or grammar errors; register matches the brief's audience ([named audience]) |
| works well | [specific behaviour] occurs when [specific action] |
| consistent | [element] is identical across [scene 1..n / all pages / all assets] |
| high resolution | at least [pixels or DPI from brief] |
| matches the brief | [name the specific requirement it matches] |
| suitable for [audience] | [the concrete property that makes it suitable] |

---

## 4. Splitting rules (Dim 9)

Split when:
- "and" joins two checkable facts
- a comma or slash list names several items
- one sentence covers presence and quality
- one sentence covers several assets, scenes or pages that could differ

Keep together only when the parts cannot be judged apart (each link opens its correct page; the caption matches its own image).

Do not over-atomise either. If several elements are meaningful only as one requested relationship or combination, grade the combination: "The colour palette is focused on cool blue, indigo and dark navy tones" is one criterion, not three colour-existence checks, unless the brief makes each colour independently mandatory. Split independent failure modes; keep dependent details together when splitting would distort what the brief asks for.

The opposite failure is under-penalisation: "The model matches the reference DWG" hides footprint, wall layout, openings, circulation and levels inside one verdict. When those can fail independently and the brief binds the task to the file, give each its own criterion.

Fast overlap test after splitting: if one specific error occurred, how many criteria would fail because of exactly that mistake? More than one means merge, narrow or rewrite.

| Compound | Split |
|---|---|
| "A complete, playable full track is delivered in MP3 format and runs approximately two minutes." | complete playable audio file / MP3 format / duration approximately two minutes |
| "Footer links to the clinic's social media correctly: Instagram, LinkedIn, and YouTube." | Instagram link present / LinkedIn link present / YouTube link present / each link opens the correct page |
| "The logo is placed top-left at the right size with correct colours." | logo top-left / logo at least [x] mm wide / logo uses brand hex values |
| "All six script steps appear in order with matching visuals." | all six script steps appear / script steps appear in the brief's order / each step's visual matches its text |

Splitting is also how you reach 30. Split first, invent later.

---

## 5. Category decision tree (Dim 17 format)

1. Does the brief or an input file state it literally? -> **Requirements Compliance**
2. Is it about how it looks or sounds as craft? -> **Presentation & Aesthetics**
3. Is it about what happens when you use it? -> **Functionality**
4. Is it a fact or figure you can verify against the inputs? -> **Content Correctness**
5. Is it something a paying client assumes without saying? -> **Usability & Realism**
6. Is it about whether a designer can modify the file later? -> **Editability**

When two fit, pick the one that names what you will actually check. A requirement that is also aesthetic (e.g. "use the brand palette") is Requirements Compliance when the brief mandates it, Presentation & Aesthetics when you are judging harmony.

---

## 6. Weight decision tree (Dim 4)

1. Find the brief's word for it.
   - must / only / required / never / hard constraint / dead file -> **8 to 10** (or -8 to -10 for the defect)
   - should / expected / standard practice / client would send it back -> **4 to 7** (or -4 to -7)
   - preferable / nice to have / polish / a client would notice but accept -> **1 to 3** (or -1 to -3)
2. If the brief is silent, ask: would a paying client reject the deliverable over this? Yes -> 8-10. Complain -> 4-7. Notice -> 1-3.
3. Keep siblings consistent: three links in a footer get the same weight; three script steps get the same weight.
4. Re-check every criterion that AD1 or AD2 fails. Those are the ones QC audits for band errors. A Critical vs Slightly mismatch there is the counted error.
5. Do not inflate weights to make the totals tell the story you want. Fix the story instead.

Example calibration from the course: "solo piano only" (must) = 10; "subtle allusion to Doctor Gradus" (should) = 8; "preferable to begin in C major" = 6; "impressionist scale colour" (expected of the style) = 6; "avoids anachronistic idioms" = 5; realistic timbre (expert expectation) = 7; no audible flaws = 7; silence window = 4; static noodling present = -7; abrupt transition present = -7.

---

## 7. Golden-neutrality decision (Dim 5)

For every criterion that fixes a specific choice, ask:
1. Did the brief or an input file mandate this exact choice? -> keep literal.
2. Is RD's choice one of several a professional could reasonably make? -> rewrite comparative ("at least as good as RD") or lenient (list alternatives).
3. Is the choice pure taste (a specific hue, a specific key, a specific font)? -> drop it, or fold into a craft criterion ("colours are harmonious and consistent").

Keep the share of arbitrary-choice criteria at or below 10% of the set. Zero is better.

---

## 8. Region-assumption traps (Dim 8)

Do not grade on any of these unless the brief states it:
- date format (DD/MM vs MM/DD), 12h vs 24h time
- units (mm vs inches, kg vs lb, Celsius vs Fahrenheit)
- currency symbol or placement
- spelling variant (colour/color, organise/organize)
- paper size (A4 vs Letter, A2 vs Tabloid)
- phone number or address format
- legal, accessibility or regulatory standards specific to a country
- voltage, plug, road-side, tax rates, holidays

If the brief is silent, write the criterion in a locale-neutral way or leave it out.

---

## 9. Reaching 30 with full coverage: the expansion ladder

Climb in this order. Stop when every coverage-matrix row has a criterion and the count is at least 30. Never pad with duplicates.

1. **Explicit requirements (R#).** One criterion per checkable fact. Split compounds.
2. **Deliverable spec (D#).** Format, count, dimensions, resolution, duration, naming.
3. **Script and copy (S#).** Each required line present; wording verbatim; order preserved.
4. **Provided material (F#).** Each input file actually used; used as instructed (as reference, as asset, as data).
5. **Implicit professional expectations** for the deliverable type (section 10 libraries). Pick the 8-15 that matter for this brief.
6. **Expert nuances.** The 3-6 checks only a professional in this field would make.
7. **Observed failures (E#).** One negative criterion per defect you saw in AD1 or AD2 that no positive criterion already catches.
8. **Justification claims.** Every praise or criticism in your three comparison paragraphs must map to a criterion. Add what is missing.
9. **Per-element aesthetics** if design is central (Dim 11): one criterion per element.
10. **Functionality per behaviour** if behaviour matters: one criterion per action you tested.
11. **Editability** if a client would modify the file.

Sanity on shape: categories spread in proportion to the brief; positive criteria carry most of the points; negatives exist for real, observed or strongly tempting defects.

---

## 10. Deliverable-type libraries

Each library lists implicit expectations (what a paying client assumes), expert nuances (what only a professional flags), typical negative criteria, functionality checks where relevant, and editability checks. Pick what fits the brief; rewrite in the brief's exact terms.

### 10.1 Audio: music track, jingle, score

**Implicit expectations**
- Complete, playable file in the requested format and sample rate
- Duration inside the requested window
- No audible clipping, distortion, dropouts, clicks or pops
- No noticeable noise floor or hiss
- Steady tempo (no unintended drift) unless rubato is stylistic
- Clear structure appropriate to the genre (intro, verse, chorus, bridge, outro, or the classical equivalents)
- Consistent loudness across sections; no sudden level jumps
- Clean start and ending; no cut-off decay; controlled leading and trailing silence
- Instrument timbres realistic for the stated instrumentation (not obviously synthetic when acoustic is implied)
- Key, mode or tonality as requested; modulations intentional and resolved

**Expert nuances**
- Stereo image balanced; no phase cancellation when summed to mono
- Frequency balance: no boomy low end or harsh highs
- Transitions between sections are prepared (no abrupt cuts or unmotivated jumps)
- Melodic and harmonic direction throughout; no long static stretches
- Reverb and effects consistent with the space implied by the brief
- Metadata and file naming as requested

**Typical negatives**
- Contains audible clipping / a dropout / a click
- Contains a stretch over 10 seconds with no melodic or harmonic direction
- Contains an abrupt, unprepared transition
- Contains an instrument or voice the brief excluded
- Ends with the final note cut off

**Editability**
- Stems or project file delivered when requested; tempo and key stated

### 10.2 Voice-over, podcast, spoken audio

- Script read verbatim (or as instructed); no skipped or added lines
- Pronunciation of names and terms correct per the brief
- Pace inside the requested words-per-minute or duration
- No mouth clicks, breaths edited to taste, no plosives
- Consistent mic distance and tone across takes
- Room tone consistent; no background noise
- Levels normalised to the requested standard if given
- Negatives: contains a mispronounced named term; contains a section with clipped audio; contains an unedited retake

### 10.3 Static graphic design: poster, flyer, social post, banner

**Implicit expectations**
- Correct dimensions, orientation and resolution for the stated use (print DPI, screen pixels)
- Bleed and safe margins present for print
- All copy from the brief present, verbatim, correctly spelled
- Type legible at the delivered size; body size not below a readable floor
- Clear hierarchy: headline, subhead, body, call to action
- Consistent alignment to a grid; even spacing
- Palette matches the brand sheet or brief; colours harmonious
- Adequate text-to-background contrast
- Imagery sharp; no pixelation, stretching or artefacts
- Logo undistorted, at legible size, with clear space
- No placeholder text (lorem ipsum) or template artefacts

**Expert nuances**
- Kerning and tracking consistent; no widows or orphans in body copy
- Optical alignment of icons and type
- Colour mode correct for the use (CMYK for print, RGB for screen)
- Fonts embedded or outlined for print; licensed fonts
- Visual weight balanced; focal point where the brief wants attention

**Typical negatives**
- Contains text that runs off the page or into the bleed
- Contains a spelling error in the supplied copy
- Contains a stretched or low-resolution image
- Contains an unrequested element (stock badge, watermark)

**Editability**
- Source file with separate layers, live text, linked or packaged assets

### 10.4 Logo and brand identity

- Works at small size (favicon) and large size (signage); legible at the smallest stated use
- Works in single colour and reversed on dark
- Clear space and minimum size defined if asked
- Vector delivered when requested; no raster-only logo
- Colour values specified (hex, CMYK, Pantone if asked)
- Distinct from the reference brands the brief names as competitors
- Negatives: contains a raster effect that breaks in vector; contains text as outlines when live text was required
- Editability: vector source with grouped, named layers

### 10.5 Illustration and character art

- Subject and attributes from the brief present (pose, features, clothing, colours)
- Style matches the reference or named style
- Anatomy and proportion consistent within the chosen style
- Line quality consistent; no stray marks
- Lighting and shadows consistent with one light source
- Background as requested (transparent, solid, scene)
- Resolution and format as requested
- Negatives: contains an extra or missing limb/finger; contains an unrequested watermark; background flattened when transparency was required
- Editability: layers for line, colour, shading, background

### 10.6 Photo editing and retouching

- Requested edits applied (background removal, colour correction, object removal)
- Edges clean; no halo, no leftover background pixels
- Skin and texture natural; no plastic smoothing
- Colour balance consistent across a set
- Original resolution preserved; no added compression artefacts
- Format and naming as requested
- Negatives: contains a visible cloning repeat; contains an unrequested crop

### 10.7 Video, animation, motion graphics

**Implicit expectations**
- Resolution, frame rate, aspect ratio and codec as requested
- Duration inside the window
- Scenes follow the script order; every script step present
- On-screen text legible and held long enough to read
- Audio in sync with visuals; levels consistent
- Transitions smooth and motivated; no black frames or freezes
- Consistent visual style across scenes
- Safe margins respected for titles and lower thirds
- Captions accurate if requested
- End card or call to action as requested

**Expert nuances**
- Easing on motion; no linear robotic moves unless stylistic
- Colour grade consistent across cuts
- Typography animates legibly (no motion blur on small text)
- Audio ducking under voice-over

**Typical negatives**
- Contains a black frame between scenes
- Contains on-screen text that is unreadable against its background
- Contains a scene where audio and visuals are out of sync
- Contains three or more scenes that reuse the same layout when the brief asked for variety

**Editability**
- Project file with layers/comps, fonts and assets packaged

### 10.8 Presentation deck

- Slide count and order as requested; every required section present
- One message per slide; headline states the takeaway
- Consistent template: margins, fonts, colours across all slides
- Charts labelled with axes, units and source
- Figures match the source data
- No spelling or grammar errors; no placeholder text
- Images sharp; icons consistent in style
- Speaker notes if requested
- Negatives: contains a slide with text overflow; contains a chart with no axis labels; contains inconsistent font across slides
- Editability: native deck file, not a flattened PDF; charts as editable objects

### 10.9 Document, report, copywriting

- Structure and sections as requested; word or page count inside the window
- Audience and tone as stated in the brief
- Every required point covered; no off-brief content
- Facts consistent with provided inputs; figures correct
- Spelling, grammar, punctuation clean; consistent style (one spelling variant, one heading style)
- Headings, lists and tables formatted consistently
- Citations or sources where the brief asks
- Negatives: contains a factual claim contradicting the input data; contains a section the brief excluded; contains inconsistent terminology for the same thing
- Editability: delivered in the requested editable format

### 10.10 Website, landing page, email template

**Implicit expectations**
- Loads without errors; no broken images or 404 links
- Every navigation link and button goes where its label says
- Responsive at the requested breakpoints; no horizontal scroll on mobile
- Copy from the brief present and correct
- Forms validate and submit (or show the requested behaviour)
- Readable type, sufficient contrast, sensible spacing
- Brand palette and logo used as specified
- No placeholder text or dummy images
- Favicon, page title, meta description if requested

**Expert nuances**
- Semantic headings in order; images have alt text
- Keyboard focus visible; tab order logical
- Performance reasonable (no multi-megabyte hero image)
- Email: renders in the named clients; width inside the safe limit; alt text on images; plain-text fallback

**Typical negatives**
- Contains a link that returns an error page
- Contains overlapping elements at the mobile breakpoint
- Contains lorem ipsum
- Contains console errors on load

**Editability**
- Source files organised; styles not inline-duplicated; components reusable

### 10.11 App UI, prototype, dashboard

- Every screen or state from the brief present
- Navigation between screens works as described
- Controls behave: filters filter, sorts sort, toggles toggle
- Data shown is correct against the input data; totals reconcile
- Charts have titles, axes, units, legends; colours distinguishable
- Empty, loading and error states handled if requested
- Consistent component styling (buttons, inputs, cards)
- Readable at the stated screen size
- Negatives: contains a control that does nothing; contains a figure that does not match the source; contains inconsistent button styles
- Editability: design file with components and styles; code with clear structure

### 10.12 Spreadsheet and data processing

- Output columns and structure as requested
- Formulas live where calculations are required (not pasted values)
- Totals and subtotals reconcile with the source
- Units, currencies and date formats consistent within the sheet
- Edge cases handled (blank rows, duplicates, negative values) as the brief states
- Named ranges or sheet names as requested
- No #REF, #VALUE or circular references
- Negatives: contains a hard-coded number where a formula is required; contains a total that differs from the recalculated sum; contains a broken reference
- Editability: not flattened to values; assumptions documented

### 10.13 Code, script, automation

- Runs without error on the stated inputs
- Produces the requested output format
- Handles the edge cases named in the brief
- Readable structure; functions named for what they do
- No hard-coded paths or secrets
- Documented usage (README or docstring) if requested
- Tests present if requested and passing
- Negatives: contains a crash on the sample input; contains an unrequested dependency; contains dead code left from generation
- Editability: modular, configurable, versioned

### 10.14 Game and interactive

- Launches and reaches the first playable state
- Controls respond as described; no input lag beyond playability
- Win, lose and restart states work
- No crashes, soft-locks or clipping through geometry
- Instructions or onboarding present if requested
- Assets consistent in style and resolution
- Audio cues fire on the right events
- Difficulty and pacing as the brief describes
- Negatives: contains a soft-lock; contains a placeholder asset; contains a collision bug
- Editability: project file with organised scenes and assets

### 10.15a Architecture / interior design (model, renders, plans, DWG)

Full library with reference-authority rules in ArchitectureReviewGuide.md section 9. Headline items:
- Every requested file present, opens in the stated tool, current version only (no outdated duplicates)
- Units and scale match the brief or reference file
- Reference geometry matched to the extent the brief binds it: footprint, exterior walls, partitions, openings, vertical circulation, levels, site placement, each its own criterion when independently failable
- Stated dimensions exact when worded exactly, in scale when worded approximately
- Requested materials, palette (as a combination), furniture and fixtures present as described
- Render realism decomposed: lighting, scale and proportion, material response, shadows and reflections, secondary elements, artifacts
- Assets represent one proposal (macro criterion, proposal-level only); plans, sections, elevations and material board agree with the model
- Circulation continuous, openings usable
- Layered, named, editable model; no merged geometry when a working model was requested
- Negatives: outdated version presented as current; merged geometry; visible render artifact; missing reference-defined opening; file fails to open

### 10.15 3D model and render

- Subject matches the brief; proportions correct
- Polygon count or resolution as requested
- Textures and materials applied, no missing textures
- UVs clean if requested; no stretching
- Lighting consistent; render at requested resolution and format
- Named, organised hierarchy
- Negatives: contains a missing-texture pink surface; contains non-manifold geometry if the brief requires print-ready
- Editability: native scene file with materials and lights intact

---

## 11. Worked expansion: from a poster brief to 30 criteria (illustrative)

**Illustrative brief (not a real task):** "Design an A2 portrait event poster using the provided layout template (layout.ai). Use the copy in copy.txt exactly. Use the brand palette in brand.pdf. Deliver a print-ready PDF and the editable source."

| ID | Criterion | Category | Weight | Source |
|---|---|---|---|---|
| C1 | The poster is sized 420 x 594 mm portrait. | Requirements Compliance | 9 | D1 |
| C2 | A print-ready PDF is delivered. | Requirements Compliance | 9 | D2 |
| C3 | An editable source file is delivered. | Editability | 8 | D3 |
| C4 | The layout follows the zones defined in layout.ai. | Requirements Compliance | 8 | F1 |
| C5 | The headline text matches copy.txt exactly. | Requirements Compliance | 9 | S1 |
| C6 | The date and venue lines match copy.txt exactly. | Requirements Compliance | 9 | S2 |
| C7 | The call-to-action line from copy.txt is present. | Requirements Compliance | 7 | S3 |
| C8 | Only the hex colours listed in brand.pdf are used for type and backgrounds. | Requirements Compliance | 8 | F2 |
| C9 | The logo from brand.pdf is present. | Requirements Compliance | 8 | F2 |
| C10 | The logo is undistorted (aspect ratio preserved). | Presentation & Aesthetics | 6 | professional |
| C11 | The logo has clear space at least equal to its height on all sides. | Presentation & Aesthetics | 3 | professional |
| C12 | The PDF includes 3 mm bleed on all sides. | Usability & Realism | 6 | professional (print) |
| C13 | No text sits inside the outer 10 mm safe margin. | Usability & Realism | 5 | professional (print) |
| C14 | The PDF is in CMYK colour mode. | Usability & Realism | 5 | professional (print) |
| C15 | Fonts are embedded or outlined in the PDF. | Usability & Realism | 6 | professional (print) |
| C16 | Raster images are at least 300 DPI at placed size. | Presentation & Aesthetics | 6 | professional (print) |
| C17 | The headline is legible from 3 metres (cap height 40 mm or larger). | Presentation & Aesthetics | 7 | expert |
| C18 | Body text is set at 12 pt or larger. | Presentation & Aesthetics | 5 | expert |
| C19 | Headline, subhead and body form a clear three-level hierarchy. | Presentation & Aesthetics | 6 | expert |
| C20 | Elements align to a consistent grid. | Presentation & Aesthetics | 5 | expert |
| C21 | Spacing between text blocks is even. | Presentation & Aesthetics | 4 | expert |
| C22 | Text-to-background contrast is at least 4.5:1 for body text. | Presentation & Aesthetics | 6 | expert |
| C23 | The overall composition is at least as balanced as RD. | Presentation & Aesthetics | 5 | comparative |
| C24 | The visual style is at least as polished as RD. | Presentation & Aesthetics | 5 | comparative |
| C25 | The source file keeps type as live text. | Editability | 6 | professional |
| C26 | The source file keeps background, imagery and type on separate layers. | Editability | 6 | professional |
| C27 | The poster contains a spelling error in the supplied copy. | Content Correctness | -8 | observed / tempting |
| C28 | The poster contains text that runs into the bleed or off the page. | Usability & Realism | -7 | observed / tempting |
| C29 | The poster contains a stretched or pixelated image. | Presentation & Aesthetics | -6 | observed / tempting |
| C30 | The poster contains placeholder text or template artefacts. | Content Correctness | -8 | observed / tempting |

Shape check: 30 criteria; 26 positive, 4 negative; every explicit requirement covered (C1-C9); print expertise covered (C12-C16); aesthetics per element (C17-C24); editability (C3, C25, C26); comparative golden-neutral checks (C23, C24) at 2 of 30 = 7%, under the 10% ceiling; no "and"; no vague adjectives; no region assumption beyond what the A2 spec itself implies.

---

*End of Rubric Writing Guide.*
