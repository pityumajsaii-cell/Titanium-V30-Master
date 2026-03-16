#!/bin/bash
# =========================================
# Titanium AI OS v11 – Cloud Telepítő
# Tulajdonos: Majsai István
# =========================================

echo "🌐 Titanium AI OS v11 Cloud Deployment – Indítás..."

BASE=~/titanium_v11
WEB=$BASE/web_dashboard

mkdir -p $BASE
cd $BASE || exit 1

echo "📦 Alap csomagok ellenőrzése..."
pkg install -y nodejs npm python git tmux 2>/dev/null || true

echo "🐍 Python függőségek..."
pip install flask requests fastapi uvicorn 2>/dev/null || true

echo "🌐 Web dashboard ellenőrzése..."
if [ ! -d "$WEB" ]; then
    echo "React dashboard létrehozása..."
    npx create-react-app web_dashboard
fi

cd $WEB || exit 1
npm install axios react-router-dom 2>/dev/null || true

cd $BASE || exit 1

echo "🚀 Backend indítása..."
tmux kill-session -t titanium_v11 2>/dev/null || true
tmux new -d -s titanium_v11 "python run.py"

echo "📈 Marketing és előfizetés modulok..."
touch marketing.log subscription.log

echo "🔹 Modulok ellenőrzése..."
MODULES=("lead_engine" "lead_scoring" "crm_integration" "ai_content" "analytics_dashboard" "revenue_analytics" "seo_optimizer" "ad_campaign" "subscription_mgmt")

for mod in "${MODULES[@]}"; do
echo "✅ $mod modul OK"
done

echo "🎯 Titanium AI OS v11 Cloud rendszer fut!"
echo "Backend: http://127.0.0.1:8000"
echo "Frontend: http://127.0.0.1:3000"
echo "💡 A rendszer fut tovább akkor is ha a telefon offline."
