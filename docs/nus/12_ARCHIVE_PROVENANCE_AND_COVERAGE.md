# Archive Provenance and Coverage

## Purpose

This record explains what the GitHub NUS archive preserves and what remains outside GitHub so future work does not confuse a structured research-history archive with the original evidence objects.

## Included in this GitHub archive

The archive consolidates the NUS Frozen-37 project information established through 2026-08-24, including:

- canonical 37-paper processing order;
- Layer 1 / Layer 2 split;
- NUS-172 reference/calibration history;
- NUS-48 immutable identity;
- frozen scientific ontology;
- focality/provenance/citation-scope rules;
- Zotero role/color/exact-wording/zero-tag standard;
- NUS-48 physical-surface inventory;
- NUS-48 development chronology from initial extraction through V8;
- S001–S013 scientific defect history;
- T001–T039 permanent regression knowledge;
- independent-certification architecture;
- Eq. 2 exactness/visual-review rule;
- metadata/front-matter failure history;
- runtime dependency-closure failure history;
- cross-component contract-normalization failure history;
- `58/58 PASS` historical premutation state;
- automated scientific adjudication over 426 claims, 11 abstract claims, and 34 surfaces;
- three preserved author inconsistencies IC001–IC003;
- 24 text + 31 region automated candidate state;
- T040 candidate generic-engine lesson;
- later declared NUS-48 state of 33 native Zotero annotations;
- output-only nature comment schema V3;
- migration boundary for existing NUS-48 comments;
- mutation-authorization equation and release state machine;
- generic NUS Evidence Engine scaling strategy;
- known artifact filenames and SHA-256 values;
- human-review provenance record.

## Layered authorities and historical states

The archive does not flatten different stages into one status.

### Historical premutation authority

```text
NUS48_ONESHOT_PREMUTATION_READINESS_V8
PASS_PREMUTATION_READY_FOR_SCIENTIFIC_ADJUDICATION
58/58 PASS
live_annotation_count = 0
```

This is the authoritative premutation baseline.

### Automated scientific adjudication authority

```text
NUS48_AUTOMATED_SCIENTIFIC_ADJUDICATION_V1
PASS_AUTOMATED_SCIENTIFIC_ADJUDICATION_READY_FOR_HUMAN_REVIEW
```

### Later native-annotation source-state update

A later project update declares:

```text
NUS-48 native annotations = 33
written under then-authorized frozen schema
```

This state is recorded with provenance:

```text
USER_DECLARED_NOT_MACHINE_REVERIFIED_IN_THIS_UPDATE
```

The archive therefore preserves the chronology:

```text
0 annotations at premutation freeze
→ later 33 native annotations
```

without inventing the missing intermediate human-approval/writer/auditor records.

### Current generic visible-comment authority

```text
NUS_COMMENT_GENERATION_RULE_V3
```

Nature is visible only for:

```text
ENGINEERING_OUTPUT
SUSTAINABLE_OUTCOME
```

The earlier all-role-nature V2 proposal is retained as superseded history.

## Evidence that remains external to this documentation archive

This GitHub documentation does not itself contain or replace:

- the focal NUS-48 PDF bytes;
- the live Zotero database;
- a machine re-verification of the currently declared 33 native annotations;
- the explicit historical human-approval event that preceded the declared write, unless supplied later;
- the complete writer/auditor artifacts associated with the 33-annotation state, unless supplied later;
- every historical runtime/source file named in the hash ledger;
- every generated JSON report/bundle/manifest unless separately committed later;
- focal-PDF visual exactness evidence for Equation 2 unless supplied later;
- any future V3 comment-migration writer/auditor artifacts.

The known hashes in `10_ARTIFACT_HASH_LEDGER.md` provide identity anchors for external artifacts where hashes are available.

## Evidence-preservation rule

If a binary/runtime/report artifact is later committed, preserve its original filename and SHA-256 and do not overwrite historical versions. Use successor versions for corrections.

State transitions must also preserve earlier valid states. For example, the premutation `0 annotations` record must not be rewritten merely because 33 annotations now exist downstream.

## Current boundary

The archive now records:

```text
PREPROCESSING FREEZE = complete historically
AUTOMATED SCIENTIFIC ADJUDICATION = complete
NUS-48 NATIVE ANNOTATION STATE = 33 declared, not machine reverified in this update
COMMENT SCHEMA V3 = frozen for generic engine
V3 RETROFIT OF EXISTING NUS-48 COMMENTS = not authorized
T040 = candidate, not permanent
```

Two legitimate next paths remain:

```text
A. Preserve NUS-48 under prior authorized schema and use V3 from NUS-18 onward

B. Build, validate, authorize, execute, and independently audit a controlled NUS-48 V3 comment-only migration
```

Freezing V3 does not itself choose between A and B.
