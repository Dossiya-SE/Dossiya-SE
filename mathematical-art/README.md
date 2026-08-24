# Mathematical Art and Verified Rendering System — V6

This directory is the **profile-level visual mathematics control layer** for `Dossiya-SE`.

Its purpose is not decoration and not capability inflation. Every equation, curve, surface, vector field, color field, network, uncertainty region, topology graphic, and animation must correspond to a declared mathematical, scientific, or explicitly conceptual object.

## Governing files

- [`MATHEMATICAL_PRESENTATION_STANDARD.md`](MATHEMATICAL_PRESENTATION_STANDARD.md) — notation, semantics, evidence states, accessibility, and scientific-integrity rules.
- [`ADAPTIVE_VISUAL_SYSTEM_V4.md`](ADAPTIVE_VISUAL_SYSTEM_V4.md) — adaptive light/dark vector rendering contract.
- [`PROFILE_RENDERING_ARCHITECTURE_V6.md`](PROFILE_RENDERING_ARCHITECTURE_V6.md) — renderer assignment and promotion rules for every major profile visual.
- [`PROFILE_FORMULA_ATLAS.md`](PROFILE_FORMULA_ATLAS.md) — human-readable profile formula atlas.
- [`formula_registry.json`](formula_registry.json) — machine-readable formula identity/provenance registry.
- [`geometry-engine/`](geometry-engine/) — verified geometry source, numerical invariants, renderer-neutral exchange, Manim source, tests, and renderer registry.

## Current public visual surfaces

The GitHub profile currently exposes the V5 adaptive visual set. V6 adds the computation/verification architecture behind those visuals without falsely relabeling conceptual graphics as computed evidence.

| Profile surface | Current asset | V6 treatment |
|---|---|---|
| Profile header | `profile-header-v5.svg` | canonical adaptive SVG + bounded Manim signature source |
| Professional trajectory | `engineering-to-mathematics-resilience-trajectory-v5.svg` | descriptive chronology; motion may reveal order only |
| Mathematics universe | `profile-mathematics-universe-v5.svg` | adaptive SVG + declared D3/Three.js/Manim interaction contract |
| Research operating system | `research-operating-system-v5.svg` | adaptive SVG + process-order Manim trace |
| Differential geometry | `differential-geometry-foundations-v5.svg` | adaptive SVG + verified geometry engine, P3 promotion target |
| Computational stack | `computational-stack-v5.svg` | static-first; implementation links preferred over animation |
| Formula evidence lattice | `formula-evidence-lattice-v5.svg` | provenance motion permitted only if evidence states remain invariant |
| Evidence maturity map | `evidence-maturity-map-v5.svg` | static; temporal motion prohibited without longitudinal evidence |

The machine-readable form of this table is [`geometry-engine/renderer_registry_v6.json`](geometry-engine/renderer_registry_v6.json).

## Verified-geometry pipeline

```math
\boxed{
\text{mathematical definition}
\rightarrow
\text{computation}
\rightarrow
\text{invariant/residual verification}
\rightarrow
\text{renderer-neutral exchange}
\rightarrow
\text{faithful renderer}
}
```

The first implemented reference object is a torus demonstrator. The source layer computes its parameterization, coordinate tangents, unit normal, first fundamental form, Gaussian curvature, sampled fields, and a renderer-neutral exchange. CI checks unit-normal and orthogonality invariants, metric symmetry/positive determinant, and analytic derivatives against independent central finite differences.

The demonstrator is **source/computed geometry only**. It does not establish that infrastructure, finance, or other application state spaces are Riemannian manifolds.

## Renderer roles

| Tool family | Permitted role |
|---|---|
| SymPy / NumPy / SciPy / Geomstats | mathematical computation and manifold algorithms |
| Matplotlib / PyVista / VTK | scientific plotting and 3-D fields |
| Manim | mathematical motion downstream of verified values |
| Blender / Geometry Nodes | cinematic rendering downstream of verified geometry |
| Three.js / WebGPU / WebGL / D3 | browser interaction and navigation |
| TikZ / Asymptote / SVG | publication and GitHub vector surfaces |
| p5.js / Processing / Houdini | explicitly identified generative mathematical art |

A renderer may change presentation variables. It may not silently change equations, topology, field values, evidence state, or scientific interpretation.

## Visual grammar

| Visual element | Mathematical/scientific meaning |
|---|---|
| coupled nodes | subsystems, state blocks, variables, or graph vertices |
| dynamic edge `G(t)` | declared time-varying interface/coupling relation |
| state trajectory | evolution under a stated dynamic model |
| dashed outer region | constraint, admissibility, or uncertainty boundary |
| nested sets | explicitly declared admissible/credible/scenario regions |
| recovery trajectory | controlled/declared return path |
| coordinate mesh | chart, discretization, or state-space reference |
| contour | level set of a declared scalar field |
| tangent/normal/binormal | mathematically defined moving frame |
| color field | scalar/vector quantity with an explicit legend |

A visual arrow means a **mapping, dependency, flow, or model relation** unless causal evidence is separately established.

## Evidence-state tags

```text
[S] source-grounded
[D] derived
[M] model
[C] computed
[V] verified
[E] empirical
[H] hypothesis
[T] target
```

A displayed object retains its evidence state across SVG, animation, website, presentation, and publication renderers.

## Design rules

1. **Equation before ornament.**
2. **Semantics before color.**
3. **Source before attribution.**
4. **Assumptions before optimization.**
5. **Uncertainty before confidence.**
6. **Geometry before metaphor.**
7. **Verification before promotion.**
8. **Validation before decision.**
9. **Accessibility by default.**
10. **Vector-first delivery for canonical GitHub/publication diagrams.**
11. **Motion must encode declared change; decorative motion is not evidence.**
12. **One mathematical object should feed multiple renderers rather than being reimplemented independently.**

## Rendering hierarchy

```text
P0 conceptual
→ P1 formula-consistent
→ P2 numerically/symbolically generated
→ P3 invariant-checked
→ P4 source-reproduced
→ P5 empirically validated
```

Visual sophistication does not change evidence level.

## Profile mathematics pipeline

```math
\boxed{
\text{Source/Evidence}
\rightarrow
\text{Definitions + Assumptions}
\rightarrow
\text{Model}
\rightarrow
\text{Computation}
\rightarrow
\text{Verification}
\rightarrow
\text{Validation}
\rightarrow
\text{Bounded Decision}
}
```
