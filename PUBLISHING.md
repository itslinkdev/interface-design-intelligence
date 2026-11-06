# Publish Interface Design Intelligence

The repository is intended to be public under [itslinkdev/interface-design-intelligence](https://github.com/itslinkdev/interface-design-intelligence). The maintainer must control that GitHub account. This release is a standalone [Agent Skill](https://agentskills.io/specification), **not** a ChatGPT plugin.

## Preflight

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/audit_public.py
python scripts/measure_footprint.py
```

Check the diff before publication. The scans are conservative and do not guarantee that every kind of secret or licensing problem will be detected.

## One-time repository creation

Using GitHub in the browser, create a **public, empty** repository named `interface-design-intelligence` under `itslinkdev` at [github.com/new](https://github.com/new). Do not initialize it with a README, license or `.gitignore`: these are already in the project.

Or, with an authenticated [GitHub CLI](https://cli.github.com/), from the extracted `interface-design-intelligence/` folder:

```bash
gh auth status                       # must identify itslinkdev
git init -b main
git add .
git commit -m "Release Interface Design Intelligence v1.3.0"
gh repo create itslinkdev/interface-design-intelligence --public --source=. --remote=origin --push
```

If you created the **empty repository in the browser** instead, replace the final `gh repo create` command with:

```bash
git remote add origin https://github.com/itslinkdev/interface-design-intelligence.git
git push -u origin main
```

If the repository already exists and contains work, do not reinitialize or force-push it; review its history and integrate the skill using a normal branch/PR.

## Publish the GitHub Agent Skill release

GitHub CLI **v2.90.0 or newer** exposes `gh skill` in preview. After pushing the repository, from the repository root run:

```bash
gh skill publish --dry-run
gh skill publish --tag v1.3.0
```

This validates the skill, offers the `agent-skills` topic and creates a versioned GitHub release. See [official documentation](https://cli.github.com/manual/gh_skill_publish). A public repository alone distributes the source; a GitHub release provides the additional published version.

## Install and verify

```bash
gh skill install itslinkdev/interface-design-intelligence interface-design-intelligence --agent codex --scope user
gh skill list
```

Substitute a supported agent ID as appropriate. See [installation options](https://cli.github.com/manual/gh_skill_install).

## After release

- Confirm the README's original SVGs and both contributor acknowledgments render correctly.
- Check the Actions workflow under **Actions → Validate skill** and fix any failing jobs.
- Add repository topics such as `agent-skills`, `ui-ux`, `design-system`, `accessibility` and `frontend`.
- Review repository security, issues and branch protection according to maintenance needs.
- Link reproducible measurements, not invented comparative quality or token-saving statistics.

The GitHub contributors graph shows commit authors; the README separately credits **@itslinkdev** and **ChatGPT (OpenAI)** without inventing an AI GitHub account or claiming OpenAI endorsement.
