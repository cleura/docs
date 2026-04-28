---
description: How to deploy a Prometheus instance in Cleura Cloud
---

# Creating a Prometheus instance

This guide covers the deployment of a self-hosted [Prometheus](https://prometheus.io/) service.

To proceed, make sure you have an [account in {{brand}}](../../getting-started/create-account.md), and you are logged in to the [{{gui}}](https://{{gui_domain}}).

## Step-by-step deployment

In the left vertical pane of the {{gui}}, expand the *Marketplace* category and click on *Discover Apps and Services*.
In the central pane, you will see all available applications and services.
Locate the *Prometheus* box and click the *View* button.

![Select the Prometheus application](assets/new-prometheus/prometheus-01_light.png#only-light)
![Select the Prometheus application](assets/new-prometheus/prometheus-01_dark.png#only-dark)

You will see the *Prometheus* information page, where you can learn more about its features, and obtain pricing information.
Click the *Deploy this App* button to start the deployment process.

![Start the Prometheus deployment process](assets/new-prometheus/prometheus-02_light.png#only-light)
![Start the Prometheus deployment process](assets/new-prometheus/prometheus-02_dark.png#only-dark)

The Prometheus application is hosted on a [Nova VM](../../openstack/nova/new-server.md), so now you may select a region, a name, a flavor, a public network, a keypair, and a security group for it.
Regarding the security group, [make sure it includes a rule](../../openstack/neutron/create-security-groups.md) allowing incoming TCP connections to port 9090.

![Specify the characteristics of the particular Prometheus deployment](assets/new-prometheus/prometheus-03_light.png#only-light)
![Specify the characteristics of the particular Prometheus deployment](assets/new-prometheus/prometheus-03_dark.png#only-dark)

Read and agree to the *Terms and Conditions.*
When you are ready, click the *Create* button.

![Agree to the Terms and Conditions, and click the Create button](assets/new-prometheus/prometheus-04_light.png#only-light)
![Agree to the Terms and Conditions, and click the Create button](assets/new-prometheus/prometheus-04_dark.png#only-dark)

The deployment takes some minutes to complete.
To check how it is going, expand the *Marketplace* category in the vertical pane on the left and click *Provisioned Apps*.
In the central pane, watch the Prometheus Heat stack row.
The animated icon at the left marks the deployment progress.

![Check the deployment progress](assets/new-prometheus/prometheus-05_light.png#only-light)
![Check the deployment progress](assets/new-prometheus/prometheus-05_dark.png#only-dark)

When the deployment is complete, you will see a check mark in a circle.

![Prometheus is deployed](assets/new-prometheus/prometheus-06_light.png#only-light)
![Prometheus is deployed](assets/new-prometheus/prometheus-06_dark.png#only-dark)

## Logging into the Prometheus dashboard

You need your deployment's URL.
For that, make sure you are in the *Provisioned Apps* pane.
Click on the Prometheus row to expand it, and select the *Stack Output* tab.

![Get default credentials and URL](assets/new-prometheus/prometheus-dashboard-01_light.png#only-light)
![Get default credentials and URL](assets/new-prometheus/prometheus-dashboard-01_dark.png#only-dark)

Click the icon at the right of the *prometheus_url* row.
A pop-up window appears.
Click the *Copy Output!* button to copy the URL into the clipboard.

![Get default credentials and URL](assets/new-prometheus/prometheus-dashboard-02_light.png#only-light)
![Get default credentials and URL](assets/new-prometheus/prometheus-dashboard-02_dark.png#only-dark)

Using your favorite web browser, navigate to your Prometheus deployment's URL.
The Prometheus page appears.

![The Prometheus page](assets/new-prometheus/prometheus-dashboard-03.png)

We recommend you start with the official [Getting Started](https://prometheus.io/docs/prometheus/latest/getting_started/) page to learn how to use your new monitoring service.
