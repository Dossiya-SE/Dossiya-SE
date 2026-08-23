# NUS-18 — Generalization Test #1 Phase 1 PASS

## Result

```text
protocol = NUS_GENERIC_READONLY_DISCOVERY_V1
status = PASS_READ_ONLY_DISCOVERY
```

## Frozen identity

```text
Paper ID       18
Parent key     BZZGBD2I
Attachment     Z8UEF2GH
DOI            10.1016/j.buildenv.2014.10.013
PDF SHA-256    826beba0d3973661137328c8d68ac992a8d03fa91860d69ee8c1c196010c3839
Annotations    0
```

## Whole-PDF discovery

```text
Page count              16
Total extracted lines   1466
Surface anchors          22
```

Phase-1 page-line artifact:

```text
NUS18_GENERIC_PHASE1_PAGE_LINES_V1.json
SHA-256:
649705ed0423bbed4835de10479e3fa63c3c37428e980cc273c62c5fa8bc3b86
```

Discovery report:

```text
NUS18_GENERIC_READONLY_DISCOVERY_V1.json
SHA-256:
c8a0d3de9e27b04a2e53225ea6710cef072b0339c7d1b61fecf1fb1932c08258
```

## Discovery proofs

The returned runtime proved:

```text
identity_components_verified = true
all_pages_basic_data_loaded = true
reader_bridge_pass = true
pdf_is_source_of_truth = true
references_hard_boundary_capability = true
surface_detection_structurally_anchored = true
zotero_run_uses_harness_native_top_level_async_contract = true
embedded_json_single_serialization_boundary_and_type_assertion = true
```

No source-state mutation occurred:

```text
zotero_mutation_performed = false
pdf_mutation_performed = false
```

## Important source observations

### References boundary

The discovery found the hard References boundary at:

```text
page_index = 14
page_label = 103
line_index = 36
```

### Page labels

Page labels are source metadata, not values to be normalized by the engine. The extracted sequence includes a transition from page label `8` to `97` and then continues `98`, `99`, `100`, `101`, etc.

The engine must preserve these labels exactly and keep them separate from internal zero-based page indices.

### Surface anchors are not final physical-object counts

The 22 discovery anchors include both true captions/headings and prose surface references, for example a prose line referring to Fig. 7 plus the actual Fig. 7 caption.

Therefore:

```text
22 discovery anchors ≠ final surface-object count
```

Phase 2 must deduplicate tables/figures by structural caption identity and conservatively recover equation objects.

## Generalization metric so far

```text
bespoke engine changes caused by NUS-18 scientific structure = 0
```

The only maintenance change before this run was T048, a generic Zotero asynchronous-runtime contract defect discovered in the identity locator and frozen into Engine V1.0.1.

## Next gate

```text
Phase 1 source map
→ generic atomic claims
→ deduplicated all-surface candidate inventory
→ scientific adjudication
```

No final scientific role and no Zotero annotation is authorized at this stage.
