# NUS-18 Dry-Run Runtime Compliance V1R4

## Status

NUS-18 final scientific target remains frozen and unchanged:

- Schema: `NUS18_FINAL_ZOTERO_TARGET_SCHEMA_V1`
- Schema SHA-256: `d033b1be1c61ccb8ac6e5c39b4ffa11c03fd78f8bc7b68770616437d9d61fb30`
- Target annotations: 25 = 16 highlights + 9 regions
- Human approval SHA-256: `70bbe412522f3bfa268bca18a0b16e44965f7ea0293423acb923633a03a25172`
- Mutation authorization: **false**

## Observed results

The writer dry-run V1R1 failed before record evaluation with `EMBEDDED_SCHEMA_SHA_MISMATCH`: expected the approved schema SHA `d033...`, but the runtime embedded bytes hashed to `2ce300...`. Root cause: a compatibility repair altered filenames inside the immutable embedded schema authority.

The independent auditor V1R3 produced strong scientific/geometry evidence: live PDF SHA matched, live native annotation count remained zero, 25/25 records passed, 16 highlights passed geometry-first reconstruction, 9 regions passed, four frozen figure crop SHA-256 values were reproduced, and the writer plan was not consumed. However, V1R3 is not accepted as the final DA gate because its implementation still consumes potentially asynchronous Zotero APIs without T048 await/type discipline and still uses Reader `_pageLabels` cache rather than complete-document T051 authority.

## Controlled successor

A V1R4 runtime-compliance successor builder was created with these constraints:

1. Start writer from byte-correct V1R2.
2. Start independent auditor from scientifically successful V1R3, preserving the spatially scoped region-anchor fix.
3. Protect `EMBEDDED_SCHEMA_RAW` and `EMBEDDED_APPROVAL_RAW` declarations from all runtime source edits.
4. Require byte-identical authority declarations before/after maintenance and recompute the frozen authority SHA-256 values.
5. Apply T048: await possible-Promise item/annotation APIs before consumption and assert annotation collection is an array.
6. Apply T051: use `PDFViewerApplication.pdfDocument.getPageLabels()` once for complete-document page-label authority; Reader `_pageLabels` is forbidden as authority.
7. If `getPageLabels()` returns null, explicitly classify `PDFJS_GETPAGELABELS_NULL_NO_CUSTOM_LABELS`; no silent per-page fallback.
8. Preserve zero mutation APIs and mutation authorization false.
9. Run writer V1R4 first; only if it passes, run independent auditor V1R4.

## T052 candidate

Candidate invariant: **immutable embedded authority byte preservation under runtime maintenance**.

> Runtime compatibility or maintenance patches must operate outside immutable embedded authority literals. Embedded schema and approval declarations must be protected from edits and byte-identical before/after maintenance; frozen SHA-256 values must recompute exactly. Any authority-byte change is a hard failure requiring a new authority version, not a runtime patch.

T052 remains candidate-only until V1R4 dry-runs pass and historical NUS-172/NUS-48 calibration retesting confirms the invariant generalizes without regression.

## Current gate

```text
Final schema approval        PASS
Writer dry-run               PENDING V1R4
Independent auditor dry-run  PENDING V1R4 runtime-compliant rerun
Mutation authorization       FALSE
Zotero mutation              FORBIDDEN
```
