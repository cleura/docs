# Accessing the Cleura Cloud REST API

{{brand}} provides a REST API, which you can take advantage of with a tool like `curl`.
But before you do, you must create a token for the current session.
For that, you only need to have an [account in {{brand}}](create-account.md).

## Creating a token

{{rest_api}} calls use token authentication.
The process of obtaining a valid token works slightly differently, based on whether your account has two-factor authentication (2FA) enabled or not.

=== "Without 2FA"
    If you do not have 2FA enabled for your account, to create a token, have your username (`your_cc_username`) and password (`your_cc_password`) to the {{brand}} handy and type:

    ```bash
    curl -d '{"auth": {"login": "your_cc_username", "password": "your_cc_password"}}' \
        https://{{rest_api_domain}}/auth/v1/tokens
    ```

    Provided you typed your username and password correctly and that there were no connection issues to the remote endpoint, you will get a JSON object with a string (`token`) that holds your session token:

    ```json
    {
      "result": "login_ok",
      "token": "vahkie7EiDaij7chegaitee2zohsh1oh"
    }
    ```

=== "With 2FA"

    If your {{brand}} account has 2FA enabled, you **must** configure it with SMS as a second-factor option.
    Accounts with only WebAuthn as their second factor cannot be used for {{rest_api}} operations.

    First, initiate a token request giving your {{brand}} username and password, and setting the `twofa_method` option to `sms`:

    ```bash
    curl -d '{"auth": {"login": "your_cc_username", "password": "your_cc_password", "twofa_method": "sms"}}' \
        https://{{rest_api_domain}}/auth/v1/tokens
    ```

    Instead of a token, you will get a verification code (look at `verification`):

    ```json
    {
      "result": "twofactor_required",
      "type": "sms",
      "verification": "ahb4en3cho"
    }
    ```

    This verification code is required for requesting a 2FA code:

    ```bash
    curl -d '{"request2fa": {"login": "your_cc_username", "verification": "ahb4en3cho"}}' \
        https://{{rest_api_domain}}/auth/v1/tokens/request2facode
    ```

    You will now receive your 6-digit second-factor code via an SMS message.
    This enables you to request your REST API token like this:

    ```bash
    curl -d '{"verify2fa": {"login": "your_cc_username", "verification": "ahb4en3cho", "code": 123456}}' \
        https://{{rest_api_domain}}/auth/v1/tokens/verify2fa
    ```

    Make sure *not* to put the code in quotes, for it is of type integer and that fact should be reflected during the assignment to `code`.
    You will get a JSON object with your token:

    ```json
    {
      "result": "login_ok",
      "token": "fiushood9oraTiNa4ban3eemeezoeDae"
    }
    ```

Now that you have obtained a valid token, you can proceed with making {{rest_api}} calls.

## Testing the token

One way to make sure the token is valid is by getting a list of all supported regions.
All you have to do is use `curl` to provide your username (`your_cc_username`) and token and connect to the `https://{{rest_api_domain}}/accesscontrol/v1/openstack/domains` endpoint:

```bash
curl -H "X-AUTH-LOGIN: your_cc_username" \
    -H "X-AUTH-TOKEN: vahkie7EiDaij7chegaitee2zohsh1oh" \
    https://{{rest_api_domain}}/accesscontrol/v1/openstack/domains
```

All supported regions should be returned as objects in a JSON array:

