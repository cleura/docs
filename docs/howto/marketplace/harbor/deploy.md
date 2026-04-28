---
description: How to deploy a Harbor instance in Cleura Cloud
---

# Creating a Harbor instance

This guide covers the deployment of a self-hosted [Harbor](https://goharbor.io/) service.

To proceed, make sure you have an [account in {{brand}}](../../getting-started/create-account.md), and you are logged in to the [{{gui}}](https://{{gui_domain}}).

## Step-by-step deployment

In the left vertical pane of the {{gui}}, expand the *Marketplace* category and click on *Discover Apps and Services*.
In the central pane, you will see all available applications and services.
Locate the *Harbor* box and click the *View* button.

![Select the Harbor application](assets/new-harbor/harbor-01_light.png#only-light)
![Select the Harbor application](assets/new-harbor/harbor-01_dark.png#only-dark)

You will see the *Harbor* information page, where you can learn more about its features, and obtain pricing information.
Click the *Deploy this App* button to start the deployment process.

![Start the Harbor deployment process](assets/new-harbor/harbor-02_light.png#only-light)
![Start the Harbor deployment process](assets/new-harbor/harbor-02_dark.png#only-dark)

The Harbor application is hosted on a [Nova VM](../../openstack/nova/new-server.md), so now you may select a region, a name, a flavor, a public network, a keypair, and a security group for it.
Regarding the security group, [make sure it includes a rule](../../openstack/neutron/create-security-groups.md) allowing incoming TCP connections to port 80.

![Specify the characteristics of the particular Harbor deployment](assets/new-harbor/harbor-03_light.png#only-light)
![Specify the characteristics of the particular Harbor deployment](assets/new-harbor/harbor-03_dark.png#only-dark)

Read and agree to the *Terms and Conditions.*
When you are ready, click the *Create* button.

![Read and agree to the Terms and Conditions, and click the Create button](assets/new-harbor/harbor-04_light.png#only-light)
![Read and agree to the Terms and Conditions, and click the Create button](assets/new-harbor/harbor-04_dark.png#only-dark)

The deployment takes some minutes to complete.
To check how it is going, expand the Marketplace category in the vertical pane on the left and click *Provisioned Apps*.
In the central pane, watch the Harbor Heat stack row.
The animated icon at the left marks the deployment progress.

![Check the deployment progress](assets/new-harbor/harbor-05_light.png#only-light)
![Check the deployment progress](assets/new-harbor/harbor-05_dark.png#only-dark)

When the deployment is complete, you will see a check mark in a circle.

![Harbor is deployed](assets/new-harbor/harbor-06_light.png#only-light)
![Harbor is deployed](assets/new-harbor/harbor-06_dark.png#only-dark)

## Logging into the Harbor dashboard

You must know Harbor's public IP address and the password automatically generated for the `admin` user.
For that, make sure you are in the *Provisioned Apps* pane.
Click on the Harbor row to expand it, and select the *Stack Output* tab.

![Locate the public IP and the admin user password](assets/new-harbor/harbor-dashboard-01_light.png#only-light)
![Locate the public IP and the admin user password](assets/new-harbor/harbor-dashboard-01_dark.png#only-dark)

In the *admin_credentials* row, click the icon in the *Action* column.
A pop-up window appears.
Click the *Copy Output!* button to copy the content of the *Output* box to the clipboard.
Paste that into a new text editor window, but don't save it in a new file.
Instead, we recommend you create a new entry in your password manager of choice and move the username and the password there.
Close the pop-up window by clicking on the *Back* button.

![Copy the username and password to the clipboard](assets/new-harbor/harbor-dashboard-02_light.png#only-light)
![Copy the username and password to the clipboard](assets/new-harbor/harbor-dashboard-02_dark.png#only-dark)

Next, get a pop-up window revealing the particular Harbor deployment's public IP address.
Click the icon in the *Action* column of the *harbor_url* row, then click the *Copy Output!* button.
Use the IP address to create a URL of the form `http://<public-ip>`, and put that URL into the Harbor password manager entry.

![Reveal the application public IP](assets/new-harbor/harbor-dashboard-03_light.png#only-light)
![Reveal the application public IP](assets/new-harbor/harbor-dashboard-03_dark.png#only-dark)

Using your favorite web browser, navigate to `http://<public-ip>`.
The Harbor login page appears.
In the left vertical pane, type in the user name (`admin`), paste the password from your password manager, and click the *LOG IN* button below.

![The Harbor login page](assets/new-harbor/harbor-dashboard-04.png)

You are directed to the Harbor main page.

![The main Harbor page](assets/new-harbor/harbor-dashboard-05.png)

On a separate browser window or tab, navigate to the [Harbor documentation page](https://goharbor.io/docs/) to learn how to start using your new self-hosted container registry.
