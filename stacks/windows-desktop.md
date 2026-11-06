# Windows desktop / native-shell implementation checks
**Use when:** designing WinUI, WPF, Windows shell integrations, or Windows-styled desktop UI.

- Identify actual framework and OS target before changing styles. Preserve native expectations, focus behavior, High Contrast/forced colors, scaling, text size and keyboard shortcuts.
- Prefer OS theme, semantic resources and native confirmation patterns; don't imitate system dialogs inaccurately.
- Use native accessibility providers or framework semantics; test DPI scaling and keyboard-only operation.
- Animations must not block commands or cause lag; respect OS reduced-motion preferences.
- Shell/context-menu integration must remain permission-aware, predictable and reversible; inspect platform restrictions before designing actions.
