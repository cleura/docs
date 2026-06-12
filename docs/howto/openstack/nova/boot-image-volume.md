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

=== "{{gui}}"
    Fire up your favorite web browser and navigate to the [{{gui}}](https://{{gui_domain}}) start page.
    Log in to your {{brand}} account if you have to.

=== "OpenStack CLI"
    To work with the OpenStack CLI, make sure to properly [enable it](../../getting-started/enable-openstack-cli.md) for the region your boot-from-image server resides in.

## Shutting down the server

=== "{{gui}}"
    Make sure the left-hand side vertical pane is in full view, then select *Compute* → [*Servers*](https://{{gui_domain}}/compute/servers).
    You will see all supported {{brand}} regions in the main pane.
    Expand the one with the boot-from-image server you want to convert to boot-from-volume.
    Click the :material-dots-horizontal-circle: icon at the right of the server row, and from the pop-up menu that appears, select *Stop Server*.

    ![Stopping server](assets/bfi-to-bfv/shot01_light.png#only-light)
    ![Stopping server](assets/bfi-to-bfv/shot01_dark.png#only-dark)

    A pop-up window appears, asking if you want to stop the server.
    Confirm by clicking on the button labeled *Yes, Stop*.

    ![Confirming server shutdown](assets/bfi-to-bfv/are-you-really-really-sure_light.png#only-light)
    ![Confirming server shutdown](assets/bfi-to-bfv/are-you-really-really-sure_dark.png#only-dark)

=== "OpenStack CLI"
    Assuming your boot-from-image server is named `ephemeral_eyjolfur`, shut it down by typing the following:

    ```bash
    openstack server stop ephemeral_eyjolfur
    ```

    To confirm that it has finished shutting down, type:

    ```bash
    openstack server show ephemeral_eyjolfur -c status -f value
    ```

    You should see this:

    ```plain
    SHUTOFF
    ```

## Taking a snapshot

=== "{{gui}}"
    When the server is shut off, click on its row to get the detailed view and go to the *Snapshots* tab.
    There, click the button labeled *Create a Snapshot*.

    ![Creating a snapshot](assets/bfi-to-bfv/shot02_light.png#only-light)
    ![Creating a snapshot](assets/bfi-to-bfv/shot02_dark.png#only-dark)

    A pop-up window appears, where you have to type in a name for the snapshot.
    You must also be explicit regarding the operation you are about to perform, so activate the switch at the left of the corresponding question.
    When you are ready, click the button labeled *Create*.

    ![Confirming snapshot creation](assets/bfi-to-bfv/shot03_light.png#only-light)
    ![Confirming snapshot creation](assets/bfi-to-bfv/shot03_dark.png#only-dark)

=== "OpenStack CLI"
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

    ```bash
    openstack image show ephemeral_eyjolfur_snap -c status -f value
    ```

    You should see this:

    ```plain
    active
    ```

## Creating a volume from the snapshot

=== "{{gui}}"
    After a few seconds, the snapshot will be created and listed in the *Snapshots* tab.
    Before you proceed, take note of its size.
    At the right-hand side of the snapshot row, click the :fontawesome-solid-database: icon to create a new volume off of the snapshot you just created.

    ![Creating volume from snapshot](assets/bfi-to-bfv/shot04_light.png#only-light)
    ![Creating volume from snapshot](assets/bfi-to-bfv/shot04_dark.png#only-dark)

    A new vertical pane will slide over from the right-hand side of the {{gui}}.
    Type in a name for the new volume, and choose a volume size **bigger** than the snapshot size.
    Then, you need to type in a description regarding the new volume.

    ![Typing in name, size, and description](assets/bfi-to-bfv/shot05_light.png#only-light)
    ![Typing in name, size, and description](assets/bfi-to-bfv/shot05_dark.png#only-dark)

    Scroll down a bit if you have to, and click the *Create* button.

    ![Starting volume creation](assets/bfi-to-bfv/shot06_light.png#only-light)
    ![Starting volume creation](assets/bfi-to-bfv/shot06_dark.png#only-dark)

=== "OpenStack CLI"
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

    ```bash
    openstack volume show ephemeral_eyjolfur_vol -c status -f value
    ```

    As soon as the new volume is ready, the `status` becomes `available`.

## Viewing the new volume

=== "{{gui}}"
    In the left-hand side vertical pane, select *Storage* → [*Volumes*](https://{{gui_domain}}/storage/volumes).
    In the main pane, select the region your boot-from-image server resides in.
    You will see the volume you created in the previous step.

    In the intersection of the volume row and the *Attached To* column, it says *-No attachments-*.
    That is expected.

    Then, notice that the volume is bootable.
    That is also expected.

    ![Viewing new volume](assets/bfi-to-bfv/shot07_light.png#only-light)
    ![Viewing new volume](assets/bfi-to-bfv/shot07_dark.png#only-dark)

=== "OpenStack CLI"
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

=== "{{gui}}"

    Go to the servers view by selecting *Compute* → [*Servers*](https://{{gui_domain}}/compute/servers), and locate the boot-from-image server.
    It is time to delete it, so click the :material-dots-horizontal-circle: icon at the right of the server row, and from the pop-up menu that appears, select *Delete Server*.

    ![Deleting server](assets/bfi-to-bfv/shot08_light.png#only-light)
    ![Deleting server](assets/bfi-to-bfv/shot08_dark.png#only-dark)

    A window titled *About to delete a server* will appear, asking you if you want to proceed with the deletion.
    Click the button labeled *Yes, Delete*.

    ![Confirming server deletion](assets/bfi-to-bfv/shot09_light.png#only-light)
    ![Confirming server deletion](assets/bfi-to-bfv/shot09_dark.png#only-dark)

=== "OpenStack CLI"
    Since you have a snapshot and a volume of your server, you can now delete it:

    ```bash
    openstack server delete ephemeral_eyjolfur
    ```

    A successful `delete` operation produces no terminal output.

## Creating a new boot-from-volume server

=== "{{gui}}"
    Now, go back to your volumes by selecting *Storage* → [*Volumes*](https://{{gui_domain}}/storage/volumes).
    Tick the volume you created a bit earlier, click the :material-dots-horizontal-circle: icon at the right of the volume row, and from the pop-up menu that appears, select *Create Server*.

    ![Creating a new server](assets/bfi-to-bfv/shot10_light.png#only-light)
    ![Creating a new server](assets/bfi-to-bfv/shot10_dark.png#only-dark)

    A vertical pane will slide over from the right-hand side of the {{gui}}, titled *Create a Server*.
    Type in a name for the new server.
    Notice that the server region is pre-selected and the same as the one in which the volume resides.
    The boot source of the server is also pre-selected and is the volume itself.

    ![Naming the server](assets/bfi-to-bfv/shot11_light.png#only-light)
    ![Naming the server](assets/bfi-to-bfv/shot11_dark.png#only-dark)

    Scroll down a bit if you have to.
    Take notice of the *Boot Target*, which should be *Volume*.
    Consider leaving the [*Recovery service*](../../../background/recovery-service.md) option enabled.

    ![Keeping the recovery service enabled](assets/bfi-to-bfv/shot12_light.png#only-light)
    ![Keeping the recovery service enabled](assets/bfi-to-bfv/shot12_dark.png#only-dark)

    To create the new server, scroll all the way down and click the button labeled *Create*.

    ![Initiating server creation](assets/bfi-to-bfv/shot13_light.png#only-light)
    ![Initiating server creation](assets/bfi-to-bfv/shot13_dark.png#only-dark)

=== "OpenStack CLI"
    To create your new boot-from-volume server (`eyjolfur`), using the volume (`ephemeral_eyjolfur_vol`) you got from the snapshot (`ephemeral_eyjolfur_snap`) of the old boot-from-image server (`ephemeral_eyjolfur`), type something like the following:

    ```bash
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

=== "{{gui}}"
    In the left-hand side vertical pane, select *Compute* → [*Servers*](https://{{gui_domain}}/compute/servers).
    In the main pane of the {{gui}}, go to the region where the new server resides
    Select the server and click on its row to see all its characteristics.
    In the *Details* tab, you will notice, among other things, that it has one attached volume;
    that would be the one you created from the snapshot you created from the old boot-from-image server.

    ![Viewing the new boot-from-volume server](assets/bfi-to-bfv/shot14_light.png#only-light)
    ![Viewing the new boot-from-volume server](assets/bfi-to-bfv/shot14_dark.png#only-dark)

=== "OpenStack CLI"
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
