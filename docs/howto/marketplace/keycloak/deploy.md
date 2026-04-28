---
description: How to deploy a Keycloak instance in Cleura Cloud
---

# Creating a Keycloak instance

This guide covers the deployment of a self-hosted [Keycloak](https://www.keycloak.org/) service.

To proceed, make sure you have an [account in {{brand}}](../../getting-started/create-account.md), and you are logged in to the [{{gui}}](https://{{gui_domain}}).

## Step-by-step deployment

In the left vertical pane of the {{gui}}, expand the *Marketplace* category and click on *Discover Apps and Services*.
In the central pane, you will see all available applications and services.
Locate the *Keycloak* box and click the *View* button.

![Select the Keycloak application](assets/new-keycloak/keycloak-01_light.png#only-light)
![Select the Keycloak application](assets/new-keycloak/keycloak-01_dark.png#only-dark)

You will see the *Keycloak* information page, where you can learn more about its features, and obtain pricing information.
Click the *Deploy this App* button to start the deployment process.

![Start the Keycloak deployment process](assets/new-keycloak/keycloak-02_light.png#only-light)
![Start the Keycloak deployment process](assets/new-keycloak/keycloak-02_dark.png#only-dark)

The Keycloak application is hosted on a [Nova VM](../../openstack/nova/new-server.md), so now you may select a region, a name, a flavor, a public network, a keypair, and a security group for it.
Regarding the security group, [make sure it includes a rule](../../openstack/neutron/create-security-groups.md) allowing incoming TCP connections to port 8080.

Optionally, select one of the available Keycloak versions.

![Specify the characteristics of the particular Keycloak deployment](assets/new-keycloak/keycloak-03_light.png#only-light)
![Specify the characteristics of the particular Keycloak deployment](assets/new-keycloak/keycloak-03_dark.png#only-dark)

Then, read and agree to the *Terms and Conditions.*
When you are ready, click the *Create* button.

![Read and agree to the Terms and Conditions, and click the Create button](assets/new-keycloak/keycloak-04_light.png#only-light)
![Read and agree to the Terms and Conditions, and click the Create button](assets/new-keycloak/keycloak-04_dark.png#only-dark)

The deployment takes some minutes to complete.
To check how it is going, expand the *Marketplace* category in the vertical pane on the left and click *Provisioned Apps*.
In the central pane, watch the Keycloak Heat stack row.
The animated icon at the left marks the deployment progress.

![Check the deployment progress](assets/new-keycloak/keycloak-05_light.png#only-light)
![Check the deployment progress](assets/new-keycloak/keycloak-05_dark.png#only-dark)

When the deployment is complete, you will see a check mark in a circle.

![Keycloak is deployed](assets/new-keycloak/keycloak-06_light.png#only-light)
![Keycloak is deployed](assets/new-keycloak/keycloak-06_dark.png#only-dark)

## Logging into the Keycloak dashboard

You need the administrator's (`admin`) predefined password and the URL of your Keycloak instance.
For that, make sure you are in the *Provisioned Apps* pane.
Click on the Keycloak row to expand it, and select the *Stack Output* tab.

![Get default credentials and URL](assets/new-keycloak/keycloak-dashboard-01_light.png#only-light)
![Get default credentials and URL](assets/new-keycloak/keycloak-dashboard-01_dark.png#only-dark)

We recommend you create a new entry in your password manager and populate all necessary fields with values from the corresponding output keys.

For the preset password, click the icon in the *Action* column of the *admin_credentials* row.
A pop-up window appears.
Click the *Copy Output!* button to copy all data below *Output* into the clipboard.
Temporarily paste that data into a text editor, and use the password for your password manager entry.
When ready, click the *Back* button to close the window.

![Reveal the administrator's password](assets/new-keycloak/keycloak-dashboard-02_light.png#only-light)
![Reveal the administrator's password](assets/new-keycloak/keycloak-dashboard-02_dark.png#only-dark)

Similarly, get the URL to your Keycloak instance from the *keycloak_url* row.

![Reveal the URL to Keycloak](assets/new-keycloak/keycloak-dashboard-03_light.png#only-light)
![Reveal the URL to Keycloak](assets/new-keycloak/keycloak-dashboard-03_dark.png#only-dark)

Using your favorite web browser, navigate to your Keycloak deployment's URL.
The Keycloak Sign-in page appears.
Use the default username (`admin`) and password from your password manager, and click the *Sign in* button.

![The Keycloak login page](assets/new-keycloak/keycloak-dashboard-04.png)

The Keycloak welcome page appears.

![The Keycloak page](assets/new-keycloak/keycloak-dashboard-05.png)

We recommend you start with the official [Keycloak guides](https://www.keycloak.org/guides) page to learn how to use your new identity and access management service.
