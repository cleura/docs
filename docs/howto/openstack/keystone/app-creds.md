---
description: A walk-through of creating and managing application credentials
---
# Application credentials

You can create application credentials and thus enable your applications to use them to authenticate against OpenStack Keystone.
Thanks to this type of credentials, you do not have to resort to your user credentials.
Applications can still authenticate using the application credentials ID along with a secret string, which has **nothing** to do with your user password.
That way, this sensitive piece of information does not have to be embedded in any particular application configuration.

One major security feature of application credentials is their capacity for expiration.
More often than not, application credentials are made to automatically expire after a certain date and time.
Passwords, on the other hand, persist essentially forever --- unless they are invalidated manually.

## Prerequisites

In {{brand}}, you manage application credentials with the OpenStack CLI, so make sure to [enable it](../../getting-started/enable-openstack-cli.md) for the region you are interested in.

## Creating application credentials

To create new application credentials with an expiration date, decide on a name and then use the `openstack` client like so:

```console
$ openstack application credential create --expiration '2024-04-30T12:00:00' angry_lamarr

+--------------+-----------------------------------------------------------------------------------+
| Field        | Value                                                                             |
+--------------+-----------------------------------------------------------------------------------+
| description  | None                                                                              |
| expires_at   | 2024-04-30T12:00:00.000000                                                        |
| id           | 98a2804b2d294b6784ae30ec67697382                                                  |
| name         | angry_lamarr                                                                      |
| project_id   | dfc700467396428bacba4376e72cc3e9                                                  |
| roles        | creator reader swiftoperator load-balancer_member member                          |
| secret       | BGXRFpTtEeh6Wi2MsohpFajz5V6ZVGMELjzH8gn53M1SD0voaOEYKlZsmtgO346FqONCHb0bEyt1wnUcv |
|              | PYYzA                                                                             |
| system       | None                                                                              |
| unrestricted | False                                                                             |
| user_id      | e50719d594f84f16ad13f88da540f762                                                  |
+--------------+-----------------------------------------------------------------------------------+
```

> The `--expiration` parameter accepts [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) strings, used for specifying date and time-related data.

In the example above, we chose the name `angry_lamarr`.
Also, a secret has been automatically generated for us.
Keep in mind that secrets are displayed only once, upon creation of the application credentials.

You may instead create a secret yourself and indicate it to the `openstack application credential create` command, like in the example below:

```console
$ PRETTY_GOOD_SECRET="$(pwgen -Bcns 24 1)"
$ openstack application credential create --expiration '2024-05-31T18:30:00' --secret $PRETTY_GOOD_SECRET elated_jones

+--------------+----------------------------------------------------------+
| Field        | Value                                                    |
+--------------+----------------------------------------------------------+
| description  | None                                                     |
| expires_at   | 2024-05-31T18:30:00.000000                               |
| id           | a39676b7b0bd4c0c84fa06bdde44b090                         |
| name         | elated_jones                                             |
| project_id   | dfc700467396428bacba4376e72cc3e9                         |
| roles        | creator reader swiftoperator load-balancer_member member |
| secret       | afduKgbMoqvf4UXyvYJAsWXN                                 |
| system       | None                                                     |
| unrestricted | False                                                    |
| user_id      | e50719d594f84f16ad13f88da540f762                         |
+--------------+----------------------------------------------------------+
```

When creating new application credentials, you may optionally provide a description.
You can do that using the `--description` parameter, like in the example below:

```console
$ openstack application credential create \
    --description 'Seasonal route between GOH, YFB' \
    --expiration '2024-08-31T23:59:59' \
    -f yaml goofy_dijkstra

description: Seasonal route between GOH, YFB
expires_at: '2024-08-31T23:59:59.000000'
id: 43649f148bbe46ab8f1d745eea095db9
name: goofy_dijkstra
project_id: dfc700467396428bacba4376e72cc3e9
roles: swiftoperator load-balancer_member reader creator member
secret: XS7YUGrH_FGZG9cEjT75tEYB7ciu-3YHgCWOoguTV3sezww8n8xcq67ae_4phzoL_vLY2ryp6avcy6eG8ihiMA
system: null
unrestricted: false
user_id: e50719d594f84f16ad13f88da540f762
```

Note that we opted for a YAML-formatted output, for this format makes it very easy to select the secret and copy it.

## Listing and viewing application credentials

To list all application credentials you have created, type the following:

