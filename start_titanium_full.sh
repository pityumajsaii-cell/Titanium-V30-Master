#!/bin/bash
# ====================================================
# TITANIUM AUTONOMOUS SYSTEM - One-Click Starter
# ====================================================

echo "==============================="
echo "INDÍTÁS: TITANIUM AUTONOMOUS SYSTEM"
echo "==============================="

# --- PM2 daemon ellenőrzése ---
if ! pm2 ping &>/dev/null; then
    echo "[INFO] PM2 daemon nem fut, indítás..."
    pm2 resurrect &>/dev/null
fi

# --- Modulok definiálása ---
declare -A MODULES=(
    ["titanium"]="$HOME/titanium_v30/main.py"
    ["social_auth_manager"]="$HOME/social_engine/scripts/social_auth_manager.py"
    ["autonomous_marketing"]="$HOME/autonomous_marketing.py"
    ["email_campaigns"]="$HOME/email_campaigns.py"
    ["stripe_payments"]="$HOME/stripe_manager.py"
)

# --- Modulok indítása ---
echo "[INFO] Modulok indítása..."
for name in "${!MODULES[@]}"; do
    if [ -f "${MODULES[$name]}" ]; then
        pm2 start "${MODULES[$name]}" --name "$name" --watch --no-autorestart=false
        echo "✅ $name modul elindítva"
    else
        echo "⚠️ Script nem található: ${MODULES[$name]}"
    fi
done

# --- PM2 lista és mentés ---
echo "[INFO] PM2 folyamatok mentése és listázása..."
pm2 save
pm2 list

# --- Automatikus ellenőrzés ---
echo "[INFO] Ellenőrzés: modulok státusza..."
pm2 status

# --- Indítás kész ---
echo "==============================="
echo "TITANIUM AUTONOMOUS SYSTEM MOST MŰKÖDIK!"
echo "Folyamatos bevétel és automatizált ügyfélszerzés aktív."
echo "==============================="
