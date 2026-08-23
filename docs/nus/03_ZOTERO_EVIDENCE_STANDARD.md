# Zotero Evidence Standard

## Visible annotation state

The frozen visible Zotero annotation standard is:

```text
exact highlight/region
+ unique top-level role color
+ short semantic label + ": " + exact author wording
+ zero annotation tags
```

The text after the colon must be author-verbatim. Do not paraphrase, summarize, grammar-correct, normalize terminology, normalize units, infer missing words, or silently repair contradictions.

## Top-level roles and colors

| Role | Color |
|---|---|
| PURPOSE | `#6b7280` |
| INTERVENTION | `#2ea8e5` |
| INPUT | `#0072b2` |
| ENGINEERING_METHOD | `#a28ae5` |
| ENGINEERING_OUTPUT | `#5fb236` |
| SUSTAINABILITY_TRANSFORMATION | `#f19837` |
| SUSTAINABILITY_METHOD | `#e56eee` |
| SUSTAINABLE_OUTCOME | `#ff6666` |
| DECISION | `#ffd400` |

## Visible semantic labels

```text
Purpose:
Intervention:
Design choice:
Input:
Engineering method:
Engineering output:
Sustainability transformation:
Sustainability method:
Environmental sustainability outcome:
Economic sustainability outcome:
Social sustainability outcome:
Integrated sustainability outcome:
Decision:
```

`Design choice:` uses the `INTERVENTION` top-level color but distinguishes comparative/selected alternatives, levels, configurations, geometries, strategies, or design variables from an intervention that authors introduce/apply/modify/replace/substitute/process/treat.

## INTERVENTION convention

Use exactly:

```text
Intervention: [exact author wording]
```

when focal authors introduce, substitute, modify, treat, or apply something.

Use:

```text
Design choice: [exact author wording]
```

when focal authors select/compare alternatives, levels, configurations, geometries, strategies, or design variables.

## Machine metadata

Detailed machine/reviewer metadata does **not** belong in the visible Zotero comment. It belongs in the external evidence ledger/repository, including:

- paper ID;
- source hash;
- claim IDs;
- source-object IDs;
- focality;
- citation scope;
- provenance;
- ontology codes;
- adjudication history;
- transformation lineage;
- geometry proof;
- writer/auditor state;
- freeze hashes.

## Mutation rule

No annotation may be created merely because a preprocessing or regression test passes. Mutation is authorized only after the full scientific/human/geometry/schema/dry-run authorization equation is true.

## Idempotence requirement

The eventual transactional writer must satisfy:

```text
Z0 → Z1
Z1 → Z1
```

on a second run. Any non-zero delta on the second writer run blocks freeze.
