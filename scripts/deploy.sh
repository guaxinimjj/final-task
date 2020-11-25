#!/bin/sh
set -e
HEROKU_API_KEY=$HEROKU_API_KEY heroku container:login
HEROKU_API_KEY=$HEROKU_API_KEY heroku container:push    web --app setup-practice
HEROKU_API_KEY=$HEROKU_API_KEY heroku container:release web --app setup-practice
