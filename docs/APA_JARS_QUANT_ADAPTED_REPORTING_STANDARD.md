# APA-JARS-QUANT-ADAPTED-V1.0

**Status:** Governing cross-project reporting standard  
**Effective date:** 2026-08-23  
**Scope:** Quantitative research reports, theses, technical papers, empirical notebooks, simulation studies, and quantitative evidence sections.  
**Source framework:** APA Style Journal Article Reporting Standards for Quantitative Research (JARS–Quant), adapted for quantitative finance, sustainable engineering, infrastructure resilience, and related computational research.

> This is an adaptation, not a replacement for discipline-specific requirements. Course instructions, journal author guidelines, ethics requirements, and domain reporting standards remain controlling when they are stricter or more specific.

## 1. Governing evidence chain

Every report must expose the complete chain

`research requirement -> question/hypothesis -> data -> transformation -> model -> diagnostics -> result -> uncertainty -> interpretation -> limitation -> reproducibility artifact`.

No conclusion may appear without a traceable result; no result may appear without a traceable method; no method may be described without identifying its data and assumptions.

## 2. Claim classes

Before analysis, classify claims as:

- **Primary:** directly answer the main research question or assignment objective.
- **Secondary:** planned supporting analyses that deepen interpretation but do not replace the primary test.
- **Exploratory:** analyses not pre-specified or added after observing results.
- **Robustness / falsification:** analyses intended to test sensitivity, alternative specifications, or failure modes.

These classes must remain visible in the Methods, Results, and Discussion. Exploratory evidence must never be written as though it were confirmatory.

## 3. Required report architecture

### 3.1 Title and front matter

The title should identify the central variables/system, the relationship or problem being studied, and the study context when material. Front matter should disclose authorship, affiliations where required, funding/support, conflicts of interest, prior dissemination, registration/preregistration if applicable, and data/code availability.

### 3.2 Abstract

The abstract must contain, in compressed form:

1. problem/context;
2. objective or research question;
3. data/sample/system and period;
4. design and principal quantitative method;
5. principal numerical results with uncertainty or effect magnitude where meaningful;
6. bounded conclusion;
7. principal limitation when it materially changes interpretation.

Avoid vague claims such as “significant improvement” without a quantitative magnitude.

### 3.3 Introduction

The Introduction must establish:

- the real scientific/engineering/financial problem;
- the literature-supported gap;
- why the gap matters;
- the conceptual or mathematical mechanism motivating the analysis;
- the primary and secondary questions/hypotheses;
- the boundary of the claimed contribution.

Do not preview results as justification for the question.

### 3.4 Methods

The Methods section must be sufficiently precise for an independent researcher to reproduce the analysis.

#### Study design and scope

State whether the work is observational, experimental, quasi-experimental, simulation-based, longitudinal/time-series, cross-sectional, replication, model-comparison, or mixed design. Define the unit of analysis, temporal scope, system boundaries, and any grouping or clustering structure.

#### Data provenance and sample construction

Report:

- source and acquisition date/version;
- inclusion and exclusion rules;
- initial and final sample sizes;
- date range or spatial/system boundary;
- missing-data handling;
- duplicate/outlier handling;
- transformations and alignment rules;
- whether exclusions were pre-specified or post hoc;
- immutable data identifiers/hashes when available.

For secondary/public data, distinguish raw source data from project-created derived datasets.

#### Variables and measures

For every key variable provide definition, unit, direction, scale, timing, transformation, and interpretation. For constructed variables give the exact equation. For instruments or questionnaires report reliability/validity evidence where relevant.

#### Sample-size or information-size rationale

Explain how the effective information size was determined. Depending on design this may be a power analysis, all available observations in a fixed historical period, simulation budget, number of scenarios, number of bootstrap replicates, or another defensible information criterion. Do not imply conventional power calculations apply where dependence/time-series structure makes them inappropriate.

#### Statistical and mathematical model

For every controlling model state:

- mathematical specification;
- estimand or target quantity;
- parameters and constraints;
- estimation algorithm;
- initialization/random seeds;
- convergence rule;
- model-selection rule;
- uncertainty estimator;
- assumptions;
- diagnostics;
- software/library/version where material.

If a black-box library is used, explain the statistical object being estimated rather than citing only a function name.

#### Missingness, exclusions, and diagnostics

Report all diagnostic rules that can alter the analyzed sample or accepted model. State what happens when a diagnostic fails. Never silently drop failed fits, observations, or scenarios.

#### Temporal/causal integrity

