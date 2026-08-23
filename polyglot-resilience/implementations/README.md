# Native Implementation Layer

This directory contains numerical solvers only when they implement a declared kernel profile.

## Current native implementations

- `python/kernel.py` — `FULL_KERNEL`, reference implementation.
- `go/main.go` — `FULL_KERNEL`, native Go implementation.
- `javascript/kernel.mjs` — `FULL_KERNEL`, native JavaScript implementation.

All three consume the same canonical JSON fixture schema and emit the same output fields.

## Promotion rule

Source code alone does not justify a `VALIDATED` label. Implementations move through:

```text
PLANNED → LEARNING → IMPLEMENTED → TESTED → VALIDATED → BENCHMARKED
```

The machine-readable status lives in `../registry/implementation-registry.json`.

## Native implementation versus adapter

A language binding, API client, SQL layer, Bash workflow or LaTeX specification may be valuable without independently solving the kernel. Those artifacts are kept outside this directory or assigned a non-native profile so that interoperability claims remain precise.
