# Visual directions: selective style recipes
**Use when:** a user names a style, provides visual inspiration, or asks for a new visual direction. **Skip** when repairing UI behavior or maintaining a settled visual identity.

## Choose deliberately
1. Inspect the product, platform, existing design tokens, and user-provided references. A screenshot is **inspiration**, not a license to copy imagery or brands.
2. Choose **one primary direction**. Add at most one compatible accent if it supports user goals. Do not choose effects simply because they are fashionable.
3. Read only the selected file in `styles/`; consult an existing UX module only for a concrete unresolved issue. Decide contrast, density, typography, geometry, effects and interaction states before coding.
4. Adapt platform implementations; CSS is illustrative **web guidance**, not a substitute for native framework materials or APIs.
5. Test light/dark themes as relevant, low-end hardware, reduced motion/transparency, touch/keyboard, rendering and readability. Provide an inexpensive fallback.

| Style | Best use | Main risk |
| --- | --- | --- |
| [Liquid Glass](liquid-glass.md) | Floating controls, nav, toolbars | Large blur regions, low contrast, platform mismatch |
| [Analog Grain](analog-grain.md) | Editorial surfaces, hero art | Grain over text, noisy animation, large textures |
| [Chrome Typography](chrome-typography.md) | Large display type, campaign marks | Small metallic text unreadable; expensive filters |
| [Pixel Accents](pixel-accents.md) | Small icons, creative UI details | Pixelation degrading functional controls |
| [Editorial Serifs](editorial-serifs.md) | Premium reading and display headings | Inappropriate dense UI typography |

**Compatible accents:** editorial serif + restrained grain; chrome display + sparse pixel details; liquid glass navigation + subtle pixel motifs in content. Avoid applying all five simultaneously.

### Rules for mixing styles
- One dominant system (color, type, surfaces) and one controlled accent; interactive states always follow usability rules.
- Glass and chrome may coexist as a **single localized hero expression** but should not coat every control. Grain never obscures labels.
- Prefer no style effect when product character, platform norms, or user tasks argue against it.
- For examples, open `examples/style-gallery.html` locally (no network or JS dependencies). Original CSS-only demonstrations are not replicas of supplied screenshots.
