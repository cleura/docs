---
description: How to create, upload, examine, duplicate, and delete SSH keypairs
---
# Managing SSH keypairs

You can use the {{gui}} or the OpenStack CLI, and by default create [Ed25519](https://en.wikipedia.org/wiki/EdDSA#Ed25519) keypairs.

??? "Using other key types"
    Due to an application's requirements, you might have to generate a keypair that employs older key types, like the ones based on the [RSA](https://en.wikipedia.org/wiki/RSA_cryptosystem) or the [DSA](https://en.wikipedia.org/wiki/Digital_Signature_Algorithm) cryptosystem.

    In cases like these, use an external tool such as `ssh-keygen` to create a keypair with the required characteristics.
    Then, when instantiating the new keypair, specify the corresponding public key you obtained from the external tool.

## Prerequisites

If you prefer to use the OpenStack CLI, please be sure to [enable it first](../../getting-started/enable-openstack-cli.md).

## Creating keypairs

=== "{{gui}}"
    In the left-hand side vertical pane of the {{gui}}, select _Compute_ and then _KeyPairs_.
    All existing keypairs appear in the central pane, named _Compute_ / _Keypairs_.
    To create a new one, click the _Add new Keypair_ link at the top right.

    ![All available keypairs](assets/keypairs/keypair-01_light.png#only-light)
    ![All available keypairs](assets/keypairs/keypair-01_dark.png#only-dark)

    A window titled _Create Keypair_ slides over from the right side of the browser window.
    Enter a _Name_ for the new keypair, and select a _Region_ for it.

    ![Create a new keypair without specifying a public key](assets/keypairs/keypair-02_light.png#only-light)
    ![Create a new keypair without specifying a public key](assets/keypairs/keypair-02_dark.png#only-dark)

    Without pasting anything in the _Public Keys_ text field, you can already instantiate the new keypair by clicking the _Create_ button.
    Alternatively, you may want to paste one of your public keys in the _Public Keys_ text field.

    In the example below, in the _Public Keys_ field, we have pasted the public key of an Ed25519 keypair.

    ![Before instantiating a new keypair, you may provide a public SSH key of yours](assets/keypairs/keypair-03_light.png#only-light)
    ![Before instantiating a new keypair, you may provide a public SSH key of yours](assets/keypairs/keypair-03_dark.png#only-dark)

    You can paste two or more public keys in the _Public Keys_ field, one per line.

    ![You may provide more than one of your public keys, one in a separate line](assets/keypairs/keypair-04_light.png#only-light)
    ![You may provide more than one of your public keys, one in a separate line](assets/keypairs/keypair-04_dark.png#only-dark)

    Whenever you choose not to provide a public key, right after creating the new keypair, a window named _Private Key_ pops up.
    From it, you can either download the private key of the keypair or copy it to the clipboard.
    In any case, you should securely store it and make it accessible to your local user only.

    ![Whenever you create a new keypair without specifying a public key, you have to download and securely store the corresponding private key](assets/keypairs/keypair-05_light.png#only-light)
    ![Whenever you create a new keypair without specifying a public key, you have to download and securely store the corresponding private key](assets/keypairs/keypair-05_dark.png#only-dark)

    After you create the new keypair, you can see it listed in its region.

    ![The new keypair is listed under its region](assets/keypairs/keypair-06_light.png#only-light)
    ![The new keypair is listed under its region](assets/keypairs/keypair-06_dark.png#only-dark)

=== "OpenStack CLI"
    The simplest way to create a new keypair is by using the `openstack keypair create` command, like in the example below:

    ```console
    $ openstack keypair create my-new-keypair

    -----BEGIN OPENSSH PRIVATE KEY-----
    b3Bl........................................................................
    ........................................................................c2gt
    ZWQy........................................................................
    ........................................................................TXAA
    AAEC....
    -----END OPENSSH PRIVATE KEY-----
    ```

    The command output includes the private key of the `my-new-keypair` keypair.
    You may __not__ want the private key displayed on the terminal, so instead of the command above, use something like this:

    ```console
    $ openstack keypair create --private-key my-priv-key my-new-keypair

    +-------------+-------------------------------------------------+
    | Field       | Value                                           |
    +-------------+-------------------------------------------------+
    | created_at  | None                                            |
    | fingerprint | 3c:90:f1:14:07:50:d4:0e:81:66:03:96:7f:5e:00:2e |
    | id          | my-new-keypair                                  |
    | is_deleted  | None                                            |
    | name        | my-new-keypair                                  |
    | type        | ssh                                             |
    | user_id     | e507abcdef19d594f84f16ad13f88pqrstuxyz          |
    +-------------+-------------------------------------------------+
    ```

    In that case, in the terminal output, you only see general information regarding `my-new-keypair`, and the private key is automatically downloaded onto the `my-priv-key` file:

    ```console
    $ file my-priv-key
    my-priv-key: OpenSSH private key
    ```

    As with any other private key, you should securely store the one `openstack keypair create` generates, and make it accessible to your local user only.

    You may also create a keypair by specifying a public key of yours, using the `--public-key` parameter.
    Example:

    ```console
    $ openstack keypair create --public-key ~/.ssh/id_ecdsa.pub my-new-keypair

    +-------------+-------------------------------------------------+
    | Field       | Value                                           |
    +-------------+-------------------------------------------------+
    | created_at  | None                                            |
    | fingerprint | 01:7f:95:8c:16:6d:03:d9:0e:b1:d6:94:b4:7b:bd:de |
    | id          | my-new-keypair                                  |
    | is_deleted  | None                                            |
    | name        | my-new-keypair                                  |
    | type        | ssh                                             |
    | user_id     | e507abcdef19d594f84f16ad13f88pqrstuxyz          |
    +-------------+-------------------------------------------------+
    ```

    In that case, you do not get to download the private key of the `my-new-keypair` keypair.

## Viewing keypair details

=== "{{gui}}"
    To get more details on a specific keypair, go to the _Compute_ / _KeyPairs_ pane, locate the keypair of interest, and click on its row.

    ![Viewing keypair details](assets/keypairs/keypair-07_light.png#only-light)
    ![Viewing keypair details](assets/keypairs/keypair-07_dark.png#only-dark)

=== "OpenStack CLI"
    Before viewing information of a specific keypair, you might want to list all keypairs in the region you are working in.
    For that, use the `openstack keypair list` command:

    ```console
    $ openstack keypair list

    +----------------+-------------------------------------------------+------+
    | Name           | Fingerprint                                     | Type |
    +----------------+-------------------------------------------------+------+
    | bahnhof        | 7a:97:fa:34:5c:80:55:06:41:bb:e9:77:14:3d:04:fb | ssh  |
    | karlskrona     | ef:43:46:3c:44:96:a9:70:67:e6:3c:9b:c5:21:cf:2e | ssh  |
    | my-new-keypair | 01:7f:95:8c:16:6d:03:d9:0e:b1:d6:94:b4:7b:bd:de | ssh  |
    | puvirnituq     | 3c:39:f0:d5:6b:04:4b:ab:c9:86:97:f3:59:1d:23:f8 | ssh  |
    +----------------+-------------------------------------------------+------+
    ```

    Now, to get detailed information regarding the `my-new-keypair` keypair, use the `openstack keypair show` command like so:

    ```console
    $ openstack keypair show my-new-keypair

    +-------------+-------------------------------------------------+
    | Field       | Value                                           |
    +-------------+-------------------------------------------------+
    | created_at  | 2026-05-28T17:24:54.000000                      |
    | fingerprint | 01:7f:95:8c:16:6d:03:d9:0e:b1:d6:94:b4:7b:bd:de |
    | id          | my-new-keypair                                  |
    | is_deleted  | False                                           |
    | name        | my-new-keypair                                  |
    | private_key | None                                            |
    | type        | ssh                                             |
    | user_id     | e50719d594f84f16ad13f88da540f762                |
    +-------------+-------------------------------------------------+
    ```

## Duplicating keypairs

You may want to use the same SSH key for authentication in multiple {{brand}} regions.
To do so, you can duplicate your keypairs.

=== "{{gui}}"
    First off, go to the _Compute_ / _KeyPairs_ pane and locate the keypair you wish to duplicate to other regions.
    At the right of the keypair row, click the :material-dots-horizontal-circle: icon.
    From the pop-up menu that appears, select _Duplicate Keypair_.

    ![Select the option for duplicating a keypair](assets/keypairs/keypair-08_light.png#only-light)
    ![Select the option for duplicating a keypair](assets/keypairs/keypair-08_dark.png#only-dark)

    A window named _Duplicate Keypair_ slides over.
    Use the toggle buttons to indicate the regions you wish to duplicate the keypair to.
    When you are ready, click the _Duplicate_ button.

    ![Indicate the regions you wish to duplicate the keypair to, then click the Duplicate button](assets/keypairs/keypair-09_light.png#only-light)
    ![Indicate the regions you wish to duplicate the keypair to, then click the Duplicate button](assets/keypairs/keypair-09_dark.png#only-dark)

    You now see your keypair under each region it is accessible from.

    ![Your keypair is now accessible from more then one regions](assets/keypairs/keypair-10_light.png#only-light)
    ![Your keypair is now accessible from more then one regions](assets/keypairs/keypair-10_dark.png#only-dark)

=== "OpenStack CLI"
    Let's assume you already have the `my-new-keypair` keypair in region `Fra1`, and now you wish to duplicate it (send it over) to region `Kna1`.

    ```console
    $ openstack keypair show my-new-keypair

    +-------------+-------------------------------------------------+
    | Field       | Value                                           |
    +-------------+-------------------------------------------------+
    | created_at  | 2026-05-29T12:43:50.000000                      |
    | fingerprint | 01:7f:95:8c:16:6d:03:d9:0e:b1:d6:94:b4:7b:bd:de |
    | id          | my-new-keypair                                  |
    | is_deleted  | False                                           |
    | name        | my-new-keypair                                  |
    | private_key | None                                            |
    | type        | ssh                                             |
    | user_id     | e50719d594f84f16ad13f88da540f762                |
    +-------------+-------------------------------------------------+
    ```

    First, save a copy of `my-new-keypair`'s public key onto a local file (e.g., `the-pubkey`):

    ```console
    $ openstack keypair show --public-key my-new-keypair > the-pubkey
    ```

    When the command above is successful, it produces no output.

    Next, [source your OpenStack credentials](../../getting-started/enable-openstack-cli.md#sourcing-the-rc-file) for region `Kna1`.

    Finally, create a new keypair named `my-new-keypair`, indicating `the-pubkey` file:

    ```console
    $ openstack keypair create --public-key ./the-pubkey my-new-keypair

    +-------------+-------------------------------------------------+
    | Field       | Value                                           |
    +-------------+-------------------------------------------------+
    | created_at  | None                                            |
    | fingerprint | 01:7f:95:8c:16:6d:03:d9:0e:b1:d6:94:b4:7b:bd:de |
    | id          | my-new-keypair                                  |
    | is_deleted  | None                                            |
    | name        | my-new-keypair                                  |
    | type        | ssh                                             |
    | user_id     | c096cf99f65a4d22a6954b67d2ec11d7                |
    +-------------+-------------------------------------------------+
    ```

    Notice the keypair fingerprint in both regions: it's the same.

## Deleting keypairs

=== "{{gui}}"
    In the _Compute_ / _KeyPairs_ pane, locate the keypair you wish to delete.
    At the right of the keypair row, click the :material-dots-horizontal-circle: icon.
    From the pop-up menu that appears, select _Delete Keypair_.

    ![Select the option for deleting a keypair](assets/keypairs/keypair-11_light.png#only-light)
    ![Select the option for deleting a keypair](assets/keypairs/keypair-11_dark.png#only-dark)

    A window appears, asking if you are sure you want to delete the keypair.
    If you are, click the _Yes, Delete_ button.

    ![Confirm that you want to delete the selected keypair](assets/keypairs/keypair-12_light.png#only-light)
    ![Confirm that you want to delete the selected keypair](assets/keypairs/keypair-12_dark.png#only-dark)

    The selected keypair is now deleted.
    Note that any duplicates, in other regions, are still available.

    ![The selected keypair is deleted, and any duplicates are still available](assets/keypairs/keypair-13_light.png#only-light)
    ![The selected keypair is deleted, and any duplicates are still available](assets/keypairs/keypair-13_dark.png#only-dark)

    If you want to delete more than one keypair at once, first go to the _Compute_ / _KeyPairs_ pane and select them.
    Then, click the :material-delete: icon at the top left.

    ![Choose more than one keypairs you wish to delete](assets/keypairs/keypair-14_light.png#only-light)
    ![Choose more than one keypairs you wish to delete](assets/keypairs/keypair-14_dark.png#only-dark)

    A window appears, asking if you are sure you want to delete the selected keypairs.
    Click the _Yes, Delete_ button to confirm, or the _No_ button if you changed your mind.

    ![Confirm that you want to delete the selected keypairs](assets/keypairs/keypair-15_light.png#only-light)
    ![Confirm that you want to delete the selected keypairs](assets/keypairs/keypair-15_dark.png#only-dark)

=== "OpenStack CLI"
    To delete a keypair, use the `openstack keypair delete` command.
    For instance, to delete the `my-new-keypair` keypair, type:

    ```console
    $ openstack keypair delete my-new-keypair
    ```

    When the command above is successful, it produces no output.

