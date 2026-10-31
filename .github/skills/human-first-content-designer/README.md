# Human-First Content Designer

**Less content. More understanding.**

A reusable skill for turning complex, technical, or unfamiliar source material into clear, engaging, accessible content experiences that help people understand, act, and remember.

This package is designed to work across agent platforms. The core methodology is platform-agnostic; platform-specific invocation instructions live in `adapters/`.

## Start here

1. Read [`SKILL.md`](SKILL.md). This is the skill's operating contract.
2. Review [`principles/`](principles/) for the editorial and learning principles behind the workflow.
3. Use [`design-system/`](design-system/) for HTML, accessibility, and reusable visual patterns.
4. Select a content pattern from [`patterns/`](patterns/) and a starter from [`templates/`](templates/).
5. Evaluate the result with [`evaluation/quality-rubric.md`](evaluation/quality-rubric.md) and [`evaluation/pre-delivery-checklist.md`](evaluation/pre-delivery-checklist.md).

## Repository map

```text
human-first-content-designer/
├── SKILL.md
├── README.md
├── principles/
│   ├── content-philosophy.md
│   ├── audience-and-purpose.md
│   ├── plain-language.md
│   ├── cognitive-load.md
│   ├── information-architecture.md
│   ├── learning-and-retention.md
│   ├── editorial-pruning.md
│   └── anti-ai-slop.md
├── design-system/
│   ├── README.md
│   ├── visual-guidelines.md
│   ├── html-standards.md
│   ├── accessibility.md
│   ├── components.md
│   └── hfc.css
├── patterns/
│   ├── README.md
│   ├── landing-page.md
│   ├── one-pager.md
│   ├── how-to-guide.md
│   ├── process-explainer.md
│   ├── training-guide.md
│   └── technical-explainer.md
├── templates/
│   ├── README.md
│   ├── landing-page.html
│   ├── one-pager.html
│   ├── how-to-guide.html
│   ├── process-explainer.html
│   ├── training-guide.html
│   └── technical-explainer.html
├── evaluation/
│   ├── quality-rubric.md
│   ├── pre-delivery-checklist.md
│   └── revision-protocol.md
├── examples/
│   ├── sample-brief.md
│   └── sample-agent-guide.html
├── adapters/
│   ├── README.md
│   ├── generic-agent.md
│   └── github-copilot.md
└── scripts/
    └── validate_package.py
```

## Quick invocation

Ask an agent to use the skill with a request such as:

> Use Human-First Content Designer to transform the supplied material into a concise, responsive HTML guide for first-time users. Prioritize comprehension and task completion over completeness. Apply the skill's workflow and evaluation rubric. Do not invent missing facts; flag them.

Supported modes:

- **Create** — create a new content experience from source material.
- **Transform** — improve an existing page, guide, or document.
- **Evaluate** — audit an existing content experience and recommend or apply revisions.

## Design intent

This is not a theme pack or a prompt that makes documents prettier. It is an editorial and experience-design method. The model is expected to make decisions about what to include, what to remove, how to explain it, and how to test whether the result works.

## Validation

Run the package's basic structural checks with:

```bash
python scripts/validate_package.py
```

This checks expected files and basic HTML structure. It is not a substitute for browser testing, an accessibility audit, or human comprehension testing.

## Assumptions and boundaries

- The skill can generate HTML and CSS as text artifacts. It does not automatically host, deploy, or test pages in every environment.
- WCAG 2.2 AA is the target, not a claim of conformance. Verify the rendered result with keyboard, screen-reader, zoom, contrast, and automated checks.
- The skill must preserve source truth. When source material is missing or ambiguous, it should state the gap rather than fill it with invented details.
- The templates are starting points, not mandatory page structures.
