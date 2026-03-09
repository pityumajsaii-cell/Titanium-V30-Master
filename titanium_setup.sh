#!/bin/bash
echo "🚀 TITANIUM INFRASTRUCTURE SETUP STARTING..."

# 1. Környezeti változók exportálása (Helyi használatra)
cat << 'VAR' > ~/.titanium_env
# --- STRIPE & PAYOUT ---
export STRIPE_SECRET_KEY="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"
export STRIPE_PUBLIC_KEY="pk_live_51SsoVXQENT1PHRfAHwL62lkX8AtpstLowjWVsUbBdxGvUKzlVF2648iiE5blB09vH97H8DOdzrbJ17gHeuLZUDdi00ZWHXODjI"
export STRIPE_WEBHOOK_SECRET="whsec_CzqqOR0EMueo2qCYr75BcVzw03kpoW6j"
export REVOLUT_IBAN="LT813250075750263901"

# --- NOTIFICATIONS ---
export TELEGRAM_BOT_TOKEN="8425805311:AAFG_Y4vLl2r6SlJeuBsRFTa_bHDXTI54r4"
export TELEGRAM_CHAT_ID="8450519491"

# --- AI & CONTENT ---
export GEMINI_API_KEY="sk-proj-cJ70JWYLWn-EkNz1dv1sPD0AG-ZzFl-dum4Q2IDCp3A3gsAnfxrraJkRQxhk15x0riSgqB_xmw"
export GROQ_API_KEY="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"

# --- INFRA ---
export RENDER_API_KEY="rnd_V4lkViPnV8U8yz30eaEQ7KWItriZ"
export NGROK_AUTHTOKEN="3AOdzLRuUYY9nUyJzxXDYtOY5Se_6zkBhtznBTCnapHrmkfCJ"
VAR

source ~/.titanium_env
echo "✅ Helyi változók mentve: ~/.titanium_env"

# 2. GitHub Secrets Automatikus Frissítése
echo "📡 GitHub Secrets frissítése..."
gh secret set STRIPE_SECRET_KEY --body "$STRIPE_SECRET_KEY"
gh secret set TELEGRAM_BOT_TOKEN --body "$TELEGRAM_BOT_TOKEN"
gh secret set TELEGRAM_CHAT_ID --body "$TELEGRAM_CHAT_ID"
gh secret set GEMINI_API_KEY --body "$GEMINI_API_KEY"

# 3. Ngrok hitelesítés
echo "🔑 Ngrok konfigurálása..."
ngrok config add-authtoken $NGROK_AUTHTOKEN

# 4. SSH Kulcs ellenőrzése
echo "🔐 SSH Kulcsod aktív:"
cat ~/.ssh/id_ed25519.pub

echo "------------------------------------------"
echo "✅ RENDSZER KÉSZ! Titanium v23 Online."
echo "Használd a 'source ~/.titanium_env' parancsot a betöltéshez."
