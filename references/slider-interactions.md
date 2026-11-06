# Sliders: interaction, animation and performance
**Use when:** designing or fixing range sliders, seek bars, brightness/volume controls, dual-thumb ranges or their motion. Skip for unrelated animation tasks.

## Choose the component first
- Prefer native/platform slider controls (`<input type="range">`, WinUI, SwiftUI, Compose etc.) when they meet product needs. A decorative easing showcase is **not** a replacement for accessible slider input.
- Use a slider for bounded approximate adjustment; use numeric input (alone or paired) when exact amounts matter. Show name, current value/unit, range and step where useful. For two thumbs, enforce ordering and ensure both remain independently reachable.
- Keep semantic state independent of graphics: numeric value is clamped to `[min,max]`, obeys `step`, stays consistent with fill and thumb. Do not use animation to delay, alter or fabricate the committed value.

## Motion from the supplied easing demonstration
- **Direct manipulation:** during pointer/touch drag, thumb and fill follow the value **without a transition or lag**. Keyboard updates must also feel immediate. Do not apply spring/bounce to each `input` event.
- **Release / programmatic change:** short `ease-out` or restrained `ease-in-out` can animate presentation to an allowed snap point or a target from code. Do not animate a media seek position away from the actual current time.
- **Intent mapping:** `linear` for progress/time; `ease-in` for disappearance; `ease-out` for arriving; `ease-in-out` for reposition; overshoot/elastic/bounce only for clearly playful *decoration*, never to put a semantic value outside the range; `steps()` only for genuine discrete values. Native animation APIs may be more appropriate than CSS.
- Cancel or retarget existing motion on a new interaction; do not queue stale animations. Honor reduced-motion and low-power settings. Never make precise selection dependent on an animation finishing.

## Input, accessibility and speed
- Native range control preserves keyboard/assistive semantics. Custom sliders must implement accessible name, min/max/current value, useful value text, focus, pointer/touch and Arrow/Home/End interactions; Page Up/Down optional. Verify with real assistive technologies, especially touch screen readers. See [W3C slider pattern](https://www.w3.org/WAI/ARIA/apg/patterns/slider/).
- Provide a substantial thumb hit target, visible focus, distinguishable filled track, contrast and high-contrast/forced-color rendering. Support touch, track click, keyboard, zoom, resizing and RTL when relevant.
- Update the visible value during dragging, but defer expensive persistence, networking or heavy data transformations until commit/release where feasible. If custom painting is necessary, coalesce work per animation frame; avoid forced layout, `left`/`width` animations and excessive `will-change` layers; prefer `transform` for decorative elements.

**QA:** min/max and off-step inputs; rapid drag and interruption; drag outside track; disabled and pending; keyboard focus and reader value; touch on real device; slow hardware; reduced motion; theme/contrast/zoom. Check actual frame pacing before claiming a performance improvement.

**Optional offline examples:** [`slider-motion-demo.html`](../examples/slider-motion-demo.html) (a real native range input and separate visual easing lanes). Motion lanes demonstrate curves only; do not treat them as production form controls. Also see [`motion-performance.md`](motion-performance.md).
