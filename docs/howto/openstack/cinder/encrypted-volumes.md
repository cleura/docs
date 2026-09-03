---
description: Using Barbican secrets for block storage encryption, you can store data in persistent storage volumes in an encrypted fashion.
---
# Encrypted volumes

{{page.meta.description}}

That encryption is transparent to virtual machines (instances) that you attach the volume to.


## Creating an encrypted volume

To create an encrypted volume, you need to provide a specific *volume type.*
You can retrieve the list of available volume types with the following command:

```console
$ openstack volume type list
+--------------------------------------+------------------------+-----------+
| ID                                   | Name                   | Is Public |
+--------------------------------------+------------------------+-----------+
| f0887a44-4f43-44d6-b701-164d7a9c4b5b | cbs-premium-encrypted  | True      |
| b74f129c-1cbf-495e-b569-42ba35c34e22 | cbs-standard-encrypted | True      |
| 4404cc47-bcf7-4504-a9b2-61ae7610b52d | cbs-premium            | True      |
| 7838c4e6-0093-4343-8cb5-2a40d1c2e629 | cbs-standard           | True      |
+--------------------------------------+------------------------+-----------+
```

> In {{brand}}, all volume types that support encryption use the suffix `-encrypted`.

To create a volume with encryption, you need to explicitly specify the `--type` option to the `openstack volume create` command.
The following example creates a volume using the `cbs-standard-encrypted` type, naming it `enc_drive` and setting its size to 10 GiB:

```console
$ openstack volume create \
  --type cbs-standard-encrypted \
  --size 10 \
  enc_drive
+---------------------+--------------------------------------+
| Field               | Value                                |
+---------------------+--------------------------------------+
| attachments         | []                                   |
| availability_zone   | az1                                  |
| bootable            | false                                |
| consistencygroup_id | None                                 |
| created_at          | 2025-02-12T15:00:12.561263           |
| description         | None                                 |
| encrypted           | True                                 |
| id                  | ffcbb423-ea86-45bd-8ffd-9993e0c26aa9 |
| multiattach         | False                                |
| name                | enc_drive                            |
| properties          |                                      |
| replication_status  | None                                 |
| size                | 10                                   |
| snapshot_id         | None                                 |
| source_volid        | None                                 |
| status              | creating                             |
| type                | cbs-standard-encrypted               |
| updated_at          | None                                 |
| user_id             | cc19369079c6457fb04a1c9ac1d023d1     |
+---------------------+--------------------------------------+
```

When you create a volume, a one-off encryption key is also created.
This key works only with this volume and is stored in Barbican.

In other words, the key created for this volume cannot decrypt any other volume, except the one it was initially created for.


## Retrieving a volume’s encryption key

After you create an encrypted volume, you can retrieve a reference to the Barbican secret that represents its encryption key.
You do this with the following command:

```bash
openstack volume show \
  --os-volume-api-version 3.66 \
  -f value \
  -c encryption_key_id \
  enc_drive
```

Instead of the volume name, you can specify its UUID:

```bash
openstack volume show \
  --os-volume-api-version 3.66 \
  -f value \
  -c encryption_key_id \
  ffcbb423-ea86-45bd-8ffd-9993e0c26aa9
```


## Deleting an encrypted volume

When you decide you no longer need an encrypted volume and want to delete it, you can do so with the `openstack volume delete` command.
As long as you do this with the same user account that created the volume, the operation succeeds without further intervention.

However, if you are trying to delete a volume that was created by a different user, you’ll run into the limitation that the *secret* associated with the volume is owned by that other user.
As a result, deleting the encrypted volume with your own user credentials will fail.

There are two options to work around this limitation:

1. You can switch to the user credentials of the user that created the volume (assuming you have access to them) and proceed with the deletion.
2. You can ask the user that created the volume to [add you to the Access Control List (ACL) for the secret](../barbican/share-secret.md).
   This will let you read the secret and delete the volume using your own credentials.


## Block device encryption caveats

Once a volume is configured for encryption and is attached to an instance in {{brand}}, some caveats apply that you might want to keep in mind.

Sometimes, automatically or through administrator intervention, we move one of your instances to another physical machine.
This process is known as *live migration,* and it normally does not interrupt the instance’s functionality at all;
typically, neither you nor the application users notice that live migration has even happened.
This is common during routine upgrades of the {{brand}} platform within our pre-announced maintenance windows.

The same considerations apply to physical node failure.
If the physical machine running your instance fails, we can automatically recover it onto another machine — an action known as *evacuation.*

Live migration or evacuation *including encrypted volumes* does, however, require that whoever performs the migration also has **at least** read access to the volume’s encryption secret.

This means that you have two options:

1. If you *do* trust us to include your instances in live migrations and evacuations, even when they attach encrypted volumes, then you can [add](../barbican/share-secret.md) our [administrative account](../../../reference/volumes/index.md) to the Access Control List (ACL) for your secrets.
2. If you *don’t* want to share your secrets but you still want to use encrypted volumes, you should build your own mechanism or process (preferably automated) so that your instances recover in case they become non-functional.
