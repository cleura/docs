# AGENTS.md — terse agent index (routing + gotchas)

Agents: explore the repo directly; this file routes, it does not teach.

## General Information

- **README.md**: General project overview and setup instructions
- **Contributor documentation**: `docs/contrib/` directory
  - Overview: `docs/contrib/index.md`
  - Modification guidelines: `docs/contrib/modifications.md`
  - Style guide: `docs/contrib/style.md`
    AI-assisted changes **must** contain exactly one, and only one, sentence per line.
    Use the serial comma ("Oxford comma").
  - Quality checks: `docs/contrib/quality.md`

## Documentation Structure

New additions must follow the [Diátaxis](https://diataxis.fr/) approach:

- How-to guides: `docs/howto/`
- Reference information: `docs/reference/`
- Explanation: `docs/background/`
- Tutorials: `docs/tutorials/`

## Session Management

Write plans, notes, and ephemeral files to `.ai/` (gitignored).
Prefer `.ai/tmp/` over the system temp directory.

## Tooling & Dependencies

When planning, review these key files:

- `mkdocs.yml`: Documentation build configuration
- `tox.ini`: Testing configuration
- `requirements.txt`: Python dependencies

## Development Workflow

- **Tests**: Run with `tox` command.
- **Git Hooks**:
  - `pre-commit` (lint only)
  - `pre-push` (functional tests) in `.githooks/` directory
- **Code Review**: Pull request series must be **unsquashed**; each commit must be independently testable and correct.
- **Git Operations**:
  - Read-only operations (`git log`, `git diff`, `git status`) are fine.
  - All mutating operations (add, commit, reset, checkout, push, stash, merge, branch, etc.) require explicit user approval.
  - All modifications require a topic branch.
  - Never commit directly to `master` or `main` branch.
  - Never bypass hooks by using the `--no-verify` option, nor by any other means.
  - For refactoring tasks, always create a *new* topic branch.
  - Always declare the AI tool and the employed model, by including `Assisted-By: <tool>/<model>` in the commit message.
  - Never include emoji in commit messages.
  - Always follow the [Conventional Commits specification](https://www.conventionalcommits.org/en/v1.0.0/#specification).
