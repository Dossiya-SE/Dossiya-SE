# Dossiya-SE Profile Formula Atlas — V3

This atlas is the human-readable companion to [`formula_registry.json`](formula_registry.json). It organizes the mathematical objects actually used, specified, or explicitly proposed across the profile.

The atlas is **not a claim of exhaustive mastery of mathematics**. It is a traceable map of the mathematical structures relevant to the profile's research and engineering work.

---

## 1. Geometry and topology

### Surface metric — [S]

```math
g_{\alpha\beta}
=
\partial_\alpha\mathbf r\cdot\partial_\beta\mathbf r.
```

Defines intrinsic length/angle structure on a regular surface chart.

### Levi-Civita connection — [S]

```math
\Gamma^\alpha_{\beta\gamma}
=
\frac12g^{\alpha\delta}
\left(
\partial_\beta g_{\gamma\delta}
+
\partial_\gamma g_{\beta\delta}
-
\partial_\delta g_{\beta\gamma}
\right).
```

### Geodesic equation — [S]

```math
\frac{d^2u^\alpha}{ds^2}
+
\Gamma^\alpha_{\beta\gamma}
\frac{du^\beta}{ds}
\frac{du^\gamma}{ds}=0.
```

The profile does not equate "geodesic" with "globally optimal recovery" unless a research model defines a metric/action for which that claim is tested.

### Gaussian curvature — [S]

```math
K=\frac{eg-f^2}{EG-F^2}.
```

### Gauss–Bonnet — [S]

```math
\iint_S K\,d\sigma=2\pi\chi.
```

Primary source anchor: the Sochi differential-geometry foundation registered in the Mathematics Research Ecosystem.

---

## 2. Coupled dynamical systems

### Generic coupled dynamics — [M]

```math
\dot x_i
=
f_i(x_i,\theta_i)
+
\sum_{j\ne i}g_{ij}(x_i,x_j,G_{ij},\theta_{ij})
+
B_i u_i
+
\xi_i.
```

This representation separates subsystem dynamics, interfaces, controls, and forcing.

### Hybrid multiscale state/interface system — [M]

```math
\begin{aligned}
\dot X &= F(X,Z,m,u,\eta;\theta),\\
\varepsilon\dot Z &= G(X,Z,m,\eta;\theta),\\
m^+ &= \Phi(X,Z,m,\eta),\\
Y &= H(X,Z;\theta)+\varepsilon_Y.
\end{aligned}
```

Primary repository: `MSE-thesis`.

---

## 3. Viability, recovery, reachability, and control

### Sustainable-equitable admissibility — [M]

```math
K_R
=
K_{phys}
\cap
K_{service}
\cap
K_{sus}
\cap
K_{eq}.
```

### Viability kernel — [M]

```math
\mathcal V_R
=
\left\{
x_0\in K_R:
\exists u(\cdot)\in\mathcal U,
\;X(t;x_0,u,\eta,\theta)\in K_R
\;\forall t\ge0
\right\}.
```

### Capture/recovery set — [M]

```math
\mathcal C_R
=
\left\{
x_0:
\exists u(\cdot),\exists T<\infty,
\;X(T;x_0,u)\in\mathcal V_R
\right\}.
```

### Recovery-time map — [M]

```math
\tau_R(x_0)
=
\inf
\left\{
T:
\exists u(\cdot),
X(T;x_0,u)\in\mathcal V_R
\right\}.
```

The profile explicitly distinguishes **viable**, **recoverable but nonviable**, and **nonrecoverable** states.

---

## 4. Networks and interfaces

### Graph Laplacian — [S]

```math
L=D-A.
```

Used only when a graph/spectral representation is actually defined. A network illustration does not imply a spectral analysis has been performed.

### Dynamic interface object — [M]

```math
G_{ij}(t)
=
\{\text{topology, capacity, authority, latency, state, uncertainty}\}.
```

### Response latency — [M]

```math
T_{response,i}
=
T_{detect,i}
+
T_{communicate,i}
+
T_{authorise,i}
+
T_{mobilise,i}
+
T_{actuate,i}.
```

A project-level timely-action condition is

```math
T_{response,i}<T_{cascade,i}.
```

Primary repository: `infrastructure-interface-resilience-review`.

---

## 5. Inverse problems and Bayesian uncertainty

### Observation model — [M]

```math
y_k=h(x_k,\theta)+\varepsilon_k.
```

### Bayesian posterior — [M]

```math
\pi(\theta\mid y)
\propto
L(y\mid\theta)\pi_0(\theta).
```

### Least-squares inverse problem — [M]

```math
\widehat\alpha
=
\arg\min_\alpha
\sum_{k=1}^m
\left[y_k-S(t_k;\alpha)\right]^2.
```

The browser portfolio includes a synthetic seeded inverse-problem demonstrator; it is not presented as empirical infrastructure identification.

---

## 6. Probability, reliability, and uncertainty quantification

### Failure probability — [M]

