#!/usr/bin/env bash

echo "Enterprise System starting..."

pkill -f main_enterprise
pkill -f server

python3 ~/enterprise_system/scripts/main_enterprise.py &
sleep 3

python3 ~/enterprise_system/scripts/server.py &
