# Mathematical Architecture Preserved from This Chat

This file preserves the cross-repository mathematical architecture used to structure the profile, website, thesis visual language and evidence-first portfolio.

## 1. Six-chain research architecture

### Chain I — Physics → Structure → Interfaces → Dynamics

Representative form:

```text
x_dot_i = f_i(x_i, theta_i)
          + sum_j g_ij(x_i, x_j, G_ij, theta_ij)
          + B_i u_i + xi_i
```

Typical mathematics:

- conservation laws;
- ODE/PDE systems;
- constitutive relations;
- hybrid systems;
- graph and multilayer-network structure;
- nonlinear dynamics;
- timescale separation;
- dynamic interface states.

### Chain II — Observe → Identify → Estimate → Predict

Representative observation model:

```text
y_k = h(x(t_k), theta) + epsilon_k
```

Representative inverse problem:

```text
theta_hat = arg min_theta sum_k ||y_k - h(x(t_k; theta))||^2
```

or, in a Bayesian formulation,

```text
p(theta | y) proportional to p(y | theta) p(theta)
```

Typical mathematics:

- inverse problems;
- identifiability;
- Bayesian inference;
- filtering;
- data assimilation;
- system identification;
- uncertainty covariance/posterior geometry.

### Chain III — Hazard → Failure → Service Loss → Consequences

Typical mathematics:

- fragility/reliability;
- stochastic processes;
- cascading failure;
- percolation/network failure;
- threshold models;
- extreme events;
- rare-event methods;
- consequence/loss functionals.

### Chain IV — Recovery → Resilience → Reachability → Viability

Composite service example:

```text
S(t) = w^T x(t),    w_i >= 0,    sum_i w_i = 1
```

One possible finite-horizon service functional:

```text
R_T = (1/T) integral_0^T S(t) dt
```

Projected admissibility example:

```text
K_R = K_phys ∩ K_service ∩ K_sus ∩ K_eq
```

Viability concept:

```text
V_R = {x_0 in K_R : exists u(.) such that x(t) in K_R for all t in [0,T]}
```

Recovery/capture concepts may be represented separately as `C_R`, recovery time `tau_R(x)` or other explicitly defined reachability objects.

### Chain V — Decision → Control → Optimization → Adaptation

Representative control feasibility:

```text
u in U_V(x)
```

Representative design problem:

```text
d* = arg min_d J(d)
subject to dynamics, admissibility, risk and service constraints
```

Typical mathematics:

- optimal control;
- robust/stochastic control;
- model-predictive control;
- convex/nonconvex optimization;
- integer/mixed-integer methods;
- multi-objective/Pareto optimization;
- sensitivity and duality.

### Chain VI — Service → Population → Equity → Critical-Service Continuity

Do not infer social/equity performance directly from physical asset states.

A rigorous architecture requires an explicit service-to-population mapping before equity constraints are interpreted.

Typical mathematics:

- spatial allocation;
- welfare/distribution functionals;
- equity constraints;
- multi-objective optimization;
- risk measures;
- accessibility/coverage metrics.

---

## 2. Parallel forcing and inference architecture

A critical correction from this chat is that the **physical forcing chain and inference chain are parallel inputs** to the scientific model.

### Physical chain

```text
climate forcing xi
→ hazard eta
→ state/interface/mode evolution (X, Z, m)
→ service trajectory Y or S
```

### Inference chain

```text
observations D_obs
→ observation operator
→ inverse problem
→ (G_hat, theta_hat, Sigma_theta)
```

### Decision chain

```text
uncertain coupled model
→ service + population mapping
→ K_R
→ V_R / C_R / reachability objects
→ feasible controls
→ design / adaptation decision
```

Do not collapse these into one literal cause-effect arrow.

---

## 3. Current P–W–T–SW browser demonstrator

The public research website implements a reduced normalized state:

```text
x(t) = [x_P, x_W, x_T, x_SW]^T in [0,1]^4
```

with an illustrative reduced model of the form:

```text
x_dot_i = r_i(1-x_i)
          + b_i u(1-x_i)
          - h_i(t)x_i
          - sum_{j != i} c_ij x_i(1-x_j)
```

Interpretation:

- endogenous recovery;
- intervention-assisted recovery;
- hazard degradation;
- asymmetric interdependency penalty.

Status: **research demonstrator, not field-calibrated physical law**.

---

## 4. Continuous-time viability/violation diagnostics

Do not use a count of stored output states as “time.”

Define a margin, for example:

```text
m_V(t) = min_i[x_i(t) - x_i,min]
```

and approximate:

```text
T_V = measure{t in [0,T] : m_V(t) >= 0}
phi_V = T_V / T
```

For a composite service floor:

