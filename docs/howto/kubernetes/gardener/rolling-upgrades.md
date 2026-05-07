---
description: How to manually upgrade machine images or Kubernetes versions for Gardener clusters
---
# Conducting rolling upgrades

By default, Kubernetes clusters created with {{k8s_management_service}} in {{brand}} are upgraded automatically.
Those upgrades take place during a specified maintenance window, and you may learn more about [what they involve and how they work](../../../background/kubernetes/gardener/autoupgrades.md).
Besides the automatic upgrades, you may manually apply any upgrades available for your cluster.

In the following two examples, we first show how to manually upgrade the machine image for cluster nodes.
Then, we show how to upgrade the Kubernetes version the cluster is running on.

## Upgrading machine images

In the left-hand vertical pane of the {{gui}}, select Containers → [{{k8s_management_service}}](https://{{gui_domain}}/containers/gardener).
In the central pane are your {{k8s_management_service}} clusters, each on its row.

If a Kubernetes upgrade is available for a shoot cluster, you will notice a :fontawesome-solid-circle-arrow-up: icon on the right of the current Kubernetes version.
Additionally, if there is a new machine image for the cluster nodes, you will also notice a :fontawesome-solid-circle-arrow-up: icon on the right of the number of Worker Groups.
In our example, the cluster has 1 Worker Group.

![Garden Linux and Kubernetes upgrades available](assets/shoot-rollupgr-01_light.png#only-light)
![Garden Linux and Kubernetes upgrades available](assets/shoot-rollupgr-01_dark.png#only-dark)

To get more information about the current machine image, click on the cluster row to bring its details into full view, then select the *Worker Groups* tab.
There, you will see the version of the current machine image.
To see the newer version of the image available, hover the mouse over any of the two :fontawesome-solid-circle-arrow-up: icons.
The upgrade process starts by clicking on any one of those.

![About to start Garden Linux upgrade](assets/shoot-rollupgr-02_light.png#only-light)
![About to start Garden Linux upgrade](assets/shoot-rollupgr-02_dark.png#only-dark)

The upgrade process starts immediately and takes some time to complete.
The animated icon at the left-hand side of the cluster row marks the progress.

![Garden Linux upgrade in progress](assets/shoot-rollupgr-03_light.png#only-light)
![Garden Linux upgrade in progress](assets/shoot-rollupgr-03_dark.png#only-dark)

As soon as the upgrade is complete, the new image version is displayed in the *Image* row of the *Worker Groups* tab.
Since we have not upgraded Kubernetes yet, there is still a :fontawesome-solid-circle-arrow-up: icon on the right of the current Kubernetes version.

![Garden Linux upgraded](assets/shoot-rollupgr-04_light.png#only-light)
![Garden Linux upgraded](assets/shoot-rollupgr-04_dark.png#only-dark)

## Upgrading Kubernetes

To get the Kubernetes upgrade process going, click the :material-dots-horizontal-circle: icon on the right-hand side of the cluster row.
In the pop-up menu that appears, there is an option named *Kubernetes Patch Available*.
That one is not always there, and when it is, it acts as yet another indicator of an available Kubernetes upgrade.
Please select the option by clicking on it.

![Kubernetes patch available](assets/shoot-rollupgr-05_light.png#only-light)
![Kubernetes patch available](assets/shoot-rollupgr-05_dark.png#only-dark)

A new pop-up window named *Upgrade Kubernetes Version for: &lt;cluster_name&gt;* appears.
From the *Version* drop-down menu, you may select the new Kubernetes version for your shoot cluster.
When ready, click the *Upgrade* button.

![About to start a Kubernetes upgrade](assets/shoot-rollupgr-06_light.png#only-light)
![About to start a Kubernetes upgrade](assets/shoot-rollupgr-06_dark.png#only-dark)

The upgrade doesn't start right away.
Instead, you are informed that the cluster is indeed ready for it, but there are some notes you might want to read up on before the actual process begins.

![Upgrade notes are available](assets/shoot-rollupgr-07_light.png#only-light)
![Upgrade notes are available](assets/shoot-rollupgr-07_dark.png#only-dark)

Click the *Upgrade* button to start the upgrade process.
The animated icon at the left-hand side of the cluster row indicates the progress of the whole upgrade process.

![Kubernetes upgrade in progress](assets/shoot-rollupgr-08_light.png#only-light)
![Kubernetes upgrade in progress](assets/shoot-rollupgr-08_dark.png#only-dark)

After some minutes, the upgrade will be over.
The new Kubernetes version will be visible on the right of the shoot cluster name.

![Kubernetes successfully upgraded](assets/shoot-rollupgr-09_light.png#only-light)
![Kubernetes successfully upgraded](assets/shoot-rollupgr-09_dark.png#only-dark)
