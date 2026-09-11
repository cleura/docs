---
description: Principles to take into account before making an architecture decision on Cleura Cloud.
---

# General Design Principles

These principles apply across all [five pillars](introduction.md) and should inform every architecture decision on {{brand}}.

- Design for failure.
  Assume any instance, volume, or availability zone can fail, and architect so the workload survives it.
- Automate everything repeatable.
  Provision through the {{company}} API, CLI, or Infrastructure-as-Code rather than one-off manual changes in the portal.
- Match the deployment model to the workload's risk profile.
  Use the {{brand_compliant}} for regulated or mission-critical data, the {{brand_public}} for general-purpose workloads, and the {{company}} Private Cloud where full isolation is required.
- Keep architectures open and portable.
  {{brand}}'s OpenStack foundation avoids proprietary lock-in — design workloads so they remain portable across regions and, if ever needed, providers.
- Build in security and compliance from day one, not as an afterthought before an audit.
- Test what you assume will work.
  Regularly test backups, failover, and scaling — not just at launch.
- Right-size continuously.
  Cloud resources are elastic;
  provisioning should be revisited as usage patterns change, not fixed at launch.
