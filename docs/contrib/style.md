# Style guide

We try to follow a handful of style rules when maintaining this documentation.

## Sections

Generally, content additions should fit somewhere within the existing top-level and second-level sections (like [_Background_](../background/index.md), or [_Kubernetes_](../howto/kubernetes/index.md)).
Try not to introduce a new top-level or second-level section.

## Headings

Keep headings concise, under 80 characters.

## One Sentence per Line

We keep our Markdown to [one sentence per line](https://sive.rs/1s), rather than forcing arbitrary line breaks by mandating a maximum line length.
This facilitates change review, and it also helps notice long run-on sentences.

## Screenshots

If you are contributing a change that contains screenshots from {{gui}}, they should have a resolution of 1920×1080 pixels (1080p).
If your screen has a larger resolution, use [Firefox Responsive Design Mode](https://firefox-source-docs.mozilla.org/devtools-user/responsive_design_mode/) or [Chrome/Chromium Device Mode](https://developer.chrome.com/docs/devtools/device-mode/) to configure your browser with 1080p.

Screenshots should be added to a directory named `assets`, located in the same directory as the Markdown file you are adding or editing.

## CLI screen dumps

If you are contributing a change that contains a screen dump from the `openstack` command-line client, please limit its width to 100 characters.
You can do this by setting the following environment variable in your terminal, before you start working on your change.

``` bash
export CLIFF_MAX_TERM_WIDTH=100
```

## Fenced code blocks

Use explicitly named, fenced [code blocks](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/#usage) to ensure correct syntax highlighting.

Specifically, use `bash` for shell scripts, `json` and `yaml` for JSON and YAML snippets, and `console` for mixed terminal input and output.

## Macros

Whenever an [`extra` variable](https://www.mkdocs.org/user-guide/configuration/#extra) is defined in `mkdocs.yml`, use a [macro](https://mkdocs-macros-plugin.readthedocs.io/) reference, rather than the plain text.

For example, write:

```markdown
{% raw %}This is supported in {{brand}}.{% endraw %}
```

... rather than

```markdown
This is supported in {{brand}}.
```

## Admonitions

We use only three types of [admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/):
Note, Warning, and Danger.

??? note

    Notes are additional bits of information that do not belong in the main text of a page.
    As such, we always make them collapsible:

    ```markdown
    ??? note
        This is a collapsible note.
    ```

!!! warning

    Warnings highlight potentially unintended side effects of otherwise supported functionality.
    We always render them extended:

    ```markdown
    !!! warning
        This is a warning.
    ```

!!! danger

    Danger admonitions highlight dangerous actions, such as ones that might cause data loss.
    As with warnings, we always render them extended:

    ```markdown
    !!! danger
        This is a danger admonition.
    ```

## Renamed sources

If you rename an existing Markdown source, the path of the rendered page's [URI](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier) will change.
In this case, be sure to define a [redirect](https://github.com/mkdocs/mkdocs-redirects) from the old URI to the new one, by adding an entry to the `plugins.redirect.redirect_maps` dictionary in the `mkdocs.yml` configuration file.
