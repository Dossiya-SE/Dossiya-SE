# SCIENTIFIC-RESEARCH-ARCHITECTURE-V1.0

**Status:** Governing upstream research-design standard  
**Effective date:** 2026-08-24  
**Scope:** Scientific papers, theses, quantitative research, mathematical/computational modeling, engineering studies, industrially motivated research, simulation studies, validation studies, and research software that supports scientific claims.

This standard governs **how a research problem is framed, modeled, computed, verified, validated, interpreted, and bounded**. It is upstream of reporting standards such as `APA_JARS_QUANT_ADAPTED_REPORTING_STANDARD.md`.

It does not replace stricter journal, institutional, ethics, safety, regulatory, or discipline-specific requirements.

---

## 1. Governing research chain

Every research project must expose a traceable chain:

```text
Real problem
-> Evidence
-> Gap architecture
-> Research question
-> Contribution class
-> System definition
-> Mathematical/statistical formulation
-> Data / parameter provenance
-> Numerical or analytical method
-> Verification
-> Calibration, if applicable
-> Validation
-> Sensitivity + uncertainty
-> Baseline comparison
-> Results
-> Scientific interpretation
-> Industrial/practical implication, if claimed
-> Limitations
-> Bounded conclusion
-> Reproducibility package
```

A project may omit a stage only when it is genuinely inapplicable and the reason is explicit.

---

## 2. Non-compensatory evidence invariant

No strength in one dimension may silently compensate for a missing required dimension.

A mathematically sophisticated model does not compensate for absent validation when validation is required. A visually convincing simulation does not become observation. Passing software tests does not establish empirical truth. Industrial relevance does not establish scientific novelty. Publication count does not establish model correctness.

For a public claim `C`, let `R(C)` be the required support dimensions and `L_k` their admissible maturity levels. Then:

```math
L(C) \le \min_{k\in R(C)} L_k
```

The weakest required support dimension bounds the claim.

---

## 3. Start from the real problem

Before selecting equations, algorithms, data, or software, define:

| Element | Required question |
|---|---|
| System | What physical, biological, financial, industrial, infrastructure, social, or computational system is studied? |
| Phenomenon | What failure, recovery, transport, instability, optimization, risk, control, inference, or other mechanism is being investigated? |
| Stakeholders | Who is affected by the phenomenon or decision? |
| Decision | What prediction, estimation, design, control, maintenance, policy, investment, or operational decision matters? |
| Scale | Component, process, network, organization, city, region, market, or other scale? |
| Time scale | What temporal horizon and resolution govern the problem? |
| Failure / success criterion | What exact condition constitutes failure, service loss, risk, infeasibility, inequity, or success? |

The research question must remain connected to this problem definition.

---

## 4. Gap architecture

Do not use one vague statement such as “few studies have examined this.” Identify the specific gap class and its evidence.

| Gap class | Core question | Minimum evidence type |
|---|---|---|
| Scientific | What phenomenon remains insufficiently understood? | Peer-reviewed literature / authoritative scientific synthesis |
| Theoretical | What concept, mechanism, relation, theorem-level structure, or theory is missing or insufficient? | Theory papers / reviews / formal literature |
| Methodological | What existing method cannot adequately estimate, predict, identify, optimize, control, or test? | Method comparisons / benchmark evidence |
| Mathematical | What variables, states, couplings, geometry, dynamics, constraints, or admissible sets are absent or inadequate? | Existing equations and mathematical models |
| Data | What observations, variables, spatial/temporal coverage, labels, or measurements are unavailable or incomplete? | Dataset documentation / measurement studies / audits |
| Validation | What has been proposed or simulated but not independently or empirically tested for the intended use? | Validation literature / benchmark evidence |
| Industrial / practice | What remains unresolved in actual engineering, operations, production, maintenance, or decision workflows? | Industry reports / operator evidence / standards / field studies |
| Technology | What current technology cannot reliably, safely, accurately, or economically accomplish? | Technical specifications / field evidence / technology assessments |
| Implementation | Why has a known scientific or technical solution not translated into reliable practice? | Case studies / implementation evidence |
| Regulatory | What law, standard, certification, safety, or regulatory condition blocks or constrains deployment? | Regulations / standards / regulator publications |
| Institutional | What ownership, governance, coordination, capability, or responsibility structure is missing? | Governance and institutional evidence |
| Economic / financial | What cost, financing, incentive, market, or bankability barrier remains? | Economic / financial evidence |
| Equity | Who is underserved, excluded, exposed, or disproportionately burdened? | Population / service / distributional evidence |
| Computational | What cannot be computed, optimized, inferred, or rendered with required accuracy, stability, speed, or scale? | Benchmarks / complexity / numerical evidence |
| Reproducibility | What result cannot be independently reconstructed from accessible data, code, configuration, and provenance? | Reproduction audit / code-data availability review |

