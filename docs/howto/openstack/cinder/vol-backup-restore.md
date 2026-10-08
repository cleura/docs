---
description: Using the OpenStack CLI or the Cleura Cloud Management Panel, you may restore Cinder backups to new or existing volumes.
---
# Restoring volume backups

{{page.meta.description}}

## Prerequisites

If you plan to use the OpenStack CLI, [enable it first](../../getting-started/enable-openstack-cli.md).

## Listing available backups

=== "{{gui}}"
    In the {{gui}}, make sure the left-hand navigation pane is fully visible.
    Expand the *Storage* category and click *Backups.*
    In the main pane, all available Cinder backups appear.

    ![All available Cinder backups](assets/backup-restore/shot-01_light.png#only-light)
    ![All available Cinder backups](assets/backup-restore/shot-01_dark.png#only-dark)

=== "OpenStack CLI"
    Use the `openstack volume backup list` command to list all available backups:

    ```console
    $ openstack volume backup list -c ID -c Name -c Description -c Status -c Size -c Incremental
    +--------------------------------------+--------------------+------------------------------+-----------+------+-------------+
    | ID                                   | Name               | Description                  | Status    | Size | Incremental |
    +--------------------------------------+--------------------+------------------------------+-----------+------+-------------+
    | 33d8c4a4-b238-465f-a063-84c6fab62e9d | my-vol-att-backup  | My attached volume backup    | available |   64 | False       |
    | 00f2e367-4e7e-4364-a2c8-600de989aca5 | my-vol-backup-imm  | My immutable volume backup   | available |   24 | False       |
    | 62071506-04e7-4643-a399-fa842de9d246 | my-vol-backup-incr | My incremental volume backup | available |   24 | True        |
    | 0dd94aa9-d291-4665-8183-06aceeaa40b8 | my-vol-backup      | My volume backup             | available |   24 | False       |
    | 6f67acf4-e040-41c0-802e-939b9964dcef | my-vol-enc-backup  | My encrypted volume backup   | available |   32 | False       |
    +--------------------------------------+--------------------+------------------------------+-----------+------+-------------+
    ```

## Restoring a backup to a new volume

=== "{{gui}}"
    Locate the Cinder backup you want to restore.
    Click the :material-dots-horizontal-circle: icon at the right of its row.
    From the pop-up menu that appears, select *Restore Backup.*

    ![Locate the Cinder backup you are interested in restoring](assets/backup-restore/shot-02_light.png#only-light)
    ![Locate the Cinder backup you are interested in restoring](assets/backup-restore/shot-02_dark.png#only-dark)

    A vertical pane named *Restore Backup* slides over from the right.
    In the *Restore to* list, use the toggle to activate the *New volume* option.
    In the *Volume Name* text field, enter a name for the new volume you are about to restore to.
    Then, use the drop-down menu below to set the *Availability Zone* to the zone you want the new volume in.
    When ready, click *Restore* to begin restoring.

    ![Name and availability zone for the new volume you are about to restore to](assets/backup-restore/shot-03_light.png#only-light)
    ![Name and availability zone for the new volume you are about to restore to](assets/backup-restore/shot-03_dark.png#only-dark)

    From the vertical navigation pane on the left, select *Storage* and then *Volumes.*
    Click on the new (restore) volume row to bring its details into view.
    Notice the *Status* parameter;
    while it starts as *restoring-backup,* when the restore process completes, it becomes *available.*
    Also, check the *Availability Zone* parameter;
    it should match the zone you selected for the restore volume.

    ![Restoration to a new volume is complete](assets/backup-restore/shot-04_light.png#only-light)
    ![Restoration to a new volume is complete](assets/backup-restore/shot-04_dark.png#only-dark)

=== "OpenStack CLI"
    To restore a backup to a new volume, use the `openstack volume backup restore` command like so:

    ```console
    $ openstack volume backup restore my-vol-backup my-vol-restored

    +-------------+--------------------------------------+
    | Field       | Value                                |
    +-------------+--------------------------------------+
    | id          | 0dd94aa9-d291-4665-8183-06aceeaa40b8 |
    | volume_id   | b1ab96f8-26c4-4847-b7c1-0c20d48fc6e5 |
    | volume_name | my-vol-restored                      |
    +-------------+--------------------------------------+
    ```

    While the restoration is progressing, the `status` field of the new volume is `restoring-backup`:

    ```console
    $ openstack volume show my-vol-restored -c status
    +--------+------------------+
    | Field  | Value            |
    +--------+------------------+
    | status | restoring-backup |
    +--------+------------------+
    ```

    As soon as the restoration completes, `status` becomes `available`:

    ```console
    $ openstack volume show my-vol-restored -c status
    +--------+-----------+
    | Field  | Value     |
    +--------+-----------+
    | status | available |
    +--------+-----------+
    ```

## Restoring a backup to an existing volume

!!! danger "Loss of existing data"
    Restoring a backup to the *original* or an *existing* volume overwrites all data currently on it.

=== "{{gui}}"
    Locate the Cinder backup you want to restore.
    Click the :material-dots-horizontal-circle: icon at the right of its row.
    From the pop-up menu that appears, select *Restore Backup.*

    ![Selecting a backup to restore](assets/backup-restore/shot-05_light.png#only-light)
    ![Selecting a backup to restore](assets/backup-restore/shot-05_dark.png#only-dark)

    A vertical pane named *Restore Backup* slides over from the right.
    In the *Restore to* list, use the toggle to activate the *Same volume (`<volume-name>`)* option.

    ![Selecting the original volume to restore into](assets/backup-restore/shot-06_light.png#only-light)
    ![Selecting the original volume to restore into](assets/backup-restore/shot-06_dark.png#only-dark)

    Another option you have is to use the toggle and select *Existing volume.*
    In that case, you indicate an existing volume that is at least as large as the original backed-up volume.

    ![Selecting an existing volume to restore into](assets/backup-restore/shot-07_light.png#only-light)
    ![Selecting an existing volume to restore into](assets/backup-restore/shot-07_dark.png#only-dark)

    Whatever you select, click *Restore* when you're ready.
    Then go to the *Volumes* main pane, locate the volume you are restoring to, and click on its row to reveal all relevant details.

    ![Restoration to existing volume is complete](assets/backup-restore/shot-08_light.png#only-light)
    ![Restoration to existing volume is complete](assets/backup-restore/shot-08_dark.png#only-dark)

    The *Status* parameter starts as *restoring-backup,* and when the restore process completes it becomes *available.*

=== "OpenStack CLI"
    Assume you want to restore the `my-vol-enc-backup` backup to the existing `my-vol-enc` volume.
    Make sure the target volume is at least as large as the backup, and use the `openstack volume backup restore` command with the `--force` switch:

    ```console
    $ openstack volume backup restore my-vol-enc-backup my-vol-enc --force
    +-------------+--------------------------------------+
    | Field       | Value                                |
    +-------------+--------------------------------------+
    | id          | 6f67acf4-e040-41c0-802e-939b9964dcef |
    | volume_id   | 681ceb2d-b0c5-4457-88af-e79b3b3009e6 |
    | volume_name | my-vol-enc                           |
    +-------------+--------------------------------------+
    ```

    Right after you enter the command above, check the status of `my-vol-enc`:

    ```console
    $ openstack volume show my-vol-enc -c status
    +--------+------------------+
    | Field  | Value            |
    +--------+------------------+
    | status | restoring-backup |
    +--------+------------------+
    ```

    Wait a few minutes and re-check.
    As soon as the restoration is complete, the status becomes `available`:

    ```console
    $ openstack volume show my-vol-enc -c status
    +--------+-----------+
    | Field  | Value     |
    +--------+-----------+
    | status | available |
    +--------+-----------+
    ```

