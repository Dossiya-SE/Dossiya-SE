# CHATGPT_COMMAND_LIBRARY.md

## Command contract

These commands control the research-rendering system. Every render command inherits the mandatory editable-artifact contract from `CHATGPT_RENDER_CONTROLLER.md`.

## 1. Render

```text
Render Research Framework V3.

Use the current governing research architecture.
Make every panel mathematically meaningful.
Preserve all equations as editable LaTeX source.
Generate the canonical SVG master, convenience-editable PPTX, PNG, PDF,
render specification, data, provenance, QA report, and source bundle.
Do not declare RENDER_PASS unless reproduction succeeds.
```

## 2. Update without redesign

```text
Update Research Framework V3.

Change only: [target component].
Preserve all unaffected geometry, equations, object IDs, and semantic mappings.
Regenerate every required artifact and rerun QA.
```

## 3. Upgrade scientific maturity

```text
Upgrade Research Framework V3 to V4.

Replace illustrative objects with computed/observed objects where evidence exists.
Do not relabel illustrative or synthetic objects as observed.
Preserve editable SVG/PPTX outputs and the complete source bundle.
```

## 4. Render one mathematical subsystem

```text
Render only the uncertainty subsystem.

Use:
U_t = {x : (x-mu_t)^T Sigma_t^{-1}(x-mu_t) <= c}

Represent covariance geometrically.
Preserve equations.tex, research_data.json, SVG, PPTX, PNG, PDF,
manifest, QA report, and source bundle.
```

## 5. Audit

```text
Audit the latest research render.

Check:
- scientific semantics
- equation fidelity
- dimensional consistency where applicable
- stage completeness
- object-status provenance
- no silent raster flattening
- editable SVG availability
- editable PPTX availability
- source-generator availability for raster layers
- reproduction from frozen render_request.yaml
- manifest/hash agreement

Return PASS/FAIL for every gate.
```

## 6. Reference-fidelity audit

```text
Audit the latest render against the supplied reference.

Measure:
- dimensions
- bounding-box placement
- text/equation presence
- object count
- layout displacement
- pixel/perceptual similarity where meaningful

Do not equate perceptual similarity with mathematical equivalence.
```

## 7. Reproduce

```text
Reproduce the latest accepted render from SOURCE_BUNDLE.zip only.

Do not use cached final images as source.
Compare regenerated outputs with the manifest hashes or declared tolerances.
Fail closed if a required source, dependency, font reference, equation,
data object, or configuration is missing.
```

## 8. Downloadable release

```text
Prepare the latest render for download.

Return:
poster_EDITABLE.svg
poster_EDITABLE.pptx
poster.png
poster.pdf
render_request.yaml
equations.tex
research_data.json
manifest.json
qa_report.json
SOURCE_BUNDLE.zip
```

## 9. Daily short commands

```text
Render V4 and give me the editable bundle.
```

```text
Change only the validation panel, rerender, audit, and give me the editable bundle.
```

```text
Audit reproducibility and editable-source completeness.
```

```text
Reproduce from source and compare against the accepted release.
```

## 10. Fail-closed rules

The controller must stop `RENDER_PASS` when any of the following occurs:

- canonical SVG missing;
- PPTX missing;
- equation source missing;
- controlling research data/parameters missing;
- raster scientific layer lacks a source generator;
- manifest cannot identify the rendering inputs;
- QA contains an unresolved blocking failure;
- reproduction cannot be completed;
- a computed/observed claim is actually illustrative or synthetic;
- visual output materially contradicts the governing mathematical object.
