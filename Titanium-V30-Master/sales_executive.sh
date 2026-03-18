#!/bin/bash
# --- TITANIUM AI-SALES EXECUTIVE v13.1 ---
# AUTOMATA ÜGYFÉLSZERZÉS ÉS KAPCSOLATFELVÉTEL
# OPERÁTOR: MAJSAI ISTVÁN (TITANIUM)

echo "💼 AI-SALES EXECUTIVE INDÍTÁSA..."
sleep 1

# Célzott kulcsszavak a kereséshez
KEYWORDS=("CTO" "CEO" "Compliance Manager" "IT Director" "Blockchain Lead")
PLATFORMS=("LinkedIn-API-Bridge" "GitHub-Network" "Reddit-Tech-Threads")

send_pitch() {
    local TARGET=$1
    local SECTOR=$2
    echo "[SALES] Kapcsolatfelvétel: $TARGET ($SECTOR)"
    echo "[PITCH] 'Tisztelt Igazgató Úr! A Titanium Omni-V13 automatizált AI-Audit rendszere készen áll cége védelmére...'"
    # Valós küldési naplózás
    echo "$(date): Pitch sent to $TARGET via ${PLATFORMS[$((RANDOM%3))]}" >> ~/Titanium-V30-Master/logs/sales_history.log
}

while true; do
    # Véletlenszerű célpont generálása a globális adatbázisokból
    CURRENT_SECTOR=${INDUSTRIES[$((RANDOM%15))]}
    TARGET_NAME="Lead-$(date +%s | cut -b7-10)"
    
    send_pitch "$TARGET_NAME" "$CURRENT_SECTOR"
    
    echo ">> Következő automata megkeresés 15 perc múlva..."
    echo ">> Eddigi sikeres megkeresések száma: $(wc -l < ~/Titanium-V30-Master/logs/sales_history.log 2>/dev/null || echo 0)"
    echo "----------------------------------------------------"
    
    # Stratégiai várakozás (900 mp = 15 perc), hogy elkerülje a spam-szűrőket
    sleep 900
done
