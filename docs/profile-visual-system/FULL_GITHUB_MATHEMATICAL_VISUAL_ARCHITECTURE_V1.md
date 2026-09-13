# Full GitHub Mathematical–Scientific Visual Architecture — V1

**Architecture ID:** `FGMVS-V1.0`  
**Status:** `FROZEN_ARCHITECTURE`  
**Account:** `Dossiya-SE`  
**Primary publication surface:** `Dossiya-SE/Dossiya-SE` profile README  
**Secondary interactive surface:** `dossiya-se.github.io`  
**Effective base:** audit `FGMVS-AUDIT-2026-08-25-V1`  
**Build rule:** architecture first; each visual is then specified → mathematized → computed → verified → rendered → audited → exported → frozen.

---

## 1. Governing objective

The GitHub profile is not treated as a collection of independent graphics. It is treated as a governed mathematical–scientific identity system:

```math
\mathcal P=(\mathcal V,\mathcal E,\mathcal M,\mathcal R,\mathcal S)
```

where:

- `V` = visual objects and visual families;
- `E` = semantic, dependency, provenance, or justified causal relations;
- `M` = mathematical objects, equations, constraints, fields, graphs, sets, and trajectories;
- `R` = research domains and programmes;
- `S` = publication surfaces and renderer states.

The profile knowledge chain is:

```text
research interests
→ mathematical foundations
→ computational methods
→ engineering/research systems
→ evidence and scientific status
→ software / repositories
→ applications
→ reproducibility artifacts
```

No visual may imply that all of these layers form one empirically validated universal model.

---

## 2. Non-compensatory visual-scientific rule

For every public claim `C`:

```math
L(C)\le\min_{k\in\mathcal R(C)}L_k.
```

Consequences for the visual system:

```text
visual fidelity cannot compensate for incorrect mathematics
mathematical elegance cannot compensate for missing evidence
verification cannot substitute for validation
calibration cannot substitute for validation
simulation cannot become observation
software breadth cannot become proficiency evidence
industrial relevance cannot establish novelty
```

A visual can be aesthetically excellent while remaining conceptual or illustrative.

---

## 3. Two orthogonal scientific-status systems

The new visual system SHALL retain two separate status dimensions.

### 3.1 Evidence state

```text
[S] source-grounded
[D] derived
[M] model
[C] computed
[V] verified
[E] empirical
[H] hypothesis
[T] target
```

### 3.2 Object provenance class

```text
USER_SPECIFIED
OBSERVED
PUBLISHED
COMPUTED
CALIBRATED
DERIVED
ASSUMED
SYNTHETIC
ILLUSTRATIVE
TO_BE_VALIDATED
```

They SHALL be stored separately:

```json
{
  "object_id": "research.validation.comparison",
  "evidence_state": "V",
  "provenance_class": "COMPUTED"
}
```

No build step may silently promote either field.

---

## 4. Frozen global visual grammar

| Visual element | Frozen semantic meaning |
|---|---|
| node | research object, mathematical object, repository, state, or explicitly typed entity |
| arrow | information dependency, transformation, or scientifically justified coupling |
| curve `γ(t)` | trajectory, evolution, recovery, control, optimization path, or system flow |
| surface / manifold `M` | model/admissible state space only when defined |
| boundary `∂Ω` | constraint, viability boundary, validity boundary, or domain boundary |
| vector | direction, gradient, control, flux, sensitivity, or influence |
| vector length | influence/sensitivity magnitude only when quantified |
| tube width | uncertainty magnitude only when quantified/defined |
| density | evidence strength only when defined |
| curvature | mathematically defined curvature only |
| convergence motif | verification |
| optimization path | calibration/optimization |
| model–observation pair | validation |
| closed region | admissible, viable, or bounded conclusion set |
| faded/broken region | unsupported, invalid, infeasible, or outside applicability |

No glow, particle field, manifold, curve, gradient, or equation may be added without a declared role.

---

## 5. Frozen semantic color ontology

The profile SHALL converge on the semantic ontology already reflected in the strongest V6 visual and Adaptive Visual System V4.

