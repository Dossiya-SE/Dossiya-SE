# Mathematical Art System

This directory defines the visual mathematics used by the GitHub profile.

The objective is not decoration. Each visual element corresponds to a mathematical object used in infrastructure-resilience research.

## Visual grammar

| Visual element | Mathematical meaning |
|---|---|
| Coupled nodes | Infrastructure subsystems and interdependencies |
| Dynamic edge `G(t)` | Time-varying interface or coupling strength |
| State trajectory | Evolution of the coupled system under disturbance and control |
| Dashed outer region | Safe-sustainable-equitable viability boundary |
| Nested ellipses | Uncertainty or nested admissible state regions |
| Recovery trajectory | Controlled return toward acceptable service states |
| Grid | State-space / phase-space reference structure |

## Canonical equations

### Coupled dynamics

$$
\dot{x}_i=f_i(x_i,\theta_i)+\sum_j g_{ij}(x_i,x_j,G_{ij},\theta_{ij})+B_i u_i+\xi_i.
$$

### Observation and inverse problem

$$
y_k=h(x_k,\theta)+\varepsilon_k,
\qquad
\pi(\theta\mid y)\propto L(y\mid\theta)\pi_0(\theta).
$$

### Reliability and failure

$$
P_f=P\left[g(X,H)\le 0\right].
$$

### Service resilience

$$
\mathcal R_T=\frac{1}{T}\int_0^T\frac{S(t)}{S_0}\,dt.
$$

### Viability

$$
\mathcal V=\{x_0:\exists u(\cdot),\;x(t)\in\mathcal K,\;\forall t\in[0,T]\}.
$$

## Design rules

1. Equations must have a scientific interpretation.
2. Geometry must map to an explicit systems concept.
3. Decorative curves must be generated from or interpretable as trajectories, manifolds, envelopes or fields.
4. Labels should use the same symbols as the research models.
5. Visuals should remain legible in GitHub dark and light themes.
6. SVG is preferred for profile assets because it is scalable and text-readable.
7. Static art should remain deterministic and version-controlled.

## Current asset

- `../assets/mathematical-resilience.svg` — coupled P-W-T-SW infrastructure, dynamic interface, control trajectory and viability geometry.

## Future mathematical-art modules

- Lorenz-style uncertainty attractor for cascading dynamics.
- Spectral graph / Laplacian visualization of interface criticality.
- Viability-kernel contour map.
- Pareto front for resilience-equity-cost tradeoffs.
- Bayesian posterior geometry for interface identification.
- Reachability tube for recovery control.
