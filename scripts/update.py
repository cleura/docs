#!/usr/bin/env python
"""Generate or update documentation files from upstream data sources."""

import os
import re
import sys

import click
import requests

# ---------------------------------------------------------------------------
# Module-level dispatch table: maps file paths to handler
# functions.  Each handler receives the file path and is responsible for
# deciding whether it owns that file.
# ---------------------------------------------------------------------------
handlers: dict[str, callable] = {}


def register_handler(path_pattern: str):
    """Decorator: register a handler for files matching *path_pattern*."""

    def wrapper(fn):
        handlers[path_pattern] = fn
        return fn

    return wrapper


# ---------------------------------------------------------------------------
# llms.md handler
# ---------------------------------------------------------------------------

# Mapping of API model IDs to their human-readable developer origin.
#
# The API only returns "Cleura AI" as the owner for all models, so we
# maintain this static list of regex patterns to infer each model's true
# origin.  Patterns are evaluated in order — the first match wins — so
# more specific patterns must appear before generic ones.
DEVELOPER_PATTERNS: list[tuple[re.Pattern, str]] = [
    (
        re.compile(r"kb-"),
        "Kungliga Biblioteket & OpenAI",
    ),
    (
        re.compile(r"eurollm"),
        "EuroLLM project",
    ),
    (
        re.compile(r"qwen"),
        "Alibaba Cloud",
    ),
    (
        re.compile(r"whisper|gpt"),
        "OpenAI",
    ),
    (
        re.compile(r"^gemma"),
        "Google",
    ),
]

# Mapping of API model IDs to their intended use case.
#
# Models are matched against this list of regex patterns in priority
# order — the first match wins.  Patterns that don't fit any pattern
# fall back to a description derived from architecture modalities.
DESIGN_PATTERNS: list[tuple[re.Pattern, str]] = [
    (
        re.compile(r"kb-whisper"),
        "Speech recognition and translation "
        "(fine-tuned for Nordic languages)",
    ),
    (
        re.compile(r"qwen3\.6"),
        "Code generation, agentic tasks",
    ),
    (
        re.compile(r"qwen3-embedding"),
        "Text embeddings, ranking",
    ),
    (
        re.compile(r"whisper"),
        "Speech recognition and translation",
    ),
    (
        re.compile(r"qwen|gemma"),
        "Complex reasoning, multimodal, agentic tasks",
    ),
    (
        re.compile(r"gpt|eurollm"),
        "Complex reasoning",
    ),
]

# Columns that the generated table will include.
TABLE_COLUMNS = ["Model", "Developed by", "Designed for"]


def api_base_url() -> str:
    """Return the base URL for the Cleura AI inference API."""
    return os.environ.get(
        "OPENAI_API_BASE_URL",
        "https://ai.cleura.cloud/v1",
    )


def api_key() -> str:
    """Return the API key from the environment."""
    return os.environ.get("OPENAI_API_KEY", "")


def fetch_models(base_url: str, key: str) -> list[dict]:
    """Fetch the list of available models from the API.

    Uses the OpenAI-compatible ``GET /v1/models`` endpoint.
    """
    url = f"{base_url}/models"
    headers = {"Authorization": f"Bearer {key}"}

    click.echo(f"Fetching models from {url} …")
    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()

    data = response.json()
    models = data.get("data", [])
    click.echo(f"Received {len(models)} model(s).")
    return models


def model_designed_for(model: dict) -> str:
    """Return the ``Designed for`` description for a model.

    Matches the model ID against a list of regex patterns in priority
    order; the first match wins.  Falls back to a description derived
    from architecture modalities.
    """
    model_id = model.get("id", "")

    # Explicit mapping (patterns evaluated in priority order)
    for pattern, description in DESIGN_PATTERNS:
        if pattern.search(model_id):
            return description

    # Derive from architecture
    architecture = model.get("architecture", {})
    input_mods = architecture.get("input_modalities", [])
    output_mods = architecture.get("output_modalities", [])

    if input_mods == ["audio"] and output_mods == ["text"]:
        return "Speech recognition"
    if input_mods == ["text"] and not output_mods:
        return "Text embeddings"
    if input_mods == ["text"] and output_mods == ["text"]:
        return "Text generation"
    if "image" in input_mods:
        return "Multimodal reasoning"

    return "N/A"


def model_developer(model: dict) -> str:
    """Return the ``Developed by`` description for a model.

    Matches the model ID against a list of regex patterns in priority
    order; the first match wins.  Falls back to ``owned_by`` from the
    API, then to ``"Unknown"``.
    """
    model_id = model.get("id", "")
    for pattern, developer in DEVELOPER_PATTERNS:
        if pattern.search(model_id):
            return developer
    return model.get("owned_by", "Unknown")


