# Permanent Regression Knowledge — T001–T047

This is the successor to the earlier T001–T039 archive. It preserves all prior regressions and adds the post-adjudication, geometry/write/migration controls through T047.

## T001–T039

The definitions of T001–T039 remain frozen as recorded in `07_REGRESSION_CORPUS_T001_T039.md`.

## T040–T047 successor controls

The programme subsequently promoted additional generic invariants through the NUS-48 scientific closure, geometry, write, audit, and output-nature migration stages.

### T040 — structurally bounded administrative metadata

Scientific claim construction must exclude orphaned administrative/address/editorial metadata even when obvious markers such as `Department`, email, or DOI are absent.

Examples include isolated address tails, editorial dates, and data-availability administration when they are not focal scientific evidence.

### T041 — deterministic geometry integrity

Every proposed annotation geometry must be source-derived, deterministic, and independently auditable. Geometry must not be guessed from page labels or approximate visual placement.

### T042 — table-grid union geometry

When a scientifically necessary table region spans multiple cells/boxes, final region geometry must be the deterministic union of the required table-grid geometry rather than a visually approximate rectangle.

### T043 — explicit page-label persistence

Visible/printed page labels and internal page indices must remain separately persisted. A geometry record must not infer one from the other.

### T044 — immediate rollback registration

Every mutation-capable writer operation must register its rollback state immediately before/with the mutation so an interruption cannot leave an untracked partial write.

### T045 — explicit Zotero runtime JSON contract

Mutation/audit runtimes must exchange explicit machine-readable JSON contracts with stable field semantics. Similar-looking field names must not be assumed equivalent across components.

### T046 — comment-only migration integrity

A comment-schema migration may change only explicitly authorized comment payloads. Annotation keys, source text, geometry, colors, roles, tags, count, PDF bytes, and unrelated Zotero state must remain unchanged, followed by independent post-write audit and zero-delta rerun.

### T047 — delta-set migration-state classification

When two schema versions differ only on a subset of records or fields, migration phase must be classified from that **discriminating subset**.

Version-invariant records:

```text
validate payload integrity
but do not vote on migration phase
```

For NUS-48 Output-Nature V2:

```text
13/13 discriminating comments V1
→ V1_READY_FOR_MIGRATION

13/13 discriminating comments V2
→ V2_ALREADY_MIGRATED

mixture among the 13
→ MIXED_PARTIAL_MIGRATION_STATE
```

This prevents the false-positive mixed state caused by exclusive state classification combined with an impossible aggregate prestate expectation.

## Current permanent boundary

```text
T001 → T047
```

This regression knowledge is frozen into Generic NUS Evidence Engine V1 and must be carried into NUS-18 generalization testing.

## Promotion rule remains unchanged

A new regression after T047 requires:

```text
new observed failure
→ paper-independent invariant
→ reproducible regression
→ calibration-paper historical retest
→ controlled engine successor
```

Do not add new regression IDs merely for deeper examples of an already-covered failure class.