```console
$ openstack application credential list

+-------------------+----------------+-------------------+-------------------+---------------------+
| ID                | Name           | Project ID        | Description       | Expires At          |
+-------------------+----------------+-------------------+-------------------+---------------------+
| 98a2804b2d294b678 | angry_lamarr   | dfc700467396428ba | None              | 2024-04-            |
| 4ae30ec67697382   |                | cba4376e72cc3e9   |                   | 30T12:00:00.000000  |
| a39676b7b0bd4c0c8 | elated_jones   | dfc700467396428ba | None              | 2024-05-            |
| 4fa06bdde44b090   |                | cba4376e72cc3e9   |                   | 31T18:30:00.000000  |
| 43649f148bbe46ab8 | goofy_dijkstra | dfc700467396428ba | Seasonal route    | 2024-08-            |
| f1d745eea095db9   |                | cba4376e72cc3e9   | between GOH, YFB  | 31T23:59:59.000000  |
+-------------------+----------------+-------------------+-------------------+---------------------+
```

You may select specific columns...

```console
$ openstack application credential list -c ID -c Name -c "Expires At"

+----------------------------------+----------------+----------------------------+
| ID                               | Name           | Expires At                 |
+----------------------------------+----------------+----------------------------+
| 98a2804b2d294b6784ae30ec67697382 | angry_lamarr   | 2024-04-30T12:00:00.000000 |
| a39676b7b0bd4c0c84fa06bdde44b090 | elated_jones   | 2024-05-31T18:30:00.000000 |
| 43649f148bbe46ab8f1d745eea095db9 | goofy_dijkstra | 2024-08-31T23:59:59.000000 |
+----------------------------------+----------------+----------------------------+
```

...or choose a different output format, like JSON:

```console
$ openstack application credential list -f json

[
  {
    "ID": "98a2804b2d294b6784ae30ec67697382",
    "Name": "angry_lamarr",
    "Project ID": "dfc700467396428bacba4376e72cc3e9",
    "Description": null,
    "Expires At": "2024-04-30T12:00:00.000000"
  },
  {
    "ID": "a39676b7b0bd4c0c84fa06bdde44b090",
    "Name": "elated_jones",
    "Project ID": "dfc700467396428bacba4376e72cc3e9",
    "Description": null,
    "Expires At": "2024-05-31T18:30:00.000000"
  },
  {
    "ID": "43649f148bbe46ab8f1d745eea095db9",
    "Name": "goofy_dijkstra",
    "Project ID": "dfc700467396428bacba4376e72cc3e9",
    "Description": "Seasonal route between GOH, YFB",
    "Expires At": "2024-08-31T23:59:59.000000"
  }
]
```

You can view specific application credentials like so:

```console
$ openstack application credential show goofy_dijkstra

+--------------+----------------------------------------------------------+
| Field        | Value                                                    |
+--------------+----------------------------------------------------------+
| description  | Seasonal route between GOH, YFB                          |
| expires_at   | 2024-08-31T23:59:59.000000                               |
| id           | 43649f148bbe46ab8f1d745eea095db9                         |
| name         | goofy_dijkstra                                           |
| project_id   | dfc700467396428bacba4376e72cc3e9                         |
| roles        | swiftoperator reader member creator load-balancer_member |
| system       | None                                                     |
| unrestricted | False                                                    |
| user_id      | e50719d594f84f16ad13f88da540f762                         |
+--------------+----------------------------------------------------------+
```

No matter how you choose to list or view application credentials, secrets are never displayed.

## Restricted vs unrestricted credentials

