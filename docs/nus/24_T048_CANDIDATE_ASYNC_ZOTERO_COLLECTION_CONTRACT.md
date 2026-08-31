# T048 Candidate — Async Zotero Collection Retrieval Contract

## Status

```text
CANDIDATE_REGRESSION
NOT_YET_PERMANENT
```

## Observed NUS-18 failure

The first NUS-18 read-only identity locator returned:

```text
protocol = NUS18_READONLY_IDENTITY_LOCATOR_V1
status = ABSTAIN_OR_FAIL
error = TypeError: all.filter is not a function
zotero_mutation_performed = false
pdf_mutation_performed = false
```

The locator source used:

```javascript
const all = Zotero.Items.getAll(LIB,false,false);
const parents = all.filter(...);
```

without resolving the asynchronous return value first.

## Failure class

```text
F2_RUNTIME_ASYNC_CONTRACT
```

This is not a NUS-18 scientific failure and not a PDF identity failure. It is a runtime/API-contract defect at the collection retrieval boundary.

## Candidate invariant

```text
Every Zotero API operation that may return a Promise must be awaited before array/object operations are applied.
The resolved value must then be explicitly type-validated before use.
```

For collection retrieval:

```text
await asynchronous Zotero call
→ verify expected resolved type
→ then filter/map/iterate
```

not:

```text
possibly asynchronous return value
→ Array.filter()
```

## Repair V1R1

The controlled repair:

- awaits `Zotero.Items.getAll(...)`;
- fails closed unless the resolved value is an array;
- uses `await Zotero.Items.getAsync(attachmentIDs)` for child attachments;
- type-validates the child collection;
- changes no scientific ontology, evidence logic, source PDF, or Zotero state.

## Promotion requirements

Promote T048 to permanent only after:

1. `NUS18_READONLY_IDENTITY_LOCATOR_V1R1` executes successfully;
2. identity/source-state output is scientifically coherent;
3. the repaired async/type contract is demonstrated as paper-independent;
4. NUS-172/NUS-48 runtime controls are reviewed for the same unsafe async pattern;
5. any generic repair passes historical regression controls;
6. Generic Engine V1 is advanced through a controlled successor if an engine code change is actually required.

Until then:

```text
T001–T047 = permanent frozen corpus
T048 = candidate discovered during NUS-18 generalization
```

## Anti-bespoke interpretation

This failure can justify a generic runtime-contract repair because it is independent of NUS-18 scientific content. It must not trigger paper-specific extraction or ontology code.
