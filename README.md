# Cleura Docs

Here's where the content of the <https://docs.cleura.cloud> documentation web site lives.
It is the authoritative source for technical information about Cleura Cloud.

This documentation is licensed under [the CC BY-SA 4.0 license](LICENSE.txt).

If you'd like to add some documentation or fix an issue, please take a look at the [Contribution Guide](https://docs.cleura.cloud/contrib/)!

## Updating generated content

Some documentation pages include content generated from external sources.
To update such pages, use `tox -e update` with the path to the file.

For example, to update the LLM reference table:

```bash
tox -e update -- docs/reference/services/ai/llms.md
```

Run `tox -e update -- --help` to see all supported file paths.
