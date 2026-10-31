# GitHub Copilot in VS Code adapter

This adapter is a starting point for a repository-local workflow. Confirm the current Copilot instruction and prompt-file conventions in your organization's enabled version before publishing; platform conventions can change.

## Suggested repository placement

```text
your-repo/
├── .github/
│   ├── copilot-instructions.md
│   └── prompts/
│       └── human-first-content.prompt.md
└── skills/
    └── human-first-content-designer/
        ├── SKILL.md
        ├── principles/
        ├── design-system/
        ├── patterns/
        └── evaluation/
```

## Suggested repository instruction

Add a concise instruction to `.github/copilot-instructions.md`:

```markdown
When creating or revising content intended for human readers, use
`skills/human-first-content-designer/SKILL.md` and its supporting references.
Optimize for reader understanding, task success, and retention—not content
volume. Preserve source truth, remove filler, use accessible semantic HTML
when HTML is appropriate, and evaluate the result before delivery.
```

## Suggested prompt file

Create `.github/prompts/human-first-content.prompt.md`:

```markdown
---
mode: agent
description: Create or improve a human-first guide, one-pager, or explainer.
---

Use the Human-First Content Designer skill in
`skills/human-first-content-designer/SKILL.md`.

Task: ${input:task:What should the content help a reader understand or do?}
Audience: ${input:audience:Who will read it?}
Source material: ${input:source:What source material should be used?}
Output: ${input:output:HTML, Markdown, or another format?}

Follow the full workflow. Do not invent missing facts. Create the artifact,
evaluate it, revise it, and report any assumptions and checks not performed.
```

## Notes

- Keep the core skill files version-controlled with the project.
- Use repository instructions for durable behavior and a prompt file for explicit invocation.
- Do not assume the prompt file is automatically available in every Copilot surface; test the team's actual VS Code setup.
- Keep proprietary source material and internal LLM/API credentials out of generated examples.
