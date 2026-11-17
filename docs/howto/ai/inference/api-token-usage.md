---
description: How to monitor API and token usage in the Cleura AI Inference Dashboard
---
# Monitoring API and token usage

??? note "Invite-only access"
    Access to {{brand_ai}} is currently invite-only.

To monitor API and token usage, log into the [{{brand_ai_inference_dashboard}}](https://{{ai_inference_api_domain}}) with an Admin [API key](api-keys.md).

In the left-hand pane, click *API Usage*.
The main pane shows this month's usage, with the *Requests* metric selected and charted per day.
The tiles above the chart summarize requests, tokens, cost, average time to first token, throughput, concurrency, and queueing.
Below the chart, a table breaks the usage down by model or by API key.

![Viewing this month's overall API usage by requests](../assets/dashboard-api-token-requests-1_light.png#only-light)
![Viewing this month's overall API usage by requests](../assets/dashboard-api-token-requests-1_dark.png#only-dark)

To chart token usage instead, click the *Tokens* tile.
The chart then splits usage into input and output tokens per day.

![Viewing this month's overall token usage](../assets/dashboard-api-token-tokens-2_light.png#only-light)
![Viewing this month's overall token usage](../assets/dashboard-api-token-tokens-2_dark.png#only-dark)

To narrow the figures to a single API key, choose one using the *All API Keys* drop-down menu above the tiles.
In the example below, the figures pertain only to the `yellowknife-devs` key.

![Viewing requests by API key filtering](../assets/dashboard-api-token-by-api-key_light.png#only-light)
![Viewing requests by API key filtering](../assets/dashboard-api-token-by-api-key_dark.png#only-dark)

To narrow the figures to a single model, choose one using the *All Models* drop-down menu.
In the example below, only the `qwen3.6-35b-a3b-fp8` model contributes to the statistics and to the chart.
To return to the unfiltered view, click *Clear filters*.

![Viewing requests by model filtering](../assets/dashboard-api-token-api-by-model_light.png#only-light)
![Viewing requests by model filtering](../assets/dashboard-api-token-api-by-model_dark.png#only-dark)
