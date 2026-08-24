# SCIENTIFIC-RESEARCH-ARCHITECTURE-V1.0 — Audit Checklist

Use this checklist before freezing a scientific paper, thesis chapter, mathematical/computational model, engineering study, simulation study, or industrially motivated research result.

## A. Problem and scope

- [ ] Real system/problem is explicit.
- [ ] Phenomenon/mechanism is explicit.
- [ ] Stakeholders or affected system/users are identified where relevant.
- [ ] Decision or scientific purpose is explicit.
- [ ] Spatial/system scale is explicit.
- [ ] Time horizon/resolution is explicit.
- [ ] Failure/success/admissibility criterion is explicit.

## B. Gap architecture

- [ ] Each claimed gap is classified: scientific, theoretical, methodological, mathematical, data, validation, industrial/practice, technology, implementation, regulatory, institutional, economic/financial, equity, computational, or reproducibility.
- [ ] Each claimed gap has evidence appropriate to that gap class.
- [ ] Absence in literature is not used as proof of industrial failure.
- [ ] Industrial difficulty is not used as proof of scientific novelty.
- [ ] Data absence is not used as proof that a phenomenon is absent.
- [ ] Simulation success is not described as field validation.
- [ ] The bridge from real problem to research contribution is explicit.

## C. Research question and contribution

- [ ] Primary research question is explicit.
- [ ] System, mechanism, condition, and outcome are defined where applicable.
- [ ] Falsification/failure condition is stated where possible.
- [ ] Primary, secondary, exploratory, and robustness claims are distinguished.
- [ ] Contribution class is stated.
- [ ] Novelty is bounded by actual evidence.

## D. System definition

- [ ] System boundary is explicit.
- [ ] Environment/external forcing is explicit.
- [ ] States and observables are defined.
- [ ] Inputs/controls are separated from disturbances.
- [ ] Interfaces/couplings are defined.
- [ ] Success/failure/service criteria are defined.

## E. Mathematical model

- [ ] Model purpose is declared: describe/explain/estimate/identify/predict/optimize/control/design/reconstruct/visualize.
- [ ] State variables are defined and interpretable.
- [ ] Parameters are defined.
- [ ] Governing equations are stated.
- [ ] Constraints are stated.
- [ ] Assumptions are numbered and explicit.
- [ ] Spatial/state/time/parameter domains are explicit.
- [ ] Initial conditions are stated where applicable.
- [ ] Boundary conditions are stated where applicable.
- [ ] Units and dimensional consistency are checked.
- [ ] Model outputs are explicitly defined.

## F. Data and parameter provenance

- [ ] Every controlling input is classified as observed/measured, published/official, calibrated, derived, assumed/design target, synthetic, or planned/unavailable.
- [ ] Assumed/synthetic values are never relabeled as observations.
- [ ] Data source/version/acquisition date are recorded.
- [ ] Inclusion/exclusion and missingness rules are explicit.
- [ ] Transformations from raw to derived evidence are reproducible.
- [ ] Immutable identifiers/hashes are recorded where possible.

## G. Numerical / analytical method

- [ ] Analytical solution is used or ruled out appropriately.
- [ ] Numerical method is named and justified.
- [ ] Discretization is documented.
- [ ] Solver/library versions are recorded where material.
- [ ] Initialization and random seeds are recorded.
- [ ] Stopping rules/tolerances are recorded.
- [ ] Failed-solve handling is explicit.

## H. Verification

- [ ] Verification question is explicit: “Did we solve the declared equations/algorithm correctly?”
- [ ] Analytical/manufactured benchmark is used where possible.
- [ ] Convergence is checked where discretization applies.
- [ ] Conservation/invariant checks are executed where applicable.
- [ ] Numerical residual/tolerance checks are executed.
- [ ] Regression/unit/integration tests are preserved where applicable.
- [ ] Verification is not described as validation.

## I. Calibration and identification

- [ ] Unknown parameters are identified.
- [ ] Calibration/estimation method is stated.
- [ ] Identification conditions are considered.
- [ ] Priors/regularization are explicit where used.
- [ ] Calibration data are distinguished from validation data.
- [ ] Parameter uncertainty/correlation is reported where material.

## J. Validation

- [ ] Intended use/domain of validation is explicit.
- [ ] Independent/external evidence is used where available.
- [ ] Validation examines relevant temporal/spatial/regime behavior, not only one scalar metric.
- [ ] Extreme/failure regimes are checked where material.
- [ ] Physical/operational feasibility is checked.
- [ ] If empirical validation is absent, that absence is explicit.

## K. Sensitivity and uncertainty

- [ ] Parameters/assumptions controlling conclusions are identified.
- [ ] Local/global sensitivity method is appropriate to model nonlinearity/interactions.
- [ ] Measurement uncertainty is considered.
- [ ] Parameter uncertainty is considered.
- [ ] Disturbance/scenario uncertainty is considered.
- [ ] Numerical uncertainty is considered where material.
- [ ] Structural/model uncertainty is acknowledged where material.
- [ ] Uncertainty is propagated to decision-relevant outputs.

## L. Baselines and comparison

- [ ] Appropriate analytical/simpler/established/industry/observed/benchmark baseline is defined.
- [ ] Comparison metric is declared before interpretation.
- [ ] Model complexity alone is not treated as improvement.
- [ ] Ablation or component contribution is tested where relevant.

## M. Results and interpretation

- [ ] Model output is separated from scientific interpretation.
- [ ] Association is not relabeled as causation.
- [ ] Simulation is not relabeled as observation.
- [ ] Negative/null/failed/non-robust results are retained.
- [ ] Results directly answer the research question.
- [ ] Claims match magnitude and uncertainty.

## N. Industrial/practical relevance

If industrial/practical relevance is claimed:

- [ ] Accuracy is adequate for the claimed use.
- [ ] Reliability is considered.
- [ ] Speed/latency is considered.
- [ ] Cost is considered.
- [ ] Data burden is realistic.
- [ ] Interpretability/auditability is considered.
- [ ] Integration with existing systems is considered.
- [ ] Maintainability/lifecycle is considered.
- [ ] Safety constraints are explicit.
- [ ] Regulatory/standards constraints are considered.
- [ ] Scalability is considered.
- [ ] Human/institutional capability and ownership are considered.

## O. Limitations and bounded conclusion

- [ ] What was not modeled is explicit.
- [ ] What was assumed is explicit.
- [ ] What was not measured is explicit.
- [ ] What remains uncalibrated/unvalidated is explicit.
- [ ] Generalizability/transferability boundary is explicit.
- [ ] Unresolved contradictory evidence is disclosed.
- [ ] Conclusion does not exceed the weakest required support dimension.

## P. Reproducibility

- [ ] Data/provenance artifact exists.
- [ ] Code exists.
- [ ] Environment/dependency specification exists.
- [ ] Parameters/configuration are frozen.
- [ ] Random seeds are frozen where applicable.
- [ ] Equations/specification are versioned.
- [ ] Verification artifacts are preserved.
- [ ] Validation artifacts are preserved.
- [ ] Figures/tables trace to computations.
- [ ] Frozen commit/tag identifies the result-producing state.

## Final gate

`SCIENTIFIC_RESEARCH_ARCHITECTURE_PASS` may be declared only when every applicable item is checked or an explicit deviation/limitation is recorded with rationale.

A failed gate must not be silently converted to PASS.