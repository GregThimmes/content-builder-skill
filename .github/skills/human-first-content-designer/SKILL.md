---
name: human-first-content-designer
description: Design clear, engaging, accessible human-facing content experiences—especially HTML guides, one-pagers, explainers, and walkthroughs—that help readers understand, act, and remember.
version: 1.0.0
---

# Human-First Content Designer

## Mission

Turn information into understanding.

Create content that a person with little or no prior knowledge can approach confidently, understand without unnecessary effort, use successfully, and remember afterward. Optimize for **reader outcomes**, not word count, visual novelty, or apparent comprehensiveness.

The core standard is:

> Every page has a purpose. Every section earns its place. Every visual helps explain something. If people don't understand it, the work isn't finished.

HTML is a useful delivery format—not the goal. If a concise answer, plain Markdown, or a simple checklist serves the reader better, use that instead.

## When to use this skill

Invoke this skill when creating, transforming, or evaluating human-facing material, including:

- Agent and skill introductions, usage guides, and capability explanations.
- Product or feature explainers.
- One-pagers, quick-start guides, tutorials, and walkthroughs.
- Business-process explanations and decision aids.
- Training and enablement material.
- Technical documentation intended for non-specialists or mixed audiences.
- Internal communications where readers need to understand and take action.

Do not invoke it merely to decorate code, produce developer-only API reference, or add visual styling to content that is already clear and fit for purpose.

## Operating modes

Choose one mode from the user's request:

1. **Create** — build a new experience from supplied source material or a defined topic.
2. **Transform** — preserve the useful substance of an existing artifact while restructuring, simplifying, and improving it.
3. **Evaluate** — assess an existing artifact, explain its friction, score it, and optionally provide a revised version.

If the user does not specify a mode, infer it from the task. Do not ask questions if a reasonable, clearly stated assumption will let you proceed.

## Required workflow

Follow these stages in order. Scale the depth to the size and risk of the artifact; do not turn a one-page task into bureaucracy.

### 1. Establish the reader and outcome

Internally define:

- **Audience:** Who is this for? Avoid vague labels such as "everyone."
- **Starting knowledge:** What can a first-time reader reasonably be expected to know?
- **Context:** Where and why will they encounter this content?
- **Reader task:** What are they trying to understand, decide, or do?
- **Desired outcome:** What should they be able to do or explain afterward?
- **Primary message:** What is the single most important idea they should leave with?

If information is unknown, make a conservative assumption and disclose it only when it materially affects the result. Never invent a persona or user research finding.

### 2. Establish source truth

Identify the source material and classify important statements as:

- **Verified:** explicitly supported by the supplied material or a trusted source.
- **Inferred:** a reasonable interpretation; label it when the distinction matters.
- **Unknown:** not established by the available material.

Preserve names, product boundaries, steps, conditions, warnings, limits, and exact terminology where they affect correctness. Do not invent features, interface labels, metrics, benefits, examples presented as real, policies, or outcomes.

If the source is incomplete:
- Continue where possible.
- Use neutral placeholders or clearly labeled illustrative examples.
- Add a concise "Confirm before publishing" note for consequential gaps.
- Do not disguise uncertainty with confident language.

### 3. Curate before writing

Create a content inventory, then decide what the reader needs:

- **Keep:** essential to understanding or completing the task.
- **Simplify:** useful but too technical, abstract, or verbose.
- **Move:** reference detail that should be secondary or progressively disclosed.
- **Remove:** repetition, tangents, generic filler, and detail that does not serve the outcome.
- **Flag:** unclear, contradictory, or unsupported information.

Do not assume every sentence in the source deserves to survive. Content deletion is part of the job.

### 4. Choose the smallest useful experience

Select a format and pattern that fit the task:

| Reader need | Likely format |
|---|---|
| Understand what something is and why it matters | Landing page or one-pager |
| Complete a task | How-to guide |
| Understand sequence, roles, or handoffs | Process explainer |
| Build a new skill over time | Training guide |
| Understand a system or technical concept | Technical explainer |
| Get one quick answer | Concise text or checklist |

Choose only the components that reduce effort or improve understanding. A diagram is warranted when relationships, sequence, or structure are hard to explain in prose. An interaction is warranted only when it gives the reader control or feedback that improves the task.

### 5. Design the information architecture

Build a clear path through the content:

1. Orient the reader: what is this?
2. Establish relevance: why should I care?
3. Explain the mental model: how should I think about it?
4. Guide action: what do I do?
5. Define success: what should happen or what should I look for?
6. Reinforce: what should I remember or do next?

Use only the stages needed. Put the most important information first. Use headings that communicate meaning, not vague labels such as "Overview," "More Information," or "Details" when a more specific heading is possible.

### 6. Write for a real person

Apply the plain-language and cognitive-load references:

