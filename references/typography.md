# Typography, hierarchy and domain font guidance
**Use when:** typographic system, font selection, line-height, density, display titles.

- Preserve existing licensed font family and design tokens unless rebranding is explicitly requested. Never download, embed, or redistribute proprietary font files without rights.
- Establish a compact scale, e.g. `16 → 20 → 25 → 32` (ratio ~1.25) as a *starting point*. Don't force proportional scaling in dense apps; tune responsive sizes using `clamp()` where useful.
- Body line-height commonly ~1.4–1.6; tighter display headlines may be appropriate. Adjust for actual font metrics, line length, script, and size. Avoid brittle global rules.
- Prefer readable regular/medium body text over very thin weights; hierarchy should rely on size, weight, position, and spacing. Verify real contrast, not just font weight.
- Limit simultaneous families/weights. Define semantic tokens (`body`, `caption`, `title`, `display`) rather than arbitrary per-component numbers.

## Domain inspiration (not mandates)
| Context | Possible fonts | Implementation note |
|---|---|---|
| Gaming/sci-fi | Orbitron, Oxanium, Rajdhani | Expressive display headings; use legible body face |
| Editorial/storytelling | Merriweather, Lora, Playfair Display | Comfortable body reading; editorial display accent |
| Ecommerce | Inter, Montserrat, DM Sans | Product scan, price hierarchy, compact labels |
| Portfolio/creative | Space Grotesk, Manrope, DM Sans | Distinct identity without distracting from work |
| SaaS/tech | Inter, Plus Jakarta Sans, Space Grotesk | Dense UI readability and predictable metrics |

**Caveats:** These are examples from provided imagery, not verified performance rankings. Check license, webfont weights, glyph/language coverage, rendering speed, fallback, and brand fit. Avoid switching fonts by industry alone.
