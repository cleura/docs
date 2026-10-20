---
description: Using flavors, you define a server’s performance characteristics and supported features.
---
# Flavors

Any server instance running in {{brand}} has a **flavor**, which defines the number of virtual CPU cores, the amount of virtual RAM, and other performance-related factors.

{{page.meta.description}}

## Naming convention

Flavor names in {{brand}} follow a convention, which can be summarized as `X.YcZgb`:

* `X` stands for a lowercase letter identifying the [compute tier](#compute-tiers), with `b` representing the general-purpose tier.
   It is always followed by a full-stop (`.`).
* `Y` stands for the number of virtual CPU cores.
   This number is always followed by the letter `c`.
* `Z` stands for the allocated amount of virtual RAM, in [gibibytes](https://en.wikipedia.org/wiki/Gigabyte#Base_2_(binary)).
   This number is always followed by the string `gb`.

For example, the flavor named `b.4c32gb` would be used for a general-purpose compute instance with 4 cores and 32 GiB RAM.


## Compute tiers

{{brand}} defines the following compute tiers:

* `b`: General purpose.
  This is the default compute tier.
  Instances launched with matching flavors use highly available network-attached storage.
  This makes them flexible to migrate within the {{brand}} infrastructure, without interruption.
  Some [limitations](../../../howto/openstack/cinder/encrypted-volumes.md#block-device-encryption-caveats) apply to instances with attached [encrypted volumes](../../../howto/openstack/cinder/encrypted-volumes.md).
* `s`: High-performance local storage.
  Instances launched with matching flavors use local, directly-attached storage.
  This generally provides higher throughput and lower latency for I/O intensive applications, but instances launched with these flavors must configure their own high availability and data replication.
* `c`: Physical CPUs.
  Instances launched with matching flavors will be assigned physical CPU cores, rather then virtual ones.
  These flavors are recommended for CPU-intensive workloads, or when there is a requirement for guaranteed CPU resources.

Some tiers are only available in select {{brand}} regions.
For details on tier availability, see the [Feature support matrix](../features/index.md).

The general-purpose tier is always available to all {{brand}} customers.
For access to other tiers, contact our [{{support}}](https://{{support_domain}}/servicedesk).
