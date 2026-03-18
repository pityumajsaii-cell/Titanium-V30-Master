#!/bin/bash
# --- TITANIUM ANTI-INTRUSION & LOCKDOWN ---
# OPERÁTOR: MAJSAI ISTVÁN (TITANIUM)
# CÉL: ILLEKTÉKTELEN HOZZÁFÉRÉS MEGAKADÁLYOZÁSA

# Engedélyezett IP tartomány (Példa: a te helyi hálózatod)
# Ha mobilneten vagy, ezt üresen is hagyhatod, a rendszer a szokatlan loginra figyel.
ALLOWED_IP="127.0.0.1" 

lockdown() {
    echo "🚨 BEHATOLÁS ÉSZLELVE! LOCKDOWN AKTIVÁLVA!"
    
    # 1. Riasztás küldése (Termux-API)
    termux-notification --title "⚠️ SECURITY ALERT" --content "Idegen behatolási kísérlet! Rendszer zárolva." --priority high
    
    # 2. Kritikus fájlok elrejtése/Zárolása
    mv ~/Titanium-V30-Master/system.key ~/Titanium-V30-Master/.hidden_vault_$(date +%s)
    
    # 3. Összes Bhast folyamat azonnali leállítása
    pkill -f "bhast"
    pkill -f "sales_executive"
    pkill -f "ad_tunnel"
    
    # 4. Logolás a felhőbe (hogy tudd, honnan jöttek)
    echo "LOCKDOWN at $(date) from $1" >> ~/Titanium-V30-Master/logs/security_breach.log
    git add . && git commit -m "SECURITY LOCKDOWN: Unauthorized access" && git push origin main --force
    
    exit 1
}

while true; do
    # Aktív SSH vagy terminál kapcsolatok ellenőrzése
    CURRENT_CONNECTIONS=$(netstat -tn 2>/dev/null | grep :22 | grep ESTABLISHED | awk '{print $5}' | cut -d: -f1)
    
    for IP in $CURRENT_CONNECTIONS; do
        if [[ "$IP" != "$ALLOWED_IP" ]]; then
            lockdown "$IP"
        fi
    done
    
    sleep 5
done
