# DNS (Designate)

**[Designate](https://docs.openstack.org/designate/latest)** is OpenStack's DNS-as-a-Service solution.
In {{brand}}, you may use Designate for the following purposes:

* [Defining zones](zones.md),
* [Managing resource record sets](recordsets.md).

Managing PTR records with Designate is currently not supported in {{brand}}.

To work with Designate, you need the OpenStack CLI and also [an account](../../getting-started/create-account.md) in {{brand}}.
Additionally, make sure you have [enabled OpenStack CLI](../../getting-started/enable-openstack-cli.md) for the region you will be working in.

Along with the Python `openstackclient` module, you will need the Python `designateclient` module.
For that, use either the package manager of your operating system, or `pip`:

=== "Debian/Ubuntu"
    ```bash
    apt install python3-designateclient
    ```
=== "Mac OS X with Homebrew"
    This particular Python module is unavailable via `brew`, but you can install it via `pip`.
=== "Python Package"
    ```bash
    pip install cleura-openstackclient
    ```
