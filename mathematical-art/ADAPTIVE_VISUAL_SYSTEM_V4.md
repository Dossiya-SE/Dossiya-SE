# Adaptive Mathematical Visual System — V4

## Purpose

This document is the theme, rendering, accessibility, and evidence-status contract for all mathematical visuals across the Dossiya-SE GitHub profile.

The objective is **one mathematical artifact with multiple faithful render states**, not separate hand-redrawn figures whose semantics can drift.

```math
\boxed{
\text{source / model}
\to
\text{verified mathematical object}
\to
\text{semantic visual layers}
\to
\text{adaptive SVG}
\to
\{\text{light},\text{dark},\text{print}\}
}
```

A theme switch may change only presentation variables. It must never alter numerical values, geometry, topology, equations, evidence state, line meaning, ordering, or scientific conclusion.

---

## 1. Adaptive rendering rule

The canonical GitHub master is SVG with an internal color-token system and a `prefers-color-scheme` media query.

```css
:root {
  --bg: #ffffff;
  --panel: #f8fafc;
  --fg: #0f172a;
  --muted: #475569;
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg: #07111f;
    --panel: #0e1d31;
    --fg: #eaf1f8;
    --muted: #9eb0c3;
  }
}
```

The same geometry and text positions are used in both modes. Only semantic color tokens, shadows, and contrast-preserving decoration may change.

### Required render profiles

- `github_adaptive` — one SVG responding to system light/dark preference;
- `publication_white` — white background, print-first contrast;
- `presentation_light` — white / very light background, 16:9;
- `presentation_dark` — dark background, 16:9;
- `journal_vector` — SVG/PDF, no rasterized equations;
- `web_interactive` — HTML/WebGL where interaction is scientifically meaningful.

---

## 2. Semantic color ontology

Color carries a declared meaning and is reinforced by line style, label, or symbol so that meaning is not encoded by color alone.

| Role | Light mode | Dark mode | Secondary cue |
|---|---:|---:|---|
| source mathematics / theorem | `#4338CA` | `#A5B4FC` | square / indigo rule |
| observed / official evidence | `#0369A1` | `#38BDF8` | solid marker |
| state / dynamics | `#1D4ED8` | `#60A5FA` | solid trajectory |
| interface / coupling | `#7E22CE` | `#C084FC` | linked nodes |
| hazard / violation | `#B91C1C` | `#FB7185` | dashed red boundary |
| uncertainty / inference | `#B45309` | `#FBBF24` | band / dotted contour |
| viability / admissibility | `#047857` | `#34D399` | closed green set |
| recovery / control | `#0F766E` | `#5EEAD4` | directed teal path |
| optimization / decision | `#A16207` | `#FACC15` | Pareto/frontier marker |
| computed / simulation | `#475569` | `#CBD5E1` | code / numeric label |
| hypothesis / unvalidated transfer | `#BE185D` | `#F472B6` | dashed magenta |

Neutral background and grid tokens are chosen separately for each theme.

---

## 3. Native-mathematics rule

A high-rigor visual is generated from the mathematical object whenever practicable.

```math
\mathbf r(u,v)
\to
\partial_\alpha\mathbf r
\to
g_{\alpha\beta}
\to
\Gamma^\alpha_{\beta\gamma}
\to
K,H
\to
\gamma(s)
\to
\text{verified geometry}
\to
\text{render}
```

For differential geometry, surface vertices, tangent fields, normals, curvature values, and geodesics must be generated from code or a declared symbolic representation when the figure is promoted beyond conceptual status.

For infrastructure, finance, ML, energy, or decision systems, the visualized quantity must likewise have a defined model/data provenance.

---

## 4. Theme invariants

For each adaptive figure `F`, let `R_L(F)` and `R_D(F)` be its light- and dark-mode renders. The following must remain invariant:

```math
\mathcal I(F)=
\{\text{equations},\text{geometry},\text{topology},\text{labels},\text{values},\text{evidence states}\}.
```

Therefore

```math
\boxed{
\mathcal I(R_L(F))=\mathcal I(R_D(F))
}
```

Only visual style parameters may vary.

---

## 5. Differential-geometry rendering contract

When a surface is shown as source mathematics, the following quantities should be generated or explicitly specified:

