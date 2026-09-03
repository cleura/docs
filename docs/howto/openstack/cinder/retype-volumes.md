---
description: Changing the type of a volume ("retyping") is an offline operation that requires detaching the volume from its server, and setting its new type.
---
# Changing a volume's type

You may occasionally need to change a volume's type.

{{page.meta.description}}
The resulting downtime may be quite substantial, particularly for large volumes.
As such, when you need to retype volumes, you should plan ahead well in advance.

## Prerequisites

To retype volumes, you must use the OpenStack CLI, so make sure you [have it enabled](../../getting-started/enable-openstack-cli.md).

If you are about to retype a large volume, or one that holds data associated with a critical service, you may want an estimate of how long the retype operation will take.
In that case, please file a support request with our [{{support}}](https://{{support_domain}}/servicedesk).

## Checking the volume's state

Assume you have the `testvol` volume, which is currently attached to the `testsrv` server:

```console
$ openstack volume list --long
+----------------+---------+--------+------+---------+----------+----------------+------------+
| ID             | Name    | Status | Size | Type    | Bootable | Attached to    | Properties |
+----------------+---------+--------+------+---------+----------+----------------+------------+
| e233e7f3-f33b- | testvol | in-use |   50 | cbs     | false    | Attached to    |            |
| 4d7a-8f5b-785b |         |        |      |         |          | testsrv on     |            |
| 34f670bf       |         |        |      |         |          | /dev/vdb       |            |
+----------------+---------+--------+------+---------+----------+----------------+------------+
```

In this example, the volume status is `in-use`, meaning it is currently attached to a server, and the volume type is `cbs`.

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
| e233e7f3-f33b-4d7a-8f5b-785b34f670bf | testvol | available |   50 |             |
+--------------------------------------+---------+-----------+------+-------------+
```

## Retyping the volume

With the volume safely detached, you can now change its volume type.
If you were to change the volume type from `cbs` to `<new-vol-type>`, you would proceed as follows:

```console
$ openstack volume set --type <new-vol-type> --retype-policy on-demand testvol

$ openstack volume list --long
+---------------+---------+----------+------+---------+----------+-------------+------------+
| ID            | Name    | Status   | Size | Type    | Bootable | Attached to | Properties |
+---------------+---------+----------+------+---------+----------+-------------+------------+
| e233e7f3-f33b | testvol | retyping |   50 | cbs     | false    |             |            |
| -4d7a-8f5b-78 |         |          |      |         |          |             |            |
| 5b34f670bf    |         |          |      |         |          |             |            |
+---------------+---------+----------+------+---------+----------+-------------+------------+
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
BadRequestException: 400: Client Error for url: https://{{api_region|lower}}.{{api_domain}}:8774/v2.1/servers/b6a26b0e-f911-4ea2-8e45-51f16442da03/os-volume_attachments, Invalid input received: Invalid volume: Volume e233e7f3-f33b-4d7a-8f5b-785b34f670bf status must be available or downloading to reserve, but the current status is retyping. (HTTP 400) (Request-ID: req-36c4f2e5-ef2f-4ff4-b912-0baed2594f4d)
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
| ID                    | d2a22868-a133-40a1-b1a6-0cbae3feaf8d |
| Server ID             | 23a391f7-57ba-4c7f-bdd1-d1b89d6e39b2 |
| Volume ID             | e233e7f3-f33b-4d7a-8f5b-785b34f670bf |
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
