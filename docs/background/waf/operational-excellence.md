---
description: Operational Excellence is the ability to run and monitor workloads reliably, and to continually improve processes and procedures.
---

# Operational Excellence

Operational Excellence is the ability to run and monitor workloads reliably, and to continually improve processes and procedures.

On {{brand}} this means treating infrastructure as code, standardizing deployments, and being able to respond to and learn from operational events.

## Design principles

- Manage infrastructure as code so changes are reviewable, repeatable, and reversible.
- Standardize and automate deployments through reusable templates and Infrastructure as Code rather than manual configuration.
- Make frequent, small, reversible changes rather than large, risky ones.
- Anticipate and plan for operational failure with documented runbooks.
- Learn from every operational event and feed it back into procedures.

## Applying this on {{brand}}

- Use {{company}}'s Launch Pad (via Heat, Ansible, or OpenTofu) to bootstrap initial connectivity into a new environment — it creates an SSH keypair, a router and network with public access, and a restrictable jump host.
  It's a convenient entry point, not a landing zone:
  project structure, quotas, IAM boundaries, and a security baseline still need to be set up separately using the practices in this framework.
- Provision and manage resources through the {{gui}} (CCMP), CLI, or API — and drive routine provisioning through Infrastructure-as-Code rather than manual clicks, so changes are auditable and repeatable.
- Use OpenStack projects to cleanly separate development, test, and production environments, and to scope team access to only what each group needs.
- Using IaC as the standard for your infrastructure deployments.
  It provides a consistent, standard methodology for development and deployment for all components of your workload.
- Build golden images or make use public cloud images and use a tool like ansible to make your hardening, configuration, upgrades.
- Integrate CI/CD pipelines with {{company}}'s managed Kubernetes ({{k8s_management_service}}) clusters for automated, auditable application deployment.
- Where internal operations capacity is limited, offload monitoring, patching, and backup management to {{company}} Managed Services so your team can focus on the application layer.
- Use {{company}}'s architects and consultants for design reviews, migrations, or CI/CD integration work that benefits from platform-specific expertise.

## Self-assessment checklist

- Is infrastructure provisioned through code or API calls rather than ad hoc manual changes?
- If the project used {{company}}'s Launch Pad to bootstrap connectivity, has project structure, IAM, quotas, and a security baseline been set up separately — since Launch Pad itself does not provide these?
- Do you have documented, tested runbooks for common operational events (failover, scale-out, incident response)?
- Are environments (dev/test/prod) cleanly separated using projects?
- Do deployments happen through a CI/CD pipeline rather than manual steps?
- After an incident, is there a process to feed lessons back into runbooks and architecture?