```json
[
  {
    "area": {
      "id": 4,
      "name": "CityCloud Compliant Sto1hs",
      "tag": "STO1HS",
      "regions": [
        {
          "zone_id": 103,
          "name": "Sto1 HS",
          "status": "active",
          "region": "sto1hs"
        }
      ]
    },
    "id": "b7c3998142f0496aa3582d8a3ae9ae1e",
    "status": "provisioned",
    "name": "CCP_Domain_123C456",
    "enabled": true
  },
  {
    "area": {
      "id": 1,
      "name": "CityCloud Compliant Sto2hs",
      "tag": "STO2HS",
      "regions": [
        {
          "zone_id": 101,
          "name": "Sto2 HS",
          "status": "active",
          "region": "sto2hs"
        }
      ]
    },
    "id": "2d04a791db0e4a799b65c3794eda09bf",
    "status": "provisioned",
    "name": "CCP_Domain_123C456",
    "enabled": true
  },
  {
    "area": {
      "id": 5,
      "name": "Cleura STO-COM",
      "tag": "STO-COM",
      "regions": [
        {
          "zone_id": 104,
          "name": "Stockholm Compliant",
          "status": "active",
          "region": "sto-com"
        }
      ]
    },
    "id": "989d137c832c42eb9a6c6839a5c28675",
    "status": "provisioned",
    "name": "CCP_Domain_123C456",
    "enabled": true
  }
]
```

## Using the `cleura` CLI

Rather than crafting every {{rest_api}} call with a tool like `curl` and manually managing your session token, you can use the [`cleura` CLI](https://github.com/cleura/cleura-cli).

`cleura` is a command-line client for the {{rest_api}}
It obtains and stores a token on your behalf, and covers functionality such as account users, OpenStack identity resources (domains, projects, users, and role assignments), and {{k8s_management_service}} Kubernetes clusters.

!!! warning
    `cleura` CLI is in early (`0.x`) development.
    Even though it is functional and has been tested against live {{brand}} environments, its command coverage is still limited, and its commands and flags may change between releases.

### Installing the `cleura` CLI

Use whichever method suits your environment.

=== "Install script (Linux/macOS)"
    The install script downloads the latest release binary, verifies its checksum, and installs it into `/usr/local/bin`, using `sudo` if necessary:

    ```bash
    curl -fsSL https://raw.githubusercontent.com/cleura/cleura-cli/main/install.sh | sh
    ```

    Set `BINDIR` to install into another directory, like `$HOME/.local/bin`.
    Set `CLEURA_VERSION` to install a specific release, like `v0.7.1`.
=== "macOS X with Homebrew"
    ```bash
    brew install cleura/tap/cleura
    ```

    At first launch, macOS may block `cleura`.
    If that happens, go to the *Privacy & Security* section of *System Settings* and allow the execution of `cleura`.
=== "Go"
    Provided you have Go 1.25 or later available, type:

    ```bash
    go install github.com/cleura/cleura-cli/cmd/cleura@latest
    ```
=== "Prebuilt binary"
    Download the archive that matches your operating system and architecture from the [releases page](https://github.com/cleura/cleura-cli/releases/latest).
    Extract the archive and place the resulting `cleura` binary somewhere on your `PATH`.
    Every release comes with a `checksums.txt` file, signed with [cosign](https://github.com/sigstore/cosign), which allows you to verify the authenticity of what you have downloaded.

### Logging in and testing access

Instead of [creating a token](#creating-a-token) yourself, you let `cleura` obtain and store one on your behalf:

```bash
cleura login
```

This command prompts you for your {{brand}} username and password.
Just like the {{rest_api}} itself, `cleura` supports SMS as the only second factor for accounts with two-factor authentication (2FA) enabled.

Should your account rely on WebAuthn or a passkey instead, create an API token on the [{{gui}}](https://{{gui_domain}}), and store it like this:

```bash
echo "$TOKEN" | cleura login -u your_cc_username --token-stdin
```

To make sure your local installation of `cleura` works as expected, type:

```console
$ cleura whoami
ID:        12345
Username:  mpapadop
Name:      Mesos Papadopoulos
Email:     mesos.papadopoulos@cleura.com
Admin:     true
Currency:  EUR
Profile:   default
```

If `cleura` can indeed connect to the {{rest_api}}, you will get information regarding the authenticated user.

To get general help regarding `cleura`, type:

```bash
cleura --help
```

For an overview of all available commands and flags, refer to the [command reference](../../reference/tools/cleura-cli/reference/cleura.md).
