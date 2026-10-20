---
description: Reference information on DNS management in Cleura Cloud
---
# DNS servers

## Server regions

By default, each [new zone](../../../howto/openstack/designate/zones.md) you create with Designate comes equipped with two name servers.
The names of those servers, like `cloud-ns1.fra1-pub.cleura.cloud.` and `cloud-ns2.kna1-pub.cleura.cloud.`, are indicative of the regions whose DNS zones and records they handle and *not* of any server's physical location.

The following matrix shows where each name server is located.

| Name server                        | Location  |
| ---------------------------------- | ----------|
| `cloud-ns1.fra1-pub.cleura.cloud.` | Frankfurt |
| `cloud-ns2.fra1-pub.cleura.cloud.` | Stockholm |
| `cloud-ns1.kna1-pub.cleura.cloud.` | Frankfurt |
| `cloud-ns2.kna1-pub.cleura.cloud.` | Stockholm |
| `cloud-ns1.sto2-pub.cleura.cloud.` | Frankfurt |
| `cloud-ns2.sto2-pub.cleura.cloud.` | Stockholm |
| `cloud-ns1.sto1-com.cleura.cloud.` | Frankfurt |
| `cloud-ns2.sto1-com.cleura.cloud.` | Stockholm |
| `cloud-ns1.sto2-com.cleura.cloud.` | Frankfurt |
| `cloud-ns2.sto2-com.cleura.cloud.` | Stockholm |
| `cloud-ns1.sto-com.cleura.cloud.`  | Frankfurt |
| `cloud-ns2.sto-com.cleura.cloud.`  | Stockholm |
