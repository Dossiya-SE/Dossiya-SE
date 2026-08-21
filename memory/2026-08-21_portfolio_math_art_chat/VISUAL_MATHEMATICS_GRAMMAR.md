# Visual Mathematics Grammar

The user explicitly requested that the GitHub portfolio demonstrate technical skill through **mathematics art, programming and scientific visuals more than text**.

This file freezes the cross-repository visual language adopted in the conversation.

## 1. Communication rule

Whenever a concept can be shown rigorously as one of the following, prefer the visual first:

- state-space geometry;
- vector field;
- phase portrait;
- network/multilayer topology;
- uncertainty ellipse/envelope/posterior region;
- viability/reachability/capture set;
- Pareto front;
- sensitivity surface;
- stochastic trajectory/distribution;
- calibration/objective surface;
- evidence/provenance pipeline;
- validation matrix;
- system/block architecture;
- causal/decision graph where relation semantics are explicit.

Then use compact prose to state what the figure means and what it does **not** prove.

## 2. Reproducible visual medium

Preferred README visual format: **SVG**.

Why:

- vector resolution;
- version-controlled source;
- text/geometry inspectability;
- GitHub-native rendering;
- accessible `title`/`desc` support;
- deterministic regeneration possible from code;
- no need to present generated raster art as evidence.

PNG/JPG remain appropriate for actual generated data plots, photos or application screenshots when provenance is clear.

## 3. Shared geometry semantics

Use the following meanings consistently when possible:

### Nodes / circles

Represent:

- subsystem;
- state family;
- evidence object;
- mathematical domain;
- process stage.

### Directed edges

Represent a declared relation or flow.

Never use an unlabeled arrow if it could be confused with theorem implication, physical causality, data flow or mere conceptual relatedness.

### Curved trajectories

Represent:

- state evolution;
- recovery path;
- optimization path;
- stochastic realization;
- continuation/bifurcation path.

### Nested regions / ellipses

Represent only when explicitly defined:

- uncertainty region;
- posterior geometry;
- admissible set;
- viability set;
- capture/recovery set;
- confidence region.

Do not use a scientific-looking ellipse without defining its semantics.

### Dashed boundaries

Preferred meanings:

- uncertainty/provisional boundary;
- future validation region;
- approximate envelope;
- non-validated design target.

### Pareto curves/fronts

Use for multi-objective trade-offs only when the objectives are stated.

Example axes:

- cost vs resilience;
- access vs security;
- emissions vs reliability;
- model fit vs complexity.

### Heatmaps

Use for actual matrices or scalar fields:

- covariance;
- correlation;
- adjacency/coupling;
- sensitivity;
- risk/intensity surface.

### Histograms/density/envelopes

Use for uncertainty or Monte Carlo results and always state:

- sample count;
- seed policy when reproducibility matters;
- parameter distribution/model;
- whether results are synthetic or empirical.

## 4. Evidence-status visual coding

Every major visual should expose an epistemic status.

Recommended categories:

- **Established mathematics** — canonical mathematical object/method.
- **Implemented demonstrator** — executable but illustrative model.
- **Synthetic experiment** — generated test data with known truth.
- **Derived result** — computed from declared inputs.
- **Proposed research object** — thesis/concept requiring validation.
- **Design target** — engineering requirement/hypothesis.
- **Validated empirical result** — only with actual evidence chain.

Do not let color imply a stronger evidence class than the text/metadata states.

## 5. Accessibility

For SVG:

- include `role="img"`;
- include `<title>` and `<desc>`;
- use readable contrast;
- do not rely on color alone;
- keep text legible at GitHub README widths;
- minimize tiny labels;
- preserve keyboard/accessibility behavior for interactive web versions.

## 6. Profile visual system

Current central profile assets:

- `assets/math-art/research-operating-system.svg`
- `assets/math-art/evidence-maturity-map.svg`
- `assets/math-art/computational-stack.svg`

