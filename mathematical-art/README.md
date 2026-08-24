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
- [`../optimization-lab/`](../optimization-lab/) — source-anchored deterministic-OR/Bayesian decision benchmarks, certificate tests, and fail-closed audit.

## Current public visual surfaces

The GitHub profile uses V5 adaptive masters for the established surfaces and introduces a V6 optimization/decision surface backed by executable verification. V6 computation/verification architecture must not falsely relabel conceptual graphics as computed evidence.

| Profile surface | Current asset | V6 treatment |
|---|---|---|
| Profile header | `profile-header-v5.svg` | canonical adaptive SVG + bounded Manim signature source |
| Professional trajectory | `engineering-to-mathematics-resilience-trajectory-v5.svg` | descriptive chronology; motion may reveal order only |
| Mathematics universe | `profile-mathematics-universe-v5.svg` | adaptive SVG + declared D3/Three.js/Manim interaction contract |
| Research operating system | `research-operating-system-v5.svg` | adaptive SVG + process-order Manim trace |
| Optimization / bounded decision | `optimization-decision-system-v6.svg` | source-anchored OR + executable certificate layer; algorithmic motion only from verified objects |
| Differential geometry | `differential-geometry-foundations-v5.svg` | adaptive SVG + verified geometry engine, P3 promotion target |
| Computational stack | `computational-stack-v5.svg` | static-first; implementation links preferred over animation |
| Formula evidence lattice | `formula-evidence-lattice-v5.svg` | provenance motion permitted only if evidence states remain invariant |
| Evidence maturity map | `evidence-maturity-map-v5.svg` | static; temporal motion prohibited without longitudinal evidence |

The machine-readable form of this table is [`geometry-engine/renderer_registry_v6.json`](geometry-engine/renderer_registry_v6.json).

## Verified computation pipeline

```math
\boxed{
\text{mathematical definition}
\rightarrow
\text{computation}
\rightarrow
\text{invariant/residual/certificate verification}
\rightarrow
\text{renderer-neutral or renderer-bounded representation}
\rightarrow
\text{faithful renderer}
}
```

The geometry engine's first implemented reference object is a torus demonstrator. The source layer computes its parameterization, coordinate tangents, unit normal, first fundamental form, Gaussian curvature, sampled fields, and a renderer-neutral exchange. CI checks unit-normal and orthogonality invariants, metric symmetry/positive determinant, and analytic derivatives against independent central finite differences.

The optimization lab separately implements compact deterministic-OR and Bayesian-decision benchmarks: LP primal/dual feasibility and complementary-slackness certificates, min-cost-flow conservation/bounds, an equality-constrained convex-QP KKT system, and EI/UCB regression semantics. These are verified benchmark objects, not empirical validation of an application system.

The geometry demonstrator is **source/computed geometry only**. It does not establish that infrastructure, finance, or other application state spaces are Riemannian manifolds. Likewise, an optimization certificate proves only the mathematical benchmark under its declared model and assumptions; it does not validate the real-world model or data.

## Renderer roles

| Tool family | Permitted role |
|---|---|
| SymPy / NumPy / SciPy / Geomstats | mathematical computation, optimization support, and manifold algorithms |
| Matplotlib / PyVista / VTK | scientific plotting and 3-D fields |
| Manim | mathematical/algorithmic motion downstream of verified values |
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
| feasible region | set satisfying declared constraints |
| primal/dual pair | paired optimization problems with declared sign/form conventions |
| certificate mark | verified feasibility, optimality identity, residual, or conservation check |
| uncertainty band / posterior | declared probabilistic construction, never generic decoration |

A visual arrow means a **mapping, dependency, flow, algorithmic update, or model relation** unless causal evidence is separately established.

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
13. **Solver output is not an optimality certificate unless feasibility/optimality conditions are independently checked where available.**
14. **A decision model is not empirically validated merely because its optimization problem is solved exactly.**

## Rendering hierarchy

```text
P0 conceptual
→ P1 formula-consistent
→ P2 numerically/symbolically generated
→ P3 invariant/certificate-checked
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
