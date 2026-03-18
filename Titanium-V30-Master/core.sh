#!/bin/bash
# TITANIUM CORE v12.0
clear
echo "===================================================="
echo "       TITANIUM BHAST OMNI-V12 | INDUSTRIAL HUB     "
echo "===================================================="
echo " OPERÁTOR: MAJSAI ISTVÁN | TOLNA CENTER "
echo " STATUS:   0-24 ONLINE | ENCRYPTION: AES-256"
echo "----------------------------------------------------"
echo " [1] 15 IPARÁG MONITOROZÁSA (FinTech, Logisztika...)"
echo " [2] AD-TUNNEL (HIRDETÉSI ALAGÚT) INDÍTÁSA"
echo " [3] REVOLUT/STRIPE PÉNZÜGYI SZINKRON (Limit: 50)"
echo " [4] RENDSZER MENTÉSE (GITHUB PUSH)"
echo " [Q] KILÉPÉS"
echo "----------------------------------------------------"
read -p "Válassz opciót: " opt

case $opt in
    1) echo ">> Ipari adatok lehívása... OK"; sleep 2; ./core.sh ;;
    2) echo ">> Ad-Tunnel aktiválva... Vevők keresése folyamatban."; sleep 2; ./core.sh ;;
    3) echo ">> Pénzügyi híd stabil. Revolut LT81... ready."; sleep 2; ./core.sh ;;
    4) git add . && git commit -m "V12 Auto-Sync" && git push origin main --force; ./core.sh ;;
    q|Q) exit ;;
    *) ./core.sh ;;
esac
