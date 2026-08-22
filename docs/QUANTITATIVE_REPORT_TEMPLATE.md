# Quantitative Research Report Template

**Conforms to:** `APA-JARS-QUANT-ADAPTED-V1.0`

Use this as the starting structure for a quantitative report. Delete prompts that do not apply, but do not silently omit an applicable reporting requirement.

---

# Title

Identify the principal system/population, main variables or model, and the relationship/problem being studied.

**Authors:**  
**Affiliations:**  
**Funding/support:**  
**Conflicts of interest:**  
**Registration/preregistration:**  
**Data/code repository and frozen release:**  

## Abstract

**Context:** [Why this problem matters.]  
**Objective:** [Primary question/hypothesis.]  
**Data/system:** [Source, sample/system, period/boundary.]  
**Method:** [Principal design/model/estimator.]  
**Results:** [Principal numerical result with magnitude and uncertainty.]  
**Conclusion:** [Bounded interpretation.]  
**Limitation:** [Most decision-relevant limitation if material.]

# 1. Introduction

## 1.1 Problem and context

Describe the scientific, engineering, financial, or policy problem. Quantify its relevance when credible evidence exists.

## 1.2 Prior evidence and gap

Synthesize the evidence directly relevant to the mechanism and question. Identify what is known, uncertain, contradictory, or untested. Avoid citation lists without synthesis.

## 1.3 Research questions and hypotheses

### Primary

- RQ/H1: [...]

### Secondary

- RQ/H2: [...]

### Exploratory

- [...]

### Robustness/falsification questions

- [...]

## 1.4 Contribution and scope

State exactly what this study adds and what it does not claim to establish.

# 2. Methods

## 2.1 Study design / system boundary

State design type, unit of analysis, temporal/spatial/system boundary, and whether evidence is observational, experimental, simulation-based, longitudinal/time-series, or another design.

## 2.2 Data provenance and sample construction

**Source:** [...]  
**Version/acquisition date:** [...]  
**Raw sample/information size:** [...]  
**Final analyzed sample/information size:** [...]  
**Date/spatial/system range:** [...]  
**Inclusion criteria:** [...]  
**Exclusion criteria:** [...]  
**Missing-data rule:** [...]  
**Outlier/duplicate rule:** [...]  
**Raw-data hash/identifier:** [...]

Provide a flow table/diagram if sample construction is nontrivial.

## 2.3 Variables, measures, and equations

For each principal variable provide:

| Variable | Definition/equation | Unit/scale | Timing | Source | Interpretation |
|---|---|---|---|---|---|
| | | | | | |

## 2.4 Preprocessing and transformations

State every transformation that changes the raw evidence: alignment, normalization, returns/differences, interpolation, filtering, scaling, encoding, winsorization, aggregation, or derived indicators. Give equations for controlling transformations.

## 2.5 Information-size rationale

Explain power/sample-size determination or, for fixed historical/simulation studies, why the chosen period/scenario/replicate budget provides the information used. Discuss effective sample size where dependence materially reduces information.

## 2.6 Mathematical/statistical model

Write the controlling model formally.

**Target/estimand:** [...]  
**Parameters:** [...]  
**Constraints:** [...]  
**Assumptions:** [...]  
**Identification conditions:** [...]  
**Selection criterion:** [...]

## 2.7 Estimation/computation

**Algorithm:** [...]  
**Initialization:** [...]  
**Random seed(s):** [...]  
**Maximum iterations:** [...]  
**Tolerance/stopping rule:** [...]  
**Failed-fit rule:** [...]  
**Software/libraries/versions:** [...]

## 2.8 Diagnostics and validation

List the tests that must pass before a model/result is accepted.

| Gate | Quantity/invariant | Acceptance rule | Result |
|---|---|---|---|
| | | | |

Examples include probability/simplex constraints, convergence, residual behavior, conservation, calibration error, time ordering, cross-engine parity, held-out error, or solver convergence.

