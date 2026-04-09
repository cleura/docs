---
description: Cleura AI enables organisations to deploy and consume large language models or make use of speech recognition services, all without managing the underlying infrastructure complexity.
---

# {{brand_ai}}

??? note "Invite-only access"
    Access to {{brand_ai}} services is currently invite-only.

{{page.meta.description}}

Large Language Models ([LLMs](https://en.wikipedia.org/wiki/Large_language_model)) represent a specific subset of artificial intelligence ([AI](https://en.wikipedia.org/wiki/Artificial_intelligence)), focused on processing and generating human language.
Unlike broader AI systems that may handle computer vision, robotics, or general pattern recognition, LLMs specialise in text-based tasks including natural language "understanding", generation, translation, and reasoning.

With {{brand_ai}} you can have managed access to such specialised models.
At the same time, you maintain full control over data residency and compliance requirements.

{{brand_ai}} falls into the broader category of AI-as-a-Service offerings.
It eliminates the operational overhead of model deployment, version management, and infrastructure scaling.
At the same time, {{brand_ai}} is compliant with data sovereignty requirements, ensuring all inference processing occurs within EU data centres.

{{brand_ai}} operates on a flexible resource allocation architecture, built around **shared and on-demand capacity.**

## Shared and on-demand capacity

On-demand AI utilises a *shared* pool of model instances, managed by {{company}}.
When you send an inference request via the API, the system

* validates the API key and checks the corresponding model access permissions,
* routes the request to an available instance of the requested model,
* processes the inference request, optionally streaming the results,
* returns the result (unless it is already streamed) and any requested usage data,
* purges the content of the actual input and response from the GPUs and system memory,
* persists *only* request metadata required for billing.

Model usage is recorded on a per-request basis, rather than by tracking resource allocation over time.
Even though multiple customers may be utilising the same model instance, security layers always guarantee complete request isolation.
No crosstalk between concurrent requests is possible, and no data containing the content of any request is ever stored after the request has been completed.

Models are pre-loaded onto pool GPUs based on usage *patterns*, to minimise cold-start latency.

## API access and authentication

{{brand_ai}} provides an [OpenAI](https://en.wikipedia.org/wiki/OpenAI)-compatible API, accessible through standard HTTPS endpoints.
Customer authentication uses API keys generated and managed via the {{gui}}.

The OpenAI-compatible API key features include:

* Optional expiry dates for time-limited access,
* IP range restrictions for network-level security,
* Model access controls,
* Usage tracking per key for billing and audit purposes.

API keys are tied to specific {{company}} customer accounts, enabling granular tracking of consumption across projects, teams, or applications.

Please find here all the details regarding the available OpenAI-compatible API paths.

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

* Timestamps of request initiation and completion,
* length (in seconds) of audio content uploaded as part of an inference request,
* prompt tokens count,
* completion tokens count,
* source IP address, and
* API key identifier.

The logged metadata enable usage billing and security audit trails, whilst preserving content privacy.
The API key identifiers link consumption to customer accounts for invoicing.
