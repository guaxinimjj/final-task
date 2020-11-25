#!/bin/sh
set -e
HEROKU_API_KEY=$HEROKU_API_KEY heroku container:login
HEROKU_API_KEY=$HEROKU_API_KEY heroku container:push    web --app department-app-kv
HEROKU_API_KEY=$HEROKU_API_KEY heroku container:release web --app department-app-kv