### Gap invariants

```text
absence in papers != industrial failure
industrial difficulty != scientific novelty
simulation success != field validation
unavailable data != proof that a phenomenon does not exist
```

Each claimed gap must have its own evidence chain.

A strong bridge is often:

```text
Industrial problem
-> scientific limitation
-> methodological/mathematical gap
-> research contribution
```

---

## 5. Research question and falsifiability

A primary research question should identify, where applicable:

```text
system + mechanism + condition + outcome
```

Examples:

```text
How does X influence Y under condition Z in system S?
```

```text
Can model M estimate / predict / control Y under uncertainty U within declared tolerances?
```

A project should identify what observation, benchmark, comparison, or failure would weaken or falsify the principal claim.

---

## 6. Contribution classes

Do not state only “this paper proposes a model.” Classify the contribution.

- **Conceptual:** new system representation or conceptual distinction.
- **Mathematical:** new equation, coupling, state representation, admissible set, theorem, derivation, or formal structure.
- **Methodological:** new estimation, inference, optimization, experimental, or validation procedure.
- **Computational:** new numerical algorithm, solver architecture, acceleration, or computational workflow.
- **Empirical:** new measurement, dataset-derived result, experiment, or observation.
- **Industrial / engineering:** implementable workflow, design, process, or operational improvement.
- **Validation:** new independent, cross-context, field, benchmark, or external validation evidence.
- **Data:** new curated, measured, linked, annotated, or provenance-controlled dataset.
- **Software:** reproducible implementation of a scientific or engineering method.

Every contribution claim must be bounded by the evidence actually present.

---

## 7. System definition

Define before solving:

- system boundary;
- environment and external forcing;
- spatial and temporal domain;
- unit of analysis;
- interfaces and couplings;
- states and observables;
- controllable inputs;
- disturbances / hazards;
- success, failure, admissibility, and service criteria.

A model is not fully specified when its system boundary is ambiguous.

---

## 8. Mathematical-model inventory

For mathematical or computational modeling, freeze the following before claiming results.

### 8.1 Purpose

State whether the model is intended to **describe, explain, estimate, identify, predict, optimize, control, design, reconstruct, or visualize**.

### 8.2 State variables

```math
\mathbf{x}(t)=[x_1(t),\ldots,x_n(t)]^\top
```

Every state must have a physical, mathematical, statistical, or operational interpretation.

### 8.3 Inputs and controls

```math
\mathbf{u}(t)
```

Identify what can be controlled and what cannot.

### 8.4 Disturbances / forcing

```math
\boldsymbol{\eta}(t)
```

Identify hazards, shocks, exogenous forcing, or stochastic disturbances separately from control variables.

### 8.5 Parameters

```math
\boldsymbol{\theta}=[\theta_1,\ldots,\theta_p]
```

Each parameter requires definition, unit, admissible range, provenance, and uncertainty status.

### 8.6 Governing equations

A generic dynamical form is:

```math
\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x},\mathbf{u},\boldsymbol{\eta},\boldsymbol{\theta},t)
```

Observation models should be explicit, for example:

```math
\mathbf{y}_k=\mathbf{h}(\mathbf{x}_k,\boldsymbol{\theta})+\boldsymbol{\varepsilon}_k
```

Optimization problems must state objective and constraints, for example:

```math
\mathbf{u}^*=\arg\min_{\mathbf{u}}J(\mathbf{x},\mathbf{u})
```

subject to declared equality and inequality constraints.

### 8.7 Assumptions

Number controlling assumptions (`A1`, `A2`, ...). State what each assumption enables and what failure of that assumption would affect.

```text
Conclusion validity is conditional on the assumptions required by that conclusion.
```

### 8.8 Domain

Declare spatial, temporal, state, and parameter domains, for example:

```math
(x,y,z)\in\Omega\subset\mathbb{R}^3, \qquad t\in[0,T], \qquad \theta\in\Theta
```

### 8.9 Initial conditions

For dynamic systems, declare:

```math
\mathbf{x}(0)=\mathbf{x}_0
```

### 8.10 Boundary conditions

For PDE or spatial models, declare the applicable boundary conditions: Dirichlet, Neumann, Robin, periodic, absorbing, reflecting, inflow/outflow, or another justified condition.

### 8.11 Units and dimensional consistency

Maintain a symbol table and verify dimensional consistency. A visually plausible equation with incompatible dimensions fails the mathematical gate.

### 8.12 Outputs

Define exactly what the model produces: state trajectory, probability, risk, optimal policy, geometry, field, estimate, forecast, uncertainty interval, or other quantity.

---

## 9. Data and parameter provenance

Classify every controlling input as one of:

