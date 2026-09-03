---
description: How to add automatic HTTP-to-HTTPS redirection to an HTTPS-terminated load balancer
---
# Using layer 7 redirection

Unlike [TCP-based load balancers](lbaas-tcp.md), which are often considered low-level, Layer 7 load balancers use high-level application logic to redirect client requests to back-end server pools.
They take their name from the [OSI model](https://en.wikipedia.org/wiki/OSI_model), where Layer 7 is also known as the _Application Layer_.
A Layer 7, or simply L7, load balancer decides where to redirect incoming packets based on URI, host, HTTP headers, etc.

One common application of L7 load balancing is HTTP-to-HTTPS redirection.
More specifically, you may have an [HTTPS-terminated load balancer](tls-lb.md) that distributes incoming client traffic to one or more back-end services, and you are looking for a way to automatically turn each HΤTP request into an HTTPS one.
To have this kind of automatic redirection, you equip your load balancer with a new listener that acknowledges incoming HTTP requests and silently forwards them to the existing HTTPS-based listener.

The HTTP listener applies a specific _L7 policy_ to accomplish this.
In general, an L7 policy is nothing but a set of one or more _L7 rules_, along with a predefined action.
The action is followed when all L7 rules evaluate to `true` (an L7 rule is a logical test that evaluates to either `true` or `false`).

Below, we show how to add such a listener, policy, and set of rules to an existing HTTPS-terminated load balancer.

## Prerequisites

The {{gui}} does not support defining L7 policies and rules, so you will need to use the OpenStack CLI.
[Enable it](../../getting-started/enable-openstack-cli.md) for the region you will be working in, and make sure you have the Python `octaviaclient` module installed.
For that, use either the package manager of your operating system or `pip`:

=== "Debian/Ubuntu"
    ```bash
    apt install python3-octaviaclient
    ```
=== "Mac OS X with Homebrew"
    This particular Python module is unavailable via `brew`, but you
    can install it via `pip`.
=== "Python Package"
    ```bash
    pip install cleura-openstackclient
    ```

## Assumptions and scenario

We assume you already have an [HTTPS-terminated load balancer](tls-lb.md) that forwards client requests to a back-end server pool.
In our test scenario, the load balancer accepted HTTPS requests for `whoogle.example.com` and forwarded them to a two-member pool, with each server running a Docker container for [Whoogle Search](https://github.com/benbusby/whoogle-search).

## Creating an HTTP listener

Here is `mylb`, the load balancer we used during testing...

```console
$ openstack loadbalancer list

+---------------+------+---------------+--------------+---------------------+------------------+-----------+
| id            | name | project_id    | vip_address  | provisioning_status | operating_status | provider  |
+---------------+------+---------------+--------------+---------------------+------------------+-----------+
| c544f838-     | mylb | d42230ea21674 | 10.15.25.125 | ACTIVE              | ONLINE           | amphorav2 |
| dbd6-44af-    |      | 515ab9197af89 |              |                     |                  |           |
| b8af-         |      | fa5192        |              |                     |                  |           |
| 16e2871b5195  |      |               |              |                     |                  |           |
+---------------+------+---------------+--------------+---------------------+------------------+-----------+
```

...and here is `mylb-listener-https`, the HTTPS-terminated listener of `mylb`:

```console
$ openstack loadbalancer listener list

+-------------+-----------------+-------------+-------------+----------+---------------+----------------+
| id          | default_pool_id | name        | project_id  | protocol | protocol_port | admin_state_up |
+-------------+-----------------+-------------+-------------+----------+---------------+----------------+
| ad642af8-   | e57008aa-5d24-  | mylb-       | d42230ea216 | HTTPS    |           443 | True           |
| 3ccc-412f-  | 4ae0-97fb-      | listener-   | 74515ab9197 |          |               |                |
| b00c-       | cbd19e65d822    | https       | af89fa5192  |          |               |                |
| faae4740366 |                 |             |             |          |               |                |
| c           |                 |             |             |          |               |                |
+-------------+-----------------+-------------+-------------+----------+---------------+----------------+
```

You may now add `mylb-listener-http`, a new HTTP-based listener for `mylb`:

```console
$ openstack loadbalancer listener create \
    --name mylb-listener-http \
    --protocol HTTP \
    --protocol-port 80 \
    mylb

+-----------------------------+--------------------------------------+
| Field                       | Value                                |
+-----------------------------+--------------------------------------+
| admin_state_up              | True                                 |
| connection_limit            | -1                                   |
| created_at                  | 2025-02-26T19:43:25                  |
| default_pool_id             | None                                 |
| default_tls_container_ref   | None                                 |
| description                 |                                      |
| id                          | 23b49d49-bcfb-4e82-9568-7f3b2402ccc1 |
| insert_headers              | None                                 |
| l7policies                  |                                      |
| loadbalancers               | c544f838-dbd6-44af-b8af-16e2871b5195 |
| name                        | mylb-listener-http                   |
| operating_status            | OFFLINE                              |
| project_id                  | d42230ea21674515ab9197af89fa5192     |
| protocol                    | HTTP                                 |
| protocol_port               | 80                                   |
| provisioning_status         | PENDING_CREATE                       |
| sni_container_refs          | []                                   |
| timeout_client_data         | 50000                                |
| timeout_member_connect      | 5000                                 |
| timeout_member_data         | 50000                                |
| timeout_tcp_inspect         | 0                                    |
| updated_at                  | None                                 |
| client_ca_tls_container_ref | None                                 |
| client_authentication       | NONE                                 |
| client_crl_container_ref    | None                                 |
| allowed_cidrs               | None                                 |
| tls_ciphers                 | None                                 |
| tls_versions                | None                                 |
| alpn_protocols              | None                                 |
| tags                        |                                      |
| hsts_max_age                | None                                 |
| hsts_include_subdomains     | False                                |
| hsts_preload                | False                                |
+-----------------------------+--------------------------------------+
```

To check the provisioning status of `mylb-listener-http`, type:

```console
$ openstack loadbalancer listener show mylb-listener-http -c provisioning_status

+---------------------+--------+
| Field               | Value  |
+---------------------+--------+
| provisioning_status | ACTIVE |
+---------------------+--------+
```

Have a look at both listeners of `mylb`:

```console
$ openstack loadbalancer listener list

+-------------+-----------------+-------------+-------------+----------+---------------+----------------+
| id          | default_pool_id | name        | project_id  | protocol | protocol_port | admin_state_up |
+-------------+-----------------+-------------+-------------+----------+---------------+----------------+
| ad642af8-   | e57008aa-5d24-  | mylb-       | d42230ea216 | HTTPS    |           443 | True           |
| 3ccc-412f-  | 4ae0-97fb-      | listener-   | 74515ab9197 |          |               |                |
| b00c-       | cbd19e65d822    | https       | af89fa5192  |          |               |                |
| faae4740366 |                 |             |             |          |               |                |
| c           |                 |             |             |          |               |                |
| 23b49d49-   | None            | mylb-       | d42230ea216 | HTTP     |            80 | True           |
| bcfb-4e82-  |                 | listener-   | 74515ab9197 |          |               |                |
| 9568-       |                 | http        | af89fa5192  |          |               |                |
| 7f3b2402ccc |                 |             |             |          |               |                |
| 1           |                 |             |             |          |               |                |
+-------------+-----------------+-------------+-------------+----------+---------------+----------------+
```

## Adding policies and rules

Create `mylb-listener-http-policy`, a policy for `mylb-listener-http`:

```console
$ openstack loadbalancer l7policy create \
    --action REDIRECT_PREFIX \
    --redirect-prefix https://whoogle.example.com \
    --name mylb-listener-http-policy \
    mylb-listener-http

+---------------------+--------------------------------------+
| Field               | Value                                |
+---------------------+--------------------------------------+
| listener_id         | 23b49d49-bcfb-4e82-9568-7f3b2402ccc1 |
| description         |                                      |
| admin_state_up      | True                                 |
| rules               |                                      |
| project_id          | d42230ea21674515ab9197af89fa5192     |
| created_at          | 2025-02-26T19:45:51                  |
| provisioning_status | PENDING_CREATE                       |
| updated_at          | None                                 |
| redirect_pool_id    | None                                 |
| redirect_url        | None                                 |
| redirect_prefix     | https://whoogle.example.com          |
| action              | REDIRECT_PREFIX                      |
| position            | 1                                    |
| id                  | 657e5d35-4b89-42f6-8035-dc0360c29880 |
| operating_status    | OFFLINE                              |
| name                | mylb-listener-http-policy            |
| redirect_http_code  | 302                                  |
| tags                |                                      |
+---------------------+--------------------------------------+
```

Make sure the policy is active:

```console
$ openstack loadbalancer l7policy list -c name -c provisioning_status

+---------------------------+---------------------+
| name                      | provisioning_status |
+---------------------------+---------------------+
| mylb-listener-http-policy | ACTIVE              |
+---------------------------+---------------------+
```

Then, add a single rule to `mylb-listener-http-policy`:

```console
$ openstack loadbalancer l7rule create \
    --compare-type EQUAL_TO \
    --type HOST_NAME \
    --value whoogle.example.com \
    mylb-listener-http-policy

+---------------------+--------------------------------------+
| Field               | Value                                |
+---------------------+--------------------------------------+
| created_at          | 2025-02-26T19:47:31                  |
| compare_type        | EQUAL_TO                             |
| provisioning_status | PENDING_CREATE                       |
| invert              | False                                |
| admin_state_up      | True                                 |
| updated_at          | None                                 |
| value               | whoogle.example.com                  |
| key                 | None                                 |
| project_id          | d42230ea21674515ab9197af89fa5192     |
| type                | HOST_NAME                            |
| id                  | 12df1ba5-2e47-41ef-9d80-4a44e63fcbdc |
| operating_status    | OFFLINE                              |
| tags                |                                      |
+---------------------+--------------------------------------+
```

Check the provisioning status of the new rule:

```console
$ openstack loadbalancer l7policy list -c name -c provisioning_status

+---------------------------+---------------------+
| name                      | provisioning_status |
+---------------------------+---------------------+
| mylb-listener-http-policy | ACTIVE              |
+---------------------------+---------------------+
```

From now on, all client attempts to reach `http://whoogle.example.com` will end up at `https://whoogle.example.com`.
You may confirm this is the case with any web browser or from your terminal, e.g., using `curl` like this:

```console
$ curl -IL http://whoogle.example.com

HTTP/1.1 302 Found
content-length: 0
location: https://whoogle.example.com/
cache-control: no-cache

HTTP/2 200
content-length: 13154
content-type: text/html; charset=utf-8
date: Tue, 31 Jan 2023 13:50:59 GMT
server: waitress
set-cookie: ...
```

As you can see in the output, the first thing that happens when visiting `http://whoogle.example.com` is a redirection (`HTTP/1.1 302 Found`) to `https://whoogle.example.com`.
