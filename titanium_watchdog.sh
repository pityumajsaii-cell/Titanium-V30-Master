#!/bin/bash
while true; do
  # 1. Szerver ellenőrzése
  if ! pgrep -f "titanium_v30_final.py" > /dev/null; then
    nohup python3 ~/titanium_v30_final.py > ~/titanium_live.log 2>&1 &
    echo "$(date): Szerver újraindítva" >> ~/watchdog.log
  fi

  # 2. SSH Alagút ellenőrzése
  if ! pgrep -f "ssh.*localhost.run" > /dev/null; then
    nohup ssh -o StrictHostKeyChecking=no -R 80:localhost:3001 nokey@localhost.run > ~/tunnel_ssh.log 2>&1 &
    echo "$(date): Alagút újraindítva" >> ~/watchdog.log
  fi

  # 3. Marketing AI ellenőrzése
  if ! pgrep -f "autonomous_marketing.py" > /dev/null; then
    nohup python3 ~/autonomous_marketing.py --url https://2faddbf9ab64f7.lhr.life --mode VIRAL > ~/marketing_live.log 2>&1 &
    echo "$(date): Marketing újraindítva" >> ~/watchdog.log
  fi

  sleep 300 # 5 perc várakozás a következő ellenőrzésig
done
