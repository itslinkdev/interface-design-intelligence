# Liquid Glass: restrained depth
**Use when:** floating navigation, compact toolbar, overlay controls or a deliberately translucent brand surface. **Avoid when:** long-form text, dense tables, full-page backgrounds or low-end devices make translucency a liability.

## Visual recipe
- Separate **functional foreground** from **opaque content**. Use a clear, pill-like layer for a *few* primary controls, not a frosted card for every section.
- Use partial transparency, a narrow light edge, a subtle inner highlight and restrained shadow. Behind it, meaningful colorful content can provide depth.
- If custom styling is needed on the web, begin with a solid/translucent fallback; enhance only when `backdrop-filter` is available. This is a **glass-inspired approximation**, not Apple's native Liquid Glass shader/refraction system.

```css
.floating-tools {
  color: #17203b;
  background: rgba(244, 248, 255, .94); /* always-readable fallback */
  border: 1px solid rgba(255,255,255,.78);
  border-radius: 999px;
  box-shadow: 0 8px 28px rgba(12,28,58,.16), inset 0 1px rgba(255,255,255,.9);
}
@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .floating-tools {
    background: rgba(244,248,255,.76);
    -webkit-backdrop-filter: blur(12px) saturate(125%);
    backdrop-filter: blur(12px) saturate(125%);
  }
}
@media (prefers-reduced-transparency: reduce) {
  .floating-tools { background: #f3f7ff; -webkit-backdrop-filter: none; backdrop-filter: none; }
}
@media (prefers-contrast: more) {
  .floating-tools { background: #fff; border-color: #3d465a; -webkit-backdrop-filter: none; backdrop-filter: none; }
}
```

## Performance, states and platforms
- Limit blur to a few small static surfaces. Avoid nested backdrops, huge 40px+ blurs, backdrop blur animations, and continuous filter updates. Never use `will-change: backdrop-filter` indiscriminately; test on target GPUs.
- Animate optional entrance through `transform`/`opacity`, only with reduced-motion fallback. Do not make translucent focus indicators; maintain solid visible focus rings, contrast and hit targets.
- Apple apps: prefer system bars/materials and platform APIs, allowing OS accessibility preferences. Windows, Qt, Android and web: follow their own materials and user settings rather than pretend their systems are Apple.
- Test legibility on the *worst-case moving background*, low contrast themes and hardware acceleration disabled/limited.

Sources: https://developer.apple.com/design/human-interface-guidelines/materials ; https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter
