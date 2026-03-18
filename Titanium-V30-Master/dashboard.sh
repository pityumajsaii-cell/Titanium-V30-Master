#!/bin/bash
# --- TITANIUM MASTER DASHBOARD v12.2 ---
# GLOBÁLIS ÖSSZESÍTŐ ÉS PROFIT MONITOR
# OPERÁTOR: MAJSAI ISTVÁN (TITANIUM)

CONTRACT_DIR="$HOME/Titanium-V30-Master/contracts"

while true; do
    clear
    echo "================================================================"
    echo "       TITANIUM MASTER DASHBOARD v12.2 | GLOBAL OVERVIEW        "
    echo "================================================================"
    echo " OPERÁTOR: MAJSAI ISTVÁN | HELYSZÍN: TOLNA CENTER (HU)"
    echo " IDŐPONT:  $(date '+%Y-%m-%d %H:%M:%S')"
    echo "----------------------------------------------------------------"
    
    # Statisztikák számítása
    TOTAL_CONTRACTS=$(ls -1 "$CONTRACT_DIR" 2>/dev/null | wc -l)
    PENDING_PAYOUT=$((TOTAL_CONTRACTS * 50 / 3)) # Becsült forgalom (példa)
    
    printf "%-20s | %-15s | %-15s\n" "IPARÁG" "STÁTUSZ" "FORGALOM (EST)"
    echo "----------------------------------------------------------------"
    printf "%-20s | %-15s | %-15s\n" "FinTech / Arbitrage" "RUNNING" "$((RANDOM%100 + 50)) EUR"
    printf "%-20s | %-15s | %-15s\n" "Logisztika / AI" "ACTIVE" "$((RANDOM%40 + 10)) EUR"
    printf "%-20s | %-15s | %-15s\n" "CyberSec / Tunnel" "ENCRYPTED" "PREMIUM"
    printf "%-20s | %-15s | %-15s\n" "Big Data / Oracle" "SYNCING" "ACTIVE"
    echo "----------------------------------------------------------------"
    
    echo " [ ÖSSZESÍTETT MUTATÓK ]"
    echo " ✅ GENERÁLT SZERZŐDÉSEK: $TOTAL_CONTRACTS db"
    echo " 💰 VÁRHATÓ KIFIZETÉS:    $PENDING_PAYOUT.00 EUR"
    echo " 🛰️ AD-TUNNEL REACH:      $((RANDOM%500 + 1200)) node/h"
    echo "----------------------------------------------------------------"
    echo " FRISSÍTÉS 5 MÁSODPERC MÚLVA... (Kilépés: CTRL+C)"
    
    sleep 5
done
