# Parameters

??? note "Invite-only access"
    Access to {{brand_ai}} is currently invite-only.

Model parameters shape how an LLM composes its responses.
We explain two very common parameters, *Temperature* and *Effort*, that you can adjust in the [Playground](../../../howto/ai/inference/playground.md).

## Temperature

With a *low* temperature, responses are more predictable, focused, and consistent.
With a *medium* temperature, responses can be more flexible without becoming overly unpredictable.
Finally, with a *high* temperature, responses are more varied, surprising, and creative, but also less coherent and less reliable.

## Effort

This controls how much computational effort an LLM puts into working through a problem.
While the temperature influences how the LLM presents an answer, the effort influences how much reasoning it performs before it starts composing its response.

When the effort is *None*, no explicit reasoning-effort level is requested, and the exact behavior depends on the provider.
*Less* effort means faster responses and fewer reasoning tokens.
*Medium* effort means a balanced amount of reasoning and processing time.
Finally, *High* effort means extensive reasoning, potentially better handling of difficult problems, but slower responses and higher token usage.
