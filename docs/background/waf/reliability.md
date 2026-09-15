---
description: Cleura Compliant Cloud's architecture provides strong building blocks.
---

# Reliability

Reliability is the ability of a workload to perform its intended function correctly and consistently, including its ability to recover quickly from failure.

{{brand_compliant}} provides a multi-availability-zone architecture and built-in snapshot-based recovery.
These features give you strong building blocks.

## Design principles

- Distribute workloads across availability zones or regions rather than relying on a single data center.
- Automate recovery from failure instead of relying on manual intervention.
- Test recovery procedures regularly, not just at initial launch.
- Scale horizontally to spread risk across multiple smaller resources.
- Manage change through automation to reduce human error.

## Applying this on {{brand}}

- Deploy production workloads across {{brand_compliant}}'s availability zones.
  Each zone is an independently powered and networked data center, interconnected by redundant, low-latency fiber.
  A single facility failure cannot take down the workload.
- Use {{company}}'s Load Balancer service to distribute traffic across instances and integrate it with auto-scaling for resilience under variable load.
- Enable {{company}}'s automated daily snapshots of virtual servers and storage volumes.
  The snapshots are retained for 10 or 30 days.
  This built-in, low-effort disaster-recovery layer delivers fast RPO/RTO without third-party backup tooling.
  Periodically test restoring from them.
  You can also choose immutable backups.
- For workloads that need regional resilience beyond a single cloud region, architect cross-region disaster recovery across {{company}}'s regions (Stockholm, Karlskrona, Frankfurt).
- Use Managed Database and Managed Kubernetes/OpenShift services where you want {{company}} to handle patching, monitoring, and high-availability configuration on your behalf.

## Designing for reliability: Virtual Machines

VM-based workloads on {{brand}} should be architected so that no single instance, host, or availability zone is a point of failure.

- Use OpenStack anti-affinity server groups to place replica instances of the same tier (e.g., web or application nodes) on different physical hosts.
  A single hypervisor failure cannot remove every replica at once.
- Spread each tier's instances across multiple availability zones in the {{brand_compliant}}, not just across hosts within one zone, so a data-center-level event only affects part of your capacity.
- Boot instances from volumes rather than local ephemeral disk when the instance needs to survive host maintenance, evacuation, or rebuild without losing its state.
- Place a Load Balancer in front of any tier that has more than one instance, with health checks configured so unhealthy instances are automatically taken out of rotation rather than continuing to receive traffic.
- Enable the automated daily snapshot policy on both instances and attached volumes.
  Periodically run a real restore, not just a backup, to confirm recovery actually works within your target RTO.
- For stateful services such as databases or message queues, do not rely on snapshots alone if you need a low RPO.
- Pair them with application-level replication (PostgreSQL streaming replication, MySQL/MariaDB replication, or MongoDB replica sets).
  Alternatively, use Managed Database's own HA configuration where the workload fits a supported engine.
- Be aware that {{brand}} does not provide a native, continuous VM-to-VM replication capability beyond the automated daily snapshot policy.
  For general-purpose VMs where daily snapshots aren't a tight enough RPO, and where the application itself has no built-in replication, you will need to add replication yourself via general purpose backup/DR vendors.
- Treat instances as replaceable, not precious.
- Keep Infrastructure-as-Code up to date so a failed VM can be recreated automatically in minutes instead of repaired by hand.
- Monitor host and instance health continuously through {{brand}} Managed Services or your own tooling.
  Detect degradation before it becomes a customer-facing incident.

## Designing for reliability: containers and Kubernetes

For containerized workloads running on {{company}}'s managed Kubernetes ({{k8s_management_service}}), reliability is split between the platform layer, which {{company}} helps manage, and the workload layer, which is your responsibility to configure correctly.

- Spread worker node pools across multiple availability zones.
  {{k8s_management_service}} supports multi-AZ pools.
  Losing one zone removes only part of your worker capacity instead of the whole cluster.
- Let {{k8s_management_service}} manage control-plane high availability (etcd and the API server) rather than self-managing it, and put your reliability effort into the workload layer where you have the most control.
- Set Pod anti-affinity rules or topology spread constraints so that replicas of the same service land on different nodes and, ideally, different availability zones.
  The default scheduler stacks all replicas on one node otherwise.
- Define readiness and liveness probes on every Deployment so Kubernetes automatically stops routing traffic to pods that aren't ready and restarts pods that have hung.
- Use PodDisruptionBudgets so voluntary disruptions like node upgrades, cluster autoscaler scale-down, and routine maintenance cannot remove every replica of a service at the same time.
- Enable the cluster autoscaler on worker pools so node capacity grows automatically under load and shrinks safely afterward, paired with the Horizontal Pod Autoscaler at the workload level for pod-level scaling.
- Remember that block storage-backed PersistentVolumeClaims are zone-affine.
  A StatefulSet's volume ties its pod to the availability zone where that volume was created.
  Plan storage-backed workload placement with this constraint in mind, particularly when combining it with multi-AZ node pools.
- Run your ingress controller with at least two replicas behind the Load Balancer service, with its own health checks, so the ingress layer itself isn't a single point of failure.
- Use rolling update strategies (maxUnavailable/maxSurge) for deployments and node pool upgrades, and rehearse upgrades in a non-production cluster before rolling them out to production.

## Self-assessment checklist

- Are production workloads distributed across multiple availability zones or regions?
- Are automated snapshots/backups enabled, and have you tested restoring from them?
- Is traffic distributed through a load balancer with health checks rather than a single instance?
- Do you have a documented and tested disaster recovery plan with defined RPO/RTO targets?
- Is scaling (up, down, out, in) automated rather than manual?
- Are VM replicas spread across hosts and zones using anti-affinity policies, rather than left to default scheduling?
- Do stateful VM workloads combine snapshot-based recovery with application-level replication where low RPO matters?
- For VM workloads needing sub-daily RPO with no application-level replication, have you evaluated a third-party or open-source replication tool rather than relying on snapshots alone?
- Are Kubernetes worker node pools spread across multiple availability zones?
- Do your Kubernetes workloads define readiness/liveness probes and PodDisruptionBudgets?