| Scientific role | Light | Dark | Secondary cue |
|---|---:|---:|---|
| source mathematics / theorem | `#4338CA` | `#A5B4FC` | square / indigo rule |
| observed / official evidence | `#0369A1` | `#38BDF8` | solid marker |
| state / dynamics | `#1D4ED8` | `#60A5FA` | solid trajectory |
| interface / coupling | `#7E22CE` | `#C084FC` | linked-node / coupling cue |
| hazard / violation | `#B91C1C` | `#FB7185` | dashed red boundary |
| uncertainty / inference | `#B45309` | `#FBBF24` | band / dotted contour |
| viability / admissibility | `#047857` | `#34D399` | closed green set |
| recovery / control | `#0F766E` | `#5EEAD4` | directed teal path |
| optimization / decision | `#A16207` | `#FACC15` | frontier / decision marker |
| computed / simulation | `#475569` | `#CBD5E1` | numeric/code cue |
| hypothesis / unvalidated transfer | `#BE185D` | `#F472B6` | dashed magenta |

Color SHALL never be the only carrier of meaning.

---

## 6. Frozen typography and GitHub surface rules

### 6.1 Canonical GitHub master

Every profile-facing figure SHALL have one adaptive SVG as the canonical GitHub master.

Required:

```text
viewBox
<title>
<desc>
responsive geometry
system-safe font stack
light/dark token system
no external scripts
no foreignObject dependency
no clipped labels/equations
```

### 6.2 Font strategy

Use system/fallback families only in public SVG:

```text
text: Inter, Segoe UI, Arial, sans-serif
math: STIX Two Math, Cambria Math, Georgia, serif
```

Do not package or distribute font files.

### 6.3 Readability targets

Every profile visual SHALL be tested at approximately:

```text
1440 px desktop
768 px compact/tablet
390 px mobile
```

A figure that only works as a giant poster is not a GitHub-profile pass.

### 6.4 Canonical render profiles

```text
github_adaptive
publication_white
presentation_light
presentation_dark
journal_vector
web_interactive (only where interaction has scientific meaning)
```

Geometry, equations, labels, values, topology, and evidence state must remain invariant between style profiles.

---

## 7. Stable object-ID namespace

Every major object SHALL have a stable semantic ID.

### 7.1 Profile

```text
profile.header.geometry
profile.header.network
profile.header.trajectory
profile.header.uncertainty
profile.header.title
profile.header.subtitle
```

### 7.2 Professional trajectory

```text
trajectory.engineering
trajectory.energy
trajectory.sustainable_engineering
trajectory.financial_engineering
trajectory.mathematics
trajectory.resilience
trajectory.transition.*
```

### 7.3 Mathematics universe

```text
math.foundation.analysis
math.foundation.linear_algebra
math.probability
math.statistics
math.ode_pde
math.numerical_analysis
math.graph_theory
math.dynamical_systems
math.control
math.differential_geometry
math.topology
math.optimization
math.uq
math.stochastic_modeling
```

### 7.4 Research system

```text
research.problem
research.evidence
research.gaps
research.question
research.contribution
research.system
research.formulation
research.provenance
research.computation
research.verification
research.calibration
research.validation
research.sensitivity
research.uncertainty
research.comparison
research.results
research.interpretation
research.industrial_implication
research.limitations
research.conclusion
research.reproducibility
```

### 7.5 Differential geometry

```text
math.diffgeom.surface
math.diffgeom.tangent_u
math.diffgeom.tangent_v
math.diffgeom.normal
math.diffgeom.metric
math.diffgeom.gaussian_curvature
math.diffgeom.mean_curvature
math.diffgeom.geodesic
math.diffgeom.transfer_boundary
```

### 7.6 Repository system

```text
repo.frontdoor.*
repo.research.*
repo.method.*
repo.prototype.*
repo.learning.*
repo.edge.*
```

The ID namespace is a release invariant. A later command such as `change only research.validation` SHALL be implementable without mutating unrelated IDs.

---

## 8. Exact frozen figure list

The core profile system SHALL contain exactly ten primary visual families plus one retained specialist visual.

