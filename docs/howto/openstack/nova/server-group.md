---
description: Server groups let you group servers by policy.
---
# Using server groups

In {{brand}}, you can use server groups to control the scheduling of a group of servers.

## Prerequisites

To use server groups, you must use the OpenStack CLI.
Make sure you have [enabled it](../../getting-started/enable-openstack-cli.md).

## Policies

A server group can have one of four different policies: affinity, soft-affinity, anti-affinity, or soft-anti-affinity.

### Affinity

A server group with the `affinity` policy ensures that all servers in the group are **always** placed on the same physical compute node.

### Soft affinity

A policy of `soft-affinity` will **try to** make sure that all the servers in that group are placed on the same physical compute node, but ultimately will allow it if otherwise not possible.

### Anti-affinity

A server group with the `anti-affinity` policy will ensure that the servers in that group are **never** placed on the same physical compute node.

### Soft anti-affinity

A policy of `soft-anti-affinity` will **try to** make sure that all the servers in that group are not placed on the same physical compute node, but ultimately will allow it if otherwise not possible.

## Creating server groups

To create a server group, use the following command:

```bash
openstack server group create \
  --policy [affinity|soft-affinity|anti-affinity|soft-anti-affinity] \
  <server_group_name>
```

With an `anti-affinity` or `soft-anti-affinity` policy, you may also configure how many servers you want to allow on the same physical compute node.
To do this, use the option `--rule max_server_per_host=<number>`, where `<number>` is the amount of servers to allow on the same physical compute node.


## Creating servers using server groups

To apply a server group policy, specify the group as a *scheduling hint* when creating a server.
To do that, use the `--hint` parameter in the following command:

```bash
openstack server create --hint group=<server_group_id> [...] <server_name>
```

If you subsequently launch more servers referencing the same server group, {{brand}} concentrates or distributes them according to the server group's policy.

## Troubleshooting common issues

If you keep creating servers within a server group with an `anti-affinity` policy, you will eventually exceed the region's total number of physical compute nodes.
The command will still succeed, but the server will subsequently fail to be scheduled to a compute node.
Instead, it will assume the `ERROR` status with the following `fault` message:
_No valid host was found.
There are not enough hosts available._

```console
$ openstack server show -c fault -c status <server_id>
+--------+--------------------------------------------------+
| Field  | Value                                            |
+--------+--------------------------------------------------+
| fault  | {'code': 500, 'created': '2022-12-23T11:21:33Z', |
|        | 'message': 'No valid host was found.             |
|        | There are not enough hosts available.'}          |
| status | ERROR                                            |
+--------+--------------------------------------------------+
```

This is normal:
{{brand}} cannot schedule the server on a different physical compute node because each node already has a server from the group.
The same scheduling error occurs, and a "fault" message appears, when you use a server group with an `affinity` policy and create more servers than a physical compute node can host.

However, with a soft affinity policy, such as `soft-affinity` or `soft-anti-affinity`, the scheduler can break the server group's policy if it can't uphold it.
This means you may want to verify whether your servers are on the same or different physical compute nodes by checking the _hostId_ value of your servers.

```console
$ openstack server show -c hostId <server_id>
+--------+----------------------------------------------------------+
| hostId | 8fae028139411e9e125d5f39895bef79f916aefce6003a7888de105d |
+--------+----------------------------------------------------------+
```

`hostId` is a unique identifier for each physical compute node.
By comparing this value across your servers, you can confirm whether your server group policy is being upheld.

> It's not possible to compare `hostId` between different projects because the values are unique for each project.
