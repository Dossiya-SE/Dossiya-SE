# Permanent Regression Knowledge — T001–T047

This is the successor to the earlier T001–T039 archive. The authoritative source is `NUS_MASTER_FAILURE_REGRESSION_CORPUS_V17`, which contains **47 permanent tests**.

## T001–T039

Definitions remain frozen as recorded in `07_REGRESSION_CORPUS_T001_T039.md` and the authoritative V17 corpus.

## T040–T047 — exact successor controls

### T040 — structurally bounded administrative fragments

**Failure:** non-scientific administrative fragments survived atomic-claim preprocessing, including orphaned affiliation-address tails and back-matter Data availability / Received / Accepted records.

**Invariant:** scientific claim construction must exclude structurally bounded non-scientific administrative fragments at every representation boundary, including orphaned address tails, data-availability statements, and editorial received/accepted metadata.

### T041 — rendered-validated table geometry union

**Failure:** a detector-only bbox for NUS-48 Table 8 stopped before the final MOE column.

**Invariant:** complete table geometry must be derived from the rendered-validated union of the table detector bbox, intersecting table-grid drawing extents, and table text extents. Detector bbox alone cannot authorize a region.

### T042 — Zotero Run JavaScript authoritative return contract

**Failure:** an unawaited top-level async IIFE displayed `undefined (completed successfully)` instead of an authoritative JSON result.

**Invariant:** authoritative Zotero Run JavaScript scripts must use the harness-native contract: top-level await for async operations and a reachable top-level JSON return. A bare unawaited async IIFE is forbidden.

### T043 — exactly one JSON serialization boundary

**Failure:** an embedded annotation schema was serialized twice, so `JSON.parse()` returned a string rather than the expected object and `SCHEMA.annotations` was undefined.

**Invariant:** every embedded JSON artifact crosses exactly one serialization boundary, followed immediately by runtime type/structure assertions.

### T044 — rollback registration before downstream failure

**Failure:** a native annotation was created, then validation failed before its key entered the rollback ledger, leaving an orphan annotation.

**Invariant:** every native annotation ID must be registered in the compensating rollback ledger immediately after native creation returns an ID and before any persistence wait, validation, or downstream operation can throw.

### T045 — explicit page-label persistence

**Failure:** a persisted annotation had `annotationPageLabel=''` although the frozen schema required page label `3`.

**Invariant:** every native Zotero annotation field participating in the frozen equality contract must be supplied explicitly when supported. `pageLabel` must be passed and verified; it cannot be inferred from page index.

### T046 — idempotent recovery utilities

**Failure:** the recovery utility returned `ABSTAIN_OR_FAIL` when the exact safe baseline already held.

**Invariant:** every recovery utility must be idempotent. If its exact verified safe postcondition already holds, it must return explicit zero-delta PASS and perform no mutation.

### T047 — delta-set migration-state classification

**Failure:** the output-nature migration prestate detector rejected a clean V1 state as mixed although all 13 mutable comments were V1 and none were V2.

**Invariant:** when source and target schemas overlap on unchanged records, migration-state classification must be performed on the mutable delta set only. Unchanged records are verified against their common payload and must not infer mutually exclusive source/target state.

For NUS-48:

```text
20 unchanged common records + 13 old comments
→ V1_READY_FOR_MIGRATION

20 unchanged common records + 13 target comments
→ V2_ALREADY_MIGRATED

any mixture among the 13 changed comments
or any immutable-field drift
→ fail closed
```

## Current permanent boundary

```text
T001 → T047
```

Authoritative corpus:

```text
NUS_MASTER_FAILURE_REGRESSION_CORPUS_V17
version = 17.0.0
test_count = 47
SHA-256 = 8595d33856aba1228a4aaeb512505241b3a8c88011a251d92ecbed16183ed77a
```

This regression knowledge is frozen into Generic NUS Evidence Engine V1 and must be carried into NUS-18 generalization testing.

## Promotion rule

A new regression after T047 requires:

```text
new observed failure
→ paper-independent invariant
→ reproducible regression
→ calibration-paper historical retest
→ controlled engine successor
```

Do not add new regression IDs merely for deeper instances of an existing failure class.
