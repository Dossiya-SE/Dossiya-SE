# Operations Research Source Anchors — V1

This file freezes exact instructional source anchors for the deterministic operations-research concepts promoted from the Fall 2025 IEE 574 lecture archive into profile-level professional mathematics.

The course material is treated as **source-grounded instructional mathematics [S]**. It is not original research, empirical validation, or a substitute for later canonical textbook/paper verification where stronger publication authority is required.

## Promotion rule

A deterministic-OR formula may be promoted into the public profile formula registry only if it has:

1. exact lecture and slide/page anchor;
2. notation normalized without changing mathematical meaning;
3. assumptions/domain declared;
4. profile role declared;
5. executable or identity-level verification where applicable.

## P0 anchors

| Candidate ID | Concept | Exact instructional anchor | Normalized mathematical object | Profile role |
|---|---|---|---|---|
| `LP-STANDARD-001` | Standard-form LP | IEE574_4_LP_Model.pdf, slide/page 28 | `min c^T x` s.t. `Ax=b`, `x>=0` | deterministic optimization foundation |
| `LP-CANONICAL-002` | Canonical-form LP | IEE574_4_LP_Model.pdf, slide/page 29 | min-form `Ax>=b` or max-form `Ax<=b`, `x>=0` | duality bridge |
| `CVX-COMB-001` | Convex combination | IEE574_5_LP_Properties.pdf, slide/page 2 | `x=sum_i lambda_i x^i`, `lambda_i>=0`, `sum_i lambda_i=1` | convex geometry foundation |
| `CVX-SET-002` | Convex set | IEE574_5_LP_Properties.pdf, slide/page 3 | `lambda x1+(1-lambda)x2 in C` for `lambda in [0,1]` | feasible-set geometry |
| `CVX-HYPERPLANE-003` | Hyperplane and normal | IEE574_5_LP_Properties.pdf, slide/page 6 | `H={x:a^T x=b}`; `a` normal to `H` | optimization-geometry bridge |
| `LP-BFS-004` | Basic feasible solution / extreme point | IEE574_6_LP_Graphic.pdf, slide/pages 23–24 | choose `m` independent columns, set nonbasic variables to zero; BFS iff extreme point for standard LP | simplex geometry |
| `LP-REDUCEDCOST-005` | Reduced cost | IEE574_7_LP_Simplex.pdf, slide/pages 5–6 | `c_j-c_B^T B^{-1}A_j` | simplex optimality certificate |
| `LP-DUAL-009` | Primal-dual canonical pair | IEE574_10_LP_Duality.pdf, slide/page 23 | primal min `c^T x`, `Ax>=b`, `x>=0`; dual max `b^T w`, `A^T w<=c`, `w>=0` | duality architecture |
| `LP-WEAKDUAL-010` | Weak duality | IEE574_10_LP_Duality.pdf, slide/page 23 | `c^T x >= b^T w` for primal/dual feasible points | lower/upper bound certificate |
| `LP-STRONGDUAL-011` | Strong duality | IEE574_10_LP_Duality.pdf, slide/page 28 | `c^T x*=b^T w*` when a finite optimum exists | optimality certificate |
| `LP-CS-012` | Complementary slackness | IEE574_10_LP_Duality.pdf, slide/pages 29–32 | `(c_j-w^T A_j)x_j=0`, `(a_i^T x-b_i)w_i=0` | primal-dual verification |
| `LP-SENS-013` | Cost sensitivity through reduced costs | IEE574_11_LP_Sensitivity.pdf, slide/pages 4, 6, 11–13 | updated reduced costs determine whether current basis remains optimal | post-optimal robustness |
| `IP-RELAX-002` | LP relaxation of MILP | IEE574_13_IP_BnB.pdf, slide/page 3 | relax integer coordinates from `Z_+` to `R_+` | integer-optimization bound |
| `IP-BOUND-003` | Branch-and-bound relaxation logic | IEE574_13_IP_BnB.pdf, slide/pages 8, 10 | integer LP-relaxation optimum certifies IP optimum; otherwise branch | discrete optimization algorithm |
| `NF-BALANCE-001` | Network-flow conservation | IEE574_15_NF_Models.pdf, slide/page 10 | `sum_out x_ij = sum_in x_ji` for transshipment nodes | infrastructure/network conservation |
| `NF-MINCOST-002` | Min-cost flow | IEE574_15_NF_Models.pdf, slide/page 11 | `min c^T x` s.t. `Ahat x=b`, `l<=x<=u` | infrastructure allocation |
| `NLP-LAGRANGE-002` | Equality-constrained Lagrangian | IEE574_17_NLP.pdf, slide/page 17 | `L(x,w)=f(x)+sum_i w_i(b_i-g_i(x))` | nonlinear optimization foundation |
| `NLP-KKT-003` | Kuhn-Tucker conditions | IEE574_17_NLP.pdf, slide/page 20 | stationarity + complementary slackness + nonnegative multipliers, under regularity conditions | constrained-optimality geometry |
| `NLP-QP-004` | Equality-constrained convex QP | IEE574_17_NLP.pdf, slide/pages 21, 24 | `min 0.5 x^T D x+c^T x` s.t. `Ax=b`; KKT closed-form system when `D` positive definite | exact executable benchmark |

## Source-specific caveats

- The lecture deck uses `max` in its Lagrange-multiplier/Kuhn-Tucker presentation. Any profile-wide minimization convention must be converted explicitly rather than copied mechanically.
- KKT/KT conditions require constraint qualifications/regularity assumptions; the lecture explicitly notes that regularity conditions are outside the course scope.
- The BFS/extreme-point equivalence is tied to standard-form LP assumptions stated in the lecture.
- Network balance notation differs for transshipment nodes versus general supply/demand nodes. The profile implementation must use the incidence-matrix form `Ahat x=b` when nonzero node supplies/demands are present.
- Course slides are appropriate for instructional source anchoring. Later publication-grade authority should additionally cite canonical OR literature before these formulas are reused in formal research claims.
