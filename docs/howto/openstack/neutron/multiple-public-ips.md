# Assigning multiple public (floating) IPs to a server

In {{brand}}, we do not pass external networks to the compute nodes.
This means you, as a user, cannot directly attach a server to the public network.

To connect to the public network (with IPv4), you need to use floating IPs.
A floating IP is created in the public subnet and is mapped to the specific network port.
All traffic comes through a virtual router.

In some scenarios, you might need more than one public IP assigned to a server.
But in the case of 1-to-1 NAT (which is how the floating IP is implemented under the hood), you can not assign more than one external IP to the internal one.
Adding a new port to the VM is not an option either;
that would cause asymmetric routing, as replies would go through the first interface with a default route.

Instead, you must first configure an additional *private* (“fixed”) IP address for your port, then associate a public (“floating”) IP address to map to it.


## Add an extra IP to the port

Assume you already have a network port inside your private network:

```console
$ openstack port show 51dae637-ad79-4ba9-9e41-78e5e0f3332c -c fixed_ips
+-----------+--------------------------------------------------------------------------+
| Field     | Value                                                                    |
+-----------+--------------------------------------------------------------------------+
| fixed_ips | ip_address='10.2.0.58', subnet_id='5efeae9f-06b8-41a5-987f-085e8c7113a6' |
+-----------+--------------------------------------------------------------------------+
```

And you also have a floating IP associated with it:

```console
$ openstack floating ip list -c ID -c "Floating IP Address" -c "Fixed IP Address" -c Port
+--------------------------------------+---------------------+------------------+--------------------------------------+
| ID                                   | Floating IP Address | Fixed IP Address | Port                                 |
+--------------------------------------+---------------------+------------------+--------------------------------------+
| 989f8a96-4ab4-4190-83e4-25b71d309ea9 | 192.0.2.169         | 10.2.0.58        | 51dae637-ad79-4ba9-9e41-78e5e0f3332c |
| c45a5eaf-2f3a-4679-89fe-266a5cbe840a | 198.51.100.12       | None             | None                                 |
+--------------------------------------+---------------------+------------------+--------------------------------------+
```

Then what you need to do is add an extra IP address to your existing port:

```bash
openstack port set --fixed-ip subnet=5efeae9f-06b8-41a5-987f-085e8c7113a6 51dae637-ad79-4ba9-9e41-78e5e0f3332c
```

You can then confirm that the port does have two entries in its `fixed_ips` list:

```console
$ openstack port show 51dae637-ad79-4ba9-9e41-78e5e0f3332c -c fixed_ips
+-----------+---------------------------------------------------------------------------+
| Field     | Value                                                                     |
+-----------+---------------------------------------------------------------------------+
| fixed_ips | ip_address='10.2.0.228', subnet_id='5efeae9f-06b8-41a5-987f-085e8c7113a6' |
|           | ip_address='10.2.0.58', subnet_id='5efeae9f-06b8-41a5-987f-085e8c7113a6'  |
+-----------+---------------------------------------------------------------------------+
```

> Don't forget to configure the new IP as an alias on the interface inside your VM!

When you have an IP address on your port that is not yet assigned to any floating IP, you can assign it to the new floating IP.
Proceed with:

```bash
openstack floating ip set c45a5eaf-2f3a-4679-89fe-266a5cbe840a \
  --port 51dae637-ad79-4ba9-9e41-78e5e0f3332c \
  --fixed-ip-address 10.2.0.228
```

Then, list the floating (public) IP addresses, together with their fixed (private) counterparts:


```console
$ openstack floating ip list -c ID -c "Floating IP Address" -c "Fixed IP Address" -c Port
+--------------------------------------+---------------------+------------------+--------------------------------------+
| ID                                   | Floating IP Address | Fixed IP Address | Port                                 |
+--------------------------------------+---------------------+------------------+--------------------------------------+
| 989f8a96-4ab4-4190-83e4-25b71d309ea9 | 192.0.2.169         | 10.2.0.58        | 51dae637-ad79-4ba9-9e41-78e5e0f3332c |
| c45a5eaf-2f3a-4679-89fe-266a5cbe840a | 198.51.100.12       | 10.2.0.228       | 51dae637-ad79-4ba9-9e41-78e5e0f3332c |
+--------------------------------------+---------------------+------------------+--------------------------------------+
```

Your server is now accessible through two different public IP addresses.
