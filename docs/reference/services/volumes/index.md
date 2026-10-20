# Volume service reference

## Volume types

The following volume types are available in {{brand}} for persistent block storage devices ("volumes") managed by OpenStack Cinder.

If you create a volume without specifying a volume type, then the default volume type applies.


| Volume type name               | Default          | [Encryption](../../../howto/openstack/cinder/encrypted-volumes.md) | max IOPS[^iops] |
| ------------------------------ | -----            | -----                                                           | -----           |
| `cbs`                          | :material-check: | :material-close:                                                | 10000           |
| `cbs-encrypted`                | :material-close: | :material-check:                                                | 10000           |

[^iops]: The maximum IOPS specification is essentially a cap, which creates an upper bound for individual device performance under *ideal* conditions.
Actual IOPS may vary based on system load and utilization. IOPS limits are only enforced in [{{brand_public}} regions](../features/public.md).

It is possible --- though somewhat involved --- to [change the type of an existing volume](../../../howto/openstack/cinder/retype-volumes.md) (also known as retyping).

## Administrative access to volume encryption secrets

If you want to enable {{brand}} support to administratively migrate virtual machines with attached [encrypted volumes](../../../howto/openstack/cinder/encrypted-volumes.md), please [share your encryption secrets](../../../howto/openstack/barbican/share-secret.md) with the following user IDs:

| {{brand}} region | Administrative user UUID           |
| ---------------- | ---------------------------------  |
| Fra1             | `a3bee416cf67420995855d602d2bccd3` |
| Kna1             | `a3bee416cf67420995855d602d2bccd3` |
| Sto2             | `a3bee416cf67420995855d602d2bccd3` |
| Sto1HS           | `ac35ff3bedf440fe8062a5ba7e17d590` |
| Sto2HS           | `17c689c90f9549a3b30ac8ecbef9abb1` |
