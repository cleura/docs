---
description: How auto-upgrading works in Gardener-managed Kubernetes clusters
---
# Automatic upgrades

By default, Kubernetes clusters created with {{brand_container_orchestration}} are upgraded automatically.

More specifically, during the specified maintenance window, {{k8s_management_service}} checks for a new Kubernetes version, and a new version of the base image that runs on the control plane and worker nodes.
If there is a new version of any of those, the cluster starts upgrading automatically.

During the upgrade, the API server may briefly be unavailable.

## Machine image upgrades

Both minor and major [Garden Linux](garden-linux.md) release upgrades are allowed and performed automatically.
Also, version jumps are allowed over minor release upgrades.

Whenever there is a new machine image available, this is indicated in the {{gui}}:

![New machine image indicator](assets/gard_new_img_sign.png)

Before the auto-upgrade kicks in, the version of the new image is displayed in the expanded view of the cluster, in the *Worker Groups* tab.

![New machine image available](assets/gard_new_img_avail.png)

## Kubernetes upgrades

Due to the Kubernetes versioning scheme, which does not follow the [semantic versioning](https://en.wikipedia.org/wiki/Software_versioning#Semantic_versioning) logic, only patch-level release upgrades and jumps are performed automatically.
For instance, an upgrade from 1.32.8 to 1.32.9 is allowed, and so is an upgrade from 1.32.9 to 1.32.11.

Minor release upgrades, such as from 1.32 to 1.33, do not happen automatically.
You must always initiate them from the {{gui}}.

## Hibernated clusters

Whenever a {{k8s_management_service}} cluster is [hibernated](hibernation.md), all of its worker nodes are removed.

If automatic upgrades are enabled on a hibernated cluster, then waking the cluster will initiate an immediate automated upgrade.
That is to say that, rather than recreating them with the old versions and waiting for the next maintenance window, {{k8s_management_service}} recreates the worker nodes using current (updated) Garden Linux and Kubernetes versions.

## Forced upgrades

For a {{k8s_management_service}} cluster, it is possible to disable automatic upgrades both for Garden Linux *and* Kubernetes.

![Disable automatic upgrades](assets/disable_automatic_upgrades.png)

Even so, you may find out that, from time to time, your cluster gets upgraded.
These seemingly unscheduled upgrades happen when either the cluster's Kubernetes or Garden Linux release _expires_.
In this context, the expiration happens about a month after the _next_ release of Kubernetes or Garden Linux is out.

You may use the [{{brand}} REST API](../../../howto/getting-started/accessing-cc-rest-api.md) to know in advance if any of your Gardener clusters is about to expire.
Consider the following example, specifically paying attention to the `expirationDate` field:

```console
$ curl -s -H "X-AUTH-LOGIN: <username>" -H "X-AUTH-TOKEN: <token>" \
    https://rest.cleura.cloud/gardener/v1/public/cloudprofile | jq

[
  {
    "name": "cleuracloud",
    "spec": {
      "kubernetes": {
        "versions": [
          {
            "version": "1.31.13",
            "expirationDate": "2025-12-29T00:00:00Z",
            "classification": "deprecated"
          },
          {
            "version": "1.31.14",
            "expirationDate": "2026-02-16T00:00:00Z",
            "classification": "deprecated"
          },
          {
            "version": "1.32.9",
            "expirationDate": "2026-01-02T00:00:00Z",
            "classification": "deprecated"
          },
          {
            "version": "1.32.10",
            "expirationDate": "2026-02-16T00:00:00Z",
            "classification": "deprecated"
          },
          {
            "version": "1.32.11",
            "classification": "supported"
          },
          {
            "version": "1.33.5",
            "expirationDate": "2026-01-02T00:00:00Z",
            "classification": "deprecated"
          },
          {
            "version": "1.33.6",
            "expirationDate": "2026-02-16T00:00:00Z",
            "classification": "deprecated"
          },
          {
            "version": "1.33.7",
            "classification": "supported"
          }
        ]
      },
      "machineImages": [
        {
          "name": "gardenlinux",
          "versions": [
            {
              "version": "1877.4.0",
              "expirationDate": "2025-12-10T00:00:00Z",
              "classification": "deprecated",
              "cri": [
                {
                  "name": "containerd"
                }
              ],
              "architectures": [
                "amd64"
              ]
            },
            {
              "version": "1877.5.0",
              "expirationDate": "2026-01-02T00:00:00Z",
              "classification": "deprecated",
              "cri": [
                {
                  "name": "containerd"
                }
              ],
              "architectures": [
                "amd64"
              ]
            },
            {
              "version": "1877.7.0",
              "expirationDate": "2026-02-23T00:00:00Z",
              "classification": "deprecated",
              "cri": [
                {
                  "name": "containerd"
                }
              ],
              "architectures": [
                "amd64"
              ]
            },
            {
              "version": "1877.9.0",
              "classification": "supported",
              "cri": [
                {
                  "name": "containerd"
                }
              ],
              "architectures": [
                "amd64"
              ]
            }
          ],
          "updateStrategy": "major"
        }
      ],

[...]
```
