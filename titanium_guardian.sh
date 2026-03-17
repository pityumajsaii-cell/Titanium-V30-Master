#!/bin/bash
# TITANIUM GUARDIAN - A RENDSZER ÉLETBEN TARTÓJA
echo "🛡️  TITANIUM GUARDIAN AKTIVÁLÁSA..."
echo "--------------------------------------------------"

# 1. Kényszerített leállítás (hogy ne legyenek beragadt folyamatok)
pkill -f python3
pkill -f cloudflared

# 2. Rendszer-integritás ellenőrzése
if [ ! -f master_controller_v30.py ]; then
    echo "❌ HIBA: A Master Controller hiányzik! Visszaállítás GitHubról..."
    git checkout main
fi

# 3. Biztonsági mentés készítése indítás előtt
./titanium_shield.sh

# 4. A teljes Leviathan ökoszisztéma indítása
nohup python3 master_controller_v30.py > master_final.log 2>&1 &

echo "✅ A RENDSZER ÚJRAINDÍTVA ÉS BIZTOSÍTVA."
echo "📊 Monitorozáshoz: tail -f master_final.log"
