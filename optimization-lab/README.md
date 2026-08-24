# Optimization and Decision Verification Lab — V1

This lab is the executable companion to the public profile's operations-research and Bayesian-decision layer.

It implements a small set of mathematically transparent benchmarks selected from the IEE 574 + Bayesian knowledge graph. The goal is **not** to reproduce the entire course. The goal is to provide compact, independently checkable objects that support the profile's public claims.

## Verification chain

```text
source anchor
→ normalized mathematical model
→ executable computation
→ independent residual/certificate checks
→ bounded profile claim
```

## Included benchmarks

1. **LP primal/dual certificate** — verifies primal feasibility, dual feasibility, strong duality, and complementary slackness.
2. **Min-cost network flow** — verifies node balance, bounds, and objective value on a small infrastructure-style network.
3. **Equality-constrained convex QP** — verifies the KKT linear system and equality feasibility.
4. **Bayesian acquisition formulas** — lightweight deterministic checks for UCB/EI semantics without claiming a full GP implementation.

## Evidence boundary

- IEE 574 formulas are instructional source-grounded mathematics `[S]`.
- Numerical outputs produced here are computed `[C]`.
- Residual/certificate checks are verified `[V]` only for the implemented benchmark instance.
- No benchmark output is empirical validation `[E]` of an infrastructure, finance, or other real-world system.

See `docs/knowledge-graphs/OR_SOURCE_ANCHORS_V1.md` for source anchors and the knowledge graph for promotion decisions.
