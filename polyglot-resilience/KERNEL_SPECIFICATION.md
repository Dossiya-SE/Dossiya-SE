# Polyglot Resilience Kernel Specification — PRK-1.0

## Status

`PRK-1.0` is the canonical scientific/numerical specification used for cross-language conformance. Any implementation claiming `FULL_KERNEL` conformance must implement this document rather than an informal approximation of it.

## Level A — continuous-time model

Let

\[
x(t)\in[0,1]^n
\]

represent normalized service states of \(n\) infrastructure sectors. The baseline dynamics are

\[
\dot{x}(t)
=
-Dx(t)
+A\phi(x(t))
+r\odot(1-x(t))
-h(t)
+Bu(t).
\]

Definitions:

- \(D\in\mathbb R^{n\times n}\): degradation operator;
- \(A\in\mathbb R^{n\times n}\): directed interdependency/interface operator;
- \(\phi:\mathbb R^n\to\mathbb R^n\): nonlinear coupling map;
- \(r\in\mathbb R^n_{\ge0}\): recovery-capacity vector;
- \(h(t)\in\mathbb R^n\): exogenous hazard forcing;
- \(B\in\mathbb R^{n\times m}\): control-incidence matrix;
- \(u(t)\in\mathbb R^m\): control/action vector;
- \(\odot\): elementwise product.

### Baseline nonlinearity

`PRK-1.0` freezes

\[
\phi(x)_i=\tanh(x_i).
\]

An implementation using a different \(\phi\) is a different model version or profile.

## Level B — discrete reference kernel

For step size \(\Delta t>0\), define

\[
f(x,h,u)
=
-Dx+A\tanh(x)+r\odot(1-x)-h+Bu.
\]

The pre-projection Euler state is

\[
\tilde{x}_{t+1}=x_t+\Delta t\,f(x_t,h_t,u_t).
\]

The admissible state is

\[
\boxed{
 x_{t+1}=\Pi_{[0,1]^n}(\tilde{x}_{t+1})
}
\]

with componentwise projection

\[
[\Pi_{[0,1]^n}(z)]_i=\min(1,\max(0,z_i)).
\]

## Required evaluation order

For deterministic conformance, implementations must compute the terms conceptually as:

1. \(\phi_t=\tanh(x_t)\);
2. degradation \(d_t=Dx_t\);
3. coupling \(c_t=A\phi_t\);
4. recovery \(q_t=r\odot(1-x_t)\);
5. control \(g_t=Bu_t\);
6. derivative \(\dot x_t=-d_t+c_t+q_t-h_t+g_t\);
7. Euler proposal \(\tilde x_{t+1}=x_t+\Delta t\dot x_t\);
8. componentwise projection.

Algebraically equivalent reordering is allowed, but observable outputs must satisfy the declared numerical tolerance.

## FULL_KERNEL requirements

A `FULL_KERNEL` implementation must:

- support a general \(n\times n\) matrix \(D\), not silently assume diagonal degradation;
- support a general \(n\times n\) matrix \(A\);
- include the full control term \(Bu\);
- use the frozen elementwise `tanh` nonlinearity;
- include recovery and hazard terms exactly as specified;
- project every output component to \([0,1]\);
- reject invalid dimensions and non-finite inputs;
- expose enough output to compare at least \(\dot x_t\) and \(x_{t+1}\) with the reference.

## Reduced profiles

### `DIAGONAL_D_KERNEL`

A reduced profile may set

\[
D=\operatorname{diag}(d).
\]

It must be labeled explicitly. It is conforming to `FULL_KERNEL` only on fixtures for which the authoritative \(D\) is diagonal.

### `BINDING`

A binding exposes a separately validated kernel to another language. It is not counted as an independent native implementation unless it independently evaluates the kernel.

### `SERVICE_WRAPPER`

A service/orchestration layer may call another solver. Its correctness concerns serialization, orchestration and provenance rather than independent numerical conformance.

### `VISUALIZATION_CLIENT`

A visualization client consumes validated outputs and is never reported as a solver.

### `ADAPTER`

SQL, Bash and LaTeX are represented as persistence/orchestration/specification adapters, not as equivalent numerical kernels.

## Weighted-service statistic

For a trajectory \(x_1,\ldots,x_T\) and weights

\[
w_i\ge0,
\qquad
\sum_i w_i=1,
\]

define

\[
R_{\mathrm{AUC}}
=
\frac1T\sum_{t=1}^{T}w^\top x_t.
\]

This is a normalized weighted-service statistic, not a complete resilience definition.

## Versioning rule

Any change to the mathematical right-hand side, nonlinear map, projection rule, required input semantics or output semantics requires a new kernel version. Tolerance changes alone require a new validation-profile version and must not silently redefine scientific equivalence.