```text
T_viol = measure{t in [0,T] : S(t) < S_min}
phi_viol = T_viol / T
```

The browser implementation approximates threshold-crossing times by linear interpolation between consecutive RK4 output states.

---

## 5. Numerical integration rule

Classical RK4 is used in the browser demonstrator.

At the final integration step:

```text
dt_k = min(dt, T - t_k)
```

so the trajectory terminates exactly at the declared horizon rather than intentionally stepping beyond it.

Future publication-grade work should additionally include timestep-convergence and independent-solver/analytical comparison where possible.

---

## 6. Synthetic inverse problem

Synthetic observations:

```text
y_k = S(t_k; alpha*) + epsilon_k
```

Grid-search/least-squares demonstrator:

```text
alpha_hat = arg min_alpha sum_k [y_k - S(t_k; alpha)]^2
```

The experiment is seeded for reproducibility.

It demonstrates inverse-problem plumbing/objective geometry. It does not establish structural identifiability or field calibration.

---

## 7. Monte Carlo uncertainty propagation

Illustrative estimator:

```text
P_hat_f = (1/N) sum_n 1{min_t S^(n)(t) < S_min}
```

The probability is conditional on the declared illustrative uncertainty distribution.

It must not be presented as a field-calibrated infrastructure failure probability.

---

## 8. Dynamic-interface uncertainty research direction

A central thesis-level mapping retained from the conversation is:

```text
D_obs
→ (G_hat_ij, theta_hat_ij)
→ Sigma_theta
→ uncertainty in coupled dynamics
→ uncertainty/deformation of K_R, V_R, C_R
```

One research question is therefore geometric:

> How does uncertainty in inferred interface structure/parameters deform the safe-sustainable-equitable viability and recovery sets?

Possible error measures include distances between true and inferred viable sets, boundary displacement, decision regret or loss of feasible-control volume, but any specific metric must be explicitly defined before use.

---

## 9. Interface-resilience timing architecture

For interface `i`:

```text
T_response,i = T_detect,i
             + T_communicate,i
             + T_authorise,i
             + T_mobilise,i
             + T_actuate,i
```

A basic timeliness condition is:

```text
T_response,i < T_cascade,i
```

Decision split retained from the interface project:

```text
A_i = C_i P_control,i
H_i = C_i (1 - P_control,i)
```

where `A_i` represents responsive priority and `H_i` pre-emptive hardening urgency under the defined project model.

---

## 10. RGAN mathematical objects

Illustrative transparent valuation architecture:

```text
V_hat = m_hat q_hat P_market - fees
```

Measurement/valuation uncertainty can be propagated locally by a Jacobian approximation:

```text
u^2(V_hat) approx J Sigma J^T
```

Other mathematical objects used visually:

- network topology from Miner → GO → HUB → STATION/market;
- inventory/custody risk;
- service/capacity constraints;
- multi-objective cost-security-accessibility trade-offs;
- Pareto design sets.

Status: design/research architecture unless backed by direct prototype/field evidence.

---

## 11. Quantitative-finance mathematical objects

Visual portfolio examples include:

- Heston/Bates stochastic dynamics;
- Fourier/Carr–Madan or Lewis pricing pathways;
- Monte Carlo estimators and confidence/error diagnostics;
- CIR short-rate dynamics;
- calibration objective surfaces;
- cross-method and numerical-stability checks.

A calibrated parameter vector is conditional on model family, data, objective, weights, bounds and numerical method. Calibration is not truth.

---

## 12. Econometrics/EDA mathematical objects

Examples preserved in the portfolio:

### Omitted-variable bias

```text
plim beta_hat_omit = b + c Cov(X,Z)/Var(X)
```

### Covariance/correlation

```text
Sigma = E[(X-mu)(X-mu)^T]
rho_ij = Sigma_ij / (sigma_i sigma_j)
```

These are association/model-structure objects, not causal claims by themselves.

---

## 13. Machine-learning evidence pipeline

Conceptual visual chain:

```text
problem
→ provenance-controlled data
→ split
→ preprocessing fitted without leakage
→ baseline
→ model
→ metrics + uncertainty
→ diagnostics/robustness
→ bounded claim
```

A repository title or installed package is not evidence of completed ML research.

---

## 14. Chatbot probability/integration boundary

Generic autoregressive factorization can be shown conceptually as:

```text
p(y_1:T | x) = product_t p(y_t | y_<t, x)
```

But the repository itself is evidence of API/UI/session integration, not evidence of model training or original LLM architecture.

---

## 15. Profile explanatory chain

For compact GitHub-profile communication, the following is acceptable:

```text
Physics → Evidence → Mathematics → Computation → Verification → Decision → Resilient Service
```

This is a portfolio narrative, not a theorem or universal systems-science ontology.
