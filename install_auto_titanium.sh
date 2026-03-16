# → Másold be a fenti kódot#!/data/data/com.termux/files/usr/bin/bash
# =====================================
# 💎 Titanium Social AutoPost Installer
# =====================================

INSTALL_DIR="$HOME/titanium_money_run/social_auth_engine"
mkdir -p "$INSTALL_DIR"

# 1️⃣ .titanium_env létrehozása, ha nincs
ENV_FILE="$HOME/.titanium_env"
if [ ! -f "$ENV_FILE" ]; then
    echo "⚠️ .titanium_env nem található, létrehozom..."
    cat > "$ENV_FILE" << 'EOF'
# Facebook tokenek (FB_PAGE_TOKEN_OLDNAME formátum)
FB_PAGE_TOKEN_PageName=your_facebook_token_here

# YouTube token
YT_ACCESS_TOKEN=your_youtube_token_here

# Teszt poszt üzenet (opcionális)
FB_TEST_MESSAGE="Ez egy automatikus teszt poszt."
EOF
    echo "✅ .titanium_env létrehozva: $ENV_FILE"
fi

# 2️⃣ titanium_check.sh létrehozása
CHECK_SCRIPT="$INSTALL_DIR/titanium_check.sh"
cat > "$CHECK_SCRIPT" << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
ENV_FILE="$HOME/.titanium_env"

if [ -f "$ENV_FILE" ]; then
    source "$ENV_FILE"
else
    echo "❌ .titanium_env fájl nem található!"
    exit 1
fi

declare -A FB_PAGES
for var in $(compgen -v | grep '^FB_PAGE_TOKEN_'); do
    FB_PAGES[$var]="${!var}"
done

echo "======================================"
echo "💎 TITANIUM SOCIAL TOKEN CHECK"
echo "======================================"

# Facebook ellenőrzés és automata poszt
for KEY in "${!FB_PAGES[@]}"; do
    TOKEN="${FB_PAGES[$KEY]}"
    PAGE_NAME="${KEY#FB_PAGE_TOKEN_}"
    RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" "https://graph.facebook.com/v25.0/me?access_token=$TOKEN")
    if [ "$RESPONSE" -eq 200 ]; then
        echo "✅ Facebook/Instagram token OK: $PAGE_NAME"

        # Automata poszt (ha van FB_TEST_MESSAGE)
        if [ ! -z "$FB_TEST_MESSAGE" ]; then
            POST_RESPONSE=$(curl -s -X POST "https://graph.facebook.com/v25.0/me/feed" \
                -d "message=$FB_TEST_MESSAGE" \
                -d "access_token=$TOKEN")
            echo "📌 Automata poszt a Facebook oldalra ($PAGE_NAME): $POST_RESPONSE"
        fi
    else
        echo "❌ Facebook/Instagram token HIBA: $PAGE_NAME"
    fi
done

# YouTube ellenőrzés
echo "🔹 Ellenőrizzük a YouTube tokent..."
if [ -z "$YT_ACCESS_TOKEN" ]; then
    echo "⚠️ YouTube token nincs beállítva!"
else
    YT_RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" "https://www.googleapis.com/oauth2/v3/tokeninfo?access_token=$YT_ACCESS_TOKEN")
    if [ "$YT_RESPONSE" -eq 200 ]; then
        echo "✅ YouTube token OK"
    else
        echo "❌ YouTube token HIBA"
    fi
fi
echo "======================================"
EOF

chmod +x "$CHECK_SCRIPT"

# 3️⃣ Alias a gyors manuális ellenőrzéshez
grep -qxF 'alias titanium_check="$HOME/titanium_money_run/social_auth_engine/titanium_check.sh"' ~/.bashrc || \
    echo 'alias titanium_check="$HOME/titanium_money_run/social_auth_engine/titanium_check.sh"' >> ~/.bashrc
source ~/.bashrc

# 4️⃣ Python runner óránkénti futtatáshoz
PYTHON_RUNNER="$INSTALL_DIR/social_auth_runner.py"
cat > "$PYTHON_RUNNER" << 'PYEOF'
import os, time, subprocess

CHECK_SCRIPT = os.path.expanduser("~/titanium_money_run/social_auth_engine/titanium_check.sh")

def run_check():
    subprocess.run([CHECK_SCRIPT], shell=True)

if __name__ == "__main__":
    while True:
        run_check()
        time.sleep(3600)  # óránként
PYEOF

# 5️⃣ PM2-be felvétel
if ! command -v pm2 >/dev/null 2>&1; then
    echo "⚠️ PM2 nincs telepítve, telepítsd: npm install -g pm2"
else
    pm2 start "$PYTHON_RUNNER" --name social_auth_engine --interpreter python3
    pm2 save
    echo "✅ PM2-be felvéve, óránként futni fog."
fi

echo "✅ Telepítés és automatikus posztoló beállítás kész!"
echo "💡 Használd a 'titanium_check' parancsot manuális futtatáshoz."
