# Gardener

{{brand_container_orchestration}} is a Kubernetes-native system that provides automated management and operation of Kubernetes clusters as a service.

First off, it allows you to create clusters and define their high-availability characteristics.
Then, you can automatically handle their lifecycle operations, including configurable maintenance windows, hibernation schedules, and automatic updates to Kubernetes control plane and worker nodes.

You may read more about {{k8s_management_service}} and its capabilities on its [documentation website](https://gardener.cloud/docs/gardener/).

## Activating the {{k8s_management_service}} service

To use {{brand_container_orchestration}}, you first need to *activate* the service.
You can conveniently do this via the {{gui}}.

To activate {{k8s_management_service}}, select Containers → [{{k8s_management_service}}](https://{{gui_domain}}/containers/gardener) in the side panel.
Then, click the _Activate {{k8s_management_service}} Service_ button:

!["Activate {{k8s_management_service}}" dialog in {{gui}}](assets/activate-gardener.png)

You only need to do this once.

## Deploying Kubernetes clusters with {{k8s_management_service}}

To learn how to use {{k8s_management_service}} in the {{gui}}, refer to [Creating Kubernetes clusters with {{k8s_management_service}}](create-shoot-cluster.md).
