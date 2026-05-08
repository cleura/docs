---
description: Cleura AI lets organisations use large language models or speech recognition without managing infrastructure.
---

# {{brand_ai}}

??? note "Invite-only access"
    Access to {{brand_ai}} services is currently invite-only.

{{page.meta.description}}

Large Language Models ([LLMs](https://en.wikipedia.org/wiki/Large_language_model)) represent a specific subset of artificial intelligence ([AI](https://en.wikipedia.org/wiki/Artificial_intelligence)), focused on processing and generating human language.
Unlike broader AI systems that may handle computer vision, robotics, or general pattern recognition, LLMs specialise in text-based tasks including natural language "understanding", generation, translation, and reasoning.

{{brand_ai}} gives you access to these models.
You control data location and legal rules.

{{brand_ai}} falls into the broader category of AI-as-a-Service offerings.
It eliminates the operational overhead of model deployment, version management, and infrastructure scaling.
At the same time, {{brand_ai}} is compliant with data sovereignty requirements, ensuring all inference processing occurs within EU data centres.

{{brand_ai}} uses shared and on-demand resources.

## Shared and on-demand capacity

On-demand AI uses shared model instances from {{company}}.
When you use the API, it

* checks your API key and model access,
* sends your request to an available model,
* processes your request, streaming results if needed,
* returns results and usage data,
* removes input and response from memory,
* keeps only metadata for billing.

Model usage is recorded on a per-request basis, rather than by tracking resource allocation over time.
Even though multiple customers may be utilising the same model instance, security layers always guarantee complete request isolation.
No crosstalk between concurrent requests is possible, and no data containing the content of any request is ever stored after the request has been completed.

Models load on GPUs based on usage patterns to reduce wait times.

## API access and authentication

{{brand_ai}} provides an [OpenAI](https://en.wikipedia.org/wiki/OpenAI)-compatible API, accessible through standard HTTPS endpoints.
Customer authentication uses API keys generated and managed via the {{gui}}.

OpenAI-compatible API keys have:

* Optional expiry dates,
* IP range limits,
* Model access control,
* Usage tracking for billing.

API keys connect to {{company}} accounts.
This tracks usage by projects, teams, or applications.

For API details, see the [AI reference section](../../reference/ai/index.md).

## Supported models

{{company}} maintains a curated selection of open-source models, optimised for a shared GPU pool.
Those models are selected based on community adoption, performance characteristics, and enterprise suitability.
The [model catalogue](../../reference/ai/llms.md) updates regularly as new versions are released.

## Data privacy and compliance

{{brand_ai}} is architected for strict data privacy and regulatory compliance.

The way data is handled guarantees that

* no data is logged beyond metadata (timestamps, token counts, IP addresses, API keys),
* no prompt or completion content is stored on {{company}} infrastructure,
* no customer data is used for model training or improvement,
* all processing occurs within a {{company}} Stockholm region data centre,
* there is full [GDPR](https://gdpr-info.eu) compliance for EU data residency requirements.

What follows are the metadata that are logged per inference request:

* Request start and end times,
* Audio length in seconds,
* Prompt tokens count,
* Completion tokens count,
* Source IP address, and
* API key identifier.

This metadata allows billing and security checks.
API key links usage to customer accounts.
