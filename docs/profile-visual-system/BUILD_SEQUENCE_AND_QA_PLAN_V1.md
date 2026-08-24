# Full GitHub Mathematical Visual System — Build Sequence and QA Plan V1

**Plan ID:** `FGMVS-BUILD-V1.0`  
**Depends on:** `FGMVS-V1.0` architecture freeze  
**Status:** `FROZEN_BUILD_ORDER`  
**Current gate:** `B00_GLOBAL_CONTRACTS_AND_REGISTRIES`

## 1. Why the hero is not built first

The profile header is the most visible artifact, but it depends on the semantic grammar, mathematical primitives, repository taxonomy, and research-system architecture established by deeper figures. Building it first would encourage decoration before meaning.

Therefore the build order is intentionally dependency-driven rather than visibility-driven.

## 2. B00 — global contracts

Before any new profile visual is rendered, create/freeze:

```text
visual-system/spec/visual_grammar.yaml
visual-system/spec/semantic_palette.yaml
visual-system/spec/typography.yaml
visual-system/spec/object_id_schema.yaml
visual-system/spec/render_profiles.yaml
visual-system/spec/editability_contract.yaml
```

Acceptance:

```text
schema parse = PASS
no duplicate semantic object IDs = PASS
all palette roles have light/dark values = PASS
all palette roles have non-color secondary cues = PASS
all public SVG font families are system-safe = PASS
```

## 3. B01 — registries and canonical sources

Create/freeze:

```text
visual-system/equations/equations.tex
visual-system/data/repository_registry.json
visual-system/data/tool_role_registry.json
visual-system/data/research_object_registry.json
visual-system/data/evidence_registry.json
visual-system/data/public_infrastructure_model.json
```

Each scientific object record should include, as applicable:

```json
{
  "object_id": "research.validation.comparison",
  "evidence_state": "V",
  "provenance_class": "COMPUTED",
  "source": "...",
  "equation_ids": ["EQ-VAL-001"],
  "data_ids": ["DATA-VAL-001"],
  "generator": "...",
  "promotion_level": "P2"
}
```

Acceptance:

```text
all IDs unique = PASS
all visual scientific objects have provenance class = PASS
all evidence-bearing objects have evidence state = PASS
all equation IDs resolve to equations.tex = PASS
all repository nodes resolve to the frozen repository registry = PASS
no private implementation detail exposed by public registry = PASS
```

## 4. Figure build order

### Stage 1 — FGMVS-02 Mathematics Universe

**Why first:** defines the dependency-graph visual language for the rest of the system.

Build target:

```math
\mathcal G_M=(V_M,E_M)
```

Required nodes include analysis/calculus, linear algebra, tensor algebra, probability, statistics, ODE/PDE, numerical analysis, graph theory, dynamical systems, control, optimization, differential geometry, topology where relevant, stochastic modeling, and UQ.

Pass gates:

```text
no mastery-score encoding
all edges have declared relation type
all labels readable at 768 px
390 px mobile fallback/crop strategy verified
adaptive light/dark invariant check
source-only reproduction
```

### Stage 2 — FGMVS-03 Differential Geometry Foundations

**Why second:** establishes the strongest genuine mathematics-generated visual primitive.

Compute:

```math
\mathbf X(u,v),\;\mathbf X_u,\;\mathbf X_v,\;g_{ij},\;\mathbf N,\;K,\;H
```

where shown.

Pass gates:

```text
||N|| = 1 within tolerance
N·X_u = 0 within tolerance
N·X_v = 0 within tolerance
g_ij symmetric
det(g) > 0 on admissible sampled domain
analytic derivatives vs finite-difference parity
geodesic residual within declared tolerance if geodesic shown
renderer uses verified geometry data, not hand-drawn substitute
```

Target promotion: `P3`.

### Stage 3 — FGMVS-04 Scientific Research Operating System

**Why third:** becomes the governing research signature visual.

Must include the full frozen chain:

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

Pass gates:

```text
stage completeness
stage order
verification/calibration/validation non-equivalence
bounded-claim rule visible
no invented numerical evidence
mobile hierarchy test
```

### Stage 4 — FGMVS-07 Formula–Evidence–Claim Lattice

Resolve the two status ontologies without collapsing them.

Pass gates:

```text
formula != evidence
simulation != observation
verification != validation
provenance_class separate from evidence_state
claim bound represented explicitly
```

### Stage 5 — FGMVS-05 Evidence Maturity

Data source must be the frozen repository registry.