```math
\mathbf e_1=\partial_u\mathbf r,
\qquad
\mathbf e_2=\partial_v\mathbf r,
```

```math
\mathbf n=
\frac{\mathbf e_1\times\mathbf e_2}
{\lVert\mathbf e_1\times\mathbf e_2\rVert},
```

```math
g_{\alpha\beta}=\mathbf e_\alpha\cdot\mathbf e_\beta,
```

```math
\Gamma^\alpha_{\beta\gamma}
=\frac12g^{\alpha\delta}
\left(
\partial_\beta g_{\gamma\delta}
+\partial_\gamma g_{\beta\delta}
-\partial_\delta g_{\beta\gamma}
\right),
```

```math
K=\frac{eg-f^2}{EG-F^2},
\qquad
H=\frac{eG-2fF+gE}{2(EG-F^2)}.
```

A curve labeled `geodesic` must satisfy the declared geodesic system numerically/symbolically to the tolerance stated by the artifact. A curve drawn for composition only must be labeled conceptual.

---

## 6. Evidence-state preservation

Every visual continues to use the profile evidence states:

`[S] source-grounded` · `[D] derived` · `[M] model` · `[C] computed` · `[V] verified` · `[E] empirical` · `[H] hypothesis` · `[T] target`.

Theme adaptation must never hide or recolor an evidence state so strongly that it appears to change category.

---

## 7. SVG accessibility contract

Every SVG must contain:

```xml
<title>...</title>
<desc>...</desc>
```

and a responsive `viewBox`.

Minimum requirements:

1. legible at ~768 px width;
2. no information conveyed by color alone;
3. dark and light contrast suitable for scientific reading;
4. no clipped equations or labels;
5. line direction remains visible after downscaling;
6. all text has a semantic role;
7. equations in the SVG must agree with the repository's canonical equations.

---

## 8. Raster-image policy

PNG/JPEG figures cannot adapt semantically after rasterization. They therefore follow one of three paths:

1. regenerate from source into separate light/dark exports;
2. use a neutral publication-white figure proven readable in both GitHub themes;
3. retain as a legacy fixed-theme artifact with an explicit migration note if source regeneration is unavailable.

A CSS inversion filter is **not** accepted for scientific plots because it can reverse semantic color meaning.

---

## 9. Computing stack

The native visual pipeline uses the mathematics-computing roles already defined in the Mathematics Research Ecosystem:

- SymPy / Mathematica / SageMath — exact/symbolic derivation;
- NumPy / SciPy — numerical geometry and verification;
- Julia / DifferentialEquations.jl / Manifolds.jl — high-performance dynamics and manifold computation;
- PyVista / VTK / Makie — scientific geometry and fields;
- LaTeX / TikZ / PGFPlots / Asymptote — publication vector assembly;
- Blender / GLSL / Manim — high-end rendering or animation after scientific verification;
- Lean / mathlib — theorem-level verification where appropriate;
- GitHub Actions — fail-closed structural and rendering audits.

---

## 10. Promotion levels

| Level | Requirement |
|---|---|
| P0 | conceptual, explicitly labeled |
| P1 | formula-consistent |
| P2 | generated numerically/symbolically |
| P3 | invariant-checked |
| P4 | source-reproduced |
| P5 | empirically validated for the represented claim |

Theme support is orthogonal to rigor: a beautiful adaptive P0 figure remains P0.

---

## 11. Repository migration rule

For each repository:

```text
inventory existing visuals
→ classify source / model / computed / empirical
→ identify canonical equation/data source
→ create adaptive SVG master
→ preserve fixed-theme raster evidence when regeneration is impossible
→ update README
→ run CI/audit
→ merge only after gates pass
```

The top-level repository visual should be a semantic summary of the repository's actual mathematical identity, not a generic profile banner.

---

## 12. Non-negotiable rules

1. No formula without a role.
2. No geometry without semantics.
3. No color without declared meaning.
4. No theme switch may change scientific meaning.
5. No AI-generated equation is accepted as canonical source text.
6. No raster inversion for scientific semantics.
7. No source theorem presented as original contribution.
8. No model/simulation presented as observation.
9. No differential-geometric language for infrastructure unless the geometric structure is formally defined or explicitly marked hypothesis/conceptual transfer.
10. No merge before repository-specific verification gates pass.
