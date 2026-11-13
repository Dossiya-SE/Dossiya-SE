# Evidence-Led Writing Templates and Examples

## General scientific pattern

**[Evidence-appropriate action verb]** [specific model, component or research question] using [method and data] to [investigated outcome], obtaining [measured finding or bound] under [conditions], while [important limitation].

The wording must describe completed work only if the work was actually completed. Do not force all five fields into every sentence.

## 1. CV or resume

**Completed model evaluation**

Evaluated a first-order transformer thermal model using 8,592 SINTEF observations; reduced holdout top-oil RMSE from 0.2517 °C for persistence to 0.2165 °C, while documenting worse MAE.

**Computational experiment**

Quantified simulated transformer load-ordering sensitivity across 106 separate 24-hour windows, observing a median 0.355 °C absolute final-temperature difference under reordered current histories.

**Scientific evidence audit**

Audited 16 candidate power and transportation datasets for physical variables, provenance and potential modeling relevance; identified the absence of synchronized transformer–EVSE observations as a limitation.

## 2. Thesis and scientific manuscript

**Research question → method → finding → limitation**

To examine the sensitivity of transient transformer thermal predictions to load history, we evaluated a reduced first-order thermal model under reordered measured-current sequences. Across 106 separate 24-hour windows, the fitted model produced a median absolute final-temperature difference of approximately 0.355 °C. This is a within-model counterfactual, not a measured EV charging intervention or validated service consequence.

**Mixed outcome**

Compared a reduced thermal model against persistence on a chronological SINTEF holdout. The fitted model had lower RMSE but worse MAE; a general superiority claim is not supported by these metrics.

**Uncertainty boundary**

Diagnosed inadequate empirical coverage in nominal 90% parameter-only bands, which included approximately 8% of held-out observations in the reported experiment. The result motivates investigation of process variability, uncertain forcing, measurement error and model discrepancy, rather than a claim that total predictive uncertainty has been calibrated.

**Proposed mechanism**

Formulated a candidate transformer-temperature-to-charging-capability mechanism, conditional on documented equipment-specific protection or load-management actions. Cross-system causality remains unqualified without synchronized physical evidence.

## 3. Engineering calculation and decision record

**Documented engineering calculation**

Calculated [quantity] from [source revision, governing inputs and applicable equations], independently checked [units, equilibrium, numerical residual or acceptance margin], and documented [applicable requirement and unresolved evidence].

**Requirement status**

- **PASS:** Applicable requirement independently checked with supported inputs, methods, and any necessary uncertainty margin.
- **FAIL:** Evidence establishes noncompliance with a mandatory requirement.
- **INCONCLUSIVE:** Evidence or uncertainty does not distinguish compliance from violation.
- **NOT CHECKED:** A required check was not executed.

A technically plausible result is not a professional release authorization or certification.

## 4. Optimization

Formulated a [LP/MILP/nonlinear] problem to minimize [defined objective] subject to [physical and operational constraints]. Verified candidate feasibility against [independent computation]; established [lower bound or optimum] under [stated mathematical assumptions]. No actual operational benefit is claimed unless measured.

## 5. Numerical verification

Derived an analytical limiting case or manufactured reference for [governing equation]. Compared [numerical method] on systematically refined resolutions, evaluated [residual and quantity of interest], and identified [convergence behavior and remaining physical-model limitations].

**Do not claim** that numerical convergence validates the physical system.

## 6. Statement of purpose

**Research narrative**

A [specific scientific question] led me to [method and independently demonstrable action]. The evidence [observed finding, including adverse outcome when material] exposed [specific unresolved problem]. I now seek [precise mathematical or computational training] to investigate [next defensible question].

**Personal experience narrative**

My [actual circumstances] required me to [specific decision]. I [completed activity] and learned [author-approved interpretation], which changed how I [subsequent action]. This experience informs [future contribution].

Maintain a continuous, authentic narrative. Do not turn the SOP into a CV list.

## 7. Scholarship and leadership writing

Coordinated [specific activities] with [actual stakeholders] during [period], delivering [count and concrete outputs]. Where effect has not been measured, describe outputs rather than claiming transformed lives, systemic impact or guaranteed outcomes.

Distinguish founded versus co-founded; led versus contributed; selected versus completed; volunteered versus hired.

## 8. GitHub README / engineering project

**IMPLEMENTED:** [file, function or feature] at [commit or path].

**TESTED:** [test command, actual environment and observed result].

**PLANNED:** [proposed design and acceptance criteria].

**BLOCKED:** [missing dataset, authorization, interface, input or benchmark condition].

**UNKNOWN:** [unverified outcome or absent execution log].

Do not claim that a published benchmark result was achieved by this repository. Source papers provide context, not local execution evidence.

## 9. Before and after examples

**Overstated:** Proved EV charging causes transformer failure under extreme heat.

**Defensible:** Investigated temperature trajectories under measured transformer loading and identified the missing synchronized data needed to test charging-induced thermal causality.

**Overstated:** Validated the entire coupled infrastructure resilience framework.

**Defensible:** Evaluated component-level thermal predictions and verified selected numerical computations while leaving cross-system physical validation open.

**Overstated:** Achieved 90% accurate prediction intervals.

**Defensible:** Reported nominal 90% parameter-only bands with approximately 8% holdout coverage in the examined experiment; identified omitted predictive uncertainty sources.

**Overstated:** Optimized transformer lifespan through EV charging.

**Defensible:** Evaluated a hypothetical charging optimization on separate observations; thermal-constrained scheduling and aging consequences remain unverified.

## 10. Editing protocol

1. Preserve original facts, dates, people, units and scientific status.
2. Inspect the actual source before choosing a high-claim verb.
3. Prefer accurate and specific sentences over motivational adjectives.
4. State only the user's verified contribution; credit team activity correctly.
5. Retain material non-improvements, assumptions and unresolved evidence.
6. Never modify a protected passage or content outside the requested scope.
7. Avoid em dashes in newly written text; leave protected text untouched.
8. Preserve authentic sequence, motivation and scientific reasoning.
9. Flag source conflicts rather than silently combining incompatible data.
10. Return the requested complete draft with minimal accompanying commentary.
