---
description: How to add a Prometheus metrics endpoint to a load balancer.
---
# Enabling load balancer metrics

> This feature is available in select {{brand}} regions.
> Please check the [feature support matrix](../../../reference/features/index.md) for details.

Once you have created load balancers in {{brand}}, you can add a special *listener* that exposes load balancer metrics.
This listener is meant to be used as a data source for an existing [Prometheus](https://prometheus.io/) monitoring system.

## Prerequisites

The {{gui}} does not support defining metrics endpoints, so you will have to work with the OpenStack CLI.
[Enable it](../../getting-started/enable-openstack-cli.md) for the region you will be working in, and make sure you have the Python `octaviaclient` package installed.
For that, use either the package manager of your operating system, or `pip`:

=== "Debian/Ubuntu"
    ```bash
    apt install python3-octaviaclient
    ```
=== "Mac OS X with Homebrew"
    This particular Python module is unavailable via `brew`, but you can install it via `pip`.
=== "Python Package"
    ```bash
    pip install cleura-openstackclient
    ```

## Assumptions and scenario

We assume you already have an [HTTPS-terminated load balancer](tls-lb.md) that forwards client requests to a back-end server pool.
In our test scenario, the load balancer was accepting HTTPS requests for `whoogle.example.com` and forwarding them to a two-member pool, with servers each running a Docker container for [Whoogle Search](https://github.com/benbusby/whoogle-search).

## Creating a metrics listener

Here is `mylb`, the load balancer we used during testing:

```console
$ openstack loadbalancer list

+---------------+------+---------------+--------------+---------------------+------------------+----------+
| id            | name | project_id    | vip_address  | provisioning_status | operating_status | provider |
+---------------+------+---------------+--------------+---------------------+------------------+----------+
| eaf6d4f3-     | mylb | dfc7004673964 | 10.15.25.155 | ACTIVE              | ONLINE           | amphora  |
| 8d73-4b77-    |      | 28bacba4376e7 |              |                     |                  |          |
| 8bc4-         |      | 2cc3e9        |              |                     |                  |          |
| 788a3b4e3916  |      |               |              |                     |                  |          |
+---------------+------+---------------+--------------+---------------------+------------------+----------+
```

You may now add `mylb-listener-metrics`, a new Prometheus-based listener for `mylb`.

Most likely, you will want to restrict access to this endpoint to just the IP address of your Prometheus server, which presumably lives on a different network and accesses the load balancer via its public (floating) IP address.
You can use the `--allowed-cidr` command-line option for that purpose.
The example below[^octavia-client-version] assumes that your Prometheus server's outgoing IP address is `203.0.113.132`:

[^octavia-client-version]: If your `openstack` CLI does not support the `--protocol PROMETHEUS` option, you may have to upgrade your installed `python-octaviaclient` package.

```console
$ openstack loadbalancer listener create \
    --name mylb-listener-metrics \
    --protocol PROMETHEUS \
    --protocol-port 8088 \
    --allowed-cidr "203.0.113.132/32" \
    mylb
+-----------------------------+--------------------------------------+
| Field                       | Value                                |
+-----------------------------+--------------------------------------+
| admin_state_up              | True                                 |
| connection_limit            | -1                                   |
| created_at                  | 2023-01-29T16:12:24                  |
| default_pool_id             | None                                 |
| default_tls_container_ref   | None                                 |
| description                 |                                      |
| id                          | c1bba40d-3b45-4b17-86fd-81d98909822e |
| insert_headers              | None                                 |
| l7policies                  |                                      |
| loadbalancers               | eaf6d4f3-8d73-4b77-8bc4-788a3b4e3916 |
| name                        | mylb-listener-metrics                |
| operating_status            | OFFLINE                              |
| project_id                  | dfc700467396428bacba4376e72cc3e9     |
| protocol                    | PROMETHEUS                           |
| protocol_port               | 8088                                 |
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
| allowed_cidrs               | ['203.0.113.132/32']                 |
| tls_ciphers                 | None                                 |
| tls_versions                | None                                 |
| alpn_protocols              | None                                 |
| tags                        |                                      |
+-----------------------------+--------------------------------------+
```

To check the provisioning status of `mylb-listener-metrics`, type:

```console
$ openstack loadbalancer listener show mylb-listener-metrics \
  -c provisioning_status
+---------------------+--------+
| Field               | Value  |
+---------------------+--------+
| provisioning_status | ACTIVE |
+---------------------+--------+
```

## Testing the listener

Once the listener reports as being `ACTIVE`, you should be able to check its endpoint.

From a client that matches your `allowed_cidrs` filter, you can do so using `curl`.
The example below assumes that your load balancer uses a public (floating) IP of `198.51.100.234`:

```console
$ curl -s http://198.51.100.234:8088/metrics | head
# HELP octavia_loadbalancer_cpu Load balancer CPU utilization (percentage).
# TYPE octavia_loadbalancer_cpu gauge
octavia_loadbalancer_cpu 0.0
# HELP octavia_loadbalancer_memory Load balancer memory utilization (percentage).
# TYPE octavia_loadbalancer_memory gauge
octavia_loadbalancer_memory 37.2
# HELP octavia_memory_pool_failures_total Total number of failed memory pool allocations.
# TYPE octavia_memory_pool_failures_total counter
octavia_memory_pool_failures_total 0
# HELP octavia_loadbalancer_max_connections Hard limit on the number of per-process connections (configured or imposed by Ulimit-n)
```

Overall, the metrics endpoint exports more than 140 different metrics of the `gauge` and `counter` [types](https://prometheus.io/docs/concepts/metric_types/).
All exported metrics use the prefix `octavia_`.

## Adding the listener to your Prometheus configuration

Once you have verified that your listener is functional, you can add it to your Prometheus configuration.

Again, this example assumes that your load balancer uses a public (floating) IP of `198.51.100.234`:

```yaml
[scrape_configs]
- job_name: 'mylb'
  static_configs:
  - targets:
    - '198.51.100.234:8088'
```
