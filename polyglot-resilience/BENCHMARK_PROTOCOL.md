# Benchmark Protocol — Polyglot Resilience Atlas

## Principle

Performance is measured only after a solver has passed the declared correctness and conformance gates.

```text
specification → implementation → conformance → convergence → benchmark
```

A faster incorrect implementation is not a scientific improvement.

## Benchmark questions

The benchmark layer is intended to answer distinct engineering questions:

1. What is the one-step latency for small state dimension \(n\)?
2. What is the throughput for long trajectories \(T\)?
3. How does runtime scale with dense matrix dimension \(n\)?
4. What memory footprint is required?
5. What is the initialization/startup overhead?
6. How well does the implementation parallelize where parallelism is part of its intended role?
7. Does the implementation preserve numerical conformance under optimized compiler/runtime settings?

## Benchmark populations

At minimum use state dimensions

\[
n\in\{10,100,1000\}
\]

for dense \(D\) and \(A\), with larger dimensions introduced only when memory requirements remain feasible and the comparison remains meaningful.

Candidate horizons:

\[
T\in\{1,10^2,10^4\}.
\]

The `n=10^4` case may be included for sparse or optimized implementations, but should not be presented as a comparable dense benchmark unless memory complexity is explicitly controlled.

## Workload generation

Benchmark inputs must be deterministic and generated from a registered seed. The generator configuration should record:

```text
BENCHMARK_ID
KERNEL_VERSION
SEED
N
M
T
DT
MATRIX_DENSITY
INPUT_SHA256
```

Benchmark input should not be chosen separately for each language.

## Warm-up and repetitions

Runtime systems with JIT compilation or VM warm-up must separate startup/warm-up from steady-state timing. Report both when relevant.

For each workload:

- execute at least one untimed validation run;
- use multiple timed repetitions;
- report median and dispersion, not only the single fastest run;
- record the timing method and whether process startup is included.

## Metrics

Required baseline metrics:

- wall-clock runtime;
- throughput in state updates per second;
- peak or representative memory where measurable;
- startup/initialization latency;
- maximum numerical deviation from the frozen/reference result.

Optional metrics:

- CPU utilization;
- parallel speedup and efficiency;
- energy consumption where a reproducible measurement method exists;
- binary/package size for deployment comparisons.

## Compiler/runtime provenance

Record at minimum:

```text
LANGUAGE
LANGUAGE_VERSION
COMPILER_OR_RUNTIME
COMPILER_VERSION
COMPILER_FLAGS
PLATFORM
CPU
OPERATING_SYSTEM
GIT_COMMIT
```

Optimized and unoptimized builds must not be mixed without labeling.

## Fairness boundary

Native implementations, bindings, service wrappers and browser clients solve different engineering problems. Do not place them in a single speed ranking without controlling for architecture.

Examples:

- native C++ vs native Rust kernel: potentially comparable;
- Python binding to a C++ kernel vs pure-Python solver: different implementation profiles;
- HTTP service vs in-process function: includes transport overhead;
- browser/WASM vs server-native solver: different deployment context.

## Numerical correctness during benchmarking

Every benchmarked result must still satisfy the conformance tolerance or an explicitly declared benchmark tolerance profile. Compiler optimizations that materially change scientific results invalidate the performance result.

## Reporting

Benchmark results belong under `benchmarks/results/` and should include:

- raw machine-readable measurements;
- environment/provenance manifest;
- summary table;
- plots generated from the raw measurements;
- interpretation that distinguishes observed performance from inferred engineering implications.

No benchmark ranking should be published before reproducibility and conformance evidence are available.
