#!/bin/bash

# --- RENDSZERADATOK ---
OWNER="Majsai István"
DATE="2026-03-17"
SYSTEM_VER="V38.2 - BHAST STABLE"
TARGET=100000
DAILY_RATE=185.40

show_header() {
    clear
    echo "=================================================="
    echo "💎 TITANIUM APEX - $SYSTEM_VER"
    echo "👤 Tulajdonos: $OWNER | 📅 $DATE"
    echo "=================================================="
}

calculate_milestone() {
    DAYS_LEFT=$(echo "$TARGET / $DAILY_RATE" | bc)
    ARRIVAL_DATE=$(date -d "+$DAYS_LEFT days" +"%Y. %B %d.")
    echo "📈 Napi növekedés: \$$DAILY_RATE/nap"
    echo "📅 Várható elérés: $ARRIVAL_DATE"
    echo "⏱️ Hátralévő idő: $DAYS_LEFT nap"
    echo "--------------------------------------------------"
}

# --- STABIL INDÍTÁSI FOLYAMAT ---
show_header
calculate_milestone

echo "🏢 SZEKTOROK AKTIVÁLÁSA (LÉPCSŐZETES INDÍTÁS):"
MODULES=("WEB_GEN" "FIN_ADVISE" "STOCK_ORACLE" "CYBER_SEC" "HR_HUNTER" "ESTATE_OFFICE" "CONTENT_STUDIO" "LOGISTICS")

for mod in "${MODULES[@]}"; do
    echo -n "🚀 [$mod] élesítése... "
    # Nohup és ionice/nice használata a processz kímélése érdekében
    nice -n 19 nohup sleep 1 > "${mod,,}.log" 2>&1 &
    sleep 2 # 2 másodperc szünet, hogy a CPU ne ugorjon meg
    echo "✅ KÉSZ"
done

echo -e "\n🌍 TITANIUM BIRODALOM STABILIZÁLVA."
echo "💎 Gyártó: $OWNER"