```text
Observed / measured
Published / official
Calibrated
Derived
Assumed / design target
Synthetic
Planned / unavailable
```

Never silently promote an assumed or synthetic value to observation.

For data-driven studies record source, version, acquisition date, inclusion/exclusion, missingness, transformations, alignment, identifiers/hashes where possible, and the relation between raw and derived datasets.

---

## 10. Analytical and numerical method

Prefer an analytical solution when it exists and is appropriate. Otherwise declare the numerical method and why it is suitable.

Examples:

```text
ODE -> RK family / BDF / symplectic method
PDE -> finite difference / finite volume / finite element / spectral method
Optimization -> LP / QP / NLP / MILP / dynamic programming
Inverse problem -> least squares / regularized inversion / Bayesian inference
Uncertainty -> Monte Carlo / bootstrap / PCE / interval / Bayesian propagation
Geometry -> symbolic derivatives / automatic differentiation / mesh-based discrete differential geometry
```

The numerical method is part of the scientific method, not merely a coding detail.

Record tolerances, discretization, solver versions, stopping criteria, initialization, random seeds, and failed-solve rules.

---

## 11. Verification

Verification asks:

> Did the implementation solve the declared equations or algorithm correctly?

Verification may include:

- analytical benchmarks;
- manufactured solutions;
- convergence studies;
- conservation / invariant checks;
- dimensional checks;
- primal/dual or KKT certificates;
- numerical residuals;
- cross-engine parity;
- regression tests;
- deterministic reproducibility;
- code-level unit/integration tests.

Where a discretization parameter `h` is refined, report convergence where applicable:

```math
\epsilon_h=\|x_h-x_{ref}\|, \qquad \epsilon_h\to0 \text{ as } h\to0
```

**Verification is not validation.**

---

## 12. Calibration and identification

When model parameters are unknown, distinguish parameter estimation from model validation.

A generic deterministic calibration may be written:

```math
\widehat{\theta}=\arg\min_\theta \|y_{obs}-y_{model}(\theta)\|^2
```

A Bayesian form is:

```math
p(\theta\mid y)\propto p(y\mid\theta)p(\theta)
```

Report identifiability, priors/regularization, parameter correlations, calibration data, and whether validation data are independent of calibration data.

---

## 13. Validation

Validation asks:

> Does the model represent the intended real system sufficiently well for its declared purpose and domain?

Use independent observations or external benchmarks where possible.

Validation should consider more than a single scalar metric. Depending on the problem, assess:

- temporal behavior;
- spatial behavior;
- regime transitions;
- extreme/failure cases;
- conservation and physical feasibility;
- calibration reliability;
- held-out predictive error;
- external validity;
- operational decision relevance.

If no empirical validation exists, state that explicitly. The model remains a mathematical/computational model or demonstrator, not a validated representation of reality.

---

## 14. Sensitivity analysis

Determine which assumptions and parameters control the conclusion.

Local sensitivity may examine:

```math
\frac{\partial Y}{\partial\theta_i}
```

Global methods should be used when interactions and nonlinearities make local derivatives inadequate.

If small plausible changes reverse the conclusion, this must be visible in the paper.

---

## 15. Uncertainty quantification

Distinguish uncertainty from:

- input measurements;
- parameters;
- disturbances;
- stochastic processes;
- model structure;
- numerical approximation;
- scenario choice;
- data coverage;
- human coding / labeling where relevant.

Propagate uncertainty to decision-relevant outputs rather than reporting only point estimates.

```math
Y=f(X,\theta,\eta) \quad \Rightarrow \quad \text{characterize }p(Y)\text{ or an appropriate uncertainty set}
```

---

## 16. Baselines and comparison

A proposed method should be compared against the strongest appropriate baseline(s):

- analytical solution;
- simpler model;
- established method;
- current industry practice;
- observed system;
- benchmark dataset;
- ablated model;
- previous literature result.

Complexity alone is not improvement.

---

## 17. Results discipline

Results answer the research question using the realized computation or evidence.

Keep distinct:

```text
model output != scientific interpretation
statistical association != causation
simulation != observation
verification != validation
visual resemblance != geometric or physical equivalence
```

Report negative, null, failed, infeasible, or non-robust results when they affect the conclusion.

---

## 18. Industrial and practical relevance

If industrial relevance is claimed, evaluate the method against the relevant deployment dimensions:

| Criterion | Required question |
|---|---|
| Accuracy | Is performance adequate for the use case? |
| Reliability | Does it work consistently across declared conditions? |
| Speed / latency | Can it operate within the required decision timescale? |
| Cost | Is acquisition, computation, deployment, and maintenance economically feasible? |
| Data burden | Can the required measurements actually be obtained at sufficient quality? |
| Interpretability | Can responsible users understand and audit the output? |
| Integration | Can it connect to existing technical and organizational systems? |
| Maintainability | Can the solution be maintained over its lifecycle? |
| Safety | Are safety constraints explicit and satisfied? |
| Regulation / standards | Are applicable regulatory and standards constraints addressed? |
| Scalability | Can performance and governance survive scale-up? |
| Human / institutional fit | Are roles, capabilities, incentives, and ownership compatible with deployment? |

