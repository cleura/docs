# Compliant Cloud


> :material-check: Feature is in production and fully supported
>
> :material-timer-sand: Feature is in deployment, not yet supported
>
> :material-logout: Feature is deprecated, being phased out
>
> :material-close: Feature is not available


The new {{api_region}} region, also known as Compliant Cloud v2, implements certain technologies that significantly differentiate it from other {{brand}} regions.


## Availability zones

The {{api_region}} region has three (3) availability zones (AZs) connected by a stretched Layer 2 network.
Resources are allocated randomly between the three whenever an AZ is **not** explicitly specified.
Each AZ has its own block storage, and no live migration between AZs is possible.


## Block storage

|                                                                 | Sto1HS           | Sto2HS           | Sto-Com          |
| ------------------------------                                  | ---------------- | ---------------- | ---------------- |
| Highly available storage                                        | :material-check: | :material-check: | :material-check: |
| [High-performance local storage](../flavors/index.md#compute-tiers)  | :material-check: | :material-check: | :material-check: |
| [Volume encryption](../../howto/openstack/cinder/encrypted-volumes.md) | :material-check: | :material-check: | :material-check: |

Volumes in {{api_region}} are provided by Ceph.
Cloud servers with ephemeral storage have low-latency disks (LLDs) that are local to the corresponding hypervisor.

## Object storage

|                                                         | Sto1HS           | Sto2HS           | Sto-Com          |
| ------------------------------                          | ---------------- | ---------------- | ---------------- |
| S3 API                                                  | :material-check: | :material-check: | :material-check: |
| S3 [SSE-C](../../howto/object-storage/s3/sse-c.md)             | :material-check: | :material-check: | :material-check: |
| S3 [object lock](../../howto/object-storage/s3/object-lock.md) | :material-check: | :material-check: | :material-check: |
| Swift API                                               | :material-check: | :material-check: | :material-check: |

The Object Store in {{api_region}} is configured so that data written in a container or a bucket are automatically stored and synchronized between all three availability zones.
Users may define policies so that a specific bucket is located in a single AZ.

> Contrary to other regions, where images live on Ceph RBD pools, images in {{api_region}} reside in an object store.
> As a result, new VMs in {{api_region}} may take longer to initialize.


## Networking (Layer 2/3)

|                      | Sto1HS           | Sto2HS           | Sto-Com          |
| -------------------- | ---------------- | ---------------- | ---------------- |
| IPv4 (with NAT)      | :material-check: | :material-check: | :material-check: |
| IPv6                 | :material-timer-sand: | :material-close: | :material-check: |
| VPN (IPsec with PSK) | :material-check: | :material-check: | :material-close: |

In {{api_region}}, Quality of Service in Neutron is configured for tenant networks, router gateways, and floating IPs:

| Port type                   | Bandwidth limit |
| --------------------------- | --------------- |
| VM ports (private networks) | 2 Gbps          |
| Floating IPs                | 1 Gbps          |
| Router Gateways             | 1 Gbps          |

## Load Balancers

|                                                                                                             | Sto1HS           | Sto2HS           | Sto-Com          |
| --------------------------------------------------------------------                                        | ---------------- | ---------------- | ---------------- |
| Transport layer (TCP/UDP)                                                                                   | :material-check: | :material-check: | :material-close: |
| Application layer (HTTP)                                                                                    | :material-check: | :material-check: | :material-check: |
| Application layer ([HTTPS, with secrets management for TLS certificates](../../howto/openstack/octavia/tls-lb.md)) | :material-check: | :material-check: | :material-check: |
| [Metrics endpoint](../../howto/openstack/octavia/metrics.md)                                                | :material-check: | :material-check: | :material-check: |


## DNS

|                      | Sto1HS                | Sto2HS                | Sto-Com               |
| -------------------- | ----------------      | ----------------      | ----------------      |
| Zones                | :material-timer-sand: | :material-timer-sand: | :material-timer-sand: |
| A records            | :material-timer-sand: | :material-timer-sand: | :material-timer-sand: |
| AAAA records         | :material-timer-sand: | :material-timer-sand: | :material-timer-sand: |
| PTR records          | :material-close:      | :material-close:      | :material-close:      |
| SRV records          | :material-timer-sand: | :material-timer-sand: | :material-timer-sand: |
| TXT records          | :material-timer-sand: | :material-timer-sand: | :material-timer-sand: |


## Kubernetes management
|                            | Sto1HS           | Sto2HS           | Sto-Com          |
| -----------------          | ---------------- | ---------------- | ---------------- |
| {{k8s_management_service}} | :material-check: | :material-check: | :material-check: |
