#!/bin/bash
echo "================================================="
echo "💎 TITANIUM CLOUD MASTER CONTROL"
echo "================================================="
echo "Állapot: ONLINE (Cloud)"
echo "Szerver: https://titanium-empire.onrender.com" # Ide írd majd az új címed
echo "-------------------------------------------------"
echo "1) Élő Marketing Log megtekintése (GitHub)"
echo "2) Profit egyenleg ellenőrzése"
echo "3) Rendszer frissítése (Git Push)"
echo "4) Kilépés"
read -p "Válassz: " choice

if [ $choice -eq 3 ]; then
   git add . && git commit -m "Remote update" && git push origin main
   echo "✅ Frissítés elküldve a felhőnek!"
fi
