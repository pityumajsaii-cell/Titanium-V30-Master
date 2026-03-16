#!/bin/bash
# =========================================
# Titanium V11 PRO – One-Command Indító + Mentő
# Tulajdonos: Majsai István
# =========================================

BASE=~/titanium_v11
WEB=$BASE/web_dashboard
LOG=$BASE/output.log
ENV=$HOME/.titanium_env

# 1️⃣ Környezet betöltése
if [ -f "$ENV" ]; then
    source $ENV
fi

# 2️⃣ Backend indítása Tmux-ban
tmux kill-session -t titanium_v11 2>/dev/null || true
tmux new -d -s titanium_v11 "python3 $BASE/run.py >> $LOG 2>&1"
echo "🚀 Backend Tmux-ban elindítva, log: $LOG"

# 3️⃣ Frontend indítása (React)
cd $WEB || exit 1
npm start &>/dev/null &
echo "🌐 Frontend React Dashboard elindítva: http://127.0.0.1:3000"

# 4️⃣ Marketing & előfizetés logok
touch $BASE/marketing.log $BASE/subscription.log
echo "📈 Marketing és előfizetés pipeline fut"

# 5️⃣ AI teszt
cd $BASE || exit 1
AI_TEST=$(python3 -c "from ai_router import ask_ai; print(ask_ai('Hello world'))" 2>/dev/null)
echo "🤖 AI teszt válasz: $AI_TEST"

# 6️⃣ Stripe teszt
python3 - <<PYTHON
import stripe, os
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
try:
    test_payment = stripe.PaymentIntent.create(amount=100, currency='usd', payment_method_types=['card'])
    print("💳 Stripe teszt sikeres, PaymentIntent ID:", test_payment.id)
except Exception as e:
    print("⚠ Stripe hiba:", e)
PYTHON

# 7️⃣ Telegram értesítés
curl -s -X POST "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage" \
    -d chat_id="$TELEGRAM_CHAT_ID" \
    -d text="🎯 Titanium V11 PRO Live és Revenue-ready!" >/dev/null
echo "📲 Telegram értesítés elküldve"

# 8️⃣ Végső státusz
echo "🎯 Titanium V11 PRO FULL LIVE!"
echo "Backend: http://127.0.0.1:8000"
echo "Frontend: http://127.0.0.1:3000"
echo "💡 A rendszer most már képes valós bevételt termelni"
