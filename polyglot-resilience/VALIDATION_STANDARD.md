# Validation Standard — PRK-1.0

## Purpose

This standard defines what evidence is required before a language implementation can be promoted from source code to tested, validated or benchmarked status.

## Evidence ladder

```text
SPECIFIED
   ↓
IMPLEMENTED
   ↓
UNIT-TESTED
   ↓
CONFORMANCE-TESTED
   ↓
NUMERICALLY VALIDATED
   ↓
BENCHMARKED
```

A language may occupy different maturity levels for different implementation profiles.

## Tolerance profile

Baseline binary64 one-step conformance uses

\[
\varepsilon_{\infty}=10^{-12}
\]

for the frozen fixtures unless a language/runtime precision profile explicitly justifies another tolerance.

The acceptance rule is

\[
\max_i\left|x_{i,t+1}^{(\ell)}-x_{i,t+1}^{(\mathrm{ref})}\right|\le\varepsilon_{\infty}
\]

and the same tolerance applies to `dx` unless documented otherwise.

Tolerance must be declared **before** evaluating a new implementation and may not be widened simply to turn a failed implementation into a pass.

## Gate 1 — structural validity

- expected project files exist;
- implementation registry parses;
- JSON schema parses;
- fixtures contain required fields;
- implementation IDs are unique;
- every claimed conforming implementation identifies a kernel version and profile.

## Gate 2 — input-contract validity

Test invalid inputs explicitly:

- non-positive `dt`;
- mismatched vector lengths;
- malformed matrix shapes;
- state values outside \([0,1]\);
- negative recovery components;
- negative weights;
- weights that do not sum to one;
- non-finite values.

A solver must fail clearly rather than silently repair these cases.

## Gate 3 — scientific invariants

### State bounds

\[
x_t\in[0,1]^n\Longrightarrow x_{t+1}\in[0,1]^n.
\]

### Determinism

Repeated evaluation of the same deterministic fixture must return the same output.

### Control-term activation

At least one fixture must use non-zero \(B\) and \(u\), preventing reduced implementations that omit \(Bu\) from passing accidentally.

### Full-\(D\) support

At least one fixture should contain a non-diagonal \(D\), preventing a diagonal-only implementation from being mislabeled `FULL_KERNEL`.

### Directional checks

When all other terms are held constant and the model structure justifies the comparison:

- stronger positive hazard should not improve the instantaneous derivative through the direct hazard term;
- stronger recovery/control should produce the expected direct contribution.

These are controlled model checks, not universal empirical claims about nonlinear infrastructure systems.

## Gate 4 — frozen-fixture conformance

Every native solver marked `conformance=PASS` must be evaluated on the same authoritative fixture values and compared with `fixtures/expected-results.json`.

For each fixture record:

```text
implementation_id
kernel_version
fixture_id
runtime/compiler
max_abs_error_dx
max_abs_error_x_next
weighted_service_error
pass/fail
```

## Gate 5 — time-discretization validation

Cross-language agreement at one step size does not establish explicit-Euler convergence. A numerical study should compare

\[
\Delta t,\quad\Delta t/2,\quad\Delta t/4
\]

for a fixed final horizon. At minimum report

\[
e_{\Delta t}=\|x^{\Delta t}(T)-x^{\Delta t/2}(T)\|_\infty.
\]

If a higher-accuracy reference solver is used, identify it separately rather than calling another Euler grid the truth.

## Gate 6 — physical / domain plausibility

Domain-specific models must document whether signs, units, coupling directions, recovery rates, control bounds and service-state meanings are physically interpretable for the application.

Passing software tests is insufficient.

## Gate 7 — benchmark eligibility

An implementation is benchmark-eligible only after Gates 1–4 pass. A performance comparison involving a known non-conforming solver is invalid.

## Promotion rules

| Status | Minimum evidence |
|---|---|
| `PLANNED` | scientific role declared |
| `LEARNING` | prototype/exploratory work, no correctness claim |
| `IMPLEMENTED` | runnable implementation exists |
| `TESTED` | implementation-specific tests pass |
| `VALIDATED` | frozen cross-language conformance passes and provenance is recorded |
| `BENCHMARKED` | validated implementation included in controlled benchmark protocol |

## Failure policy

A failed check remains visible until corrected. Do not relabel a failure as a version difference without demonstrating that the implementation intentionally follows a different declared model specification.
