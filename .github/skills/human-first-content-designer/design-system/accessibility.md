# Accessibility target: WCAG 2.2 AA

Target WCAG 2.2 AA for generated HTML. This document is implementation guidance, not a certification or conformance claim. The rendered artifact must still be tested.

## Required practices

### Structure and navigation
- Use semantic landmarks and a logical heading hierarchy.
- Include a skip link for pages with repeated navigation or substantial length.
- Ensure all functionality is keyboard operable.
- Provide visible focus indicators that are not obscured.
- Keep focus order logical.

### Text and contrast
- Meet WCAG AA contrast: generally 4.5:1 for normal text and 3:1 for large text.
- Ensure meaningful UI boundaries and graphical information have sufficient contrast.
- Do not communicate meaning through color alone.
- Support text resizing and browser zoom without loss of content or functionality.
- Use readable line length and spacing.

### Images and media
- Provide concise, useful alt text for informative images.
- Use empty alt text (`alt=""`) for decorative images.
- Do not put essential instructions only in an image.
- Caption or provide alternatives for meaningful audio/video content.

### Interaction
- Use native controls where possible.
- Give controls accessible names.
- Provide clear instructions and error messages.
- Avoid hover-only information.
- Avoid time limits unless essential; provide adjustment or extension where applicable.
- Respect `prefers-reduced-motion` if motion is used.

### Reflow and touch
- Support narrow viewport reflow without two-dimensional scrolling for ordinary content.
- Make touch targets comfortably large; use WCAG 2.2 target-size requirements where applicable.
- Do not rely on precise pointer gestures.

## Before claiming accessibility

Check:
- Keyboard-only operation.
- Visible focus.
- Heading and landmark structure.
- Contrast.
- Zoom and reflow.
- Link and control names.
- Screen-reader reading order.
- Form labels and error handling, if forms exist.
- Reduced motion, if motion exists.

Automated tools can find some issues but cannot establish that content is understandable or that every interaction works. State exactly which checks were performed.
