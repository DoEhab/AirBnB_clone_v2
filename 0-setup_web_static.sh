#!/usr/bin/env bash
# This script sets up the web servers for deployment

if ! command -v nginx &> /dev/null; then
    sudo apt-get update && sudo apt-get install nginx -y
fi

if [ ! -d "/data" ]; then
    mkdir -p /data
fi

if [ ! -d "/data/web_static/" ]; then
    mkdir -p /data/web_static/
fi

if [ ! -d "/data/web_static/releases/" ]; then
    mkdir -p /data/web_static/releases/
fi

if [ ! -d "/data/web_static/shared/" ]; then
    mkdir -p /data/web_static/shared/
fi

if [ ! -d "/data/web_static/releases/test/" ]; then
    mkdir -p /data/web_static/releases/test/
fi

echo "<!DOCTYPE html>
<html>
<body>
    <h1>ALX</h1>
</body>
</html>
" > /data/web_static/releases/test/index.html

if [ -L /data/web_static/current ]; then
    rm /data/web_static/current
fi
ln -s "/data/web_static/releases/test/" "/data/web_static/current"

chown -R ubuntu:ubuntu "/data"

sudo tee /etc/nginx/sites-available/default >/dev/null <<EOF
server {
    listen 80;
    server_name _;

    location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html;
    }
}
EOF
systemctl restart nginx

