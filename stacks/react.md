# React-specific UI checks
**Use when:** the UI task has a React-specific implementation or accessibility issue; otherwise use normal project patterns.

- Match existing component architecture, router, state management, styling and UI primitives. Avoid unnecessary dependencies or abstractions.
- Keep controlled/uncontrolled inputs intentional; avoid render loops, unstable keys and duplicated state. Preserve label/input IDs, focus, keyboard and error announcement.
- For overlays, manage focus on open/close, Escape, inert/background handling and portals carefully; prefer existing accessible primitives.
- Avoid animation-driven rerenders; measure actual expensive components before memoizing. Respect reduced-motion styles.
- Test changed states and keyboard flows with project test tools; don't infer passing tests from code inspection.
