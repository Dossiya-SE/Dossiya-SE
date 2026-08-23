# NUS-18 T051 Candidate — Page-Label Authority Initialization

## Observed failure

```text
NUS18_READER_EXACTNESS_GEOMETRY_CONTEXT_V1R1
FAIL:LIVE_READER_PAGE_LABEL_MISMATCH
record_id = E001
page_index = 2
Phase-1/approved label = 3
live Reader label = 91
```

No Zotero or PDF mutation occurred.

## Diagnosis

Phase-1 discovery persisted page labels using a per-page cache expression equivalent to:

```js
view._pageLabels?.[pageIndex] || (pageIndex + 1)
```

This can silently substitute the physical page number before the complete document page-label metadata has initialized. The earlier observed sequence `1..8 -> 97..104` is therefore not authoritative unless independently reproduced from the document-level page-label API.

## T051 candidate invariant

Page-label authority must be obtained for the complete PDF document before any page labels are persisted. A missing per-page Reader cache entry must never silently become a physical page number while document page-label metadata may still exist.

Allowed cases:

```text
PDF.js getPageLabels() returns complete array -> persist exact array
PDF.js getPageLabels() returns null           -> explicitly record NO_CUSTOM_PAGE_LABELS and use physical 1..N
```

Forbidden case:

```text
per-page cache missing -> silently use pageIndex + 1
```

## Current gate

```text
geometry = BLOCKED_PENDING_PAGE_LABEL_AUTHORITY_RECONCILIATION
mutation_authorized = false
```

The approved scientific adjudication remains intact, but HR18-008 page-label metadata must be corrected if the all-page audit confirms the defect.

## Repair runtime

```text
NUS18_PAGE_LABEL_AUTHORITY_AUDIT_AND_PHASE1_REPAIR_V1.txt
SHA-256: 13c758d8df57528178157f56ad54b6ff7c0f2aa016eee08eb5b79cd6af4063af
```

The runtime creates a successor `NUS18_GENERIC_PHASE1_PAGE_LINES_V1R1.json`; it does not overwrite the frozen Phase-1 artifact and asserts that no text/line-geometry content changes.