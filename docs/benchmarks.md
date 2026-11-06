# Benchmarks: what is measured and what is not

The package is optimized for selective loading. **That does not prove total token savings or higher-quality generated interfaces.** Benchmark reports must distinguish static file sizes from model usage and blind-reviewed results.

## Reproducible static measures

Executed locally on the public release using `python scripts/measure_footprint.py`:

| File group | Files | UTF-8 bytes | Characters | Character / 4 estimate |
| --- | ---: | ---: | ---: | ---: |
| Core `SKILL.md` | 1 | 3,462 | 3,430 | 858 |
| Optional knowledge modules | 16 | 32,132 | 32,056 | 8,014 |
| Optional framework adapters | 9 | 5,848 | 5,848 | 1,462 |
| Searchable pattern catalog | 1 | 8,322 | 8,322 | 2,081 |
| Optional style recipes and guide | 6 | 11,713 | 11,711 | 2,928 |
| Optional style keyword catalog | 1 | 884 | 884 | 221 |

These are **on-disk measurements**, not live model token counts. The v1.3.0 core is approximately 858 char/4 units; optional dark/slider/style guides are not loaded for unrelated changes. Character/4 is a rough English-language proxy that can deviate substantially between providers and types of content. Also, progressive reads still accumulate in a typical agent context.

## Controlled agent tests (not yet run)

The [`tests/scenarios.md`](../tests/scenarios.md) file specifies tasks such as improving an OTP form, auditing a desktop settings page, fixing an animation, and creating a landing page.

For each comparison:
1. Pin the model/version, project snapshot, prompt, available tools, and iteration budget.
2. Run without a skill, with this skill, and (optionally) with another skill independently. Randomize run order if possible.
3. Record true model input/output tokens from provider logs, counting tool use and retries.
4. Verify functionality and accessibility and score visible results blindly against a predefined rubric.
5. Report matched successful scenarios, variance, failures, sample sizes and total tokens per successful task.

Input format: [`tests/benchmark-template.csv`](../tests/benchmark-template.csv). Aggregation: `python scripts/benchmark_summary.py measured-results.csv`. The summarizer does not call models, so it cannot produce real benchmarks by itself.

**Output quality, savings vs. Anthropic Frontend Design, and savings vs. UI UX Pro Max remain unmeasured.** No claims are published before independent, reproducible runs.

## Style routing verification

`python -m unittest discover -s tests -p "test_*.py" -v` verifies all five style names, representative concept searches, bounded results, and that a no-match query returns no arbitrary style. This is **deterministic CLI coverage**, not a model quality evaluation. The offline example can also be reviewed visually in a browser, but should not be described as a live product benchmark.
