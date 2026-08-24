# Optimization and Decision Verification Lab — V1

This lab is the executable companion to the public profile's **operations-research and Bayesian-decision layer**.

It implements a deliberately small set of mathematically transparent benchmarks selected from the IEE 574 + Bayesian knowledge graph. The goal is **not** to reproduce course material. The goal is to expose compact, independently checkable mathematical objects that support bounded public-profile claims.

## Verification chain

```text
source anchor
→ normalized mathematical model
→ executable computation
→ independent residual/certificate checks
→ bounded profile claim
```

## Implemented benchmarks

| Benchmark | Mathematical certificate | Evidence state |
|---|---|---|
| LP primal/dual pair | primal feasibility + dual feasibility + zero duality gap + complementary slackness | `[S] → [C] → [V]` |
| Min-cost network flow | incidence-balance residual + capacity bounds + independent objective recomputation | `[S] → [C] → [V]` |
| Equality-constrained convex QP | KKT stationarity + equality feasibility + positive-definiteness check | `[S] → [C] → [V]` |
| Expected Improvement | deterministic limit + uncertainty-response regression | secondary source → `[C/V]` formula behavior |
| Upper Confidence Bound | uncertainty-weight regression in `κ` | secondary source → `[C/V]` formula behavior |

## Reproduce locally

From the repository root:

```bash
python -m pip install -e './optimization-lab[test]'
pytest optimization-lab/tests
cd optimization-lab && python audit_decision_math.py
```

The fail-closed audit also verifies that:

- the knowledge graph contains exactly 17 IEE 574 lecture nodes;
- graph node IDs are unique and dependency edges are non-dangling;
- the P0 deterministic-OR objects have exact source anchors;
- the professional V6 decision SVG satisfies its structural adaptive-rendering contract;
- all implemented numerical certificates pass their declared tolerance.

## Traceability

- **Knowledge graph:** [`../docs/knowledge-graphs/IEE574_BAYESIAN_KNOWLEDGE_GRAPH_V1.md`](../docs/knowledge-graphs/IEE574_BAYESIAN_KNOWLEDGE_GRAPH_V1.md)
- **Machine-readable graph:** [`../docs/knowledge-graphs/iee574_bayesian_knowledge_graph_v1.json`](../docs/knowledge-graphs/iee574_bayesian_knowledge_graph_v1.json)
- **Deterministic-OR source anchors:** [`../docs/knowledge-graphs/OR_SOURCE_ANCHORS_V1.md`](../docs/knowledge-graphs/OR_SOURCE_ANCHORS_V1.md)
- **Promotion matrix:** [`../docs/knowledge-graphs/PROFILE_PROMOTION_MATRIX_V1.csv`](../docs/knowledge-graphs/PROFILE_PROMOTION_MATRIX_V1.csv)
- **Verification report:** [`verification_report.md`](verification_report.md)
- **Public visual:** [`../assets/math-art/optimization-decision-system-v6.svg`](../assets/math-art/optimization-decision-system-v6.svg)

## Evidence boundary

- IEE 574 formulas are instructional source-grounded mathematics `[S]`, not original research.
- Numerical outputs produced here are computed `[C]`.
- Residual/certificate checks are verified `[V]` **only for the implemented benchmark instance**.
- The Bayesian thesis is used as a secondary source for acquisition-function architecture and formula behavior; it is not treated as sole canonical authority for the field.
- No benchmark output is empirical validation `[E]` of an infrastructure, finance, energy, or other real-world system.
- Solver success alone is insufficient: the lab recomputes independent mathematical conditions wherever the benchmark permits it.
