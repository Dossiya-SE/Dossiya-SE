# Permanent Regression Knowledge — T001–T039

The regression corpus preserves failure knowledge discovered during NUS-172/NUS-48 calibration. Not every historical test belongs to the current paper-level master executable; package, certification, and orchestration regressions are tracked separately.

## Core engineering — T001–T016

| ID | Invariant |
|---|---|
| T001 | Validate substantive invariants, not summary status alone |
| T002 | Geometry must be independent of visible page numbering assumptions |
| T003 | Reader/API bridge must be explicitly proven |
| T004 | Preserve 2-D table semantics |
| T005 | Fragmented-equation handling must be regression-protected |
| T006 | MIXED evidence must support segmentation/splitting |
| T007 | Undefined-symbol/runtime preflight exists |
| T008 | Closure authority must be explicit |
| T009 | No manual stale Phase-1/Phase-2 dependency |
| T010 | Embedded self-hash is not authoritative; use external hash authority |
| T011 | Executable code must be self-contained/hash-verified |
| T012 | Mutation is hard-blocked before science and dry-run gates |
| T013 | Generic architecture must not copy NUS-172 semantics |
| T014 | No preset final annotation count `N_final` |
| T015 | PURPOSE vs design-choice atomicity must be preserved |
| T016 | Final artifact hash links must be fresh and verified |

## NUS-48 preprocessing/scientific-surface failures — T017–T026

| ID | Invariant |
|---|---|
| T017 | Heading-less abstract must be detected |
| T018 | References is a hard scientific-extraction boundary |
| T019 | Bibliographic metadata and Keywords remain outside scientific claims |
| T020 | Explicit purpose semantics dominate embedded method vocabulary |
| T021 | Citation IDs must not become scientific quantities |
| T022 | Sustainability transformations must be surfaced |
| T023 | Input candidates and relevant input surfaces must be represented |
| T024 | Physical-surface detection must use anchored structural syntax |
| T025 | Abstract miniature-model completeness must be tested |
| T026 | Physical-object inventory must be complete and unique |

## Certification/governance failures — T027–T031

| ID | Invariant |
|---|---|
| T027 | Persistent corpus IDs and executable regression IDs must agree |
| T028 | Declared certification count must equal executable count |
| T029 | Certifier and persisted-report schema must agree |
| T030 | Returned certification and persisted certification must not diverge |
| T031 | Integrity manifest must be hash-verified, not merely loaded |

## Advanced equation / metadata / runtime failures — T032–T038

| ID | Invariant |
|---|---|
| T032 | Reference-anchored/non-text equation recovery must never masquerade as exact formula extraction |
| T033 | Deterministic contact/publisher/affiliation boilerplate must be excluded before/through claim construction |
| T034 | Punctuation-ended equation-reference transformations must not fail because of invalid trailing word-boundary logic |
| T035 | Affiliation detection must tolerate detached/fragmented affiliation markers |
| T036 | Metadata exclusion must be rechecked at every representation boundary: line → block → sentence → clause |
| T037 | Every executable regression must be dependency-closed; master tests cannot call private helpers from another runtime |
| T038 | Semantic transformation classification must remain stable when citation suffixes attach directly to equation references, e.g. `Eq. (2)90.` |

## Orchestration — T039

| ID | Invariant |
|---|---|
| T039 | Cross-component contracts are validated in native schemas and normalized only at orchestration boundaries |

## Current NUS-48 executable allocation

### Paper-level master

```text
T001–T026
T032–T038
= 33 executable master regressions
```

### Independent certifier

```text
SG001–SG024
= 24 independent certification gates
```

### Orchestration

```text
1 cross-component contract gate
```

### Final V8 total

```text
33 + 24 + 1 = 58/58 PASS
```

## Failure-promotion rule

A new regression is justified only if the observed issue is a **genuinely new general failure class**. A deeper instance of an existing invariant should strengthen the existing test/implementation rather than create duplicate regression IDs.

## Architectural lessons encoded by the corpus

1. `PDF text layer ≠ rendered PDF object`.
2. `Equation existence ≠ exact formula recovery`.
3. Citation IDs can attach directly to equation syntax and must remain separate from quantities.
4. Metadata can emerge after representation transformations, not only in raw lines.
5. Cleaner extraction can expose hidden semantic-classification defects; all semantic regressions must rerun after extraction changes.
6. Primary-harness PASS is insufficient; independent certification is mandatory.
7. JavaScript syntax validity does not prove runtime dependency closure.
8. Similar field names across components are not the same interface contract.
9. Fail-closed behavior is a feature, not a defect.
