# Cleura Cloud Management Panel vs. OpenStack API

You can do many tasks in {{brand}} via the [{{gui}}](https://{{gui_domain}}) or via the OpenStack API, e.g., with the help of the [OpenStack CLI](../howto/getting-started/enable-openstack-cli.md) tool.
For some tasks, though, you *will need* the OpenStack API.

But when does it make sense to prefer a particular way of working?
What are the reasons, if any, for choosing one method over the other?

## The case for the {{gui}}

Ease of use is probably the main reason for choosing the {{gui}} over the OpenStack API.
Provided you have an [account in {{brand}}](../howto/getting-started/create-account.md), you can simply log in and then follow step-by-step guides to create entities such as [networks](../howto/openstack/neutron/new-network.md) or [servers](../howto/openstack/nova/new-server.md).

You can just as easily perform administrative tasks like

* creating [security groups](../howto/openstack/neutron/create-security-groups.md),
* setting up [region-to-region VPN](../howto/openstack/neutron/vpnaas.md) connections,
* [deleting networks](../howto/openstack/neutron/delete-network.md),
* modifying [billing data](../howto/account-billing/change-account-data.md), or
* [managing invoices](../howto/account-billing/manage-invoices.md).

All in all, there are many instances when the {{gui}} is all you want and, at the same time, is more than enough for what you want.

## The case for the OpenStack API

There will be times when working from the terminal of your laptop is preferable to using the {{gui}}.
In cases like this, you will use the OpenStack API via a tool like the OpenStack CLI.
Although `openstack` usually requires some reading before doing a specific task, it doesn't take much time to get used to its logic for constructing commands to achieve what you want.
Plus, there is hardly a thing you can't do with `openstack` or a CLI tool that talks to the OpenStack API.

We should also point out that specific tasks can be performed _only_ via the OpenStack API, for there is no counterpart tool in the {{gui}} toolbox.

For instance, whenever you need to [move servers between regions](../howto/openstack/nova/move-server-between-regions.md), then `openstack` is your only option.
Another instance where you work with the OpenStack API and various CLI tools, is when you have to interact with the [S3 API](../howto/object-storage/s3/index.md) or the [Swift API](../howto/object-storage/swift/index.md).

Even though the command syntax of `openstack` may sometimes look overly complicated, the potential for scripting can speed up many operations considerably.
In addition to that, the OpenStack API is employed by configuration management systems and automation platforms like [Ansible](https://www.ansible.com), and infrastructure as code systems like [Terraform](https://www.terraform.io) and [Pulumi](https://www.pulumi.com).
