#!/bin/bash
set -e
cmd="$@"

# sync permission
#./manage.py fix_permissions
#./manage.py sync_permissions

exec $cmd
