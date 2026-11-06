# Vue-specific UI checks
**Use when:** the UI task has Vue-specific state, component or interaction concerns.

- Reuse project Composition/Options API convention, styling system and established primitives. Keep props/events semantics clear.
- Prefer computed state over duplicated derived refs. Ensure `v-model` bindings, validation, and reactive theme changes are predictable.
- Give `v-for` items stable keys. Preserve focus across conditional mounting (`v-if`) and visibility changes (`v-show`).
- Check keyboard semantics and overlay focus management; prefer established accessible controls.
- Validate layout, states, and responsiveness with existing Vue test/build tooling; avoid needless dependencies.
