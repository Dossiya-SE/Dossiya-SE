# NUS-48 Current Authoritative State — 58/58 Premutation PASS

## Identity

```text
paper_id = 48
parent_key = LYG93FY6
attachment_key = 3UL86A9R
pdf_sha256 = bd27b10cb8110d7a48a0b28923e3e0cc2adc0fb2d7e416fb25714f8483db3609
```

## Current protocol

```text
protocol = NUS48_ONESHOT_PREMUTATION_READINESS_V8
status = PASS_PREMUTATION_READY_FOR_SCIENTIFIC_ADJUDICATION
```

## Automated assurance

```text
Master regression          33/33 PASS
Independent certification  24/24 PASS
Orchestration contract       1/1 PASS
--------------------------------------
Total                       58/58 PASS
```

## Source-state safety

```text
live_annotation_count = 0
zotero_annotation_mutation_performed = false
pdf_mutation_performed = false
mutation_authorized = false
```

## Preprocessing outputs proven

```text
abstract_claim_count = 11
physical tables = 8
physical figures = 19
physical equations = 7
physical_object_total = 34
```

Known V2R2 preprocessing snapshot during the final development sequence:

```text
body_claim_count = 421
excluded_reference_line_count = 242
excluded_boilerplate_line_count = 64
```

## Current physical inventory

```text
Tables:    1–8
Figures:   1–19
Equations: 1–7
```

Equation 2 exactness remains deliberately conservative:

```text
detection_mode = REFERENCE_ANCHORED_NON_TEXT_OR_FRAGMENTED
formula_text = null
content_exactness = REFERENCE_ONLY_FORMULA_TEXT_NOT_RECOVERED
visual_review_required = true
```

## Current scientific candidate architecture

### Focal purpose

The paper contains an explicit focal purpose statement covering combined JF/CCA effects, mechanical properties, embodied carbon, RSM modelling, and optimization. `PURPOSE` must dominate embedded method vocabulary in that sentence.

### Design/input variables

CCA levels:

```text
0%, 5%, 10%, 15%, 20%
```

JF levels:

```text
0%, 0.25%, 0.50%, 0.75%, 1.0%
```

These carry both design-choice/intervention meaning and RSM-input meaning and must be atomically represented rather than forced into one role.

### Mechanical outputs reported in abstract

At `0.50% JF + 10% CCA`, 28-day abstract values are approximately:

```text
Flexural strength           5.3 MPa
Splitting tensile strength  3.8 MPa
Compressive strength       32.88 MPa
Modulus of elasticity      33.11 GPa
```

These are not final human-approved evidence until body reconciliation is complete.

### Sustainability branches

1. **Embodied carbon** — environmental sustainability.
2. **Eco-strength efficiency** — sustainability-related coupling metric using engineering performance and embodied carbon.
3. **Material/concrete cost** — economic sustainability.

### Transformation interpretation

```text
Eq. 1: material quantities × embodied-carbon factors → embodied carbon
link_status = PARALLEL_ONLY unless an engineering output is explicitly consumed

Eq. 2: 28-day compressive strength / embodied carbon → ESE
link_status = COUPLED
exact displayed focal-PDF formula still requires visual verification

Eq. 3: material quantities × unit costs → total concrete cost
link_status = PARALLEL_ONLY unless an engineering output is explicitly consumed
```

### Candidate decision

The paper contains a recommendation around:

```text
10% CCA + 0.50% JF
```

It remains pending formal body-level decision confirmation.

## Current release position

Reached:

```text
IDENTITY_VERIFIED
EXTRACTION_COMPLETE
PREMUTATION_REGRESSION_PASS
INDEPENDENT_CERTIFICATION_PASS
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

## Interpretation

`58/58 PASS` is a strong **premutation readiness** state. It is not scientific closure and must never be used to bypass focality, citation-scope, human-approval, geometry, writer, or audit gates.
