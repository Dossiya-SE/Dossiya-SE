<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/generated/coupled-network-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/generated/coupled-network-light.svg">
  <img src="./assets/generated/coupled-network-light.svg" width="100%" alt="Rigorous coupled Power and Transportation multilayer network with typed nodes, shared EV charging interface C1, causal interdependency object, explanatory disturbance-control-recovery dynamics and formal mathematical annotations">
</picture>

<div align="center">

### Physics · Mathematical Foundations · Sustainable Engineering · Infrastructure Systems

**Physical Reality → Causal Mechanisms → Mathematical Structure → Engineering Decision**

[Research Portfolio](https://dossiya-se.github.io/) · [Research Laboratory](https://dossiya-se.github.io/lab.html) · [LinkedIn](https://www.linkedin.com/in/dossiya-dakou-/) · [ORCID](https://orcid.org/0009-0004-1071-9948)

</div>

---

## Research position

I study **interdependent engineering systems** by starting from the physical system: components, service flows, operating constraints, disturbances and timescales. I then identify the causal mechanisms by which one subsystem can alter another, and only after that introduce mathematical structure for dynamics, uncertainty, viability and engineering decision-making.

My current physical system is **Power ↔ Transportation**, with **Information + Organization** included when they materially alter operation, coordination, failure propagation or recovery.

```math
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
```

> **Research principle:** topology first · mechanism before model · physics before abstraction · validation before strong claims.

---

## Coupled physical system

The profile hero is generated from governed network data rather than hand-drawn decorative geometry:

```math
\boxed{
\mathcal G
=
\left(
\mathcal G_P,
\mathcal G_T,
\mathcal I_{PT}
\right)
}
```

with

```math
\mathcal G_P=(V_P,E_P),
\qquad
\mathcal G_T=(V_T,E_T).
```

### Typed physical objects

| Layer | Node geometry | Engineering meaning |
|---|---|---|
| Power | `● G` | generator / source |
| Power | `□ S` | substation / switching-transformation node |
| Power | `○ L` | electrical load |
| Shared interface | `◇ C` | EV charging / cross-infrastructure coupling asset |
| Transportation | `○ O,D` | origin / destination |
| Transportation | `□ I` | intersection / junction |
| Transportation | `● H` | mobility hub |
| Transportation | `△ T` | terminal / logistics endpoint |

The same physical object **`C_1`** is represented in both layers. It is therefore not merely a floating arrow between networks: it is the shared charging/coupling asset through which explicitly defined mechanisms act.

A cross-infrastructure interface is represented as

```math
\boxed{
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
\right)
}
```

The governed profile model distinguishes at least three mechanisms: **Power→Transportation electricity supply**, **Transportation→Power charging demand**, and **conditional V2G support**. Delays and coupling magnitudes remain symbolic until case-specific evidence supports calibration.

---

## From topology to viability

<img src="./assets/generated/graph-to-viability.svg" width="100%" alt="Graph-to-viability transformation from coupled topology and causal interface through dynamics to viable region, critical boundary, resilience margin and engineering decision">

The mathematical transformation is

```math
\boxed{
\mathcal G
\rightarrow
\mathfrak I
\rightarrow
F_{\mathcal G}
\rightarrow
Y(t)
\rightarrow
\mathcal V
\rightarrow
\rho_g
\rightarrow
u^\star
}
```

with coupled state evolution

```math
\dot Y
=
F_{\mathcal G}(Y,u,\eta;\theta),
```

viability

```math
\mathcal V
=
\left\{
Y_0:
\exists u(\cdot),\;
Y(t)\in K\;\forall t
\right\},
```

and, when a physically defensible metric is available,

```math
\rho_g(Y)
=
d_g\!\left(Y,\partial\mathcal V\right).
```

The visual geometry is explanatory: it shows how topology and causal coupling can be transformed into dynamics and viability reasoning. Geometry alone does not establish empirical validity.

---

## Dynamic scientific semantics

The network animation follows a controlled explanatory cycle:

```math
\boxed{
\text{Nominal}
\rightarrow
\text{Disturbance}
\rightarrow
\text{Propagation}
\rightarrow
\text{Control}
\rightarrow
\text{Recovery}
}
```

- **Nominal:** green directional motion represents admissible service flow.
- **Disturbance:** one local power-network connection becomes red; the entire network is not declared failed.
- **Propagation:** a red dashed path illustrates a source → interface → receiver mechanism through `C_1`.
- **Control:** a light-yellow intervention path represents \(u^\star\).
- **Recovery:** green motion represents return toward admissible service.

**Animation illustrates model structure and propagation semantics; it is not measured infrastructure behavior or live telemetry.** The phase durations are visual-design parameters, not event-duration estimates.

---

## Scientific visual language

| Visual encoding | Scientific meaning |
|---|---|
| **Green** | viable / sustainable / admissible state and service flow |
| **Red** | active constraint / critical boundary / disturbance or propagation path |
| **Light yellow** | causal interface / highlighted mechanism / engineering intervention |
| **Charcoal** | neutral physical topology and baseline structure |

Color and motion never increase the evidence strength of a scientific claim.

---

## Living research state

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/generated/research-state-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/generated/research-state-light.svg">
  <img src="./assets/generated/research-state-light.svg" width="100%" alt="Governed current research state for Power and Transportation infrastructure with active causal-mechanism to coupled-dynamics transition and public evidence timestamps">
</picture>

**Current question:** How do physically supported power–transport interfaces generate time-dependent coupled state evolution under disturbance and control?

The profile separates two evidence classes:

- **Declared research configuration** — system boundary, active scientific stage, mathematical objects, explanatory topology and integrity rules.
- **Observed public evidence** — metadata from explicitly allowlisted public repositories only.

Repository activity can show that public work changed. It cannot establish that a physical mechanism or mathematical model is empirically valid.

---

## Seven-stage research architecture

<img src="./assets/generated/research-pipeline.svg" width="100%" alt="Seven-stage research architecture with the current Causal Mechanisms to Coupled Hybrid Multiscale Dynamics transition highlighted">

```math
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
```

The current governed transition is **Causal Mechanisms → Coupled Hybrid Multiscale Dynamics**: from physically defensible interfaces toward coupled state evolution, not from correlation directly to a graph or differential equation.

---

## Mathematical foundations

| Foundation | Engineering role |
|---|---|
| **Graph theory & topology** | multilayer structure, typed connectivity, interfaces and propagation paths |
| **Analysis & differential equations** | coupled state evolution, bounds and continuous dynamics |
| **Dynamical systems** | equilibria, transitions, cascading propagation and recovery trajectories |
| **Differential geometry** | state-space structure, metrics, boundaries and resilience margins |
| **Probability & stochastic processes** | hazards, uncertainty, reliability and inference |
| **Optimization & control** | intervention, restoration, constrained design and resource allocation |

Mathematics is selected after the physical variables, mechanisms and admissible assumptions have been made explicit.

---

## Selected public research systems

<img src="./assets/generated/project-system.svg" width="100%" alt="Observed allowlisted public research systems using the governed scientific visual palette">

**Mathematics for Sustainable Resilience** — differential geometry · dynamical systems · resilience mathematics  
[Repository →](https://github.com/Dossiya-SE/Differential-geometry-and-Mathematics-arts-for-sustainability-and-resilience)

**Optimization for Sustainability and Resilience** — LP/MILP · network optimization · constrained engineering decisions  
[Repository →](https://github.com/Dossiya-SE/Optimization-for-sustainability-and-resilience)

**Africa Energy Dignity** — energy systems · geospatial engineering · infrastructure planning  
[Repository →](https://github.com/Dossiya-SE/africa-energy-dignity)

**Engineering Computation** — scientific computing · numerical analysis · reproducible engineering workflows  
[Repository →](https://github.com/Dossiya-SE/Python-for-rapid-engineering-solution)

**Mathematical Research Portfolio** — interactive mathematical communication · executable research demonstrations  
[Portfolio →](https://dossiya-se.github.io/) · [Laboratory →](https://dossiya-se.github.io/lab.html)

---

## Research experience

**National University of Singapore** — Visiting Graduate Researcher, 2026  
Research on infrastructure-system interfaces and resilience: representing, measuring and connecting cross-infrastructure dependencies to failure, propagation and recovery behavior.

---

## Education

| Institution | Program |
|---|---|
| **Arizona State University** | MSE · Sustainable Engineering · Ongoing |
| **WorldQuant University** | MSc · Financial Engineering · Ongoing |
| **Université d’Abomey-Calavi** | Licence · Énergies Renouvelables et Systèmes Énergétiques |

---

<details>
<summary><b>Scientific standard</b></summary>

A mathematical analogy is not automatically a physical model. A defensible engineering model should state, where applicable:

- system boundary, variables, parameters, units and initial/boundary conditions;
- conservation, constitutive, operational, safety and capacity relations;
- causal assumptions, delays, feedback, activation conditions and timescales;
- numerical method, convergence/verification checks and limiting cases;
- measurement, parameter, structural, scenario and numerical uncertainty;
- validation evidence, validity domain, limitations and decision relevance.

```math
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
```

The governing invariant is

```math
\boxed{
\text{claim strength}\leq\text{evidence strength}
}
```

</details>

<details>
<summary><b>Living-profile architecture</b></summary>

```text
power-network.json ───────┐
transport-network.json ───┤
interfaces.json ──────────┼─→ network validation ─→ SVG rendering ─→ README
network-dynamics.json ────┘

research-state.json ──────┐
allowlisted public state ─┴─→ profile validation ─→ research-state visuals
```

The SVGs are self-contained, have a `prefers-reduced-motion` fallback, use no embedded JavaScript, and are regenerated through GitHub Actions only after governed data pass validation.

</details>

---

<div align="center">

**Observe the physical system. Identify the mechanism. Formalize mathematically. Compute. Validate. Intervene.**

**Green = viable · Red = critical · Light yellow = causal / decision · Charcoal = topology**

[Research Portfolio](https://dossiya-se.github.io/) · [Research Laboratory](https://dossiya-se.github.io/lab.html) · [LinkedIn](https://www.linkedin.com/in/dossiya-dakou-/) · [ORCID](https://orcid.org/0009-0004-1071-9948)

</div>
