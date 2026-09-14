---
description: How to manage Cleura AI API keys via the dashboard
---
# Managing API keys

??? note "Invite-only access"
    Access to {{brand_ai}} services is currently invite-only.

Whether you want to integrate a specific set of {{brand_ai}} LLMs into your application or web site, or access the models via a third party application you prefer, you first have to create an API key.

## Creating an API key

Expand the *AI* section and select *API Keys*.
On the main pane, all existing API keys appear.
To create a new one, click the *Create API Key* button.

![Creating a new API key for a set of LLMs](assets/create-api-key-01_light.png#only-light)
![Creating a new API key for a set of LLMs](assets/create-api-key-01_dark.png#only-dark)

A new pane slides over.
There, enter a *Name* for the new API key.
Using the *Model Access Selection_ drop-down menu, you may have the new key pertain to all available {{brand_ai}} models (*All*), to specific models only (*Inclusive*), or to all but a few models (*Exclusive*).

You may also use the *Allow access from* section, to allow access to the models from one or more networks only.
Please note that restricting the use of an API key to an IPv4 source network or to a set of IPv4 source networks, blocks using that key via IPv6 altogether.
Also, restricting API key access to an IPv6 source network is not possible.

Finally, you can set an expiration date for the API key;
beyond that date, access to any model using that key will not be possible.

When you are ready, click the *Create* button.

![Set key properties and create the key](assets/create-api-key-02_light.png#only-light)
![Set key properties and create the key](assets/create-api-key-02_dark.png#only-dark)

A new window titled *API Key Created Successfully* pops up.

![Get a copy of the API URL and the bearer token](assets/create-api-key-03_light.png#only-light)
![Get a copy of the API URL and the bearer token](assets/create-api-key-03_dark.png#only-dark)

There are two pieces of information on that window that you need to jot down or, better yet, copy to a suitable password manager entry:

* The *OpenAI Compatible URL,* and
* the *Bearer Token.*

The bearer token is only displayed once, and as soon as you close the pop-up window you do not get to see the token again.

When you have secured the bearer token, click anywhere on the {{gui}} but on the pop-up window to close it.
You will then see all the API keys, including the one you just created, listed on the main pane.

![A list of all API keys, including the new one](assets/create-api-key-04_light.png#only-light)
![A list of all API keys, including the new one](assets/create-api-key-04_dark.png#only-dark)

## Deleting API keys

To delete an API key, first go to the *API Keys* pane of the {{gui}}.
Locate the key you wish to delete, click the :material-dots-horizontal-circle: icon at the right of its row, and select *Delete*.

![Locate the API key you wish to delete](assets/delete-api-key-01_light.png#only-light)
![Locate the API key you wish to delete](assets/delete-api-key-01_dark.png#only-dark)

A popup window appears at the top of the page, asking if you really want to delete the key.
If you are sure you do not need the key anymore, click the *OK* button.

![Confirm API key deletion](assets/delete-api-key-02_light.png#only-light)
![Confirm API key deletion](assets/delete-api-key-02_dark.png#only-dark)

This deletes the API key.
The list of keys is now shortened by one, and you get a confirmation on a bubble at the bottom of the page.

![The API key has been deleted](assets/delete-api-key-03_light.png#only-light)
![The API key has been deleted](assets/delete-api-key-03_dark.png#only-dark)
