# T047 — Migration Prestate Classification Must Use Discriminating Records Only

## Observed failure

The first NUS-48 output-nature migration one-shot failed closed with:

```text
FAIL:MIXED_PARTIAL_MIGRATION_STATE
v1Changed = 13
v2Changed = 0
mutation_attempted_key_count = 0
rollback_registered_count = 0
current_annotation_count = 33
```

The PDF SHA-256 remained:

```text
bd27b10cb8110d7a48a0b28923e3e0cc2adc0fb2d7e416fb25714f8483db3609
```

and no migration write was attempted.

## Root cause

The original `classifyState()` implementation uses exclusive classification:

```text
if record matches V1 → V1
else if record matches V2 → V2
```

For the 20 annotations whose comments are unchanged between V1 and V2, the V1 and V2 expected payloads are identical. Because V1 is tested first, these records are classified as `V1` only.

However, the original prestate gate expected:

```text
state.v1 === 33 && state.v2 === 20
```

for a complete V1 state, based on the assumption that the 20 invariant records would increment both counters.

That aggregate state is unreachable under the exclusive classifier.

The returned diagnostic:

```text
v1Changed = 13
v2Changed = 0
```

actually proves that **all 13 comments that differ between schema versions remain in V1 form**. It is not evidence of a true partial migration.

## Permanent invariant

```text
When two schema versions differ only on a subset of records or fields,
version state must be inferred from the discriminating subset only.
Version-invariant records validate payload integrity but do not vote on version state.
```

For this migration:

```text
13/13 discriminating comments V1
→ V1_READY_FOR_MIGRATION

13/13 discriminating comments V2
→ V2_ALREADY_MIGRATED

any V1/V2 mixture among the 13
→ MIXED_PARTIAL_MIGRATION_STATE
```

The 20 unchanged records must still match their expected payload exactly, but their state label is irrelevant to migration phase.

## Regression ID

```text
T047
Migration prestate classification uses discriminating records only
```

### Positive controls

1. 20 version-invariant records + 13 changed records all V1 → `V1_READY_FOR_MIGRATION`.
2. 20 version-invariant records + 13 changed records all V2 → `V2_ALREADY_MIGRATED`.

### Negative control

A mixture among the 13 discriminating records must fail closed as `MIXED_PARTIAL_MIGRATION_STATE` before any mutation.

## Repair scope

The correction is intentionally narrow. It does **not** change:

- the 33-annotation schema;
- annotation keys;
- roles;
- colors;
- tags;
- geometry;
- exact author wording;
- output-nature target comments;
- PDF bytes;
- migration authorization chain;
- rollback logic;
- postwrite audit logic;
- zero-delta/idempotency requirement.

Only the migration prestate classification rule is repaired.

## Safety interpretation

This failure is a software state-machine defect, not a NUS-48 scientific or annotation-payload failure.

The failed run is safe because:

```text
mutation_attempted_key_count = 0
rollback_registered_count = 0
pdf_mutation_performed = false
annotation_count = 33
```

The corrected runtime must be rerun from this unchanged state; no manual annotation editing is permitted.
