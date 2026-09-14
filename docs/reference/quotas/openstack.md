---
description: Resource limits (quotas) for OpenStack resources
---
# OpenStack quotas

Most of the OpenStack resources you create in {{brand}} are subject to quotas.
Once you hit a quota limit, the creation of new resources of that type will fail, until you either reduce your resource utilization or your quota is raised.

{{brand}} applies most quotas on a per-project basis.
Your {{brand}} *account* can manage up to 3 projects.

The following quotas apply in any of your {{brand}} projects by default:

| Quota name             | Value            | Notes                 |
| -------------          | ---------------- | --------------------- |
| `cores`                | 20               | Maximum number of virtual CPU cores allocatable across all servers ("instances"). |
| `floating_ips`         | 50               | Maximum number of public ("floating") IPv4 addresses *allocated* in your project. The limit on floating IP addresses applies regardless of how many are "in use" (that is, *associated* with a port) at any given time. |
| `gigabytes`            | 1000             | Maximum total amount of persistent storage used by all volumes (in GiB). |
| `instances`            | 10               | Maximum number of servers in your project. This limit applies irrespective of whether the server is running, suspended, or shut down. |
| `networks`             | 100              | Maximum number of [networks](../../howto/openstack/neutron/new-network.md). |
| `ports`                | 500              | Maximum total number of ports (virtual network interfaces) across all servers, routers, and load balancers. |
| `ram`                  | 51200            | Maximum total amount of RAM used by all servers (in MiB). |
| `rbac_policies`        | 10               | Maximum number of Role-Based Access Control (RBAC) rules defined for your networks. (Rarely used.) |
| `routers`              | 10               | Maximum number of virtual routers. |
| `secgroup_rules`       | 100              | Maximum number of security group rules (across all [security groups](../../howto/openstack/neutron/create-security-groups.md)). |
| `secgroups`            | 10               | Maximum number of [security groups](../../howto/openstack/neutron/create-security-groups.md). |
| `server_group_members` | 10               | Maximum number of servers allocated to one [server group](../../howto/openstack/nova/server-group.md). |
| `server_groups`        | 10               | Maximum number of [server groups](../../howto/openstack/nova/server-group.md). |
| `snapshots`            | 10               | Maximum number of volume snapshots. |
| `subnets`              | 100              | Maximum number of subnets. Note that subnets are either for IPv4 or IPv6, so in a dual-stack environment every *network* corresponds to two *subnets*. |                                                                                                  |
| `volumes`              | 50               | Maximum total number of persistent volumes. |

There is one other quota that applies per OpenStack API *user*, not per project:

| Quota name             | Value            | Notes                 |
| -------------          | ---------------- | --------------------- |
| `key_pairs`            | 100              | Maximum number of secure shell key pairs. |

## Reviewing your quota

Using the [`openstack` CLI](../../howto/getting-started/enable-openstack-cli.md), you can always review the applicable quota settings for your project with the following command:

```bash
openstack quota show
```

## Requesting a quota increase

If you find that you need to deploy more resources in one project than the default quota allows, or if you need to manage more than 3 projects in your account, please file a support request with our [{{support}}](https://{{support_domain}}/servicedesk).
