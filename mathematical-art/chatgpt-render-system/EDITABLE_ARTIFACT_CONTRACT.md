# EDITABLE_ARTIFACT_CONTRACT.md

## Contract ID

`EDITABLE-RESEARCH-VISUAL-CONTRACT-V1.0`

## Governing rule

Every accepted research render must be delivered as an editable, reproducible release rather than as a flattened image only.

\[
\boxed{
\text{Every render}
\Rightarrow
\text{editable master}
+
\text{publication outputs}
+
\text{reproducibility source}
}
\]

## Required artifacts

1. `poster_EDITABLE.svg` — canonical fidelity/editability master.
2. `poster_EDITABLE.pptx` — convenience-editable presentation derivative.
3. `poster.png` — high-resolution preview/raster export.
4. `poster.pdf` — publication/print export.
5. `render_request.yaml` — frozen specification.
6. `equations.tex` — editable mathematics.
7. `research_data.json` — controlling data and parameters.
8. `manifest.json` — provenance, versions, hashes.
9. `qa_report.json` — scientific, mathematical, visual, editability, and reproducibility QA.
10. `SOURCE_BUNDLE.zip` — complete reproduction/editing package.

## Canonical authority

`poster_EDITABLE.svg` is the visual authority.

`poster_EDITABLE.pptx` is a required convenience derivative. If PowerPoint cannot preserve an advanced construct exactly, the difference must be documented rather than silently redefining the canonical SVG.

## No silent flattening

No scientific object may become an unexplained raster.

If rasterization is required, retain all inputs and generator code necessary to regenerate that raster.

## Pass condition

`RENDER_PASS` is prohibited until every required artifact exists and the reproduction test passes.

## Reproduction principle

The accepted render must be reproducible from the frozen source package without using the accepted final PNG/PDF/SVG as an input substitute.
