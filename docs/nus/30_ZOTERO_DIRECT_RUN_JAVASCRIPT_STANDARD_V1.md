# Zotero Direct Run JavaScript Standard V1

## Status

```text
STANDARD_ID = NUS_ZOTERO_DIRECT_RUN_JAVASCRIPT_STANDARD_V1
STATUS      = FROZEN_REUSABLE_CODING_STANDARD
SCOPE       = NUS Frozen-37 and future Zotero Run JavaScript work
```

This is the canonical coding standard for every future Zotero script executed through:

```text
Tools
→ Developer
→ Run JavaScript
→ Run as async function
```

The governing design is:

```text
ONE self-contained direct JavaScript program
+ embedded immutable authority/configuration where practical
+ one mode selector
+ one target-paper selector
+ isolated native-annotation adapter
+ fail-closed gates
+ top-level await
+ explicit top-level return
+ deterministic rollback/audit
```

This standard replaces ad-hoc one-off Zotero scripts as the default NUS coding pattern.

---

## 1. Canonical architecture

The preferred end-state is one reusable engine:

```text
NUS_FROZEN37_DIRECT_RUN_V3
│
├── frozen 37-paper order
├── paper identities
├── current paper states
├── role/color ontology
├── output-nature ontology
├── evidence/focality/provenance rules
├── annotation schemas
├── source-map/page-label logic
├── Reader geometry functions
├── native annotation adapter
├── rollback ledger
├── internal zero-delta audit
├── standalone-style secondary audit
├── regression controls
└── execution MODE
```

The program must not require 37 different codebases. Scientific paper-specific content is data; generic behavior is code.

Desired engineering invariant:

```text
bespoke_code_change_count = 0
engine_files_changed       = 0
```

except for controlled paper-independent maintenance justified by a real general failure.

---

## 2. Supported execution modes

Every reusable direct runner should expose an explicit mode selector:

```javascript
const MODE = "STATUS";
const TARGET_PAPER_ID = 18;
```

Recommended modes:

```text
STATUS
DISCOVER
EXTRACT
ADJUDICATE_CHECK
GEOMETRY
PREFLIGHT
AUDIT
WRITE
FREEZE_CHECK
```

`WRITE_ALL` must remain fail-closed unless every paper in scope is independently mutation-ready.

---

## 3. Top-level Zotero Run JavaScript rule

Use top-level `await` and end with an explicit top-level `return`:

```javascript
const result = await run();
return JSON.stringify(result, null, 2);
```

Do not use an unawaited outer async IIFE such as:

```javascript
(async () => {
  // ...
})();
```

The Zotero runner already supplies the async execution context.

---

## 4. Async discipline

Any Zotero API that may return a Promise must be awaited before filtering, iteration, array assertions, or field access.

Canonical pattern:

```javascript
const annotations = await Promise.resolve(
  attachment.getAnnotations?.() || []
);

if (!Array.isArray(annotations)) {
  throw new Error("FAIL:ANNOTATION_COLLECTION_NOT_ARRAY");
}

const live = annotations.filter(a => a && !a.deleted);
```

Never consume a possibly asynchronous Zotero collection directly.

This is the permanent T048 rule.

---

## 5. Identity and source integrity first

Before any scientific extraction or mutation, verify:

```text
paper_id
parent_key
attachment_key
DOI/title when required
attachment-parent relationship
PDF file existence
PDF SHA-256
expected initial/live annotation state
```

Nothing downstream may compensate for an identity or PDF-hash failure.

---

## 6. Page-label authority

Store and distinguish:

```text
page_index
physical_page
authoritative_page_label
page_label_authority_mode
```

Never use a premature per-page fallback such as:

```javascript
view._pageLabels?.[pageIndex] || (pageIndex + 1)
```

Instead query complete-document authority:

```javascript
const labels = await PDFViewerApplication.pdfDocument.getPageLabels();
```

Allowed states:

```text
PDFJS_GETPAGELABELS_COMPLETE_ARRAY
PDFJS_GETPAGELABELS_NULL_NO_CUSTOM_LABELS
```

This is the T051 candidate learning and must remain fail-closed until promoted or superseded by controlled evidence.

---

## 7. Scientific annotation schema

Every final annotation record should support, as applicable:

```text
schema_id
record_id
paper_id
attachment_key
zotero_annotation_type
page_index
page_label
position.rects
sort_anchor_rects
exact_author_text
annotation_text
annotation_comment
annotation_color
role
output_nature
provenance
ontology_code
source_claim_ids
source_object_ids
annotation_tags = []
```

The native writer does not decide science. All role, nature, provenance, exact wording, geometry, and inclusion/redundancy decisions must be frozen before `WRITE`.

---

## 8. Roles and colors

```text
PURPOSE                        #6b7280
INTERVENTION                   #2ea8e5
INPUT                          #0072b2
ENGINEERING_METHOD             #a28ae5
ENGINEERING_OUTPUT             #5fb236
SUSTAINABILITY_TRANSFORMATION  #f19837
SUSTAINABILITY_METHOD          #e56eee
SUSTAINABLE_OUTCOME            #ff6666
DECISION                       #ffd400
```

Zotero annotation tags must remain exactly zero.

---

## 9. Visible comment generation

For non-output roles:

```text
Purpose : [exact author wording]
Intervention : [exact author wording]
Input : [exact author wording]
Engineering method : [exact author wording]
Sustainability transformation : [exact author wording]
Sustainability method : [exact author wording]
Decision : [exact author wording]
```

