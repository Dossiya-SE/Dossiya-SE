# CHATGPT_RENDER_CONTROLLER.md

## Status

**Governing controller standard:** `CHATGPT-RENDER-CONTROLLER-V1.1`  
**Applies to:** every research-visual render, update, rerender, audit, or export initiated through ChatGPT or GitHub.

## Mission

Translate a natural-language research-visual request into a deterministic, scientifically traceable rendering specification and require an editable/reproducible artifact set.

The governing chain is:

\[
\text{research specification}
\rightarrow
\text{mathematical objects}
\rightarrow
\text{computation}
\rightarrow
\text{verification}
\rightarrow
\text{rendering}
\rightarrow
\text{audit}
\rightarrow
\text{editable release}
\]

A render is not complete when only a PNG exists.

## Mandatory editable-artifact contract

Every accepted render MUST produce:

| Artifact | Role |
|---|---|
| `poster_EDITABLE.svg` | Canonical fidelity/editability master |
| `poster_EDITABLE.pptx` | Convenience-editable presentation version |
| `poster.png` | High-resolution raster preview/export |
| `poster.pdf` | Publication/print output |
| `render_request.yaml` | Frozen render specification |
| `equations.tex` | Editable mathematical source |
| `research_data.json` | Data/parameters controlling the visual |
| `manifest.json` | Provenance, versions, hashes, render metadata |
| `qa_report.json` | Scientific, mathematical, visual, and reproducibility QA |
| `SOURCE_BUNDLE.zip` | Complete reproduction/editing package |

The invariant is:

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

### Canonical master

\[
\boxed{\text{SVG}=\text{fidelity master}}
\]

`poster_EDITABLE.svg` is authoritative for composition, geometry, labels, paths, scientific panels, and vector plots.

### Convenience master

\[
\boxed{\text{PPTX}=\text{convenience editing format}}
\]

`poster_EDITABLE.pptx` is required for practical editing, but it is not allowed to silently redefine the canonical geometry if PowerPoint cannot preserve an advanced SVG/optical construct exactly.

## No silent flattening

\[
\boxed{
\text{No scientific object may become an unexplained raster image.}
}
\]

When rasterization is technically required, the source bundle MUST preserve:

- source equation(s);
- parameters;
- input data;
- generation code;
- random seed if applicable;
- camera/view configuration;
- rendering configuration;
- generated raster;
- provenance/hash information.

Rasterized scientific content must remain regenerable.

## Mathematical-source preservation

For every mathematical element:

```text
visible equation
      ↓
equations.tex
      ↓
symbolic/numerical verification where applicable
      ↓
SVG/vector rendering
```

The displayed vector form does not replace the editable mathematical source.

## Scientific visual grammar

Default semantics:

| Visual element | Meaning |
|---|---|
| Node | research state/object |
| Arrow | information, dependency, or justified causal relation |
| Curve `gamma(t)` | trajectory |
| Surface `M` | model/admissible state space |
| Boundary `partial Omega` | constraint/validity boundary |
| Width/tube | uncertainty |
| Vector length | sensitivity/influence |
| Density | evidence strength |
| Convergence | verification |
| Optimization path | calibration |
| Model/observation comparison | validation |
| Closed admissible region | bounded conclusion |
| Faded/broken region | unsupported/out-of-domain state |

Do not use a visual encoding with a scientific meaning that conflicts with this grammar unless the render specification explicitly declares the alternative.

## Epistemic status labels

Every controlling object is internally classified as one of:

- `USER_SPECIFIED`
- `COMPUTED`
- `OBSERVED`
- `PUBLISHED`
- `CALIBRATED`
- `DERIVED`
- `ASSUMED`
- `SYNTHETIC`
- `ILLUSTRATIVE`
- `TO_BE_VALIDATED`

No object may silently change class.

## Required controller response

For a substantive request, resolve:

1. Intent
2. Scientific scope
3. Mathematical objects
4. Visual mapping
5. Data/parameter provenance
6. Assumptions
7. Rendering plan
8. QA/audit plan
9. Editable output plan

## RENDER_PASS gate

A render may declare `RENDER_PASS` only if all applicable gates pass:

\[
\boxed{
\text{RENDER_PASS}
\iff
\begin{cases}
\text{scientific QA}=\text{PASS}\\
\text{mathematical QA}=\text{PASS}\\
\text{visual QA}=\text{PASS}\\
\text{editable master exists}\\
\text{PPTX convenience master exists}\\
\text{source bundle exists}\\
\text{required provenance exists}\\
\text{reproduction test}=\text{PASS}
\end{cases}}
\]

A missing required artifact is a failed gate, not a warning.

## Acceptance philosophy

Priority order:

\[
\text{scientific meaning}
>
\text{mathematical correctness}
>
\text{traceability}
>
\text{editability}
>
\text{reproducibility}
>
\text{aesthetic polish}
\]

A visually impressive render that fails a required scientific or reproducibility gate does not pass.
