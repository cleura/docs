---
description: Gardener runs its worker and control plane nodes on Garden Linux.
---
# Garden Linux

In a {{k8s_management_service}} cluster, worker nodes run [Garden Linux](https://gardenlinux.io), which is a [Linux distribution](https://en.wikipedia.org/wiki/Linux_distribution) based on [Debian GNU/Linux](https://www.debian.org/).

## Version scheme

Garden Linux uses an unusual version scheme: releases use a major version number derived from the "gardenlinux epoch", and should ostensibly reflect the number of days since April 1, 2020 (although in reality, the major release numbers are off by a number of days).

For example, the major release that landed on August 22, 2024 was release [1592](https://github.com/gardenlinux/gardenlinux/releases/tag/1592.1).
The next major release, on July 11, 2025, had the major release number [1877](https://github.com/gardenlinux/gardenlinux/releases/tag/1877.1).

Minor releases are numbered with incrementing integer minor version numbers.
They tend to include mostly bug fixes, as opposed to functionality updates or new features.
For example, [1877.3](https://github.com/gardenlinux/gardenlinux/releases/tag/1877.3) was a Garden Linux release that fixed a lot of security issues in the 1877 release series.

## Linux kernel

Garden Linux runs on the latest [longterm release](https://www.kernel.org/category/releases.html) Linux kernel version available at the time of a major release.
For instance, Garden Linux 1592 includes the Linux 6.6.47 kernel, whereas Garden Linux 1877 includes Linux 6.12.36.

## Container runtime

Garden Linux defaults to using the [Podman](https://podman.io/) container runtime.