| ID | Canonical family | Current state | Frozen disposition | Primary purpose |
|---|---|---|---|---|
| `FGMVS-00` | Master Profile Header | existing V5 | **REBUILD** | Compress the profile's mathematical identity into one minimal, meaningful hero using verified/declared primitives rather than decorative tech imagery. |
| `FGMVS-01` | Professional Research-State Trajectory | existing V5 | **REBUILD** | Express progression from engineering to deeper mathematics/research as a state-transition architecture, not a generic timeline. |
| `FGMVS-02` | Mathematics Universe / Dependency Graph | existing V5 | **REBUILD** | Show mathematically defensible dependencies among core mathematical domains without implying mastery ranking. |
| `FGMVS-03` | Differential Geometry Foundations | existing V5 | **REBUILD FROM VERIFIED GEOMETRY** | Generate surface, tangents, normal, metric, curvature, and geodesic from code; preserve transfer boundary to engineering applications. |
| `FGMVS-04` | Scientific Research Operating System | existing V5 | **REBUILD — SIGNATURE VISUAL** | Encode the complete governing research architecture from real problem to reproducibility and bounded conclusion. |
| `FGMVS-05` | Evidence Maturity / Scientific Rigor Architecture | existing V5 | **REBUILD DATA LAYER** | Separate implementation maturity, validation maturity, evidence state, and provenance without numeric quality ranking. |
| `FGMVS-06` | Computational Mathematics Stack | existing V5 | **REBUILD AS ROLE GRAPH** | Map software to explicit symbolic, numerical, geometry, visualization, animation, rendering, web, testing, and reproducibility roles. |
| `FGMVS-07` | Formula–Evidence–Claim Lattice | existing V5 | **IMPROVE / ONTOLOGY RECONCILE** | Show that formulas, models, computations, verification, evidence, and claims are different objects with bounded transitions. |
| `FGMVS-08` | Coupled Infrastructure Resilience Mathematical System | new | **BUILD NEW** | Public high-level model of P–W/D–T–SW coupling, interfaces, forcing, control, service, recovery, uncertainty, and validity boundary without fabricating data. |
| `FGMVS-09` | Repository Navigation Knowledge Graph | new | **BUILD NEW** | Map all 16 repositories into front doors, flagship research, methods/tools, prototypes, and learning/archive roles with navigation value. |
| `FGMVS-S01` | Optimization · Uncertainty · Bounded Decision | existing V6 | **KEEP / AUDIT / MINOR HARMONIZATION** | Preserve the strongest current specialist figure and harmonize global IDs/palette/manifest only where required. |

No additional primary visual may be added to the README until these families are frozen or an explicit architecture revision is approved.

---

## 9. Mathematical object inventory by figure

### FGMVS-00 — Master Profile Header

The header SHALL NOT pretend that all displayed primitives belong to one physical model. It is a mathematical identity atlas composed of separately typed objects:

```math
\mathbf r(u,v)\quad\text{(geometry)}
```

```math
L=D-A\quad\text{(network structure)}
```

```math
\dot{\mathbf x}=f(\mathbf x,\mathbf u,\boldsymbol\eta,\boldsymbol\theta,t)\quad\text{(dynamics)}
```

```math
(x-\mu)^\top\Sigma^{-1}(x-\mu)\le c\quad\text{(uncertainty/admissible ellipse)}
```

The composition is conceptual; object equations remain individually valid/declared.

### FGMVS-01 — Professional Research-State Trajectory

Use categorical research states and typed transitions rather than fabricated skill scores:

```text
Engineering
→ Energy Systems
→ Sustainable Engineering
→ Financial Engineering / stochastic modeling
→ Deeper Mathematics
→ Sustainable Resilience Research
```

Represent as a state-transition graph or trajectory through typed domains. Numeric coordinates, if used for layout, are `ILLUSTRATIVE` and SHALL NOT be labeled as measured proficiency.

### FGMVS-02 — Mathematics Universe

Define a dependency graph:

```math
\mathcal G_M=(V_M,E_M)
```

with edges only where a defensible mathematical/prerequisite relation is declared. Core nodes:

```text
analysis/calculus
linear algebra
tensor algebra
probability
statistics
ODE/PDE
numerical analysis
graph theory
dynamical systems
control
optimization
differential geometry
topology where relevant
stochastic modeling
uncertainty quantification
```

No node size or radial distance may imply mastery unless a separate evidence basis is defined.

### FGMVS-03 — Differential Geometry

For a parameterized surface:

```math
\mathbf X(u,v)
```

compute:

```math
\mathbf X_u,\quad \mathbf X_v
```

```math
E=\mathbf X_u\cdot\mathbf X_u,\quad
F=\mathbf X_u\cdot\mathbf X_v,\quad
G=\mathbf X_v\cdot\mathbf X_v
```

```math
\mathbf N=\frac{\mathbf X_u\times\mathbf X_v}{\|\mathbf X_u\times\mathbf X_v\|}
```

and, where shown:

```math
K,\quad H,\quad \nabla K,\quad \gamma(s).
```

The geodesic must satisfy the declared geodesic equations to tolerance if labeled as a geodesic.

### FGMVS-04 — Scientific Research Operating System

Frozen chain:

```text
Real Problem
→ Evidence
→ Gap Architecture
→ Research Question
→ Contribution Class
→ System Definition
→ Mathematical/Statistical Formulation
→ Data/Parameter Provenance
→ Analytical/Numerical Method
→ Verification
→ Calibration if applicable
→ Validation
→ Sensitivity
→ Uncertainty
→ Baseline Comparison
→ Results
→ Scientific Interpretation
→ Industrial/Practical Implication if claimed
→ Limitations
→ Bounded Conclusion
→ Reproducibility Package
```

Core objects may include:

```math
E(\mathbf z)=\sum_iE_i\phi_i(\mathbf z)
```

```math
\mathbf G=(g_1,\dots,g_m)^\top
```

```math
\dot{\mathbf x}=f(\mathbf x,\mathbf u,\boldsymbol\eta,\boldsymbol\theta,t)
```

```math
\widehat\theta=\arg\min_\theta J(\theta)
```

```math
D=d(y_{\mathrm{model}},y_{\mathrm{obs}})
```

```math
\mathcal C_{\mathrm{admissible}}
```

and the non-compensatory claim rule.

### FGMVS-05 — Evidence Maturity

Use separate dimensions, not a single score:

```text
implementation maturity
validation maturity
evidence state
provenance class
```

A repository point may be plotted only from a frozen account registry. Ordinal categories SHALL NOT be transformed into a fake 0–100 quality score.

### FGMVS-06 — Computational Stack

Define tool-role graph:

```math
\mathcal G_C=(V_C,E_C)
```

Role clusters:

```text
symbolic mathematics
numerical mathematics
scientific computation
geometry/manifolds
visualization
animation
rendering
web interaction
formal/software verification
reproducibility/publication
```

Tools are nodes because of declared implementation roles, not because repository presence proves proficiency.

### FGMVS-07 — Formula–Evidence–Claim Lattice

Frozen semantic chain:

```text
question
→ assumptions
→ formula/model
→ data/parameters
→ computation
→ verification
→ calibration if required
→ validation
→ result
→ bounded claim
```

Required visual assertions:

```text
formula != evidence
simulation != observation
verification != validation
model output != scientific interpretation
```

### FGMVS-08 — Coupled Infrastructure Resilience

Public conceptual/model architecture only unless public evidence supports promotion.

System graph:

```math
\mathcal G_I=(V_I,E_I)
```

with sectors:

```text
Power
Water/Drainage
Transportation
Solid Waste
```

Generic dynamics:

```math
\dot{\mathbf x}=f(\mathbf x,\mathbf u,\boldsymbol\eta,\boldsymbol\theta,t)
```

The figure may show interfaces, hazards/forcing, controls, service outputs, recovery, uncertainty, viability/admissibility, and population/service mapping only if each mapping is defined. Differential-geometric language remains `HYPOTHESIS/TRANSFER` unless a state-space geometry is formally specified.

### FGMVS-09 — Repository Navigation

Define account graph:

```math
\mathcal G_R=(V_R,E_R)
```

Layers:

```text
Layer 0 — front doors
Layer 1 — flagship research laboratories
Layer 2 — reusable methods/meta-platforms
Layer 3 — applied prototypes
Layer 4 — learning/bounded archives
```

Edges encode navigation/dependency/role relationships, not scientific quality.

---

## 10. Rendering technology freeze

