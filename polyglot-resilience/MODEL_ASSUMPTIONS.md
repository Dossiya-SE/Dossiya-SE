# Model Assumptions and Interpretation Boundary

`PRK-1.0` is a research computing kernel for studying coupled service-state dynamics. It is not presented as a universally validated law of infrastructure resilience.

## State normalization

Each component

\[
x_i(t)\in[0,1]
\]

represents a normalized service state, where interpretation of 0 and 1 must be specified by the application. The projection operator enforces numerical admissibility; it does not prove that the underlying physics truly evolves by hard saturation.

## Degradation operator

The matrix \(D\) contributes through

\[
-Dx.
\]

The baseline contract allows a full matrix. A diagonal-only degradation model is a reduced model and must be labeled as such.

## Interdependency operator

The matrix \(A\) represents directed interdependency/interface effects acting on the nonlinear transformed state

\[
A\tanh(x).
\]

No symmetry is assumed:

\[
A_{ij}\neq A_{ji}
\]

in general. The sign and magnitude of each element require domain-specific interpretation.

## Recovery

The recovery term

\[
r\odot(1-x)
\]

is state-dependent and vanishes as service approaches one. The baseline assumes

\[
r_i\ge0.
\]

This form is a modeling choice; it does not imply every real recovery process is linear in service deficit.

## Hazard forcing

The baseline subtracts \(h\):

\[
-h.
\]

Positive hazard therefore depresses the instantaneous service derivative, holding all other terms fixed. A different sign convention requires a different semantic contract.

## Control

The control term

\[
Bu
\]

allows interventions to influence multiple sectors. The baseline contract does not impose an optimization objective, cost function, actuator limits or control law. Those belong to a higher-level decision/control specification.

## Nonlinearity

The baseline uses elementwise `tanh`. This is a bounded smooth coupling map selected for a reproducible reference kernel, not an empirical claim that infrastructure interfaces universally follow hyperbolic tangent response curves.

## Time discretization

The reference implementation uses explicit Euler. Consequently:

- results depend on \(\Delta t\);
- stability is not guaranteed for arbitrary parameters or time steps;
- cross-language equality at one \(\Delta t\) is not evidence of time-discretization convergence;
- convergence must be assessed separately using decreasing step sizes.

## Resilience metric boundary

The scalar

\[
R_{\mathrm{AUC}}=T^{-1}\sum_t w^Tx_t
\]

is a weighted mean-service statistic. It can conceal different minima, outage durations, recovery times, threshold violations and distributional effects. It must not be described as a complete resilience metric without additional justification.

## Scientific validity hierarchy

The project distinguishes:

```text
mathematical consistency
≠ software correctness
≠ cross-language agreement
≠ numerical convergence
≠ physical plausibility
≠ empirical validation
```

Each level requires its own evidence.
