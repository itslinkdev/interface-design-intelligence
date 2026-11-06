# Design audit — use only for substantial review
Record **observed evidence** (screen/component + state), severity, user impact, smallest safe fix, verification.

## Prioritize
- **P0:** broken task, data loss, security/privacy harm, severe accessibility blocker.
- **P1:** major confusion, unworkable interaction, serious contrast/focus/layout regression.
- **P2:** hierarchy, spacing, theme, touch, feedback, copy issues with noticeable impact.
- **P3:** cosmetic polish not impacting task success.

## Scan
1. User's key task and primary action clear? Hidden capabilities? Navigation predictable?
2. Grouping, hierarchy, font sizing, density, icon alignment, radius/spacing and semantic color consistent?
3. Inputs labeled, required/optional apparent, actionable validation, paste/autofill functional?
4. Keyboard, focus, screen-reader, touch target, contrast, zoom/reflow and reduced motion considered?
5. States for loading/error/empty/selected/destructive operations complete and honest?
6. Responsive/theme/platform variants appropriate; no animation lag or unintended changes?

Return prioritized findings, not fabricated scores. Label untested checks explicitly.
