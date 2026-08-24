# IEE 574 + Bayesian Optimization Knowledge Graph — V1

**Graph ID:** `DD-OR-KG-001`  
**Status:** source-inventoried / candidate-promotion architecture  
**Boundary:** no candidate below is automatically promoted into the live formula registry.

## Purpose

Build a formal operations-research and Bayesian-optimization spine for the mathematical profile:

```text
foundations
→ modeling
→ convexity / feasible geometry
→ deterministic algorithms
→ optimality certificates
→ sensitivity / uncertainty
→ bounded decisions
```

Artifact codes: **PF** profile formula, **EX** executable example, **VV** verified visualization, **MA** Manim animation, **RB** research-only background.

## 17-lecture inventory

| # | Lecture | Main mathematical role | Promotion | Priority |
|---:|---|---|---|---|
| 1 | Introduction to Operations Research | problem / decision / rules / goal / data → mathematical model | PF, VV, RB | P0 |
| 2 | Basic Linear Algebra | vectors, inner products, norms, independence, basis, rank, linear systems | PF, EX, VV, MA | P0 |
| 3 | Mathematical Modeling | indexed sets/parameters/variables, TSP, diet, transportation, formulation rules | PF, EX, VV, MA, RB | P0 |
| 4 | Linear Programming Models | standard/canonical LP, transformations, power-capacity model, linearization | PF, EX, VV, MA | P0 |
| 5 | LP Properties | convexity, hyperplanes, halfspaces, extreme points, recession | PF, EX, VV, MA | P0 |
| 6 | LP Graphical Representation / BFS | feasible polyhedra, objective level sets, extreme points, BFS | PF, EX, VV, MA | P0 |
| 7 | Simplex | basis/nonbasis, reduced costs, improving directions, pivots, unbounded rays | PF, EX, VV, MA | P0 |
| 8 | Simplex Tableau / Revised Simplex | tableau, minimum-ratio test, revised simplex | EX, VV, MA, RB | P1 |
| 9 | Infeasible LP / Initial BFS | artificial variables, Phase I/II, Big-M | EX, VV, RB | P1 |
| 10 | LP Duality | shadow prices, weak/strong duality, complementary slackness | PF, EX, VV, MA | P0 |
| 11 | LP Sensitivity | cost/RHS perturbations, basis stability, reduced-cost stability | PF, EX, VV, MA | P0 |
| 12 | Integer Programming Models | integer/binary variables, scheduling, knapsack, TSP | PF, EX, VV, MA | P0 |
| 13 | Branch and Bound | LP relaxation, integer hull, bounds, branching/pruning | PF, EX, VV, MA | P0 |
| 14 | Cutting Planes | valid cuts, separation, Gomory fractional cuts | EX, VV, MA, RB | P1 |
| 15 | Network Flow Models | conservation, incidence matrix, min-cost flow, total unimodularity | PF, EX, VV, MA | P0 |
| 16 | Network Flow Algorithms | critical path, longest/shortest path, Dijkstra, algorithm validation | PF, EX, VV, MA | P0 |
| 17 | Nonlinear Programming | local/global optima, gradient/Hessian, Lagrangian, KT/KKT, QP | PF, EX, VV, MA | P0 |

## Candidate deterministic-OR formula families

These are normalized source candidates. Exact slide anchoring and notation audit are still required before live-registry promotion.

```text
OR-MODEL-001       general decision/objective/constraint/parameter schema
LA-DOT-001         aᵀb = Σᵢ aᵢbᵢ
LA-PNORM-002       ||a||ₚ
LA-LINSYS-003      Ax = b
OR-ASSIGN-002      Σⱼ xᵢⱼ = 1
OR-LINK-003        yᵢⱼ ≤ xⱼ
OR-MAXLIN-004      min t s.t. t ≥ fᵢ(x)
LP-STANDARD-001    min cᵀx s.t. Ax=b, x≥0
LP-CANONICAL-002   min cᵀx s.t. Ax≥b, x≥0
LP-ABS-003         min t s.t. t≥x, t≥−x
CVX-COMB-001       convex combination
CVX-SET-002        convex-set definition
CVX-HYPERPLANE-003 H={x:aᵀx=b}
LP-BFS-004         x_B=B⁻¹b, x_N=0
LP-REDUCEDCOST-005 c̄ⱼ=cⱼ−c_BᵀB⁻¹Aⱼ
LP-SIMPLEX-006     x_B=B⁻¹b−B⁻¹Nx_N
LP-MRT-007         minimum-ratio test
LP-PHASE1-008      Phase-I feasibility objective
LP-DUAL-009        primal ↔ dual pair
LP-WEAKDUAL-010    weak-duality bound
LP-STRONGDUAL-011  cᵀx*=bᵀw*
LP-CS-012          complementary slackness
LP-SENS-013        B⁻¹b / reduced-cost perturbation relations
IP-MODEL-001       integer LP model
IP-RELAX-002       integer set vs LP relaxation
IP-BOUND-003       relaxation bound
IP-CUT-004         generic valid separating cut
IP-GOMORY-005      Gomory fractional-cut relation
NF-BALANCE-001     node flow conservation
NF-MINCOST-002     min-cost-flow model
NF-LONGEST-003     longest-path recurrence
NF-SHORTEST-004    shortest-path recurrence
NLP-GENERAL-001    generalized NLP
NLP-LAGRANGE-002   Lagrangian
NLP-KKT-003        Kuhn-Tucker/KKT conditions
NLP-QP-004         equality-constrained quadratic program
```

