# Volume service reference

## Volume types

The following volume types are available in {{brand}} for persistent block storage devices ("volumes") managed by OpenStack Cinder.

If you create a volume without specifying a volume type, then the default volume type applies.

| Volume type              | Default          | [Encryption](../../../howto/openstack/cinder/encrypted-volumes.md) |
| -----------              | -------          | ------------                                                    |
| `cbs-standard`           | :material-check: | :material-close:                                                |
| `cbs-premium`            | :material-close: | :material-close:                                                |
| `cbs-standard-encrypted` | :material-close: | :material-check:                                                |
| `cbs-premium-encrypted`  | :material-close: | :material-check:                                                |

It is possible --- though somewhat involved --- to [change the type of an existing volume](../../../howto/openstack/cinder/retype-volumes.md) (also known as retyping).

In {{api_region}}, Quality of Service for Cinder is as follows:

| Volume type    | Min IOPS | IOPS / Provisioned GB | Max IOPS[^iops] | Min throughput (MBps) | Throughput / Provisioned GB (MBps) | Max throughput (MBps) |
| -----------    | -------- | --------------------- | --------------- | --------------------- | ---------------------------------- | --------------------- |
| `cbs-standard` | 500      | 50                    | 8000            | 50                    | 3                                  | 500                   |
| `cbs-premium`  | 3000     | 100                   | 16000           | 100                   | 6                                  | 1000                  |
| Local Storage  | 40000    | N/A                   | 40000           | 1000                  | N/A                                | 1000                  |

[^iops]: The maximum IOPS specification is essentially a cap, which creates an upper bound for individual device performance under *ideal* conditions. Actual IOPS may vary based on system load and utilization.

## Administrative access to volume encryption secrets

If you want to enable {{brand}} support to administratively migrate virtual machines with attached [encrypted volumes](../../../howto/openstack/cinder/encrypted-volumes.md), please [share your encryption secrets](../../../howto/openstack/barbican/share-secret.md) with the following user IDs:

| {{brand}} region | Administrative user UUID           |
| ---------------- | ---------------------------------  |
| Fra1             | `a3bee416cf67420995855d602d2bccd3` |
| Kna1             | `a3bee416cf67420995855d602d2bccd3` |
| Sto2             | `a3bee416cf67420995855d602d2bccd3` |
| Sto1HS           | `ac35ff3bedf440fe8062a5ba7e17d590` |
| Sto2HS           | `17c689c90f9549a3b30ac8ecbef9abb1` |
| Sto-Com          | `9df720317c964e399d5bf6bc1e49e6a8` |
