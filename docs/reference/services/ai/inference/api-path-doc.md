---
description: Cleura AI API documentation and endpoints
---

# API documentation and endpoints

??? note "Invite-only access"
    Access to {{brand_ai}} is currently invite-only.

Here you may find information on the API documentation and endpoints, and a list of OpenAPI compatible API paths with related documentation.

## API documentation and API endpoints

API documentation and API endpoint URLs are at the [{{brand_ai_inference_service}} API](https://{{ai_inference_api_domain}}/swagger) page.

## OpenAI compatible API paths and documentation

| Path                       | URL                                                           | Reference Documentation                                                                                                  |
|----------------------------|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| `/v1/models`               | `https://{{ai_inference_api_domain}}/v1/models`               | [models](https://developers.openai.com/api/reference/resources/models)                                                   |
| `/v1/chat/completions`     | `https://{{ai_inference_api_domain}}/v1/chat/completions`     | [chat completions](https://developers.openai.com/api/reference/resources/chat/subresources/completions)                  |
| `/v1/completions`          | `https://{{ai_inference_api_domain}}/v1/completions`          | [completions](https://developers.openai.com/api/reference/resources/completions)                                         |
| `/v1/embeddings`           | `https://{{ai_inference_api_domain}}/v1/embeddings`           | [embeddings](https://developers.openai.com/api/reference/resources/embeddings/methods/create)                            |
| `/v1/audio/transcriptions` | `https://{{ai_inference_api_domain}}/v1/audio/transcriptions` | [transcriptions](https://developers.openai.com/api/reference/resources/audio/subresources/transcriptions/methods/create) |
| `/v1/decisions`            | `https://{{ai_inference_api_domain}}/v1/decisions`            | [decisions](https://developers.openai.com/api/reference/resources/decisions/)                                            |
| `/v1/responses`            | `https://{{ai_inference_api_domain}}/v1/responses`            | [responses](https://developers.openai.com/api/reference/resources/responses/)                                            |

## Anthropic compatible API paths and documentation

| Path           | URL                                               | Reference Documentation                                           |
|----------------|---------------------------------------------------|-------------------------------------------------------------------|
| `/v1/messages` | `https://{{ai_inference_api_domain}}/v1/messages` | [messages](https://platform.claude.com/docs/en/api/http/messages) |

## Jina AI compatible API paths and documentation

| Path         | URL                                             | Reference Documentation                                                     |
|--------------|-------------------------------------------------|-----------------------------------------------------------------------------|
| `/v1/rerank` | `https://{{ai_inference_api_domain}}/v1/rerank` | [rerank](https://docs.jina.ai/#tag/search-foundation-models/POST/v1/rerank) |

## TypeSafe AI (SystemOne) compatible API paths and documentation

| Path            | URL                                                | Reference Documentation                              |
|-----------------|----------------------------------------------------|------------------------------------------------------|
| `/v1/systemone` | `https://{{ai_inference_api_domain}}/v1/systemone` | [systemone](https://docs.typesafe.ai/api/system-one) |
