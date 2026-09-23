# NUS-48 Full Development History — From Unannotated PDF to 58/58 Premutation PASS

## 1. Scientific objective

NUS-48 was used as the final heavy calibration/stress-test paper before freezing the generic NUS Evidence Engine.

Target pipeline:

```text
PDF
→ Source Map
→ Atomic Claims
→ Physical Surfaces
→ Scientific Candidates
→ Regression Tests
→ Independent Certification
```

before:

```text
Scientific Adjudication
→ Human Approval
→ Geometry
→ Writer
→ Audit
→ Zotero
```

Safety rule:

```text
uncertainty or failed control
→ ABSTAIN_OR_FAIL
```

## 2. Immutable source identity

**Paper:** NUS-48  
**Title:** *Combined effect of jute fiber and corn cob ash on sustainability assessment and mechanical properties of roller compacted concrete using RSM modelling*  
**DOI:** `10.1038/s41598-024-81345-7`

```text
Parent key      LYG93FY6
Attachment key  3UL86A9R
PDF SHA-256     bd27b10cb8110d7a48a0b28923e3e0cc2adc0fb2d7e416fb25714f8483db3609
```

Throughout development:

```text
live_annotation_count = 0
PDF mutation = false
Zotero mutation = false
mutation_authorized = false
```

## 3. Frozen scientific architecture

```text
Q → I → M_E → P → F → M_S → S → D
```

`PURPOSE` remains outside the chain.

```text
P + S ≠ P → S
P → S ≤ ExplicitTransformation
```

## 4. Frozen adjudication order

```text
WritingMode
→ ClaimOwner
→ Focality
→ CitationScope
→ EvidenceEligibility
→ Role
→ Ontology
```

Focality:

```text
FOCAL
FOCAL_ADOPTED
EXTERNAL
MIXED
UNCLEAR
```

Rules:

```text
EXTERNAL → reject
MIXED → split
UNCLEAR → ABSTAIN
FOCAL / FOCAL_ADOPTED → continue
```

## 5. Frozen Zotero writing standard

Future visible annotations must use:

```text
short semantic label + ": " + exact author wording
```

with exact highlight/region, role color, verbatim author wording, and zero annotation tags.

## 6. Physical-object completeness target

Paper-specific inspection established:

```text
Tables 1–8      = 8
Figures 1–19    = 19
Equations 1–7   = 7
Total           = 34 physical objects
```

Every physical object must eventually receive `INCLUDE`, `EXCLUDE`, `REDUNDANT`, or `ABSTAIN` with reason.

## 7. Initial Phase-1 discovery

First read-only source-layer runtime:

```text
NUS48_PHASE1_READONLY_DISCOVERY_V1.txt
SHA-256: aeb6cef7ef46ce891bce11fead0583d012dda3f9a703fc8eedec5c573f7145ce
```

It established the page/line source layer without Zotero mutation.

## 8. Initial Phase-2 V1

```text
NUS48_PHASE2_ATOMIC_CLAIM_PREPROCESSOR_V1
SHA-256: 01895fa6769cfdb792923e7e5616000bfb4ef543a02929af0c01c3e1c176c3f0
```

It initially generated roughly 113 claims, but scientific review showed significant defects.

## 9. First 13 scientific defects

The first deep scientific audit identified:

- **S001** — heading-less abstract missed.
- **S002** — reference-list content entered scientific claims.
- **S003** — title/author metadata merged with scientific prose.
- **S004** — Keywords merged into Introduction.
- **S005** — explicit purpose classified as method.
- **S006** — multifunction claims not atomically separated.
- **S007** — abstract completeness not explicitly tested.
- **S008** — citation numerals contaminated quantitative extraction.
- **S009** — numeric citation scope underdetected.
- **S010** — physical-surface false positives.
- **S011** — Equations 1–3 not represented as sustainability transformations.
- **S012** — input coverage from Tables 3–5 / RSM incomplete.
- **S013** — all-surface completeness not scientifically demonstrated.

This froze the development rule:

```text
Failure
→ Invariant
→ Permanent Regression
→ Historical Retest
```

## 10. First regression architecture: T001–T026

The engineering/scientific preprocessing regression programme accumulated T001–T026, covering substantive validation, geometry independence, Reader/API boundaries, table semantics, fragmented equations, MIXED segmentation, undefined-symbol preflight, closure authority, dependency control, external hash authority, self-contained executable verification, mutation blocking, anti-semantic-copying, no preset N_final, PURPOSE/design-choice atomicity, final-file hashes, abstract recognition, References boundary, metadata separation, purpose dominance, citation-safe quantities, transformations, inputs, surface syntax, abstract completeness, and complete physical-object inventory.

