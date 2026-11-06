# Electron / Tauri desktop
**Use when:** building desktop UIs backed by web technologies.
- Respect window scaling, keyboard shortcuts, focus, menus, native dialogs and OS theme.
- Audit security boundaries: do not expose privileged APIs to UI code; follow framework-specific permission policies.
- Reuse the existing component system; avoid animated overlays that cause frame drops.
- Test resize behavior, touchpad scrolling, high-DPI display, long content and reduced motion.
