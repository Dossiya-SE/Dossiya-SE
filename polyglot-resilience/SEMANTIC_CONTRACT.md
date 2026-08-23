# Semantic Contract — PRK-1.0

This contract defines the shapes, units/normalizations, admissibility rules and serialization semantics that all `FULL_KERNEL` implementations must share.

## State and control dimensions

For state dimension \(n\ge1\) and control dimension \(m\ge1\):

\[
x,r,h,w\in\mathbb R^n,
\qquad
D,A\in\mathbb R^{n\times n},
\qquad
B\in\mathbb R^{n\times m},
\qquad
u\in\mathbb R^m.
\]

The implementation input field is named `u` even though the mathematical control symbol is \(u\).

## Required input fields

| Field | Shape | Contract |
|---|---:|---|
| `kernel_version` | scalar string | must equal `PRK-1.0` for this contract |
| `fixture_id` | scalar string | provenance identifier |
| `dt` | scalar | finite and strictly positive |
| `x` | `n` | finite; every component in \([0,1]\) |
| `D` | `n x n` | finite; general matrix permitted |
| `A` | `n x n` | finite; directed/asymmetric matrix permitted |
| `r` | `n` | finite and componentwise non-negative |
| `h` | `n` | finite; sign interpretation follows experiment specification |
| `B` | `n x m` | finite |
| `u` | `m` | finite |
| `weights` | `n` | finite, non-negative, sum to one within tolerance |

## Output contract

A one-step solver returns at least:

```json
{
  "kernel_version": "PRK-1.0",
  "fixture_id": "...",
  "dx": [0.0],
  "x_next": [0.0],
  "weighted_service_next": 0.0
}
```

where:

- `dx` is the unprojected right-hand side \(f(x,h,u)\);
- `x_next` is the projected Euler state;
- `weighted_service_next = weights^T x_next`.

## Numerical type

The baseline conformance profile assumes IEEE-754 binary64-equivalent arithmetic where the language/runtime supports it. Implementations using materially different precision must declare that precision in the implementation registry and use a separately justified tolerance profile.

## Matrix orientation

Matrices use row-major mathematical semantics regardless of in-memory representation:

\[
(Dx)_i=\sum_{j=1}^{n}D_{ij}x_j,
\qquad
(A\phi)_i=\sum_{j=1}^{n}A_{ij}\phi_j,
\qquad
(Bu)_i=\sum_{q=1}^{m}B_{iq}u_q.
\]

This contract prevents silent transposition across languages.

## Nonlinearity

`PRK-1.0` fixes

\[
\phi_i=\tanh(x_i)
\]

elementwise. Matrix hyperbolic tangent or any alternative nonlinear transformation is non-conforming.

## Projection

Projection is componentwise clipping after the Euler proposal. Clipping intermediate model terms is not equivalent and is not allowed by the baseline contract.

## Weight semantics

Weights are convex service-importance weights:

\[
w_i\ge0,
\qquad
\sum_i w_i=1.
\]

Negative weights are invalid because they would destroy the interpretation of `weighted_service_next` as a normalized service aggregate.

## Serialization

JSON is the canonical small-fixture interchange format. Large scientific experiments may use Arrow/Parquet/HDF5/NetCDF, but any alternative format must preserve exactly the same semantic field definitions and provenance identifiers.

## Errors

An implementation must fail explicitly rather than silently reshape, truncate, pad or coerce scientifically invalid dimensions. Invalid-state clipping on **input** is forbidden; projection applies to the **computed next state**, not to malformed input data.

## Determinism

With identical deterministic input values and the same implementation/runtime configuration, one-step results must be deterministic. Any future stochastic extension must introduce an explicit random-number contract, generator family and seed provenance rather than overloading `PRK-1.0`.
