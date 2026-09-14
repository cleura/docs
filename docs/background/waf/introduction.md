---
description: Cloud architecture is never finished — it is continuously evaluated, tested, and improved as your business and workloads evolve.
---

# Introduction

{{page.meta.description}}

The {{brand}} Well-Architected Framework gives customers a structured, repeatable way to design, build, and operate workloads on {{brand}}.

It is organized around **five pillars:**

1. [Operational Excellence](operational-excellence.md),
2. [Security & Digital Sovereignty](security-digital-sovereignty.md),
3. [Reliability](reliability.md),
4. [Performance Efficiency](performance-efficiency.md), and
5. [Cost Optimization](cost-optimization.md).

Each pillar defines design principles, practical guidance specific to {{brand}}'s OpenStack-based platform, and a self-assessment checklist you can use during design reviews.

The framework is deployment-model agnostic:
the same principles apply whether you run on {{brand_public}}, {{brand_compliant}}, or {{company}} Private Cloud, though the specific controls available differ between them (see the deployment model note below).

## Who this is for

- Solution architects and platform teams designing new workloads on {{brand}}.
- Engineering and operations teams who want a checklist-driven way to review existing workloads.
- Compliance, security and procurement stakeholders evaluating whether a workload meets internal or regulatory requirements before go-live.

## How to use this framework

1. Define the workload.
   Scope the review to one workload or system at a time — not your entire estate.
2. Work through each pillar.
   Use the design principles as guidance and the checklist as a gap-finder.
3. Prioritize findings.
   Not every gap needs fixing immediately — weigh risk, cost, and effort.
4. Create an improvement backlog.
   Track remediation items alongside your normal engineering backlog.
5. Repeat regularly.
   Re-run the review after major changes, and at minimum quarterly for production workloads.

## A note on deployment models

{{company}} offers three IaaS deployment models built on the same open-source, OpenStack foundation:
Public Cloud (flexible, standard-tools environment for developers and SMBs), Compliant Cloud (enhanced security configuration, availability zones, and controls for regulated and mission-critical workloads), and Private Cloud (a dedicated, turnkey OpenStack environment).

Many of the practices below — particularly under Security & Digital Sovereignty and Reliability — are strongest on Compliant Cloud or Private Cloud.
Choosing the right model is a foundational decision that should be made early, based on the workload's regulatory, security, and availability requirements, since it shapes which controls and practices in this framework are available to you from the outset.

## A note on {{brand}} Launch Pad

[Launch Pad](../../howto/getting-started/launch-pad/index.md) is a lightweight bootstrap utility, not a landing zone in the enterprise sense.

Run via OpenStack Heat, Ansible, or OpenTofu, it creates:

- an SSH keypair,
- a virtual router connected to an internal IPv4/IPv6 network with public internet access, and
- a Pad Ramp jump host that you can restrict to a specific source IP or network.

That's a genuinely useful starting point for reaching a brand-new environment.
Launch Pad does not create projects, quotas, IAM boundaries, a security baseline beyond the jump host's own access rule, logging, or multi-environment structure.
Treat every other practice in this framework, including basic hygiene like project segmentation and security groups, as work that still needs to happen after Launch Pad hands off.

