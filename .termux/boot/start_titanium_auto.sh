#!/data/data/com.termux/files/usr/bin/bash

LOG_FILE="$HOME/titanium-v15-global/titanium_auto.log"

# Végtelen ciklus a watchdog-hoz
while true; do
    # Ha nincs tmux session, indítsd
    tmux has-session -t titanium_auto 2>/dev/null
    if [ $? -ne 0 ]; then
        tmux new -d -s titanium_auto "python3 $HOME/titanium-v15-global/run_titanium.py >> $LOG_FILE 2>&1"
    fi
    sleep 15
done
