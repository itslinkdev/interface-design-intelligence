---
name: interface-design-intelligence
description: Design, implement, refine and audit accessible web, desktop and mobile UI. Use for component design, visual systems, dark themes, interaction and animation quality, or UI fixes; load task-specific guides only when needed.
license: MIT
metadata:
  version: "1.3.0"
---
# Interface Design Intelligence

## Contract
- Inspect actual UI, user task, code, existing tokens/components and platform first. Preserve working behavior and visual identity unless asked to change them.
- Mode: **PLAN** (choices and acceptance criteria), **BUILD** (implement and verify) or **AUDIT** (evidence-based findings; no edits unless asked).
- Priorities: correctness/safety > accessibility > user goals > platform patterns > consistency/performance > decoration. Design heuristics are not laws.

## Context discipline
- Start with **this file only**. Routine edits need **zero** references.
- For a concrete unresolved design choice, read a relevant *section* of **one** module; add another only as needed. Never bulk-read modules, catalog or diagrams. Prior reads still consume context.
- Find a specific rule via `python <skill-root>/scripts/find_pattern.py "topic" --limit 2`. Only open the recommended module if useful.
- If the user explicitly requests a style or a new aesthetic direction, use `python <skill-root>/scripts/find_style.py "style or project" --limit 2` and read **one** matching `styles/` recipe. Do not load style recipes during normal UX fixes.
- Stack adapters in `stacks/` are optional and used only for framework-specific questions. Keep project decisions brief; avoid re-reading.

## Routing
- Cognitive load → `references/ux-principles.md`; hierarchy → `references/visual-hierarchy.md`
- New visual identity → `references/aesthetic-direction.md`; token system → `references/design-system.md`
- Fonts → `references/typography.md`; spacing/radii → `references/geometry-spacing.md`
- Colors/themes → `references/color-themes.md`; dark-mode depth → `references/dark-mode-design.md`; forms/errors → `references/forms-inputs.md`
- Controls/navigation → `references/controls-navigation.md`; slider drag/easing → `references/slider-interactions.md`; feedback/loading → `references/feedback-states.md`
- Motion/jank → `references/motion-performance.md`; accessibility → `references/accessibility.md`
- Native/responsive → `references/platform-responsive.md`; ethics → `references/ethical-ux.md`

## Style guardrail
- For new identity work, select one primary visual direction; at most one supporting accent. Prioritize brand fit, task clarity, performance and accessible fallbacks over visual trends. Inspiration images are not reusable source assets.

## Execution
1. Diagnose context and task; distinguish observed issues from assumptions.
2. Choose the smallest coherent solution and load only necessary guidance.
3. Implement with established components; for new brands, choose a deliberate aesthetic direction.
4. Verify relevant interactions, keyboard/focus, contrast, screen sizes, themes and performance. Render if tools permit; don't claim tests not performed.
5. Report changed behavior, evidence, unresolved issues.

## Hard rules
Persistent labels, specific error messages, visible focus, semantic controls, and no color-only states. Provide one clear primary action per decision context; avoid dark patterns. Honor reduced motion and protect existing functionality.
