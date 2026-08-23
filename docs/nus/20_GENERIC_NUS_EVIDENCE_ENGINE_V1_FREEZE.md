# Generic NUS Evidence Engine V1.0.1 — Frozen Maintenance Baseline

## Status

```text
NUS Evidence Engine V1.0.1 = FROZEN FOR GENERALIZATION TESTING
```

V1.0.1 is the frozen maintenance successor to V1.0.0. It preserves the NUS-172/NUS-48 scientific and mutation architecture and adds only permanent regression `T048`, discovered during the NUS-18 identity locator.

## Release authority

```text
Package: NUS_EVIDENCE_ENGINE_V1.0.1_FROZEN.zip
Package SHA-256:
2ca74e7e99b3862e54d626ea90f37f9011112c1a08c0d77a5cdd9c9dfed74ee6

Freeze-manifest SHA-256:
9d09ae86a416cdabbd7b0c8bc9c7a165c34b7329837cb360f7427ccc41c6df2b

Static controls: 19/19 PASS
Regression range: T001–T048
```

## Maintenance change — T048

Permanent invariant:

```text
Any Zotero API that may return a Promise must be awaited before filtering,
iteration, array assertions, or field access.
```

The triggering failure was read-only:

```text
TypeError: all.filter is not a function
```

caused by using `Zotero.Items.getAll(...)` without resolving the asynchronous return first.

The repair did not alter scientific ontology, source interpretation, writer logic, or NUS-48 frozen evidence.

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

Only output roles expose scientific nature visibly:

```text
Engineering output here is [engineering nature] : [exact author wording]
Sustainability output here is [environmental/economic/social/integrated] : [exact author wording]
```

The other seven roles retain simple labels. Nature is evidence-grounded and never guessed.

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

The writer remains fail-closed and transactional:

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

```text
T001 → T048
```

The engine must preserve all applicable regressions when processing later papers.

## NUS-18 generalization result so far

NUS-18 Phase 1 discovery has now passed with no engine change:

```text
PASS_READ_ONLY_DISCOVERY
pages = 16
lines = 1466
surface anchors = 22
live annotations = 0
PDF mutation = false
Zotero mutation = false
```

The source map preserves the PDF's extracted page labels exactly, including the transition from `8` to `97`; the engine must not silently renumber them.

## Generic paper interface

NUS-18 demonstrates the intended minimal interface:

```json
{
  "paper_id": 18,
  "parent_key": "BZZGBD2I",
  "attachment_key": "Z8UEF2GH",
  "expected_pdf_sha256": "826beba0d3973661137328c8d68ac992a8d03fa91860d69ee8c1c196010c3839"
}
```

No paper-specific scientific conclusion may be encoded into generic engine code.

## Generalization success criterion

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

A new engine modification is permitted only if NUS-18 demonstrates a genuinely new general failure class:

```text
observed failure
→ general invariant
→ permanent regression
→ historical retest on calibration authorities
→ controlled engine successor
```

Different titles, methods, values, journal layouts, figure counts, page labels, or conclusions are not by themselves grounds for engine redesign.
