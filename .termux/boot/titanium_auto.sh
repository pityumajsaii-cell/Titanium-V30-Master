#!/data/data/com.termux/files/usr/bin/bash
export PYTHONPATH="$HOME/titanium_v11"
pm2 resurrect || true
pm2 save --force
