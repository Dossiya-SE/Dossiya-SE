# T050 Candidate — Immutable Authority Dependency Closure

## Status

```text
CANDIDATE_REGRESSION_PENDING_RUNTIME_CONFIRMATION
```

## First observed failure

NUS-18 Reader exactness/geometry runtime V1 stopped safely with:

```text
FAIL:APPROVAL_FILE_MISSING
zotero_mutation_performed = false
pdf_mutation_performed = false
mutation_authorized = false
```

The scientific approval itself was already valid and frozen. The failure was caused only by requiring a duplicate approval JSON file to be manually present in Zotero Downloads.

## Candidate invariant

A downstream authorized runtime must prove availability of every immutable authority before source processing. A previously approved immutable authority may be embedded byte-for-byte with its frozen SHA-256; any external duplicate is optional but, if present, must hash-match exactly.

## NUS-18 repair

```text
Runtime: NUS18_READER_EXACTNESS_GEOMETRY_CONTEXT_V1R1.txt
SHA-256: 7e54714054eb7f0d67ca9a67a5b1c280e746bbfde61177997e7e1dda483cec4c
Static validation: 13/13 PASS
```

Frozen approval authority:

```text
NUS18_HUMAN_SCIENTIFIC_APPROVAL_V1.json
SHA-256: de5f1fbbaf07f9cf21e1f396f36d29d505dde89b4012088b188ff6501ed518d4
```

V1R1 embeds those exact approval bytes and verifies the embedded SHA-256 before Reader processing. If an external approval copy is present, it is cross-checked and must match the same hash. The Phase-1 page-lines artifact remains a required source-data dependency.

## Mutation boundary

The repair does not alter scientific adjudication, role ontology, geometry logic, source identity, PDF hash, annotation baseline, or mutation authorization. It adds no annotation creation/deletion/save/PDF-write path.

## Promotion rule

Do not add T050 to the permanent regression corpus yet. Promote only after V1R1 passes runtime controls and the dependency-closure invariant is confirmed as generic rather than paper-specific.
