# Chapter Context

This file preserves durable conceptual and historical knowledge for Chapter 07. It is not the manuscript, a status dashboard, or a chronological task log.

## Chapter identity

- **Chapter:** CH07
- **Current title:** Cross-Case Synthesis and Industrial Validation
- **Repository:** `phd-ch07-cross-case`
- **Source of truth:** This repository owns Chapter 07 academic content; `phd-thesis-control` owns orchestration.

## Current state

- `main.tex` contains the complete first doctoral-quality Chapter 07 draft created under `CH07-001`.
- `references.bib` is chapter-local and contains only keys cited or retained for this chapter.
- `FIGURE_PLAN.md` records two original synthesis schematics that remain visible placeholders in the manuscript.
- The current work is uncommitted pending user review and explicit Git authorization.

## Scope and role

Chapter 07 owns the cross-case synthesis of the thermal and electroluminescence programmes and the explicit answer to canonical SRQ3. It compares methodological functions, evidence boundaries, traceability, dependability, and industrial-validation evidence. It does not repeat the detailed methods or results owned by Chapters 05 and 06, and it does not own the final answer to the overarching research question, the final thesis contribution list, thesis-wide significance, the final limitations synthesis, or future work, which remain Chapter 08 responsibilities.

The chapter is structured around:

1. purpose and limits of comparison;
2. the common methodological core;
3. modality-specific strategies;
4. experimental-evidence synthesis;
5. domain structure and traceability;
6. stage-wise dependability and error propagation;
7. industrial validation;
8. robustness, human and operational evidence;
9. threats to validity and cross-case lessons;
10. the explicit answer to SRQ3 and the boundary with Chapter 08.

## Stable decisions

- Canonical SRQ3 is: “Which methodological and workflow principles for producing dependable and traceable inspection information are shared across the thermal and electroluminescence cases, and which remain specific to their sensing and industrial contexts?”
- The common cross-case chain is: sensor evidence → domain-relevant representation → localized prediction → structural association → interpretation or policy → structured, traceable inspection output.
- Comparability is methodological and evidential, not numerical. Thermal and EL metrics must not be combined into a leaderboard or treated as measurements from a common benchmark.
- The principal thermal adaptations are temperature-aware representation and downstream plant, module, row/string, geospatial, metadata, and retrieval context.
- The principal EL adaptations are module-to-cell decomposition and indexing, defect-to-cell relation, coverage calculation, configurable criticality policy, and module-level reporting.
- Dependability is assessed stage by stage. Component prediction, structural association, policy correctness, retrieval, and reporting require distinct evidence.
- Industrial validation is assessed through six thesis-level analytical dimensions: industrial data realism; component technical validation; structural and downstream validation; independent-domain validation; operational and human validation; and deployment evidence. This is not a standardized maturity scale.
- `Documented`, `documented but bounded`, `partial`, and `not established` are descriptive evidence states within individual dimensions. They are non-ordinal, do not form a composite score, and do not rank the thermal and EL cases.
- Both cases have documented industrial data realism and bounded component validation. Both have partial downstream evidence. Independent-domain, formal human/operational, and sustained deployment validation are not established.
- A configurable EL coverage-based criticality policy is documented, but the exact threshold values and their selection, derivation, calibration, optimization, expert provenance, and sensitivity are not documented.
- Traceability means retaining the source evidence, localized prediction, structural relation, interpretation or policy state, and final record so that a finding can be reconstructed and reviewed.
- The eight cross-case lessons are evidence-bounded propositions derived from the two PV inspection cases; they are not asserted as universal laws of industrial computer vision.
- The chapter uses exactly two planned original synthesis schematics; neither is scientific evidence.

## Content moved elsewhere

- Detailed thermal methods, results, caveats, and the SRQ1 answer remain in Chapter 05.
- Detailed EL methods, results, caveats, and the SRQ2 answer remain in Chapter 06.
- The final thesis conclusions, final overarching-research-question answer, consolidated thesis contributions, thesis-wide significance, final limitations synthesis, and future work remain in Chapter 08.

## Rejected or superseded approaches

- A cross-modality metric leaderboard is rejected because datasets, labels, evaluators, units, and interventions are not comparable.
- Industrial imagery is not treated as sufficient evidence of industrial validation or deployment.
- Strong component metrics are not treated as proof of structural, end-to-end, operational, or human-use correctness.
- Image-area coverage and configurable thresholds are not treated as validated physical or electrical severity.

## Important historical / implementation notes

THESIS-001 introduced the standard orchestration infrastructure without creating manuscript content.

CH07-001 created the first complete manuscript by synthesizing the final Chapter 04--06 manuscripts directly. No new experiment was performed. Numerical values retain their case-specific evaluators, and unresolved arithmetic, lineage, grouping, association, policy, runtime, and deployment questions remain explicit.

## Cross-chapter dependencies

- Chapter 01 supplies canonical SRQ3, the overarching question, and objective framework.
- Chapter 03 supplies the state-of-the-art gap concerning asset association, traceability, human review, reporting, and independent validation.
- Chapter 04 supplies the common methodological/evaluation framework and the rule that component and downstream claims remain separate.
- Chapter 05 supplies the thermal evidence and final SRQ1 answer.
- Chapter 06 supplies the EL evidence and final SRQ2 answer.
- Chapter 08 will use the Chapter 07 synthesis to answer the overarching question and state the final thesis conclusions.

## Open issues

- Create and approve final artwork for `FIG-CH07-01` and `FIG-CH07-02` without changing their evidential role.
- Resolve source-level unknowns only if authoritative evidence becomes available: thermal dataset lineage and electrical-string ground truth; EL evaluator, aggregation, grouping, association rule, and policy calibration; and runtime, human-use, and deployment evidence in both cases.
- Validate compilation in an available LaTeX environment if the current environment cannot render the chapter.

## Relevant decisions

No accepted decisions recorded yet.

## Relevant completed tasks

- `THESIS-001` — bootstrap chapter repository infrastructure.
- `CH07-001` — complete first draft and final targeted academic hardening of cross-case synthesis and industrial validation (worktree state pending review and Git checkpoint).