## 11. V2 preprocessing repair

This produced:

```text
NUS48_PHASE2_ATOMIC_CLAIM_PREPROCESSOR_V2
NUS48_MASTER_PREMUTATION_REGRESSION_HARNESS_V2
```

Master SHA-256:

```text
00c8772cccc462c1fed6060838d257537644875b38cd69e5e376154e87b13ddd
```

The master preserved all 26 original regression tests.

## 12. Independent-certifier architecture

Primary regression and independent certification were intentionally separated:

```text
Primary Regression ≠ Independent Certification
```

The independent architecture exposed package/governance defects that became:

- **T027** — regression corpus IDs inconsistent with executable IDs.
- **T028** — declared certification count differed from executable count.
- **T029** — certifier expected fields from the wrong persisted schema location.
- **T030** — returned certification object differed from persisted bytes.
- **T031** — integrity manifest loaded but not actually hash-verified.

## 13. First live premutation failure — Equation 2

A live run reached:

```text
24/26 PASS
T022 FAIL
T026 FAIL
```

Detected equations:

```text
[1,3,4,5,6,7]
```

Equation 2 was missing from the physical-surface register.

No state damage occurred.

## 14. Equation 2 root cause

Equation 2 exists in the rendered paper, but its displayed formula was not reliably recoverable from the PDF text layer. The text layer exposed an equation reference such as `Eq. (2)90.` rather than a trustworthy exact formula string.

Critical distinction:

```text
Equation existence ≠ formula text-layer recoverability
```

## 15. T032 — non-text/fragmented equation exactness

Permanent regression T032 requires reference-anchored/non-text/fragmented equations to be represented conservatively:

```text
detection_mode = REFERENCE_ANCHORED_NON_TEXT_OR_FRAGMENTED
formula_text = null
content_exactness = REFERENCE_ONLY_FORMULA_TEXT_NOT_RECOVERED
visual_review_required = true
```

Equation 2 could therefore enter the physical inventory without pretending its exact displayed formula had been recovered.

## 16. Master V2R1

After T032:

```text
Master = 27/27 PASS
Equations = [1,2,3,4,5,6,7]
```

## 17. Independent certification exposed SG009 and SG013

A later run produced:

```text
Master = 27/27 PASS
Independent = 22/24
```

Failures:

```text
SG009
SG013
```

This demonstrated that the independent layer was genuinely capable of contradicting the master.

## 18. SG009 — publisher/contact metadata contamination

A bad candidate contained author email, `OPEN`, journal footer, DOI/publisher URLs, and similar page furniture. This produced **T033**.

### T033 invariant

Deterministic non-scientific contact/publisher/affiliation boilerplate must be excluded before scientific claim construction and must not reappear at later representation boundaries.

## 19. SG013 — Equation 3 transformation classification

The focal paper states that total concrete cost was computed using Eq. (3), but the transformation classifier failed to surface it. A punctuation-sensitive regular-expression defect contributed to the failure. This produced **T034**.

### T034 invariant

Regex alternatives that terminate in punctuation must not rely on an inappropriate global trailing word boundary.

## 20. V2R2 preprocessing

After these corrections, Phase 2 returned:

```text
PASS_READ_ONLY_PREPROCESSOR_V2R2
Abstract claims        11
Body claims           421
Reference lines       242 excluded
Boilerplate lines      64 excluded
Tables                   8
Figures                 19
Equations                7
annotations              0
mutation_authorized   false
```

## 21. Affiliation metadata still leaked — T035

The master still detected affiliation claims such as `2Department of Chemical Engineering...` and `3Department of Civil and Environmental Engineering...`.

PDF extraction can detach an affiliation marker from the following institutional line, so line-level regexes were insufficient.

### T035 invariant

Front-matter affiliation detection must tolerate detached/fragmented affiliation markers and continuation structure.

## 22. V2R3 revealed representation-boundary leakage — T036

Even when line-level/block-level affiliation filtering passed, metadata could re-emerge after sentence splitting:

```text
mixed block
→ sentence splitting
→ metadata-only sentence
```

### T036 invariant

Deterministic metadata filtering must apply at every representation boundary:

```text
raw line
→ assembled block
→ sentence
→ atomic clause
```

## 23. Runtime-scope failure — T037

A later master failed with:

```text
ReferenceError: splitSentences is not defined
```

T036 existed in master scope but attempted to call a helper private to the Phase-2 runtime.

This was not scientific evidence failure; it was a runtime/package dependency defect.

### T037 invariant

```text
Every executable regression must be dependency-closed.
```

A regression may inspect public/persisted artifacts or use a self-contained/master-owned helper. It must not call an unexported private helper belonging to another runtime.

