---
description: Performance Efficiency is the ability to use computing resources efficiently to meet requirements, and to maintain that efficiency as conditions change.
---

# Performance Efficiency

Performance Efficiency is the ability to use computing resources efficiently to meet requirements, and to maintain that efficiency as demand, technology, and workload characteristics evolve.

## Design principles

- Select the compute, storage, and network resources that actually match the workload's characteristics.
- Use elasticity — scale resources up and down as demand changes rather than provisioning for peak permanently.
- Prefer managed services over self-managed infrastructure where they remove undifferentiated operational work.
- Continuously monitor and benchmark rather than sizing once and forgetting.

## Applying this on {{brand}}

- Choose the VM flavor profile that fits the workload:
  Generic for general-purpose use, Low Latency Disk for I/O-sensitive applications, or High Intensity CPU for compute-bound workloads.
- Right-size Kubernetes worker pools using mixed VM flavors through {{k8s_management_service}}-managed clusters, matching node types to the actual mix of workloads running on them.
- Match storage to access pattern: high-performance block storage for latency-sensitive workloads, S3-compatible object storage for scalable unstructured data, and archival/lifecycle tiers for cold data.
- Place workloads in the {{company}} region closest to your users — Stockholm, Karlskrona, or Frankfurt — to minimize latency.
- Monitor resource utilization through CCMP or the API on an ongoing basis, and adjust instance flavors, worker pool sizes, and volume types as usage patterns change rather than only at initial deployment.

## Self-assessment checklist

- Are compute and storage types explicitly matched to the workload's actual performance profile?
- Is the workload deployed in the region closest to its primary users?
- Do you monitor utilization on an ongoing basis and adjust sizing accordingly?
- Are Kubernetes worker pools right-sized for the workloads they run, rather than using one flavor for everything?
