# Human-First HTML design system

The design system provides a restrained visual language and reusable CSS primitives. It should support the content—not become the content.

## Files

- `hfc.css` — starter stylesheet and accessible component primitives.
- `visual-guidelines.md` — hierarchy, layout, and visual restraint.
- `html-standards.md` — semantic markup and responsive implementation.
- `accessibility.md` — WCAG 2.2 AA-oriented implementation guidance.
- `components.md` — component selection and usage rules.

## Design direction

Use editorial typography, generous but efficient spacing, strong contrast, a narrow reading measure, and a clear primary action. The default style is calm and professional rather than flashy.

Customize tokens to match a brand when required, but do not weaken contrast, focus visibility, or readability to match a visual theme.

## CSS usage

For a page in `templates/`, link to:

```html
<link rel="stylesheet" href="../design-system/hfc.css">
```

For a deployed page, copy the stylesheet to the page's asset location and update the path. The sample in `examples/` is self-contained so it can be opened directly.
