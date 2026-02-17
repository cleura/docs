---
description: How to spin up a Kubernetes cluster with Gardener
---
# Creating a Kubernetes cluster

To create a Kubernetes cluster, you may use the {{gui}} and, in particular, the {{k8s_management_service}} service.

## Prerequisites

* If this is your first time using {{brand_container_orchestration}}, you need to [activate the service](index.md) from the {{gui}}.
* To access the Kubernetes cluster from your computer, you must [install `kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl) on your local host.

## Creating a Kubernetes cluster in {{gui}}

To get started, navigate to <https://{{gui_domain}}> and, in the left-hand side panel, choose *Containers → [{{k8s_management_service}}](https://{{gui_domain}}/containers/gardener)*.
A central pane named *{{k8s_management_service}} / Shoot Clusters* appears.
There, you can create and manage your {{k8s_management_service}}-based clusters.
In {{k8s_management_service}} terminology, a Kubernetes cluster is called a **shoot** (as in [new plant growth](https://en.wikipedia.org/wiki/Shoot)).

At the top right-hand side of the central pane, click *Create Kubernetes cluster*.

![{{k8s_management_service}} page in {{gui}}](assets/create-shoot-01.png)

A new pane named *Create {{k8s_management_service}} Shoot Cluster* slides over from the right-hand side of the browser.
Type in a name for the new shoot cluster, and select a region.
Also, select the version of Kubernetes the new cluster will be running.
In the example below, we have chosen version 1.33.7.
Please note the *Load balancer provider* parameter, which is already set.
By turning on the setting below, which is by default disabled, you may enable high availability for the **control plane** of the new cluster.

![Create {{k8s_management_service}} Shoot Cluster panel, showing options to type in a cluster name, select a region, set the Kubernetes version, and turn on HA for the control plane](assets/create-shoot-02.png)

You should keep in mind that once you enable high availability for the control plane, you cannot disable it for that particular cluster.

![Once you enable high availability for the control plane, you cannot disable it](assets/create-shoot-03.png)

Next, you may accept the proposed network address (in [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation)) for the worker nodes, or type in the one you prefer.

![Accept the proposed CIDR network address for the worker nodes or type in the CIDR network address you prefer](assets/create-shoot-04.png)

Alternatively, reveal the drop-down menu at the right-hand side of *Network for worker nodes*.
From the available menu items, choose a pre-existing network.
Be sure to select one that has an assigned subnet and is connected to a router.

![Select a pre-existing network](assets/create-shoot-05.png)

Then, define a new subnet for the worker nodes by typing in a CIDR network address.
If the new subnet overlaps with one of the subnets of the network you just selected, you will see an error message in red.

![Try selecting a pre-existing CIDR for the worker nodes](assets/create-shoot-06.png)

Instead, you should define a subnet that does not overlap with any of the subnets of your selected network.

![Set a new, valid subnet for the worker nodes](assets/create-shoot-07.png)

Now, scroll down a bit until you bring the *Worker Groups* section into full view.
Make sure there is at least one defined.
(By default, you start with one Worker Group.)
Pay attention to the values you may set for the following parameters, and keep in mind that they apply to the particular Worker Group only.
If you create another Worker Group, you'll have another set of parameters for it.

* *Flavor:* The [flavor](../../../reference/flavors/index.md) your worker nodes will use;
this determines the number of CPU cores and the amount of RAM allocated to each node.
* *Volume Size:* The amount of local storage allocated to each worker node.
* *Autoscaler Min:* The minimum number of worker nodes to run at any time.
* *Autoscaler Max:* The maximum number of worker nodes the cluster automatically scales to, in case the current number of nodes cannot handle the deployed workload.
* *Max Surge:* The maximum number of additional nodes to deploy in an autoscaling event.

![Worker Group settings](assets/create-shoot-08.png)

For a test cluster, feel free to leave each parameter at its default value.

Scrolling a bit further down, you see that for each Worker Group you may add [*Labels*](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels), [*Annotations*](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations), or [*Taints*](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration).

![Define Labels, Annotations, or Taints](assets/create-shoot-09.00.png)

Each shoot cluster in {{brand}} has a maintenance window.
Additionally, the operating system of the worker nodes can be automatically updated, and so can Kubernetes itself.
Do not change anything regarding the maintenance window or the [updates](rolling-upgrades.md), for everything is already set for you.
Also, do not bother with the *[Hibernation](hibernate-shoot-cluster.md) Schedule* for now.

![Maintenance window and auto-updates](assets/create-shoot-09.01.png)

By default, you can access your shoot clusters from anywhere on the internet.
Still, you may choose to restrict cluster access, permitting it *only* from certain networks.
The allowed networks are described in [CIDR&nbsp;notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation), and you can define one or more by clicking on the green *Set CIDRs...* button.

![You may optionally define networks to allow cluster access from](assets/create-shoot-09.02.png)

In the example below, we only allow access from one Class C network, expressed in CIDR notation.

![Define a Class C network, from which access to the cluster is allowed](assets/create-shoot-09.03.png)

You can define more networks from which cluster access is allowed.
Please keep in mind that, besides new shoot clusters, you can add or remove "allow networks" to or from existing clusters.

When populating the list of allowed networks, include the {{ gui_management_service }} source IP address (`{{gui_management_service_ip}}/32`) to preserve [monitoring](#viewing-details-and-monitoring) functionality.

![You can define more than one networks, from which access to the cluster is allowed](assets/create-shoot-09.04.png)

When you are ready, click the green *Create* button at the bottom of the pane.

![About to create a new {{k8s_management_service}} Shoot Cluster](assets/create-shoot-10.png)

In the list of clusters, you will see your new {{k8s_management_service}} shoot bootstrapping.
The animated icon on the left-hand side of the cluster row marks the progress.
Creating the cluster may take several minutes.

![Shoot cluster bootstrapping](assets/create-shoot-11.png)

Once your {{k8s_management_service}} cluster has successfully launched, a green check mark (:material-check-circle:) will appear to the left of the cluster row.

![Shoot cluster is ready](assets/create-shoot-12.png)

### A note on quotas

Your {{k8s_management_service}} worker nodes are subject to [quotas](../../../reference/quotas/openstack.md) applicable to your {{brand}} project.
It would be best if you kept that in mind when selecting the worker node [*flavor*](../../../reference/flavors/index.md), setting the _volume size_ and the _Autoscaler Max_ values, or when creating more than one Worker Groups, so you will not be at risk of violating any quota.

For example, if your project is configured with the [default quotas](../../../reference/quotas/openstack.md), and you select the `b.4c16gb` flavor for your worker nodes, your cluster would be able to run with a maximum of 3 worker nodes (since their total memory footprint would be 3×16=48 GiB, just short of the default 50 GiB limit).
A 4th node would push your total memory allocation to 64 GiB, violating your quota.

If necessary, be sure to request a quota increase via our [{{support}}](https://{{support_domain}}/servicedesk).

## Viewing details and monitoring

After the new shoot cluster finishes bootstrapping, you may click its row to bring all relevant details into view.
For instance, click the *Details* tab to get networking information about the worker nodes.

![Details regarding the new cluster](assets/create-shoot-13.png)

Next, go to the *Monitoring* tab.
There, you will notice two orange buttons:
one for launching [Prometheus](https://prometheus.io), and one for launching [Plutono](https://github.com/credativ/plutono).

![Monitoring tab for launching Prometheus or Plutono](assets/create-shoot-14.png)

As an example, we have clicked the button for Plutono.
Before launching the dashboard, a pop-up window appears.
This shows the default username (`admin`), and the automatically generated *masked* password.
You get this pop-up every time you click on either of the orange buttons.
In any case, to copy the password into the clipboard, click the related button shown below.
Then, click the orange button labeled *Open Dashboard*.

![Copy the Plutono password](assets/create-shoot-15.png)

After typing in the default username and pasting the password, you get access to the Prometheus or Plutono dashboard for your shoot cluster.
In the example below, we have the Plutono dashboard displaying graphical information regarding the cluster nodes.

![Plutono dashboard displaying information about the worker nodes](assets/create-shoot-16.png)

## Interacting with your cluster

Once your new shoot cluster is operational, you can [start interacting with it](kubectl.md).

