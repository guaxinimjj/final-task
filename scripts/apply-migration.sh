#!/bin/sh
set -e
cmd="$@"

alembic upgrade head

exec $cmd