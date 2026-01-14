# Kubernetes service limitations


## {{k8s_management_service}}

### Kubernetes version

The latest Kubernetes version you can install in {{brand}} with {{k8s_management_service}} is 1.33.

### IP version

In {{brand}}, you can use {{k8s_management_service}} to deploy Kubernetes clusters that use IPv4.
IPv6 clusters or services (whether single-stack or dual-stack) are not supported.

### Service annotations

In {{k8s_management_service}}-managed clusters, we do not support `loadbalancer.openstack.org` [annotations](https://github.com/kubernetes/cloud-provider-openstack/blob/master/docs/openstack-cloud-controller-manager/expose-applications-using-loadbalancer-type-service.md) for Kubernetes [services](https://kubernetes.io/docs/concepts/services-networking/service/) of the [`LoadBalancer`](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer) type.

### Persistent volumes (PVs)

In {{k8s_management_service}}-managed Kubernetes clusters, the supported PV [access modes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes) are `ReadWriteOnce` (`RWO`), and `ReadWriteOncePod` (`RWOP`).
Note that `RWO` enables multiple Pods to access the same volume, as long as they are [configured to run on the same node](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/).
Use `RWOP` to restrict the volume to one pod only.

You cannot use `ReadWriteMany` (`RWX`) or `ReadOnlyMany` (`ROX`) PVs.

### Dynamic volume provisioning storage classes

In {{brand}}, {{k8s_management_service}}-managed clusters contain a single [storage class](https://kubernetes.io/docs/concepts/storage/storage-classes/) named `default`, which is the supported storage class you should use for all dynamically-provisioned persistent volumes.
We do not provide support for any user-defined storage classes.