| Figure | Mathematical/source layer | Canonical rendering | Optional enhancement | Promotion target |
|---|---|---|---|---|
| FGMVS-00 Header | NumPy/SymPy generated primitives + repository identity specification | adaptive SVG | bounded Manim/portfolio-site motion | P2/P3 for primitives; header composition conceptual |
| FGMVS-01 Trajectory | structured state-transition registry | SVG + deterministic graph layout | Manim chronological reveal | P1/P2 descriptive |
| FGMVS-02 Mathematics Universe | NetworkX/structured dependency graph | SVG | D3/Three.js on portfolio site | P2 declared mapping |
| FGMVS-03 Differential Geometry | SymPy + NumPy/SciPy + geometry engine | SVG/vector projection; PyVista for QA | Manim/PyVista/Blender/Three.js downstream | **P3 required** |
| FGMVS-04 Research OS | structured research architecture + equation registry | SVG | Manim process trace / web drill-down | P2/P3 structural verification |
| FGMVS-05 Evidence Maturity | account registry / evidence-state data | Matplotlib/SVG or direct SVG | source tooltips on portfolio site | P2/P3 data-consistent |
| FGMVS-06 Computational Stack | tool-role registry | NetworkX/SVG | clickable web map | P2 mapping |
| FGMVS-07 Formula Evidence Lattice | equation/provenance/evidence registries | SVG | provenance drill-down | P2/P3 semantic QA |
| FGMVS-08 Infrastructure Resilience | public model architecture only | NetworkX/NumPy/SVG | PyVista/Manim only after model gates | P1/P2 until validation supports more |
| FGMVS-09 Repository Navigation | live/frozen GitHub repository registry | NetworkX/SVG | D3 interactive portfolio map | P2 source-grounded mapping |
| FGMVS-S01 Optimization | existing SVG + verification lab | adaptive SVG | bounded interactive demos | preserve current verified semantics |

Generative-image systems may be used only for ideation/reference exploration. They SHALL NOT be the authoritative source for equations, stage numbering, labels, scientific plots, or reproducibility-critical geometry.

---

## 11. Dependency order — frozen build sequence

The hero is intentionally built last because it depends on the visual language established by the deeper figures.

```text
B00 Global contracts
  ↓
B01 equation registry + provenance/evidence schema + semantic palette + typography
  ↓
B02 Mathematics Universe
  ↓
B03 Differential Geometry Foundations
  ↓
B04 Scientific Research Operating System
  ↓
B05 Formula–Evidence–Claim Lattice
  ↓
B06 Evidence Maturity / account registry
  ↓
B07 Computational Mathematics Stack
  ↓
B08 Coupled Infrastructure Resilience System
  ↓
B09 Repository Navigation Graph
  ↓
B10 Professional Research-State Trajectory
  ↓
B11 Master Profile Header
  ↓
B12 Audit/harmonize Optimization V6
  ↓
B13 README integration
  ↓
B14 source-only reproduction + final profile release candidate
```

No downstream visual may redefine a frozen upstream semantic token without architecture versioning.

---

## 12. Figure-level build contract

For every primary visual:

```text
SPECIFY
→ MATHEMATIZE
→ CLASSIFY EVIDENCE/PROVENANCE
→ COMPUTE
→ VERIFY
→ RENDER
→ VISUAL AUDIT
→ GITHUB COMPATIBILITY AUDIT
→ EXPORT EDITABLE MASTER
→ REPRODUCE FROM SOURCE
→ FREEZE
```

Each figure release SHALL include, where applicable:

```text
<visual>_EDITABLE.svg
<visual>_EDITABLE.pptx
<visual>.png
<visual>.pdf
render_request.yaml
equations.tex
research_data.json
manifest.json
qa_report.json
SOURCE_BUNDLE.zip
```

For reference-preserving migrations additionally:

```text
reference_layout.json
change_log.json
reference_overlay.png
visual_diff.png
fidelity_report.json
```

SVG remains the canonical visual authority.

---

## 13. QA test plan — frozen

### 13.1 Scientific QA

- every visual assertion has an evidence/provenance classification;
- no source theorem is presented as original contribution;
- no model/simulation is presented as observation;
- no unvalidated geometry transfer is presented as established application geometry;
- claim strength obeys the non-compensatory rule.

### 13.2 Mathematical QA

- canonical equations originate from `equations.tex` / formula registry;
- symbol definitions and units are recorded where applicable;
- symbolic checks are run where feasible;
- numerical invariants are tested where applicable;
- differential-geometry surface/tangent/normal/metric/curvature tests pass before promotion;
- optimization figures retain feasibility/optimality/uncertainty/validation distinctions.

### 13.3 Visual-semantic QA

- stable IDs present;
- every color follows semantic ontology;
- meaning reinforced by shape/line/label;
- no decorative formula without role;
- no decorative geometry mislabeled as computed geometry;
- no clipped text/equations;
- no unsupported visual metaphor.

### 13.4 GitHub compatibility QA

- valid script-free SVG;
- responsive `viewBox`;
- `<title>` and `<desc>`;
- tested at 1440/768/390 px widths;
- acceptable contrast in light and dark modes;
- no reliance on CSS inversion;
- no external font dependency;
- no broken relative paths.