For forecasting, finance, control, sequential decisions, or longitudinal analyses, explicitly identify the information set available at each decision time. Prevent look-ahead leakage. Distinguish retrospective quantities from quantities admissible for historical/causal decisions.

#### Sensitivity and robustness

Predefine the principal robustness dimensions. Examples: alternative state counts, windows, priors, discretizations, cost assumptions, boundary conditions, hazard scenarios, parameter uncertainty, alternative model families, or exclusion rules. Robustness analyses must not replace the primary specification after results are known.

#### Reproducibility

State:

- repository and commit/tag;
- environment/dependency lock;
- deterministic seeds;
- raw-data provenance;
- data/config/code hashes where possible;
- execution order;
- generated-artifact locations;
- whether cached outputs are hash-validated;
- known platform dependencies.

## 4. Results reporting standard

### 4.1 Start with the analyzed sample/system

Report the realized sample size, period, exclusions, missingness, failed fits/scenarios, and any deviations from the planned analysis before reporting inferential results.

### 4.2 Descriptive evidence first

Provide relevant distributions, central tendency, dispersion, ranges, frequencies, state occupancies, system parameters, or scenario summaries before model-based conclusions.

### 4.3 Primary results before secondary/exploratory results

Use the order:

`primary -> secondary -> robustness/falsification -> exploratory`.

Do not choose ordering by visual impressiveness or statistical significance.

### 4.4 Report magnitude and uncertainty

Prefer estimates accompanied by uncertainty: confidence/credible intervals, standard errors, bootstrap intervals, posterior intervals, sensitivity ranges, or simulation quantiles as appropriate. Report effect sizes or economically/engineering meaningful magnitudes rather than relying on p-values alone.

When null-hypothesis tests are used, report the statistic, degrees of freedom where relevant, exact or appropriately bounded p-value, effect magnitude, and uncertainty. Never equate `p > .05` with proof of no effect.

### 4.5 Model fit and diagnostics

Report the diagnostics necessary to assess the credibility of the model: convergence, residual or error behavior, state support, goodness-of-fit/model-selection criteria, calibration, validation error, conservation checks, numerical stability, or other design-relevant diagnostics.

### 4.6 Negative and failed results

Report failed model fits, non-robust findings, null findings, and sensitivity failures when they affect the scientific conclusion. They are evidence, not defects to hide.

## 5. Figures and tables

Every figure/table must answer a specific quantitative question.

Required figure principles:

- generated from the controlling data object whenever possible;
- source code retained in the notebook/repository;
- deterministic data and style inputs;
- axes, units, dates, states, and denominators explicitly labeled;
- uncertainty shown when it is central to interpretation;
- identical variables use consistent visual encoding across figures;
- no misleading truncation, aspect distortion, decorative 3-D, or visual exaggeration;
- color must not be the only carrier of meaning when accessibility matters;
- export a vector master (SVG/PDF) plus high-resolution raster when required;
- caption must state what is shown, the population/sample/system, and the principal interpretive boundary;
- store data/code/config provenance or hashes for final figures.

Tables should expose exact values when readers need numerical comparison. Do not duplicate an entire table with a figure unless each serves a distinct analytical purpose.

## 6. Discussion standard

The Discussion must proceed in this order:

1. answer the primary research question using the actual magnitude of evidence;
2. interpret the mechanism without overstating causality;
3. compare the result with prior literature/evidence;
4. explain robustness and specification dependence;
5. state limitations and threats to validity;
6. state generalizability/transferability boundaries;
7. explain engineering, financial, policy, or scientific implications;
8. identify the next falsifiable research step.

The conclusion must be no stronger than the design. Observational association is not causal evidence. A backtest is not proof of deployable superiority. A simulation is not empirical field validation. A literature-derived mechanism is not a measured effect.

## 7. Limitations taxonomy

Each final report must explicitly consider, where relevant:

- data quality and measurement;
- sampling/coverage/selection;
- missingness and exclusions;
- model misspecification;
- parameter uncertainty;
- numerical/optimization uncertainty;
- temporal dependence and nonstationarity;
- external validity/generalizability;
- causal-identification limitations;
- implementation costs/constraints;
- scenario uncertainty;
- computational reproducibility;
- multiple testing/model-search risk;
- researcher degrees of freedom.

## 8. Reproducibility package

A report is not considered project-final until the repository contains enough evidence to reconstruct its controlling results. At minimum:

- README with execution instructions;
- data provenance/manifest;
- environment/dependency specification;
- controlling configuration;
- analysis code/notebook;
- final result tables;
- native figure code and exported figures;
- validation/audit results;
- hashes or immutable identifiers for frozen evidence;
- changelog or version tag for the report-producing release.

