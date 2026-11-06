# Chrome Typography: controlled metallic display
**Use when:** brand marks, hero headings, Y2K-inspired campaign titles, merch and album-inspired creative. **Avoid when:** body copy, dashboards, controls or lengthy paragraphs need immediate legibility.

## Visual recipe
- One large, condensed or heavy display face; reflective metallic bands with alternating cool highlights and deep steel. Keep the rest of the layout quiet and dark.
- Use the technique on a *single decorative heading*, not every word. Ensure the meaning stays readable if gradients or clipping are unsupported.

```css
.chrome-title {
  color: #d2d7e3; /* fallback */
  font: 900 clamp(2.8rem, 9vw, 7rem)/.9 system-ui, sans-serif;
  letter-spacing: -.075em;
  text-transform: uppercase;
}
@supports (-webkit-background-clip: text) {
  .chrome-title {
    background: linear-gradient(180deg,
      #fff 0%, #edf0fb 16%, #747e93 34%, #f6f8ff 46%,
      #a5adc1 56%, #3b4357 70%, #cdd3de 83%, #f7f9ff 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
  }
}
```

## Performance and accessibility
- Prefer a static gradient over canvas/WebGL shaders, 3D fonts or continuously animated reflections. Avoid heavy blur/glow under every glyph.
- Make the fallback solid and high contrast; check the darkest metallic bands. If text is essential and contrast varies too much, use an accessible solid alternative.
- Support forced-colors/high-contrast modes by returning to solid `CanvasText` and disabling decorative backgrounds.
- Never redistribute a commercial typeface without its license; generic or appropriately licensed fonts are fine.
