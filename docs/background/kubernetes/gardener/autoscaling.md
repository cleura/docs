---
description: Autoscaling allows your cluster to grow and shrink as needed.
---
# Autoscaling

Autoscaling is the ability of your {{k8s_management_service}} shoot cluster to add and remove nodes as needed, based on the workload you deploy to the Kubernetes cluster.

Autoscaling in {{brand}} is always **horizontal** rather than vertical, meaning {{k8s_management_service}} adds or removes nodes of the pre-defined machine type ([flavor](../../../reference/services/flavors/index.md)), rather than changing the flavor of existing nodes in-place.

## Default Settings

By default, {{k8s_management_service}} launches 3 initial worker nodes, and limits your cluster to a maximum of 5 nodes.

You can modify these settings (*Autoscaler Min* and *Autoscaler Max*) when you [create a new shoot cluster](../../../howto/kubernetes/gardener/create-shoot-cluster.md), or at any time thereafter.

## How autoscaling works

Autoscaling is designed to be a "hands-off" cluster feature.

Once your cluster decides its resources are insufficient to manage the current workload, it adds nodes to handle it.
This is called **scale-out.**

When the workload becomes less, it removes the extra nodes again.
This is called **scale-in.**

Scale-out is triggered if any [Pod](https://kubernetes.io/docs/concepts/workloads/pods/) on the cluster fails to be [scheduled](https://kubernetes.io/docs/concepts/scheduling-eviction/) to an existing node.
This may be because the node is already overloaded (meaning its `DiskPressure`, `MemoryPressure` or `PIDPressure` [node condition](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/#node-conditions) is active), or because a newly launched Pod is configured with a [request](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#requests-and-limits) that none of the existing nodes can meet.
Thus, scaling out is nearly immediate: as soon as a Pod scheduling failure occurs for one of these reasons, the cluster launches a new worker node --- unless it is already running with the maximum number of nodes, as defined by *Autoscaler Max*.

Scale-in, in contrast, happens when a node's utilization drops below 50% for a period of 30 minutes.
Therefore, scaling in occurs in a delayed fashion.
This is by design: if the dip in resource utilization is only temporary, sufficient worker node capacity is already available when it rebounds.

## Autoscaling limitations

Autoscaling may sometimes not occur when you expect it to, including the following situations:

* If a Pod [spec](https://kubernetes.io/docs/concepts/overview/working-with-objects/#object-spec-and-status) contains a [request](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#requests-and-limits) that is impossible to meet even *with* scale-out, no autoscaling occurs.
  For example, if a Pod were to request 1TiB of memory, and the configured worker node [flavor](../../../reference/services/flavors/index.md) has less than that, then scale-out would not help:
  to run such a Pod, you would instead have to add a new worker group (with a larger flavor) to the cluster.

* If a [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) contains Pods with [anti-affinity rules](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity) that restrict multiple [replicas](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/) from running on the same node, *and* its number of running replicas is already equal to the current number of worker nodes in the group, then no scale-in is possible.
  For example, suppose a Deployment is running with 4 replicas of an anti-affinity Pod in a cluster with default *Autoscaler Min* and *Autoscaler Max* values.
  When at some point that cluster has 4 worker nodes, the fourth node will remain even if its utilization is permanently below 50%.
