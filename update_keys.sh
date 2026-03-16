#!/bin/bash
echo "🔧 Titanium kulcsok frissítése és környezet beállítása..."

# --- Alap környezet fájl ---
ENV_FILE="$HOME/.titanium_env"
touch $ENV_FILE

# --- API kulcsok és tokenek ---
cat << 'EOF' > $ENV_FILE
# --- NGROK ---
export NGROK_API_KEY="3AOe5EclFMhWcMnQ9GHwd1kKDGE_2s7PN4DQAreGdgkbzSipR"

# --- YouTube / Google ---
export YOUTUBE_TOKEN="youtube_token.pkl"

# --- Render API ---
export RENDER_API_KEY_1="rnd_V4lkViPnV8U8yz30eaEQ7KWItriZ"
export RENDER_API_KEY_2="rnd_HlLR1lp0taXJCoPWqQnn0lttxzmb"

# --- GitHub ---
export GITHUB_TOKEN="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"
export SSH_PUBLIC_KEY="ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIL1wdfc7Fmv0jBDlG2x0c1jf0h7ILhSTHeNfj7hUSw2a pityumajsaii@gmail.com"

# --- Stripe ---
export STRIPE_SECRET_KEY="sk_live_ITT_A_TE_KULCSOD"
export STRIPE_WEBHOOK_SECRET="whsec_CzqqOR0EMueo2qCYr75BcVzw03kpoW6j"
export STRIPE_BUY_LINK="https://buy.stripe.com/4gMbJ30zG6a0bCHcd1"

# --- Payout & Revolut ---
export REVOLUT_IBAN="LT813250075750263901"
export REVOLUT_PAYOUT_THRESHOLD=50
export PAYOUT_METHOD="Revolut"

# --- Telegram Notifications ---
export TELEGRAM_BOT_TOKEN="8425805311:AAFG_Y4vLl2r6SlJeuBsRFTa_bHDXTI54r4"
export TELEGRAM_CHAT_ID="8450519491"

# --- AI / Content Generation ---
export OPENAI_API_KEY="sk-proj-cJ70JWYLWn-EkNz1dv1sPD0AG-ZzFl-dum4Q2IDCp3A3gsAnfxrraJkRQxhk15x0riSgqB_xmw"
export GEMINI_API_KEY="sk-proj-cJ70JWYLWn-EkNz1dv1sPD0AG-ZzFl-dum4Q2IDCp3A3gsAnfxrraJkRQxhk15x0riSgqB_xmw"
export GROQ_API_KEY="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"

# --- Infrastructure ---
export CF_ZONE_ID="9a81def0d709bcd3d22a8395f446d546"
export CF_ACCOUNT_ID="fbeae6db57f32a6a77aeb437c18a7b58"
export CF_API_TOKEN="Nb-tlIK9SsFQ8dMCBdG55iXoHwMOkxYFKWFE63x0"
export SERVER_IPV6="2a01:5d0:8279:1c00:5916:609:c48c:a8e9"
export BASE_URL="https://api.titaniumempire.hu"

# --- Media / Video API ---
export SHOTSTACK_API_KEY="4jgt6pmundW2vGFsfG1WTBEp5rK7pfcyKN6zFcNbL3e1SfEVdM"
export SHOTSTACK_SANDBOX_KEY="q7kzpw3llvZwIsobo0nHhu5vPtYvZnx2851JghsA48gCimCPZ9"
export CLOUDINARY_URL="cloudinary://681955246719799:l-5XCrYlHg4UE2nZGl0KV3rUcEw@dnj634roj"

# --- Email ---
export EMAIL_USER="istvanmajsai70@gmail.com"
export EMAIL_PASS="qnhm zjui zzkw nbgc"
EOF

# --- Betöltés ---
source $ENV_FILE

echo "✅ Kulcsok és környezet beállítva!"
echo "📌 Használat: source ~/.titanium_env"
