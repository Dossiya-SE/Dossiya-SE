# Professional Profile Decision Architecture — V1

## Purpose

This document defines how the IEE 574 deterministic-optimization knowledge graph and the Bayesian-optimization source are allowed to appear in the public `Dossiya-SE/Dossiya-SE` profile.

The profile is a **front door**, not a course archive. Only concepts that strengthen the mathematical research identity, connect to implemented verification, and remain evidence-bounded are promoted.

## Public profile architecture

```text
Problem / system
→ data and parameters
→ mathematical model
→ feasible geometry / conservation
→ optimization / inference
→ verification certificate
→ sensitivity / uncertainty
→ bounded decision
```

Two mathematical rails feed that architecture:

```text
Deterministic OR:
model → convex/feasible structure → algorithm → optimality/duality → sensitivity

Bayesian sequential optimization:
observations → probabilistic surrogate → posterior uncertainty → acquisition → new evaluation → update
```

These rails are related but not interchangeable.

## Publicly promoted concepts

### Tier A — root-profile mathematics

- mathematical-model anatomy: variables, objective, constraints, parameters;
- convex feasible geometry;
- LP standard form;
- primal/dual optimality and strong duality;
- complementary slackness as an optimality certificate;
- sensitivity as post-optimal robustness analysis;
- network-flow conservation/min-cost structure;
- Lagrangian/KKT constrained optimality;
- Bayesian posterior/acquisition/update cycle;
- EI and UCB as compact acquisition examples.

### Tier B — executable lab / linked detail

- basic feasible solutions and simplex pivots;
- reduced-cost calculations;
- Phase I / initialization;
- LP relaxation and branch-and-bound;
- cutting planes;
- shortest/longest path algorithms;
- equality-constrained QP closed-form benchmark;
- Sobol initialization;
- detailed Bayesian-optimization benchmark experiments.

### Tier C — research/course background only

- full tableau arithmetic;
- Big-M mechanics;
- complete Gomory derivations;
- every classroom application example;
- low-level Ax API walkthroughs;
- claims that would require empirical evidence not present in the source material.

## Professional visual rule

The root README uses `assets/math-art/optimization-decision-system-v6.svg` as a conceptual/process surface only. Complex equations remain in GitHub-supported math blocks or machine-readable registries to avoid Unicode transcription drift inside SVG text.

Scientific color roles are semantic rather than decorative:

- indigo: source/model mathematics;
- blue: state/feasible geometry;
- violet: acquisition/interface relation;
- amber: uncertainty;
- green: admissibility/verified optimality;
- gold: bounded decision;
- slate: computation/verification.

## Evidence boundary

The public profile may say that the repository implements or verifies the included benchmark identities. It may not imply that:

- course material is original research;
- a verified benchmark validates a real infrastructure system;
- Bayesian optimization is always superior to deterministic optimization;
- KKT conditions are sufficient without the required convexity/regularity assumptions;
- a solver output is a scientifically validated decision without model/data validation.

## Promotion invariant

```math
L(C) \le \min_{k\in\mathcal R(C)} L_k
```

where `L(C)` is the maturity level of a public claim and `R(C)` is the set of support dimensions required by that claim.

No mathematical sophistication, numerical precision, animation quality, or solver output compensates for a missing required support dimension.
