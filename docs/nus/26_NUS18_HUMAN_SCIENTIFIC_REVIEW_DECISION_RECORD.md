# NUS-18 Human Scientific Review Decision Record

## Status

```text
PENDING_EXPLICIT_HUMAN_SCIENTIFIC_APPROVAL
```

This gate prevents a technically valid Phase-2 package from being silently promoted to geometry/write authorization.

## Already established

```text
Identity verified                      yes
Whole-PDF discovery                    PASS
Phase-2 package manifest               verified
Physical objects reconciled            30
Static Phase-2 controls                19/19 PASS
Generic Engine V1.0.2 / T049           frozen
Zotero annotations                     0
Zotero mutation                        false
PDF mutation                           false
```

## HR18-001 — Physical-object reconciliation

Current scientific inventory:

```text
10 tables + 9 figures + 11 numbered equations = 30 objects
9 INCLUDE / 19 REDUNDANT / 2 EXCLUDE
```

Decision required: accept, revise, or reject the scientific dispositions before geometry is treated as final.

Human decision: `PENDING`

## HR18-002 — Proposed evidence set is provisional

Current set:

```text
25 proposed nonredundant annotations
16 text
9 regions
```

This is evidence-derived, not preset. Exact Reader wording, region geometry, visual QA, and final redundancy control may still reduce/change the set.

Human decision: `PENDING`

## HR18-003 — Engineering-output nature `energy`

NUS-18 contains focal EUI/whole-building energy outputs. Engine V1.0.2 now supports:

```text
Engineering output here is energy : [exact author wording]
```

Do not coerce these outputs to `thermal` because the reported EUI includes lighting, equipment, conditioning, and other loads.

Human decision: `PENDING`

## HR18-004 — Sustainability-domain ruling

Current ruling:

```text
environmental = supported
economic      = no focal quantified outcome found
social        = no focal quantified outcome found
integrated    = not established
```

`Integrated energy-emergy` describes methodological coupling and does not itself establish integrated environmental-economic-social sustainability.

Human decision: `PENDING`

## HR18-005 — Validation ruling

Current classification:

```text
InternallyValidated
```

Target: focal emergy metamodel.

Basis:

- analytical-versus-predicted comparison;
- Fig. 8;
- residual standard error / F-value;
- regression significance tests.

No external validation is claimed.

Human decision: `PENDING`

## HR18-006 — Explicit engineering→sustainability coupling

The transformation ledger identifies two direct P→S couplings:

```text
operational energy contribution → total building emergy (Eq. 1b architecture)
operational energy use → operational emergy (Eq. 3 architecture)
```

Other transformations remain `PARALLEL_ONLY` unless an engineering output is actually consumed.

Human decision: `PENDING`

## HR18-007 — Energy-optimal vs emergy-optimal decisions

The focal paper reports distinct optimization decisions for:

```text
operational-energy optimum
emergy optimum
```

These must remain separate decision scopes and must not be collapsed into a single universal optimum.

Human decision: `PENDING`

## HR18-008 — Page labels

The Reader-extracted native labels contain the observed transition:

```text
8 → 97
```

The labels remain source metadata and must be persisted exactly. They must not be silently normalized to sequential display numbers.

Human decision: `PENDING`

## HR18-009 — Exact author wording and geometry are still open

Line-joined Phase-2 strings are scientific-adjudication evidence only. They are not yet the final Zotero comment payload.

Before schema/write authorization:

```text
Reader token exactness
→ atomic exact wording
→ exact highlight/region geometry
→ visual QA
```

must be proven.

Human decision: `PENDING`

## Approval vocabulary

A human reviewer must explicitly choose one of:

```text
APPROVE_AS_ADJUDICATED
APPROVE_WITH_RECORDED_EXCEPTIONS
REVISE_BEFORE_APPROVAL
REJECT_ADJUDICATION
```

Automated tooling must not infer approval from package PASS, Engine V1.0.2 freeze, or the existence of 25 proposed records.

## State after approval

Only after explicit approval may NUS-18 advance to:

```text
READER_EXACTNESS_AND_ALL_SURFACE_GEOMETRY
→ FINAL_PROPOSED_SCHEMA
→ WRITER_DRYRUN
→ INDEPENDENT_AUDITOR_DRYRUN
→ MUTATION_AUTHORIZATION
```

Until then:

```text
mutation_authorized = false
```
