---
description: A walk-through of managing resource record sets with Designate
---
# Managing resource record sets

Assuming you have already [added the `example.com.` zone](zones.md) in Designate, let us now add a type A record (IPv4 address), and also a type AAAA record (IPv6 address) for a new subdomain in that zone.

Suppose the new subdomain is named `nuuk`.
Then, go ahead and create a new *resource record set* (simply *record set* or even *recordset*) by defining a new type A record like so:

```console
$ openstack recordset create --type A --record 198.51.100.200 example.com. nuuk
+-------------+--------------------------------------+
| Field       | Value                                |
+-------------+--------------------------------------+
| action      | CREATE                               |
| created_at  | 2025-08-18T14:20:22.000000           |
| description | None                                 |
| id          | a9596efb-4f1d-42c1-99d5-97cc3d3416d9 |
| name        | nuuk.example.com.                    |
| project_id  | e2548c8b1a474b988027ea93bfc9248c     |
| records     | 198.51.100.200                       |
| status      | PENDING                              |
| ttl         | None                                 |
| type        | A                                    |
| updated_at  | None                                 |
| version     | 1                                    |
| zone_id     | 1e76fc59-4b2c-4782-a852-d4f5bcc460d8 |
| zone_name   | example.com.                         |
+-------------+--------------------------------------+
```

In the same recordset, define a new type AAAA record for `nuuk`:

```console
$ openstack recordset create --type AAAA --record 2001:db8:ffff:ffff:ffff:ffff:ffff:ffff example.com. nuuk
+-------------+----------------------------------------+
| Field       | Value                                  |
+-------------+----------------------------------------+
| action      | CREATE                                 |
| created_at  | 2025-08-18T14:21:51.000000             |
| description | None                                   |
| id          | 6c26a499-09c1-41e5-8aac-221360fe6e67   |
| name        | nuuk.example.com.                      |
| project_id  | e2548c8b1a474b988027ea93bfc9248c       |
| records     | 2001:db8:ffff:ffff:ffff:ffff:ffff:ffff |
| status      | PENDING                                |
| ttl         | None                                   |
| type        | AAAA                                   |
| updated_at  | None                                   |
| version     | 1                                      |
| zone_id     | 1e76fc59-4b2c-4782-a852-d4f5bcc460d8   |
| zone_name   | example.com.                           |
+-------------+----------------------------------------+
```

## Listing recordsets and record types

To list all recordsets and record types in a zone, you first need either the `id` or the `name` of the zone.
Then, you can get information regarding recordsets **and** record types in the zone you are interested in, like so:

```command
$ openstack recordset list example.com.
+--------------------------------------+-------------------+------+-----------------------------------------------------------------------------------+--------+--------+
| id                                   | name              | type | records                                                                           | status | action |
+--------------------------------------+-------------------+------+-----------------------------------------------------------------------------------+--------+--------+
| 67cb2f46-1fa9-4601-9e7c-fbd2ad4fa488 | example.com.      | NS   | cloud-ns1.fra-pub.cleura.cloud.                                                   | ACTIVE | NONE   |
|                                      |                   |      | cloud-ns2.fra-pub.cleura.cloud.                                                   |        |        |
| f30c73f6-c774-4bd2-a3bc-72aebd691834 | example.com.      | SOA  | cloud-ns2.fra-pub.cleura.cloud. admin.example.com. 1755526914 3524 600 86400 3600 | ACTIVE | NONE   |
| a9596efb-4f1d-42c1-99d5-97cc3d3416d9 | nuuk.example.com. | A    | 198.51.100.200                                                                    | ACTIVE | NONE   |
| 6c26a499-09c1-41e5-8aac-221360fe6e67 | nuuk.example.com. | AAAA | 2001:db8:ffff:ffff:ffff:ffff:ffff:ffff                                            | ACTIVE | NONE   |
+--------------------------------------+------------------------+------+------------------------------------------------------------------------------+--------+--------+
```

## Examining specific records

In the example output above, notice the two records, one of type A and one of type AAAA, in the `example.com` zone.
You may get detailed information for any record using the `openstack recordset show <zone-name> <record-name>` command.
But because we have two records with the same `name`, you can always specify one with its `id`.
For instance, to get detailed information about the type AAAA record pointing to the `nuuk` subdomain of `example.com.`, type the following:

