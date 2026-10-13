# Object storage in {{brand}}

Object storage in {{brand}} is implemented via the [Ceph Object Gateway](https://docs.ceph.com/en/tentacle/radosgw/index.html), also known as `radosgw` (commonly pronounced "[rados](https://docs.ceph.com/en/tentacle/glossary/#term-RADOS) gateway").

This facility exposes access to objects via two RESTful APIs: the [Amazon S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/), and the [OpenStack Swift API](https://docs.openstack.org/api-ref/object-store/).
It is, however, important to understand that radosgw shares no code with Amazon S3, nor with OpenStack Swift.

As such, object storage in {{brand}} is not expected to behave *exactly* as Amazon S3 or OpenStack Swift, although it tracks their behavior very closely.
The Ceph upstream documentation lists API deviations from the respective reference implementations, for both the [S3](https://docs.ceph.com/en/tentacle/radosgw/s3/) and the [Swift](https://docs.ceph.com/en/tentacle/radosgw/swift/) API.
Our [reference section](../reference/index.md) lists additional [limitations](../reference/limitations/object-storage.md) specific to {{brand}}.

## Object storage integration with OpenStack authentication

In {{brand}}, the OpenStack `object‑store` service endpoints point not to native OpenStack Swift proxy servers, but to radosgw endpoints.
This is to say that radosgw acts as a "drop-in" replacement for OpenStack Swift.

As such, it is fully integrated with OpenStack's authentication facility, OpenStack Keystone.
This means that once you have configured the [OpenStack CLI](../howto/getting-started/enable-openstack-cli.md) correctly, you can interact with the `object‑store` endpoint as with any other OpenStack service, using the Swift API.

The S3 API, however, does not natively "know" about OpenStack authentication.
The radosgw endpoints in {{brand}} *still* authenticate via Keystone, albeit taking a little detour:
you must first [create AWS-style credentials](../howto/object-storage/s3/credentials.md) and configure your S3 client with them, which it can then use to make properly authenticated S3 API calls.

## Multi-tenancy

OpenStack Swift has the concept of multi-tenancy built-in.
Thus, if you use the Swift API with credentials for an [OpenStack user](../howto/getting-started/enable-openstack-cli.md) that authenticates against a specific {{brand}} *region* and uses a specific *project*, it can only interact with objects stored in containers belonging to that project by default.

In {{brand}}, you also get multi-tenancy for S3 objects, even though this concept is not intrinsic to S3 itself.
Here, again, a slight conceptual detour applies: when you [create AWS-style credentials](../howto/object-storage/s3/credentials.md), then those are linked to a specific OpenStack user, region, and project.
When you subsequently use those credentials for S3 interactions, any buckets and objects thus created belong to the project to which the credentials are linked.

## Object identity in {{brand}}

Whether you access a specific object via the Swift API or the S3 API, *it is the same object.*
This also means that the object's *container* (accessed via the Swift API) is identical to its containing *bucket* (accessed via the S3 API).

Thus, if you

* [enable the OpenStack CLI](../howto/getting-started/enable-openstack-cli.md) with a certain set of user credentials;
* use those credentials to [create a private container](../howto/object-storage/swift/private-container.md) named `test` and an object named `my‑object`, using the Swift API;
* use the same OpenStack credentials to [create AWS-style credentials](../howto/object-storage/s3/credentials.md);
* then use those AWS-style credentials to list your buckets and objects, using the S3 API,

you will find an S3 bucket named `test`, containing an object named `my‑object`.

## Permission and feature conflicts

The fact that objects are identical when accessed via Swift and S3 also entails that bucket and object permissions, set via one API, also apply to object access using the other API.

For example, if you [make a container public](../howto/object-storage/swift/public-container.md) via the Swift API, it also becomes a [public bucket](../howto/object-storage/s3/public-bucket.md) that is accessible via an S3 API path.
You cannot simultaneously retain mandatory private (authenticated) access to the corresponding bucket via the S3 API.

Object storage in {{brand}} also does *not* allow you to make competing feature settings on containers/buckets, based on the API used to access them.
For example, it is not possible to create [a Swift container that enables versioning](../howto/object-storage/swift/versioning.md), while disabling [bucket versioning](../howto/object-storage/s3/versioning.md) on the corresponding S3 bucket.

Sometimes, this creates unavoidable conflicts if a specific feature is only available in one of the supported APIs.
For example, if you [set a public read policy](../howto/object-storage/s3/public-bucket.md) on an S3 bucket, the corresponding Swift container will still show an empty Read ACL, making the Swift container *look* like it is private, even though its objects are accessible through simple public URLs.
This is because Swift has no concept of fine-grained bucket policies, as they exist in S3.

## Object versioning

In regular default buckets, each object has just one representation, and all operations (like removal or upload) operate on this one entity.
With versioned buckets, modifications like uploading an object with the same name only modify a view of the bucket.
In this mode of operation, each object receives a unique version ID, and modifications retain prior versions.
This allows you to restore an earlier version of an object.

| Operation                    | Default bucket                | Versioned bucket                                                      |
| ---------------------------- | ----------------------------  | -------------------------------------                                 |
| Uploading a new object       | New object is stored          | New object is stored                                                  |
| Overwrite of existing object | New object overwrites old one | New object version becomes current                                    |
| Delete object                | Object is deleted             | Delete marker is placed, subsequent object access returns "Not found" |

Once you [enable versioning on a bucket](../howto/object-storage/s3/versioning.md#enabling-bucket-versioning), you cannot turn it off.
You can, however, suspend it.
When versioning is suspended, new objects are created with a version ID of `null`, overwriting any existing `null` version.
All previously versioned objects remain unchanged and accessible.

### Delete markers

When you delete an object in a versioned bucket, the object isn't actually removed.
Instead, a special placeholder called a delete marker acts as the current version of the object.
This marker has a unique version ID, causing the object service to return a 404 "Not found" error whenever you attempt to retrieve the object.

However, trying to access any older version of the object works as expected.
Delete markers themselves can also be deleted.
When you delete a delete marker, the previous version becomes current again, effectively "undeleting" the object.
To permanently remove an object version, you must delete it by specifying its version ID.


## Object lock

Object lock is a feature in S3 that essentially allows you to protect objects from being deleted or overwritten.
There are two methods for managing object retention: **Retention periods** and **Legal hold**.

### Retention periods

Retention periods specify the length of time that an object remains locked and protected from being overwritten or deleted.
When you set a retention period, the object is safeguarded for the specified time.
You can set the retention period in either days or years, with a **minimum of one day** and no maximum limit.

In addition to retention periods, you can choose the retention mode that applies to your objects (either Governance or Compliance).
In {{brand}}, the only supported retention mode is **Compliance**.

Compliance mode is recommended when storing compliant data, as it prevents objects from being overwritten or deleted by any user.
If you configure an object with this mode, you cannot shorten or change its retention period, ensuring that the data remains **secure** and **compliant** with regulatory requirements.

### Legal hold

Legal hold is a feature designed for situations when you are uncertain about the length of time you need to retain an object.
It can be enabled/disabled for any object in a locked bucket, regardless of the lock configuration, object retention, or age.

This feature provides the same level of protection as a retention period but with no fixed expiration date.
Instead, a legal hold will remain in effect until you remove it explicitly.
