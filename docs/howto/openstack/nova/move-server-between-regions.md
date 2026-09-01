---
description: How to transfer a virtual server between Cleura Cloud regions
---
# Moving a server from one region to another

This guide will show you how to move a server to a different region in {{brand}}.

## Prerequisites

In order to move a server from one region to another, you will need

- a correctly installed and configured [OpenStack CLI client](../../getting-started/enable-openstack-cli.md),
- access to the RC files with credentials for both the source and target region,
- enough space on the local machine to be able to download an image of your server,
- a sufficiently configured target region including a [virtual network](../neutron/new-network.md) and necessary [security groups](../neutron/create-security-groups.md).

## Finding a volume's ID

To work with the OpenStack CLI, be sure to [source the RC file first](../../getting-started/enable-openstack-cli.md).

Use the server ID instead of the server name.
This ensures you operate on the correct server.

Find the ID of your server by matching the name, using the following command:

```console
$ openstack server list --name 'name'
+-----------------+-----------------+---------+-----------------+--------------------+-------------+
| ID              | Name            | Status  | Networks        | Image              | Flavor      |
+-----------------+-----------------+---------+-----------------+--------------------+-------------+
| 4e88215e-2df9-4 | Name2           | SHUTOFF | STO2_test_netwo | N/A (booted from v | b.1c1gb     |
| 9ca-8d39-31c01d |                 |         | rk=10.x.y.z     | olume)             |             |
| 5b7eae          |                 |         |                 |                    |             |
| fad16a17-a4f1-4 | Name1           | ACTIVE  | STO2_test_netwo | N/A (booted from v | b.1c1gb     |
| 74c-9b90-de14c8 |                 |         | rk=10.x.y.z     | olume)             |             |
| ab8100          |                 |         |                 |                    |             |
+-----------------+-----------------+---------+-----------------+--------------------+-------------+
```

This guide applies only to servers that boot from a volume.
To verify this, make sure your server's `Image` value is `N/A (booted from volume)`.

To get the ID of your server's boot volume, use the following command:

```console
$ openstack server show -c volumes_attached <server_id>
+------------------+-------------------------------------------+
| Field            | Value                                     |
+------------------+-------------------------------------------+
| volumes_attached | id='14942b23-25ef-4181-9c54-e5c100e4eeb8' |
|                  | id='34e2ca96-3c34-464f-ac66-9fef7a6810b8' |
|                  | id='68756558-dbf0-44db-9475-1bc24822371c' |
+------------------+-------------------------------------------+
```

If multiple volumes are attached, the first volume in the list is the server system volume.
Copy this ID.

If you want to move any other attached volumes along with your server's system volume, follow the same steps for each volume.

## Stopping a running server

In the next step, you are instructed to copy the server's system volume.
Some operating systems or applications may have issues when copied while they are performing operations.

While this step is not strictly required, we recommend powering off your server first.

Stop the running server with the following command:

```bash
openstack server stop <server_id>
```

## Creating a copy of a volume

Begin by making a copy of the volume, using the following command:

```bash
openstack volume create --source <source_volume_id> <copy_volume_name>
```

You will get a printout showing information about the created volume.
The `source_volid` field has the ID of the volume you just copied, while the `id` field has the ID of the **new** volume.
You will use the `id` value in the next step to create an image.

```plain
+---------------------+--------------------------------------+
| Field               | Value                                |
+---------------------+--------------------------------------+
| attachments         | []                                   |
| availability_zone   | nova                                 |
| bootable            | true                                 |
| consistencygroup_id | None                                 |
| created_at          | 2022-11-10T15:12:11.821647           |
| description         | None                                 |
| encrypted           | False                                |
| id                  | 2fde1e6d-2d72-4d70-b12d-1a2d314dba72 |
| multiattach         | False                                |
| name                | <copy_volume_name>                   |
| properties          |                                      |
| replication_status  | None                                 |
| size                | 20                                   |
| snapshot_id         | None                                 |
| source_volid        | 14942b23-25ef-4181-9c54-e5c100e4eeb8 |
| status              | creating                             |
| type                | default                              |
| updated_at          | None                                 |
| user_id             | 9e19-9424-42c4-b70f-a371ec0db5d3     |
+---------------------+--------------------------------------+
```

## Creating an image of a volume

Create an image of the copied volume by using the following command:

```bash
openstack image create --volume <copy_volume_id> <new_image_name>
```

> Substitute `<copy_volume_id>` with the ID from the newly created volume in the previous step.

After a while, you will get a printout showing information about the new image, such as the image disk format (`disk_format`) and the image ID (`image_id`).
You will soon need the values of `disk_format` and `image_id`.

```plain
+---------------------+--------------------------------------+
| Field               | Value                                |
+---------------------+--------------------------------------+
| container_format    | bare                                 |
| disk_format         | raw                                  |
| display_description | None                                 |
| id                  | 2fde1e6d-2d72-4d70-b12d-1a2d314dba72 |
| image_id            | cfa8620a-52d7-4d84-91ef-b25bb24e6e33 |
| image_name          | <new_image_name>                     |
| protected           | False                                |
| size                | 20                                   |
| status              | uploading                            |
| updated_at          | 2022-11-10T15:22:12.000000           |
| visibility          | shared                               |
| volume_type         | default                              |
+---------------------+--------------------------------------+
```

Depending on the volume size, the upload may take some time;
while it uploads, the image `status` is `uploading`.
Before you continue to the next step, make sure the image `status` is `active`.
If it isn't yet, wait a bit and then check again with:

```bash
openstack image show -c status <image_id>
```

The printout should look like this before you continue.

```plain
+--------+--------+
| Field  | Value  |
+--------+--------+
| status | active |
+--------+--------+
```

