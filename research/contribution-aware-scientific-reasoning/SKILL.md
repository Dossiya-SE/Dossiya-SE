---
name: contribution-aware-scientific-reasoning
description: Research planning, evidence checking, scientific claims, and contributor attribution using the NISO CRediT taxonomy as an attribution vocabulary. Keep scientific credibility and authorship separate.
version: 1.0.0
---

# Contribution-Aware Scientific Reasoning Protocol

**Status:** Reusable research-methodology extension, **not** an official CRediT method, an established thesis result, a new thesis objective, or an authorship decision.

**Central rule:** A research contribution is credited by its documented nature and extent; a scientific claim is accepted only to the extent justified by its physical, mathematical, computational and empirical evidence. These are different evaluations.

## Source authority and scope

- Official CRediT: https://credit.niso.org/implementing-credit/
- Official role descriptors: https://credit.niso.org/contributor-roles-defined/
- CRediT has 14 contributor roles. A person can have several roles; several people can share a role; irrelevant roles need not be assigned. Discuss and confirm assignments with contributors where possible.
- Optional contribution extent may be described as **lead / equal / supporting**, but is **not part of the formal CRediT standard**.
- CRediT is not an authorship test. Institutional, supervisory, publisher and journal policies govern authorship, acknowledgments and disclosure.
- CRediT's "Validation" is a contribution role about verification and reproducibility of research outputs. This does **not** alone prove independent field validation of a physical model.
- Apply this protocol to ASU thesis research on **Engineering of Power–Electrified Transportation Interdependencies for Resilience** and, when appropriate, other research programs. It does not amend any frozen thesis objectives, equations, hypothesis list, dataset eligibility criteria or protected text.
- Do not publish personal attribution details, unpublished original data or confidential materials to a public repository without the contributors' approval and permissions. Keep real contribution ledgers in an approved private workspace until authorized.

## Research cycle: question to justified conclusion

This ordered outline is a **planning aid**, not a claim that scientific research is strictly linear. Funding, supervision, administration and writing can occur throughout; unresolved evidence can return the study to an earlier stage.

| Phase | Question to resolve | CRediT categories that may contribute | Required evidence |
| --- | --- | --- | --- |
| 1. Conceptualization | Which observation or falsifiable question matters? What competing explanations exist? | Conceptualization, Supervision | Dated question, motivation, scope, competing hypotheses |
| 2. Physics and mathematical methodology | What conservation laws, constitutive relations, states, parameters, boundaries and assumptions are necessary? | Methodology, Formal analysis | Derivation, parameter definitions and units, model applicability |
| 3. Data and investigation | What observations, instrumentation and experiment design can distinguish hypotheses? | Investigation, Data curation, Resources | Source provenance, sensor semantics, missingness, timeline, sample selection, design |
| 4. Calculation and computation | What can be implemented or derived, and how accurate is the numerical solution? | Software, Formal analysis | Code version, solver, deterministic tests, analytic checks, convergence, independent comparator |
| 5. Critical verification and validation | Which conclusion survives independent checks? What evidence contradicts it? | Validation, Investigation, Formal analysis | Numerical reproduction, uncertainty, independent physical data if claiming physical validity |
| 6. Scientific interpretation | What is actually supported and within which domain? What is unresolved? | Formal analysis, Visualization, Writing – original draft, Writing – review & editing | Source-linked claims, adverse results, alternative explanations, error and limits |
| 7. Attribution and accountability | Who contributed what, at which point, and how is it confirmed? | All relevant roles | Contribution record with evidence and contributor confirmation |

**Cross-cutting:** Funding acquisition, Project administration, Supervision and Resources can enable any phase; contributions are not ranked solely by position in the sequence.

## Seven-question research gate

Before a result enters a report or manuscript, answer all seven. A checked box records consideration, **not proof**.

1. **Question:** Is there a precise falsifiable statement with alternatives and a documented physical or scientific purpose?
2. **Model:** Are source equations, derived equations, assumptions, units, initial conditions, boundary conditions and parameter meanings identified?
3. **Evidence:** Are original data, sensor meanings, ownership, timestamps, completeness, provenance and applicable conditions understood?
4. **Experimental design:** Is there a comparison capable of testing the target statement rather than merely demonstrating one model output?
5. **Independent checks:** Have numerical methods, implementation, holdout handling, calibration, uncertainty and rival models been checked appropriately?
6. **Interpretation:** Does the conclusion distinguish observed data, fitted model, conditional simulation, mechanistic inference and validated causality?
7. **Contribution record:** Is each material human contribution described with its role, output, evidence, extent where agreed, and review status?

If a critical gate fails, **report BLOCKED / INCONCLUSIVE / NOT CHECKED**, name the blocker, and do not substitute a model output for physical evidence.

## Two linked, separate registers

### A. Scientific claim register: what is defensible?

Use [SCIENTIFIC_CLAIMS_TEMPLATE.csv](templates/SCIENTIFIC_CLAIMS_TEMPLATE.csv). Record:
- claim ID, research objective, testable statement, hypothesis/alternative;
- model/evidence type: analytic, observational, synthetic, simulation, or mixed;
- source record and version, equations, assumptions, units, comparator and quantitative result;
- independent numerical check and physical validation **as separate fields**;
- uncertainty, falsifier, applicability domain, scientific status and permissible claim wording;
- decision maker and date.

