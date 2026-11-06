# Accessibility quality gates (web: WCAG 2.2 AA oriented)
**Use when:** accessibility review, nonstandard widgets, keyboard, touch, contrast, form semantics.

- Use native semantic elements first. All actionable controls require accessible names, predictable focus order, visible focus, and keyboard operation; dialogs manage focus on open/close.
- **Text contrast:** ≥4.5:1 normal, ≥3:1 large; **non-text:** ≥3:1 for applicable essential UI/graphics. Exceptions apply; check current WCAG text, rendered states, and backdrops.
- **Targets:** aim for comfortable 44×44 CSS pixel touch areas as design guidance. WCAG 2.2 SC 2.5.8 (AA) uses a *24×24 CSS pixel* minimum or sufficient spacing/other exceptions; 44×44 is not the AA minimum. 2.5.5 enhanced target is 44×44 (AAA) with exceptions.
- Labels should persist independently of placeholders; error associations (`aria-describedby`/`aria-errormessage` as appropriate), required state, and status announcements must be tested.
- Do not communicate state by color alone. Support text scaling, 200% zoom and narrow-width reflow as applicable, high-contrast themes, and reduced motion.
- Custom combobox, tabs, sliders, switches follow WAI-ARIA APG patterns and keyboard expectations. Semantic ARIA is not a replacement for functional keyboard behavior.
- Consider locale, RTL, screen readers, non-pointer input, visible focus not obscured by sticky headers.

**Verification:** use automated scanners as a baseline; verify keyboard sequence, screen reader names/roles/values, touch and focus visually. An automated pass does not prove WCAG conformance.

Authoritative sources: https://www.w3.org/TR/WCAG22/ and https://www.w3.org/WAI/ARIA/apg/patterns/ .