```math
P_f
=
\mathbb P\!\left[g(X,H)\le0\right].
```

### Covariance — [S]

```math
\Sigma
=
\mathbb E\!\left[(X-\mu)(X-\mu)^T\right].
```

### Correlation — [S]

```math
\rho_{ij}
=
\frac{\Sigma_{ij}}{\sigma_i\sigma_j}.
```

Association is not interpreted as causation.

---

## 7. Energy systems

### Energy balance — [M]

```math
P_{gen}+P_{import}+P_{dis}
=
P_{load}+P_{loss}+P_{ch}+P_{export}.
```

### Storage accounting — [M]

```math
SOC_{t+1}
=
SOC_t
+
\eta_cE_{ch}
-
\frac{E_{dis}}{\eta_d}.
```

### Rapid-deployment decomposition — [M]

```math
T_{impact}
=
T_{diagnosis}
+
T_{design}
+
T_{approval}
+
T_{finance}
+
T_{procurement}
+
T_{construction}
+
T_{commissioning}.
```

Primary repository: `africa-energy-dignity`; storage prototype example also appears in `testasu`.

---

## 8. Optimization and decision mathematics

### Multiobjective engineering design — [M]

```math
\min_d
\left[
C(d),E(d),T(d),Risk(d)
\right],
\qquad
\max_d
\left[
Service(d),Resilience(d),Sovereignty(d)
\right].
```

No single scalar optimum is implied unless preferences, constraints, and scalarization are declared.

### Transparent weighted score — [T]

```math
s(x)=\sum_jw_j\phi_j(x),
\qquad
w_j\ge0,
\qquad
\sum_jw_j=1.
```

This is a future decision-support design target in `Kudo-IA`, not a validated scholarship-success predictor.

---

## 9. Quantitative finance

### Stochastic-volatility price process — [M]

```math
dS_t
=
\mu S_t\,dt
+
\sqrt{v_t}S_t\,dW_t^S
+
\text{jump term}.
```

### Square-root variance process — [M]

```math
dv_t
=
\kappa(\theta-v_t)\,dt
+
\sigma\sqrt{v_t}\,dW_t^v.
```

### CIR-style short rate — [M]

```math
dr_t
=
\kappa(\theta-r_t)\,dt
+
\sigma\sqrt{r_t}\,dW_t.
```

### Calibration — [M]

```math
\widehat\theta
=
\arg\min_\theta
\sum_i
w_i
\left[
V_{model}(K_i,T_i;\theta)-V_{market,i}
\right]^2.
```

Primary repository: `Dossiya-SE-mscfe-quantitative-finance-lab`.

---

## 10. Econometrics and model risk

### Omitted-variable-bias target — [D]

```math
\operatorname{plim}\widehat\beta_{omit}
=
\beta
+
\gamma
\frac{\operatorname{Cov}(X,Z)}{\operatorname{Var}(X)}.
```

Primary repository: `dossiyadakou-mac-project`.

This is displayed as an analytical model-risk mechanism, not as universal causal identification.

---

## 11. Machine learning

### Regularized empirical risk — [M/T]

```math
\theta^*
=
\arg\min_\theta
\sum_i
\ell(f_\theta(x_i),y_i)
+
\lambda\Omega(\theta).
```

### Held-out empirical risk — [M/T]

```math
\widehat R_{test}
=
\frac{1}{n_{test}}
\sum_i
\ell(f_\theta(x_i),y_i).
```

Primary repository: `Data-Science-an-Machine-Learning`, currently a learning/quality scaffold rather than validated-model evidence.

---

## 12. Measurement, valuation, and secure systems design

### Measurement model — [M]

```math
\widehat m=m+\varepsilon_m,
\qquad
\widehat q=q+\varepsilon_q.
```

### Transparent valuation — [M]

```math
\widehat V
=
\widehat m\,\widehat q\,P_{market}
-
fees.
```

### Custody-risk abstraction — [M]

```math
Risk
=
\mathbb P(loss\mid state)
\times
Consequence(value).
```

Primary repository: `responsible-gold-access-network-rgan`.

---

## 13. Probabilistic sequence models

### Autoregressive factorization — [S]

```math
p(y_{1:T}\mid x)
=
\prod_{t=1}^{T}
p(y_t\mid x,y_{1:t-1}).
```

In `chatbot` this formula is explanatory only. The repository integrates an external model service and does not claim implementation of the model's training or internal inference mathematics.

---

## 14. Cross-profile synthesis

The common mathematical workflow is

```math
\boxed{
\text{Evidence}
\rightarrow
\text{State/Geometry}
\rightarrow
\text{Dynamics}
\rightarrow
\text{Inference}
\rightarrow
\text{Uncertainty}
\rightarrow
\text{Constraints}
\rightarrow
\text{Control/Optimization}
\rightarrow
\text{Verification}
\rightarrow
\text{Validation}
\rightarrow
\text{Decision}
}
```

The profile's visual mathematics should make this chain visible without hiding the evidence boundaries between its stages.
