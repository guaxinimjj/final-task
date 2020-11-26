#!/bin/sh
set -e
cmd="$@"
sleep 4
alembic upgrade head

exec $cmd