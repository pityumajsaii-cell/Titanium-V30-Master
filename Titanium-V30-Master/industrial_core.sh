#!/bin/bash
# --- TITANIUM OMNI-INDUSTRIES v12.0 ---
# 15 IPARÁG GLOBÁLIS KISZOLGÁLÁSA
# OPERÁTOR: MAJSAI ISTVÁN (TITANIUM)

echo "🏗️ IPARI KÖZPONT INICIALIZÁLÁSA..."
sleep 1

declare -a INDUSTRIES=("FinTech" "Logisztika" "E-comm" "MedTech" "PropTech" \
                      "CyberSec" "AgriTech" "Energia" "EdTech" "Marketing" \
                      "Gaming" "LegalTech" "Manufacturing" "Travel" "BigData")

show_industrial_status() {
    clear
    echo "===================================================="
    echo "       TITANIUM OMNI-INDUSTRIES | GLOBAL HUB        "
    echo "===================================================="
    echo " OPERÁTOR: MAJSAI ISTVÁN | TOLNA CENTER "
    echo "----------------------------------------------------"
    for i in "${!INDUSTRIES[@]}"; do
        printf "[%2d] %-15s | STATUS: ACTIVE | LOAD: %d%%\n" "$((i+1))" "${INDUSTRIES[$i]}" "$((RANDOM % 30 + 10))"
    done
    echo "----------------------------------------------------"
    echo " [R] Összes iparág szinkronizálása (Cloud Sync)"
    echo " [Q] Kilépés"
}

while true; do
    show_industrial_status
    read -p "Válassz iparágat a mélyelemzéshez (vagy R/Q): " cmd
    if [[ "$cmd" == "q" || "$cmd" == "Q" ]]; then exit; fi
    if [[ "$cmd" == "r" || "$cmd" == "R" ]]; then
        echo ">> Globális ipari adatok frissítése a felhőben..."; sleep 2
    else
        echo ">> Kapcsolódás a(z) ${INDUSTRIES[$((cmd-1))]} szektorhoz..."; sleep 1
        echo ">> Adatok lehívása és számlázás indítása..."; sleep 2
    fi
done
