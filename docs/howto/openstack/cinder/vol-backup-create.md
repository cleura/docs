---
description: Using the OpenStack CLI or the Cleura Cloud Management Panel, you may create full or incremental backups of available or attached Cinder volumes.
---
# Creating volume backups

{{page.meta.description}}
You can encrypt the volumes you back up.

You can also examine backup characteristics.
For example, you might want to see whether a backup is incremental.

## Prerequisites

If you plan to use the OpenStack CLI, make sure you [enable it](../../getting-started/enable-openstack-cli.md).

## Identifying the volume

=== "{{gui}}"
    Make sure the left-hand side vertical pane is expanded.
    To view all volumes and identify the ones you wish to back up, go to the *Storage* subsection and click *Volumes.*
    You will see all volumes listed in the central pane of the {{gui}}.

    ![All volumes are in the main pane](assets/backup-create/shot-01_light.png#only-light)
    ![All volumes are in the main pane](assets/backup-create/shot-01_dark.png#only-dark)

=== "OpenStack CLI"
    Use the `openstack volume list` command to identify any volumes you may wish to back up:

    ```console
    $ openstack volume list
    +--------------------------------------+------------------+-----------+------+---------------------------------+
    | ID                                   | Name             | Status    | Size | Attached to                     |
    +--------------------------------------+------------------+-----------+------+---------------------------------+
    | a84388d9-b3dc-456b-9aab-9da8e9fa1633 | my-vol           | available |   24 |                                 |
    | 681ceb2d-b0c5-4457-88af-e79b3b3009e6 | my-vol-enc       | available |   32 |                                 |
    | 5faf793f-521b-4bfb-b531-72908bab8bf7 | my-vol-att       | in-use    |   64 | Attached to my-srv on /dev/vdb  |
    +--------------------------------------+------------------+-----------+------+---------------------------------+
    ```

    In the example output above, we have a volume named `my-vol`, which is available (not attached to an instance).
    We also have a volume named `my-vol-att`, which is in use (attached to an instance).
    Finally, we have the volume named `my-vol-enc`, which is available and encrypted:

    ```console
    $ openstack volume show my-vol-enc -c encrypted
    +-----------+-------+
    | Field     | Value |
    +-----------+-------+
    | encrypted | True  |
    +-----------+-------+
    ```

## Creating a full backup

=== "{{gui}}"
    Locate the volume you want to back up.
    At the right-hand side of its row, click the :material-dots-horizontal-circle: icon.
    A drop-down menu appears.
    Select *Create Cinder Backup.*

    ![Initiate the creation of a Cinder Backup](assets/backup-create/shot-02_light.png#only-light)
    ![Initiate the creation of a Cinder Backup](assets/backup-create/shot-02_dark.png#only-dark)

    A vertical pane named *Cinder Backup* slides into view from the right.

    ![Name the backup you are about to create](assets/backup-create/shot-03_light.png#only-light)
    ![Name the backup you are about to create](assets/backup-create/shot-03_dark.png#only-dark)

    At the top of that pane, type in a name for the backup you are about to create.
    For a regular backup, leave the *Backup Policy* toggle as is (*Mutable*).
    You may optionally enter a *Description* for the backup.
    When you are ready, click *Create* to start the backup.

    While the backup is being created, a :material-content-save: icon appears to the left of the volume row.

    ![A save-icon indicates a backup is in progress](assets/backup-create/shot-04_light.png#only-light)
    ![A save-icon indicates a backup is in progress](assets/backup-create/shot-04_dark.png#only-dark)

    Expand the volume row and go to the *Details* tab;
    the value of the *Status* label is *backing-up*.

    ![Viewing the details of a volume with a backup in progress](assets/backup-create/shot-05_light.png#only-light)
    ![Viewing the details of a volume with a backup in progress](assets/backup-create/shot-05_dark.png#only-dark)

    Once the backup completes, the :material-content-save: icon disappears.
    Bring the *Backup* tab into view and see all related volume backups.

    ![All backups of the selected volume](assets/backup-create/shot-06_light.png#only-light)
    ![All backups of the selected volume](assets/backup-create/shot-06_dark.png#only-dark)

=== "OpenStack CLI"
    To create a full backup of `my-vol`, type:

    ```console
    $ openstack volume backup create my-vol
    +-----------+--------------------------------------+
    | Field     | Value                                |
    +-----------+--------------------------------------+
    | id        | b2821cde-d08e-411d-9798-61bc63517cc4 |
    | name      | None                                 |
    | volume_id | 9a7d10ba-c371-4b58-9a44-63cd8cc93639 |
    +-----------+--------------------------------------+
    ```

    The command above does not name the backup or add a description.
    Whenever you want to name your backup or give it a description, type:

    ```console
    $ openstack volume backup create --name my-vol-backup --description "My volume backup" my-vol
    +-----------+--------------------------------------+
    | Field     | Value                                |
    +-----------+--------------------------------------+
    | id        | 0dd94aa9-d291-4665-8183-06aceeaa40b8 |
    | name      | my-vol-backup                        |
    | volume_id | a84388d9-b3dc-456b-9aab-9da8e9fa1633 |
    +-----------+--------------------------------------+
    ```

## Examining a backup

=== "{{gui}}"
    In the left-hand side vertical pane of the {{gui}}, expand the *Storage* subcategory.
    Select *Backups*, and in the main pane, all existing backups appear.
    Locate the one you want, click its row, and view all relevant details.

    ![Get details regarding the selected backup](assets/backup-create/shot-07_light.png#only-light)
    ![Get details regarding the selected backup](assets/backup-create/shot-07_dark.png#only-dark)

=== "OpenStack CLI"
    To view details regarding an existing backup, use the `openstack volume backup show` command:

    ```console
    $ openstack volume backup show my-vol-backup
    +-----------------------+--------------------------------------+
    | Field                 | Value                                |
    +-----------------------+--------------------------------------+
    | availability_zone     | backup-local                         |
    | container             | mutable                              |
    | created_at            | 2026-09-09T09:24:44.000000           |
    | data_timestamp        | 2026-09-09T09:24:44.000000           |
    | description           | My volume backup                     |
    | encryption_key_id     | None                                 |
    | fail_reason           | None                                 |
    | has_dependent_backups | False                                |
    | id                    | 0dd94aa9-d291-4665-8183-06aceeaa40b8 |
    | is_incremental        | False                                |
    | metadata              | {}                                   |
    | name                  | my-vol-backup                        |
    | object_count          | 492                                  |
    | project_id            | None                                 |
    | size                  | 24                                   |
    | snapshot_id           | None                                 |
    | status                | available                            |
    | updated_at            | 2026-09-09T09:29:05.000000           |
    | user_id               | None                                 |
    | volume_id             | a84388d9-b3dc-456b-9aab-9da8e9fa1633 |
    +-----------------------+--------------------------------------+
    ```

## Creating an incremental backup

=== "{{gui}}"
    To create an incremental backup, enable this feature in the *Create Backup* pane.

    ![Making sure the new backup is incremental](assets/backup-create/shot-08_light.png#only-light)
    ![Making sure the new backup is incremental](assets/backup-create/shot-08_dark.png#only-dark)

    To check whether a backup is incremental, go to the left-hand side vertical pane, click *Storage,* and then click *Backups.*
    Locate your backup, expand its row, and look for the *Incremental backup* field;
    it should be set to *True.*

    ![Checking whether a backup is incremental](assets/backup-create/shot-09_light.png#only-light)
    ![Checking whether a backup is incremental](assets/backup-create/shot-09_dark.png#only-dark)

=== "OpenStack CLI"
    You can create an incremental backup of an existing volume backup;
    only the blocks that have changed since the most recent backup will be copied.

    For instance, to create an incremental backup of `my-vol`, type:

    ```console
    $ openstack volume backup create --name my-vol-backup-incr --incremental my-vol
    +-----------+--------------------------------------+
    | Field     | Value                                |
    +-----------+--------------------------------------+
    | id        | 62071506-04e7-4643-a399-fa842de9d246 |
    | name      | my-vol-backup-incr                   |
    | volume_id | a84388d9-b3dc-456b-9aab-9da8e9fa1633 |
    +-----------+--------------------------------------+
    ```

    To check whether a backup is incremental, enter:

    ```console
    $ openstack volume backup show my-vol-backup-incr -c is_incremental
    +----------------+-------+
    | Field          | Value |
    +----------------+-------+
    | is_incremental | True  |
    +----------------+-------+
    ```

## Creating backups in immutable containers

=== "{{gui}}"
    To create a backup in an immutable container, in the *Create Backup* pane, toggle the *Backup Policy* to *Immutable.*
    Then, from the *Days immutable* drop-down menu, select either *30 days* or *90 days.*

    ![Switching the backup policy to "immutable" and selecting immutability period](assets/backup-create/shot-10_light.png#only-light)
    ![Switching the backup policy to "immutable" and selecting immutability period](assets/backup-create/shot-10_dark.png#only-dark)

    To check whether a backup is in an immutable container, in the vertical pane on the left, click *Storage,* and then *Backups.*
    Locate your backup and expand its row.
    Look for the *Policy* field;
    it should be either *Immutable 30 days* or *Immutable 90 days.*

    ![Checking whether a backup is in an immutable container](assets/backup-create/shot-11_light.png#only-light)
    ![Checking whether a backup is in an immutable container](assets/backup-create/shot-11_dark.png#only-dark)

=== "OpenStack CLI"
    You can create backups in immutable containers by specifying a special container named `30d-immutable` or `90d-immutable`.

    For example, if you want to create a backup of `my-vol` in an immutable-for-30-days container, issue the following:

    ```console
    $ openstack volume backup create --name my-vol-backup-imm --container 30d-immutable my-vol
    +-----------+--------------------------------------+
    | Field     | Value                                |
    +-----------+--------------------------------------+
    | id        | 00f2e367-4e7e-4364-a2c8-600de989aca5 |
    | name      | my-vol-backup-imm                    |
    | volume_id | a84388d9-b3dc-456b-9aab-9da8e9fa1633 |
    +-----------+--------------------------------------+
    ```

    To verify that your `my-vol-backup-imm` backup is indeed in the `30d-immutable` container, type:

    ```console
    $ openstack volume backup show -c container my-vol-backup-imm
    +-----------+---------------+
    | Field     | Value         |
    +-----------+---------------+
    | container | 30d-immutable |
    +-----------+---------------+
    ```

    Although you *can* delete backups in immutable containers, you may also restore a deleted backup by [raising a support ticket](../../support/raise-issues.md) within 30 or 90 days of deletion.

## Backing up an attached volume

=== "{{gui}}"
    You may create backups of volumes attached to instances.
    While creating such a backup, you see a related warning and a suggestion;
    to ensure the backup is consistent, detach the volume first.

    ![Create backups of attached volumes as per usual](assets/backup-create/shot-12_light.png#only-light)
    ![Create backups of attached volumes as per usual](assets/backup-create/shot-12_dark.png#only-dark)

=== "OpenStack CLI"
    To create a backup of a volume that is attached to a VM, use the `openstack volume backup create` command with the `--force` directive:

    ```console
    $ openstack volume backup create --name my-vol-att-backup --force --description "My attached volume backup" my-vol-att
    +-----------+--------------------------------------+
    | Field     | Value                                |
    +-----------+--------------------------------------+
    | id        | 33d8c4a4-b238-465f-a063-84c6fab62e9d |
    | name      | my-vol-att-backup                    |
    | volume_id | 5faf793f-521b-4bfb-b531-72908bab8bf7 |
    +-----------+--------------------------------------+
    ```

## Backing up encrypted volumes

=== "{{gui}}"
    To back up an encrypted volume, follow the same steps as for an unencrypted one.

    ![Create backups of encrypted volumes as you would with unencrypted volumes](assets/backup-create/shot-13_light.png#only-light)
    ![Create backups of encrypted volumes as you would with unencrypted volumes](assets/backup-create/shot-13_dark.png#only-dark)

=== "OpenStack CLI"
    You can back up an encrypted volume the same way you would an unencrypted one.
    For example, suppose you want to back up the encrypted volume `my-vol-enc`.
    Then, go ahead and create a backup of it as usual:

    ```console
    $ openstack volume backup create --name my-vol-enc-backup --description "My encrypted volume backup" my-vol-enc
    +-----------+--------------------------------------+
    | Field     | Value                                |
    +-----------+--------------------------------------+
    | id        | 964b182a-8bea-405c-ad03-24b00e090931 |
    | name      | my-vol-enc-backup                    |
    | volume_id | 681ceb2d-b0c5-4457-88af-e79b3b3009e6 |
    +-----------+--------------------------------------+
    ```

    Get the details on the backup of your encrypted volume:

    ```console
    $ openstack volume backup show my-vol-enc-backup
    +-----------------------+--------------------------------------+
    | Field                 | Value                                |
    +-----------------------+--------------------------------------+
    | availability_zone     | backup-local                         |
    | container             | mutable                              |
    | created_at            | 2026-09-09T09:57:47.000000           |
    | data_timestamp        | 2026-09-09T09:57:47.000000           |
    | description           | My encrypted volume backup           |
    | encryption_key_id     | d6f78ff8-48e3-4d7f-bdf1-87a56be4bc27 |
    | fail_reason           | None                                 |
    | has_dependent_backups | False                                |
    | id                    | 964b182a-8bea-405c-ad03-24b00e090931 |
    | is_incremental        | False                                |
    | metadata              | {}                                   |
    | name                  | my-vol-enc-backup                    |
    | object_count          | 0                                    |
    | project_id            | None                                 |
    | size                  | 32                                   |
    | snapshot_id           | None                                 |
    | status                | creating                             |
    | updated_at            | 2026-09-09T09:57:51.000000           |
    | user_id               | None                                 |
    | volume_id             | 681ceb2d-b0c5-4457-88af-e79b3b3009e6 |
    +-----------------------+--------------------------------------+
    ```
