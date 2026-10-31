# HTML implementation standards

## Semantic structure

Use:
- `<header>` for introductory or site-level content.
- `<nav aria-label="...">` for meaningful navigation.
- `<main>` for the primary content.
- `<section>` for thematic groups, with a heading.
- `<article>` for self-contained content where appropriate.
- `<aside>` for supporting content.
- `<footer>` for closing or metadata content.
- `<ol>` for ordered steps; `<ul>` for unordered collections.
- `<table>` only for tabular data, with headers.
- `<button>` for actions and `<a>` for navigation.

Do not use generic `<div>` elements when a semantic element better describes the content.

## Document essentials

Every HTML page should include:
- `<!doctype html>`
- `<html lang="en">` or the correct language
- UTF-8 charset
- viewport meta tag
- a specific `<title>`
- a useful meta description when appropriate
- one clear `<h1>`
- logical heading order
- a skip link when page navigation is present or the page is long

## Links and controls

- Link text should describe the destination or action.
- Buttons should have clear action labels.
- Every form control needs a programmatic label.
- Do not use placeholder text as the only label.
- Indicate required fields in text, not color alone.
- Avoid opening new tabs without a clear reason; if unavoidable, tell the reader.

## Responsive behavior

- Start with a single-column layout.
- Add columns only when they improve comprehension at larger widths.
- Avoid fixed widths and fixed heights for content.
- Allow tables to scroll horizontally only when necessary and provide context.
- Test at narrow mobile widths and at 200% zoom.
- Ensure long URLs and code blocks do not break the page.

## Progressive enhancement

Content and essential navigation must remain available without JavaScript. Prefer native HTML elements such as `<details>` and `<summary>` over custom widgets.

## Performance and portability

- Prefer local CSS and system fonts.
- Keep JavaScript small and optional.
- Avoid frameworks unless the project explicitly requires one.
- Do not embed huge base64 images in normal documentation.
- Keep pages usable when external fonts, scripts, or images fail.