## 9. Project-specific adaptations

### Quantitative finance / MScFE

Add explicit controls for train/test separation, model-selection leakage, look-ahead bias, filtered versus smoothed state probabilities, execution lag, benchmark construction, turnover/transaction costs, state-label canonicalization, walk-forward refitting, failed-fit handling, and sensitivity to model/state/window choices.

### Sustainable engineering / infrastructure systems

Add governing equations, units, physical conservation laws, system boundaries, initial/boundary conditions, parameter provenance, calibration/validation evidence, scenario/hazard definition, solver tolerances, numerical convergence, uncertainty propagation, sensitivity/global sensitivity where appropriate, and the distinction between simulated behavior and observed field evidence.

### Infrastructure-interface empirical/review work

For systematic-review stages use PRISMA or the controlling review protocol in addition to this standard. For quantitative coding/empirical analysis add inclusion/exclusion logic, coder agreement, evidence-anchor traceability, missingness, repeated-measures structure, clustering, model diagnostics, and design-appropriate uncertainty. JARS–Quant governs the quantitative reporting layer; it does not replace systematic-review standards.

### Product/prototype testing and challenge projects

Use this standard only for quantitative claims, experiments, surveys, pricing tests, reliability tests, or performance evidence. Pitch-deck narrative and design communication are not themselves JARS–Quant reports.

## 10. Final acceptance gates

A report receives `REPORTING_STANDARD_PASS` only if all applicable gates pass:

1. research questions and claim classes are explicit;
2. data/sample/system provenance is reconstructable;
3. exclusions and missingness are disclosed;
4. mathematical/statistical methods are reproducible;
5. assumptions and diagnostics are reported;
6. temporal/causal boundaries are respected;
7. primary results include meaningful magnitude and uncertainty;
8. robustness and failures are disclosed;
9. figures/tables are traceable to computations;
10. conclusions are bounded by design and evidence;
11. limitations and generalizability are explicit;
12. code/data/configuration provenance is recorded;
13. final report outputs correspond to a frozen repository state.

Any failed gate must be resolved or explicitly documented as a limitation; it must not be silently converted to PASS.

## 11. Standard report template

```text
Title
Author / affiliation / disclosures / data-code availability

Abstract

1. Introduction
   1.1 Problem and context
   1.2 Literature and evidence gap
   1.3 Research questions / hypotheses
   1.4 Contribution and scope

2. Methods
   2.1 Study design / system boundary
   2.2 Data provenance and sample construction
   2.3 Variables / measures / equations
   2.4 Preprocessing and exclusions
   2.5 Statistical / mathematical model
   2.6 Estimation / computation
   2.7 Assumptions and diagnostics
   2.8 Uncertainty quantification
   2.9 Validation / temporal-integrity controls
   2.10 Sensitivity / robustness plan
   2.11 Reproducibility environment

3. Results
   3.1 Final analyzed sample/system
   3.2 Descriptive evidence
   3.3 Primary results
   3.4 Secondary results
   3.5 Robustness / falsification
   3.6 Exploratory analyses
   3.7 Failed/non-robust specifications

4. Discussion
   4.1 Direct answer to primary question
   4.2 Mechanistic / financial / engineering interpretation
   4.3 Comparison with literature
   4.4 Robustness and specification dependence
   4.5 Limitations
   4.6 Generalizability
   4.7 Implications and next tests

5. Conclusion

Data and Code Availability
Author Contributions / Funding / Conflicts as applicable
References
Appendices / Supplementary reproducibility evidence
```

## 12. Sources and authority

Primary sources:

- APA Style JARS–Quant: https://apastyle.apa.org/jars/quantitative
- American Psychological Association, APA Style Journal Article Reporting Standards: https://www.apa.org/pubs/journals/resources/apa-style-jars
- Appelbaum, M., Cooper, H., Kline, R. B., Mayo-Wilson, E., Nezu, A. M., & Rao, S. M. (2018). Journal article reporting standards for quantitative research in psychology: The APA Publications and Communications Board task force report. *American Psychologist, 73*(1), 3–25. https://doi.org/10.1037/amp0000191
- EQUATOR Network JARS–Quant entry and design-module index: https://www.equator-network.org/reporting-guidelines/journal-article-reporting-standards-for-quantitative-research-in-psychology-the-apa-publications-and-communications-board-task-force-report/

## 13. Version control

Changes to this standard must increment the version identifier and record the rationale. Project-specific standards may add stricter requirements but should not silently weaken this canonical standard.
