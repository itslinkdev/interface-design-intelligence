# Aesthetic direction and visual originality
**Use when:** creating new pages, rebranding, choosing a visual identity, or explicitly requesting more distinctive design. **Skip** for routine fixes in an established design system.

## Direction before decoration
1. Write a **one-sentence visual thesis** suited to the audience and product (e.g. "quiet editorial research tool" or "high-energy sci-fi game portal"). Choose 2–3 distinguishing traits (type, composition, imagery, color or motion), not every novelty at once.
2. Establish typography, density, grid, signature shape treatment, and color roles. Make the first screen's hierarchy obvious in grayscale before accents.
3. Prefer an intentional composition: purposeful whitespace, aligned edges, measured asymmetry, meaningful rhythm, and clear section transitions. Don't default to a generic hero + three identical cards unless it genuinely fits.
4. Use images, icons, gradients, borders, texture and shadows **only if** they reinforce the thesis. Avoid random glassmorphism, gratuitous gradients, decorative blobs, emoji icons, and mismatched icon families.
5. Ensure contrast and reading comfort. Distinctiveness is not an excuse for inaccessible text or unconventional controls without benefit.

## Two cases
- **New product/brand:** explore 2 viable directions briefly; select one for user goals and implementation cost; establish a few semantic tokens. Consult `design-system.md` only if a reusable token system is needed.
- **Existing product:** inventory existing visual language and refine it. Don't substitute the agent's personal style for the product's identity.

## Review after rendering
- Does the interface have a coherent recognizable character, not just more styling?
- What draws attention first, and is it the correct action or content?
- Are typography, spatial rhythm, imagery, icon style and component states consistent?
- Are responsive variants deliberate rather than a compressed desktop mockup?
- Which effects can be removed without losing meaning? Is originality undermining clarity?

Catalog patterns (text-only): REF-012 (aesthetic/usability), REF-033–036 (before/after product screen), REF-047–049 and REF-061–062 (domain typography), REF-055–057 (consistency/hierarchy).

For a named aesthetic (glass, analog grain, chrome, pixels, editorial serif), search `scripts/find_style.py` and read only the selected `styles/` recipe. Style guidance is opt-in, not a requirement for ordinary fixes.