A mathematically elegant model may fail industrially; that failure is scientifically relevant when industrial applicability is part of the claim.

---

## 19. Limitations and applicability boundary

Every final study must state, as applicable:

- what was not modeled;
- what was assumed;
- what was not measured;
- what remains uncalibrated or unvalidated;
- where the model may fail;
- where results should not be generalized;
- data and measurement limitations;
- identification limitations;
- numerical limitations;
- uncertainty not propagated;
- implementation constraints;
- regulatory/institutional constraints;
- unresolved contradictory evidence.

Limitations are part of the result boundary, not editorial decoration.

---

## 20. Reproducibility package

A reproducible computational study should preserve, where applicable:

```text
data
+ code
+ environment
+ parameters/configuration
+ random seeds
+ equations/specification
+ tests
+ validation artifacts
+ figures/tables
+ provenance/hashes
+ frozen commit/tag
```

Another researcher should be able to determine which exact evidence, configuration, code, and environment produced each controlling result.

---

## 21. Paper architecture

The default scientific-engineering paper structure is:

### Introduction

`real problem -> importance -> industrial/scientific context -> gap architecture -> research question -> contribution -> scope`

### Background / related work

`theory + prior scientific evidence + methods + industrial/practice evidence where relevant`

### System definition

`boundary + states + interfaces + forcing + scales + success/failure criteria`

### Mathematical / statistical formulation

`states + parameters + equations + constraints + assumptions + units + initial/boundary conditions`

### Methods

`data + provenance + transformations + algorithms + numerical methods + calibration/identification + experimental/computational design`

### Verification

`evidence that the implementation correctly solves the declared mathematical/computational problem`

### Validation

`evidence that the model is adequate for the intended real-world purpose`

### Sensitivity and uncertainty

`parameter/assumption dependence + propagated uncertainty`

### Results

`primary -> secondary -> robustness/falsification -> exploratory -> failures/non-robust results`

### Discussion

`direct answer -> mechanism -> comparison -> industrial/practical implications -> robustness -> limitations -> transferability -> next falsifiable test`

### Conclusion

`what was tested -> what was found -> what is supported -> what is not established -> most important boundary`

---

## 22. Acceptance gates

A project may declare `SCIENTIFIC_RESEARCH_ARCHITECTURE_PASS` only when every applicable gate below passes or is explicitly recorded as a deviation/limitation:

1. real problem and decision context are explicit;
2. each claimed gap is classified and separately evidenced;
3. scientific novelty and industrial relevance are not conflated;
4. primary research question is explicit and falsifiable/bounded;
5. contribution class is declared;
6. system boundary is defined;
7. controlling variables, parameters, units, assumptions, domains, equations, constraints, and initial/boundary conditions are defined where applicable;
8. data and parameter provenance are classified;
9. analytical/numerical method is reproducible;
10. verification is completed and distinguished from validation;
11. calibration/identification is documented where applicable;
12. validation evidence matches the intended use claim, or absence of validation is explicit;
13. sensitivity and uncertainty affecting conclusions are evaluated;
14. appropriate baselines are compared;
15. failed/non-robust outcomes are preserved;
16. industrial implications, if claimed, are supported by industrial/practice evidence and deployment constraints;
17. limitations and applicability boundaries are explicit;
18. conclusions do not exceed the weakest required support dimension;
19. reproducibility artifacts are linked to a frozen repository state.

A failed gate must never be silently converted to PASS.

---

## 23. Relationship to other repository standards

Use this hierarchy:

1. **Destination authority:** journal, institution, ethics, law, regulation, safety, course requirements.
2. **Research-design authority:** `SCIENTIFIC_RESEARCH_ARCHITECTURE_V1.md`.
3. **Quantitative reporting authority:** `APA_JARS_QUANT_ADAPTED_REPORTING_STANDARD.md`.
4. **Final-report audit:** `APA_JARS_QUANT_REPORT_CHECKLIST.md`.
5. **Writing scaffold:** `QUANTITATIVE_REPORT_TEMPLATE.md`.
6. **Domain/project protocols:** stricter project-specific methods, systematic-review protocols, validation plans, evidence engines, or release gates.

Lower layers may add stricter controls but must not silently weaken higher applicable requirements.

---

## 24. Version control

Any change that alters required gates, evidence classes, gap taxonomy, model inventory, or claim boundaries must increment the version and record the rationale. Project-specific adaptations may be stricter but must remain traceable to this governing architecture.