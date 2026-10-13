---
description: You can use the S3 API to temporarily allow access to individual objects without authentication from a browser, using pre-signed URLs.
---
# Pre-signed object URLs

{{page.meta.description}}

This approach is distinct from enabling *permanent* [anonymous access to objects in a bucket](public-bucket.md).
If you are planning to use pre-signed URLs in a bucket, then that bucket should *not* have a public read policy.

> Pre-signed URLs are typically found in web applications using a Software Development Kit (SDK) to interact with the S3 API.
> An example of such an SDK would be [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) for Python applications.
>
> This how-to guide instead uses command-line utilities to illustrate the concept, and to facilitate testing pre-signed URLs in {{brand}}.

## Prerequisites

The use of pre-signed URLs requires that you configure your environment with [working S3-compatible credentials](credentials.md).

## Creating a pre-signed URL

To create a pre-signed URL for an object, you use the following command (replace `<seconds>` with the number of seconds you want the pre-signed URL to be valid):

=== "aws"
    ```bash
    aws --profile {{api_region|lower}} \
      s3 presign \
      --expires-in <seconds> \
      s3://<bucket-name>/<object-name>
    ```
=== "mc"
    ```bash
    mc share download --expire <seconds>s {{api_region|lower}}/<bucket-name>
    ```
    Note the `s` suffix for the `--expire` option.
    `mc` also supports the suffix `m` for minutes, `h` for hours, and `d` for days.

    If you do not set `--expire`, `mc` defaults to creating a pre-signed URL that is valid for 7 days.
=== "s3cmd"
    > For pre-signed URLs generated with `s3cmd` to work correctly in {{brand}}, you must use an `s3cmd` version later than 2.0.1, and set `signurl_use_https = True` in your configuration file.

    ```bash
    s3cmd -c ~/.s3cfg-{{api_region|lower}} signurl s3://<bucket-name>/<object-name> +<seconds>
    ```
    Note the `+` prefix on the expiry.
    `s3cmd` also supports setting an absolute expiry date, which does not use the `+` prefix and must be formatted in [Unix time](https://en.wikipedia.org/wiki/Unix_time).

The command will return the valid pre-signed URL.

## Accessing objects with a pre-signed URL

To access an object in a public bucket from a web browser or a generic HTTP/HTTPS client like `curl`, open the URL that the pre-sign command returned:

```console
curl -f -O https://s3-{{api_region|lower}}.{{api_domain}}/<bucket-name>/<object-name>?AWSAccessKeyId=<access-key>&Signature=<signature>&Expires=<expiry>
```

As long as the query parameters are correct and the signature has not yet expired, this command will succeed.
If the query parameters are incorrect or the pre-signed URL is past its expiry date, it will fail with HTTP 403 (Forbidden) instead.

> Pre-signed URLs are valid for HTTP `GET` requests only.
> Thus, even a valid pre-signed URL will result in HTTP 403 if you force a different HTTP method (such as `HEAD`, by setting `curl -I`).

For example, to retrieve an object named `bar.pdf` in a bucket named `foo` in the {{brand}} {{api_region}} region via its pre-signed URL, you would run:

```console
$ curl -o bar.pdf https://s3-{{api_region|lower}}.{{api_domain}}/foo/bar.pdf?AWSAccessKeyId=07576783684248f7b2745e34356c6025&Expires=1673521496&Signature=%2Frm9nLV3moP%2FQz7aGCAnrESXjbk%3D
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 62703  100 62703    0     0   186k      0 --:--:-- --:--:-- --:--:--  186k
```

## Setting the download filename on the object

When you use `curl` (and potentially other browsers or HTTP/HTTPS clients) to download an object from a pre-signed URL, the default behavior is to set its filename to the name of the downloaded object *including* the query parameters.
This can lead to rather unwieldly filenames.

To ensure that an object named `bar.pdf` in a bucket named `foo` is always downloaded and stored with `bar.pdf` as its filename, you can set its `Content-Disposition` header.

### Setting `Content-Disposition` on object creation

=== "aws"
    ```bash
    aws --profile {{api_region|lower}} \
      s3api put-object \
      --content-disposition 'attachment;filename="bar.pdf"' \
      --bucket <bucket-name> \
      --key <object-name>
    ```
=== "mc"
     The `mc` client does not correctly support this feature.

     You can set the attribute on object creation:
     ```bash
     mc cp --attr Content-Disposition='attachment;filename="bar.pdf"' bar.pdf {{api_region|lower}}/foo/
     ```
     However, `mc` cuts off the `Content-Disposition` header at the semicolon, rendering it useless:
     ```console
     $ mc stat {{api_region|lower}}/foo/bar.pdf
     Name      : bar.pdf
     Date      : 2023-01-12 12:53:52 CET
     Size      : 57 KiB
     ETag      : 630f6e1bf441a0eee63f9cb06804dc79
     Type      : file
     Metadata  :
       Content-Type       : application/pdf
       X-Amz-Meta-Filename: bar.pdf
       Content-Disposition: attachment
     ```
     You should thus set the `Content-Disposition` header with a different client.
=== "s3cmd"
    ```bash
    s3cmd -c ~/.s3cfg-{{api_region|lower}} modify \
      --add-header 'Content-Disposition: attachment; filename="bar.pdf"' \
      s3://foo/bar.pdf
    ```

### Setting `Content-Disposition` on existing objects

=== "aws"
    To modify the `Content-Disposition` header of an existing object without downloading and re-uploading its contents, you must use `s3api copy-object`, with the object being its own copy source, and the metadata directive set to `replace`:
    ```bash
    aws --profile {{api_region|lower}} \
      s3api copy-object \
      --copy-source <bucket-name>/<object-name> \
      --content-disposition 'attachment;filename="bar.pdf"' \
      --metadata-directive replace \
      --bucket <bucket-name> \
      --key <object-name>
    ```
=== "mc"
     The `mc` client does not support modifying object metadata in-place.
=== "s3cmd"
    `s3cmd` comes with a handy `modify --add-header` subcommand for updating object metadata in-place:
    ```bash
    s3cmd -c ~/.s3cfg-{{api_region|lower}} modify \
      --add-header 'Content-Disposition: attachment; filename="bar.pdf"' \
      s3://foo/bar.pdf
    ```

### Testing the `Content-Disposition` header

Once you have set the `Content-Disposition` header on an object and created a pre-signed URL for it, you can test its functionality with the `curl -OJ` command:

```console
$ curl -f -OJ 'https://s3-{{api_region|lower}}.{{api_domain}}/foo/bar.pdf?AWSAccessKeyId=07576783684248f7b2745e34356c6025&Expires=1673521496&Signature=%2Frm9nLV3moP%2FQz7aGCAnrESXjbk%3D'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 58503  100 58503    0     0   178k      0 --:--:-- --:--:-- --:--:--  178k
curl: Saved to filename 'bar.pdf'
```

### Caution: do not abuse `Content-Disposition`

Please keep in mind that there is nothing that keeps you from having two objects in the same bucket, with `Content-Disposition` on one object matching the object name of the other.

For example, in the `foo` bucket, you may have

* an object named `spam.pdf` with no `Content-Disposition` header, and
* another object named `eggs.pdf`, with `Content-Disposition` set to include `filename="spam.pdf"`.

If you were now to generate a pre-signed URL on `eggs.pdf` and downloaded it with `curl -OJ`, you would end up with a local file *named* `spam.pdf`, with the *contents* of `eggs.pdf`.
This is obviously **not a good idea,** and you should avoid setting a `Content-Disposition` header that does not agree with the object name.
