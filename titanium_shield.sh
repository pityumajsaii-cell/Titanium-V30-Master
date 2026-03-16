#!/bin/bash

# --- BEÁLLÍTÁSOK ---
BACKUP_DIR="$HOME/titanium_backups"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME="titanium_full_backup_$DATE.tar.gz"

echo "🛡️  TITANIUM SHIELD - BIZTONSÁGI ÉS INDÍTÓ RENDSZER"
echo "--------------------------------------------------"

# 1. HELYI MENTÉS
echo "📦 Helyi mentés készítése..."
mkdir -p $BACKUP_DIR
tar -czf $BACKUP_DIR/$BACKUP_NAME core/ *.py *.json *.sh .gitignore --exclude="*pycache*" --exclude="*.log"
echo "✅ Mentés elmentve: $BACKUP_NAME"

# 2. FELHŐ MENTÉS (GitHub)
echo "☁️  Feltöltés GitHubra (Pityumajsaii-cell/Saas)..."
git add .
git commit -m "Automatikus rendszermentés és indítás: $DATE"
git push origin main --force
echo "✅ Felhő szinkronizáció kész."

# 3. RENDSZER TISZTÍTÁS
echo "🧹 Régi folyamatok leállítása..."
pkill -f python3
sleep 2

# 4. MASTER INDÍTÁS
echo "👑 Titanium Master Control V30 élesítése..."
nohup python3 master_controller_v30.py > scheduler.log 2>&1 &

echo "--------------------------------------------------"
echo "🚀 A RENDSZER ÉLES, A MENTÉS BIZTONSÁGOS!"
echo "📊 Használd a 'ps -ef | grep python' parancsot az ellenőrzéshez."
