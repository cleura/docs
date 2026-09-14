---
description: A Well-Architected review is a structured conversation about a specific workload and works best as a recurring practice.
---

# Running a Well-Architected Review & Next Steps

A Well-Architected review is a structured conversation about a specific workload, not a one-off compliance exercise.
It works best as a recurring practice.


## Suggested process

1. Scope the review to a single workload or system with a clear owner.
2. Work through each pillar's checklist with the people who actually operate the workload.
3. Flag every "no" or "unsure" answer as a candidate finding.
   Don't pre-filter.
4. Prioritize findings by risk and effort.
   Not everything needs to be fixed immediately.
5. Record findings and improvement actions in your normal backlog, with owners and target dates.
6. Re-run the review after major architecture changes, and at least quarterly for production workloads.

## Cadence

For new workloads, run a lightweight review before going live, focused on Security and Reliability.

For production workloads, conduct a full review on a quarterly basis, and after any major change (new region, new compliance requirement, significant scale change).

For regulated workloads, align your review cadence with your compliance/audit calendar (e.g., ahead of NIS2 or DORA-related assessments).

## Getting help

{{company}}'s architects and consultants can facilitate a Well-Architected review directly, particularly useful for compliance-sensitive workloads, migrations, or when validating a new architecture before launch.

## Quick Reference: Pillars and {{brand}} Capabilities

| **Pillar**                                                              | **Relevant {{brand}} capability**                                                                                                                                 |
|:------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **[Operational Excellence](operational-excellence.md)**                 | CCMP, CLI & API, Infrastructure-as-Code, projects & quotas, {{k8s_management_service}} CI-CD integration, Managed Services                                        |
| **[Security & Digital Sovereignty](security-digital-sovereignty.md)**   | Compliant Cloud, security groups, project isolation, EU-only regions, ISO 27001 / MSB Protection Class 3 facilities, VPN connectivity                             |
| **[Reliability](reliability.md)**                                       | Availability zones, Load Balancer + auto-scaling, automated daily snapshots (10-day retention), multi-region DR, Managed Database/Kubernetes HA                   |
| **[Performance Efficiency](performance-efficiency.md)**                 | VM flavor profiles (Generic / Low Latency Disk / High Intensity CPU), block & object storage tiers, regional placement, {{k8s_management_service}} worker pools   |
| **[Cost Optimization](cost-optimization.md)**                           | Per-second billing, storage lifecycle policies, project quotas, transparent pricing & volume discounts, Managed Services trade-off                                |

## Next Steps

1. Pick one production workload and run it through the five checklists in this document.
2. Log every gap found as a backlog item, prioritized by risk.
3. Confirm the workload's deployment model was chosen deliberately based on its regulatory, security, and availability requirements — not by default.
4. Schedule the next review — quarterly is a reasonable default for production workloads.

