---
description: Cost Optimization is the ability to run workloads at the lowest price point that still meets business requirements.
---

# Cost Optimization

Cost Optimization is the ability to run workloads at the lowest price point that still meets business requirements, and to understand and control spend over time.

{{company}}'s pay-as-you-go, per-second billing model rewards workloads that are actively right-sized rather than statically over-provisioned.

## Design principles

- Pay only for what you consume, and treat over-provisioning as a cost to be actively eliminated.
- Use storage lifecycle policies to move data to cheaper tiers as it ages.
- Track and attribute cost by project or team so accountability is clear.
- Continuously measure cost-efficiency rather than treating it as a one-off exercise.

## Applying this on {{brand}}

- Take advantage of per-second billing on virtual machines — only pay for the compute time actually used, and shut down non-production instances outside working hours.
- Apply lifecycle and versioning policies on object storage to automatically move aging or infrequently accessed data into archival tiers.
- Use per-project quotas to prevent unplanned overspend and to attribute cost cleanly across teams, environments, or business units.
- Periodically re-evaluate the build-vs-offload trade-off:
  compare the cost of {{company}} Managed Services against your internal operations overhead for patching, monitoring, and backup management.
- Use {{company}}'s transparent, published pricing and available volume discounts to forecast spend accurately and negotiate proactively rather than reactively.

## Self-assessment checklist

- Do you regularly review actual utilization against provisioned quotas and flavors?
- Are storage lifecycle policies in place to move cold data to lower-cost tiers?
- Is spend tracked and attributed by project, team, or environment?
- Are non-production environments scaled down or shut off outside business hours?
- Have you compared the cost of self-managing versus using {{company}} Managed Services for this workload?

