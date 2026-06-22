# Using Barbican for secret storage

**[Barbican](https://docs.openstack.org/barbican/latest/)** is OpenStack's secret storage facility.
In {{brand}}, Barbican is supported for the following purposes:

* [Generic secret storage](generic-secret.md),
* [encryption for persistent volumes](../cinder/encrypted-volumes.md),
* [certificate storage for HTTPS load balancers](../octavia/tls-lb.md).

To manage secrets with Barbican, you will need the `openstack` command line interface (CLI), and its Barbican plugin.
You can install them both with the following commands:

```bash
pip install cleura-openstackclient
```

On Debian/Ubuntu platforms, you may also install these utilities via their APT packages:

```bash
apt install python3-openstackclient python3-barbicanclient
```
