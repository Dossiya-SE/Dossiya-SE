# APA-JARS-QUANT-ADAPTED-V1.0 — Final Report Checklist

Use this checklist before a quantitative report, thesis chapter, technical paper, or empirical appendix is frozen.

## A. Research framing

- [ ] Main research question is explicit.
- [ ] Primary, secondary, exploratory, and robustness claims are distinguished.
- [ ] Contribution is stated without overstating novelty.
- [ ] Study design is named correctly.
- [ ] Causal language matches the design.

## B. Data and sample/system

- [ ] Data source, version, acquisition date, and provenance are recorded.
- [ ] Initial and final sample/information size are reported.
- [ ] Inclusion/exclusion criteria are explicit.
- [ ] Missing data and duplicate/outlier rules are reported.
- [ ] Date/spatial/system boundaries are explicit.
- [ ] Derived variables are defined mathematically and with units.
- [ ] Data hashes or immutable identifiers are stored where possible.

## C. Methods

- [ ] Controlling equations/model specification are stated.
- [ ] Estimand/target quantity is identified.
- [ ] Parameter constraints are documented.
- [ ] Estimation/optimization algorithm is documented.
- [ ] Random seeds/initialization are documented.
- [ ] Convergence and model-acceptance criteria are documented.
- [ ] Model-selection rule is declared before final comparison.
- [ ] Statistical assumptions are stated.
- [ ] Diagnostics are defined and actually executed.
- [ ] Failed fits/scenarios are retained in the audit trail.
- [ ] Uncertainty method is reported.
- [ ] Sensitivity/robustness plan is stated.
- [ ] Temporal-information boundary is explicit for sequential/time-series studies.

## D. Results

- [ ] Final analyzed sample/system is reported before model conclusions.
- [ ] Descriptive evidence precedes inferential/model conclusions.
- [ ] Primary results appear before secondary/exploratory results.
- [ ] Effect/economic/engineering magnitude is reported.
- [ ] Uncertainty intervals or equivalent are reported where meaningful.
- [ ] Exact test statistics/p-values are reported where inferential tests are used.
- [ ] Model fit and diagnostics are reported.
- [ ] Robustness results are reported.
- [ ] Null, negative, and failed specifications are not hidden.
- [ ] Results text agrees exactly with tables/figures/code outputs.

## E. Figures and tables

- [ ] Every visual answers a defined question.
- [ ] Every visual is generated from the controlling data object where possible.
- [ ] Native plotting code is retained.
- [ ] Axes, units, dates, states, and denominators are clear.
- [ ] Uncertainty is visualized where central.
- [ ] Encoding is consistent across figures.
- [ ] No misleading scales, truncation, decorative 3-D, or visual exaggeration.
- [ ] Final vector master and high-resolution raster exist where appropriate.
- [ ] Caption is interpretable without reading the plotting code.
- [ ] Figure/table provenance or data hash is recorded.

## F. Discussion and conclusion

- [ ] Discussion directly answers the primary question.
- [ ] Mechanistic interpretation is distinguished from empirical identification.
- [ ] Results are compared with relevant literature.
- [ ] Specification dependence is discussed.
- [ ] Limitations are explicit.
- [ ] Generalizability/transferability boundary is explicit.
- [ ] Practical implications are proportional to evidence.
- [ ] Future work is formulated as a testable next step.
- [ ] Conclusion is no stronger than the design.

## G. Reproducibility

- [ ] Repository/commit/tag producing the report is recorded.
- [ ] Environment/dependency specification exists.
- [ ] Execution instructions are complete.
- [ ] Configuration and random seeds are frozen.
- [ ] Final result tables are stored.
- [ ] Figure-generation code and outputs are stored.
- [ ] Validation/audit outputs are stored.
- [ ] Cached outputs, if used, are protected by scientific/config hashes.
- [ ] Report-producing release has an immutable tag or commit SHA.

## H. Domain-specific gates

### Quantitative finance / time series

- [ ] No look-ahead leakage.
- [ ] Train/development/test separation is documented.
- [ ] Model selection is not based on final test performance.
- [ ] Filtered vs smoothed probabilities are distinguished when applicable.
- [ ] Execution lag is explicit.
- [ ] Benchmark construction is reproducible.
- [ ] Turnover and transaction costs are considered where investment claims are made.
- [ ] State-label/canonicalization convention is documented for latent-state models.

### Sustainable/infrastructure engineering

- [ ] Units and dimensional consistency are checked.
- [ ] Physical conservation/feasibility constraints are checked.
- [ ] Initial and boundary conditions are reported.
- [ ] Parameter provenance is documented.
- [ ] Solver tolerances and numerical convergence are reported.
- [ ] Scenario/hazard assumptions are explicit.
- [ ] Uncertainty/sensitivity is propagated to conclusions.
- [ ] Simulation evidence is not described as observed field evidence.

### Systematic review + quantitative synthesis/empirical analysis

- [ ] Review protocol and screening standard are reported separately (e.g. PRISMA where applicable).
- [ ] Coding/extraction rules are reproducible.
- [ ] Coder agreement or adjudication is reported when relevant.
- [ ] Evidence anchors link quantitative claims to source material.
- [ ] JARS–Quant is applied to the quantitative analysis layer, not used as a replacement for review standards.

## Final gate

`REPORTING_STANDARD_PASS` may be declared only when every applicable item is either checked or explicitly documented as a limitation/deviation with a rationale.
