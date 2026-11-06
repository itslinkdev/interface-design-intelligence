# Analog Grain: tactile gradients
**Use when:** editorial hero backgrounds, posters, branded packaging-inspired surfaces and visual transitions. **Avoid when:** the texture would compete with content, charts, text, or dense controls.

## Visual recipe
- Begin with 2–3 warm, muted pigments (e.g. cream, burnt orange, rust), wide organic gradients, slightly irregular boundaries and enough quiet space for type.
- Place a **subtle static grain layer** on top of the art region, not on important text or input controls. Let the composition retain readable flat areas.
- Prefer pre-rendered small, licensed/original compressed texture tiles in production; load them only where used. Never fetch screenshot assets or third-party textures without permission.

```css
.analog-art {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  background: radial-gradient(ellipse at 22% 85%, #f3e4cd 0%, transparent 58%),
              radial-gradient(ellipse at 83% 14%, #bd4c30 0%, transparent 58%),
              linear-gradient(125deg, #ddaa7e, #9b4336);
}
.analog-art::after {
  content: ''; position: absolute; inset: 0; pointer-events: none;
  opacity: .10; mix-blend-mode: multiply;
  /* Replace with a small static authored tile in production. */
  background-image: repeating-linear-gradient(93deg,
    transparent 0 2px, rgba(28,18,12,.19) 2px 3px, transparent 3px 5px);
}
.analog-art > * { position: relative; z-index: 1; }
```

## Performance and accessibility
- Do not animate a high-resolution noise filter or regenerate random pixels on every frame. Prefer a single static texture and compositor-friendly container transitions.
- Respect reduced motion, use a solid-color fallback if textures fail, and verify text contrast over every gradient location. If it fails, add an opaque text zone rather than cranking noise down arbitrarily.
- Keep grain a visual surface treatment, not a metaphor for disabled states, errors or feedback.
