---
description: Security is the ability to protect data, systems, and assets while meeting business and regulatory requirements.
---

# Security & Digital Sovereignty

Security is the ability to protect data, systems, and assets while meeting business and regulatory requirements.

{{brand}} adds a distinctive dimension here:
as a fully European provider not subject to US extraterritorial surveillance laws, {{company}} lets you design for data sovereignty as a first-class architectural concern, not just a compliance checkbox.

## Design principles

- Apply defense in depth across network, host, and application layers.
- Enforce least-privilege access and isolate workloads by project.
- Choose the deployment model and region that match your data's regulatory tier.
- Encrypt data at rest and in transit, and control key management deliberately.
- Maintain traceability through logging and monitoring of security-relevant events.

## Applying this on {{brand}}

- Segment workloads into separate OpenStack projects, each with its own quotas and access controls, so a compromise in one project cannot easily spread to another.
- Use stateful security group rules at the instance and subnet level to enforce least-privilege network access, and prefer private networking with VPN extension over exposing services directly to the internet.
- For regulated workloads — healthcare, financial services, public sector, or anything with GDPR, NIS2, or DORA obligations — run on {{brand_compliant}}, which layers additional hardware and software security configuration on top of the standard platform.
- Take advantage of EU-only data residency:
  {{company}}'s regions (Stockholm, Karlskrona, Frankfurt) keep data inside the EU and outside the reach of US extraterritorial legislation such as FISA 702 — a meaningful architectural input when designing for sovereignty-sensitive customers or sectors.
- For the highest-assurance tier, note that the {{brand_public}} and the {{brand_compliant}} facilities are ISO 27001-certified and, in Sweden, meet MSB Protection Class 3 physical security guidelines — factor this into where your most sensitive workloads are placed.
- Engage {{company}}'s professional services for a compliance-aligned architecture review when a workload is subject to sector-specific regulation.

## Self-assessment checklist

- Have you explicitly chosen a deployment model (Public, Compliant, or Private Cloud) based on the workload's regulatory and sensitivity profile?
- Are workloads segmented into separate projects with least-privilege access controls?
- Are security groups and network segmentation applied consistently per workload tier?
- Is sensitive or regulated data confined to EU-resident, appropriately certified infrastructure?
- Do you have logging and alerting in place for security-relevant events?
- Is data encrypted at rest and in transit, with a clear key-management approach?
