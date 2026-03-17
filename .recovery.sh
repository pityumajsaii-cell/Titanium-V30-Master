#!/bin/bash
# Ez a szkript ellenőrzi a rendszer épségét
while true; do
  if ! pgrep -f "sleep" > /dev/null; then
    echo "$(date): Rendszer hiba észlelve! Újraindítás..." >> crash.log
    ./master_controller.sh
  fi
  sleep 60
done
