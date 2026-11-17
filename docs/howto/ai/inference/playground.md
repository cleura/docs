---
description: How to use the Cleura AI Inference Dashboard Playground
---
# Using the Playground

??? note "Invite-only access"
    Access to {{brand_ai}} is currently invite-only.

To access the Playground, log into the [{{brand_ai_inference_dashboard}}](https://{{ai_inference_api_domain}}) with a User or an Admin [API key](api-keys.md).
The dashboard layout differs by API key type.
The following examples are from the User API key dashboard.

## Chat

In the left-hand pane, click *Chat*.
Then, in the right-hand pane, use the *Model* drop-down menu to select an available LLM.

![Chatting with the selected model](../assets/dashboard-playground-chat_light.png#only-light)
![Chatting with the selected model](../assets/dashboard-playground-chat_dark.png#only-dark)

Before you start chatting, you might want to adjust parameters like [*System prompt*](../../../background/ai/inference/prompts.md), [*Temperature*, and *Effort*](../../../background/ai/inference/parameters.md).

To begin chatting, enter your prompt in the *Ask anything* text input box at the bottom of the main pane.
When you're ready, press `Enter` or click the *Send* button.
The answer appears above, and at the top of the page you also see the prompt you just entered.
Note that you may expand the *Reasoning* box and see what the model understood about your prompt and how it decided to produce an answer.

### Comparing answers

For any prompt, you might want to compare the answers of two different models.
In that case, first click the *Compare* button at the top of the main pane.
Then, on the right-hand pane, use the *PRIMARY* and *SECONDARY* tabs to select the two models.
In the example we provide here, we use the [*System prompt*](../../../background/ai/inference/prompts.md) box to describe a common characteristic for each model.

![Trying the same prompt on two different models](../assets/dashboard-playground-chat-compare_light.png#only-light)
![Trying the same prompt on two different models](../assets/dashboard-playground-chat-compare_dark.png#only-dark)

After you type your prompt and send it, the main pane splits vertically.
In the left half, you get the answer from the *PRIMARY* model, and in the right half, the answer from the *SECONDARY* model.

## Embeddings

To create [*Embeddings*](../../../background/ai/inference/embeddings.md), click that label in the left-hand pane.
In the right-hand pane, notice that a suitable model is selected automatically.

In the *INPUT* box of the main pane, type anything you wish to convert into a vector in a multidimensional space.

![Turning a sentence into an element of a 4096-dimensional vector space](../assets/dashboard-playground-embeddings_light.png#only-light)
![Turning a sentence into an element of a 4096-dimensional vector space](../assets/dashboard-playground-embeddings_dark.png#only-dark)

Click *Run embedding*, and 8 floating-point numbers appear in the *OUTPUT* box.
In the example above, those are only the first 8 coordinates of an element in a 4096-dimensional vector space.

## Audio

You can select the *Audio* tool to transcribe audio input into text.
First, go to the right-hand pane and select any model capable of transcription.
Then, use the *SOURCE* box in the main pane to upload an audio file you wish to transcribe.

![Box for uploading an audio file for transcription](../assets/dashboard-playground-audio-upload_light.png#only-light)
![Box for uploading an audio file for transcription](../assets/dashboard-playground-audio-upload_dark.png#only-dark)

In the example below, we have uploaded the second chapter of [*The&nbsp;Aurora&nbsp;Borealis&nbsp;in&nbsp;1719&nbsp;by&nbsp;Sidney&nbsp;Perley&nbsp;(1858-1928)*](https://librivox.org/coffee-break-collection-13-weather-by-various/), from [LibriVox](https://librivox.org).

![Audio file is uploaded](../assets/dashboard-playground-audio-input_light.png#only-light)
![Audio file is uploaded](../assets/dashboard-playground-audio-input_dark.png#only-dark)

Click *Run transcription* to begin.

![Audio file is transcribed](../assets/dashboard-playground-audio-transcribed_light.png#only-light)
![Audio file is transcribed](../assets/dashboard-playground-audio-transcribed_dark.png#only-dark)

The transcribed text appears in the *TRANSCRIPTION* box, below the *SOURCE* box.

