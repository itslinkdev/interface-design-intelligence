# Dark-mode design: surfaces, color and readable depth
**Use when:** building or auditing a dark theme, its contrast, elevation or theme preference. Skip for unrelated UI tasks.

## Apply principles, not absolutes
1. **Backgrounds.** Start with semantic roles, not a magic hex: `canvas → surface → raised → interactive`. Near-blacks such as `#121212`, `#0B0B0C`, `#0E0E10` are options. Pure `#000000` is valid for OLED/immersive contexts and can support established platform design. Avoid using black solely as a default without testing.
2. **Depth.** Differentiate adjacent surfaces with subtle *tonal* changes, measured outlines, spacing and occlusion. Elevated controls often use lighter surfaces, but native/platform materials take precedence. Dark shadows alone have limited effect; **don't ban them** for overlays/popovers when they actually improve separation. Keep 2–3 purposeful surface tiers instead of making every card different.
3. **Chroma.** Reduce aggressively saturated *large areas* when they cause glare or hierarchy problems. Accent icons and important actions may be vivid if contrast, brand and meaning work. No universal saturation percentage or "tone 200–500" rule exists across color models; inspect rendered colors.
4. **Text.** Define `text-primary`, `text-secondary`, `text-muted` as measured semantic tokens. `#FFFFFF` is valid; slightly softer near-white can reduce glare. Suggested fixed white-alpha levels (87/65/30%) are **not guaranteed readable** on every surface, especially low-opacity copy. Measure the final composited foreground on each background; never use low-opacity text to convey required information.
5. **Accessibility.** WCAG 2.2 AA: normal text >=4.5:1, large text >=3:1, essential graphical/control indicators >=3:1 (subject to the criteria's exceptions). Test placeholders, focus rings, separators essential for understanding, selected/pressed/disabled, error states, overlays and light/dark pairings. Do not use color alone to encode state. Accessibility preferences/high contrast may override brand tokens.
6. **Theme preference.** Follow the OS theme by default and support changes while the app is running. Add Light/Dark/System controls only if useful for the product and consistent with its platform (Apple generally recommends respecting the system setting over redundant per-app controls). Theme switches must update native system colors, focus, forms, charts and modal surfaces—not merely invert pixels.

## Compact role-token example (illustrative, not a mandatory palette)
```css
[data-theme="dark"] {
  --ui-canvas: #0e0e10;
  --ui-surface: #19191d;
  --ui-raised: #25252b;
  --ui-border: #42424b; /* subtle decorative border */
  --ui-control-outline: #80808d; /* check interactive indicators */
  --ui-text: #f4f4f5;
  --ui-text-secondary: #bfc0ca;
  --ui-accent: #aaaaff;
}
```
Always verify actual text/accent pairings against the *rendered* target surface. CSS above is only one aesthetic example; prefer platform-native semantic colors when available. Avoid overproducing tokens unless the product requires them.

**Optional local check:** `python scripts/check_contrast.py '#BFC0CA' '#19191D' --target normal` (or add `--alpha 0.30` for translucent foreground). It checks solid sRGB compositing only; still inspect real gradients, glass and interactions.

**Primary references:** [W3C text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), [W3C non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html), [Apple Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode), [Material 3 tonal elevation](https://developer.android.com/develop/ui/compose/designsystems/material3).

**QA:** test light/dark, dim/bright screens, color-vision differences, reduced transparency and high-contrast; judge legibility first and decorative style second.
