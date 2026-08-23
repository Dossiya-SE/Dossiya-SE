# NUS-48 — Next Scientific Adjudication Work

The preprocessing-engineering phase is frozen at V8 `58/58 PASS`. The next work is scientific adjudication, not another preprocessing redesign.

## Workstream 1 — Claim adjudication

For every scientifically relevant candidate, adjudicate strictly in this order:

```text
WritingMode
→ ClaimOwner
→ Focality
→ CitationScope
→ EvidenceEligibility
→ Role
→ Ontology
```

Do not allow role assignment to override unresolved ownership/focality/citation scope.

## Workstream 2 — Abstract-body adjudication

All **11 abstract claims** must receive exactly one state:

```text
BODY_CONFIRMED
BODY_MORE_SPECIFIC
ABSTRACT_ONLY
BODY_CONTRADICTS
NONCOMPARABLE
UNRESOLVED
```

Abstract values should not become final annotations solely because they passed preprocessing; use the strongest nonredundant body evidence when available.

## Workstream 3 — Physical-surface adjudication

All **34 physical objects** must be dispositioned:

```text
Tables 1–8
Figures 1–19
Equations 1–7
```

Allowed dispositions:

```text
INCLUDE
EXCLUDE
REDUNDANT
ABSTAIN
```

Each object requires a scientific reason.

## Workstream 4 — Evidence architecture

Build explicit lineage:

```text
EvidenceAnchor
→ Observation
→ Transformation
```

and reconstruct:

```text
Q → I → M_E → P → F → M_S → S → D
```

Do not infer `P → S` from co-occurrence.

## Workstream 5 — Transformation ledger

### Eq. 1 — embodied carbon

Target architecture:

```text
material quantities + embodied-carbon factors
→ sum-product environmental transformation
→ embodied carbon
```

Likely input provenance includes focal-adopted (`FA`) embodied-carbon factors and focal mixture quantities. Final provenance propagation must be explicitly adjudicated.

Initial link status:

```text
PARALLEL_ONLY
```

unless an engineering output is proven to enter the transformation.

### Eq. 2 — eco-strength efficiency

Target architecture:

```text
28-day compressive strength + embodied carbon
→ ratio/coupling transformation
→ eco-strength efficiency
```

Initial link status:

```text
COUPLED
```

because engineering performance participates directly.

Exact focal-PDF displayed equation requires visual verification before any exact-formula/geometry claim.

### Eq. 3 — cost

Target architecture:

```text
material quantities + unit material costs
→ sum-product economic transformation
→ total concrete cost
```

Initial link status:

```text
PARALLEL_ONLY
```

unless an engineering output is proven to enter the cost transformation.

## Candidate evidence already requiring body reconciliation

### Intervention/design/input

```text
CCA: 0%, 5%, 10%, 15%, 20%
JF: 0%, 0.25%, 0.50%, 0.75%, 1.0%
```

These are multifunction evidence: design choice/intervention and RSM input.

### Mechanical outputs reported in abstract

At `0.50% JF + 10% CCA` at 28 days:

```text
Flexural strength           5.3 MPa
Splitting tensile strength  3.8 MPa
Compressive strength       32.88 MPa
Modulus of elasticity      33.11 GPa
```

All require body confirmation, specificity assessment, and nonredundancy decisions.

### Sustainability

```text
Environmental: embodied carbon
Economic: material/concrete cost
Coupling metric: eco-strength efficiency
```

Do not create a false `INTEGRATED` sustainability outcome merely because environmental and economic dimensions co-occur.

### Decision

Candidate focal recommendation:

```text
10% CCA + 0.50% JF
```

Retain only after body-level decision confirmation and focality/citation-scope adjudication.

## Human approval gate

AI-assisted adjudication output must remain:

```text
NOT_HUMAN_APPROVED
```

until the user explicitly approves the scientific state.

## After human approval

Only then proceed:

```text
approved evidence
→ exact geometry
→ complete hypothetical final Zotero state Z*
→ schema validation
→ writer dry-run
→ independent auditor dry-run
→ mutation authorization check
```

No direct annotation creation is permitted before those gates pass.
