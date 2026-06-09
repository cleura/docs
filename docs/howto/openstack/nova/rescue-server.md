---
description: How to access a server in rescue mode
---
# Rescuing a server

This guide walks you through the required steps for accessing a server in [rescue mode](https://docs.openstack.org/nova/latest/user/rescue.html).

When you boot a server into rescue mode, you can then access its boot disk to fix a corrupted file system, reset access credentials, or perform other emergency recovery tasks.


## Prerequisites

You can boot a server into rescue mode by using the {{gui}}.
If, on the other hand, you prefer to work with the OpenStack CLI, then make sure to properly [enable it first](../../getting-started/enable-openstack-cli.md).


## Initiating the rescue

=== "{{gui}}"
    Using the left-hand side navigation pane, bring into view the server you are interested in.

    ![Use the left-hand side navigation panel, reveal the "servers" central pane, and locate the server of interest](assets/rescue-server/left-side-panel_light.png#only-light)
    ![Use the left-hand side navigation panel, reveal the "servers" central pane, and locate the server of interest](assets/rescue-server/left-side-panel_dark.png#only-dark)

    Click the :material-dots-horizontal-circle: icon at the right-hand side of the server row.
    From the drop-down menu that appears, select _Rescue Server_.

    ![From the server's drop-down menu, select "rescue server"](assets/rescue-server/menu-list_light.png#only-light)
    ![From the server's drop-down menu, select "rescue server"](assets/rescue-server/menu-list_dark.png#only-dark)

    The rescue dialog window appears.
    Leave the default option, _Use System Rescue Image_, selected.
    Click the _Rescue_ button to proceed.

    ![Make sure the "use system rescue image" toggle is active, then click the "rescue" button](assets/rescue-server/rescue-button_light.png#only-light)
    ![Make sure the "use system rescue image" toggle is active, then click the "rescue" button](assets/rescue-server/rescue-button_dark.png#only-dark)

    The server starts rebooting into rescue mode.
    When it finishes booting, its status icon has an exclamation mark.

    ![The exclamation mark at the left indicates that the server has finihsed booting into rescue mode](assets/rescue-server/server-booted-into-rescue-mode_light.png#only-light)
    ![The exclamation mark at the left indicates that the server has finihsed booting into rescue mode](assets/rescue-server/server-booted-into-rescue-mode_dark.png#only-dark)

=== "OpenStack CLI"
    First, get the `id` of the server of interest.
    For example, use `openstack` like so:

    ```console
    $ openstack server show -c id <server_of_interest_name>
    +-------+--------------------------------------+
    | Field | Value                                |
    +-------+--------------------------------------+
    | id    | c9fb10a0-4de9-11f1-8eb0-c319c95cc812 |
    +-------+--------------------------------------+
    ```

    Then, find the `id` of a system rescue image:

    ```console
    $ openstack image list --tag system-rescue
    +--------------------------------------+---------------+--------+
    | ID                                   | Name          | Status |
    +--------------------------------------+---------------+--------+
    | bdf8030f-aa9d-44ba-afb9-bb1597ff1b2e | system-rescue | active |
    +--------------------------------------+---------------+--------+
    ```

    To boot the server of interest using the system rescue image, use the following command, substituting the correct `id` for the `system-rescue` image in your {{brand}} region:

    ```bash
    openstack server rescue \
      --image bdf8030f-aa9d-44ba-afb9-bb1597ff1b2e \
      <server_id>
    ```

    For as long as the server is in rescue mode, the server's `OS-EXT-STS:vm_state` and `status` fields are set to `rescued` and `RESCUE` respectively:

    ```console
    $ openstack server show -c OS-EXT-STS:vm_state -c status <server_id>
    +---------------------+---------+
    | Field               | Value   |
    +---------------------+---------+
    | OS-EXT-STS:vm_state | rescued |
    | status              | RESCUE  |
    +---------------------+---------+
    ```

## Accessing the server in rescue mode

You can now proceed to accessing the remote console of your server, [as you would with any other active server](new-server.md#connecting-to-the-server-console).

Please refer to the [System Rescue documentation](https://www.system-rescue.org/manual/) for details on the available tools and features bundled with System Rescue.

## Bringing the server back to normal mode

=== "{{gui}}"

    Click the :material-dots-horizontal-circle: icon at the right-hand side of the server-in-rescue-mode row.
    From the drop-down menu that appears, select _Unrescue Server_.

    ![From the server-in-rescue drop-down menu, select "unrescue server"](assets/rescue-server/unrescue_light.png#only-light)
    ![From the server-in-rescue drop-down menu, select "unrescue server"](assets/rescue-server/unrescue_dark.png#only-dark)

=== "OpenStack CLI"

    Send the `unrescue` sub-command to the server, like so:

    ```
    $ openstack server unrescue <server_id>
    ```

In a few seconds, the server finishes rebooting into normal mode.
