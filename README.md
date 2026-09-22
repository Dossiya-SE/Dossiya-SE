<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/generated/research-hero-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/generated/research-hero-light.svg">
  <img src="./assets/generated/research-hero-light.svg" width="100%" alt="Dossiya Dakou research portrait linking coupled Power and Transportation infrastructure, causal interfaces, mathematical structure, viability geometry, critical boundaries and engineering decision">
</picture>

<div align="center">

**Physics-Grounded Mathematical Engineering for Sustainable Infrastructure**

Power ↔ Transportation · Dynamics · Viability · Resilience · Optimization · Geometry

[Research Portfolio](https://dossiya-se.github.io/) · [Research Laboratory](https://dossiya-se.github.io/lab.html) · [Repositories](https://github.com/Dossiya-SE?tab=repositories) · [ORCID](https://orcid.org/0009-0004-1071-9948) · [LinkedIn](https://www.linkedin.com/in/dossiya-dakou-/)

</div>

---

## 01 · Research problem

I study how **physical interdependencies between critical infrastructures generate coupled dynamics, cascading disruption and recovery**, and how mathematical models can identify viable and resilient intervention pathways.

| Research layer | Current focus |
|---|---|
| **Physical system** | Power ↔ Transportation |
| **Scientific object** | typed interfaces → coupled dynamics → viability |
| **Current transition** | Causal Mechanisms → Coupled Hybrid Multiscale Dynamics |
| **Decision objective** | identify admissible interventions that preserve service and increase distance from critical boundaries |

~~~math
\boxed{
\mathcal R_{\mathrm{phys}}
\rightarrow
\mathcal C
\rightarrow
(\mathcal G,\mathfrak I)
\rightarrow
F_{\mathcal G}
\rightarrow
\mathcal V
\rightarrow
\rho_g
\rightarrow
u^\star
}
~~~

**Topology first. Mechanism before model. Physics before abstraction. Validation before strong claims.**

<img src="./assets/generated/research-question.svg" width="100%" alt="Current research question linking Power–Transportation interfaces, coupled dynamics under disturbance and control, and the sustainable viability objective">

---

## 02 · Coupled physical system

The physical model is a typed multilayer system:

~~~math
\mathcal G
=
\left(
\mathcal G_P,
\mathcal G_T,
\mathcal I_{PT}
\right),
\qquad
\mathcal G_P=(V_P,E_P),
\quad
\mathcal G_T=(V_T,E_T).
~~~

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/generated/coupled-network-3d-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/generated/coupled-network-3d-light.svg">
  <img src="./assets/generated/coupled-network-3d-light.svg" width="100%" alt="Static isometric 3D coupled Power and Transportation multilayer network with a shared EV charging interface and separate schematic viability geometry">
</picture>

The **same physical object**, written **C_1** in the governed network data and **C₁** in display notation, is a physical coupling asset shared by both layers—not a decorative cross-layer arrow. Vertical separation in the figure is only a **visual encoding of multilayer structure**. It is **not geographic elevation**, GIS height, measured infrastructure behavior, or live infrastructure telemetry.

A governed interdependency can be represented as

~~~math
\mathfrak I_{PT}^{(1)}
=
\left(
E_i^P,
E_j^T,
M_{ij},
w_{ij},
\delta_{ij},
\tau_{ij},
a_{ij},
m,
\mathcal H_t
\right).
~~~

Coupling magnitude, sign, delay, activation and operating mode remain symbolic until case-specific evidence supports calibration.

---

## 03 · Graph → dynamics → viability

<img src="./assets/generated/graph-to-viability.svg" width="100%" alt="Transformation from graph and model space into state and viability space with coupled dynamics, viable region, critical boundary, resilience margin and engineering decision">

The central transformation is

~~~math
\mathcal G
\rightarrow
\mathfrak I
\rightarrow
F_{\mathcal G}
\rightarrow
Y(t)
\rightarrow
\mathcal V_{\mathrm{sus}}
\rightarrow
\rho_g
\rightarrow
u^\star.
~~~

with coupled state evolution

~~~math
\dot Y=F_{\mathcal G}(Y,u,\eta;\theta),
~~~

sustainable viability

~~~math
Y(t)\in\mathcal V_{\mathrm{sus}}(t),
~~~

and, when a physically defensible metric exists,

~~~math
\rho_g(Y)=d_g\!\left(Y,\partial\mathcal V\right).
~~~

A coherent trajectory, metric or viable region is a mathematical object. It becomes an engineering claim only through explicit physical interpretation, verification, calibration and validation.

---

## 04 · Current research state

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/generated/research-state-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/generated/research-state-light.svg">
  <img src="./assets/generated/research-state-light.svg" width="100%" alt="Governed research state showing the Power–Transportation focus and the active Causal Mechanisms to Coupled Hybrid Multiscale Dynamics transition">
</picture>

**Active transition:** Causal Mechanisms → Coupled Hybrid Multiscale Dynamics.

The objective is to move from physically defensible interfaces to coupled state evolution under disturbance and control—not from correlation directly to a graph, differential equation or causal conclusion.

---

## 05 · Mathematical foundations for the physical problem

<img src="./assets/generated/flat-geometry.svg" width="100%" alt="Geometry of flats: regular polygons from triangle through decagon, circle, ellipse and semicircle, followed by affine point, line and plane geometry and a hyperplane distance construction">

The figure deliberately separates **plane figures** from **affine flats**. Regular polygons, circles and ellipses are bounded figures or curves in a plane; an affine (k)-flat is an object of the form (x_0+\operatorname{span}\{v_1,\ldots,v_k\}). The bridge to resilience research is **constraint and state-space geometry**, not an identification of polygons with subspaces.

<details>
<summary><b>Reproducible flat-geometry sources</b></summary>

**Publication authority:** [TikZ / Overleaf](./mathematical-art/flat-geometry/overleaf/flat_geometry.tex)  
**Deterministic GitHub renderer:** [Python](./scripts/render_flat_geometry.py)  
**Mathematical computation mirror:** [Julia](./mathematical-art/flat-geometry/julia/flat_geometry.jl)  
**Interactive web mirror:** [React](./mathematical-art/flat-geometry/react/FlatGeometry.tsx) + [CSS](./mathematical-art/flat-geometry/react/flat-geometry.css)  
**Static renderer mirror:** [Go](./mathematical-art/flat-geometry/go/main.go)  
**Engineering integration mirror:** [C#](./mathematical-art/flat-geometry/csharp/FlatGeometry.cs)

All sources implement the same governed contract: **FLAT-GEOMETRY-V1**.

</details>

| Foundation | Engineering role |
|---|---|
| **Graph theory & topology** | multilayer structure, connectivity, typed interfaces and propagation paths |
| **Analysis & differential equations** | coupled state evolution, bounds and continuous dynamics |
| **Dynamical systems** | equilibria, transitions, cascading propagation and recovery |
| **Differential geometry** | state-space structure, metrics, boundaries and resilience margins |
| **Probability & stochastic processes** | hazards, uncertainty, reliability and inference |
| **Optimization & control** | intervention, restoration, constrained design and resource allocation |

The mathematical method is selected **after** the physical variables, mechanisms, assumptions, units, constraints and admissible states are made explicit.

---

## 06 · Research systems

<img src="./assets/generated/project-system.svg" width="100%" alt="Four featured public research systems rendered as a restrained publication-style research index">

<div align="center">

**[Africa Energy Dignity](https://github.com/Dossiya-SE/africa-energy-dignity)** ·
**[Mathematics Exploration for Sustainable Resilience](https://github.com/Dossiya-SE/Differential-geometry-and-Mathematics-arts-for-sustainability-and-resilience)** ·
**[Optimization for Sustainability and Resilience](https://github.com/Dossiya-SE/Optimization-for-sustainability-and-resilience)** ·
**[Mathematical Surface Engineering](https://github.com/Dossiya-SE/Math-Surface-Engineer-Demo)**

[Research Portfolio](https://dossiya-se.github.io/) · [All Public Repositories](https://github.com/Dossiya-SE?tab=repositories)

</div>

Each repository is treated as a bounded research system: implemented software, mathematical structure, experiments, validation evidence and future research claims remain distinguishable.

---

## 07 · Experience and education

**National University of Singapore** — Visiting Graduate Researcher · 2026  
Infrastructure-system interfaces and resilience: cross-infrastructure dependencies, failure propagation and recovery.

| Institution | Program | State |
|---|---|---|
| **Arizona State University** | MSE · Sustainable Engineering | Ongoing |
| **WorldQuant University** | MSc · Financial Engineering | Ongoing |
| **Université d’Abomey-Calavi** | Licence · Énergies Renouvelables et Systèmes Énergétiques | Completed |

The trajectory is cumulative: practical and physical engineering foundations → sustainable systems → quantitative modeling → deeper mathematical structures for resilience research.

---

<details>
<summary><b>Full seven-stage research architecture</b></summary>

<img src="./assets/generated/research-pipeline.svg" width="100%" alt="Seven-stage research architecture from multilayer structure through causal mechanisms, coupled dynamics, control, viability and sustainable transformation">

~~~math
\boxed{
\text{Multilayer Structure}
\rightarrow
\text{Causal Mechanisms}
\rightarrow
\text{Coupled Hybrid Multiscale Dynamics}
\rightarrow
\text{Feedback \& Control}
\rightarrow
\text{Viability}
\rightarrow
\text{Resilience--Sustainability Interface}
\rightarrow
\text{Sustainable Transformation Pathways}
}
~~~

The currently governed transition is **Causal Mechanisms → Coupled Hybrid Multiscale Dynamics**.

</details>

<details>
<summary><b>Scientific standard</b></summary>

A defensible engineering model should state the system boundary, variables, parameters, units, assumptions, conservation or constitutive relations, constraints, initial/boundary conditions, uncertainty sources, numerical method, verification checks, validation evidence and validity domain.

~~~math
\boxed{
\text{mathematical consistency}
\neq
\text{physical plausibility}
\neq
\text{numerical verification}
\neq
\text{empirical validation}
\neq
\text{engineering usefulness}
}
~~~

~~~math
\boxed{\text{claim strength}\leq\text{evidence strength}}
~~~

</details>

<details>
<summary><b>Scientific visual and accessibility standard</b></summary>

The profile uses **sRGB** with a neutral publication canvas and sparse semantic color. Approximate composition is **65% neutral canvas · 20% light geometry · 10% structural semantic color · ≤5% strong emphasis**.

| Encoding | Meaning | Redundant cue |
|---|---|---|
| **Power — #C8102E** | physical power-system structure | POWER label + solid topology + node geometry |
| **Transportation — #16823A** | physical transportation structure | TRANSPORTATION label + solid topology + node geometry |
| **Information — #1D4ED8** | sensing, estimation, communication | INFORMATION label + dashed relation |
| **Organization — #A66F00** | coordination, procedure, recovery action | ORGANIZATION label + dotted relation |
| **Viability — green** | admissible / sustainable / recovery state | region geometry + trajectory + label |
| **Criticality — red** | constraint, violation, critical boundary | dashed/thicker overlay + boundary label |
| **Causal / control — ochre-gold** | interface, mechanism, intervention | interface geometry + dashed/double line + explicit label |
| **Mathematical model — violet** | separate mathematical abstraction cue | equation/symbol label + geometric context |
| **Inference / state information — cyan** | observation or data-mediated state cue | state marker + label |

RGB defines appearance and navigation—not scientific truth. Color never carries meaning alone; geometry, line pattern, direction and labels remain authoritative. The permanent state-semantic subset remains **green** for viable/recovery state, **red** for criticality/boundaries, and **light yellow / ochre** for causal or intervention emphasis. The machine-readable authority for these values is [`data/visual-palette.json`](data/visual-palette.json).

Some SVG sources retain motion-capable CSS semantics for compatible renderers, but **GitHub should not be treated as guaranteeing SVG animation**. Any motion is explanatory and is **not a measured flow**, not measured infrastructure behavior, and not live infrastructure telemetry.

</details>

<details>
<summary><b>Living-profile engine</b></summary>

~~~text
governed JSON state
      ↓
network + research validation
      ↓
deterministic SVG rendering
      ↓
palette + layout validation
      ↓
runtime rendering checks
      ↓
README research interface
~~~

The generated figures use controlled light/dark palettes, deterministic SVG geometry, no embedded JavaScript, XML/accessibility validation, semantic color checks, non-color redundancy and explicit evidence boundaries.

</details>

---

<div align="center">

**Observe the physical system. Identify the mechanism. Formalize mathematically. Compute. Verify. Validate. Intervene.**

[Research Portfolio](https://dossiya-se.github.io/) · [Research Laboratory](https://dossiya-se.github.io/lab.html) · [ORCID](https://orcid.org/0009-0004-1071-9948) · [LinkedIn](https://www.linkedin.com/in/dossiya-dakou-/)

</div>
