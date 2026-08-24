# Frozen-37 Annotation Registry V1

## Purpose

This registry preserves the annotation-level state of the NUS Frozen-37 corpus without conflating current native annotations, human-approved proposed records, and historical/provisional evidence seeds.

## Current authority boundary

| Paper / scope | State | Count | Meaning |
| --- | --- | ---: | --- |
| NUS-172 | `CURRENT_GOLD_NATIVE` | 31 | Closed gold native annotations. Preserve the approved paper-specific comment convention. |
| NUS-48 | `CURRENT_FROZEN_NATIVE` | 33 | Frozen native Output-Nature V2 annotations: 20 highlights + 13 regions; tags = 0. |
| NUS-18 | `HUMAN_APPROVED_PREGEOMETRY_PROPOSED_NOT_NATIVE` | 25 | Scientific content approved, but page-label authority, exact geometry, final redundancy and final schema remain open. No native write is authorized. |
| Frozen-37 source seeds | `HISTORICAL_OR_PROVISIONAL_SEED` or current-support seed | 39 | Recall/provenance layer only; these are not additional current native annotations. |

Current native total = **64**. Human-approved proposed NUS-18 records = **25**. The two categories must never be added together and described as 89 native annotations.

## Machine annotation registries

- `machine/nus172_current_gold_annotations_v1.json`
  - 31 records
  - SHA-256 `da5ecb9a684bff3d99f25b260c451f2aa364dffaf4748c69bafd0b2f404ad938`
- `machine/nus48_current_frozen_annotations_v1.json`
  - 33 records
  - SHA-256 `d0f2935ef0afb9d50b03985dbcffd359d3ede387bedac32db7a1c3cae4e0cfad`
- `machine/nus18_approved_proposed_annotations_v1.json`
  - 25 records
  - SHA-256 `b563296f8c1a76b2ab29510f9a59496dcb5b0ce0ffdd91c84d937529eb956655`
- `machine/frozen37_annotation_paper_summary_v1.json`
  - 37 paper status records
  - SHA-256 `00d91dcd79347c8f979e80542e2845ba4747eedcf6382f6b6deae32ba4c240a9`
- `machine/frozen37_annotation_registry_v1_compact_manifest.json`
  - registry manifest and exact artifact hashes.

## Full session artifacts

- `NUS_FROZEN37_ANNOTATION_REGISTRY_V1.json`
  - SHA-256 `deffeb6db78cb8527d4b9191a644d8b95e66b9c4b46a6469c8c6f5b68496ee3c`
- `NUS_FROZEN37_ANNOTATION_REGISTRY_V1.xlsx`
  - SHA-256 `1cb311127528f0bea815e89e16ad84d8c3b005e39083c97c5829e4395f90cdc1`

The connected GitHub contents interface stores the compact UTF-8 machine registries directly. The XLSX binary remains hash-locked as a session artifact rather than silently transformed.

## Role distributions

### NUS-172 — 31 current gold native

- PURPOSE 1
- INTERVENTION 3
- INPUT 4
- ENGINEERING_METHOD 7
- ENGINEERING_OUTPUT 5
- SUSTAINABILITY_TRANSFORMATION 1
- SUSTAINABILITY_METHOD 5
- SUSTAINABLE_OUTCOME 4
- DECISION 1

### NUS-48 — 33 current frozen native

- PURPOSE 1
- INTERVENTION 4
- INPUT 3
- ENGINEERING_METHOD 6
- ENGINEERING_OUTPUT 6
- SUSTAINABILITY_TRANSFORMATION 3
- SUSTAINABILITY_METHOD 2
- SUSTAINABLE_OUTCOME 7
- DECISION 1

All six NUS-48 engineering outputs have nature `mechanical`. Sustainable outcomes are environmental = 4, economic = 3, social = 0, integrated = 0.

### NUS-18 — 25 human-approved proposed, not native

- PURPOSE 2
- INTERVENTION 1
- INPUT 1
- ENGINEERING_METHOD 2
- ENGINEERING_OUTPUT 2 (`energy`)
- SUSTAINABILITY_TRANSFORMATION 4
- SUSTAINABILITY_METHOD 7
- SUSTAINABLE_OUTCOME 4 (`environmental`)
- DECISION 2

NUS-18 remains blocked by T051 page-label authority and geometry. `mutation_authorized = false`.

## Project-memory semantics

This GitHub registry is the durable project-memory artifact for future NUS work. It records the annotation identities and authority states in version control. No separate ChatGPT persistent-memory write is represented or claimed by this commit.

## Scientific invariants

`INPUT <= USED_IN_FOCAL_METHOD`

`P + S != P -> S`

`P -> S <= EXPLICIT_TRANSFORMATION`

`ENV + ECO + SOC != INT`

Historical/provisional evidence must never silently override current adjudication. Unsupported fields remain unresolved/abstained rather than inferred.

## Mutation status

This registry task performs no Zotero or PDF mutation and does not authorize a new native write.