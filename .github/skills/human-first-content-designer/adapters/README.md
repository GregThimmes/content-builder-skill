# Platform adapters

Keep platform-specific packaging separate from the core methodology. The root `SKILL.md` is the source of truth. An adapter should explain how a particular agent environment discovers and invokes the skill; it should not fork or silently change the editorial rules.

## Adapter responsibilities

- Identify where the platform expects skill instructions.
- Copy or reference the core `SKILL.md`.
- Make supporting reference files available to the agent.
- Define how the calling agent passes audience, source material, constraints, and output requirements.
- Define where generated files are written and how they are returned.
- Preserve factuality, accessibility, and evaluation requirements.

Do not duplicate the full methodology in every adapter. Link to or package the canonical references.
