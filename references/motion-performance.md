# Motion, interaction animation and smoothness
**Use when:** animated agents, transitions, dropdown motion, lag, layout shift, visual feedback.

- Motion explains relationship, change, progress, or attention; remove effects with no clear purpose. Avoid all-motion redesigns.
- Prefer compositor-friendly `transform` and `opacity` for frequent animations; avoid needless layout/reflow work. Profile actual rendering before asserting performance gains.
- Motion timing should match distance, context, and platform convention; avoid rigid universal duration/easing. Use consistent motion tokens and preserve interruption/reversal behavior.
- **Easing by intent (heuristics, not rigid presets):** linear = mechanical/progress indication; ease-out = entrances; ease-in = exits; ease-in-out = repositioning; small overshoot = expressive confirmation; elastic/bounce = rare playful moments; steps = genuinely discrete state changes (e.g., counters). Prefer platform motion curves over generic CSS when native. Avoid bouncing primary controls during routine tasks.
- Choose durations for perceived distance and input modality; prefer short feedback to theatrical motion. Avoid perpetual decorative loops, and ensure that `steps()` does not impair reading or cause flashing.
- Respect `prefers-reduced-motion` or native OS accessibility settings. Provide no-motion or restrained fallback, never hide essential meaning inside animation.
- Dropdowns/dialogs: focus management, position stability, pointer safety, and keyboard operation matter more than elaborate entrance effects.
- Eliminate accidental square artifacts, flashing, stutters, and layout jumps by finding root cause (paint/compositing/overdraw/state), not adding overlays to hide bugs.
- Treat interactions as states: idle, hover, focus, pressed, pending, confirmed, error, exit; implement only applicable transitions.

**QA:** test low-end hardware or throttling where available; watch main-thread long tasks, layout shifts, frame pacing, network delays, reduced-motion, and hidden/background tab behavior.
