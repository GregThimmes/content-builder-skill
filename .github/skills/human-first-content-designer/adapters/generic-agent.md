# Generic agent integration

## System/developer instruction

When producing content intended for people to read or use, invoke the Human-First Content Designer methodology in `SKILL.md`. Treat it as the required editorial and experience-design process.

Before generating:
1. Identify the audience, starting knowledge, context, task, desired outcome, and primary message.
2. Establish what is verified, inferred, and unknown from the source.
3. Choose Create, Transform, or Evaluate mode.
4. Select the smallest useful format and pattern.

Before delivering:
1. Remove filler and content that does not serve the reader.
2. Apply the relevant plain-language, cognitive-load, structure, and accessibility guidance.
3. Score and revise using the evaluation rubric.
4. State what was actually tested and disclose material limitations.

## Suggested invocation payload

```text
MODE: Create
AUDIENCE: [reader]
STARTING KNOWLEDGE: [what they know]
READER CONTEXT: [why they opened this]
READER TASK: [what they need to do]
DESIRED OUTCOME: [observable result]
SOURCE MATERIAL: [provided content or source locations]
OUTPUT FORMAT: [HTML, Markdown, one-pager, etc.]
CONSTRAINTS: [brand, platform, length, accessibility, security]
```

## Tooling expectations

If file creation is available, create the artifact as a file and return its path. If browser rendering is available, inspect the rendered page at desktop and narrow widths. If no browser or accessibility tooling is available, do not imply those tests were run.
