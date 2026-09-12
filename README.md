<p align="center">
  <img src="assets/math-art/profile-header-v5.svg" width="100%" alt="Dossiya Dakou — Mathematical Systems Engineering for Sustainable Resilience" />
</p>

<p align="center">
  <a href="https://dossiya-se.github.io/"><img src="https://img.shields.io/badge/Research%20Portfolio-Live-176A38?style=flat-square" alt="Research portfolio" /></a>
  <a href="https://orcid.org/0009-0004-1071-9948"><img src="https://img.shields.io/badge/ORCID-0009--0004--1071--9948-A6CE39?style=flat-square&logo=orcid&logoColor=white" alt="ORCID" /></a>
  <a href="https://www.linkedin.com/in/dossiya-dakou-/"><img src="https://img.shields.io/badge/LinkedIn-Dossiya%20Dakou-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
</p>

<p align="center">
  <a href="#research-direction">Research</a> ·
  <a href="#current-system">Current system</a> ·
  <a href="#mathematical-architecture">Mathematics</a> ·
  <a href="#computational-architecture">Computation</a> ·
  <a href="#evidence--validation">Evidence</a> ·
  <a href="#featured-repositories">Repositories</a>
</p>

# Dossiya Dakou

**Engineer and quantitative researcher developing mathematical and computational frameworks for sustainable and resilient systems.**

My trajectory connects **electrical and energy systems → sustainable engineering → quantitative modeling → advanced mathematical structures**. The current research focus is the behavior of **coupled infrastructure systems under disturbance, uncertainty, feedback, recovery and sustainability constraints**.

> **Evidence invariant:** a mathematical model is not an observed mechanism; software verification is not empirical validation; a research architecture is not a universal theory.

---

## Research direction

The central engineering question is:

> **How can the structure, dynamics and interfaces of interdependent systems be represented rigorously enough to identify failure propagation, viable operating regions and defensible interventions?**

