# Pixel Accents: crisp digital microdetails
**Use when:** small decorative symbols, cursor-inspired motifs, status illustrations, creative callouts, playful campaign UI. **Avoid when:** primary navigation must resemble standard platform widgets or pixels would reduce legibility.

## Visual recipe
- Use a clean sans typographic foundation, spacious white or near-black canvas, and **one bold accent** (electric blue works) with a restrained pixel motif.
- Keep pixel geometry crisp: integer-sized squares and hard edges. Mix precise digital motifs with polished conventional components rather than pixelating all icons.

```css
.pixel-accent {
  display: inline-block;
  width: 8px; height: 8px;
  background: #477dff;
  box-shadow: 8px 0 #477dff, 16px 0 #477dff,
              8px 8px #477dff, 16px 16px #477dff,
              8px 24px #477dff;
  image-rendering: pixelated;
}
/* Pixel illustrations should be aria-hidden; describe functional actions in text. */
```

## Accessibility and engineering
- Do not make functional icon meaning depend on a handful of ambiguous pixels; label actions, preserve familiar hit areas and focus rings.
- Use CSS boxes or original tiny SVG for static motifs rather than icon libraries with hundreds of unused assets.
- Snap layouts to pixel grid at the chosen display scale, test 125%/150% zoom, high DPI and very narrow viewports.
- Keep transitions minimal. Pixel art needn't imply jerky or degraded animations.