> It is now safe to remove the volume you created earlier, using the command: `openstack volume delete <copy_volume_id>`

## Downloading an image

Download the image to your local computer using the following command:

```bash
openstack image save --file <local_image_name>.<disk_format> <image_id>
```

> Substitute `<disk_format>` with the value from the printout in the previous step.
>
> Substitute `<image_id>` with the ID from the printout in the previous step.

When you have downloaded the file, verify that the checksum of the file is the same as the `checksum` value of the image.

```bash
md5 <local_image_name>.<disk_format>
```

This will output the checksum of your local file.

```plain
MD5 (<local_image_name>.<disk_format>) = 4b086035a943cc1676583c0cc78f0896
```

Show the checksum of the image in the cloud using the following command:

```bash
openstack image show -c checksum <image_id>
```

These two checksums should match.

```plain
+----------+----------------------------------+
| Field    | Value                            |
+----------+----------------------------------+
| checksum | 4b086035a943cc1676583c0cc78f0896 |
+----------+----------------------------------+
```

You are now done with the steps for the source region.
The following steps will be done on the target region.

> It is now safe to remove the image you created earlier, using the command:
> ```bash
> openstack image delete <image_id>
> ```

## Uploading an image

Source the RC file for the region you want to upload to.

```bash
source <target_region_openrc>
```

Upload the image to the new region.
Set the correct disk format:
enter the path to the image file, and select a name for the new image.

```bash
openstack image create --disk-format <disk_format> --file <local_image_name>.<disk_format> <new_image_name>
```

The upload will take some time, depending on your internet upload speed and the image size.
When the upload finishes, you get a printout with information about your image.

```plain
+------------------+-------------------------------------------------------------------------------+
| Field            | Value                                                                         |
+------------------+-------------------------------------------------------------------------------+
| container_format | bare                                                                          |
| created_at       | 2022-11-17T16:26:58Z                                                          |
| disk_format      | raw                                                                           |
| file             | /v2/images/df4593a9-a4d4-46fe-9c82-1b8f88ecac5d/file                          |
| id               | df4593a9-a4d4-46fe-9c82-1b8f88ecac5d                                          |
| min_disk         | 0                                                                             |
| min_ram          | 0                                                                             |
| name             | <new_image_name>                                                              |
| owner            | facabd68822643d19be8c9de84e27c49                                              |
| properties       | locations='[]', os_hidden='False', owner_specified.openstack.md5='',          |
|                  | owner_specified.openstack.object='images/<new_image_name>',                   |
|                  | owner_specified.openstack.sha256=''                                           |
| protected        | False                                                                         |
| schema           | /v2/schemas/image                                                             |
| status           | saving                                                                        |
| tags             |                                                                               |
| updated_at       | 2022-11-17T16:26:58Z                                                          |
| visibility       | shared                                                                        |
+------------------+-------------------------------------------------------------------------------+
```

Your image is not ready yet;
{{brand}} still needs to process the file, which shouldn't take long.
To check the status of the image, use the ID of the new image with the following command:

```console
$ openstack image show <new_image_id>
+------------------+-------------------------------------------------------------------------------+
| Field            | Value                                                                         |
+------------------+-------------------------------------------------------------------------------+
| checksum         | 4b086035a943cc1676583c0cc78f0896                                              |
| container_format | bare                                                                          |
| created_at       | 2022-11-17T16:26:58Z                                                          |
| disk_format      | raw                                                                           |
| file             | /v2/images/df4593a9-a4d4-46fe-9c82-1b8f88ecac5d/file                          |
| id               | df4593a9-a4d4-46fe-9c82-1b8f88ecac5d                                          |
| min_disk         | 0                                                                             |
| min_ram          | 0                                                                             |
| name             | <new_image_name>                                                              |
| owner            | facabd68822643d19be8c9de84e27c49                                              |
| properties       | locations='[]', os_hidden='False', owner_specified.openstack.md5='',          |
|                  | owner_specified.openstack.object='images/<new_image_name>',                   |
|                  | owner_specified.openstack.sha256=''                                           |
| protected        | False                                                                         |
| schema           | /v2/schemas/image                                                             |
| status           | active                                                                        |
| tags             |                                                                               |
| updated_at       | 2022-11-17T16:26:58Z                                                          |
| visibility       | shared                                                                        |
+------------------+-------------------------------------------------------------------------------+
```

When the image's `status` is `active`, the upload process is complete.

Verify that the checksum of the new image matches the checksum of your local file:

```bash
openstack image show -c checksum <new_image_id>
```

> It is now safe to remove the image file from your local computer.

## Creating a volume from an image

First, you must choose the image you want to create a volume from.

List all your private images with the following command:

```console
$ openstack image list --private
+--------------------------------------+--------------------------+--------+
| ID                                   | Name                     | Status |
+--------------------------------------+--------------------------+--------+
| f9ce95de-564e-4f6e-ad0e-789c84f30b7c | <new_image_name>         | active |
+--------------------------------------+--------------------------+--------+
```

Then create the volume using the ID of the image in this command:

```bash
openstack volume create --size <GB> --image <new_image_id> <new_volume_name>
```

> Substitute `<GB>` with the size in gigabytes you wish the volume to be.

## Creating a server from a volume

Now create the new server using the system volume.
To create a new server, follow [this guide](new-server.md).

=== "{{gui}}"
    If you use the {{gui}}, when choosing a _boot source,_ select _Boot from volume,_ then select your server's system volume.
=== "OpenStack CLI"
    If you use the OpenStack CLI, forgo the `--image` and `--boot-from-volume` options and instead use `--volume <new_volume_name>`

If you also moved other volumes, when you finish creating the server, do not forget to attach those volumes.
