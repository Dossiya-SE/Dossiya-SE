# Mathematical Art and Professional Formula System — V3

This directory is the **profile-level visual mathematics control layer** for `Dossiya-SE`.

The objective is not decoration and not capability inflation. Every equation, curve, surface, vector field, color field, network, uncertainty region, and topology graphic must correspond to a declared mathematical or scientific object.

## Governing files

- [`MATHEMATICAL_PRESENTATION_STANDARD.md`](MATHEMATICAL_PRESENTATION_STANDARD.md) — typography, notation, semantics, evidence states, accessibility, and cross-repository display rules.
- [`PROFILE_FORMULA_ATLAS.md`](PROFILE_FORMULA_ATLAS.md) — human-readable mathematical atlas across the profile.
- [`formula_registry.json`](formula_registry.json) — machine-readable formula identity/provenance registry.

## New V3 profile visuals

<p align="center">
  <img src="../assets/math-art/profile-mathematics-universe-v3.svg" width="100%" alt="Profile-wide mathematics universe connecting foundations, dynamics, networks, inference, viability and decision mathematics" />
</p>

[`profile-mathematics-universe-v3.svg`](../assets/math-art/profile-mathematics-universe-v3.svg) maps the mathematical families actually used or explicitly specified across the portfolio. It is not presented as a map of all mathematics.

<p align="center">
  <img src="../assets/math-art/differential-geometry-viability-v3.svg" width="100%" alt="Differential geometry source mathematics separated from infrastructure viability research transfer" />
</p>

[`differential-geometry-viability-v3.svg`](../assets/math-art/differential-geometry-viability-v3.svg) separates three layers that must never be conflated:

```text
source differential geometry
≠ geometric metaphor
≠ formally defined research-state geometry
```

<p align="center">
  <img src="../assets/math-art/formula-evidence-lattice-v3.svg" width="100%" alt="Formula evidence lattice from provenance through verification and validation to bounded decisions" />
</p>

[`formula-evidence-lattice-v3.svg`](../assets/math-art/formula-evidence-lattice-v3.svg) encodes the provenance and scientific-status contract for displayed mathematics.

---

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

---

## Canonical profile equations

### Coupled dynamics — [M]

```math
\dot{x}_i
=
f_i(x_i,\theta_i)
+
\sum_{j\ne i}g_{ij}(x_i,x_j,G_{ij},\theta_{ij})
+
B_i u_i
+
\xi_i.
```

### Observation and inverse problem — [M]

```math
y_k=h(x_k,\theta)+\varepsilon_k,
\qquad
\pi(\theta\mid y)\propto L(y\mid\theta)\pi_0(\theta).
```

### Reliability — [M]

```math
P_f
=
\mathbb P\!\left[g(X,H)\le0\right].
```

### Service resilience — [M]

```math
\mathcal R_T
=
\frac{1}{T}
\int_0^T
\frac{S(t)}{S_0}\,dt.
```

### Viability — [M]

```math
\mathcal V
=
\left\{
x_0:\exists u(\cdot),\;x(t)\in\mathcal K,\;\forall t\in[0,T]
\right\}.
```

### Differential geometry — [S]

```math
g_{\alpha\beta}=\partial_\alpha\mathbf r\cdot\partial_\beta\mathbf r,
\qquad
K=\frac{eg-f^2}{EG-F^2}.
```

```math
\frac{d^2u^\alpha}{ds^2}
+
\Gamma^\alpha_{\beta\gamma}
\frac{du^\beta}{ds}
\frac{du^\gamma}{ds}=0.
```

The differential-geometry source layer is anchored to the Sochi foundation registered in `Dossiya-SE/Dossiya-SE-Dossiya-SE`.

---

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

A displayed formula retains its status when reused across repositories.

---

## Design rules

1. **Equation before ornament:** the visual object must have a mathematical role.
2. **Semantics before color:** color encodes a declared quantity or category.
3. **Source before attribution:** theorem/source mathematics is never presented as original research.
4. **Assumptions before optimization:** objective and constraints must be explicit.
5. **Uncertainty before confidence:** bands/tubes require a stated construction.
6. **Geometry before metaphor:** metric/curvature language requires a formal geometric object.
7. **Verification before promotion:** invariant or cross-method checks should exist when feasible.
8. **Validation before decision:** software correctness is not empirical validity.
9. **Accessibility by default:** all SVGs include `<title>`, `<desc>`, scalable `viewBox`, and non-color-only meaning.
10. **Vector-first delivery:** SVG/PDF/TeX are preferred for publication-grade mathematical diagrams; raster is reserved for data images/rendered scenes.

---

## Rendering hierarchy

```text
P0 conceptual
→ P1 formula-consistent
→ P2 numerically generated
→ P3 invariant-checked
→ P4 source-reproduced
→ P5 empirically validated
```

Visual sophistication does not change evidence level.

---

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

This pipeline is the common visual and mathematical language of the profile.
