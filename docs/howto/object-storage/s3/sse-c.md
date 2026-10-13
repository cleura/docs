---
description: SSE-C provides server-side S3 object encryption with pre-shared secrets.
---
# Server-side object encryption with customer-provided keys (SSE-C)

You can use object encryption via the S3 API, according to the [Amazon SSE-C](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html) specification.
This means that you need to provide an encryption/decryption key with each request to the object.

You can store the encryption key in [Barbican](../../openstack/barbican/index.md), and provide it to the S3 client at runtime.

## Requirements

This guide assumes familiarity with the following tools:

* `python-openstackclient` (with the `python-barbicanclient` plugin),
* `pwgen`,
* `rclone` version 1.54 or later, or the `aws` command-line interface (`awscli`) version 1.

## Prerequisites

In order to manipulate S3 objects using SSE-C, you must

* configure the [OpenStack CLI](../../getting-started/enable-openstack-cli.md),
* obtain [S3-compatible credentials](credentials.md).


## Creating encryption details

According to the SSE-C specification, in order to use server-side encryption, any S3 client needs to provide three pieces of information, which it includes in the request headers for each S3 request being made:

* Encryption algorithm: the only valid option here is AES256.
* Encryption key: a valid AES key, which means that key length must be 32 bytes.
* Encryption key checksum: the MD5 checksum of the encryption key.
  Your S3 API client uses this for integrity checks, and normally adds it automatically to your request.

In order to generate encryption key and store it in Barbican, proceed as follows.

1. Generate an encryption secret:
   ```bash
   secret_raw=$(pwgen 32 1)
   ```

2. Store the secret in Barbican:
   ```bash
   barbican_secret_url=$(openstack secret store --name objectSecret --algorithm aes --bit-length 256 --payload ${secret_raw} -f value -c 'Secret href')
   ```

3. Then, whenever you need to upload or download encrypted objects, retrieve the secret from Barbican:
   ```bash
   secret=$(openstack secret get ${barbican_secret_url} -p -c Payload -f value)
   ```

## Managing encrypted objects in S3

Once you have your encryption secret available, you can create or access encrypted objects.

=== "aws"
    1. Create an S3 bucket:
       ```bash
       aws --profile {{api_region|lower}} \
         s3 mb s3://{{brand|lower|replace(' ','')}}-encrypted
       ```
    2. Sync a directory to the S3 bucket, encrypting the files it contains on upload:
       ```bash
       aws --profile {{api_region|lower}} \
         s3 sync \
         ~/media/ s3://{{brand|lower|replace(' ','')}}-encrypted \
         --sse-c AES256 \
         --sse-c-key ${secret}
       ```
    3. Retrieve a file from S3 and decrypt it:
       ```bash
       aws --profile {{api_region|lower}} \
         s3 cp \
         s3://{{brand|lower|replace(' ','')}}-encrypted/file.png . \
         --sse-c AES256 \
         --sse-c-key ${secret}
       ```

    Note that attempting to download an encrypted file *without* providing an encryption key results in an immediate HTTP 400 ("Bad Request") error:
    ```console
    $ aws --profile {{api_region|lower}} \
      s3 cp \
      s3://{{brand|lower|replace(' ','')}}-encrypted/file.png .
    fatal error: An error occurred (400) when calling the HeadObject operation: Bad Request
    ```
=== "mc"
    1. Create an S3 bucket:
       ```bash
       mc mb {{api_region|lower}}/{{brand|lower|replace(' ','')}}-encrypted
       ```
    2. Sync a directory to the S3 bucket, encrypting the files it contains on upload.
       Note that you must specify the encryption secret as the argument to the `--encrypt-key` option, using a syntax of `<minio-alias>/<bucket-name>=<encryption-key>`:
       ```bash
       mc cp \
         --recursive \
         --encrypt-key "{{api_region|lower}}/{{brand|lower|replace(' ','')}}-encrypted=${secret}" \
         ~/media/ {{api_region|lower}}/{{brand|lower|replace(' ','')}}-encrypted
       ```
    3. Retrieve a file from S3 and decrypt it.
       Again, specify the encryption key in the same manner:
       ```bash
       mc cp \
         --encrypt-key "{{api_region|lower}}/{{brand|lower|replace(' ','')}}-encrypted=${secret}" \
         {{api_region|lower}}/{{brand|lower|replace(' ','')}}-encrypted/file.png .
       ```

    Note that attempting to download an encrypted file *without* providing an encryption key results in an immediate HTTP 400 ("Bad Request") error:
    ```console
    $ mc cp \
      {{api_region|lower}}/{{brand|lower|replace(' ','')}}-encrypted/file.png .
    mc: <ERROR> Unable to validate source `{{api_region|lower}}/{{brand|lower|replace(' ','')}}-encrypted/file.png`.
    ```

=== "s3cmd"
    You cannot use `s3cmd` in combination with SSE-C.

    > `s3cmd` does contain a *client* side encryption facility, using GnuPG for encryption.
    > It also supports SSE-KMS, which is a different SSE flavor that is currently not available in {{brand}}.
=== "rclone"
    SSE-C encryption has been implemented/fixed with version 1.54.
    Earlier `rclone` versions won't work.

    1. To start with, modify the section in your configuration file that is named after your target region, adding the `sse_customer_algorithm` option:
       ```ini
       [{{api_region|lower}}]
       type = s3
       provider = Ceph
       env_auth = false
       access_key_id = <access key id>
       secret_access_key = <secret key>
       endpoint = s3-{{api_region|lower}}.{{api_domain}}
       acl = private
       sse_customer_algorithm = AES256
       ```
    2. Create an S3 bucket:
       ```bash
       rclone mkdir {{brand|lower|replace(' ','')}}-encrypted
       ```
    3. Sync a directory to the S3 bucket, encrypting the files it contains on upload:
       ```bash
       rclone sync ~/media/ {{brand|lower|replace(' ','')}}-encrypted \
         --s3-sse-customer-key=${secret}
       ```
    4. Retrieve a file from S3 and decrypt it:
       ```bash
       rclone copy {{brand|lower|replace(' ','')}}-encrypted/file.png \
         --s3-sse-customer-key=${secret}
       ```

    For more examples on how to use rclone, please use its [reference documentation](https://rclone.org/docs/#subcommands).
