# Dossiya Dakou

**Physical Reality → Causal Mechanisms → Mathematical Structure → Engineering Decision**  
**Physics · Pure Mathematical Foundations · Sustainable Engineering · Infrastructure Systems**

I study engineering systems by starting from **what physically exists, how it interacts, and what can causally change what**. Mathematics enters after the physical and causal structure is identified, as the formal language for representation, analysis, computation, uncertainty, and decision-making.

[Research Portfolio](https://dossiya-se.github.io/) · [LinkedIn](https://www.linkedin.com/in/dossiya-dakou-/) · [ORCID](https://orcid.org/0009-0004-1071-9948)

---

## Professional profile

My research direction is **physics-grounded and mathematics-intensive**.

I begin with the engineering system itself: components, flows, services, constraints, hazards, operating limits, spatial structure, timescales, feedback, and failure/recovery processes. I then identify the **causal mechanisms** that transmit effects between system elements. Only after those mechanisms are stated do I introduce mathematical structures such as graphs, differential equations, dynamical systems, probability, optimization, topology, and differential geometry.

The governing logic is:

```math
\boxed{
\text{Physical Reality}
\rightarrow
\text{Causal Mechanisms}
\rightarrow
\text{Governing Physical Relations}
\rightarrow
\text{Mathematical Abstraction}
\rightarrow
\text{Analysis + Computation}
\rightarrow
\text{Uncertainty + Validation}
\rightarrow
\text{Engineering Decision / Control}
}
```

The purpose of mathematics is therefore not to decorate an engineering problem. It is to make the physical problem **precise, internally consistent, analyzable, testable, and decision-relevant**.

---

## Engineering reasoning framework

### 1 · Physical reality

Define what exists before defining symbols.

- physical components and interfaces;
- material, energy, information, and mobility flows;
- service requirements and operational limits;
- spatial and temporal scales;
- hazards, disturbances, degradation, and recovery processes;
- measurable state variables, parameters, and units.

This step establishes the **system boundary** and prevents the mathematical model from drifting away from the engineering object.

### 2 · Causal mechanisms

Determine **how and why one part of the system affects another**.

A dependency is not accepted merely because two variables are correlated. The mechanism should identify, when possible:

```math
\boxed{
\text{source}
\rightarrow
\text{physical / operational mechanism}
\rightarrow
\text{receiver}
\rightarrow
\text{effect}
}
```

with direction, sign, magnitude, delay, timescale, activation conditions, uncertainty, and evidence stated explicitly.

For interdependent infrastructure, I use a rigorous dependency object of the form

```math
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
\right),
```

so that an interdependency is treated as more than an arrow in a network diagram.

### 3 · Governing physical relations

The model must respect the relevant physics and engineering constraints.

A generic constrained system representation may contain

```math
C(Y,u,\eta;\theta)=0,
\qquad
G(Y,u,\eta;\theta)\le 0,
```

where equality constraints may encode conservation or constitutive relations and inequality constraints may encode capacity, safety, feasibility, or operating limits.

The exact equations must come from the system being studied; they are not assumed universally.

### 4 · Mathematical abstraction

Only after the physical system and causal mechanisms are defined do I choose the mathematical representation.

Examples include:

| Physical / engineering question | Mathematical structure |
|---|---|
| What is connected to what? | graph theory, multilayer networks, topology |
| How does the state evolve? | ODEs, DAEs, PDEs, hybrid dynamical systems |
| What states are feasible? | constraint sets, manifolds, admissible state spaces |
| How does disturbance propagate? | coupled dynamics, Jacobians, spectral structure |
| How uncertain is the model? | probability, stochastic processes, Bayesian inference |
| How far is the system from failure? | viability theory, distance functions, geometric structure |
| What intervention is best? | optimization, optimal control, robust decision models |

The mathematical object is selected because it matches the engineering mechanism—not because it is mathematically sophisticated.

### 5 · Analysis before simulation

Before large numerical experiments, I look for what can be established analytically:

- dimensional consistency;
- conservation and invariants;
- equilibria and stability;
- sensitivity and Jacobian structure;
- eigenvalues and spectral properties;
- bifurcation or regime-transition conditions;
- structural controllability / observability where relevant;
- limiting cases and asymptotic behavior.

This reduces the risk of using computation to hide a poorly formulated model.

### 6 · Computation

Numerical methods are used where analytical treatment is insufficient.

```math
\text{model}
\rightarrow
\text{discretization / algorithm}
\rightarrow
\text{numerical solution}
\rightarrow
\text{verification}
\rightarrow
\text{engineering interpretation}
```

Computation may include simulation, numerical integration, network algorithms, optimization, Monte Carlo methods, sensitivity analysis, or state estimation.

### 7 · Uncertainty

A deterministic output is not automatically a certain engineering conclusion.

I separate uncertainty associated with:

- measurements;
- parameters;
- model structure;
- hazard realization;
- causal assumptions;
- numerical approximation;
- future operating conditions.

Where appropriate, uncertainty is propagated into the quantities used for engineering decisions rather than reported separately from them.

### 8 · Verification and validation

I distinguish between:

```text
mathematical consistency
        ≠
physical plausibility
        ≠
numerical verification
        ≠
empirical validation
        ≠
engineering usefulness
```

A model can be mathematically correct and computationally reproducible while still being a poor representation of the physical system.

### 9 · Engineering decision and control

The final purpose is not merely to produce equations or predictions. It is to support a defensible engineering action:

```math
\boxed{
\text{understand}
\rightarrow
\text{predict}
\rightarrow
\text{compare interventions}
\rightarrow
\text{control / design / restore}
}
```

---

## Current research direction

### Interdependent power and transportation infrastructure

My present engineering focus is **coupled power and transportation systems**, while accounting for informational and organizational mechanisms when they alter physical operation, coordination, or recovery.

The research chain is:

```text
Physical infrastructure and service requirements
        ↓
Causal interdependencies and interface mechanisms
        ↓
Multilayer structural representation
        ↓
Coupled hybrid multiscale dynamics
        ↓
Feedback, control and uncertainty
        ↓
Viability and resilience boundaries
        ↓
Engineering intervention
        ↓
Sustainable transformation pathways
```

A compact mathematical abstraction is

```math
\mathcal R_{\mathrm{phys}}
\rightarrow
\mathcal C
\rightarrow
\mathcal G,\mathfrak I
\rightarrow
F_{\mathcal G}
\rightarrow
\mathcal V
\rightarrow
\rho_g
\rightarrow
u^\star,
```

where:

- `\mathcal R_{\mathrm{phys}}` denotes the physical system and operating reality;
- `\mathcal C` denotes causal mechanisms;
- `\mathcal G,\mathfrak I` represent structure and interdependencies;
- `F_{\mathcal G}` represents coupled system dynamics;
- `\mathcal V` represents a viable/admissible operating region;
- `\rho_g` represents a geometric resilience quantity when such a metric is justified;
- `u^\star` represents an engineering intervention or control decision.

These objects are research constructs whose physical interpretation, assumptions, and validation must be established for the specific system being studied.

---

## Physics and mathematics

I treat physics and mathematics as complementary but non-interchangeable.

```math
\boxed{
\begin{aligned}
\text{Physics} &:\ \text{What mechanisms and constraints govern the system?}\\
\text{Mathematics} &:\ \text{What follows logically from the formalized model?}\\
\text{Computation} &:\ \text{What can be evaluated numerically?}\\
\text{Data} &:\ \text{What is supported by observation?}\\
\text{Engineering} &:\ \text{What should be designed, controlled, or changed?}
\end{aligned}
}
```

### Mathematical foundations used for engineering applications

| Mathematical area | Role in the research |
|---|---|
| **Differential geometry** | state-space geometry, metrics, geodesic structure, constrained-state interpretation |
| **Graph theory & topology** | multilayer infrastructure structure, connectivity, interfaces, propagation pathways |
| **Analysis & differential equations** | continuous state evolution, stability, bounds and coupled dynamics |
| **Dynamical systems** | equilibria, stability, bifurcation, regime transitions and recovery trajectories |
| **Probability & stochastic processes** | hazards, measurement uncertainty, parameter uncertainty and reliability |
| **Optimization & control** | intervention, restoration, design and constrained resource allocation |

Pure mathematical structures are valuable here precisely because they can expose structure that is difficult to see directly in raw engineering data—but their engineering interpretation must remain physically defensible.

---

## Selected research & engineering work

### 01 · Mathematics for Sustainable Resilience
**Differential geometry · dynamical systems · resilience mathematics · mathematical communication**  
Explores mathematical structures and computational representations relevant to sustainability and resilience, with explicit separation between formal mathematics and physical interpretation.  
[Repository →](https://github.com/Dossiya-SE/Differential-geometry-and-Mathematics-arts-for-sustainability-and-resilience)

### 02 · Optimization for Sustainability and Resilience
**Linear algebra · LP/MILP · network optimization · constrained decision models**  
Develops optimization foundations for engineering decisions in which variables, objectives, constraints, feasibility and interpretation must be stated explicitly.  
[Repository →](https://github.com/Dossiya-SE/Optimization-for-sustainability-and-resilience)

### 03 · Africa Energy Dignity
**Energy systems · geospatial engineering · constrained planning**  
Engineering research on energy-access and infrastructure planning with emphasis on physical constraints, spatial reasoning, transparent assumptions and reproducible computation.  
[Repository →](https://github.com/Dossiya-SE/africa-energy-dignity)

### 04 · Python for Rapid Engineering Solutions
**Scientific computing · numerical analysis · reproducible engineering workflows**  
Computational work focused on converting engineering problems into auditable numerical procedures rather than isolated scripts.  
[Repository →](https://github.com/Dossiya-SE/Python-for-rapid-engineering-solution)

### 05 · Mathematical Research Portfolio
**Interactive mathematical communication · research demonstrations**  
A public surface for mathematical and computational research demonstrations that require richer interaction than a GitHub README can provide.  
[Portfolio →](https://dossiya-se.github.io/) · [Repository →](https://github.com/Dossiya-SE/dossiya-se.github.io)

---

## Research experience

### National University of Singapore
**Visiting Graduate Researcher · 2026**  
Research focus: **infrastructure-system interfaces and resilience**, including how dependencies between infrastructure components can be represented, measured, and connected to failure and recovery behavior.

---

## Education

**Arizona State University**  
MSE · Sustainable Engineering · Ongoing

**WorldQuant University**  
MSc · Financial Engineering · Ongoing

**Université d’Abomey-Calavi**  
Licence · Énergies Renouvelables et Systèmes Énergétiques

---

## Research and engineering capabilities

| Capability | Current emphasis |
|---|---|
| **Physical-system reasoning** | components, flows, constraints, operating limits, hazards and service functions |
| **Causal mechanism modeling** | directionality, interfaces, delays, feedback and propagation mechanisms |
| **Mathematical abstraction** | selecting formal structures consistent with the engineering mechanism |
| **Dynamical modeling** | coupled, hybrid and multiscale state evolution |
| **Optimization & control** | constrained decisions, restoration and intervention design |
| **Scientific computing** | numerical analysis, simulation, network computation and reproducible workflows |
| **Uncertainty reasoning** | parameter, measurement, structural and scenario uncertainty |
| **Verification & validation** | separating implementation correctness from empirical adequacy |

### Computational toolkit

**Scientific computing:** Python · NumPy · SciPy · SymPy · pandas · NetworkX · Matplotlib  
**Optimization / numerical work:** mathematical programming · numerical linear algebra · Julia / MATLAB where appropriate  
**Research communication:** LaTeX · Overleaf · TikZ · Markdown  
**Engineering workflow:** Git · GitHub Actions · reproducible computational pipelines

---

## Research standard

My working standard is:

```math
\boxed{
\text{Mechanism before model}
\quad\cdot\quad
\text{Physics before abstraction}
\quad\cdot\quad
\text{Analysis before interpretation}
\quad\cdot\quad
\text{Validation before strong claims}
}
```

In practice:

- correlation is not treated as causation without a defensible mechanism;
- equations must have defined variables, parameters, units, domains and assumptions;
- conservation and constitutive relations are enforced where physically applicable;
- mathematically elegant structures are not automatically physically meaningful;
- simulation is not relabeled as observation;
- passing software tests is not relabeled as empirical validation;
- uncertainty is propagated when it materially affects engineering conclusions;
- every model should have a stated validity domain and known limitations.

---

## Research interests

**Physics-grounded mathematical engineering** · Pure mathematical structures for engineering applications · Differential geometry · Graph theory · Topology · Dynamical systems · Analysis · Optimization · Uncertainty · Complex systems · Sustainable infrastructure · Infrastructure resilience

---

## Connect

[Research Portfolio](https://dossiya-se.github.io/) · [LinkedIn](https://www.linkedin.com/in/dossiya-dakou-/) · [ORCID](https://orcid.org/0009-0004-1071-9948)

**Observe the physical system. Identify the mechanism. Formalize mathematically. Compute. Validate. Intervene.**
