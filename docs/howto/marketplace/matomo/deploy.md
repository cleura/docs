---
description: How to deploy a Matomo instance in Cleura Cloud
---

# Creating a Matomo instance

This guide covers the deployment of a self-hosted [Matomo](https://matomo.org/) service.

To proceed, make sure you have an [account in {{brand}}](../../getting-started/create-account.md), and you are logged in to the [{{gui}}](https://{{gui_domain}}).

## Step-by-step deployment

In the left vertical pane of the {{gui}}, expand the *Marketplace* category and click on *Discover Apps and Services*.
In the central pane, you will see all available applications and services.
Locate the *Matomo* box and click the *View* button.

![Select the Matomo application](assets/new-matomo/matomo-01_light.png#only-light)
![Select the Matomo application](assets/new-matomo/matomo-01_dark.png#only-dark)

You will see the *Matomo* information page, where you can learn more about its features, and obtain pricing information.
Click the *Deploy this App* button to start the deployment process.

![Start the Matomo deployment process](assets/new-matomo/matomo-02_light.png#only-light)
![Start the Matomo deployment process](assets/new-matomo/matomo-02_dark.png#only-dark)

The Matomo application is hosted on a [Nova VM](../../openstack/nova/new-server.md), so now you may select a region, a name, a flavor, a public network, a keypair, and a security group for it.
Regarding the security group, [make sure it includes a rule](../../openstack/neutron/create-security-groups.md) allowing incoming TCP connections to port 80.

![Specify the characteristics of the particular Matomo deployment](assets/new-matomo/matomo-03_light.png#only-light)
![Specify the characteristics of the particular Matomo deployment](assets/new-matomo/matomo-03_dark.png#only-dark)

Read and agree to the *Terms and Conditions.*
When you are ready, click the *Create* button.

![Read and agree to the Terms and Conditions, then click the Create button](assets/new-matomo/matomo-04_light.png#only-light)
![Read and agree to the Terms and Conditions, then click the Create button](assets/new-matomo/matomo-04_dark.png#only-dark)

The deployment takes some minutes to complete.
To check how it is going, expand the Marketplace category in the vertical pane on the left and click *Provisioned Apps*.
In the central pane, watch the Matomo Heat stack row.
The animated icon at the left marks the deployment progress.

![Check the deployment progress](assets/new-matomo/matomo-05_light.png#only-light)
![Check the deployment progress](assets/new-matomo/matomo-05_dark.png#only-dark)

When the deployment is complete, you will see a check mark in a circle.

![Matomo is deployed](assets/new-matomo/matomo-06_light.png#only-light)
![Matomo is deployed](assets/new-matomo/matomo-06_dark.png#only-dark)

## Logging into the Matomo dashboard

Next, you need the URL of your Matomo instance.
For that, make sure you are in the *Provisioned Apps* pane.
Click on the Matomo row to expand it, and select the *Stack Output* tab.

![Get the URL of your Matomo instance](assets/new-matomo/matomo-dashboard-01_light.png#only-light)
![Get the URL of your Matomo instance](assets/new-matomo/matomo-dashboard-01_dark.png#only-dark)

Get a pop-up window revealing the URL of the particular Matomo deployment.
Click the icon in the *Action* column of the *matomo_url* row, then click the *Copy Output!* button.
Close the pop-up window by clicking on the *Back* button.

![Reveal the application URL](assets/new-matomo/matomo-dashboard-02_light.png#only-light)
![Reveal the application URL](assets/new-matomo/matomo-dashboard-02_dark.png#only-dark)

Using your favorite web browser, navigate to your Matomo deployment's URL.
The Matomo welcome page appears.

![The Matomo welcome page](assets/new-matomo/matomo-dashboard-03.png)

To configure your new traffic analytics service, and to learn how to use it, start with the [Matomo Help Centre](https://matomo.org/help/).

Keep in mind that while configuring Matomo, you will need pieces of information provided in the application's *Stack Output* tab.
