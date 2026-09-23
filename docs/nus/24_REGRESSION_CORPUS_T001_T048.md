# Permanent Regression Knowledge — T001–T048

This is the successor to the T001–T047 archive. Definitions T001–T047 remain frozen as previously recorded.

## T048 — Async Zotero collection/runtime contract

### Trigger

During the NUS-18 read-only identity locator, the runtime failed with:

```text
TypeError: all.filter is not a function
```

The locator had called:

```text
Zotero.Items.getAll(...)
```

without awaiting its asynchronous return before applying `.filter()`.

### Permanent invariant

```text
Any Zotero API that may return a Promise must be awaited before filtering,
iteration, array assertions, field access, or downstream structural logic.
```

After resolution, the value must be explicitly type-validated before collection operations.

### Positive control

```text
const all = await Zotero.Items.getAll(...)
assert Array.isArray(all)
all.filter(...)
```

### Negative control

```text
const all = Zotero.Items.getAll(...)
all.filter(...)
```

must be rejected by static/runtime contract validation.

### Scope

T048 is a runtime/API-contract control. It does not alter scientific adjudication, focality, ontology, physical-surface semantics, or final evidence.

## Current permanent boundary

```text
T001 → T048
```

## Engine authority

T048 is incorporated into:

```text
NUS Evidence Engine V1.0.1
```

with release controls:

```text
19/19 static checks PASS
0 failures
```

Package SHA-256:

```text
2ca74e7e99b3862e54d626ea90f37f9011112c1a08c0d77a5cdd9c9dfed74ee6
```

Freeze-manifest SHA-256:

```text
9d09ae86a416cdabbd7b0c8bc9c7a165c34b7329837cb360f7427ccc41c6df2b
```

## Promotion rule beyond T048

A future T049+ regression requires:

```text
new observed failure
→ failure not already covered by T001–T048
→ paper-independent invariant
→ reproducible regression
→ historical calibration retest
→ controlled engine successor
```
