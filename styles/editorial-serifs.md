# Editorial Serifs: typographic restraint
**Use when:** premium products, magazines, storytelling, architecture, quiet portfolios and long-form editorial. **Avoid when:** a dense tool, data-heavy app or small-screen controls would become harder to scan.

## Visual recipe
- Pair a high-contrast serif **display heading** with a pragmatic sans-serif UI/body font. Use an elegant italic word selectively.
- Favor off-white paper tones, dark charcoal ink, wide margins, thin deliberate separators and aligned edges. Asymmetry should improve pacing, not disrupt reading order.
- For content cards, one large statement and a small running label are usually enough. Keep buttons and forms in the stable UI typeface.

```css
.editorial {
  --paper: #f0ece6;
  --ink: #201d1a;
  color: var(--ink);
  background: var(--paper);
}
.editorial h1 {
  max-width: 14ch;
  margin: 0;
  font: 400 clamp(3.2rem, 8vw, 7rem)/.96 Georgia, 'Times New Roman', serif;
  letter-spacing: -.05em;
  text-wrap: balance;
}
.editorial h1 em { font-style: italic; }
.editorial .meta { font: 600 .75rem/1.4 system-ui, sans-serif; letter-spacing: .11em; }
```

## Production checks
- Check serif glyph availability for localized copy and graceful fallback. Don't assume a particular paid font is installed.
- Avoid ultra-thin strokes at small sizes. Inspect actual paragraph width and line-height, especially when zoomed or translated.
- Keep semantic document order, clear focus, reliable navigation, and adequate click targets. Typography is the ornament; do not add excessive flourishes.