```console
$ openstack recordset show example.com. 6c26a499-09c1-41e5-8aac-221360fe6e67
+-------------+----------------------------------------+
| Field       | Value                                  |
+-------------+----------------------------------------+
| action      | NONE                                   |
| created_at  | 2025-08-18T14:21:51.000000             |
| description | None                                   |
| id          | 6c26a499-09c1-41e5-8aac-221360fe6e67   |
| name        | nuuk.example.com.                      |
| project_id  | e2548c8b1a474b988027ea93bfc9248c       |
| records     | 2001:db8:ffff:ffff:ffff:ffff:ffff:ffff |
| status      | ACTIVE                                 |
| ttl         | None                                   |
| type        | AAAA                                   |
| updated_at  | None                                   |
| version     | 1                                      |
| zone_id     | 1e76fc59-4b2c-4782-a852-d4f5bcc460d8   |
| zone_name   | example.com.                           |
+-------------+----------------------------------------+
```

## Querying authoritative name servers

In the output of `openstack recordset list example.com.`, you get the two authoritative DNS servers of `example.com`.
To double-check that `nuuk.example.com` properly resolves to its IPv4 address, use the `dig` utility to ask any of the two authoritative servers:

```console
$ dig @cloud-ns1.fra-pub.cleura.cloud nuuk.example.com

; <<>> DiG 9.18.33 <<>> @cloud-ns1.fra-pub.cleura.cloud nuuk.example.com
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 4427
;; flags: qr aa rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;nuuk.example.com.     IN  A

;; ANSWER SECTION:
nuuk.example.com.  3600    IN  A   198.51.100.200

;; Query time: 130 msec
;; SERVER: 86.107.242.75#53(cloud-ns1.fra-pub.cleura.cloud) (UDP)
;; WHEN: Fri Aug 15 02:09:12 EEST 2025
;; MSG SIZE  rcvd: 66
```

If you would like to get the IPv6 address of `nuuk.example.com`, use the same command with the `-t AAAA` option:

```console
$ dig -t AAAA @cloud-ns1.fra-pub.cleura.cloud nuuk.example.com

; <<>> DiG 9.18.33 <<>> -t AAAA @cloud-ns1.fra-pub.cleura.cloud nuuk.example.com
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 20277
;; flags: qr aa rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;nuuk.example.com.     IN  AAAA

;; ANSWER SECTION:
nuuk.example.com.  3600    IN  AAAA    2001:db8:ffff:ffff:ffff:ffff:ffff:ffff

;; Query time: 125 msec
;; SERVER: 86.107.242.75#53(cloud-ns1.fra-pub.cleura.cloud) (UDP)
;; WHEN: Fri Aug 15 02:10:03 EEST 2025
;; MSG SIZE  rcvd: 78
```

> For extra resilience, the two name servers in any zone reside in different geographic locations.
> You may see the location of a name server [in the Reference section](../../../reference/services/dns/index.md).

## Deleting recordsets

To delete a recordset, you use the `openstack recordset delete` command and specify the name of the zone, together with the `id` of the recordset.

For instance, to delete the recordset that sets a type AAAA record for `nuuk.example.com` in the `example.com.` zone, note the `id` of that specific recordset (`6c26a499-09c1-41e5-8aac-221360fe6e67`), and type the following:

```console
$ openstack recordset delete example.com. 6c26a499-09c1-41e5-8aac-221360fe6e67
+-------------+----------------------------------------+
| Field       | Value                                  |
+-------------+----------------------------------------+
| action      | DELETE                                 |
| created_at  | 2025-08-18T14:21:51.000000             |
| description | None                                   |
| id          | 6c26a499-09c1-41e5-8aac-221360fe6e67   |
| name        | nuuk.example.com.                      |
| project_id  | e2548c8b1a474b988027ea93bfc9248c       |
| records     | 2001:db8:ffff:ffff:ffff:ffff:ffff:ffff |
| status      | PENDING                                |
| ttl         | None                                   |
| type        | AAAA                                   |
| updated_at  | 2025-08-19T15:49:18.000000             |
| version     | 2                                      |
| zone_id     | 1e76fc59-4b2c-4782-a852-d4f5bcc460d8   |
| zone_name   | example.com.                           |
+-------------+----------------------------------------+
```
