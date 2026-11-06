# Platform and responsive adaptation
**Use when:** desktop applications, mobile, native conventions, responsive behavior.

- Before choosing styles, identify supported platforms (web, native Windows, Electron/Tauri, iOS/Android), input modes, density, touch capability, and theme conventions.
- Respect platform-native components, shortcuts, dialogs, window behavior, safe areas, and assistive technology integration unless user requests a bespoke replacement.
- Design responsive behavior from content constraints: wrap grids, resize controls, avoid clipping; test narrow width, high zoom, long translation, large system text, orientation, and empty/loaded states.
- For Windows-like dialogs, mimic native conventions only when appropriate; custom visuals must retain keyboard focus, Escape semantics, scaling, contrast, and window modality. Don't falsely claim a custom modal is native.
- Use semantic design tokens that adapt to themes rather than duplicating an entire visual codebase. Icon and typography sizing must suit platform DPI.
- Retain pointer, mouse, touch, pen, and keyboard usability; don't depend on hover for essential information.

**QA:** supported viewport/device matrix, platform state transitions, window resize, system theme change, screen-reader behavior, and no functional regressions.
