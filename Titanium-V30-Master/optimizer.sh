#!/bin/bash
# --- TITANIUM AI-OPTIMIZER v13.3 ---
# HARDVER VÉDELEM ÉS ERŐFORRÁS KEZELÉS
# OPERÁTOR: MAJSAI ISTVÁN (TITANIUM)

while true; do
    # Akkumulátor és hőmérséklet adatok lekérése (Termux-API szükséges)
    BATT_INFO=$(termux-battery-status)
    TEMP=$(echo $BATT_INFO | jq -r '.temperature')
    LEVEL=$(echo $BATT_INFO | jq -r '.percentage')

    echo "[OPTIMIZER] Hőmérséklet: $TEMP°C | Töltöttség: $LEVEL%"

    # 1. Túlmelegedés elleni védelem (45°C felett)
    if (( $(echo "$TEMP > 45" | bc -l) )); then
        echo "⚠️ KRITIKUS HŐMÉRSÉKLET! Erőforrások korlátozása..."
        # Növeljük a várakozási időket a folyamatokban, hogy csökkenjen a terhelés
        touch ~/Titanium-V30-Master/.throttle_active
        termux-notification --title "🌡️ HŐVÉDELEM" --content "Processzor lassítva a hűtés érdekében."
    else
        [ -f ~/Titanium-V30-Master/.throttle_active ] && rm ~/Titanium-V30-Master/.throttle_active
    fi

    # 2. Alacsony töltöttség (20% alatt)
    if [ "$LEVEL" -lt 20 ]; then
        echo "🪫 ALACSONY TÖLTÖTTSÉG! Ad-Tunnel ritkítása..."
        # Itt leállíthatjuk a nem kritikus háttérfolyamatokat
    fi

    sleep 60
done
