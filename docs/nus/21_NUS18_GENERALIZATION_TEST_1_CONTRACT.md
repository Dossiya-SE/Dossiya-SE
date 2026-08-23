# NUS-18 — Generalization Test #1 Contract

## Paper identity

**Paper:** NUS-18  
**Title:** *An integrated energy-emergy approach to building form optimization: Use of EnergyPlus, emergy analysis and Taguchi-regression method*  
**DOI:** `10.1016/j.buildenv.2014.10.013`

Zotero parent key, attachment key, and focal-PDF SHA-256 must be resolved and verified before any extraction run.

## Test objective

NUS-18 is not another calibration paper. It is the first true generalization test of Generic NUS Evidence Engine V1.

The governing question is:

```text
Can the frozen engine process a structurally different paper correctly
without bespoke pipeline redesign?
```

## Success criterion

```text
NUS18_SUCCESS =
  correct source identity
  AND complete read-only extraction
  AND complete physical-surface inventory
  AND applicable T001–T047 regressions pass
  AND independent certification passes
  AND scientifically defensible adjudication
  AND no paper-specific engine redesign
```

## What may change

Only paper-specific configuration/data should normally change:

```text
paper_id
parent_key
attachment_key
expected_pdf_sha256
source-derived claim counts
surface counts
scientific evidence content
scientific conclusions
final evidence count
```

## What must not change merely because this is NUS-18

```text
nine-role ontology
focality-before-role order
provenance architecture
surface-adjudication contract
output-nature visible-comment rule
role colors
zero-tag rule
exact-author-wording rule
mutation authorization equation
transactional writer contract
independent auditor contract
T001–T047 knowledge
```

## NUS-18 paper-specific scientific risk areas to test without hard-coding

The title indicates a combination of:

```text
building-form alternatives
EnergyPlus-based engineering/energy simulation
emergy analysis
Taguchi/regression analysis
optimization/decision selection
```

These are hypotheses about likely evidence structures only. The engine must derive the actual roles, transformations, metrics, outputs, and decisions from focal evidence rather than from the title or prior expectations.

## Required first-run sequence

```text
1. Identity verification
2. PDF SHA-256 lock
3. Live annotation baseline inventory
4. Read-only extraction
5. Atomic-claim construction
6. Physical table/figure/equation inventory
7. Master regression suite
8. Independent certification
9. Scientific adjudication
10. Human review
11. Geometry/schema/writer/auditor only after authorization
```

## Fail-closed rule

If NUS-18 reveals an apparent defect, first classify it:

```text
paper-specific scientific difference
vs
existing known failure class
vs
new general failure class
```

Only the third category can justify a generic engine modification.

## Anti-bespoke gate

Before adding any new code, answer:

```text
1. What exact observed failure occurred?
2. Why is it not already covered by T001–T047?
3. What paper-independent invariant does it violate?
4. What new permanent regression would reproduce it?
5. Does the proposed fix pass historical NUS-172/NUS-48 regression controls?
```

If these five questions cannot be answered, do not redesign the engine.

## Generalization metrics

Record:

```text
manual_execution_steps
manual_adjudication_actions
new_defect_count
new_general_failure_count
new_regression_count
bespoke_code_change_count
engine_files_changed
paper_config_fields_changed
```

Target:

```text
bespoke_code_change_count = 0
engine_files_changed = 0
```

for a clean first generalization pass.

## Output-nature contract for NUS-18

Visible nature is exposed only for outputs:

```text
Engineering output here is [evidence-grounded nature] : [exact author wording]
Sustainability output here is [environmental/economic/social/integrated] : [exact author wording]
```

No nature is added to PURPOSE, INTERVENTION, INPUT, ENGINEERING_METHOD, SUSTAINABILITY_TRANSFORMATION, SUSTAINABILITY_METHOD, or DECISION.

## Completion states

Possible outcomes:

```text
PASS_GENERALIZATION_NO_ENGINE_CHANGE
PASS_GENERALIZATION_WITH_NEW_GENERAL_REGRESSION
ABSTAIN_OR_FAIL_SOURCE_STATE
ABSTAIN_OR_FAIL_ENGINE
ABSTAIN_OR_FAIL_SCIENTIFIC
```

The preferred outcome is:

```text
PASS_GENERALIZATION_NO_ENGINE_CHANGE
```

That is the decisive evidence that the NUS architecture is becoming scalable.
