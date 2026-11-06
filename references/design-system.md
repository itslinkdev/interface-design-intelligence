# Lean design-system specification and generation
**Use when:** establishing a new design system, rebranding, or consolidating inconsistent components. **Skip** if the project already has usable tokens and needs only a local fix.

## Derive, don't overwrite
1. Inventory existing variables, component APIs, themes, fonts, spacing, breakpoints and iconography. Preserve what works.
2. Define semantic **color roles** (background, surface, foreground, muted, primary, destructive, success, warning, border, focus), not one-off hex values per component. Provide explicit theme values; never assume dark mode is an inversion.
3. Use a small spacing scale (4/8px multiples as a starting point), typography roles (body/title/caption/display), radii, border and shadow roles. Reuse role tokens across components.
4. Specify high-value components through a compact **state contract**: default, hover, focus-visible, active, selected, disabled, loading, and error only when applicable. Include keyboard semantics, responsive changes and escape routes.
5. Validate foreground/background pairs and non-text controls against relevant WCAG requirements. Do not claim untested combinations pass; adjust per rendered state.

## Optional artifact generator
If explicitly asked to scaffold CSS variables from a specification, use the **stdlib-only** script:
`python <skill-root>/scripts/build_tokens.py --config path/to/project-tokens.json --out path/to/tokens.css`
Config format: `examples/token-config.sample.json`. It emits literal semantic CSS custom properties from **provided values**, plus optional `--json-out` manifest. It **does not invent a palette, run contrast checks, or edit the application**. Make a project copy and choose values deliberately; never overwrite existing theme files without consent.

## Review
Is each token used more than once? Are colors named by meaning, not hue? Do input/button states stay predictable across themes? Does the system fit the product's visual thesis and platform? Can the developer update one token instead of dozens of components?

Catalog patterns (text-only): REF-037 (nested geometry), REF-039–040 (scales), REF-050–055 (states, semantic roles, consistency).