## Bayesian-optimization extension

The Bayesian source adds a probabilistic sequential-decision branch:

```text
BO-GP-001       Gaussian-process surrogate
BO-RBF-002      RBF covariance kernel
BO-MATERN-003   Matérn covariance kernel
BO-EI-004       Expected Improvement
BO-PI-005       Probability of Improvement
BO-UCB-006      Upper Confidence Bound
BO-QEI-007      q-Expected Improvement
BO-SOBOL-008    Sobol low-discrepancy initialization
BO-LOOP-009     posterior → acquisition → evaluation → update loop
BO-MOO-010      multiobjective / outcome-constrained BO
BO-INTEGER-011  discrete/integer BO bridge
```

## Cross-reference with the current profile formula registry

- `INV-BAYES-001` already covers posterior inference. Add GP/acquisition-specific children rather than replacing it.
- `OPT-MULTI-001` is an application-level multiobjective design formula; link it to the general OR/BO optimization spine.
- `NET-LAPLACIAN-001` is adjacent to, but mathematically distinct from, node-arc incidence and flow optimization. Do not conflate them.
- `ENERGY-BAL-001` can be cross-linked conceptually to flow conservation while preserving its physical energy-balance meaning.
- `FIN-CAL-004` and `ML-RISK-001` are domain-specific optimization objectives and should become children/applications of the general NLP layer.
- `VIA-KERNEL-001` should connect only at the constrained-decision architecture level; viability theory must not be reduced to static OR.
- `DG-METRIC-001` can connect to constraint geometry only when manifold/metric assumptions are explicitly defined.

## Registry gap conclusion

The live registry has strong differential-geometry, dynamics, viability, Bayesian-posterior, network-Laplacian, energy, finance, and ML application formulas, but it lacks a coherent deterministic OR foundation. Highest-value missing families are:

1. LP standard/canonical form;
2. convex feasible-set geometry;
3. BFS/extreme points and reduced costs;
4. primal-dual certificates and complementary slackness;
5. sensitivity analysis;
6. integer relaxations, B&B and cuts;
7. flow conservation and min-cost flow;
8. Lagrangian/KKT/QP;
9. GP/acquisition/Sobol Bayesian-optimization nodes.

## Highest-value public profile objects

1. `OR-MODEL-001` — problem → variables/objective/constraints/parameters.
2. `LP-STANDARD-001` — deterministic optimization foundation.
3. `CVX-SET-002` — convex feasible-set geometry.
4. `LP-BFS-004` + `LP-REDUCEDCOST-005` — geometry-to-simplex bridge.
5. `LP-DUAL-009` + `LP-STRONGDUAL-011` — optimality certificate / shadow-price logic.
6. `LP-SENS-013` — robustness after optimization.
7. `NF-BALANCE-001` + `NF-MINCOST-002` — infrastructure/network optimization bridge.
8. `NLP-LAGRANGE-002` + `NLP-KKT-003` — constrained nonlinear decision geometry.
9. `BO-GP-001` + `BO-UCB-006` or `BO-EI-004` — uncertainty-aware sequential optimization.
10. `BO-SOBOL-008` — rigorous mathematical-animation candidate through coverage/discrepancy.

## Executable-lab shortlist

- LP power-capacity planning from Lecture 4.
- 2-D feasible geometry + simplex trace from Lectures 5–8.
- Primal-dual certificate + sensitivity dashboard from Lectures 10–11.
- Integer lattice + branch-and-bound/cutting-plane demonstrator from Lectures 12–14.
- Min-cost flow / shortest path infrastructure lab from Lectures 15–16.
- KKT/QP residual checker + constraint-geometry visualization from Lecture 17.
- Rosenbrock + GP posterior + EI/UCB + Sobol benchmark from the Bayesian source.

## Manim shortlist

1. problem statement → mathematical model;
2. convex combination → feasible polytope → extreme point;
3. simplex edge walk using reduced costs and the ratio test;
4. primal ↔ dual bounds + complementary slackness;
5. LP relaxation → integer lattice → B&B tree;
6. fractional optimum → Gomory cut → tighter relaxation;
7. network flow with invariant node balances;
8. constraint level sets → gradient/tangent geometry → Lagrange/KKT;
9. GP observations → posterior uncertainty → EI/UCB → next sample;
10. pseudo-random vs Sobol coverage with measured discrepancy.

## Research-only background

Keep detailed tableau arithmetic, Big-M mechanics, full Gomory derivation, exhaustive domain examples, detailed golden-section arithmetic, and implementation-specific Ax API descriptions mainly in study/lab documentation. They are important learning material but would overload the root research profile.

## Promotion gate

A candidate becomes a live profile formula/visual only after: source slide/page anchor → notation normalization audit → assumptions/domain declaration → implementation where applicable → numerical/symbolic tests → visual semantics/accessibility checks → live formula-registry linkage → repository-role review.

No course formula is presented as original research. No Bayesian-thesis formula should be treated as final authority without checking the canonical literature or official implementation documentation during promotion.