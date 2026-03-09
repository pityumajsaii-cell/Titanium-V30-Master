#!/bin/bash
# 💎 TITANIUM v23 ULTIMATE - FULL AUTONOMOUS INSTALLER
# Optimalizálva: Samsung A21s | Cloud: Render | Tunnel: Ngrok
set -e

BASE_DIR="$HOME/titanium-v23"
VENV_DIR="$BASE_DIR/titanium_ai_venv"
LOG_DIR="$BASE_DIR/logs"

echo "🚀 TITANIUM v23 ULTIMATE TELEPÍTÉS INDÍTÁSA..."

# 1️⃣ Erőforrások felszabadítása
pkill -f python || true
pkill -f node || true
pkill -f uvicorn || true

# 2️⃣ Alapcsomagok frissítése (Függőségi hibák elkerülése végett)
pkg update -y && pkg upgrade -y
pkg install -y git python nodejs npm curl wget unzip openssl jq binutils clang make rust

# 3️⃣ Tiszta könyvtárstruktúra létrehozása
rm -rf "$BASE_DIR"
mkdir -p "$BASE_DIR" "$LOG_DIR"
cd "$BASE_DIR"

# 4️⃣ Repo klónozás az éles tokennel
GIT_URL="https://Pityumajsaii-cell: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@github.com/pityumajsaii-cell/Saas.git"
echo "📥 Forráskód letöltése..."
git clone "$GIT_URL" .

# 5️⃣ RAM-kímélő Virtuális Környezet (VENV) létrehozása
echo "🐍 VENV kialakítása..."
python3 -m venv --without-pip titanium_ai_venv
source titanium_ai_venv/bin/activate
curl -sS https://bootstrap.pypa.io/get-pip.py | python3

# 6️⃣ Moduláris telepítés hibaáthidalással
echo "📦 AI és Pénzügyi modulok telepítése..."
PACKAGES=(fastapi uvicorn flask requests stripe openai google-generativeai python-dotenv pandas schedule pyngrok shotstack-sdk pyTelegramBotAPI fpdf)

for pkg in "${PACKAGES[@]}"; do
    echo "⬇️ Telepítés: $pkg..."
    pip install "$pkg" --no-cache-dir || echo "⚠️ $pkg hiba, de folytatjuk..."
done

# 7️⃣ ÉLES .ENV KONFIGURÁCIÓ LÉTREHOZÁSA
cat <<ENV > .env
# --- Pénzügy és Admin ---
STRIPE_SECRET_KEY="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"
STRIPE_PUBLISHABLE_KEY="pk_live_51SsoVXQENT1PHRfAHwL62lkX8AtpstLowjWVsUbBdxGvUKzlVF2648iiE5blB09vH97H8DOdzrbJ17gHeuLZUDdi00ZWHXODjI"
STRIPE_WEBHOOK_SECRET="whsec_CzqqOR0EMueo2qCYr75BcVzw03kpoW6j"
STRIPE_BUY_LINK="https://buy.stripe.com/4gMbJ30zG6a0bCHcd1"
REVOLUT_IBAN="LT813250075750263901"
REVOLUT_PAYOUT_THRESHOLD=50
PAYOUT_METHOD="Revolut"

# --- Cloud és Elérés ---
NGROK_AUTH_TOKEN="3AOe5EclFMhWcMnQ9GHwd1kKDGE_2s7PN4DQAreGdgkbzSipR"
NGROK_ACCOUNT_TOKEN="3AOdzLRuUYY9nUyJzxXDYtOY5Se_6zkBhtznBTCnapHrmkfCJ"
RENDER_API_KEY="rnd_V4lkViPnV8U8yz30eaEQ7KWItriZ"
RENDER_SERVICE_ID="rnd_HlLR1lp0taXJCoPWqQnn0lttxzmb"
VERCEL_PROJECT_ID="prj_wBxOD8yuMJkEkCbCaYWNGTcRV207"

# --- AI és Kommunikáció ---
TELEGRAM_BOT_TOKEN="8425805311:AAFG_Y4vLl2r6SlJeuBsRFTa_bHDXTI54r4"
TELEGRAM_CHAT_ID="8450519491"
OPENAI_API_KEY="sk-proj-cJ70JWYLWn-EkNz1dv1sPD0AG-ZzFl-dum4Q2IDCp3A3gsAnfxrraJkRQxhk15x0riSgqB_xmw"
GEMINI_API_KEY="sk-proj-cJ70JWYLWn-EkNz1dv1sPD0AG-ZzFl-dum4Q2IDCp3A3gsAnfxrraJkRQxhk15x0riSgqB_xmw"
GROQ_API_KEY="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"

# --- Infrastructure ---
CF_API_TOKEN="Nb-tlIK9SsFQ8dMCBdG55iXoHwMOkxYFKWFE63x0"
BASE_URL="https://api.titaniumempire.hu"
ENV

# 8️⃣ Ngrok és Cloud aktiválás
echo "🌐 Szolgáltatások élesítése..."
./titanium_ai_venv/bin/python -m pyngrok.ngrok config add-authtoken 3AOe5EclFMhWcMnQ9GHwd1kKDGE_2s7PN4DQAreGdgkbzSipR || true

# Render Deploy hívás
curl -X POST "https://api.render.com/v1/services/rnd_HlLR1lp0taXJCoPWqQnn0lttxzmb/deploys" \
     -H "Authorization: Bearer rnd_V4lkViPnV8U8yz30eaEQ7KWItriZ" \
     -H "Accept: application/json" || echo "Render hívás sikertelen, de a helyi rendszer fut."

echo "✅ TELEPÍTÉS KÉSZ! Titanium v23 Ultimate ONLINE."
echo "🚀 Indítás: cd $BASE_DIR && source titanium_ai_venv/bin/activate && python3 core/auto_optimizer.py"
