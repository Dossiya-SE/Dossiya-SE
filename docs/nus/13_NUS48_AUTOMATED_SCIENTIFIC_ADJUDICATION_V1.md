# NUS-48 Automated Scientific Adjudication V1

## Status

```text
PASS_AUTOMATED_SCIENTIFIC_ADJUDICATION_READY_FOR_HUMAN_REVIEW
```

This state is downstream of the V8 `58/58` premutation readiness freeze. It is **not human approval** and does **not authorize Zotero writing**.

## Controlled input consistency

The adjudication input is internally consistent with the frozen NUS-48 handoff:

```text
paper_id = 48
pdf_sha256 = bd27b10cb8110d7a48a0b28923e3e0cc2adc0fb2d7e416fb25714f8483db3609
premutation = 58/58 PASS
atomic claims = 426
abstract claims = 11
physical surfaces = 34
live annotations = 0
mutation authorized = false
```

## Claim adjudication totals

Every claim was passed through:

```text
WritingMode
→ ClaimOwner
→ Focality
→ CitationScope
→ EvidenceEligibility
→ Role
→ Ontology
```

Focality/ownership state:

| State | Count |
|---|---:|
| FOCAL | 289 |
| FOCAL_ADOPTED | 20 |
| EXTERNAL | 111 |
| Administrative / non-scientific | 6 |
| **Total** | **426** |

Annotation-level reduction:

| Decision | Count |
|---|---:|
| INCLUDE as text candidate | 25 claims |
| REDUNDANT / ledger-only | 229 |
| EXCLUDE | 169 |
| SPLIT_REQUIRED | 2 |
| ABSTAIN | 1 |

Two adjacent decision claims are merged into one proposed highlight, yielding **24 proposed text annotations** from the 25 included claims.

This count is evidence-derived and not a preset `N_final`.

## Abstract/body adjudication

All 11 abstract claims were resolved:

| State | Count |
|---|---:|
| BODY_CONFIRMED | 5 |
| BODY_MORE_SPECIFIC | 4 |
| BODY_CONTRADICTS | 1 |
| ABSTRACT_ONLY | 1 |
| NONCOMPARABLE | 0 |
| UNRESOLVED | 0 |

### Critical contradiction — abstract claim C0006

For `0.50% JF + 10% CCA`, the abstract reports:

```text
FS  = 5.3 MPa
STS = 3.8 MPa
CS  = 32.88 MPa
```

The body/conclusion reports:

```text
FS  = 5.60 MPa
STS = 3.50 MPa
CS  = 39.42 MPa
```

Adjudication state:

```text
BODY_CONTRADICTS
```

No averaging, plausibility selection, or silent correction is permitted.

## Preserved author inconsistencies

### IC001 — Abstract vs body mechanical values

The FS/STS/CS values above disagree.

```text
status = UNRESOLVED_AUTHOR_INCONSISTENCY
```

### IC002 — Modulus-of-elasticity composition

One body statement reports:

```text
33.11 GPa at 0.50% JF + 0% CCA
```

while another body statement/conclusion associates the same maximum with:

```text
33.11 GPa at 0.50% JF + 10% CCA
```

Both are preserved without correction.

### IC003 — R² assignment

Table 7 gives approximately:

```text
R²_CS  = 0.9913
R²_STS = 0.9699
R²_FS  = 0.9913
R²_ME  = 0.9913
```

The conclusion reports approximately:

```text
CS  = 99.13%
STS = 99%
FS  = 97%
ME  = 99%
```

The lower value appears attached to a different response in the conclusion. Both source states remain preserved.

## Optimization-scope separation

Three values must not be collapsed into one optimum:

### Local FS response-surface condition

```text
CCA = 14%
JF  = 0.70%
```

### Numerical RSM optimum

```text
CCA = 10.24%
JF  = 0.52%
```

with predicted responses approximately:

```text
CS  = 39.71
STS = 3.47
FS  = 5.64
ME  = 33.36
```

### Authors' practical recommendation

```text
CCA = 10%
JF  = 0.50%
```

Frozen interpretation:

```text
local response condition
≠ numerical RSM optimum
≠ practical recommendation
```

## Physical-surface adjudication

All 34 surfaces were scientifically dispositioned:

```text
8 tables + 19 figures + 7 equations = 34
```

| Disposition | Count |
|---|---:|
| INCLUDE | 31 |
| REDUNDANT | 3 |
| EXCLUDE | 0 |
| ABSTAIN scientifically | 0 |

Current redundant surfaces:

```text
Figure 1
Figure 18
Figure 19
```

