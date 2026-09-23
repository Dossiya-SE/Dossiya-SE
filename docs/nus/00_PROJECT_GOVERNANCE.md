# NUS Frozen-37 Project Governance

## Scope

This archive governs the NUS construction-sustainability evidence workflow built around a fixed 37-paper corpus. The unit of analysis is one focal publication. Paper IDs are permanent and are written as `NUS-<ID>`.

The external ledger/repository is the machine/audit layer. Zotero remains the human reading and visible evidence layer. The two must stay synchronized through explicit identifiers, hashes, and release gates.

## Evidence hierarchy

1. Focal PDF bytes and verified identity.
2. Read-only source map / page-line extraction.
3. Atomic claim register and physical-surface inventory.
4. Candidate scientific evidence.
5. Regression and independent certification.
6. Scientific adjudication.
7. Explicit human approval.
8. Exact geometry and proposed final state.
9. Writer and independent auditor dry-runs.
10. Transactional Zotero mutation.
11. Zero-delta rerun and independent final audit.
12. Frozen release package and hashes.

## Fail-closed principle

At every stage:

```text
uncertainty or failed control
→ ABSTAIN_OR_FAIL
```

Never guess a missing value, unit, link, method, role, provenance state, or author meaning. Never silently reconcile contradictory evidence.

## Scientific/source-state separation

A software/runtime failure does not imply a scientific failure. The workflow distinguishes at least:

- source-state failure;
- runtime/package failure;
- extraction failure;
- physical-surface failure;
- semantic candidate-generation failure;
- independent-certification failure;
- scientific-adjudication uncertainty;
- geometry/schema/dry-run failure;
- post-write audit failure.

Engineering defects should approach zero. Scientific uncertainty must remain allowed and should resolve to `ABSTAIN` when the paper cannot support a defensible conclusion.

## Frozen corpus discipline

- Do not substitute a different PDF or metadata record without identity re-verification.
- Do not change canonical paper IDs.
- Do not preset the final number of annotations.
- Do not allow a paper-specific expected result to drive generic engine logic.
- Do not treat a primary harness PASS as scientific closure; independent certification is mandatory.
- Do not label AI-assisted adjudication as human reference/approval.

## Development rule

Every legitimate engine correction follows:

```text
Observed failure
→ general invariant
→ permanent regression
→ rerun historical regression suite
```

Do not add complexity merely because an alternative implementation appears cleaner.

## Current calibration policy

- `NUS-172`: first rigorous reference/calibration architecture.
- `NUS-48`: final heavy hardening/stress-test paper.
- `NUS-18`: generalization test 1.
- `NUS-191`: generalization test 2.
- `NUS-67`: final generalization test.
- `NUS-15` onward: production operation unless a genuinely new failure class appears.

The objective is to make assurance increase while manual execution steps remain approximately constant.
