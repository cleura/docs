---
description: How to modernize old boot-from-image servers
---
# Converting a boot-from-image server to boot-from-volume

You can freely move any server [between {{brand}} regions](move-server-between-regions.md), provided it boots from a volume.
Having boot-from-volume servers is something we generally recommend, since it affords more flexibility than booting from an image.

You may still have boot-from-image servers, though.
To verify that a particular server is of that type, you can go to the {{gui}}, locate the server, and expand its detailed view.
Go to the *Details* tab and pay attention to the *Boot Target* field.
If this is a boot-from-image server, it will say *Ephemeral Disk*.

![Checking the boot target of a server](assets/bfi-to-bfv/ephemeral_light.png#only-light)
![Checking the boot target of a server](assets/bfi-to-bfv/ephemeral_dark.png#only-dark)

Whenever you decide to move a boot-from-image server between regions, you will discover that you cannot do so.
The solution is first to convert it to a boot-from-volume server and then move it.
In the following, we show how to perform the conversion using the OpenStack CLI.

## Preparation

To work with the OpenStack CLI, make sure to properly [enable it](../../getting-started/enable-openstack-cli.md) for the region your boot-from-image server resides in.

## Shutting down the server

Assuming your boot-from-image server is named `ephemeral_eyjolfur`, shut it down by typing the following:

```plain
openstack server stop ephemeral_eyjolfur
```

To confirm that it has finished shutting down, type:

```plain
openstack server show ephemeral_eyjolfur -c status -f value
```

You should see this:

```plain
SHUTOFF
```

## Taking a snapshot

To take a snapshot of the server, all you have to do is type something like the following:

```console
$ openstack server image create --name ephemeral_eyjolfur_snap ephemeral_eyjolfur

+------------+-------------------------------------------------------------------------------------+
| Field      | Value                                                                               |
+------------+-------------------------------------------------------------------------------------+
| created_at | 2026-06-05T11:30:29Z                                                                |
| file       | /v2/images/4a556439-7f97-4808-96db-83ffaa971a1f/file                                |
| id         | 4a556439-7f97-4808-96db-83ffaa971a1f                                                |
| min_disk   | 50                                                                                  |
| min_ram    | 512                                                                                 |
| name       | ephemeral_eyjolfur_snap                                                             |
| owner      | 94109c764a754e24ac0f6b01aef82359                                                    |
| properties | architecture='x86_64', base_image_ref='ef290941-280b-47f5-8bd4-a02f4d0179f1',       |
|            | boot_roles='load-balancer_member,swiftoperator,member,creator,reader',              |
|            | cim_image_name='Debian 12 Bookworm x86_64', cim_time='1778515848',                  |
|            | hw_cdrom_bus='ide', hw_disk_bus='virtio', hw_input_bus='usb', hw_machine_type='pc', |
|            | hw_pointer_model='usbtablet', hw_qemu_guest_agent='yes', hw_video_model='virtio',   |
|            | hw_vif_model='virtio', hypervisor_type='qemu', image_build_date='2026-05-11',       |
|            | image_description='https://docs.cleura.cloud/reference/images/',                    |
|            | image_original_user='debian', image_source='private', image_type='snapshot',        |
|            | instance_uuid='d3d1e351-ca9f-43e6-bcc8-a7be0216bc01', locations='[]',               |
|            | os_distro='debian', os_hidden='False', os_type='linux', os_version='12',            |
|            | owner_project_name='Meanwhile-in-Drama', owner_specified.openstack.md5='',          |
|            | owner_specified.openstack.object='images/Debian 12 Bookworm x86_64 (2026-05-11)',   |
|            | owner_specified.openstack.sha256='', owner_user_name='CCP_User_43597_f1',           |
|            | provided_until='notice', replace_frequency='monthly',                               |
|            | user_id='c096cf99f65a4d22a6954b67d2ec11d7', uuid_validity='last-1'                  |
| protected  | False                                                                               |
| schema     | /v2/schemas/image                                                                   |
| status     | queued                                                                              |
| tags       |                                                                                     |
| updated_at | 2026-06-05T11:30:29Z                                                                |
| visibility | private                                                                             |
+------------+-------------------------------------------------------------------------------------+
```

At first, the status of the snapshot is `queued`.
To make sure the snapshot has been successfully created, type:

```plain
openstack image show ephemeral_eyjolfur_snap -c status -f value
```

You should see this:

```plain
active
```

## Creating a volume from the snapshot

Before creating a volume off of the snapshot you just created, jot down its size like this:

```bash
openstack image show nanisivik_snap -c min_disk -f value
```

In our example, the size of the snapshot is `50` [gibibytes](https://en.wikipedia.org/wiki/Gigabyte#Base_2_(binary)).
Now, go ahead and create a volume slightly larger than the size of the snapshot:

```console
$ openstack volume create --size 56 --image ephemeral_eyjolfur_snap ephemeral_eyjolfur_vol

+--------------------------------+--------------------------------------+
| Field                          | Value                                |
+--------------------------------+--------------------------------------+
| attachments                    | []                                   |
| availability_zone              | nova                                 |
| backup_id                      | None                                 |
| bootable                       | False                                |
| cluster_name                   | None                                 |
| consumes_quota                 | True                                 |
| created_at                     | 2026-06-05T11:36:18.033818           |
| description                    | None                                 |
| encrypted                      | False                                |
| group_id                       | None                                 |
| id                             | 07f13557-125e-48d2-a867-21f0a51ea891 |
| multiattach                    | False                                |
| name                           | ephemeral_eyjolfur_vol               |
| os-vol-host-attr:host          | None                                 |
| os-vol-mig-status-attr:migstat | None                                 |
| os-vol-mig-status-attr:name_id | None                                 |
| os-vol-tenant-attr:tenant_id   | None                                 |
| properties                     |                                      |
| provider_id                    | None                                 |
| replication_status             | None                                 |
| service_uuid                   | None                                 |
| shared_targets                 | True                                 |
| size                           | 56                                   |
| snapshot_id                    | None                                 |
| source_volid                   | None                                 |
| status                         | creating                             |
| type                           | cbs                                  |
| updated_at                     | None                                 |
| user_id                        | c096cf99f65a4d22a6954b67d2ec11d7     |
| volume_type_id                 | 5f7ecf32-4b4b-4e95-82c8-5d0eccae887e |
+--------------------------------+--------------------------------------+
```

As you can see in the example above, we named our volume `ephemeral_eyjolfur_vol`, and its `status` was at first `creating`.
You may check the progress of this operation by typing this:

```plain
openstack volume show ephemeral_eyjolfur_vol -c status -f value
```

As soon as the new volume is ready, the `status` becomes `available`.

## Viewing the new volume

To view all details regarding the volume you just created off of the boot-from-image server snapshot, type the following:

```console
$ openstack volume show ephemeral_eyjolfur_vol

+--------------------------------+-----------------------------------------------------------------+
| Field                          | Value                                                           |
+--------------------------------+-----------------------------------------------------------------+
| attachments                    | []                                                              |
| availability_zone              | nova                                                            |
| backup_id                      | None                                                            |
| bootable                       | True                                                            |
| cluster_name                   | None                                                            |
| consumes_quota                 | True                                                            |
| created_at                     | 2026-06-05T11:36:18.000000                                      |
| description                    | None                                                            |
| encrypted                      | False                                                           |
| group_id                       | None                                                            |
| id                             | 07f13557-125e-48d2-a867-21f0a51ea891                            |
| multiattach                    | False                                                           |
| name                           | ephemeral_eyjolfur_vol                                          |
| os-vol-host-attr:host          | None                                                            |
| os-vol-mig-status-attr:migstat | None                                                            |
| os-vol-mig-status-attr:name_id | None                                                            |
| os-vol-tenant-attr:tenant_id   | 94109c764a754e24ac0f6b01aef82359                                |
| properties                     |                                                                 |
| provider_id                    | None                                                            |
| replication_status             | None                                                            |
| service_uuid                   | cb0af1f1-5c8b-4654-94bc-977e27c9f6a3                            |
| shared_targets                 | False                                                           |
| size                           | 56                                                              |
| snapshot_id                    | None                                                            |
| source_volid                   | None                                                            |
| status                         | available                                                       |
| type                           | cbs                                                             |
| updated_at                     | 2026-06-05T11:37:24.000000                                      |
| user_id                        | c096cf99f65a4d22a6954b67d2ec11d7                                |
| volume_image_metadata          | {'signature_verified': 'False', 'architecture': 'x86_64',       |
|                                | 'base_image_ref': 'ef290941-280b-47f5-8bd4-a02f4d0179f1',       |
|                                | 'boot_roles': 'load-                                            |
|                                | balancer_member,swiftoperator,member,creator,reader',           |

[...]

|                                | 'disk_format': 'qcow2', 'min_disk': '50', 'min_ram': '512',     |
|                                | 'size': '2434793472'}                                           |
| volume_type_id                 | 5f7ecf32-4b4b-4e95-82c8-5d0eccae887e                            |
+--------------------------------+-----------------------------------------------------------------+
```

Note that the new volume is bootable:

```console
$ openstack volume show ephemeral_eyjolfur_vol -c bootable

+----------+-------+
| Field    | Value |
+----------+-------+
| bootable | True  |
+----------+-------+
```

## Deleting the boot-from-image server

Since you have a snapshot and a volume of your server, you can now delete it:

```plain
openstack server delete ephemeral_eyjolfur
```

A successful `delete` operation produces no terminal output.

## Creating a new boot-from-volume server

To create your new boot-from-volume server (`eyjolfur`), using the volume (`ephemeral_eyjolfur_vol`) you got from the snapshot (`ephemeral_eyjolfur_snap`) of the old boot-from-image server (`ephemeral_eyjolfur`), type something like the following:

```plain
openstack server create \
    --flavor b.2c4gb \
    --volume ephemeral_eyjolfur_vol \
    --network network-{{api_region|lower}} \
    --security-group default \
    --key-name karlskrona \
    --wait \
    eyjolfur
```

The most important parameter in the command above is `--volume`, which is used to specify the boot volume of the server.
Regarding server creation in general, you might want to [check the corresponding guide](new-server.md).

## Viewing the new server

You may see all details regarding the new boot-from-volume server by typing something like the following:

```console
$ openstack server show eyjolfur

+-------------------------------------+------------------------------------------------------------+
| Field                               | Value                                                      |
+-------------------------------------+------------------------------------------------------------+
| OS-DCF:diskConfig                   | MANUAL                                                     |
| OS-EXT-AZ:availability_zone         | nova                                                       |
| OS-EXT-SRV-ATTR:host                | None                                                       |
| OS-EXT-SRV-ATTR:hostname            | eyjolfur                                                   |

[...]

| addresses                           | network-kna1=10.15.30.181                                  |
| config_drive                        |                                                            |
| created                             | 2026-06-05T12:16:57Z                                       |
| description                         | None                                                       |
| flavor                              | description=, disk='0', ephemeral='0',                     |
|                                     | extra_specs.cleura:flavor_type='generic', id='b.2c4gb',    |
|                                     | is_disabled=, is_public='True', location=, name='b.2c4gb', |
|                                     | original_name='b.2c4gb', ram='4096', rxtx_factor=,         |
|                                     | swap='0', vcpus='2'                                        |
| hostId                              | 431c867fc15bbf17cc956c4666cec40ef295ed2f469ee836b70c43aa   |
| host_status                         | None                                                       |
| id                                  | 55a42291-5ec1-491e-9683-7e6297417be7                       |
| image                               | N/A (booted from volume)                                   |
| key_name                            | karlskrona                                                 |
| locked                              | False                                                      |
| locked_reason                       | None                                                       |
| name                                | eyjolfur                                                   |
| pinned_availability_zone            | nova                                                       |
| progress                            | 0                                                          |
| project_id                          | 94109c764a754e24ac0f6b01aef82359                           |
| properties                          |                                                            |
| scheduler_hints                     |                                                            |
| security_groups                     | name='default'                                             |
| server_groups                       | None                                                       |
| status                              | ACTIVE                                                     |
| tags                                |                                                            |
| trusted_image_certificates          | None                                                       |
| updated                             | 2026-06-05T12:17:14Z                                       |
| user_id                             | c096cf99f65a4d22a6954b67d2ec11d7                           |
| volumes_attached                    | delete_on_termination='False',                             |
|                                     | id='07f13557-125e-48d2-a867-21f0a51ea891'                  |
+-------------------------------------+------------------------------------------------------------+
```

Pay attention to the value of the `image` field, which confirms that this is indeed a boot-from-volume server.
