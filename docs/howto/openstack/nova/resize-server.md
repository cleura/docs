---
description: How to adjust the number of CPU cores and amount of memory for a virtual server
---
# Resizing a server

This guide will walk you through the required steps to change the number of CPU cores and the amount of memory your server has access to, this is done by changing the server's [flavor](../../../reference/flavors/index.md).

[Resize](https://docs.openstack.org/nova/latest/admin/configuration/resize.html) (or Server resize) is the ability to change the flavor of a server, thus allowing it to upscale or downscale according to user needs.
A resize operation is a two-step process for the user:

1. Initiate the resize.
2. Either confirm (verify) success and release the old server, or declare a revert to release the new server and restart the old one.

## Prerequisites

You need to have a server you wish to resize.
Additionally, if you prefer to work with the OpenStack CLI, then make sure to properly [enable it first](../../getting-started/enable-openstack-cli.md).

## Listing available flavors

=== "{{gui}}"
    Navigate to the server list.

    ![In the left hand side navigation panel, select "compute" and then "servers"](assets/resize-server/01-left-side-panel_light.png#only-light)
    ![In the left hand side navigation panel, select "compute" and then "servers"](assets/resize-server/01-left-side-panel_dark.png#only-dark)

    Find the server you want to resize in the list.
    At the right-hand side of its row, click the :material-dots-horizontal-circle: icon.
    In the drop-down menu that appears, click on _Modify Server_.

    ![In the drop-down menu of the server you want to resize, click on "modify server"](assets/resize-server/02-menu-list_light.png#only-light)
    ![In the drop-down menu of the server you want to resize, click on "modify server"](assets/resize-server/02-menu-list_dark.png#only-dark)

    Near the top of the options panel, find the _Flavor_ section.
    See the current flavor used by the server.
    Expand the dropdown menu to get all available flavors.

    ![The server's current flavor](assets/resize-server/03-modify-server_light.png#only-light)
    ![The server's current flavor](assets/resize-server/03-modify-server_dark.png#only-dark)
=== "OpenStack CLI"
    To list all available flavors you can simply run `openstack flavor list`, but that will return a very long unsorted list, instead we recommend the following command:

    ```bash
    openstack flavor list -c Name -f value | grep '[0-9]c[0-9]' | sort -V
    ```

    The printout is a simple and clean list, sorted by the compute type, the number of cores and then by the amount of memory.

    ```plain
    b.1c1gb
    b.1c2gb
    b.1c4gb
    b.2c2gb
    b.2c4gb
    b.2c8gb
    b.2c16gb
    b.4c4gb
    ...
    ```

## Initiating the resize

Choose a new flavor that you want your server to use instead.

> A resize is only possible with [flavors](../../../reference/flavors/index.md) using the same prefix letter. Most commonly you will have a `b.` flavor, thus you must select another `b.` flavor.

=== "{{gui}}"
    As soon as you select a new flavor, the _Resize_ button appears.

    ![The server's new flavor](assets/resize-server/04-resize-button_light.png#only-light)
    ![The server's new flavor](assets/resize-server/04-resize-button_dark.png#only-dark)

    Click on it to start the resize.

    While the resize is ongoing, you see a spinning circle and the message "Resize is in progress".

    ![Server resize operation in progress](assets/resize-server/05-resize-in-progress_light.png#only-light)
    ![Server resize operation in progress](assets/resize-server/05-resize-in-progress_dark.png#only-dark)
=== "OpenStack CLI"
    To start the resize use the following command:

    ```bash
    openstack server resize --flavor <new_flavor> <server_id>
    ```

    While the resize is ongoing the server should have the `OS-EXT-STS:task_state` of `resize_migrating` and the `status` of `RESIZE`.

    ```bash
    openstack server show -c OS-EXT-STS:task_state -c OS-EXT-STS:vm_state -c status <server_id>
    ```

    ```plain
    +-----------------------+------------------+
    | Field                 | Value            |
    +-----------------------+------------------+
    | OS-EXT-STS:task_state | resize_migrating |
    | OS-EXT-STS:vm_state   | active           |
    | status                | RESIZE           |
    +-----------------------+------------------+
    ```

    You may proceed with the next step once your server status is `VERIFY_RESIZE`.

    ```plain
    +-----------------------+---------------+
    | Field                 | Value         |
    +-----------------------+---------------+
    | OS-EXT-STS:task_state | None          |
    | OS-EXT-STS:vm_state   | resized       |
    | status                | VERIFY_RESIZE |
    +-----------------------+---------------+
    ```

The resize process might take a minute or more.
{{brand}} will now make a restore point in case the resize process fails.
It would then restore your server to the state it was before the resize.

## Confirming the resize

Your server is now using the new flavor you selected earlier, and you need to make sure the server is working as intended after the resize.

Once you are certain your server is working as intended, you should confirm the resize.
If you do not confirm the resize, your server will automatically have the resize confirmed after 24 hours.

=== "{{gui}}"
    This is done by clicking the _Confirm_ button.

    ![Confirm or cancel the server resize attempt](assets/resize-server/06-resize-confirm_light.png#only-light)
    ![Confirm or cancel the server resize attempt](assets/resize-server/06-resize-confirm_dark.png#only-dark)

    > If your server is not working as intended, or you simply regret the resize, instead click _Cancel_.
=== "OpenStack CLI"
    This is done by using the following command:

    ```bash
    openstack server resize confirm <server_id>
    ```

    Alternatively, if your server is not working as intended, revert the resize with the following command:

    ```bash
    openstack server resize revert <server_id>
    ```

This concludes the process of resizing a server in {{brand}}.
