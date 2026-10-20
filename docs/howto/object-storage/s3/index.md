# S3 API

[S3](https://en.wikipedia.org/wiki/Amazon_S3) is an object-access API based on HTTP and HTTPS.

In {{brand}}, you interact with the S3 API using either the `s3cmd` command-line interface (CLI), the MinIO client CLI (`mc`), or the standard `aws` CLI.

Either way, [in addition to installing and configuring the Python `openstackclient` module](../../getting-started/enable-openstack-cli.md), you need to install one of the aforementioned utilities.

=== "Debian/Ubuntu"
    ```bash
    apt install s3cmd aws
    ```
=== "Mac OS X with Homebrew"
    ```bash
    brew install minio-mc s3cmd
    ```
=== "Python Package"
    ```bash
    pip install s3cmd
    ```

## Availability

The S3 API is available in select {{brand}} regions.
Refer to [the feature support matrix](../../../reference/services/features/index.md) for details on S3 API availability.
