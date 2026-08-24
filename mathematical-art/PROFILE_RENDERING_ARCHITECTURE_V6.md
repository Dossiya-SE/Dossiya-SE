# Profile Rendering Architecture — V6

## Governing invariant

```math
\boxed{
\text{mathematical object}
\rightarrow
\text{verified numerical/symbolic representation}
\rightarrow
\text{renderer-neutral exchange}
\rightarrow
\text{faithful renderer}
}
```

A renderer may improve legibility, motion, camera, lighting, interaction, and aesthetic quality. It may not silently change equations, topology, field values, evidence state, or scientific interpretation.

## Profile-wide implementation matrix

| Profile part | Canonical GitHub surface | High-rigor enhancement | Verification boundary |
|---|---|---|---|
| Profile header | adaptive SVG | bounded Manim signature film | conceptual only; no quantitative meaning |
| Professional trajectory | adaptive SVG | chronological reveal | descriptive chronology only |
| Mathematics universe | adaptive SVG | D3/Three.js navigation; bounded Manim transformations | declared mappings only; not a mastery map |
| Research operating system | adaptive SVG | Manim process trace + provenance drill-down | order/mapping semantics only |
| Differential geometry foundations | adaptive SVG | verified geometry engine → Manim/PyVista/Blender/Three.js | P3 target; invariants must pass before rendering |
| Computational stack | adaptive SVG | implementation links; mostly static | tool presence is not proficiency evidence |
| Formula evidence lattice | adaptive SVG | provenance trace | evidence states must remain invariant |
| Evidence maturity map | adaptive SVG | static + source tooltips | no temporal motion without longitudinal data |

The machine-readable contract is [`geometry-engine/renderer_registry_v6.json`](geometry-engine/renderer_registry_v6.json).

## Differential-geometry promotion gate

The V6 engine currently implements a reference torus as a computational verification demonstrator:

```math
\mathbf r(u,v)=
\begin{bmatrix}
(R+r\cos v)\cos u\\
(R+r\cos v)\sin u\\
r\sin v
\end{bmatrix},
\qquad R>r>0.
```

Before the object is eligible for a verified render, CI checks:

```math
\|\mathbf n\|=1,
\qquad
\mathbf n\cdot\partial_u\mathbf r=0,
\qquad
\mathbf n\cdot\partial_v\mathbf r=0,
```

```math
g_{\alpha\beta}=g_{\beta\alpha},
\qquad
\det g>0,
```

and verifies the analytic tangent basis against an independent central-difference approximation.

The torus demonstrator does **not** establish a Riemannian structure for infrastructure, finance, or other research state spaces. Those transfers remain separate modeling hypotheses until their geometric structures are formally defined and validated.

## Renderer roles

- **SymPy / NumPy / SciPy / Geomstats** — mathematical computation and manifold algorithms.
- **Manim** — mathematical motion and explanation downstream of verified values.
- **Matplotlib / PyVista / VTK** — scientific plotting and 3-D fields.
- **Blender / Geometry Nodes** — cinematic rendering downstream of verified geometry.
- **Three.js / WebGPU / WebGL / D3** — interactive browser delivery.
- **TikZ / Asymptote / SVG** — publication and GitHub vector surfaces.
- **p5.js / Processing / Houdini** — generative mathematical art, explicitly separated from evidence-bearing scientific visualization.

## Promotion levels

```text
P0 conceptual
→ P1 formula-consistent
→ P2 numerically/symbolically generated
→ P3 invariant-checked
→ P4 source-reproduced
→ P5 empirically validated for the represented claim
```

Visual sophistication cannot promote an artifact by itself.
