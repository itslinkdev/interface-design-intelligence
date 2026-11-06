# Tailwind CSS implementation checks
**Use when:** Tailwind utility decisions, design tokens, theme variants, or class proliferation affect a task.

- Follow the project's installed Tailwind version and configuration; do not assume a specific major version or plugin.
- Reuse existing theme variables/utilities and component primitives. Avoid scattered arbitrary values when tokens already exist.
- Define semantic light/dark role tokens; `dark:` should reflect intended theme behavior, not mere inversion.
- Keep focus-visible, hover, active, disabled and reduced-motion variants distinct and accessible.
- Do not concatenate unrecognized dynamic class fragments that may be missed by class generation; use explicit mappings.
- Prefer simple, readable class composition; do not add a UI library just for an isolated component.