## 2.9 Uncertainty quantification

State the uncertainty estimator: analytical standard errors, bootstrap, Monte Carlo, posterior distribution, scenario distribution, parameter interval, or another method. State replicate count, seed, resampling structure, priors, or distributional assumptions as applicable.

## 2.10 Temporal/causal controls

For sequential/time-series studies identify the exact information set available at prediction/decision time. State any lag between signal and realized outcome. Distinguish retrospective/smoothed information from historical/causal decision inputs.

## 2.11 Sensitivity and robustness plan

List predeclared alternative specifications and the scientific question each tests.

| Robustness test | Baseline | Alternative | What failure would mean |
|---|---|---|---|
| | | | |

## 2.12 Reproducibility environment

**Repository:** [...]  
**Commit/tag:** [...]  
**Environment/dependency file:** [...]  
**Configuration hash:** [...]  
**Data hash:** [...]  
**Execution mode/order:** [...]  
**Artifact directory:** [...]

# 3. Results

## 3.1 Final analyzed sample/system

Report actual sample/period/system, exclusions, missingness, failed models/scenarios, and deviations from plan.

## 3.2 Descriptive evidence

Present distributions, central tendency, dispersion, frequencies, occupancies, physical parameters, or scenario summaries needed to interpret later results.

## 3.3 Primary results

For each primary question report:

1. estimate/result;
2. effect/economic/engineering magnitude;
3. uncertainty;
4. model/test statistic if applicable;
5. figure/table reference;
6. one bounded factual interpretation.

Do not mix Discussion-level speculation into this subsection.

## 3.4 Secondary results

Report planned supporting analyses using the same structure.

## 3.5 Robustness / falsification

Report all material alternative specifications, including failures and non-robust findings.

## 3.6 Exploratory analyses

Clearly label analyses that were not pre-specified. Do not present them as confirmatory evidence.

## 3.7 Negative, null, and failed specifications

Document findings that constrain the conclusion: null effects, unstable estimates, convergence failures, sensitivity failures, infeasible scenarios, or contradictory evidence.

# 4. Discussion

## 4.1 Direct answer to the primary question

Answer using the magnitude and uncertainty actually observed.

## 4.2 Mechanistic / engineering / financial interpretation

Explain what the result means within the model/design. Separate association, prediction, simulation, and causal evidence.

## 4.3 Comparison with prior evidence

Explain agreements and disagreements with literature. Discuss differences in data, scale, specification, boundary, or measurement that could explain divergence.

## 4.4 Robustness and specification dependence

State what remains stable and what changes under alternative assumptions.

## 4.5 Limitations

Address applicable limitations: data quality, selection, missingness, measurement, model form, parameter/numerical uncertainty, dependence/nonstationarity, causal identification, generalizability, implementation constraints, researcher degrees of freedom, and reproducibility.

## 4.6 Generalizability / transferability

Specify exactly where the result may and may not apply.

## 4.7 Implications and next falsifiable test

Translate the result into an appropriately bounded implication, then state the next analysis/experiment that could falsify or strengthen the conclusion.

# 5. Conclusion

Use a short evidence hierarchy:

1. what was tested;
2. what was found quantitatively;
3. what is supported;
4. what is not established;
5. what condition most limits application.

# Data and Code Availability

State what is available, where, under what version/tag/commit, and any access restriction.

# Author Contributions / Funding / Conflicts

Report as required by the destination journal/course/institution.

# References

Use the required citation style consistently. For APA-style outputs, follow APA 7 conventions.

# Appendices / Supplementary Evidence

Include material required for auditability but too detailed for the main narrative: full parameter tables, diagnostics, sensitivity grids, validation logs, data dictionary, computational environment, additional figures, or evidence manifests.

---

## Final pre-freeze declaration

A report may declare:

`REPORTING_STANDARD_PASS`

only after completing `APA_JARS_QUANT_REPORT_CHECKLIST.md` and linking the report to its frozen repository state.
