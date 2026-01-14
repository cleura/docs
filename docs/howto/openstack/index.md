# OpenStack

{{brand}} is built around the [OpenStack](https://www.openstack.org/) Infrastructure-as-a-Service (IaaS) platform.

Thus, most {{brand}} components correspond to OpenStack services:

* [Compute (Nova)](nova/index.md) is the service you use for launching and managing virtual servers.
* [Networking (Neutron)](neutron/index.md) allows you to manage virtual networks and connectivity.
* [Load balancing (Octavia)](octavia/index.md) is for managing load balancers supporting the TCP and HTTP(S) protocols.
* [Block storage (Cinder)](cinder/index.md) provides persistent block storage for virtual servers.
* [Image management (Glance)](glance/index.md) provides ready-to-launch, preconfigured operating system images for virtual servers.
* [Identity (Keystone)](keystone/index.md) is for managing credentials and authentication.
* [Secret storage (Barbican)](barbican/index.md) provides key and secret management.

{{brand}} does not natively implement [OpenStack Swift](https://docs.openstack.org/swift/), but it does support [object storage](../object-storage/index.md) that is compatible with the [Swift API](../object-storage/swift/index.md).
