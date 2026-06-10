---
description: How to put a new server behind a Clavister NetWall instance
---

# Creating servers behind a Clavister NetWall instance

Provided you have a [Clavister NetWall instance](../../marketplace/clavister/deploy.md) up and running, you may use the {{gui}} to create a new server and place it behind the firewall.

## Creating a new server

You may follow our [server creation guide](new-server.md) using the {{gui}} or the OpenStack CLI *almost* to the letter.
You should only pay *extra* attention to the region the new server will reside in and the network it will be connected to.

More specifically, the new server must be in the region where the Clavister NetWall instance you are interested in resides.

=== "{{gui}}"

    After you type in the new server's name, choose its region from the drop-down menu named *Region*.

    ![Select a region for the new server](assets/new-server-cnw/new-server-cnw-01_light.png#only-light)
    ![Select a region for the new server](assets/new-server-cnw/new-server-cnw-01_dark.png#only-dark)

=== "OpenStack CLI"

    Make sure you have sourced an [RC file](../../getting-started/enable-openstack-cli.md#sourcing-the-rc-file) from the same region the Clavister NetWall instance belongs to.

In addition to residing in the correct region, the server must also be in a network behind the Clavister NetWall instance.

=== "{{gui}}"

    While creating your new server, use the *Networks* drop-down menu to select a network.

    ![Select a network for the new server](assets/new-server-cnw/new-server-cnw-02_light.png#only-light)
    ![Select a network for the new server](assets/new-server-cnw/new-server-cnw-02_dark.png#only-dark)

=== "OpenStack CLI"

    In the `openstack` CLI client, use the `--network` parameter to specify a network to which the server will be connected.
    For instance, here is how to create a server named `gostenhof`, connected to a network named `inside-net`, which is behind a Clavister NetWall instance:

    ```bash
    openstack server create \
        --flavor b.1c1gb \
        --image "Ubuntu 24.04 Noble Numbat x86_64" \
        --boot-from-volume 20 \
        --network inside-net \
        --security-group default \
        --key-name my-public-key  \
        --wait \
        gostenhof
    ```

## Getting network connectivity information

=== "{{gui}}"

    Make sure the vertical pane on the left-hand side of the page is expanded.
    From it, select *Compute*, then *Servers*.
    In the central pane, select the region in which your new server resides.
    Click on the server row to expand it, and go to the *Addresses* tab.

    ![View server connectivity information](assets/new-server-cnw/new-server-cnw-03_light.png#only-light)
    ![View server connectivity information](assets/new-server-cnw/new-server-cnw-03_dark.png#only-dark)

    There, you can see the server's IP address.
    You might also want to jot down the corresponding MAC address.

=== "OpenStack CLI"

    To get the IP of the `gostenhof` server, type:

    ```console
    $ openstack server show gostenhof -c addresses
    +-----------+---------------------------+
    | Field     | Value                     |
    +-----------+---------------------------+
    | addresses | inside-net=192.168.201.47 |
    +-----------+---------------------------+
    ```

    Also, you may want to take note of the server's network adapter MAC address:

    ```console
    $ openstack port list --server gostenhof -c 'MAC Address' -c Status
    +-------------------+--------+
    | MAC Address       | Status |
    +-------------------+--------+
    | fa:16:3e:e8:75:7c | ACTIVE |
    +-------------------+--------+
    ```

## Viewing the new server from the Clavister NetWall dashboard

Login to the Clavister NetWall instance.
From the left-hand side vertical pane, make sure you have expanded the *Run-time Information* category.
Go to the *SUB SYSTEMS* sub-category and select *Neighbor Devices*.
The firewall has two network interfaces: `if1` is the external interface, and `if2` is the internal interface, which any server behind the firewall faces.

![View Clavister NetWall neighbor devices](assets/new-server-cnw/new-server-cnw-04.png)

You will notice the IP address of the new server you just spun up and its network adapter MAC address.
Finally, in the *Status* column, there is a box labeled *ACTIVE*, indicating that the server is accessible to the firewall.
