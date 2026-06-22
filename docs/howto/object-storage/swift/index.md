# Swift API

[OpenStack Swift](https://docs.openstack.org/swift/) (not to be confused with [the programming language of the same name](https://en.wikipedia.org/wiki/Swift_(programming_language))) is an object-access API similar to, but distinct from, the [S3](../s3/index.md) object storage API.

In {{brand}}, you interact with the Swift API using either the `swift` command-line interface (CLI), or the standard `openstack` CLI.

Either way, [in addition to installing and configuring the Python `openstackclient` module](../../getting-started/enable-openstack-cli.md), you need to install the Python `swiftclient` module.
Use either the package manager of your operating system, or `pip`:

=== "Debian/Ubuntu"
    ```bash
    apt install python3-swiftclient
    ```
=== "Mac OS X with Homebrew"
    This Python module is unavailable via `brew`, but you can
    install it via `pip`.
=== "Python Package"
    ```bash
    pip install cleura-openstackclient
    ```

## Availability

The OpenStack Swift API is available in select {{brand}} regions.
Refer to [the feature support matrix](../../../reference/features/index.md) for details on Swift API availability.
