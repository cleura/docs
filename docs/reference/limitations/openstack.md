# OpenStack service limitations


## OpenStack users, groups, and roles

### Administrative privileges

No OpenStack user that you create while [enabling the OpenStack CLI](../../howto/getting-started/enable-openstack-cli.md) ever gets privileges exceeding administrative rights bound to a project.

This means that you cannot use an OpenStack user to *create* a new project.
You must do so via the {{gui}}, or the [{{rest_api}}](../api/cc/index.md).

It also means that you cannot use the following `openstack` CLI commands; they all return `Unauthorized` (HTTP 403):

* `openstack user [create|delete|list|set]`.
  > You can use `openstack user show` and `openstack user password set`, but only for your own user account.
* `openstack group <subcommand>`
* `openstack role <subcommand>`
* `openstack project <subcommand>` (except `list`).
  > You can use `openstack project list`, but this will only list the project(s) that your user account has access to.
* `openstack domain <subcommand>`

## Cinder

### Volume backup service

{{brand}} does not support the OpenStack volume backup service (`cinder-backup`).

For automated, scheduled volume *snapshots,* consider configuring your servers for [Disaster Recovery (DR)](../../background/disaster-recovery.md) via the {{gui}}.

## Glance

### Image imports

The web-download import method, which allows importing images from remote URLs, is not supported.
Although we recommend you use one of our [supported images](../images/index.md), it is possible to [create or upload a custom image](../../howto/openstack/glance/custom.md) using the `openstack` CLI.

## Nova

### Nested virtualization

Running nested virtualization is only supported for Nova instances ([servers](../../howto/openstack/nova/new-server.md)) running Linux.
The server must run a [Linux kernel](https://www.kernel.org/) of version 5.0 or later, and [QEMU/KVM](https://www.qemu.org/) 4.1 or later.

This means that you can run nested virtualization on servers booted from a CentOS 9 (or later), Ubuntu 20.04 (or later), or Debian 11 (or later) base image.

Furthermore, you must ensure that the Nova server [passes the `pcid` CPU feature flag](https://qemu-project.gitlab.io/qemu/system/qemu-cpu-models.html#important-cpu-features-for-intel-x86-hosts) to nested guests.

### Maximum attached volumes per server

A Nova [server](../../howto/openstack/nova/new-server.md) in {{brand}} can concurrently attach a maximum of 25 persistent volumes.
This is a limitation of the `virtio-blk` storage driver that ships as part of the guest operating system's kernel.

## Neutron

### Dynamic routing

Neutron in {{brand}} does not support dynamic routing protocols in a customer-accessible manner.
We currently do not expose the ability to configure [BGP](https://en.wikipedia.org/wiki/Border_Gateway_Protocol) speakers or peers.

While {{brand}} does use [BGP dynamic routing](https://docs.openstack.org/neutron/latest/admin/config-bgp-dynamic-routing.html) *internally,* our Neutron configuration restricts the ability to use these features to administrative accounts only.

## Octavia

### Dual-stack support

A single load balancer managed by OpenStack Octavia can support IPv4 *or* IPv6, but not both.
To expose a service via IPv4 *and* IPv6, you must set up two separate load balancers pointing to the same backend.

## Designate

### PTR Records

The [OpenStack Designate](../../howto/openstack/designate/index.md) DNS-as-a-service (DNSaaS) facility in {{brand}} currently does not support managing [PTR records](https://en.wikipedia.org/wiki/PTR_record).

## Manila

The [OpenStack Manila](https://docs.openstack.org/manila/) filesystem-as-a-service (FSaaS) facility is currently not available in {{brand}}.
If you require multiple servers to be able to access the same files, [create a server](../../howto/openstack/nova/new-server.md) that exposes an internal NFS or CIFS service, backed by a Cinder volume.

## Magnum

The [OpenStack Magnum](https://docs.openstack.org/magnum/) container orchestration service facility, previously available in {{brand}}, is no longer supported.

To manage Kubernetes clusters, you can use [{{brand_container_orchestration}}](../../howto/kubernetes/gardener/index.md) instead.