For outputs only:

```text
Engineering output here is [engineering nature] : [exact author wording]
Sustainability output here is [environmental/economic/social/integrated] : [exact author wording]
```

No paraphrase is allowed after the colon.

---

## 10. Output-nature rule

Controlled engineering natures currently include:

```text
mechanical
fresh-state
physical
durability
transport/permeability
thermal
structural/functional
fracture/damage
time-dependent
constructability/production
energy
```

Controlled sustainability natures:

```text
environmental
economic
social
integrated
```

Never coerce a legitimate output into the nearest existing nature. If no exact controlled nature fits, fail closed, adjudicate the new nature, version the ontology, and add a permanent regression before schema generation.

This is permanent T049.

---

## 11. Native Reader adapter isolation

Native PDF annotation creation uses a version-sensitive internal Reader adapter and must be isolated behind one capability-tested function.

Conceptual boundary:

```javascript
async function createNativeAnnotation(reader, record, sortIndex) {
  const manager = reader?._internalReader?._annotationManager;

  if (!manager || typeof manager.addAnnotation !== "function") {
    throw new Error("FAIL:NATIVE_ANNOTATION_API_UNAVAILABLE");
  }

  // construct exact payload
  // create annotation
  // return native ID
}
```

If Zotero changes this internal API, fail closed and modify only the adapter after controlled testing. Do not spread Reader-internal calls throughout the engine.

---

## 12. Transactional safety

Immediately after native creation returns an ID, register it in the rollback ledger before waiting for persistence or performing downstream validation.

```text
create
→ obtain native ID
→ register rollback identity immediately
→ wait for persistence
→ verify exact fields
→ continue
```

On any downstream failure:

```text
reverse(createdLedger)
→ eraseTx() each created annotation
→ report rollback result
→ stop
```

This is permanent T044.

---

## 13. Write authorization equation

Mutation is allowed only when all required gates are independently true:

```text
identity_pass
AND pdf_hash_pass
AND scientific_approval
AND surface_complete
AND page_label_authority
AND geometry_proven
AND final_schema_approval
AND writer_dryrun_pass
AND auditor_dryrun_pass
AND mutation_authorized
```

Human scientific approval and exact final-schema approval are separate gates.

A registry/inventory artifact never authorizes Zotero mutation by itself.

---

## 14. Idempotency and zero-delta

Two valid starting states exist:

```text
EMPTY       → CREATE
EXACT TARGET → ZERO_DELTA
```

Any other non-empty state fails closed unless a controlled migration protocol explicitly applies.

After writing, rerun target-state comparison. Required result:

```text
internal_second_pass_delta_count = 0
```

Then perform a separately implemented secondary audit.

---

## 15. PDF immutability

A native-annotation write must preserve the source PDF byte-for-byte.

Always verify:

```text
PDF_SHA_before == PDF_SHA_after == frozen_PDF_SHA
```

The direct runner must not write to the PDF path.

---

## 16. Source/surface/geometry rules

Raw discovery signals are not equivalent to reconciled physical objects.

```text
raw surface signal != physical scientific object
caption bbox != full figure/table region
```

Complete tables/figures/equations require deterministic/visual reconciliation and proven geometry before mutation.

For tables, preserve the T041 rule:

```text
final table geometry
= union(rendered-validated detector bbox, grid drawing extents, text extents)
```

Never invent geometry from a caption alone.

---

## 17. Scientific invariants that every direct runner must preserve

```text
FOCALITY_BEFORE_ROLE
INPUT <= USED_IN_FOCAL_METHOD
P + S != P→S
P→S <= EXPLICIT_TRANSFORMATION
ENV + ECO + SOC != INT
EXTERNAL -> reject
MIXED -> split or abstain
UNCLEAR -> abstain
Role != Nature != Metric != Result
```

Unsupported values remain null/ABSTAIN rather than inferred.

---

## 18. Frozen-37 current mutation boundary

Current corpus state:

```text
NUS-172  31 native annotations  → ZERO_DELTA / AUDIT ONLY
NUS-48   33 native annotations  → ZERO_DELTA / AUDIT ONLY
NUS-18   25 human-approved proposed records → WRITE FORBIDDEN until T051 + geometry + final schema
Remaining 34 → WRITE FORBIDDEN until current-engine re-extraction/adjudication
```

A corpus-wide write must currently fail closed with zero new annotations.

---

## 19. Reuse rule for future code generation

Whenever a new Zotero Run JavaScript script is designed for this NUS project, use this standard as the default governing contract.

The script should explicitly state:

```text
Conforms to: NUS_ZOTERO_DIRECT_RUN_JAVASCRIPT_STANDARD_V1
```

and must not weaken a frozen invariant silently.

If a real runtime failure exposes a general defect:

```text
observed failure
→ root cause
→ paper-independent invariant
→ regression
→ historical calibration retest
→ controlled engine successor
```

Do not patch one paper locally unless the difference is genuinely scientific data rather than engine behavior.

---

## 20. Recommended reusable header

```javascript
/*
Conforms to: NUS_ZOTERO_DIRECT_RUN_JAVASCRIPT_STANDARD_V1
Execution: Tools -> Developer -> Run JavaScript -> Run as async function
Outer async IIFE: forbidden
Top-level await: allowed
Top-level return: required
Mutation default: false
Fail-closed: required
*/

const MODE = "STATUS";
const TARGET_PAPER_ID = null;
```

This header should appear in future NUS Run JavaScript programs unless a controlled successor standard explicitly replaces V1.
