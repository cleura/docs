# AGENTS.md — terse agent index (routing + gotchas)

Agents: explore the repo directly; this file routes, it does not teach.

**IMPORTANT:** When invoking any agent on this repository, you MUST run the following commands **immediately** upon evaluation of this file, before doing anything else:

```shell
git submodule update --init
git config core.hooksPath .githooks
```

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

## When planning

Read these to understand dependencies and tooling:

- `mkdocs.yml`: Documentation build configuration
- `tox.ini`: Testing configuration
- `requirements.txt`: Python dependencies

## Tooling

### Tests

Entry point is **`tox`**.
