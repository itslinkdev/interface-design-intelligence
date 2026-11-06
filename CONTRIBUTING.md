# Contributing

Bug reports, accessibility fixes, concise pattern guidance and cross-platform examples are welcome. Please open an issue before proposing a major new module.

1. Keep `SKILL.md` short and route-only. Extend a focused module rather than duplicating advice.
2. Add a `Use when` sentence and a practical exception to new modules.
3. Do not add third-party screenshots, licensed font binaries, customer/project data or identifiable user information without documented permission. SVGs should be original and self-contained.
4. Preserve honest benchmarks: report actual token logs, model, tasks, tools and evaluation method. Never invent comparative performance claims.
5. Run `python scripts/validate_skill.py` and `python -m unittest discover -s tests -p 'test_*.py'` before opening a PR. Run `python scripts/refresh_manifest.py` after changes.
6. Show before/after screenshots only when you own or have permission to share them; redact sensitive data.

See [SECURITY.md](SECURITY.md) for reporting issues involving credentials or private material.
