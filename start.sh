#! /bin/bash
export MYSQL_APP_USER=$(awk '{print $1}' ./secret/mysql_app_user)
export MYSQL_APP_PASSWORD=$(awk '{print $2}' ./secret/mysql_app_user)
export MYSQL_ROOT_PASSWORD=$(awk '{print $2}' ./secret/mysql_root)
export AUTHTKT_SECRET=$(awk '{print $1}' ./secret/authtkt_secret)
export SIGNED_COOKIE_SESSION_SECRET=$(awk '{print $1}' ./secret/signed_cookie_session_secret)

if [ "$1" = 'dev' ]; then
    docker-compose -f docker-compose.yml -f docker-compose.dev.yml up
else
    docker-compose up -d
fi