The working research pipeline is

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
\text{Resilience-to-Sustainability Interface}
\rightarrow
\text{Transformation Pathways}
}
```

This is a **research programme and testable architecture**, not a claim that one mathematical formalism has already been validated across all infrastructure sectors.

---

## Current system

### Multilayer interdependent infrastructure

The present technical case centers on **power and transportation**, while explicitly separating physical, informational and organizational mechanisms when they affect system behavior.

<table>
<tr>
<td width="25%" valign="top"><strong>POWER</strong><br><sub>generation · networks · substations · charging supply</sub></td>
<td width="25%" valign="top"><strong>TRANSPORT</strong><br><sub>roads · mobility · EV demand · accessibility</sub></td>
<td width="25%" valign="top"><strong>INFORMATION</strong><br><sub>sensing · communication · estimation · control signals</sub></td>
<td width="25%" valign="top"><strong>ORGANIZATION</strong><br><sub>operators · decisions · procedures · recovery coordination</sub></td>
</tr>
</table>

A dependency is treated as a structured scientific object rather than only an edge in a graph:

```math
\boxed{
\mathfrak I_{ij}^{\alpha\beta}
=
\left(
E_i^\alpha,
E_j^\beta,
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

The purpose is to distinguish **who depends on whom, through what mechanism, with what strength, direction, delay, operating mode and time-varying context** before embedding the dependency in coupled dynamics.

---

## Mathematical architecture

<p align="center">
  <img src="assets/math-art/research-operating-system-v5.svg" width="96%" alt="Research operating system connecting evidence, state, dynamics, inference, uncertainty, viability, control and validation" />
</p>

A generic coupled-system representation is

```math
\dot{x}_i
=
f_i(x_i,\theta_i)
+
\sum_{j\neq i} g_{ij}(x_i,x_j,\mathfrak I_{ij},\theta_{ij})
+
B_i u_i
+
\xi_i,
```

with subsystem state $x_i$, coupling object $\mathfrak I_{ij}$, intervention $u_i$, model parameters $\theta$, and disturbance/uncertainty $\xi_i$.

For a constraint set $K$ and viable set $\mathcal V\subseteq K$, one geometric quantity of interest is

```math
\rho_g(x)=d_g\!\left(x,\partial\mathcal V\right).
```

`ρ_g` is first a **geometric margin**. It becomes a resilience indicator only after the metric, boundary, physical interpretation and empirical relationship to system performance are justified.

<table>
<tr>
<td width="25%" valign="top"><strong>STRUCTURE</strong><br><sub>multilayer graphs · interfaces · topology · dependency objects</sub></td>
<td width="25%" valign="top"><strong>DYNAMICS</strong><br><sub>hybrid systems · multiscale evolution · cascades · recovery</sub></td>
<td width="25%" valign="top"><strong>GEOMETRY</strong><br><sub>state spaces · metrics · boundaries · geodesic distance</sub></td>
<td width="25%" valign="top"><strong>DECISION</strong><br><sub>control · optimization · uncertainty · intervention testing</sub></td>
</tr>
</table>

---

## Computational architecture

The profile and research repositories separate **scientific meaning** from **presentation technology**.

```text
Markdown + LaTeX
      ↓
structured research records
      ↓
TypeScript contracts
      ↓
HTML / SVG views
      ↓
JavaScript interaction
      ↓
Python / Julia computation and verification
```

| Layer | Responsibility |
|---|---|
| **Markdown + LaTeX** | definitions, assumptions, derivations, references and equations |
| **TypeScript** | typed records for dependencies, mechanisms, evidence states and validity domains |
| **HTML** | semantic structure and navigation |
| **CSS / SVG** | visual hierarchy, responsive presentation and mathematical graphics |
| **JavaScript** | filtering, inspection, linked diagrams and interactive research exploration |
| **Python / Julia** | simulation, optimization, inference, uncertainty analysis and reproducible numerical verification |

**GitHub README constraint:** GitHub does not execute arbitrary project JavaScript or TypeScript inside a profile README. Therefore this page remains a static, auditable research surface, while richer interaction belongs in the linked research portfolio.

---

## Evidence & validation

The research workflow is deliberately asymmetric:

```math
\boxed{
\text{Evidence}
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
\text{Decision}
}
```

| Evidence level | Meaning |
|---|---|
| **Observed / sourced** | supported by data, literature, measurements or authoritative records |
| **Modeled** | mathematically represented under explicit assumptions |
| **Computed** | produced by reproducible numerical or symbolic procedures |
| **Verified** | implementation checked against stated mathematical/software properties |
| **Validated** | compared against appropriate empirical or external evidence |
| **Decision-ready** | usable only inside a stated validity domain and uncertainty boundary |

See the public [Research Integrity Standard](docs/RESEARCH_INTEGRITY.md).

---

## Featured repositories

| Research system | Primary role | Maturity boundary |
|---|---|---|
| [**Mathematical Research Portfolio**](https://github.com/Dossiya-SE/dossiya-se.github.io) | Interactive nonlinear dynamics, inverse problems, uncertainty, viability and mathematical visualization | Research demonstrators; not a calibrated digital twin |
| [**Mathematics Exploration for Sustainable Resilience**](https://github.com/Dossiya-SE/Differential-geometry-and-Mathematics-arts-for-sustainability-and-resilience) | Differential geometry, dynamical systems, resilience mathematics, reproducible computation and mathematical art | Research architecture under development |
| [**Optimization for Sustainability and Resilience**](https://github.com/Dossiya-SE/Optimization-for-sustainability-and-resilience) | Linear algebra, LP/MILP, network optimization and constrained sustainability/resilience models | Deterministic optimization foundations |
| [**Mathematical Rendering & Verification**](https://github.com/Dossiya-SE/Math-Surface-Engineer-Demo) | Renderer-aware mathematical publication and regression checking across Markdown, MDX, Quarto, LaTeX, Jupyter and HTML | Verification demonstrator |
| [**Africa Energy Dignity**](https://github.com/Dossiya-SE/africa-energy-dignity) | Energy-system modeling, geospatial engineering and constrained planning | Pre-alpha research system |

<details>
<summary><strong>Additional research systems and mathematical tooling</strong></summary>

<br>

- [Mathematics Research Ecosystem](https://github.com/Dossiya-SE/Dossiya-SE-Dossiya-SE)
- Mathematical visualization with Matplotlib, PyVista/VTK, Manim, SVG and TikZ/Asymptote
- Scientific computing with Python, Julia, MATLAB, NumPy, SciPy and symbolic mathematics
- Network, uncertainty, optimization and formal-verification directions where mathematically appropriate

</details>

---

## Education

- **MSE Sustainable Engineering — Arizona State University, ongoing**
- **MS Financial Engineering — WorldQuant University, ongoing**
- **Licence Professionnelle, Énergies Renouvelables et Systèmes Énergétiques — Université d’Abomey-Calavi**

The profile emphasizes a cumulative capability trajectory rather than treating education, research interests and validated expertise as equivalent claims.

---

## Connect

<p align="center">
  <a href="https://dossiya-se.github.io/"><strong>Research portfolio</strong></a>
  &nbsp;·&nbsp;
  <a href="https://orcid.org/0009-0004-1071-9948"><strong>ORCID</strong></a>
  &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/dossiya-dakou-/"><strong>LinkedIn</strong></a>
</p>

<p align="center"><strong>Evidence → Mathematics → Computation → Verification → Validation → Decision</strong></p>