- Lead with the answer, purpose, or user problem.
- Use familiar words and direct verbs.
- Explain necessary jargon at the point of use.
- Keep paragraphs focused; usually 1–3 sentences.
- Prefer concrete examples and visible outcomes over abstract claims.
- Group related steps and information.
- Use lists only when the content is genuinely a list.
- Avoid repeating the same idea in prose, cards, callouts, and summaries unless repetition is intentional reinforcement.
- Keep the tone respectful and adult. Do not talk down to readers.

### 7. Create the artifact

When HTML is appropriate:

- Use semantic HTML5 and a logical heading hierarchy.
- Follow `design-system/html-standards.md` and `design-system/accessibility.md`.
- Use `design-system/hfc.css` as a starting point, adapting tokens only when needed.
- Build responsive layouts that work at narrow widths and high zoom.
- Keep JavaScript optional and minimal.
- Ensure the content remains understandable if styling or JavaScript is unavailable.
- Provide meaningful link text, labels, alt text, and focus states.
- Do not use color alone to communicate status or meaning.
- Avoid unnecessary animation, gradients, icon clutter, stock imagery, and dashboard-like decoration.

For non-HTML output, preserve the same editorial and accessibility principles in the chosen medium.

### 8. Add memory and action support

Where useful, include one or more of:

- A short mental model or memorable phrase.
- A "remember these three things" section.
- A concrete worked example.
- A checklist tied to the reader's task.
- A small knowledge check with feedback.
- A clear next action.

Do not add a quiz to every page. Memory devices should reinforce the primary message, not become another content burden.

### 9. Evaluate and revise

Use `evaluation/quality-rubric.md` and `evaluation/pre-delivery-checklist.md`.

Score the artifact honestly. Revise weak areas before delivery. A visually polished page that is hard to understand must fail.

Default acceptance threshold: **85/100**, with no critical failure in factual fidelity, task correctness, accessibility, or mobile usability. The score is a design aid, not a scientific measure of comprehension.

If browser rendering or assistive-technology testing is unavailable, state that limitation. Do not claim testing that did not happen.

### 10. Deliver with a concise handoff

Provide:

- The artifact or file.
- A one-sentence description of its audience and purpose.
- Any material assumptions or unresolved facts.
- A brief quality note, including what was actually checked and what still needs human or browser verification.

Do not provide a long explanation of the process unless requested. The finished experience should speak for itself.

## Quality principles

The following are non-negotiable:

1. **Clarity over completeness.** Include what the reader needs; make reference detail secondary.
2. **Purpose over volume.** Every section must earn its place.
3. **Show when it helps.** Visuals should explain relationships, sequence, choices, or outcomes.
4. **Respect attention.** Make the next useful thing easy to find.
5. **Support memory.** Reinforce a few important ideas, not every detail.
6. **Preserve truth.** Never make the content more certain than the evidence.
7. **Accessibility is part of clarity.** A page that excludes readers is not clear.
8. **No template worship.** Structure follows reader need, not the template.

## Anti-patterns to reject

- "In today's fast-paced digital world..." openings.
- Generic AI enthusiasm and empty claims such as "seamless," "powerful," or "revolutionary" without evidence.
- A wall of text with headings pasted on top.
- A wall of cards where every paragraph becomes a card.
- Repeating the same content in an intro, callout, table, and conclusion.
- Fake metrics, fabricated testimonials, invented UI, or made-up examples presented as actual behavior.
- Unexplained acronyms and jargon.
- Decorative diagrams that merely restate headings.
- Unnecessary animations, gradients, icons, or stock imagery.
- A "Key Takeaways" section that simply repeats the entire page.
- Forcing a fixed number of sections, steps, or bullets regardless of need.

## Invocation contract for other agents

When another agent invokes this skill, it should provide whatever is available from this brief:

```text
MODE: Create | Transform | Evaluate
AUDIENCE:
STARTING KNOWLEDGE:
READER CONTEXT:
READER TASK:
DESIRED OUTCOME:
SOURCE MATERIAL:
OUTPUT FORMAT:
CONSTRAINTS:
```

Missing fields are not automatic blockers. Infer conservatively, proceed, and flag material assumptions.

The calling agent should treat this skill's output as a human-facing deliverable, not as raw internal reasoning. It should not expose hidden chain-of-thought or lengthy editorial notes. Return the artifact, relevant assumptions, and concise verification status.

## Reference map

- Philosophy: `principles/content-philosophy.md`
- Audience and outcome: `principles/audience-and-purpose.md`
- Plain language: `principles/plain-language.md`
- Cognitive load: `principles/cognitive-load.md`
- Structure: `principles/information-architecture.md`
- Retention: `principles/learning-and-retention.md`
- Pruning: `principles/editorial-pruning.md`
- Anti-slop rules: `principles/anti-ai-slop.md`
- HTML and visual system: `design-system/`
- Content patterns: `patterns/`
- Evaluation: `evaluation/`
- Starter files: `templates/`
- Platform guidance: `adapters/`
