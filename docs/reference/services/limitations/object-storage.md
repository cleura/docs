# Object storage limitations

## Swift API

### Versioning

When using [object versioning](../../../howto/object-storage/swift/versioning.md) with the Swift API, only the `X-Versions-Location` header is supported.
In {{brand}}, there is no support for `X-History-Location`.

### `.rlistings` ACL element

In access control lists (ACLs) set on containers via the Swift API, the `.rlistings` [ACL element](https://docs.openstack.org/swift/latest/overview_acl.html#common-acl-elements) has no effect.
In a public container (one with one or more `.r:` elements in its ACL), any client that is able to retrieve objects is also able to list them.

### Container-to-container sync

In {{brand}}, there is no support for [container-to-container synchronization](https://docs.openstack.org/swift/latest/overview_container_sync.html).

## S3 API

### Bucket replication

There is currently no support for [S3 bucket replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html) in {{brand}}.

### Bucket notifications

There is currently no support for [S3 bucket notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html) in {{brand}}.

### Object lock retention modes

For buckets configured with [object lock](../../../howto/object-storage/s3/object-lock.md), the only supported retention mode is `COMPLIANCE`.
We do not support `GOVERNANCE` mode.

### SSE-KMS

There is currently no support for SSE-KMS in {{brand}}.
SSE-C, in contrast, [is fully supported](../../../howto/object-storage/s3/sse-c.md).

### Request checksum calculation

Due to changes in AWS SDKs in early 2025, uploading objects to {{brand}} object storage services may fail when using tools that depend on those SDKs.
Calls using the previously optional checksum requirement will fail because our backend storage doesn't recognize these requests.

This can be resolved by setting the environment variable `AWS_REQUEST_CHECKSUM_CALCULATION` to `WHEN_REQUIRED` or by changing the AWS CLI defaults.
Other tools can have similar options that can be changed to retain compatibility.

=== "aws"
    ```sh
    export AWS_REQUEST_CHECKSUM_CALCULATION=WHEN_REQUIRED
    ```

    or

    ```ini
    [default]
    request_checksum_calculation = WHEN_REQUIRED
    ```
    For better compatibility, ensure you're using a current version (>=2.23.5) of the AWS CLI that should accept `AWS_REQUEST_CHECKSUM_CALCULATION` environment variable and config options.

=== "Terraform/OpenTofu"
    Please disable checksums.
    ```terraform
    terraform {
      required_version = ">= 1.6.3"

      backend "s3" {
        endpoints = {
          s3 = "https://s3-{{api_region|lower}}.{{api_domain}}"
        }

      bucket = "<your_bucket_name>"
      key    = "<state_file_name>"

      # Deactivate a few AWS-specific checks
      skip_credentials_validation = true
      skip_requesting_account_id  = true
      skip_metadata_api_check     = true
      skip_region_validation      = true
      skip_s3_checksum            = true
      region                      = "us-east-1"
      }
    }
    ```
