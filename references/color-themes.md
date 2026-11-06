# Semantic color systems and themes
**Use when:** palette, dark mode, feedback colors, active states, visual emphasis.

- Inspect existing semantic tokens first (`surface`, `text`, `border`, `primary`, `danger`, `success`, `warning`, `focus`, `disabled`). Set role-based colors rather than hardcoded component hex values.
- **60/30/10** can spark initial palette balance (neutral/base, support, accent) but is *not* a measurable UI requirement. Reserve strongest emphasis for current task priorities.
- Distinguish selection, hover, pressed, keyboard focus, disabled, loading, success, warning, and error by more than hue. Ensure semantic meanings remain consistent.
- Dark mode is **not** simple RGB inversion. Build surface elevation and contrast for dark backgrounds; adjust chroma and brightness *per color*, verify brand identity and readability. For dark-specific depth/text/theme decisions, optionally read `references/dark-mode-design.md` instead of expanding this general guide.
- Pure white/black may be valid; off-white/near-black are stylistic options. Increasing saturation in light mode (or dark mode) is never automatic.
- **Contrast reference (WCAG 2.2 AA):** normal text ≥4.5:1; large text ≥3:1; essential non-text UI boundaries/graphics ≥3:1, with exceptions defined by WCAG. Focus should remain perceptible. Use computed luminance of rendered colors; account for transparency/gradients.
- Never signal errors/success only by red/green. Pair color with clear text, shape, status, or icon. Test color-vision differences and high-contrast/system themes when applicable.

**QA:** compare light and dark themes side by side, including muted text, placeholders, error borders, overlays, selected tabs, and disabled controls. Do not treat 'looks subtle' as proof of contrast.
