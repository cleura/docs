# Kubernetes in Cleura Cloud

{{brand}} has a management facility for Kubernetes clusters, based on [{{k8s_management_service}}](../../howto/kubernetes/gardener/index.md).

{{k8s_management_service}} supports recent Kubernetes versions and offers you a great degree of "hands-off" management.

For more details on the merits of {{k8s_management_service}}, refer to the sections below.

## General characteristics
|                                                                 | {{k8s_management_service}}   |
| -------------                                                   | ----------------             |
| Kubernetes Cloud Provider                                       | OpenStack                    |
| Base operating system for nodes                                 | Garden Linux                 |
| Latest installable Kubernetes minor release                     | 1.33                         |


## API and CLI support
|                                                                 | {{k8s_management_service}}   |
| -------------                                                   | ----------------             |
| Manageable via Cleura Cloud REST API                            | :material-check:             |
| Manageable via OpenStack REST API                               | :material-close:             |
| Manageable via OpenStack CLI                                    | :material-close:             |

## Updates and upgrades
|                                                                 | {{k8s_management_service}}   |
| -------------                                                   | ----------------             |
| Automatic update to new Kubernetes patch release                | :material-check:             |
| Rolling upgrade to new Kubernetes minor release                 | :material-check:             |
| Automatic upgrade to new Kubernetes minor release               | :material-check:             |
| Rolling upgrade to new base operating system release            | :material-check:             |
| Automatic upgrade to new base operating system release          | :material-check:             |

## Functional features
|                                                       | {{k8s_management_service}}          |
| -------------                                         | ----------------                    |
| Built-in private registry for container images        | :material-close:                    |
| [Hibernation](gardener/hibernation.md)                | :material-check:                    |
| Manual vertical scaling (bigger/smaller worker nodes) | :material-check:[^vertical-scaling] |
| Vertical autoscaling                                  | :material-close:                    |
| Manual horizontal scaling (more/fewer worker nodes)   | :material-check:                    |
| Horizontal [autoscaling](gardener/autoscaling.md)     | :material-check:                    |
| Kubernetes dashboard                                  | :material-check:[^dashboard]        |

[^vertical-scaling]: Vertical scaling is only supported via defining additional worker node groups.

[^dashboard]: You must separately [deploy](https://github.com/kubernetes/dashboard/#install) the Kubernetes Dashboard.

## Charges and billing
|                                                                 | {{k8s_management_service}}   |
| -------------                                                   | ----------------             |
| Monthly subscription fee                                        | :material-check:             |
| {{brand}} charges for Kubernetes control plane nodes            | :material-close:             |
| {{brand}} charges for Kubernetes worker nodes                   | :material-check:             |

