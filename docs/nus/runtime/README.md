# NUS Zotero Run JavaScript Runtime

This directory is the reusable entry point for future NUS Zotero code executed through:

```text
Tools -> Developer -> Run JavaScript -> Run as async function
```

## Governing standard

- [`../30_ZOTERO_DIRECT_RUN_JAVASCRIPT_STANDARD_V1.md`](../30_ZOTERO_DIRECT_RUN_JAVASCRIPT_STANDARD_V1.md)
- Machine policy: [`../machine/zotero_direct_run_javascript_standard_v1.json`](../machine/zotero_direct_run_javascript_standard_v1.json)
- Reusable code template: [`NUS_ZOTERO_DIRECT_RUN_TEMPLATE_V1.txt`](NUS_ZOTERO_DIRECT_RUN_TEMPLATE_V1.txt)

## Default rule for future code

Whenever a new NUS Zotero Run JavaScript program is written, begin from the reusable template and include:

```text
Conforms to: NUS_ZOTERO_DIRECT_RUN_JAVASCRIPT_STANDARD_V1
```

Do not create a separate ad-hoc architecture unless a controlled successor standard explicitly requires it.

Generic behavior belongs in the reusable engine. Paper-specific identity, scientific evidence, roles, nature, geometry, and final schema are data.

## Required execution properties

```text
top-level await                  required/allowed
explicit top-level return        required
outer async IIFE                 forbidden
mutation default                 false
fail-closed                      required
possible Promise consumption     await first
PDF SHA-256 lock                 required
complete-document page labels    required
per-page label fallback          forbidden
annotation tags                  exactly 0
native Reader adapter            isolated
rollback registration            immediate after native creation
PDF bytes                        immutable
zero-delta second pass           required after write
secondary independent audit      required after write
```

## Frozen-37 current writing boundary

```text
NUS-172: 31 native current -> ZERO_DELTA / AUDIT only
NUS-48:  33 native current -> ZERO_DELTA / AUDIT only
NUS-18:  25 approved proposed -> WRITE FORBIDDEN until T051 + geometry + final schema
Remaining 34 -> WRITE FORBIDDEN until current-engine re-extraction/adjudication
```

## Failure-learning rule

```text
observed failure
-> root cause
-> paper-independent invariant
-> regression
-> historical calibration retest
-> controlled engine successor
```

Never silently weaken a frozen invariant to make one paper pass.
