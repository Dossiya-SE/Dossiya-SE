# NUS-48 Native Annotation State and V3 Migration Boundary

## New source-state update

A subsequent project update states that NUS-48 now has:

```text
33 native Zotero annotations
```

written under the then-authorized frozen schema.

This is downstream of the historically preserved premutation state in which:

```text
live_annotation_count = 0
```

The two records are not to be collapsed. The zero-annotation state remains valid evidence of the premutation stage; the 33-annotation state is the newly declared later state.

## Verification status in this GitHub update

The count of 33 is recorded from the user-supplied project update. This GitHub update does not independently re-query the live Zotero database and therefore marks the state as:

```text
USER_DECLARED_NOT_MACHINE_REVERIFIED_IN_THIS_UPDATE
```

This is not a reason to discard the update; it is a provenance statement about how the repository learned the new state.

## Schema relationship

The 33 native annotations were written under the earlier authorized comment schema.

The newly frozen output-nature schema V3 changes visible comments only for:

```text
ENGINEERING_OUTPUT
SUSTAINABLE_OUTCOME
```

Examples:

```text
Engineering output : ...
→ Engineering output here is mechanical : ...
```

```text
Sustainability output : ...
→ Sustainability output here is environmental : ...
```

This is a payload/schema mutation even when:

- annotation geometry remains unchanged;
- source highlight text remains unchanged;
- role remains unchanged;
- role color remains unchanged;
- tags remain zero.

## No manual retrofit

The 33 comments must not be edited manually one by one.

If NUS-48 is retrofitted to V3, the controlled path is:

```text
V3 schema freeze
→ migration regression suite
→ exact migration plan
→ explicit mutation authorization
→ transactional comment-only migration
→ rerun with zero delta
→ independent audit
→ migration freeze
```

## Required migration invariants

A future V3 migration must prove at least:

1. **Cardinality stability** — annotation count does not change solely because of comment-schema migration.
2. **Identity stability** — existing annotation keys/identities are preserved when technically possible and authorized.
3. **Geometry stability** — highlight/region coordinates remain byte-for-byte or semantically equivalent according to the frozen geometry contract.
4. **Role stability** — role assignment does not change merely because a nature label is added.
5. **Color stability** — role colors remain unchanged.
6. **Tag stability** — annotation tags remain zero.
7. **Author-text stability** — text after the colon remains exact author wording.
8. **Nature-grounding** — a nature is added only where directly supported by the focal output.
9. **Fallback safety** — when nature is not defensible, retain the broader output label.
10. **No evidence-count inflation** — the migration does not create new annotations.
11. **Idempotence** — migration rerun produces zero delta.
12. **Independent audit** — a separately implemented auditor verifies the resulting state.

## Migration is optional, not implied

The V3 schema can govern NUS-18 and later papers even if NUS-48 remains historically frozen under its prior schema.

Therefore there are two legitimate paths:

### Path A — preserve NUS-48 as historical calibration state

```text
NUS-48 stays under prior authorized schema
NUS-18 onward uses V3
```

### Path B — controlled NUS-48 comment-only migration

```text
NUS-48 prior state
→ validated V3 migration
→ independently audited V3 state
```

No path is chosen merely by freezing V3.

## Current authorization

```text
manual V3 retrofit = NOT AUTHORIZED
comment-only migration = NOT AUTHORIZED
```

A future explicit authorization must reference a validated migration package, not the comment convention alone.
