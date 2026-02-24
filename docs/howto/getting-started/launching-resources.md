---
description: An action-list on launching your first resources in Cleura Cloud
---

# Launching your first resources

{{brand}} is built around the [OpenStack](https://www.openstack.org/) Infrastructure-as-a-Service (IaaS) platform.

OpenStack enables organizations build and manage their own infrastructure in the cloud.
For that, it offers a readily available array of services such as Nova (compute), Neutron (networking), and Designate (DNS).

As a new user of {{brand}}, we suggest you start building by taking the following steps.

* [Getting started with networks, subnets, and routers](#getting-started-with-networks-subnets-and-routers)
* [Creating a security group](#creating-a-security-group)
* [Launching a Bastion host](#launching-a-bastion-host)
* [Connecting via SSH](#connecting-via-ssh)

Keep in mind that the above tasks can be fully automated by employing either the [OpenStack Heat](https://docs.openstack.org/heat/latest/) orchestration service, the [OpenTofu](https://opentofu.org/) infrastructure-as-code tool, or the [Ansible](https://docs.ansible.com/) automation platform.

Additionally, take your time to get acquainted with load balancers, DNS, and Kubernetes in {{brand}}:

* [Creating a load balancer](#creating-a-load-balancer)
* [Creating and managing a DNS zone](#creating-and-managing-a-dns-zone)
* [Launching a Gardener Kubernetes cluster](#launching-a-gardener-kubernetes-cluster)

## Getting started with networks, subnets, and routers

The Neutron service in OpenStack is responsible for creating networks.

You can think of these networks as software constructs that enable connectivity among routers, load balancers, virtual machines, and other software-defined entities.

Even though a Neutron network does define a logical topology, it knows nothing about IP addresses;
for these, you need at least one subnet in the network.
That's because each subnet has an IP address range and may be connected to a router.

Then, depending on how this router is configured, communication with other subnets or even with the internet is possible.

Go ahead and [create a new network with a subnet, and connect it to a router](../openstack/neutron/new-network.md) who knows how to get packets to and from the internet.

## Creating a security group

In addition to networks, subnets, and routers, the OpenStack Neutron service is also responsible for security groups.
You can liken a security group to a virtual firewall, which you can put in front of one or more virtual machines.
A security group has one or more rules, filtering outgoing (egress) and incoming (ingress) traffic.

A typical setup for a security group is to allow all outgoing traffic, but allow only incoming SSH traffic to port `22/TCP`.
[Follow this guide](../openstack/neutron/create-security-groups.md) and create a new security group configured like the one we just described.

## Launching a Bastion host

By now, you should have a network with a subnet, connected to a virtual router with an internet-facing public interface.
You should also have a security group in place, ready to be used as a firewall for your virtual machines.

OpenStack Nova is the service for creating and managing virtual machines.
To see how you can work with Nova, [create a new virtual machine](../openstack/nova/new-server.md) doubling as a [Bastion host](https://en.wikipedia.org/wiki/Bastion_host).
Do not forget to protect it with the security group you created earlier.

## Connecting via SSH

Your new Bastion host should now be up and running.
Due to the security group in front of it, the host should be accepting incoming SSH connections.

Use the guide for [creating virtual servers](../openstack/nova/new-server.md) to also create a new floating (public) IP address and assign it to the server.
Then, with your SSH client of choice, securely connect to your Bastion host via SSH.

## Creating a load balancer

The OpenStack Octavia service is responsible for spinning up load balancers.
Whenever you want to deploy resilient and highly available services, one of your choices is to put them behind load balancers.
That way, you spread incoming traffic (and workload) across many instances.


Go ahead and follow our guide for deploying a low-level [TCP-based load balancer](../openstack/octavia/lbaas-tcp.md).
Alternatively, see how you can deploy a higher-lever load balancer that uses [Layer 7 redirection](../openstack/octavia/lbaas-l7pol.md).

## Creating and managing a DNS zone

Designate is the OpenStack DNS‑as‑a‑Service component.

Thanks to it, you can programmatically create and manage DNS zones and record sets.
Then, you will have the option to refer to your services or applications by name.

Learn how you can [define a new zone](../openstack/designate/zones.md), and then move on to [creating resource record sets](../openstack/designate/recordsets.md) for it.

## Launching a Gardener Kubernetes cluster

[Gardener](https://gardener.cloud/) is a "Kubernetes‑as‑a‑Service" platform:
instead of provisioning a single Kubernetes cluster, it allows you to manage one or more such clusters from a single place in the {{gui}}.

You can start right away with Gardener by [creating a full-blown Kubernetes cluster](../kubernetes/gardener/create-shoot-cluster.md). Then, go ahead and see how you can manage your new cluster [using the `kubectl` client](../kubernetes/gardener/kubectl.md).