No arbitrary numeric ranking.

Pass gates:

```text
implementation and validation maturity remain separate
ordinal labels retained
no 0–100 quality score
repository placements trace to registry
private-repository detail remains bounded
```

### Stage 6 — FGMVS-06 Computational Mathematics Stack

Build a role graph rather than a logo wall.

Required role clusters:

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

Pass gates:

```text
every tool has declared role
software presence != proficiency claim
no decorative logo dependence
role edges resolve to tool registry
```

### Stage 7 — FGMVS-08 Coupled Infrastructure Resilience System

Public architecture only.

Core sectors:

```text
Power
Water/Drainage
Transportation
Solid Waste
```

Generic model form:

```math
\dot{\mathbf x}=f(\mathbf x,\mathbf u,\boldsymbol\eta,\boldsymbol\theta,t)
```

Pass gates:

```text
all public couplings defined
no fabricated quantitative values
hazard/control/state/interface semantics distinct
service/population mapping labeled if used
no differential-geometric claim without formal state geometry
model status visibly bounded
```

### Stage 8 — FGMVS-09 Repository Navigation Graph

All 16 account repositories must resolve to the frozen repository registry.

Pass gates:

```text
all 16 accounted for
no duplicate role authority
front-door distinction retained
private repositories reveal only already-public role metadata
edges encode navigation/dependency, not quality ranking
all public links valid
```

### Stage 9 — FGMVS-01 Professional Research-State Trajectory

Use typed state transitions, not fabricated skill coordinates.

Pass gates:

```text
chronology/role provenance explicit
no numeric proficiency scale
no domain equation presented as evidence of achievement
future research direction visually distinguished from completed work
```

### Stage 10 — FGMVS-00 Master Header

Built after upstream figures pass.

The hero may combine verified/declared primitives from:

```text
geometry
network structure
dynamics
uncertainty
resilience/recovery
```

but must not imply they form one validated universal model.

Pass gates:

```text
true editable/adaptive SVG
no unexplained embedded raster
minimal text
recognizable at README width
works without reading small labels
light/dark theme invariant
source-only reproduction
```

### Stage 11 — FGMVS-S01 Optimization V6 harmonization

Do not redesign unless QA identifies a real defect.

Allowed changes:

```text
stable object IDs
manifest/source packaging
semantic-token harmonization
accessibility corrections
```

Disallowed without architecture amendment:

```text
collapse deterministic/Bayesian rails
remove validation boundary
change scientific meaning for visual uniformity
```

## 5. Figure release package

Every accepted final figure SHALL export:

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

Reference migrations additionally export:

```text
reference_layout.json
change_log.json
reference_overlay.png
visual_diff.png
fidelity_report.json
```

## 6. QA severity model

```text
BLOCKING
HIGH
MEDIUM
LOW
INFORMATIONAL
```

Any `BLOCKING` issue prevents `RENDER_PASS`.

Examples of blocking conditions:

```text
incorrect equation
unresolved source/provenance
scientific object mislabeled as observed/validated
missing canonical SVG
missing source bundle
reproduction failure
broken GitHub render
unreadable critical label at target width
unexplained raster scientific layer
```

## 7. RENDER_PASS definition

For a visual `F`:

```math
G_{\mathrm{render}}(F)=
G_{\mathrm{science}}
\land G_{\mathrm{math}}
\land G_{\mathrm{visual}}
\land G_{\mathrm{github}}
\land G_{\mathrm{editability}}
\land G_{\mathrm{provenance}}
\land G_{\mathrm{reproduction}}.
```

Only if all required gates are true:

```text
RENDER_PASS
```

Otherwise:

```text
RENDER_FAIL
```

Warnings cannot be silently converted into pass when they affect a required gate.

## 8. README integration gate

No individual new visual becomes profile-facing merely because it passes its own figure tests.

README integration requires:

```text
all primary figures intended for visible placement frozen
profile hierarchy frozen
mobile density reviewed
relative paths verified
GitHub light/dark rendering reviewed
redundant predecessor references removed or archived
selected specialist visuals placed under details where appropriate
```

## 9. Final release gate

The final profile release candidate requires:

```text
full README render
all links verified
all canonical SVGs verified
all mathematical QA complete
all visual-regression gates complete
source-only reproduction complete
account/profile manifest generated
no automatic merge
```

**Current state:** `ARCHITECTURE_FROZEN — BUILD NOT STARTED`  
**Next executable action:** implement `B00` and `B01`; only then begin `FGMVS-02`.
