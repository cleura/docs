---
description: How to enable HA for the control plane or Worker Groups of a Gardener cluster
---
# Enabling high availability

When you [create a new {{k8s_management_service}} cluster](create-shoot-cluster.md), you have the option to enable high availability (HA) features for its control plane.
In case you have an existing {{k8s_management_service}} cluster with a non-HA control plane, you may at any time enable the HA features for that control plane.

!!! warning "HA for control plane cannot be disabled"
    Keep in mind that once you enable HA for the control plane of a {{k8s_management_service}} cluster, you cannot disable it for that particular cluster.

Additionally, you may add HA characteristics to one or more Worker Groups of an existing cluster.

## Enabling HA for the control plane

Using your favorite web browser, navigate to <https://{{gui_domain}}> and log in.
In the left-hand side panel, choose *Containers → [{{k8s_management_service}}](https://{{gui_domain}}/containers/gardener)*.
Then, in the central pane of the {{gui}}, you see all of your {{k8s_management_service}} clusters, organized by {{brand}} region.

![Get the list of all available {{k8s_management_service}} clusters](assets/shoot-enable-ha-01_light.png#only-light)
![Get the list of all available {{k8s_management_service}} clusters](assets/shoot-enable-ha-01_dark.png#only-dark)

Locate the cluster you are interested in, and click the :material-dots-horizontal-circle: icon on the right of the corresponding row.
From the drop-down menu that appears, select *Modify Cluster*.

![Select the option for modifying a cluster](assets/shoot-enable-ha-02_light.png#only-light)
![Select the option for modifying a cluster](assets/shoot-enable-ha-02_dark.png#only-dark)

A vertical pane titled *Modify Gardener Shoot Cluster* slides over from the right.
In it, you see the disabled option *Enable Highly Available Control Plane*.
Click on it to enable HA for the control plane of the shoot cluster.

As soon as you enable HA, Control Plane components spread out and live across all Availability Zones.
Then, in case of an Availability Zone outage, the Control Plane for the cluster remains available.

![Notice the option for enabling control plane HA](assets/shoot-enable-ha-03_light.png#only-light)
![Notice the option for enabling control plane HA](assets/shoot-enable-ha-03_dark.png#only-dark)

Before the change is applied, a warning appears:
enabling HA is an irreversible action.
Once you take it, there is no way to disable HA at a later time.

![Select HA for the control plane](assets/shoot-enable-ha-04_light.png#only-light)
![Select HA for the control plane](assets/shoot-enable-ha-04_dark.png#only-dark)

If you are sure you want to enable HA, scroll down a bit until you see the *Update* button and click on it.

![Activate HA for the control plane](assets/shoot-enable-ha-05_light.png#only-light)
![Activate HA for the control plane](assets/shoot-enable-ha-05_dark.png#only-dark)

Enabling HA for the control plane of any {{k8s_management_service}} cluster takes a few minutes.
You can see how the process is progressing by the animated icon on the left of the cluster row.

![HA for control plane is being prepared](assets/shoot-enable-ha-06_light.png#only-light)
![HA for control plane is being prepared](assets/shoot-enable-ha-06_dark.png#only-dark)

As soon as HA is enabled, the animated icon changes into a check mark (:material-check-circle:).

![HA for control plane is now enabled](assets/shoot-enable-ha-07_light.png#only-light)
![HA for control plane is now enabled](assets/shoot-enable-ha-07_dark.png#only-dark)

## Enabling HA for Worker Groups

You may add HA characteristics to one or more Worker Groups by modifying the *Autoscaler&nbsp;Min* and *Autoscaler&nbsp;Max* parameters.

First off, select the {{k8s_management_service}} cluster you are interested in.
Click on the cluster row to expand its characteristics, then select the *Worker Groups* tab.

![View Worker Group details](assets/shoot-enable-ha-08_light.png#only-light)
![View Worker Group details](assets/shoot-enable-ha-08_dark.png#only-dark)

Click once more on the :fontawesome-solid-pen-to-square: icon of the Worker Group you wish to modify.
A vertical pane named *Modify Worker Group* slides over from the right.

![Modify Worker Group](assets/shoot-enable-ha-09_light.png#only-light)
![Modify Worker Group](assets/shoot-enable-ha-09_dark.png#only-dark)

Modify the *Autoscaler&nbsp;Min* and *Autoscaler&nbsp;Max* parameters.
You may, for instance, set *Autoscaler&nbsp;Min* to 5 and *Autoscaler&nbsp;Max* to 7.
When you are ready to apply the changes, click the *Update* button.

![Modify autoscaling parameters](assets/shoot-enable-ha-10_light.png#only-light)
![Modify autoscaling parameters](assets/shoot-enable-ha-10_dark.png#only-dark)

After a few seconds, the new values for the autoscaler parameters will be visible in the *Worker Groups* tab.

![View modified Worker Group](assets/shoot-enable-ha-11_light.png#only-light)
![View modified Worker Group](assets/shoot-enable-ha-11_dark.png#only-dark)

## Having Worker Groups in different Availability Zones

Another way to make Worker Groups highly available is to have *at least* two such groups, each in its own Availability Zone (AZ).

To create a new Worker Group in its own AZ, begin by locating the cluster you are interested in, then click its row to have all relevant details in full view.
Click once more on the *Worker Groups* tab to see all available groups.
In the example below, there is only one Worker Group that resides in the AZ named `az1`.
To create a new Worker Group, click on the green *Create a Worker Group* button.

![{{k8s_management_service}} cluster with one Worker Group](assets/shoot-enable-ha-12_light.png#only-light)
![{{k8s_management_service}} cluster with one Worker Group](assets/shoot-enable-ha-12_dark.png#only-dark)

A vertical pane named *Create Worker Group* slides over from the right.
There, you see the parameters of a new group.
Before you create it, click on the drop-down menu for *Availability Zones*, and indicate an AZ for the new group.
Make sure you pick one which is **different** from the AZ where the first Worker Group resides.

![selecting an availability zone for a new worker group](assets/shoot-enable-ha-13_light.png#only-light)
![selecting an availability zone for a new worker group](assets/shoot-enable-ha-13_dark.png#only-dark)

Optionally, you can have the new Worker Group reside **only** in the new AZ you just selected:
for that, click the old AZ label to remove it.
Finally, click on the green *Create* button to instantiate the new WG.

![Removing the label of the default Availability Zone and create the new Worker Group](assets/shoot-enable-ha-14_light.png#only-light)
![Removing the label of the default Availability Zone and create the new Worker Group](assets/shoot-enable-ha-14_dark.png#only-dark)

When the new Worker Group is ready, you can see all groups in the *Worker Groups* tab, each in its own AZ.

![Two Worker Groups, each in its own Availability Zone](assets/shoot-enable-ha-15_light.png#only-light)
![Two Worker Groups, each in its own Availability Zone](assets/shoot-enable-ha-15_dark.png#only-dark)