def render_llms_table(models: list[dict]) -> str:
    """Render an alphabetically-sorted Markdown table for the given models."""
    # Sort alphabetically by model ID so the table is reproducible.
    models = sorted(models, key=lambda m: m["id"])

    # Determine column widths
    widths = [len(col) for col in TABLE_COLUMNS]
    rows: list[list[str]] = []
    for m in models:
        row = [
            f"`{m['id']}`",
            model_developer(m),
            model_designed_for(m),
        ]
        widths = [max(w, len(c)) for w, c in zip(widths, row)]
        rows.append(row)

    # Build header, separator, and body rows with consistent pipe alignment.
    header = "| " + " | ".join(
        col.ljust(widths[i]) for i, col in enumerate(TABLE_COLUMNS)
    ) + " |"
    sep = (
        "|"
        + "|".join("-" * widths[i] for i in range(len(TABLE_COLUMNS)))
        + "|"
    )
    body_lines = []
    for row in rows:
        body_lines.append(
            "| "
            + " | ".join(cell.ljust(widths[i]) for i, cell in enumerate(row))
            + " |"
        )

    return header + "\n" + sep + "\n" + "\n".join(body_lines) + "\n"


def update_llms_md(table: str, path: str) -> None:
    """Update the table in *path* with the generated *table* string."""
    # Count model rows: starts with '| \`', i.e. a pipe followed by a
    # backtick-enclosed model ID.
    model_count = sum(
        1 for line in table.strip().splitlines()
        if line.startswith("| `")
    )

    summary = (
        "{{brand_ai}} currently offers "
        f"{model_count} on-demand models."
    )

    try:
        with open(path) as f:
            lines = f.readlines()
    except FileNotFoundError:
        click.echo(f"Error: file not found: {path}", err=True)
        sys.exit(1)

    # Find the index of the "Refer to the table" line (original file).
    # If that line isn't present (already updated), fall back to finding
    # the model-count summary line instead.
    refer_index = None
    for i, line in enumerate(lines):
        if "Refer to the table" in line:
            refer_index = i
            break

    if refer_index is None:
        # Already updated: find the "{{brand_ai}} currently offers" line.
        for i, line in enumerate(lines):
            if "{{brand_ai}} currently offers" in line:
                refer_index = i
                break

    if refer_index is None:
        click.echo(
            "Error: could not find the model summary line in file.",
            err=True,
        )
        sys.exit(1)

    # The "Refer to the table" line is preceded by the model-count summary.
    # Include that line in the replacement range so the old summary is removed.
    # If we already found the summary line directly (re-run), don't go back.
    is_original = "Refer to the table" in lines[refer_index]
    start = refer_index - 1 if is_original and refer_index > 0 else refer_index

    # Find the end of the table block:
    #   - Skip blank lines immediately after the "Refer to" line.
    #   - Consume all lines starting with '|'.
    #   - Stop at the first non-blank, non-table line (or end of file).
    table_end = refer_index + 1
    while table_end < len(lines):
        stripped = lines[table_end].rstrip()
        if stripped == "":
            table_end += 1
            continue
        if stripped.startswith("|"):
            table_end += 1
            continue
        break

    # Replace lines [start, table_end) with the new content.
    replacement = [summary + "\n\n"] + table.splitlines(keepends=True) + ["\n"]
    lines[start:table_end] = replacement

    with open(path, "w") as f:
        f.writelines(lines)

    click.echo(f"Updated {path} with {model_count} model(s).")


@register_handler(".md")
def handle_llms(path: str) -> None:
    """Handle ``docs/reference/services/ai/llms.md``."""
    if not path.endswith("services/ai/llms.md"):
        return

    key = api_key()
    if not key:
        click.echo("Error: OPENAI_API_KEY is not set.", err=True)
        sys.exit(1)

    base_url = api_base_url()
    models = fetch_models(base_url, key)
    table = render_llms_table(models)
    update_llms_md(table, path)


# ---------------------------------------------------------------------------
# CLI entry-point
# ---------------------------------------------------------------------------

# Collect every path that handlers mention in their docstrings
# (which are formatted as ``path/to/file``).
HANDLER_PATHS: list[str] = []
for fn in handlers.values():
    if fn.__doc__:
        for part in fn.__doc__.split():
            if part.startswith("``") and part.endswith("``"):
                HANDLER_PATHS.append(part.strip("`"))
            elif part.startswith("``") and part.endswith("``."):
                HANDLER_PATHS.append(part.rstrip(".").strip("`"))


class _HelpCommand(click.Command):
    """Command that appends a paths listing to the help text."""

    def get_help(self, ctx: click.Context) -> str:
        text = super().get_help(ctx)
        if HANDLER_PATHS:
            text += "\n\nSupported paths:"
            for p in HANDLER_PATHS:
                text += f"\n  {p}"
        return text


@click.command(cls=_HelpCommand)
@click.argument("path", type=click.Path(exists=True))
def main(path: str) -> None:
    """Generate or update documentation files from upstream data sources."""

    for suffix, handler in handlers.items():
        handler(path)


if __name__ == "__main__":
    main()