All 8 tables remain scientifically relevant. All 7 equations remain scientifically relevant.

Scientific `INCLUDE` does not imply final Zotero geometry or exact formula text has been approved.

## Sustainability transformation ledger

### Eq. 1 — embodied carbon

Conceptual transformation:

```text
W_i × CO2_i → EC
```

Classification:

```text
link_status = PARALLEL_ONLY
ontology = ENV01
```

No engineering performance output enters Eq. 1.

### Eq. 2 — eco-strength efficiency

The focal procedure combines 28-day compressive strength with embodied carbon.

Classification:

```text
link_status = COUPLED
```

This supports a genuine `P → F → S` relationship.

But:

```text
coupled engineering + environmental metric
≠ integrated sustainability
```

Exactness remains restricted:

```text
Exists(Eq.2) = true
ExactFormula(Eq.2) = not yet verified
visual_review_required = true
```

### Eq. 3 — cost

Conceptual transformation:

```text
W_i × Cost_i → Cost_RCC
```

Classification:

```text
link_status = PARALLEL_ONLY
ontology = ECO17
```

No engineering output enters Eq. 3.

## Final scientific evidence architecture

```text
Q → I → M_E → P → F → M_S → S → D
```

with `PURPOSE` outside the chain.

Current reconstruction:

```text
Q   = limited combined JF+CCA RCC evidence/problem
I   = CCA substitution + JF reinforcement/design
M_E = mechanical testing + RSM + ANOVA
P   = CS, STS, FS, ME
F   = factor-response/correlation models
M_S = Eq. 1, Eq. 2, Eq. 3
S   = embodied carbon, ESE, cost
D   = 10% CCA + 0.50% JF practical recommendation
```

Supported sustainability dimensions:

```text
Environmental + Economic
```

Not supported as focal quantified outcomes:

```text
Social = not established
Integrated sustainability = not established
```

## Current proposed Zotero evidence set

```text
24 text candidates
31 region candidates
55 generated candidate annotations
```

This is not a target count and may decrease/change after visual verification, human review, geometry, and final redundancy analysis.

No annotation has been created.

## New generic-engine lesson — T040 candidate

Even after the V8 `58/58` preprocessing PASS, six non-scientific records remained in the atomic register, including orphaned address tails and editorial metadata such as:

```text
Tronoh, Perak 32610, Malaysia.
Box 11099, Taif 21944, Saudi Arabia.
Data availability ...
Received: 1 July 2024
Accepted: 26 November 2024
```

These were safely excluded during adjudication and did not contaminate final scientific evidence.

Proposed candidate invariant:

```text
T040_candidate:
Scientific claim construction must exclude all structurally bounded administrative metadata,
including orphaned address tails and editorial metadata even when Department/email/DOI markers are absent.
```

`T040` remains **candidate**, not a frozen permanent regression, until deliberately promoted under the regression-governance rule before NUS-18 generalization.

## Adjudication artifacts

```text
NUS48_AUTOMATED_SCIENTIFIC_ADJUDICATION_V1.json
SHA-256: 0ac73aaaf5ca0c8d2fc418e5b4c0cd50c9e0f81f320b40260bd4c1eb7087b804

NUS48_AUTOMATED_SCIENTIFIC_ADJUDICATION_REPORT_V1.md
SHA-256: 11530e457a43fe9e10c32df561814f1099b79d2cecfb359e12a8041d795b0898

NUS48_AUTOMATED_SCIENTIFIC_ADJUDICATION_MANIFEST_V1.json
SHA-256: b077dc69466d97279a95a6963359c39855fd956b2f569af4248f29cda4cbfe9f

NUS48_AUTOMATED_SCIENTIFIC_ADJUDICATION_REVIEW_PACKAGE_V1.zip
SHA-256: 8e9645b3b559a278ade368b4ae6db31dc6930793d40e3965deea3f6133714093
```

## Current gate

```text
AUTOMATED SCIENTIFIC ADJUDICATION
→ HUMAN SCIENTIFIC REVIEW
```

No Zotero writing is authorized.

Human review must explicitly accept/reject the adjudication, especially:

- IC001 abstract/body mechanical contradiction;
- IC002 modulus-of-elasticity composition inconsistency;
- IC003 R² assignment inconsistency;
- Eq. 2 visual exactness requirement;
- Table 1 provenance uncertainty;
- candidate T040 generic-engine lesson.

Only after explicit human approval may the workflow proceed to visual exactness, exact geometry, schema validation, writer dry-run, and independent auditor dry-run.