Statuses: **PROPOSED, FORMULATED, EXECUTED_UNVERIFIED, NUMERICALLY_VERIFIED, PHYSICALLY_SUPPORTED_IN_DOMAIN, REFUTED, INCONCLUSIVE, BLOCKED**. These are project conventions, not official CRediT labels. A claim can have several evidence tags; choose the narrowest defensible statement.

### B. Contribution register: who did which work?

Use [CONTRIBUTIONS_TEMPLATE.csv](templates/CONTRIBUTIONS_TEMPLATE.csv). Record:
- human contributor (real attribution belongs in an authorized project register);
- official CRediT role, distinct work description, actual artifact, dates, supporting reference;
- optional contribution extent **lead / equal / supporting / not assessed**;
- confirmation status **PENDING / CONFIRMED / DISPUTED**;
- publication/acknowledgment status as a **separate pending institutional decision**.

**Never** infer contributions from an author list alone. Someone who conceptualized the problem, secured funding, designed methods, conducted experiments or wrote a paper can have an important contribution without personally performing every other stage. Multiple contributors can legitimately share a role.

### AI-assisted computational work

Record **human** role and decisions separately from tool involvement:
- research question, hypotheses, scientific constraints and acceptance criteria defined by whom;
- AI tool/version and exact intended assistance, prompts or execution log if permitted;
- code, input hashes, runtime and output artifacts;
- independently re-run checks and human interpretation;
- what remains unreviewed or unvalidated.

Do not treat AI software as a human CRediT contributor or an independent accountable author. Follow institutional and publisher AI-use policies for disclosure. Neither AI execution nor human conceptualization alone establishes external validation.

## ASU MSE thesis objectives and bounded example

**SO1:** Identify and qualify thermally sensitive states and directional power–electrified transportation interdependency mechanisms.

**SO2:** Develop a physics-based state-time model of qualified thermal interdependencies and propagation under extreme heat.

**SO3:** Quantify critical transition times, propagation delays, and electricity and mobility service consequences.

The following are **previously reported research findings**, not newly reproduced observations or new approvals:

- **THERM-001:** Reported model-based load-order sensitivity: 106 separate 24-hour current-order simulations produced a median absolute final transformer temperature difference near **0.355 °C**. The result is a *within-model counterfactual*, not measured causal EV charging impact or service improvement.
- **THERM-002:** Reported first-order SINTEF top-oil model: holdout RMSE **0.2165 °C** compared with **0.2517 °C** persistence across an analysis using **8,592 original hourly records**; MAE was worse. The difference in metric performance matters.
- **THERM-003:** Reported nominal **90%** parameter-only uncertainty bands covered approximately **8%** of holdout outcomes in a specified experiment. The bands omitted other predictive uncertainty sources. Do not conflate with separate residual-calibrated experiments.
- **SO1 evidence gate:** Separate SINTEF transformer and EV charging datasets do **not** establish a synchronized, physically connected transformer–EVSE causal pathway.
- **SO3 evidence gate:** Do not claim a real thermal trip, equipment aging-life consequence or mobility-service shortfall without suitable equipment-specific thresholds and service observations.

**Reasoning exercise for THERM-001**
- Conceptualization: Does time ordering affect terminal temperature under a fixed aggregate squared-current history?
- Methodology: Derive the first-order thermal recurrence and its weighted-history expression; justify constant/variable ambient assumptions.
- Investigation: Preserve the declared input invariant; specify initial temperature and paired input sequences.
- Formal analysis: Calculate the terminal and peak-temperature contrasts with uncertainty and sensitivity to time constant.
- Validation: Reproduce numerical calculations and distinguish this from comparison against independent connected-site observations.
- Interpretation: Report a bounded **model sensitivity**, not validated cross-system resilience.
- Attribution: Assign each verified human contribution only after reviewing design notes, code history, execution, oversight and drafting records.

## Reporting and interpretation rules

- Do not collapse a separate scientific claim register into the contributor list. Document **scientific truth-conditions** separately from **who contributed**.
- Do not assign responsibilities based on academic rank, funding amount or authorship position alone.
- Do not create fictitious consent, approval, experimental runs, external validation or impact.
- Preserve negative findings and alternatives; do not suppress model failure to promote a stronger verb.
- Treat missing source, uncertain sensor semantics, absent governing threshold, mismatched site and unverified code as actual blockers.
- Use [Research Decision Record](templates/RESEARCH_DECISION_RECORD.md) for every material design choice or exception.
- Review [the full official role list](CREDIT_ROLE_MAP.md) before finalizing contribution labels.
- When preparing text, consult the [Evidence-Led Action-Verb Writing Skill](../../writing/evidence-led-action-verb-writing/SKILL.md) and [Authentic Voice](../../writing/dossiya-authentic-voice/SKILL.md); protected passages and the user's specified edit scope take priority.

## Acceptance criteria before publication

- All 14 official role names used correctly; no unconfirmed personal roles.
- Scientific statement, source, numerical method, physical validation and stated operating domain traceable.
- Distinct model-based versus empirical outcomes, with testable alternatives and uncertainty.
- No authorship promises or unjustified AI coauthorship.
- Official CRediT citation and separate statement that this reasoning protocol is a project extension.
- Any thesis-source conflict referred to existing thesis authority rather than silently rewritten.
