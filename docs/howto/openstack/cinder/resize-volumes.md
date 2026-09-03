---
description: A server may require additional capacity for a persistent storage volume attached to it. You can expand a volume online while it is attached to a running server.
---
# Resizing a volume

{{page.meta.description}}

## Prerequisites

To expand a volume online (that is, without detaching it from its server), you must use the OpenStack CLI.
Make sure you have [enabled it](../../getting-started/enable-openstack-cli.md).

## Checking the volume's state

Assume you have a volume named `testvol` that is currently attached to a server named `testsrv`:

```console
$ openstack volume list
+-----------------------------------+---------+--------+------+----------------------------------+
| ID                                | Name    | Status | Size | Attached to                      |
+-----------------------------------+---------+--------+------+----------------------------------+
| 357e1022-4156-4383-a49d-729f86e84 | testvol | in-use |    2 | Attached to testsrv on /dev/vdb  |
| 347                               |         |        |      |                                  |
+-----------------------------------+---------+--------+------+----------------------------------+
```

As you can see, this volume's status is `in-use`, meaning it is currently attached to a server, and the volume's size is 2 GiB.

You can also use `openstack server ssh` to verify the current state of the block device.
In this example, the virtual block device `/dev/vdb` contains an XFS file system and is mounted to `/srv`:

```console
$ openstack server ssh testsrv -- -l ubuntu "mount | grep /dev/vdb"
/dev/vdb on /srv type xfs (rw,relatime,attr2,inode64,logbufs=8,logbsize=32k,noquota)
```

## Expanding the volume

You can now change the volume's size (in this example, we'll use a new size of 5 GiB).
Note that in order to be able to do this while the volume is attached to a server, you must invoke the `openstack` command with the `--os-volume-api-version` flag:

```console
$ openstack --os-volume-api-version 3.42 volume set --size 5 testvol

$ openstack volume list 
+-----------------------------------+---------+--------+------+----------------------------------+
| ID                                | Name    | Status | Size | Attached to                      |
+-----------------------------------+---------+--------+------+----------------------------------+
| 357e1022-4156-4383-a49d-729f86e84 | testvol | in-use |    5 | Attached to testsrv on /dev/vdb  |
| 347                               |         |        |      |                                  |
+-----------------------------------+---------+--------+------+----------------------------------+
```

When using [one of the VirtIO storage drivers](https://www.qemu.org/2021/01/19/virtio-blk-scsi-configuration/), the operating system on the server immediately becomes aware of the new device size.
There is no need to rescan the block devices from within the guest operating system.

You can verify this by using the `blockdev` command in a shell session, querying the block device size in bytes:
```console
$ openstack server ssh testsrv -- -l ubuntu "sudo blockdev --getsize64 /dev/vdb"
5368709120
```

## Using the resized volume

Resizing a volume only resizes the block device;
it does not touch any data structures on that block device.
In our example, this means that in order to use the block device's expanded capacity, you must also resize its filesystem:

```console
$ openstack server ssh testsrv -- -l ubuntu "sudo xfs_growfs /dev/vdb"
meta-data=/dev/vdb               isize=512    agcount=4, agsize=131072 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=1        finobt=1, sparse=1, rmapbt=0
         =                       reflink=1
data     =                       bsize=4096   blocks=524288, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0, ftype=1
log      =internal log           bsize=4096   blocks=2560, version=2
         =                       sectsz=512   sunit=0 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
data blocks changed from 524288 to 1310720
```

Once this is complete, you can verify that the filesystem is now available at the desired (expanded) capacity:

```console
$ openstack server ssh testsrv -- -l ubuntu "df -h /srv"
Filesystem      Size  Used Avail Use% Mounted on
/dev/vdb        5.0G   69M  5.0G   2% /srv
```
