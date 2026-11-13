---
description: How to review available models, create aliases, and view requests
---
# Reviewing available models

??? note "Invite-only access"
    Access to {{brand_ai}} is currently invite-only.

To review all currently available models, log into the [{{brand_ai_inference_dashboard}}](https://{{ai_inference_api_domain}}) with an Admin [API key](api-keys.md).

In the left-hand pane, click *Models*.
A list of every available model appears in the main pane.
Each row shows the model's provider, type, health, and creation date.

![List of all currently available models](../assets/dashboard-model-list_light.png#only-light)
![List of all currently available models](../assets/dashboard-model-list_dark.png#only-dark)

To inspect a model, click its name.
The dialog that opens has an *Overview* tab with the model's health, type, and capabilities, and an *Aliases* tab with its aliases.
From this dialog, you can also click *View requests* or *Try in Playground*.

![Details of the selected model](../assets/dashboard-model-details_light.png#only-light)
![Details of the selected model](../assets/dashboard-model-details_dark.png#only-dark)

## Setting aliases

An alias is a short name that stands in for a model's full name.
A short alias makes the model easier to reference.
To create one, click *Aliases* in the left-hand pane, then click *Add Alias* in the top-right corner of the main pane.

![Choosing to add an alias](../assets/dashboard-model-aliases-1_light.png#only-light)
![Choosing to add an alias](../assets/dashboard-model-aliases-1_dark.png#only-dark)

The *Create Alias* dialog opens.
Enter a name in the *Alias Name* text box, then pick the target model from the *Model* drop-down menu.
Click *Create Alias*.

![Creating a new alias for the selected model](../assets/dashboard-model-aliases-2_light.png#only-light)
![Creating a new alias for the selected model](../assets/dashboard-model-aliases-2_dark.png#only-dark)

The new alias now appears in the list, mapped to the model you chose and marked *Active*.
In the example below, the alias `my-fav-qwen` points to the model `qwen3.6-35b-a3b-fp8`.

![Current list of all aliases](../assets/dashboard-model-aliases-3_light.png#only-light)
![Current list of all aliases](../assets/dashboard-model-aliases-3_dark.png#only-dark)

## Viewing requests

A request is a single call that an application or the Playground made to a model.
To review the requests for a model, click *Requests* in the left-hand pane.
Then, in the main pane, choose the model in the model filter above the request list.
All matching requests appear, with their status, token counts, and creation time.

![All requests for the selected model](../assets/dashboard-model-requests-1_light.png#only-light)
![All requests for the selected model](../assets/dashboard-model-requests-1_dark.png#only-dark)

To see the details of a request, click the :material-eye: icon in its *Actions* column.
The *Request Details* dialog opens, showing the request's ID, status, model, and API key, among other details.

![Viewing details of a specific request](../assets/dashboard-model-requests-2_light.png#only-light)
![Viewing details of a specific request](../assets/dashboard-model-requests-2_dark.png#only-dark)
