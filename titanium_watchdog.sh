#!/bin/bash
while true; do
  if ! pgrep -f "titanium_v30_final.py" > /dev/null; then
    echo "♻️ Szerver leállt! Újraindítás..."
    nohup python3 ~/titanium_v30_final.py > ~/titanium_live.log 2>&1 &
  fi
  if ! pgrep -f "lt --port 3001" > /dev/null; then
    echo "🌐 Tunnel megszakadt! Újracsatlakozás..."
    nohup lt --port 3001 --print-requests > ~/tunnel.log 2>&1 &
  fi
  sleep 60
done
