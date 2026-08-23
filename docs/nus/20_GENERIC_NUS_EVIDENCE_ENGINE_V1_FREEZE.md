# Generic NUS Evidence Engine V1 — Freeze Specification

## Status

```text
GENERIC NUS EVIDENCE ENGINE V1 = FROZEN FOR GENERALIZATION TESTING
```

The engine is frozen from the accumulated lessons of NUS-172 and NUS-48 through permanent regression T047.

## Purpose

The engine must now demonstrate that the NUS methodology is reusable across structurally different papers without another bespoke engineering cycle.

The target transition is:

```text
NUS-48 closure
→ Generic NUS Evidence Engine V1 freeze
→ NUS-18 generalization test #1
```

## Frozen scientific architecture

```text
PURPOSE

Q → I → M_E → P → F → M_S → S → D
```

with strict ordered adjudication:

```text
WritingMode
→ ClaimOwner
→ Focality
→ CitationScope
→ EvidenceEligibility
→ Role
→ Ontology
```

## Nine evidence roles remain unchanged

```text
PURPOSE
INTERVENTION
INPUT
ENGINEERING_METHOD
ENGINEERING_OUTPUT
SUSTAINABILITY_TRANSFORMATION
SUSTAINABILITY_METHOD
SUSTAINABLE_OUTCOME
DECISION
```

## Frozen visible-comment rule

Only output roles expose scientific nature visibly.

```text
Engineering output here is [engineering nature] : [exact author wording]
Sustainability output here is [environmental/economic/social/integrated] : [exact author wording]
```

The other seven roles retain simple labels.

Nature is evidence-grounded and never guessed.

## Frozen engineering-output natures

```text
mechanical
fresh-state
physical
durability
transport/permeability
thermal
structural/functional
fracture/damage
time-dependent
constructability/production
```

## Frozen sustainability-output natures

```text
environmental
economic
social
integrated
```

Invariant:

```text
ENV + ECO + SOC ≠ INT
```

unless focal authors explicitly integrate dimensions.

## Frozen evidence-state separations

```text
Role ≠ Nature
Nature ≠ Metric
Metric ≠ Result
EvidenceState ≠ Nature
Mention/Hypothesis ≠ ObservedOutput
Co-occurrence ≠ Transformation
```

External metadata retains at least:

```text
role
nature
metric
method
result
unit
alternative
origin
evidence_state
provenance
ontology_code
annotation_key
page
geometry
```

## Frozen mutation safety

The writer remains fail-closed and transactional.

Required principles:

```text
exact-author wording
zero tags
role-based colors only
schema validation before write
exact deterministic geometry
immediate rollback registration
comment-only migration controls
idempotent recovery
post-write independent audit
second-pass Δ = 0
```

## Frozen surface rules

- inspect every physical table, figure, and equation;
- do not infer scientific inclusion from physical existence;
- preserve table-grid union geometry where required;
- persist page labels explicitly;
- distinguish rendered PDF evidence from text-layer extraction;
- preserve `formula_text = null` when exact formula text is not recoverable;
- require visual verification for visually recoverable but text-fragmented equations.

## Frozen regression architecture

Permanent regression history:

```text
T001 → T047
```

The engine must preserve all applicable regressions when processing later papers.

Key general invariants include:

- focality before role;
- complete physical-surface inventory;
- citation-safe quantitative extraction;
- deterministic metadata/front-matter exclusion;
- representation-boundary metadata rechecks;
- dependency-closed regressions;
- native-schema cross-component contracts;
- explicit JSON runtime contracts;
- comment-only migration controls;
- delta-set migration-state classification;
- fail-closed mutation;
- independent auditing;
- zero-delta post-write certification.

## Generic paper interface

A new paper should normally require only identity/configuration changes, for example:

```json
{
  "paper_id": 18,
  "parent_key": "<resolved Zotero parent key>",
  "attachment_key": "<resolved Zotero attachment key>",
  "expected_pdf_sha256": "<resolved focal PDF SHA-256>"
}
```

No paper-specific scientific conclusion may be encoded into generic engine code.

## Generalization success criterion

For paper `i`:

```text
SUCCESS_i = scientifically defensible result
            AND no bespoke pipeline redesign
```

Track:

```text
E_i = (
  T_manual,
  N_manual_actions,
  N_new_defects,
  N_new_regressions,
  N_bespoke_code_changes
)
```

Desired:

```text
N_bespoke_code_changes → 0
ManualExecutionSteps ≈ constant
Assurance ↑
```

## Change-control rule

The engine is frozen for NUS-18 generalization.

A new engine modification is permitted only if NUS-18 demonstrates a genuinely new general failure class:

```text
observed failure
→ general invariant
→ permanent regression
→ historical retest on calibration authorities
→ controlled engine successor
```

Different titles, methods, values, journal layouts, figure counts, or conclusions are not by themselves grounds for engine redesign.
