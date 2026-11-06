# Implementation verification — use after substantive code changes
Only check the areas impacted by the change; expand for large redesigns.

- [ ] Core workflow/feature still works; tests/build checks run and results recorded.
- [ ] Existing components/tokens reused; no unintended cross-screen changes.
- [ ] Relevant states implemented: default, focus, active, selected, disabled, loading, error, success.
- [ ] Keyboard, semantic labels, focus restoration, contrast and useful screen-reader feedback checked.
- [ ] Narrow/wide layouts, text zoom, dark/light/system themes and content overflow checked as relevant.
- [ ] Images/icons/touch areas and spacing remain consistent; motion respects reduced-motion and avoids jank.
- [ ] Actual screenshots/render evidence reviewed if browser exists; otherwise visual checks marked unverified.
- [ ] User-facing summary distinguishes implemented, verified, and recommended follow-up.