## 24. Master reached 32/32

After T037:

```text
Master = 32/32 PASS
```

but independent certification still found SG013 for Equation 2 semantic coverage.

## 25. Deeper Equation 2 semantic failure — T038

The relevant focal text effectively used:

```text
... evaluated using Eq. (2)90.
```

where `(2)` is the equation number and `90` is a citation reference. Cleaner segmentation had separated the ESE heading from the method sentence, exposing a classifier dependency on clean equation-reference endings or heading context.

### T038 invariant

```text
Semantic classification must be invariant to citation-suffix attachment.
```

Thus `evaluated using Eq. (2)90.` can surface the transformation while `90` remains excluded from quantitative values.

## 26. Master 33/33 + Independent 24/24

After T038:

```text
Master = 33/33 PASS
Independent = 24/24 PASS
```

Equation transformation coverage existed for Eq. 1, Eq. 2, and Eq. 3. Metadata checks passed. Physical inventory remained 8 tables + 19 figures + 7 equations. No final focality, role, or annotation decision had been assigned prematurely.

## 27. Outer orchestration contract failure — T039

The V7 scientific certifier itself passed 24/24, but the outer orchestration failed `CERTIFIER_MUTATION_GUARD_FAIL` because the certifier exposed:

```text
zotero_mutation_performed
```

while the outer orchestrator expected:

```text
zotero_annotation_mutation_performed
```

This was a schema-contract mismatch, not scientific failure.

### T039 invariant

```text
Validate each component against its native schema
→ normalize only at orchestration boundary
```

Similar-looking field names must not be assumed equivalent.

## 28. Final V8 run — 58/58

The final V8 one-shot returned:

```text
protocol = NUS48_ONESHOT_PREMUTATION_READINESS_V8
status = PASS_PREMUTATION_READY_FOR_SCIENTIFIC_ADJUDICATION
```

Breakdown:

```text
Master regression          33/33 PASS
Independent certification  24/24 PASS
Orchestration contract       1/1 PASS
--------------------------------------
Total                       58/58 PASS
```

## 29. Final immutable V8 state

```text
paper_id = 48
parent_key = LYG93FY6
attachment_key = 3UL86A9R
pdf_sha256 = bd27b10cb8110d7a48a0b28923e3e0cc2adc0fb2d7e416fb25714f8483db3609
live_annotation_count = 0
zotero_annotation_mutation_performed = false
pdf_mutation_performed = false
mutation_authorized = false
```

## 30. Current V8 artifacts

```text
NUS48_ONESHOT_PREMUTATION_READINESS_BUNDLE_V8.json
SHA-256: 5359ccd275db4d4aefb1a2ab76d734a2b2e7ef547207b098f28e92ed4541d69e

NUS48_ONESHOT_PREMUTATION_READINESS_MANIFEST_V8.json
SHA-256: 646e312f7e74f878575e5cb2d6d5ec82d5023a13afce793ce5fa4086ca1dfd9e

NUS48_ONESHOT_PREMUTATION_READINESS_V8.txt
SHA-256: b4b4ba0448607e531f07eee39d30a6a114172d9f6aed3a2a080bc992f13f3988

NUS_MASTER_FAILURE_REGRESSION_CORPUS_V10.json
SHA-256: 6f75090892388582800b407c1efb8f094802fbaef72d3570f61d8d300f736ccc
```

## 31. Permanent regression knowledge

The historical failure corpus preserves knowledge through T039.

Current NUS-48 paper-level master executable suite:

```text
T001–T026
T032–T038
= 33 tests
```

Package/certification/governance history:

```text
T027–T031
```

Orchestration:

```text
T039
```

## 32. Scientific candidate-level knowledge already established

### Design/intervention variables

CCA substitution levels:

```text
5%, 10%, 15%, 20%
```

JF levels:

```text
0.25%, 0.50%, 0.75%, 1.00%
```

### Mechanical outcomes in abstract

For `0.50% JF + 10% CCA` at 28 days, the abstract reports approximately:

```text
Flexural strength           5.3 MPa
Splitting tensile strength  3.8 MPa
Compressive strength       32.88 MPa
Modulus of elasticity      33.11 GPa
```

These remain subject to final body-level scientific adjudication.

### Sustainability domains

```text
Environmental: embodied carbon
Economic: material/concrete cost
Coupling-related metric: eco-strength efficiency
```

### RSM/methods

```text
Response Surface Methodology
ANOVA
response-prediction models
optimization
```

The abstract reports R² values around 96–99%, subject to final adjudication.

### Candidate decision

The paper contains a practical recommendation around:

```text
10% CCA + 0.50% JF
```

