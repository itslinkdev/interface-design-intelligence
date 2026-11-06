# Controlled evaluation — real agent runs required

Run each task with the **same model/version, repository snapshot, prompt, tools and budget**: baseline (no skill), this skill, and optionally a third-party skill. Record actual aggregate token usage from the provider/agent (including tool contexts if available) in `benchmark-template.csv` and aggregate with `python <skill-root>/scripts/benchmark_summary.py results.csv`. These scripts do **not** execute models, inspect rendered UI or claim benchmarks took place.

## Scenarios
1. **Minor padding adjustment** — change no unrelated UI. Expected reference reads: 0.
2. **Login/OTP form** — persistent labels, paste/autofill, exact field errors. Expected: forms module.
3. **Long dropdown (200 options)** — keyboard-friendly search or native alternative. Expected: controls module.
4. **Desktop settings** — correct switch/segmented semantics, Windows contrast and themes.
5. **Light/dark palette** — semantic roles, rendered contrast validation, meaningful focus/disabled states; optionally read dark guide when specifically needed.
6. **Ecommerce detail** — clear primary CTA and price, no removed factual purchase choices.
7. **Laggy UI animation** — diagnose jank with measurements, easing intent (enter/exit/move/progress), interruption and reduced-motion behavior.
8. **Cancel subscription** — neutral copy, usable exit, no dark patterns.
9. **Audit-only mode** — prioritized evidenced findings; no unrequested edits or fabricated checks.
10. **Typography** — brand fit, glyph support, restrained scale, licensing awareness.
11. **New creative landing page** — compare generic vs distinctive aesthetic direction; legibility preserved.
12. **New design-system tokens** — derive semantic light/dark tokens from supplied brand requirements, use generator only if requested, test resulting CSS.
13. **React form** — avoid unrelated refactors; keyboard flow and controlled state preserved.
14. **Vue/Tailwind/Windows scenario** — use only the relevant adapter and verify native/framework idioms.

## Quality scoring (six criteria, 0–2 each; maximum 12)
- Task correctness and scope adherence.
- Functional behavior, regression prevention.
- Accessibility and keyboard/focus support.
- Coherent visual hierarchy, deliberate aesthetics and responsive quality.
- Appropriate design-system reuse or creation.
- Honest verification and useful evidence.

Score *observed* artifacts, not agent confidence. A critical regression fails regardless of score. Blind-score visuals where possible; check both light and dark, mobile and desktop when relevant. Record **number of optional module reads and image reads** separately in notes if traceable. Report tokens per successful task and quality; do not treat char/4 proxies as actual token usage.


## Style selection scenarios (evaluate separately)
- Explicit glass toolbar on a real app: preserve controls and provide stable reduced-transparency/contrast fallbacks, without coating all content panels.
- Warm editorial brand hero: choose Analog Grain with readable type; reject constantly animated noise.
- Creative landing header: use Chrome Typography only for display copy; fallback must remain legible.
- Minimal campaign with pixel accent: keep focus, labels, and native controls intact.
- Premium editorial product page: balance serif display with readable body/UI typography and mobile responsiveness.
- Negative-control task: fix a signup form validation bug without loading any style recipe or changing the visual identity.

A quality claim requires blind-reviewed visible outputs, functional tests and actual model usage logs; source-file size alone does not show quality.

## New dark-mode negative controls
- **Never use pure black?** Test an immersive/OLED use case: do not reject black simply because it is black.
- **White at 30% opacity?** Check actual composited WCAG text contrast and reject unreadable required copy.
- **No shadows ever?** Verify tonal surfaces first, but permit subtle overlays/popovers if effective.
- **Toggle everywhere?** Honor OS preference; add a manual switch only when product/platform benefits.
- **Fizzy motion?** Pick easing by user intent; avoid bounce/elastic for core tasks and respect reduced-motion.
- **No redesign requested?** Skip dark-mode guide and style recipes for an unrelated one-line UI fix.

## Slider interaction scenario
- **Native slider, active drag:** thumb and numeric value follow input immediately; no easing-induced lag or value overrun. Verify Arrow/Home/End, screen-reader value and real touch input.
- **Programmatic target / snap:** animated decoration follows chosen curve, never changes semantic numeric range; interruptions are reversible; reduced-motion remains usable.
- **Boundary & performance:** min/max, steps, high contrast, disabled, rapid alternating direction, resize, RTL, and low-end frame pacing. Confirm no network/persistence call is made for every pointer movement without need.
- **Negative control:** fix a navbar padding bug without reading slider or motion guides.

## Release acceptance
- Agent discovery of root `SKILL.md` works when installed at each documented path; optional modules do not need preload.
- Install and smoke-test at least one real supported agent before claiming production compatibility; offline tests do not exercise model tool selection.
