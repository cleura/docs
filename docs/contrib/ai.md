# AI-assisted contributions

When making a contribution to this repository, you may use coding agents that assist you with generative artificial intelligence (GenAI), provided you adhere to the following guidelines for their use.

## Your personal responsibility

You bear all responsibility for your AI-assisted contributions.

## Agent instructions

You must configure your coding assistant to read and follow the `AGENTS.md` file that is included in [the repository's]({{config.repo_url}}) base directory.

Most coding assistants do this automatically.
If yours does not, create appropriate symlinks (such as `CLAUDE.md`).

## Declaration required

When you submit an AI-assisted contribution, you must declare the tool you used, and the model your tool employed, in an `Assisted-by:` line in your commit message.

For example:

```patch
feat: Cover superfrobnication

Document the new superfrobnication facility in Cleura AI.

Assisted-by: coding-assistant/blerg3.6-coder
```
