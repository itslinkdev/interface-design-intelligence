# Qt / PySide / PyQt
**Use when:** implementing QWidget/Qt Quick interfaces, dialogs or models in Qt.
- Prefer native layout managers and size policies over absolute coordinates; test high-DPI scaling and long/localized strings.
- For item-heavy views use model/view components; keep expensive work off the GUI event loop.
- Provide keyboard focus, proper accessible names, shortcut behavior, and platform-consistent confirmation dialogs.
- Respect system palette unless the user explicitly wants an app theme. Avoid applying web CSS assumptions to Qt.
- Verify Windows/macOS/Linux behavior on supported targets; render both scaled and unscaled if applicable.