Their roles:

### Research operating system

Shows the portfolio as a coupled mathematical research process:

`physics/dynamics ↔ observation/inverse problem ↔ uncertainty ↔ viability/recovery ↔ control/optimization ↔ validation`.

### Evidence maturity map

Separates evidence-bearing implementations from prototypes/scaffolds.

It is descriptive, not a ranking or certification.

### Computational stack

Maps mathematics to numerical methods, languages/tools, verification and validation roles.

It is not a language-mastery claim.

## 7. Repository-specific visuals

### `dossiya-se.github.io`

Visual theme:

- P–W–T–SW coupled dynamics;
- synthetic observation/inverse geometry;
- seeded UQ;
- viability region;
- runtime verification.

### `MSE-thesis`

Master architecture should visually separate:

- observations;
- inferred interfaces/parameters;
- dynamic P–W–T–SW model;
- admissibility;
- viability;
- recovery/capture;
- uncertainty;
- control/design;
- falsifiable research questions.

### `africa-energy-dignity`

Visual theme:

`geospatial evidence → energy balance/system model → resilience/service → Pareto trade space → engineering/deployment validation`.

### `infrastructure-interface-resilience-review`

Visual theme:

- interface as stateful object, not just an edge;
- topology uncertainty;
- response/cascade timing;
- controllability;
- intervention/hardening split;
- evidence-to-decision pipeline.

### `responsible-gold-access-network-rgan`

Visual theme:

- Miner → GO → HUB → STATION topology;
- mass/quality measurement uncertainty;
- transparent value equation;
- custody/security risk;
- access/security/cost trade-offs;
- hybrid energy/service constraints.

### Quantitative-finance lab

Visual theme:

- stochastic differential equations;
- Fourier vs Monte Carlo pathways;
- calibration surface;
- CIR/term-structure evolution;
- numerical/model-risk validation.

### Econometrics repository

Visual theme:

- omitted-variable bias geometry;
- leverage/outlier influence;
- model-selection trade-off;
- unit-root/stationarity behavior;
- structural breaks.

### Python EDA repository

Visual theme:

- feature-space geometry;
- covariance/correlation matrices;
- pairwise diagnostics;
- actual committed heatmaps/pairplot;
- source-reproducibility boundary.

### Solar + STEM

Visual theme:

- PV/storage energy balance;
- learning-system state concept;
- product-to-outcome validation chain;
- causal-evidence boundary.

### Data Science / ML

Visual theme:

`provenance → split → preprocessing → baseline/model → metric uncertainty → diagnostics → bounded claim`.

### Chatbot

Visual theme:

- UI/session/API/streaming architecture;
- generic autoregressive probability factorization;
- integration vs model-training boundary.

### Kudos IA

Visual theme:

- official scholarship source/provenance;
- applicant feature vector;
- transparent score/uncertainty;
- fairness/calibration checks;
- human review;
- outcome validation.

## 8. Mathematics-art should demonstrate programming skill

Where practical, preserve or add a deterministic generator:

```text
source data / equations
→ code
→ SVG/PNG
→ verification/checksum
→ README inclusion
```

Strong future examples:

- Python/Matplotlib/SymPy generated SVG;
- Julia numerical geometry;
- D3 interactive graph from typed JSON;
- WebGL shader field visualization;
- graph layout generated from MSC/SKOS data;
- Wolfram symbolic/geometry validation where justified;
- automated CI ensuring expected visual assets exist and source compiles.

Do not add languages only to manipulate GitHub language statistics.

## 9. Text-density rule

The README should not become unreadable in the opposite direction.

Use text for:

- definitions;
- evidence boundaries;
- limitations;
- reproducibility commands;
- provenance;
- interpretation.

Use visuals for:

- architecture;
- relationships;
- equations with geometry;
- uncertainty;
- trade-offs;
- dynamics;
- validation flow.

The target is **visual mathematical evidence**, not decorative minimalism.
