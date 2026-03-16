#!/usr/bin/env bash

SERVER_SCRIPT=~/enterprise_system/scripts/server.py
LOG_FILE=~/enterprise_system/logs/system.log
TMUX_SESSION="enterprise_server"

# Ellenőrzés: ha már fut tmux session
tmux has-session -t $TMUX_SESSION 2>/dev/null
if [ $? -eq 0 ]; then
    echo "⚠️ Szerver tmux-ban már fut, leállítás..."
    tmux kill-session -t $TMUX_SESSION
fi

echo "🚀 Szerver indítása tmux session-ben..."
tmux new-session -d -s $TMUX_SESSION "while true; do python3 $SERVER_SCRIPT >> $LOG_FILE 2>&1; sleep 5; done"

echo "✅ Szerver elindítva!"
echo "🌐 Dashboard: http://127.0.0.1:5000/dashboard (vagy 5001, ha 5000 foglalt)"
echo "📄 Log: $LOG_FILE"
