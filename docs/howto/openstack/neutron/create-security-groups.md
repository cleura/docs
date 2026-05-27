# Creating security groups

[By definition](https://docs.openstack.org/nova/latest/admin/security-groups.html), security groups are _"[...] sets of IP filter rules that are applied to all project instances, which define networking access to the instance.
Group rules are project specific; project members can edit the default rules for their group and add new rule sets."_

## Creating a security group

Navigate to the [{{gui}}](https://{{gui_domain}}) page, and log into your {{brand}} account.
On the other hand, if you prefer to work with the OpenStack CLI, please do not forget to [source the RC file first](../../getting-started/enable-openstack-cli.md).

=== "{{gui}}"
    To create a security group, first make sure the left-hand side vertical pane is fully visible.
    Click on _Security&nbsp;Groups_, and then on the top-right corner of the central pane, click on _Create new Security Group_.

    ![Initiating the creation of a new security group](assets/create-security-groups/create-secgroup-01_light.png#only-light)
    ![Initiating the creation of a new security group](assets/create-security-groups/create-secgroup-01_dark.png#only-dark)

    > An alternative way to create a Security&nbsp;Group is by clicking on the round-cornered _Create_ button, in the top bar.

    Type in a _Name_ for the new security group, and choose a _Region_ to create it in.
    You may optionally type in a _Description_ for the security group.
    Click on the _Create_ button when you are ready.

    ![Setting parameters for the new security group](assets/create-security-groups/create-secgroup-02_light.png#only-light)
    ![Setting parameters for the new security group](assets/create-security-groups/create-secgroup-02_dark.png#only-dark)
=== "OpenStack CLI"
    To create a security group, use the following command:

    ```bash
    openstack security group create <name>
    ```

    When the command is executed successfully, you will get information regarding your new security group:

    ```plain
    +-----------------+--------------------------------------------------------------------------------+
    | Field           | Value                                                                          |
    +-----------------+--------------------------------------------------------------------------------+
    | created_at      | 2025-02-19T17:58:05Z                                                           |
    | description     | <name>                                                                         |
    | id              | a463b1de-7b12-43a0-b080-189f0fb09fd8                                           |
    | name            | <name>                                                                         |
    | project_id      | d42230ea21674515ab9197af89fa5192                                               |
    | revision_number | 1                                                                              |
    | rules           | created_at='2025-02-19T17:58:05Z', direction='egress', ethertype='IPv4',       |
    |                 | id='45dee5b4-2d3b-4ac0-9304-02e3ca6229fe', standard_attr_id='305189',          |
    |                 | updated_at='2025-02-19T17:58:05Z'                                              |
    |                 | created_at='2025-02-19T17:58:05Z', direction='egress', ethertype='IPv6',       |
    |                 | id='a48fbf92-a608-4518-97a4-24e6c9fa8caf', standard_attr_id='305192',          |
    |                 | updated_at='2025-02-19T17:58:05Z'                                              |
    | shared          | False                                                                          |
    | stateful        | True                                                                           |
    | tags            | []                                                                             |
    | updated_at      | 2025-02-19T17:58:05Z                                                           |
    +-----------------+--------------------------------------------------------------------------------+
    ```

## Removing default ingress rules

By default, a security group named `default` has already been created for you.
Its rules block all traffic from any source (ingress), except from servers and ports in the same security group.
All traffic to any destination (egress) is allowed by default.

=== "{{gui}}"
    Navigate to the _Security&nbsp;Groups_ page.
    Click on the `default` security group and select the _Rules_ tab to view its rules.

    ![List of rules in the default security group](assets/create-security-groups/default-rules_light.png#only-light)
    ![List of rules in the default security group](assets/create-security-groups/default-rules_dark.png#only-dark)

=== "OpenStack CLI"
    View the details of the `default` security group using the following command:

    ```bash
    openstack security group show default
    ```

    You will get a printout similar to this:

    ```plain
    +-----------------+--------------------------------------------------------------------------------+
    | Field           | Value                                                                          |
    +-----------------+--------------------------------------------------------------------------------+
    | created_at      | 2024-04-11T07:02:49Z                                                           |
    | description     | Default security group                                                         |
    | id              | 5b6a6004-d40e-41ed-938e-48fc09f950f2                                           |
    | name            | default                                                                        |
    | project_id      | d42230ea21674515ab9197af89fa5192                                               |
    | revision_number | 1                                                                              |
    | rules           | belongs_to_default_sg='True', created_at='2024-04-11T07:02:49Z',               |
    |                 | direction='egress', ethertype='IPv6',                                          |
    |                 | id='486f7d60-a486-46e6-ab70-7d91ce65cdc7', standard_attr_id='73',              |
    |                 | updated_at='2024-04-11T07:02:49Z'                                              |
    |                 | belongs_to_default_sg='True', created_at='2024-04-11T07:02:49Z',               |
    |                 | direction='ingress', ethertype='IPv4',                                         |
    |                 | id='58785232-3635-49ca-a9d9-5f762c26c92a',                                     |
    |                 | remote_group_id='5b6a6004-d40e-41ed-938e-48fc09f950f2', standard_attr_id='67', |
    |                 | updated_at='2024-04-11T07:02:49Z'                                              |
    |                 | belongs_to_default_sg='True', created_at='2024-04-11T07:02:49Z',               |
    |                 | direction='egress', ethertype='IPv4',                                          |
    |                 | id='5a7fca17-f02a-4c72-a4a3-19ce4618a0cc', standard_attr_id='64',              |
    |                 | updated_at='2024-04-11T07:02:49Z'                                              |
    |                 | belongs_to_default_sg='True', created_at='2024-04-11T07:02:49Z',               |
    |                 | direction='ingress', ethertype='IPv6',                                         |
    |                 | id='baf7d080-32b0-49e3-aa04-b91a20358fd5',                                     |
    |                 | remote_group_id='5b6a6004-d40e-41ed-938e-48fc09f950f2', standard_attr_id='70', |
    |                 | updated_at='2024-04-11T07:02:49Z'                                              |
    | shared          | False                                                                          |
    | stateful        | True                                                                           |
    | tags            | []                                                                             |
    | updated_at      | 2024-04-11T07:02:49Z                                                           |
    +-----------------+--------------------------------------------------------------------------------+
    ```

If you want to restrict the ingress rules to disallow access from other servers and ports in the group, you need to **remove the default two ingress rules.**

=== "{{gui}}"
    Click each of the:material-delete-circle: buttons on the right-hand side of the **IPv4 ingress** and also of the **IPv6 ingress** rows.

    Your `default` or newly created security group rules will now look like the following example.

    ![List of default ingress rules](assets/create-security-groups/default-rules-egress_light.png#only-light)
    ![List of default ingress rules](assets/create-security-groups/default-rules-egress_dark.png#only-dark)

=== "OpenStack CLI"
    To view the rules, use the following command:

    ```bash
    openstack security group rule list default
    ```

    The printout will be similar to this:

    ```plain
    +-----------+-------------+-----------+-----------+------------+-----------+-----------------------+----------------------+
    | ID        | IP Protocol | Ethertype | IP Range  | Port Range | Direction | Remote Security Group | Remote Address Group |
    +-----------+-------------+-----------+-----------+------------+-----------+-----------------------+----------------------+
    | 486f7d60- | None        | IPv6      | ::/0      |            | egress    | None                  | None                 |
    | a486-     |             |           |           |            |           |                       |                      |
    | 46e6-     |             |           |           |            |           |                       |                      |
    | ab70-     |             |           |           |            |           |                       |                      |
    | 7d91ce65c |             |           |           |            |           |                       |                      |
    | dc7       |             |           |           |            |           |                       |                      |
    | 58785232- | None        | IPv4      | 0.0.0.0/0 |            | ingress   | 5b6a6004-d40e-41ed-   | None                 |
    | 3635-     |             |           |           |            |           | 938e-48fc09f950f2     |                      |
    | 49ca-     |             |           |           |            |           |                       |                      |
    | a9d9-     |             |           |           |            |           |                       |                      |
    | 5f762c26c |             |           |           |            |           |                       |                      |
    | 92a       |             |           |           |            |           |                       |                      |
    | 5a7fca17- | None        | IPv4      | 0.0.0.0/0 |            | egress    | None                  | None                 |
    | f02a-     |             |           |           |            |           |                       |                      |
    | 4c72-     |             |           |           |            |           |                       |                      |
    | a4a3-     |             |           |           |            |           |                       |                      |
    | 19ce4618a |             |           |           |            |           |                       |                      |
    | 0cc       |             |           |           |            |           |                       |                      |
    | baf7d080- | None        | IPv6      | ::/0      |            | ingress   | 5b6a6004-d40e-41ed-   | None                 |
    | 32b0-     |             |           |           |            |           | 938e-48fc09f950f2     |                      |
    | 49e3-     |             |           |           |            |           |                       |                      |
    | aa04-     |             |           |           |            |           |                       |                      |
    | b91a20358 |             |           |           |            |           |                       |                      |
    | fd5       |             |           |           |            |           |                       |                      |
    +-----------+-------------+-----------+-----------+------------+-----------+-----------------------+----------------------+
    ```

    The IDs of the two ingress rules, one for IPv4 traffic and one for IPv6, in this case, are:
    `5e5e9f4d-1faa-492d-91f1-c105b464072b` and `86b9413a-ad23-46c4-a35e-9306945dc63c`.

    Delete them by using the following command:

    ```bash
    openstack security group rule delete \
      58785232-3635-49ca-a9d9-5f762c26c92a baf7d080-32b0-49e3-aa04-b91a20358fd5
    ```

    Print the rules again:

    ```bash
    openstack security group rule list default
    ```

    Now, the remaining rules are only the egress ones.

    ```plain
    +-----------+-------------+-----------+-----------+------------+-----------+-----------------------+----------------------+
    | ID        | IP Protocol | Ethertype | IP Range  | Port Range | Direction | Remote Security Group | Remote Address Group |
    +-----------+-------------+-----------+-----------+------------+-----------+-----------------------+----------------------+
    | 486f7d60- | None        | IPv6      | ::/0      |            | egress    | None                  | None                 |
    | a486-     |             |           |           |            |           |                       |                      |
    | 46e6-     |             |           |           |            |           |                       |                      |
    | ab70-     |             |           |           |            |           |                       |                      |
    | 7d91ce65c |             |           |           |            |           |                       |                      |
    | dc7       |             |           |           |            |           |                       |                      |
    | 5a7fca17- | None        | IPv4      | 0.0.0.0/0 |            | egress    | None                  | None                 |
    | f02a-     |             |           |           |            |           |                       |                      |
    | 4c72-     |             |           |           |            |           |                       |                      |
    | a4a3-     |             |           |           |            |           |                       |                      |
    | 19ce4618a |             |           |           |            |           |                       |                      |
    | 0cc       |             |           |           |            |           |                       |                      |
    +-----------+-------------+-----------+-----------+------------+-----------+-----------------------+----------------------+
    ```

## Allowing SSH access

The next thing to do is allow SSH access on **port 22** for IPv4 and IPv6 client connections -- but _only_ from specific addresses or subnets.

=== "{{gui}}"
    To do this, while on the _Rules_ tab, click on the _Create new rule_ button.
    A pane named _Create a Security Group Rule_ will slide over from the right-hand side of the browser window.

    For the IPv4 ingress SSH rule, make sure you set _Protocol_ to _TCP_, _Direction_ to _Ingress_, and _Ether&nbsp;Type_ to _IPv4_.
    Then, set _From_ to _Network/IP_ and, in the _Custom&nbsp;CIDR_ text box below, type in either the IPv4 address of your client host or the CIDR of your client subnet.

    To create the new rule, click the _Create_ button.

    ![Create ingress rule for IPv4 SSH connections](assets/create-security-groups/default-rules-ingress-ssh-ipv4_light.png#only-light)
    ![Create ingress rule for IPv4 SSH connections](assets/create-security-groups/default-rules-ingress-ssh-ipv4_dark.png#only-dark)

    You may work similarly for the IPv6 ingress SSH rule;
    just be sure to set _Ether&nbsp;Type_ to _IPv6_.

    ![Create ingress rule for IPv6 SSH connections](assets/create-security-groups/default-rules-ingress-ssh-ipv6_light.png#only-light)
    ![Create ingress rule for IPv6 SSH connections](assets/create-security-groups/default-rules-ingress-ssh-ipv6_dark.png#only-dark)

    When you are done creating the two ingress rules for SSH, you see them listed in the _Rules_ tab of the security group.

    ![New ingress rules for SSH connections](assets/create-security-groups/default-rules-ingress-ssh_light.png#only-light)
    ![New ingress rules for SSH connections](assets/create-security-groups/default-rules-ingress-ssh_dark.png#only-dark)
=== "OpenStack CLI"
    To create this rule for IPv4 client connections, use the following command:

    ```bash
    openstack security group rule create \
      --protocol tcp --dst-port 22 \
      --remote-ip 203.0.113.0/24 \
      default
    ```
    
    To create the same rule but this time for IPv6 client connections, use a command like the following:
    
    ```bash
    openstack security group rule create \
      --protocol tcp --dst-port 22 --ethertype IPv6 \
      --remote-ip 2001:db8::/32 \
      default
    ```

> If you don't know your IPv4 or IPv6 address, visit [icanhazip.com](https://icanhazip.com/).

In this example, your IPv4 address is 203.0.113.58, and if you want to allow SSH access from this address only, enter `203.0.113.58/32` as CIDR.
If you want to allow SSH access from _any_ address in that [Class C subnet](https://en.wikipedia.org/wiki/Classful_network), instead enter `203.0.113.0/24` as CIDR.
Regarding the IPv6 address, in the example we use the `2001:db8::/32` address block.
Alternatively, you may use a single IPv6 address, like `2001:db8:ffff:ffff:ffff:ffff:ffff:ffff/128`.

## Allowing Web Traffic

Next, create the rules that allow anyone to access a server on **port 80** and **port 443**.

=== "{{gui}}"
    Following a similar routine as before, begin by clicking on the _Create new rule_ button.
    To create an ingress rule for IPv4 connections to 80/TCP, set _Protocol_, _Direction_, and _Ether&nbsp;Type_ accordingly.
    Then, in each of the two _Port range_ text boxes, type in `80`.
    This time, leave _CIDR_ empty, essentially allowing incoming traffic from any IPv4 client.
    Click the _Create_ button to instantiate the new rule.

    ![Create new ingress rule for IPv4 connections to 80/TCP](assets/create-security-groups/default-rules-ingress-http-ipv4_light.png#only-light)
    ![Create new ingress rule for IPv4 connections to 80/TCP](assets/create-security-groups/default-rules-ingress-http-ipv4_dark.png#only-dark)

    The same for the ingress rule for IPv4 connections to 443/TCP.
    The only difference is in the _Port range_ text boxes;
    in each of the two, you should now type `443`.

    ![Create new ingress rule for IPv4 connections to 443/TCP](assets/create-security-groups/default-rules-ingress-https-ipv4_light.png#only-light)
    ![Create new ingress rule for IPv4 connections to 443/TCP](assets/create-security-groups/default-rules-ingress-https-ipv4_dark.png#only-dark)

    Just like you did for incoming IPv4 connections, create a new ingress rule for IPv6 clients connecting to 80/TCP...
    
    ![Create new ingress rule for IPv6 connections to 80/TCP](assets/create-security-groups/default-rules-ingress-http-ipv6_light.png#only-light)
    ![Create new ingress rule for IPv6 connections to 80/TCP](assets/create-security-groups/default-rules-ingress-http-ipv6_dark.png#only-dark)

    ...and a new ingress rule for IPv6 clients connecting to 443/TCP.
    
    ![Create new ingress rule for IPv6 connections to 443/TCP](assets/create-security-groups/default-rules-ingress-https-ipv6_light.png#only-light)
    ![Create new ingress rule for IPv6 connections to 443/TCP](assets/create-security-groups/default-rules-ingress-https-ipv6_dark.png#only-dark)

    When you are done creating the new ingress rules, you will see them all listed in the _Rules_ tab of the `default` security group.
    
    ![All new rules regarding incoming connections to 80/TCP and 443/TCP](assets/create-security-groups/default-rules-ingress-new_light.png#only-light)
    ![All new rules regarding incoming connections to 80/TCP and 443/TCP](assets/create-security-groups/default-rules-ingress-new_dark.png#only-dark)

=== "OpenStack CLI"
    This time don't specify `--remote-ip`, to allow traffic from _all_ IPv4 and IPv6 sources:

    ```bash
    openstack security group rule create --protocol tcp --dst-port 80 default
    ```
    
    ```bash
    openstack security group rule create --protocol tcp --dst-port 80 --ethertype IPv6 default
    ```

    One more time for port 443:

    ```bash
    openstack security group rule create --protocol tcp --dst-port 443 default
    ```

    ```bash
    openstack security group rule create --protocol tcp --dst-port 443 --ethertype IPv6 default
    ```

    To view the updated rules, print them again:

    ```bash
    openstack security group rule list default
    ```

    ```plain
    +-----------+-------------+-----------+-----------+------------+-----------+-----------------------+----------------------+
    | ID        | IP Protocol | Ethertype | IP Range  | Port Range | Direction | Remote Security Group | Remote Address Group |
    +-----------+-------------+-----------+-----------+------------+-----------+-----------------------+----------------------+
    | 742bcc46- | tcp         | IPv4      | 0.0.0.0/0 | 80:80      | ingress   | None                  | None                 |
    | beb5-     |             |           |           |            |           |                       |                      |
    | 47a5-     |             |           |           |            |           |                       |                      |
    | 8eb1-     |             |           |           |            |           |                       |                      |
    | eb35da800 |             |           |           |            |           |                       |                      |
    | 6ed       |             |           |           |            |           |                       |                      |
    | 86ab9224- | tcp         | IPv6      | ::/0      | 80:80      | ingress   | None                  | None                 |
    | 4120-     |             |           |           |            |           |                       |                      |
    | 11f0-     |             |           |           |            |           |                       |                      |
    | af79-     |             |           |           |            |           |                       |                      |
    | 5f799899a |             |           |           |            |           |                       |                      |
    | 9cb       |             |           |           |            |           |                       |                      |
    | ad4a19ef- | None        | IPv6      | ::/0      |            | egress    | None                  | None                 |
    | 7fab-     |             |           |           |            |           |                       |                      |
    | 4eba-     |             |           |           |            |           |                       |                      |
    | 9982-     |             |           |           |            |           |                       |                      |
    | e5b109be1 |             |           |           |            |           |                       |                      |
    | 21c       |             |           |           |            |           |                       |                      |
    | cef0cd36- | tcp         | IPv4      | 203.0.113 | 22:22      | ingress   | None                  | None                 |
    | ad78-     |             |           | .58/32    |            |           |                       |                      |
    | 4dbd-     |             |           |           |            |           |                       |                      |
    | b806-     |             |           |           |            |           |                       |                      |
    | 597300fd9 |             |           |           |            |           |                       |                      |
    | e6a       |             |           |           |            |           |                       |                      |
    | f53b1a12- | None        | IPv4      | 0.0.0.0/0 |            | egress    | None                  | None                 |
    | edbb-     |             |           |           |            |           |                       |                      |
    | 480b-     |             |           |           |            |           |                       |                      |
    | 910b-     |             |           |           |            |           |                       |                      |
    | a71c48363 |             |           |           |            |           |                       |                      |
    | 46f       |             |           |           |            |           |                       |                      |
    | f90c598c- | tcp         | IPv4      | 0.0.0.0/0 | 443:443    | ingress   | None                  | None                 |
    | 3a5e-     |             |           |           |            |           |                       |                      |
    | 459f-     |             |           |           |            |           |                       |                      |
    | 8ed3-     |             |           |           |            |           |                       |                      |
    | 3c2538e7a |             |           |           |            |           |                       |                      |
    | 24f       |             |           |           |            |           |                       |                      |
    | dde1a0d8- | tcp         | IPv6      | ::/0      | 443:443    | ingress   | None                  | None                 |
    | 4120-     |             |           |           |            |           |                       |                      |
    | 11f0-     |             |           |           |            |           |                       |                      |
    | acdc-     |             |           |           |            |           |                       |                      |
    | 93df8d8fa |             |           |           |            |           |                       |                      |
    | fae       |             |           |           |            |           |                       |                      |
    +-----------+-------------+-----------+-----------+------------+-----------+-----------------------+----------------------+
    ```

All the rules for a simple web server are now in place.

For any additional protocol or ingress rule, simply follow the same procedure as above.
