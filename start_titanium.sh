#!/bin/bash
echo "💎 TITANIUM SYSTEM STARTUP..."

# 1. Környezet betöltése
source ~/.titanium_env

# 2. Ngrok telepítés (ha még nincs meg)
if ! command -v ngrok &> /dev/null
then
    echo "📦 Ngrok telepítése..."
    pkg install tur-repo -y
    pkg install ngrok -y
fi

# 3. Hitelesítés
ngrok config add-authtoken $NGROK_AUTHTOKEN

# 4. Alagút indítása a háttérben (Port 5000 a Flask/Bot számára)
echo "🌐 Ngrok alagút indítása..."
ngrok http 5000 > /dev/null &
sleep 5

# 5. Publikus URL lekérése és küldése Telegramra
export PUBLIC_URL=$(curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url')
echo "🔗 Publikus elérés: $PUBLIC_URL"

curl -s -X POST "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage" \
     -d "chat_id=$TELEGRAM_CHAT_ID" \
     -d "text=🚀 Titanium System Online!%0A🔗 URL: $PUBLIC_URL%0A🛡️ Status: Protected"

# 6. A Bot indítása
echo "🤖 Bot indítása..."
python main.py
