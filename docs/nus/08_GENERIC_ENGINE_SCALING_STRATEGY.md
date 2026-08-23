# Generic NUS Evidence Engine Scaling Strategy

## Objective

The heavy NUS-48 development cost is acceptable only because it is being converted into reusable engine knowledge. It must not become the normal processing cost for each remaining paper.

Target manual workflow:

```text
PDF
→ one master execution
→ automatic regression/certification
→ candidate evidence manifest
→ scientific adjudication
→ one explicit human approval
→ transactional Zotero write
→ audit
```

Manual effort should not scale linearly with regression count.

## Desired asymptotic behavior

```text
Assurance_n ↑
ManualExecutionSteps_n ≈ constant
BespokeCodeChanges_n → 0
```

A new paper must normally change only identity/configuration, not engine code.

## Minimal paper interface

Target configuration:

```json
{
  "paper_id": 48,
  "parent_key": "LYG93FY6",
  "attachment_key": "3UL86A9R",
  "expected_pdf_sha256": "bd27b10cb8110d7a48a0b28923e3e0cc2adc0fb2d7e416fb25714f8483db3609"
}
```

For NUS-18, NUS-191, NUS-67, etc., these paper-identity fields should normally be the only changes required to execute the engine.

## Target generic architecture

```text
NUS_EVIDENCE_ENGINE/
├── config/
├── contracts/
├── governance/
├── regression/
├── engine/
│   ├── identity/
│   ├── extraction/
│   ├── segmentation/
│   ├── citation_scope/
│   ├── focality/
│   ├── surface_inventory/
│   ├── evidence_architecture/
│   ├── transformation_engine/
│   ├── schema_validation/
│   ├── geometry/
│   ├── writer/
│   └── auditor/
└── outputs/
```

## Paper output tree

```text
PAPER_<ID>/
├── identity.json
├── source_map.json
├── atomic_claims.json
├── surface_inventory.json
├── abstract_body_crosscheck.json
├── evidence_manifest.json
├── surface_adjudication.json
├── transformation_ledger.json
├── premutation_report.json
├── writer_report.json
├── auditor_report.json
└── freeze_manifest.json
```

## Genericity rule

For NUS-18 onward:

```text
new paper ≠ new methodology
```

and:

```text
new bespoke code
→ must be justified by a demonstrated new general failure class
```

Different titles, values, methods, figure counts, journal layouts, or scientific conclusions are not sufficient reasons for bespoke software.

## Calibration programme

| Paper | Role |
|---|---|
| NUS-172 | first reference architecture |
| NUS-48 | major hardening/final heavy stress test |
| NUS-18 | generalization test 1 |
| NUS-191 | generalization test 2 |
| NUS-67 | final generalization test |
| NUS-15 onward | production operation |

A successful generalization test requires both:

```text
scientifically correct result
+ no bespoke pipeline redesign
```

## Efficiency metrics

For paper `i`, track at least:

```text
E_i = (
  T_manual,
  N_manual_actions,
  N_new_defects,
  N_new_regressions,
  N_bespoke_code_changes
)
```

The most important scaling indicator is:

```text
N_bespoke_code_changes → 0
```

while assurance and scientific traceability remain constant or improve.

## Safe automatic exclusions

Human adjudication should focus on scientifically necessary ambiguity, not obvious noise. The engine may safely exclude deterministic structural material such as:

```text
References
bibliographic metadata
Keywords
publisher/page furniture
contact/affiliation boilerplate
duplicates
empty/formatting artifacts
```

But it must not automatically discard `MIXED`, `UNCLEAR`, or scientifically ambiguous evidence.

## Scientific-attention funnel

```text
all extracted content
→ deterministic structural exclusions
→ deduplication
→ focality/citation candidate screening
→ scientific candidate set
→ human/scientific adjudication
→ final evidence set
```

`N_final` is always derived from evidence and is never predetermined.

## Engine-change stop rule

After NUS-48 V8, preprocessing is frozen. A new preprocessing change is allowed only by:

```text
new observed failure
→ general invariant
→ permanent regression
→ historical retest
```

Implementation preference alone is insufficient.
