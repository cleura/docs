# Public Cloud

> :material-check: Feature is in production and fully supported
>
> :material-timer-sand: Feature is in deployment, not yet supported
>
> :material-logout: Feature is deprecated, being phased out
>
> :material-close: Feature is not available

## Virtualization
|                                                              | Kna1                  | Sto2                  | Fra1             |
| -------------                                                | ----------------      | --------------------- | ---------------- |
| [Physical CPUs](../flavors/index.md#compute-tiers)           | :material-close:      | :material-timer-sand: | :material-close: |


## Block storage
|                                                                        | Kna1             | Sto2             | Fra1             |
| ------------------------------                                         | ---------------- | ---------------- | ---------------- |
| Highly available storage                                               | :material-check: | :material-check: | :material-check: |
| [High-performance local storage](../flavors/index.md#compute-tiers)    | :material-check: | :material-check: | :material-check: |
| [Volume encryption](../../howto/openstack/cinder/encrypted-volumes.md) | :material-check: | :material-check: | :material-check: |


## Object storage
|                                                                | Kna1             | Sto2             | Fra1             |
| ------------------------------                                 | ---------------- | ---------------- | ---------------- |
| S3 API                                                         | :material-check: | :material-check: | :material-check: |
| S3 [SSE-C](../../howto/object-storage/s3/sse-c.md)             | :material-check: | :material-check: | :material-check: |
| S3 [object lock](../../howto/object-storage/s3/object-lock.md) | :material-check: | :material-check: | :material-check: |
| Swift API                                                      | :material-check: | :material-check: | :material-check: |


## Networking (Layer 2/3)
|                      | Kna1             | Sto2             | Fra1             |
| -------------------- | ---------------- | ---------------- | ---------------- |
| IPv4 (with NAT)      | :material-check: | :material-check: | :material-check: |
| IPv6                 | :material-check: | :material-check: | :material-check: |
| VPN (IPsec with PSK) | :material-check: | :material-check: | :material-check: |


## Load Balancers
|                                                                                                                    | Kna1             | Sto2             | Fra1             |
| --------------------------------------------------------------------                                               | ---------------- | ---------------- | ---------------- |
| Transport layer (TCP/UDP)                                                                                          | :material-check: | :material-check: | :material-check: |
| Application layer (HTTP)                                                                                           | :material-check: | :material-check: | :material-check: |
| Application layer ([HTTPS, with secrets management for TLS certificates](../../howto/openstack/octavia/tls-lb.md)) | :material-check: | :material-check: | :material-check: |
| [Metrics endpoint](../../howto/openstack/octavia/metrics.md)                                                       | :material-check: | :material-check: | :material-check: |


## DNS

|                      | Kna1                  | Sto2                  | Fra1                  |
| -------------------- | ----------------      | ----------------      | ----------------      |
| Zones                | :material-timer-sand: | :material-timer-sand: | :material-timer-sand: |
| A records            | :material-timer-sand: | :material-timer-sand: | :material-timer-sand: |
| AAAA records         | :material-timer-sand: | :material-timer-sand: | :material-timer-sand: |
| PTR records          | :material-close:      | :material-close:      | :material-close:      |
| SRV records          | :material-timer-sand: | :material-timer-sand: | :material-timer-sand: |
| TXT records          | :material-timer-sand: | :material-timer-sand: | :material-timer-sand: |


## Kubernetes management
|                            | Kna1             | Sto2             | Fra1             |
| -----------------          | ---------------- | ---------------- | ---------------- |
| {{k8s_management_service}} | :material-check: | :material-check: | :material-check: |
