---
description: Changing the type of a volume ("retyping") is an offline operation that requires detaching the volume from its server, and setting its new type.
---
# Changing a volume's type

You may occasionally need to change a volume's type.

{{page.meta.description}}
The process of volume retyping incurs a short downtime.
Depending on the kind of application the server hosts, when you need to retype volumes, you should plan ahead well in advance.

## Prerequisites

To retype volumes, you must use the OpenStack CLI, so make sure you [have it enabled](../../getting-started/enable-openstack-cli.md).

If you are about to retype a large volume, or one that holds data associated with a critical service, you may want an estimate of how long the retype operation will take.
In that case, please file a support request with our [{{support}}](https://{{support_domain}}/servicedesk).

## Checking the volume's state

Assume you have the `testvol` volume, which is currently attached to the `testsrv` server:

```console
$ openstack volume list --long
+--------------+---------+--------+------+-------------+----------+--------------+------------+
| ID           | Name    | Status | Size | Type        | Bootable | Attached to  | Properties |
+--------------+---------+--------+------+-------------+----------+--------------+------------+
| 0e6f15f8-    | testvol | in-use |   75 | cbs-premium | false    | Attached to  |            |
| 8105-4043-   |         |        |      |             |          | testsrv on   |            |
| beb1-        |         |        |      |             |          | /dev/vdb     |            |
| 43f2364460f2 |         |        |      |             |          |              |            |
+--------------+---------+--------+------+-------------+----------+--------------+------------+
```

In this example, the volume status is `in-use`, meaning it is currently attached to a server, and the volume type is `cbs-premium`.

## Detaching the volume

You cannot retype a volume while it is attached to a server.
You must thus detach it first.
It is safest to do this while the server is shut off:

```console
$ openstack server stop testsrv

$ openstack server list -c Name -c Status
+---------+---------+
| Name    | Status  |
+---------+---------+
| testsrv | SHUTOFF |
+---------+---------+
```

Once your server is in the `SHUTOFF` state, you can safely proceed to detach the volume.
This will change the volume status from `in-use` to `available`:

```console
$ openstack server remove volume testsrv testvol

$ openstack volume list
+--------------------------------------+---------+-----------+------+-------------+
| ID                                   | Name    | Status    | Size | Attached to |
+--------------------------------------+---------+-----------+------+-------------+
| 0e6f15f8-8105-4043-beb1-43f2364460f2 | testvol | available |   75 |             |
+--------------------------------------+---------+-----------+------+-------------+
```

## Retyping the volume

With the volume safely detached, you can now change its volume type.
If you were to change the volume type from `cbs-premium` to `cbs-standard`, you would proceed as follows:

```console
$ openstack volume set --type cbs-standard --migration-policy on-demand testvol

$ openstack volume list --long
+-------------+---------+-----------+------+-------------+----------+-------------+------------+
| ID          | Name    | Status    | Size | Type        | Bootable | Attached to | Properties |
+-------------+---------+-----------+------+-------------+----------+-------------+------------+
| 0e6f15f8-   | testvol | available |   75 | cbs-        | false    |             |            |
| 8105-4043-  |         |           |      | standard    |          |             |            |
| beb1-       |         |           |      |             |          |             |            |
| 43f2364460f |         |           |      |             |          |             |            |
| 2           |         |           |      |             |          |             |            |
+-------------+---------+-----------+------+-------------+----------+-------------+------------+
```

Note that the volume status changes from `available` to `retyping`:
this status change kicks off the actual data migration, which might take a significant amount of time.

!!! warning "Retyping and encryption"
    You **cannot** use retyping to convert an [encrypted volume](encrypted-volumes.md) to an unencrypted one, or vice versa.
    Instead, you will need to move your data:

    * Attach a new volume to a running VM that **also** has the original volume attached,
    * copy data over to the new volume.

## Re-attaching the volume

If you attempt to re-attach the volume while it is still retyping, you will receive an error:

```console
$ openstack server add volume testsrv testvol
BadRequestException: 400: Client Error for url: https://compute.{{api_region|lower}}.{{api_domain}}/v2.1/servers/b6a26b0e-f911-4ea2-8e45-51f16442da03/os-volume_attachments, Invalid input received: Invalid volume: Volume e233e7f3-f33b-4d7a-8f5b-785b34f670bf status must be available or downloading to reserve, but the current status is retyping. (HTTP 400) (Request-ID: req-36c4f2e5-ef2f-4ff4-b912-0baed2594f4d)
```

You must now wait until the volume status changes back from `retyping` to `available`.
One way to do this is with a bash `until` loop:

```bash
until [ `openstack volume show -f value -c status testvol` = "available" ]; do
  sleep 5
done
```

Once the volume has returned to the `available` status, you can re-attach it to the server:

```console
$ openstack server add volume testsrv testvol
+-----------------------+--------------------------------------+
| Field                 | Value                                |
+-----------------------+--------------------------------------+
| ID                    | 0e6f15f8-8105-4043-beb1-43f2364460f2 |
| Server ID             | 42049bba-3a48-4bc3-9940-bcaca120ec74 |
| Volume ID             | 0e6f15f8-8105-4043-beb1-43f2364460f2 |
| Device                | /dev/vdb                             |
| Tag                   | None                                 |
| Delete On Termination | False                                |
+-----------------------+--------------------------------------+
```

Finally, start the server:

```console
$ openstack server start testsrv

$ openstack server list -c Name -c Status
+---------+--------+
| Name    | Status |
+---------+--------+
| testsrv | ACTIVE |
+---------+--------+
```
