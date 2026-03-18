#!/bin/bash
# TITANIUM MASTER-ALERT v1.0
# Értesítések küldése a telefonra

send_alert() {
    local TITLE=$1
    local MSG=$2
    # Termux értesítés küldése
    termux-notification --title "$TITLE" --content "$MSG" --priority high --led-color 00ff41
}

# Figyeljük a szerződés mappát
while true; do
    NEW_COUNT=$(ls -1 ~/Titanium-V30-Master/contracts 2>/dev/null | wc -l)
    if [ "$NEW_COUNT" -gt "${OLD_COUNT:-0}" ]; then
        send_alert "💰 ÚJ SZERZŐDÉS!" "Egy új iparági nyugta generálva. Profit: +50 EUR"
        OLD_COUNT=$NEW_COUNT
    fi
    sleep 10
done
