# Geometry, spacing and optical alignment
**Use when:** paddings, nested cards, icon geometry, uneven segmented controls, visual rhythm.

- Use the project's spacing tokens first. If absent, a compact 4px-based scale (4, 8, 12, 16, 24, 32, 48) is a useful *starter*, not a universal mandate.
- Between groups > within groups. Align to visible content edges; avoid arbitrary margins and one-off values unless justified.
- **Nested radii:** for evenly inset rounded shapes, start with `inner_radius ≈ max(0, outer_radius − inset)`. Check visually; don't use a universal 1:2 ratio. Radius geometry may differ with asymmetric or transformed shapes.
- **Optical alignment:** circles, triangles, glyphs, badges, and icons can look off-center even with mathematically equal bounds. Correct small visual offsets after measuring, without destroying hit target geometry.
- **Segmented controls:** equal or intentionally balanced segment widths typically improve rhythm and target consistency. Long localized labels may require content-based widths or overflow handling.
- Maintain consistent border weights, component heights, icon optical sizes, corner families, and elevation levels. Adjacent elements shouldn't seem randomly proportional.
- Check design at text zoom, constrained width, localization, and right-to-left layout where applicable. Avoid spacing choices that cause wrapping or clipping.

**Validation:** compare boundaries, baselines, target rectangles, nested corner curves, and content density at supported sizes. Distinguish optical correction from masking a layout bug.