### 13.5 Editability QA

- canonical SVG has logical groups and stable IDs;
- text remains text where practical;
- equations retain editable LaTeX source even if path-converted for publication;
- raster layers are declared and regenerable;
- PPTX derivative exists for accepted final visuals.

### 13.6 Provenance QA

- source/data/config hashes recorded;
- renderer/tool versions recorded;
- random seeds recorded if relevant;
- camera/view configuration recorded for rasterized 3-D layers;
- generated assets linked to source generators.

### 13.7 Reproduction QA

The accepted release SHALL be regenerated from the frozen source bundle in a clean path/environment without using the accepted final raster/vector output as an input shortcut.

For deterministic artifacts:

```text
expected hash == regenerated hash
```

Where rendering has unavoidable nondeterminism, a declared tolerance and perceptual/layout metric SHALL replace exact-hash equality.

### 13.8 Reference-fidelity QA

For `REFERENCE_PLUS_CORRECTIONS` or `STRICT_REFERENCE` migrations:

```text
reference layout
+ overlay
+ visual diff
+ object presence
+ stage order
+ text/equation presence
+ bounding-box displacement
+ SSIM/RMSE where meaningful
```

No unmeasured `100% fidelity` claim is allowed.

---

## 14. README publication architecture

The profile README SHALL become more concise, not larger.

Recommended visible hierarchy:

```text
1. Master header
2. concise identity + evidence invariant
3. research programmes
4. professional research-state trajectory
5. mathematics universe
6. research operating system
7. differential geometry / mathematical art
8. computational stack
9. evidence + formula/claim lattice
10. repository navigation
11. selected repository table
12. education / profile governance
```

Secondary figures such as the evidence maturity map and detailed optimization architecture may remain under `<details>` or move to the interactive portfolio when their full-width presence would create profile overload.

The profile README is the concise front door; `dossiya-se.github.io` is the interactive visual laboratory.

---

## 15. Repository-role architecture for FGMVS-09

The source account contains 16 repositories in the current account audit. The navigation visual SHALL use role layers rather than a quality ranking.

```text
Layer 0 — FRONT DOORS
Dossiya-SE
dossiya-se.github.io

Layer 1 — FLAGSHIP RESEARCH / ACADEMIC LABS
MSE-thesis
infrastructure-interface-resilience-review
Dossiya-SE-mscfe-quantitative-finance-lab
africa-energy-dignity
Differential-geometry-and-Mathematics-arts-for-sustainability-and-resilience
responsible-gold-access-network-rgan

Layer 2 — METHODS / META / SPECIALIST TOOLS
Dossiya-SE-Dossiya-SE
Math-Surface-Engineer-Demo
polyglot-resilience (currently subsystem in profile repository; future extraction only if separately approved)

Layer 3 — APPLIED PROTOTYPES
Kudo-IA
testasu

Layer 4 — LEARNING / BOUNDED ARCHIVES
dossiyadakou-mac-project
Python-for-rapid-engineering-solution
Data-Science-an-Machine-Learning
chatbot
```

Private repository nodes may show only role metadata already publicly declared by the profile; no private implementation detail is permitted.

---

## 16. Version and archive policy

After a successor family passes all gates:

```text
current canonical master
→ remains in assets/math-art/

superseded generations
→ assets/math-art/archive/<family>/
```

Do not delete provenance history. Do not keep multiple ambiguous current masters.

Naming pattern:

```text
<family>-v7.svg
<family>-v7.manifest.json
<family>-v7.qa.json
```

The first full-system successor generation is designated **V7** because the profile already contains V6 rendering architecture/specialist assets. The system architecture itself remains `FGMVS-V1.0`.

---

## 17. Freeze decision

The following are now frozen for the build phase:

```text
10 primary visual families
1 retained specialist visual
semantic visual grammar
semantic color ontology
stable object-ID namespaces
two-dimensional evidence/provenance status model
canonical adaptive SVG policy
editable artifact policy
build dependency order
QA/reproduction gates
README publication hierarchy
archive/version policy
```

Changes to any of these require a versioned architecture amendment.

**Architecture gate:** `FROZEN_ARCHITECTURE_V1_PASS`  
**Next gate:** `B00_GLOBAL_CONTRACTS_AND_REGISTRIES`  
**Rendering of profile visuals:** may begin only after B00/B01 source registries are created and pass their static checks.