which appears eligible for `DECISION`, pending formal body confirmation.

## 33. Sustainability-transformation architecture

### Equation 1 — embodied carbon

Conceptual transformation:

```text
material quantities × embodied-carbon factors
→ total embodied carbon
```

Current coupling interpretation: `PARALLEL_ONLY` unless an engineering output is explicitly consumed.

### Equation 2 — eco-strength efficiency

Conceptual transformation:

```text
28-day compressive strength / embodied carbon
→ ESE
```

This is structurally `COUPLED` because engineering performance participates in the transformation.

Important exactness state:

```text
Equation existence = established
Exact focal-PDF displayed formula = visual verification required
```

External/publisher rendering must not silently substitute for focal-PDF evidence.

### Equation 3 — cost

Conceptual transformation:

```text
material quantities × unit costs
→ total concrete cost
```

Current coupling interpretation: `PARALLEL_ONLY` unless an engineering output explicitly participates.

## 34. Physical surfaces proven complete

```text
|Tables| = 8
|Figures| = 19
|Equations| = 7
|Physical objects| = 34
```

No physical object may disappear silently during adjudication.

## 35. Abstract completeness

The heading-less abstract is correctly detected and contains **11 atomic claims**. Each must eventually receive one body-crosscheck state:

```text
BODY_CONFIRMED
BODY_MORE_SPECIFIC
ABSTRACT_ONLY
BODY_CONTRADICTS
NONCOMPARABLE
UNRESOLVED
```

## 36. What 58/58 proves

It proves coherence through:

```text
PDF
→ extraction
→ claims
→ surfaces
→ regression
→ independent certification
→ orchestration
```

## 37. What 58/58 does not prove

It does **not** prove:

- all candidate claims are focal;
- all roles/ontologies are final;
- all surfaces should be annotated;
- all annotation geometries are exact;
- comments are ready;
- human approval exists;
- mutation is authorized.

Therefore:

```text
58/58 ≠ scientific closure
58/58 = premutation readiness
```

## 38. Current release-state position

Reached:

```text
UNVERIFIED
→ IDENTITY_VERIFIED
→ EXTRACTION_COMPLETE
→ PREMUTATION_REGRESSION_PASS
→ INDEPENDENT_CERTIFICATION_PASS
```

Current gate:

```text
SCIENTIFIC_ADJUDICATION
```

Not reached:

```text
HUMAN_APPROVED
SURFACES_COMPLETE
GEOMETRY_PROVEN
SCHEMA_PASS
WRITER_DRYRUN_PASS
AUDITOR_DRYRUN_PASS
MUTATION_AUTHORIZED
MUTATED
WRITER_RERUN_ZERO_DELTA
INDEPENDENT_AUDIT_PASS
FROZEN
```

## 39. Freeze rule after V8

Freeze:

- PDF identity;
- source-extraction architecture;
- claim-segmentation architecture;
- physical-surface inventory;
- T001–T039 failure knowledge;
- premutation master architecture;
- independent-certifier architecture;
- V8 premutation PASS state.

Do not continue changing preprocessing because of preference. New change requires a new observed failure, general invariant, permanent regression, and historical retest.

## 40. Immediate next work

Move from candidate evidence to scientifically adjudicated evidence through five workstreams:

1. Claim adjudication using the frozen decision order.
2. Abstract-body adjudication for all 11 abstract claims.
3. Surface adjudication for all 34 physical objects.
4. EvidenceAnchor → Observation → Transformation lineage and Q→I→M_E→P→F→M_S→S→D reconstruction.
5. Transformation ledger for every sustainability result.

Human approval remains separate. No AI-generated adjudication package becomes `HUMAN_APPROVED` until the user explicitly approves it.

## 41. Scaling lesson

The objective of the NUS-48 effort was not one bespoke annotation job. It was to convert failures into reusable system knowledge.

Desired trajectory:

```text
NUS-48: high development cost
NUS-18: reuse/generalization
NUS-191: reuse/generalization
NUS-67: final generalization
NUS-15 onward: production
```

If NUS-18 requires another long bespoke development cycle, that is evidence that the architecture is not sufficiently generic.

## 42. Final interpretation

NUS-48 began with zero annotations, unproven extraction, unproven surface completeness, unproven semantic coverage, and unproven independent certification.

It reached:

```text
33/33 Master
24/24 Independent
1/1 Orchestration
58/58 Total
34 physical objects represented
11 abstract claims controlled
0 live annotations
0 Zotero mutations
0 PDF mutations
0 failed automated premutation checks
0 mutation authorization
```

The governing transition is now:

```text
PREPROCESSING FREEZE
→ NUS-48 SCIENTIFIC ADJUDICATION
```
