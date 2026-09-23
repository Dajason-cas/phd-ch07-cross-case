# Agent Guidance

## Repository role and boundaries

- This repository is the academic source of truth for PhD Thesis Chapter 07, currently titled **Cross-Case Synthesis and Industrial Validation**.
- `phd-thesis-control` owns orchestration and thesis-wide operational knowledge; it does not own or duplicate this chapter's manuscript content.
- Approved tasks may originate in `phd-thesis-control/tasks/`. Implement only the repositories and scope listed in the approved task.
- The task file is the execution contract. Do not assume ChatGPT Work and Codex share conversation history.
- Consult relevant global `THESIS_OUTLINE.md`, `STYLE_GUIDE.md`, `GLOSSARY.md`, `SOURCE_REGISTER.md`, and accepted decisions selectively when required.

## Persistent chapter context

- Consult `CHAPTER_CONTEXT.md` before substantive work.
- Perform the Chapter Context Update Check before completing substantive work and promote durable knowledge to the appropriate canonical file.
- Do not use chapter context as a chronological task log.

## Academic, LaTeX, and scope integrity

- Never invent references, citations, papers, authors, DOIs, datasets, experiments, figures, results, metrics, methods, evidence, or conclusions.
- Mark missing, uncertain, inferred, or unverified information explicitly and preserve source traceability.
- When LaTeX exists, preserve compilability, labels, references, citations, and figure paths whenever practical.
- Do not create or restructure manuscript content unless the approved task requires it.
- Preserve unrelated work; do not opportunistically rewrite material or silently modify an unlisted repository.

## Git and reporting

- Do not commit or push unless the user explicitly authorizes it.
- Report inspected and changed files, validation, Chapter Context Update outcome, Git status, and unresolved issues.
- Keep responses concise; do not print full diffs, full files, or long command output unless requested.
