# NUS-172 Calibration History

## Role in the programme

`NUS-172` was the first rigorous calibration/reference paper for the Frozen-37 workflow. It established the initial Zotero annotation architecture and demonstrated the need to separate visible human-readable annotations from the external machine/audit ledger.

**Title:** *Age dependent properties of concrete incorporating mechanically processed ultra-fine sugarcane bagasse ash*  
**DOI:** `10.1016/j.conbuildmat.2025.143509`

## Historical V1 state

The first human-reviewed NUS-172 baseline contained **31 annotations**, with:

- preserved annotation keys and geometries;
- role colors;
- zero annotation tags;
- independent audit PASS.

That historical V1 is evidence history and must not be overwritten.

## Visible-comment standard strengthened after V1

The final visible comment contract became:

```text
short semantic label + ": " + exact author wording
```

The earlier NUS-172 comments that used paraphrased wording therefore require re-audit/conversion before any final V2 freeze. This is a visible-state quality correction, not permission to destroy the historical V1 record.

## New explicit PURPOSE evidence discovered for V2

A later source review identified an explicit objectives passage:

> The specific objectives of the study are: (i) to investigate the effect of SCBA on compressive, tensile, and flexural strengths of concrete over time; (ii) to assess long-term sulphate resistance through weight loss, strength loss, length expansion, and microstructural changes; and (iii) to quantify the environmental benefits in terms of embodied energy, global warming potential (GWP), and sustainability index (Si).

This creates a planned additional `PURPOSE` annotation for NUS-172 V2.

## Planned V2 role distribution

The planned NUS-172 V2 state contains **32 annotations**:

| Role | Count |
|---|---:|
| PURPOSE | 2 |
| INTERVENTION | 3 |
| INPUT | 4 |
| ENGINEERING_METHOD | 7 |
| ENGINEERING_OUTPUT | 5 |
| SUSTAINABILITY_TRANSFORMATION | 1 |
| SUSTAINABILITY_METHOD | 5 |
| SUSTAINABLE_OUTCOME | 4 |
| DECISION | 1 |
| **Total** | **32** |

The count is descriptive of the planned calibrated state, not a generic preset annotation count for later papers.

## Transferable lessons from NUS-172

1. Exact source wording must remain visible after the semantic label.
2. Visible Zotero comments should remain concise; provenance/audit metadata belongs externally.
3. Annotation tags remain zero.
4. A gold/reference paper is useful for calibration but must not impose its scientific semantics on later papers.
5. Historical states must be preserved rather than overwritten.
6. Human approval is distinct from automated validation.

## Relationship to NUS-48

NUS-172 established the first architecture. NUS-48 was deliberately selected as a substantially different stress test to determine whether the system could generalize across abstract structure, RSM, sustainability equations, physical surfaces, metadata contamination, and independent certification.

The generic engine must preserve lessons from both papers without encoding either paper's expected conclusions into reusable logic.
