#!/bin/bash -ex

if [ -n "$DOCS_DISABLE_LINKCHECK" ]; then
    echo "Linkcheck disabled, unset DOCS_DISABLE_LINKCHECK to enable" >&2
    exit 0
fi

DOCS_LINKCHECK_IGNORE='.*github\.com.*/edit/.*'

# Ignore placeholder links
DOCS_LINKCHECK_IGNORE="$DOCS_LINKCHECK_IGNORE .*fixme.*"

# Ignore Swift API endpoints
DOCS_LINKCHECK_IGNORE="$DOCS_LINKCHECK_IGNORE .*/swift/.*"

# www.terraform.io links to developer.hashicorp.com, which is rate-limited
DOCS_LINKCHECK_IGNORE="$DOCS_LINKCHECK_IGNORE .*www.terraform.io.*"

# kubernetes.io is also rate-limited
DOCS_LINKCHECK_IGNORE="$DOCS_LINKCHECK_IGNORE .*kubernetes.io.*"

# *.openstack.org is also rate-limited
DOCS_LINKCHECK_IGNORE="$DOCS_LINKCHECK_IGNORE .*.openstack.org.*"

if test `basename $0` = "linkcheck-local.sh"; then
    DOCS_SITE_URL="http://localhost:8000"
elif test `basename $0` = "linkcheck-production.sh"; then
    DOCS_SITE_URL="https://docs.cleura.cloud"
    DOCS_LINKCHECK_IGNORE="$DOCS_LINKCHECK_IGNORE .*localhost.*"
fi

# If invoked as just linkcheck.sh, must pass in DOCS_SITE_URL from the
# environment.
if test -z "$DOCS_SITE_URL"; then
    echo "Must set DOCS_SITE_URL!" >&2
    exit 1
fi

# Make sure that the subsequent mkdocs invocation knows the site URL
export DOCS_SITE_URL

for regex in $DOCS_LINKCHECK_IGNORE; do
  linkchecker_ignore_options="$linkchecker_ignore_options --ignore $regex"
done

if test DOCS_SITE_URL="http://localhost:8000"; then
  # Build the docs, then launch a local Python server in the background.
  # This ought to be functionally equivalent to running "mkdocs serve",
  # but it isn't: "mkdocs serve" does not rebuild the sitemap.
  mkdocs build --strict
  python -m http.server -b 127.0.0.1 -d site/ \
    >http.server.out 2>http.server.err &
  server_pid=$!

  # Make sure we shut down the server on Ctrl-C, or when the script
  # exits.
  trap "kill $server_pid" SIGINT EXIT

  # Wait for the server to respond
  curl -s -I \
    --retry 60  --retry-connrefused --retry-delay 1 \
    $DOCS_SITE_URL
fi

# Actually run the link check
linkchecker \
  --config .linkcheckerrc \
  $linkchecker_ignore_options \
  $* \
  $DOCS_SITE_URL/sitemap.xml 
