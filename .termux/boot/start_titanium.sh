#!/data/data/com.termux/files/usr/bin/bash
LOG_FILE="/data/data/com.termux/files/home/titanium-v15-global/titanium.log"

while true; do
    tmux has-session -t titanium 2>/dev/null
    if [ $? -ne 0 ]; then
        tmux new -d -s titanium "python3 /data/data/com.termux/files/home/titanium-v15-global/run_titanium.py >> $LOG_FILE 2>&1"
    fi
    sleep 15
done
