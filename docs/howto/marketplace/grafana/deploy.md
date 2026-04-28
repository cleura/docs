---
description: How to deploy a Grafana instance in Cleura Cloud
---

# Creating a Grafana instance

This guide covers the deployment of a self-hosted [Grafana](https://grafana.com/) service.

To proceed, make sure you have an [account in {{brand}}](../../getting-started/create-account.md), and you are logged in to the [{{gui}}](https://{{gui_domain}}).

## Step-by-step deployment

In the left vertical pane of the {{gui}}, expand the *Marketplace* category and click on *Discover Apps and Services*.
In the central pane, you will see all available applications and services.
Locate the *Grafana* box and click the *View* button.

![Select the Grafana application](assets/new-grafana/grafana-01_light.png#only-light)
![Select the Grafana application](assets/new-grafana/grafana-01_dark.png#only-dark)

You will see the *Grafana* information page, where you can learn more about its features, and obtain pricing information.
Click the *Deploy this App* button to start the deployment process.

![Start the Grafana deployment process](assets/new-grafana/grafana-02_light.png#only-light)
![Start the Grafana deployment process](assets/new-grafana/grafana-02_dark.png#only-dark)

The Grafana application is hosted on a [Nova VM](../../openstack/nova/new-server.md), so now you may select a region, a name, a flavor, a public network, a keypair, and a security group for it.
Regarding the security group, [make sure it includes a rule](../../openstack/neutron/create-security-groups.md) allowing incoming TCP connections to port 3000.

![Specify the characteristics of the particular Grafana deployment](assets/new-grafana/grafana-03_light.png#only-light)
![Specify the characteristics of the particular Grafana deployment](assets/new-grafana/grafana-03_dark.png#only-dark)

Read and agree to the *Terms and Conditions.*
When you are ready, click the *Create* button.

![Read and agree to the Terms and Conditions, then click the Create button](assets/new-grafana/grafana-04_light.png#only-light)
![Read and agree to the Terms and Conditions, then click the Create button](assets/new-grafana/grafana-04_dark.png#only-dark)

The deployment takes some minutes to complete.
To check how it is going, expand the Marketplace category in the vertical pane on the left and click *Provisioned Apps*.
In the central pane, watch the Grafana Heat stack row.
The animated icon at the left marks the deployment progress.

![Check the deployment progress](assets/new-grafana/grafana-05_light.png#only-light)
![Check the deployment progress](assets/new-grafana/grafana-05_dark.png#only-dark)

When the deployment is complete, you will see a check mark in a circle.

![Grafana is deployed](assets/new-grafana/grafana-06_light.png#only-light)
![Grafana is deployed](assets/new-grafana/grafana-06_dark.png#only-dark)

## Logging into the Grafana dashboard

You need the administrator's predefined username and password, as well as the URL of your Grafana instance.
For that, make sure you are in the *Provisioned Apps* pane.
Click on the Grafana row to expand it, and select the *Stack Output* tab.

![Get default credentials and URL](assets/new-grafana/grafana-dashboard-01_light.png#only-light)
![Get default credentials and URL](assets/new-grafana/grafana-dashboard-01_dark.png#only-dark)

We recommend you create a new entry in your password manager, and populate all necessary fields with values from the corresponding output keys.

For the preset password, click the icon in the *Action* column of the *admin_password* row.
A pop-up window appears.
Click the *Copy Output!* button to copy the password into the clipboard.
When ready, click the *Back* button to close the window.

![Reveal the administrator's password](assets/new-grafana/grafana-dashboard-02_light.png#only-light)
![Reveal the administrator's password](assets/new-grafana/grafana-dashboard-02_dark.png#only-dark)

Similarly, get the administrator's username from the *admin_username* row.

![Reveal the administrator's user name](assets/new-grafana/grafana-dashboard-03_light.png#only-light)
![Reveal the administrator's user name](assets/new-grafana/grafana-dashboard-03_dark.png#only-dark)

And finally, get your Grafana deployment's URL from the *grafana_url* row.

![Reveal the application's URL](assets/new-grafana/grafana-dashboard-04_light.png#only-light)
![Reveal the application's URL](assets/new-grafana/grafana-dashboard-04_dark.png#only-dark)

Using your favorite web browser, navigate to your Grafana deployment's URL.
The Grafana login page appears.
Use the default username and password, and click the *Log in* button.

![The Grafana login page](assets/new-grafana/grafana-dashboard-05.png)

The Grafana landing page appears.

![The Grafana landing page](assets/new-grafana/grafana-dashboard-06.png)

Start from the official [Grafana documentation](https://grafana.com/docs/grafana/latest/) page to learn how to use your new data visualization service.