By default, application credentials are created as being *restricted*.
That is why, in the `openstack application credential show` output above, the `unrestricted` parameter is set to `False`.
You cannot use restricted application credentials for Heat, or for managing other application credentials or [trusts](https://docs.openstack.org/keystone/latest/user/trusts.html).
This restricted-by-default policy acts as a safeguard, so compromised application credentials cannot be used for creating other sets of application credentials.
If your application **has** to be able to perform such actions, and you accept the risks involved, you may create *unrestricted* application credentials like this:

```console
$ openstack application credential create --expiration '2024-02-15T23:59:59' modest_mccarthy --unrestricted

+--------------+---------------------------------------------------------------+
| Field        | Value                                                         |
+--------------+---------------------------------------------------------------+
| description  | None                                                          |
| expires_at   | 2024-02-15T23:59:59.000000                                    |
| id           | c3505060e42542a29ce1b77435112590                              |
| name         | modest_mccarthy                                               |
| project_id   | dfc700467396428bacba4376e72cc3e9                              |
| roles        | creator reader swiftoperator load-balancer_member member      |
| secret       | qsV9G-qklvbZ8Fz5m7arghW7hHYDRCYWE3vim5dm3-EcXgQn-             |
|              | pkvrDAOAW5nR7vfj32_HwtQbLjq0TyWM-gETg                         |
| system       | None                                                          |
| unrestricted | True                                                          |
| user_id      | e50719d594f84f16ad13f88da540f762                              |
+--------------+---------------------------------------------------------------+
```

In the example output above, the `unrestricted` parameter is set to `True`.

## Using application credentials

One way to use application credentials is by instantiating certain `OS_` variables.
Then, you may work with the OpenStack CLI as you typically do.
Let us see how you can go about this, by first creating a new set of application credentials:

```console
$ PRETTY_GOOD_SECRET="$(pwgen -Bcns 32 1)"
$ openstack application credential create --expiration '2024-02-29T23:59:59' practical_swanson --secret $PRETTY_GOOD_SECRET
$ openstack application credential show practical_swanson

+--------------+----------------------------------------------------------+
| Field        | Value                                                    |
+--------------+----------------------------------------------------------+
| description  | None                                                     |
| expires_at   | 2024-02-29T23:59:59.000000                               |
| id           | 3e04d504d754445e8b8d503e0e7af3c5                         |
| name         | practical_swanson                                        |
| project_id   | dfc700467396428bacba4376e72cc3e9                         |
| roles        | swiftoperator reader member creator load-balancer_member |
| system       | None                                                     |
| unrestricted | False                                                    |
| user_id      | e50719d594f84f16ad13f88da540f762                         |
+--------------+----------------------------------------------------------+
```

You need to instantiate four `OS_` variables:

* `OS_AUTH_URL`, which, in our example, is set to `https://{{api_region|lower}}.{{api_domain}}:5000`,
* `OS_AUTH_TYPE`, which should be set to `v3applicationcredential`,
* `OS_APPLICATION_CREDENTIAL_ID`, which should be set to the value of `id` (as displayed in the table above),
* `OS_APPLICATION_CREDENTIAL_SECRET`, which should be set to `$PRETTY_GOOD_SECRET`.

> Instead of `OS_APPLICATION_CREDENTIAL_ID`, you may instead initialize `OS_APPLICATION_CREDENTIAL_NAME` by simply setting it to the name of the application credentials.
> That way, you will not have to bother with the application credentials ID.

Create a new file named `acRC`, with the following content:

```bash
export OS_AUTH_URL=https://{{api_region|lower}}.{{api_domain}}:5000
export OS_AUTH_TYPE=v3applicationcredential
export OS_APPLICATION_CREDENTIAL_ID=3e04d504d754445e8b8d503e0e7af3c5
export OS_APPLICATION_CREDENTIAL_SECRET=<value_of_PRETTY_GOOD_SECRET>
```

In your setup, replace the values of `OS_AUTH_URL`, `OS_APPLICATION_CREDENTIAL_ID`, and `OS_APPLICATION_CREDENTIAL_SECRET` accordingly.

Next, switch to a new local environment (e.g., start a new shell), where **none** of the variables in your OpenStack RC file is initialized.
There, source the `acRC` file you just created:

```console
source acRC
```

You can now use the `openstack` client as usual.
One example:

```console
$ openstack token issue -f yaml

expires: 2024-01-23T22:40:49+0000
id: vgAAAAABlr5exIHPqjgksbMfmbdg24xN7uqLHLm4...
project_id: dfc700467396428bacba4376e72cc3e9
user_id: e50719d594f84f16ad13f88da540f762
```

## Troubleshooting application credentials usage

Having created a fresh set of application credentials to use with OpenStack CLI, you may find out that the `openstack` client starts behaving like its privileges are suddenly limited.
Any command you might try will fail, returning an error like in the following example:

```console
$ openstack token issue

Error authenticating with application credential: Application credentials cannot request a scope. (HTTP 401) (Request-ID: req-d59edba0-2cb5-450b-83c7-f094bd8e5654)
```

This happens because either of the `OS_PROJECT_NAME` or `OS_TENANT_NAME` variables is initialized, causing the `openstack` client to request a project scope for your token --- and that is not allowed.

This is why we advised making sure no pre-existing `OS_` variable is set *before* initializing the four `OS_` variables `openstack` needs, in order to use your application credentials.

You might want to add this function to your `.bashrc`:

```bash
function unset_os_vars() {
    unset -v `env | grep -o "^OS_[^=]*"`
}
```

From then on, you can unset all `OS_` variables by simply typing `unset_os_vars`.

## Deleting application credentials

If there are application credentials you suspect are compromised or simply do not need anymore, you may go ahead and delete them by specifying the corresponding ID or name, like so:

```console
$ openstack application credential delete goofy_dijkstra
$ openstack application credential show goofy_dijkstra

No applicationcredential with a name or ID of 'goofy_dijkstra' exists.
```

Even though expired application credentials can no longer be used for authentication, they stay around until you explicitly delete them.

