---
description: Object lock enables you to keep S3 objects from being deleted or overwritten.
---
# Object lock


Object lock is a feature in S3 that enables you to lock your objects to prevent them from being deleted or overwritten.
This feature can be helpful when you want to maintain data integrity, comply with regulations, or retain data for a specific period.

Note that this feature is distinct from *object expiry*, which is covered in a [separate guide](expiry.md).

You should also keep in mind that object lock offers two methods for managing object retention: [Retention periods and Legal hold](../../../background/object-storage.md#object-lock).

## Prerequisites

In order to manage object lock, you must install `aws` or `mc`, and [configure it with working credentials](credentials.md).

You cannot (reliably) use `s3cmd` to manage this functionality.

## Enabling object lock

To use the object lock feature, you must first create a new bucket.

> Existing buckets cannot have object lock enabled.
> To enable object lock on existing data, you must first create a new bucket with object lock, and then sync your pre-existing objects into that bucket.

=== "aws"
    ```bash
    aws --profile {{api_region|lower}} \
      s3api create-bucket \
      --bucket <bucket-name> \
      --object-lock-enabled-for-bucket
    ```
=== "mc"
    ```bash
    mc mb {{api_region|lower}}/<bucket> \
      --with-lock
    ```

Note that this will enable [bucket versioning](versioning.md) as well.

## Configure the default object lock mode and retention period for a bucket

To configure your bucket to use the **Compliance** mode, use one of the following commands:

=== "aws"
    ```bash
    aws --profile {{api_region|lower}} \
      s3api put-object-lock-configuration \
      --bucket <bucket-name> \
      --object-lock-configuration \
      '{ "ObjectLockEnabled": "Enabled", "Rule": { "DefaultRetention": { "Mode": "COMPLIANCE", "Days": 30 }}}'
    ```
=== "mc"
    ```bash
    mc retention set \
      --default compliance 30d \
      {{api_region|lower}}/<bucket>
    ```
    > The `--default` parameter sets the default object lock settings for new objects, and is optional.

    > To specify a duration, use a string formatted as `Nd` for days or `Ny` for years.
    > For example, use `30d` to indicate 30 days after the object creation, or use `1y` to indicate 1 year after the object creation.

## Configure the object lock mode and retention period for a single object

If you want to set a specific retention period for an object, instead of using the default retention period, use one of the following commands.
You can also use these commands to update the retention period for an object:

=== "aws"
    ```bash
    aws --profile {{api_region|lower}} \
      s3api put-object-retention \
      --bucket <bucket-name> \
      --key <object-name> \
      --retention '{ "Mode": "COMPLIANCE", "RetainUntilDate": "2023-01-01T12:00:00.00Z" }'
    ```
    > For the value of the `RetainUntilDate` parameter, use the [ISO 8601 date-time representation](https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations) format.
=== "mc"
    ```bash
    mc retention set \
      COMPLIANCE 30d \
      {{api_region|lower}}/<bucket>/<object-name>
    ```
    > To specify a duration, use a string formatted as `Nd` for days or `Ny` for years.
    > For example, use `30d` to indicate 30 days after the object creation, or use `1y` to indicate 1 year after the object creation.

## Retrieve the object lock mode and retention period

### Bucket-level

To view the default object lock mode and retention period set on a bucket, use the following command:

=== "aws"
    ```bash
    aws --profile {{api_region|lower}} \
      s3api get-object-lock-configuration \
      --bucket <bucket-name>
    ```
    Example output:
    ```json
    {
      "ObjectLockConfiguration": {
        "ObjectLockEnabled": "Enabled",
        "Rule": {
          "DefaultRetention": {
            "Mode": "COMPLIANCE",
            "Days": 2
          }
        }
      }
    }
    ```
=== "mc"
    ```bash
    mc retention info --json --default {{api_region|lower}}/<bucket>
    ```
    Example output:
    ```json
    {
      "op": "info",
      "enabled": "Enabled",
      "mode": "COMPLIANCE",
      "validity": "2DAYS",
      "status": "success"
    }
    ```

### Object-level

To view the default object lock mode and retention period set on an object, use the following command:

=== "aws"
    ```bash
    aws --profile {{api_region|lower}} \
      s3api get-object-retention \
      --bucket <bucket-name> \
      --key <object-name>
    ```
    Example output:
    ```json
    {
      "Retention": {
        "Mode": "COMPLIANCE",
        "RetainUntilDate": "2023-02-25T20:04:23.383915+00:00"
      }
    }
    ```
    > For the value of the `RetainUntilDate` parameter, use the [ISO 8601 date-time representation](https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations) format.
=== "mc"
    ```bash
    mc retention info --json {{api_region|lower}}/<bucket>/<object-name>
    ```
    Example output:
    ```json
    {
      "mode": "COMPLIANCE",
      "until": "2023-02-25T20:04:23.383915502Z",
      "urlpath": "region/bucket/object",
      "versionID": "",
      "status": "success",
      "error": null
    }
    ```


## Configure the object lock legal hold for an object

**Legal hold** requires that the specified bucket has object locking enabled.

### Per bucket

To configure the legal hold for all objects in a bucket, use the following command:

=== "aws"
    The `aws s3api` command **can only set the legal hold for a single object** at a time.
    However, you can use the `ls` command along with `--recursive` to list all objects in a bucket, and then set the legal hold for each object in your bucket.

    ```bash
    aws --profile {{api_region|lower}} \
      s3api list-objects \
      --bucket <bucket-name> \
      | jq .Contents[].Key \
      | xargs -n1 aws --profile {{api_region|lower}} s3api put-object-legal-hold --legal-hold Status=ON --bucket <bucket-name> --key
    ```
=== "mc"
    ```bash
    mc legalhold set \
      --recursive \
      {{api_region|lower}}/<bucket>
    ```

### Per object

To configure the legal hold for a single object, use the following command:

=== "aws"
    ```bash
    aws --profile {{api_region|lower}} \
      s3api put-object-legal-hold \
      --bucket <bucket-name> \
      --key <object-name> \
      --version-id <version-id> \
      --legal-hold Status=ON
    ```
    > Note that if you don't specify a version ID, the legal hold will be applied to the latest version of the object.
=== "mc"
    ```bash
    mc legalhold set \
      {{api_region|lower}}/<bucket>/<object-name>
    ```
    > To remove the legal hold, use the `clear` command instead of `set`.

## Retrieve the legal hold status for an object

To display the legal hold status for an object, use the following command:

=== "aws"
    ```bash
    aws --profile {{api_region|lower}} \
      s3api get-object-legal-hold \
      --bucket <bucket-name> \
      --key <object-name>
    ```
    Example output:
    ```json
    {
      "LegalHold": {
        "Status": "ON"
      }
    }
    ```
=== "mc"
    ```bash
    mc legalhold info \
      --json {{api_region|lower}}/<bucket>/<object-name>
    ```
    Example output:
    ```json
    {
      "legalhold": "ON",
      "urlpath": "https://s3-{{api_region|lower}}.{{api_domain}}/<bucket>/<object-name>",
      "key": "<object-name>",
      "versionID": "",
      "status": "success"
    }
    ```
