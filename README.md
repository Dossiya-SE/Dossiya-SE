<p align="center">
  <img src="assets/math-art/profile-header-v5.svg" width="100%" alt="Dossiya Dakou — Mathematical Systems Engineering for Sustainable Resilience" />
</p>

<p align="center">
  <a href="https://dossiya-se.github.io/"><img src="https://img.shields.io/badge/Research%20Portfolio-Live-176A38?style=flat-square" alt="Research portfolio" /></a>
  <a href="https://orcid.org/0009-0004-1071-9948"><img src="https://img.shields.io/badge/ORCID-0009--0004--1071--9948-A6CE39?style=flat-square&logo=orcid&logoColor=white" alt="ORCID" /></a>
  <a href="https://www.linkedin.com/in/dossiya-dakou-/"><img src="https://img.shields.io/badge/LinkedIn-Dossiya%20Dakou-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
</p>

# Dossiya Dakou

**Mathematical Systems Engineering for Sustainable Resilience**

Sustainable systems engineering · mathematical modeling · optimization · infrastructure resilience

I develop mathematical and computational methods for understanding, testing, and improving complex sustainable and resilient systems. My current work concentrates on **infrastructure systems, optimization, dynamical systems, scientific computing, differential geometry, viability theory, uncertainty quantification, and network science**.

The cross-sector direction is a research programme, **not a claim of an already validated universal theory**.

## About

My work follows a simple engineering principle:

```math
\boxed{\text{physical system}\rightarrow\text{mathematical model}\rightarrow\text{computation}\rightarrow\text{verification}\rightarrow\text{bounded decision}}
```

The central question is how mathematical structure can support decisions about systems that are **coupled, uncertain, constrained, and required to remain functional under disturbance**.

Current emphasis:

- **Infrastructure resilience** — coupled systems, interfaces, cascading effects, recovery, service and viability.
- **Optimization** — linear, network and constrained models for sustainability and resilience decisions.
- **Mathematical geometry** — differential geometry and state-space geometry where the geometric structure is explicitly defined.
- **Scientific computing** — reproducible numerical experiments, uncertainty analysis, verification and mathematical visualization.

## Featured research

| Research system | What it demonstrates | Current boundary |
|---|---|---|
| [**Mathematical Research Portfolio**](https://github.com/Dossiya-SE/dossiya-se.github.io) | Browser-based nonlinear dynamics, inverse problems, seeded uncertainty experiments, viability visualization and D3/WebGL mathematical interaction | Research demonstrators; not a calibrated digital twin |
| [**Mathematics Exploration for Sustainable Resilience**](https://github.com/Dossiya-SE/Differential-geometry-and-Mathematics-arts-for-sustainability-and-resilience) | Domain-neutral research platform connecting differential geometry, dynamical systems, sustainability/resilience mathematics, reproducible computation and mathematical art | Phase-0 architecture and scope validation |
| [**Optimization for Sustainability and Resilience**](https://github.com/Dossiya-SE/Optimization-for-sustainability-and-resilience) | Linear algebra, mathematical modeling, LP/MILP, network optimization, sustainability objectives and resilience models | Phase-1 deterministic optimization foundations |
| [**Africa Energy Dignity**](https://github.com/Dossiya-SE/africa-energy-dignity) | Energy-system modeling, geospatial engineering and constrained planning for Sub-Saharan African energy systems | Pre-alpha research system |
| [**Mathematics Research Ecosystem**](https://github.com/Dossiya-SE/Dossiya-SE-Dossiya-SE) | Source-grounded mathematics, models, reproductions, visualization, scientific computing and verification in one bootstrap research ecosystem | Monorepo prototype; modules remain separable |
| [**Mathematical Rendering & Verification**](https://github.com/Dossiya-SE/Math-Surface-Engineer-Demo) | Reproducible mathematical publication across GitHub Markdown, MDX, Quarto, LaTeX, Jupyter and HTML with renderer-aware regression checks | Rendering/verification demonstrator |

## Research framework

<p align="center">
  <img src="assets/math-art/research-operating-system-v5.svg" width="96%" alt="Research operating system from evidence through state, dynamics, inference, uncertainty, viability and control to validation" />
</p>

The research workflow separates mathematical construction from empirical claims:

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

A representative coupled-system model is

```math
\dot{x}_i
=
f_i(x_i,\theta_i)
+
\sum_{j\neq i}g_{ij}(x_i,x_j,G_{ij},\theta_{ij})
+
B_i u_i
+
\xi_i,
```

where $x_i$ represents subsystem state, $G_{ij}$ an interface or coupling structure, $u_i$ an admissible intervention, and $\xi_i$ uncertainty or disturbance.

## Mathematical focus

<p align="center">
  <img src="assets/math-art/differential-geometry-foundations-v5.svg" width="96%" alt="Differential-geometry foundations from parameterization and tangent basis through metric, curvature and geodesics" />
</p>

| Mathematical area | Research role |
|---|---|
| **Dynamical systems** | state evolution, stability, disturbance and recovery trajectories |
| **Optimization** | objectives, constraints, network flows, trade-offs and intervention design |
| **Network science** | multilayer coupling, interfaces, propagation and structural criticality |
| **Probability & uncertainty** | stochastic disturbances, parameter uncertainty, reliability and model risk |
| **Viability / reachability** | feasible long-horizon operation under constraints and control |
| **Differential geometry** | metrics, geodesics, curvature and geometric analysis when a valid state-space geometry is defined |

For a viable state set $\mathcal V$ with metric $g$, one geometric quantity of interest is

```math
\rho_g(x)=d_g\!\left(x,\partial\mathcal V\right).
```

This is a **geometric margin**. It becomes an engineering resilience measure only if its physical interpretation and empirical relationship to system performance are separately established.

## Computational toolkit

| Role | Tools |
|---|---|
| **Numerical modeling** | Python, NumPy, SciPy, Julia, MATLAB |
| **Symbolic / geometric mathematics** | SymPy, Geomstats, SageMath, Mathematica |
| **Optimization / decision models** | SciPy/HiGHS, mathematical programming formulations, numerical sensitivity analysis |
| **Scientific visualization** | Matplotlib, PyVista/VTK, Manim, SVG, TikZ/Asymptote |
| **Interactive mathematics** | D3.js, Three.js, WebGL/WebGPU |
| **Verification direction** | pytest, regression tests, reproducibility checks, Lean/mathlib and Coq where formal proof is appropriate |

Tool presence indicates a **research role**, not equal proficiency in every listed system.

## Education

- **MSE Sustainable Engineering — Arizona State University, ongoing**
- **MS Financial Engineering — WorldQuant University, ongoing**
- **Licence Professionnelle, Énergies Renouvelables et Systèmes Énergétiques — Université d’Abomey-Calavi**

## Research integrity

Mathematical models, simulations, software verification, empirical validation and engineering decisions are treated as distinct evidence levels. A model is not promoted to an observed mechanism because it is mathematically elegant; passing software tests does not establish empirical validity; and differential-geometric language is used for engineering systems only when the required geometric structure is formally defined.

See the concise [Research Integrity Standard](docs/RESEARCH_INTEGRITY.md) for the public claim and evidence rules.

## Connect

- **Research portfolio:** https://dossiya-se.github.io/
- **ORCID:** https://orcid.org/0009-0004-1071-9948
- **LinkedIn:** https://www.linkedin.com/in/dossiya-dakou-/

<p align="center"><strong>Evidence → Mathematics → Computation → Verification → Validation → Decision</strong></p>
