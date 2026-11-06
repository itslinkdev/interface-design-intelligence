# UX principles — contextual rules
**Use when:** interaction architecture, complex choice, navigation confusion, onboarding. **Heuristics ≠ guarantees.**

- **Hick:** many meaningful choices → prioritize, group, filter, or progressively reveal; avoid creating unnecessary submenu levels.
- **Jakob:** follow users' established product/platform patterns unless unfamiliar behavior offers a concrete gain.
- **Fitts:** important controls need an adequate target and placement; pointer travel and available space matter. See `accessibility.md` only if checking target requirements.
- **Miller/chunking:** organize concepts into meaningful sections; never enforce an arbitrary 7±2 item cap.
- **Gestalt proximity:** related fields/cards/actions should be nearer each other than unrelated groups; use labels/containers where spacing alone is ambiguous.
- **Prägnanz:** favor stable, recognizable forms and simpler visual organization, not indiscriminate removal of useful details.
- **Tesler:** complexity moves between system and user. Use defaults, templates, and progressive settings while preserving transparency and control.
- **Zeigarnik:** visible unfinished progress can help resume tasks; don't manufacture artificial pressure.
- **Peak-end:** completion and recovery states deserve clear, reassuring feedback; test overall task experience, not only the last screen.
- **Serial position:** key content may benefit from prominent placement; don't treat first/last recall as universal layout law.
- **Aesthetic-usability:** coherence improves perceived quality but cannot compensate for broken or inaccessible functionality.

**Conflict resolution:** if a simplified flow hides necessary controls, increase discoverability; if grouping increases navigation effort, flatten; if novelty harms familiarity, prefer the familiar pattern. Test with real tasks when stakes merit it.

Example: settings screen → group preferences by user mental model, show common settings first, tuck advanced controls behind an explicit section, preserve direct search if settings are numerous.
