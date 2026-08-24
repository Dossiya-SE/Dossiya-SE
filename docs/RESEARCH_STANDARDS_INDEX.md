# Research Standards Index

This repository uses a layered research-governance architecture. The layers are complementary; lower layers may add stricter controls but must not silently weaken higher applicable requirements.

## 1. Upstream research-design standard

**[Scientific Research Architecture V1.0](SCIENTIFIC_RESEARCH_ARCHITECTURE_V1.md)**  
Governs problem definition, gap architecture, research questions, contribution classes, system definition, mathematical modeling, provenance, numerical methods, verification, calibration, validation, sensitivity, uncertainty, industrial relevance, limitations, bounded conclusions, and reproducibility.

**[Scientific Research Architecture Audit Checklist](SCIENTIFIC_RESEARCH_ARCHITECTURE_CHECKLIST.md)**  
Operational pre-freeze gate for papers, theses, computational models, simulation studies, and industrially motivated research.

## 2. Quantitative reporting standard

**[APA JARS–Quant Adapted Reporting Standard](APA_JARS_QUANT_ADAPTED_REPORTING_STANDARD.md)**  
Governs quantitative reporting structure, claim classes, methods disclosure, diagnostics, uncertainty, figures/tables, discussion, limitations, and reproducibility.

**[APA JARS–Quant Final Report Checklist](APA_JARS_QUANT_REPORT_CHECKLIST.md)**  
Final report audit before release.

**[Quantitative Research Report Template](QUANTITATIVE_REPORT_TEMPLATE.md)**  
Writing scaffold for quantitative scientific and engineering reports.

## 3. Required order of use

```text
Destination authority
(journal / institution / ethics / law / regulation / safety / course)
        ↓
Scientific Research Architecture
        ↓
Project-specific scientific protocol
        ↓
APA JARS–Quant Adapted Reporting Standard
        ↓
Domain-specific reporting / validation requirements
        ↓
Pre-freeze audit checklists
        ↓
Frozen repository state + reproducibility package
```

## 4. Core invariants

The portfolio uses the following non-negotiable distinctions:

```text
scientific gap != industrial gap
industrial difficulty != scientific novelty
simulation != observation
verification != validation
calibration != validation
model output != scientific interpretation
visual resemblance != mathematical or physical equivalence
software test pass != empirical validity
```

For any public claim, the weakest required support dimension bounds the permitted claim strength.

## 5. Domain additions

Projects may impose stricter standards for, among others:

- systematic reviews and evidence synthesis;
- quantitative finance and causal backtesting;
- sustainable/infrastructure engineering;
- mathematical physics and differential geometry;
- inverse problems and uncertainty quantification;
- industrial/prototype validation;
- safety-, regulatory-, or standards-constrained systems;
- research software and numerical verification.

These additions must remain traceable to the governing research architecture and must not weaken its evidence boundaries.