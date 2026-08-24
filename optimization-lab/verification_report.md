# Verification Report — Optimization and Decision Lab V1

This report records the benchmark certificates implemented in `optimization-lab/src/decision_math.py`.

## LP primal/dual certificate

Instructional anchor: IEE 574 Lecture 10, slide/pages 23 and 28–32.

Benchmark primal:

```math
\max\;30x_1+20x_2
```

subject to

```math
3x_1+3x_2\le36,\qquad
2x_1+5x_2\le50,\qquad
6x_1+2x_2\le60,\qquad
x\ge0.
```

Candidate primal optimum:

```math
x^*=(9,3).
```

Candidate dual optimum:

```math
w^*=(5,0,2.5).
```

The executable certificate verifies:

- primal feasibility;
- dual feasibility;
- zero duality gap;
- complementary slackness for primal and dual slack products.

Expected benchmark objective:

```math
c^Tx^*=b^Tw^*=330.
```

## Min-cost flow certificate

Instructional anchor: IEE 574 Lecture 15, slide/pages 10–11.

The executable benchmark uses a four-node directed network and verifies:

```math
\widehat A x=b,
```

all lower/upper capacity bounds, and independent objective recomputation after solving the LP with HiGHS through SciPy.

The network is a compact computational benchmark, not an empirical infrastructure model.

## Equality-constrained convex QP certificate

Instructional anchor: IEE 574 Lecture 17, slide/pages 21 and 24.

The implemented benchmark solves

```math
\min_x\;\tfrac12x^TDx+c^Tx
\qquad\text{s.t.}\qquad Ax=b
```

through the KKT linear system

```math
\begin{bmatrix}D&A^T\\A&0\end{bmatrix}
\begin{bmatrix}x\\w\end{bmatrix}
=
\begin{bmatrix}-c\\b\end{bmatrix}.
```

The certificate verifies stationarity, equality feasibility, and positive definiteness of `D`.

## Bayesian acquisition checks

Secondary source: *Bayesian Optimization for Hyperparameters Tuning in Neural Networks* (Onorato, 2024), especially the GP/acquisition discussion and EI/UCB sections.

The lab implements compact EI and UCB functions only. Tests verify:

- zero-variance EI reduces to positive deterministic improvement;
- at the incumbent mean, larger predictive uncertainty increases EI;
- increasing `kappa` increases the uncertainty contribution to UCB when `sigma>0`.

These are formula-level regression checks, not a complete Gaussian-process/Bayesian-optimization implementation.
