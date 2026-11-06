# Navigation and control selection
**Use when:** navbar, tab, segmented control, switches, sliders, selection, hit targets.

- Switch = immediate on/off **state**; radio/segmented control = mutually exclusive **choices** (grid vs list). Check whether changes apply instantly; if not, use a clear save/submit flow.
- Segmented options need balanced targets and clear selected state; equal widths are usually appropriate when labels fit. Consider localization, narrow widths, and non-equal semantic needs.
- Tabs navigate related panels; links navigate destinations; buttons invoke actions. Preserve browser/OS semantics and a visible current location.
- Navbar: use predictable destinations, concise labels, consistent order/icons; active section must be explicit. Mobile navigation must avoid safe-area overlap.
- Sliders suit continuous or bounded approximate values (volume, brightness). Show value/unit, scale/min/max where meaningful; offer keyboard operation and numeric alternative for precision-critical data.
- Long lists: offer search, filtering, keyboard navigation, and list scrolling; short lists should remain simple. Don't build a heavy custom combobox if a native control suffices.
- Make click/touch areas sufficiently generous; don't confuse icon graphic size with hit target size. Check nearby target spacing.
- Expose relevant states: default, hover, focus, selected, pressed, disabled, and busy. Never make focus identical to hover or selected.

**QA:** keyboard order, selection semantics, active nav, text expansion, touch reach, pointer and screen reader feedback.
