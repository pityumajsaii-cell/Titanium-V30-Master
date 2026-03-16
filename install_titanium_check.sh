# → Másold be a fenti kódot#!/data/data/com.termux/files/usr/bin/bash
# =====================================
# 💎 Titanium Social Token Check Installer
# =====================================

# 1️⃣ Telepítési könyvtár
INSTALL_DIR="$HOME/titanium_money_run/social_auth_engine"
mkdir -p "$INSTALL_DIR"

# 2️⃣ .titanium_env létrehozása (ha nincs)
ENV_FILE="$HOME/.titanium_env"
if [ ! -f "$ENV_FILE" ]; then
    echo "⚠️ .titanium_env nem található, létrehozom..."
    touch "$ENV_FILE"
    echo "# Ide írd a Facebook és YouTube tokeneket:" >> "$ENV_FILE"
    echo "FB_PAGE_TOKEN_PageName=your_facebook_token_here" >> "$ENV_FILE"
    echo "YT_ACCESS_TOKEN=your_youtube_token_here" >> "$ENV_FILE"
    echo "✅ .titanium_env létrehozva: $ENV_FILE"
fi

# 3️⃣ titanium_check.sh létrehozása
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

echo "======================================"
echo "💎 TITANIUM SOCIAL TOKEN CHECK"
echo "======================================"

declare -A FB_PAGES
for var in $(compgen -v | grep '^FB_PAGE_TOKEN_'); do
    FB_PAGES[$var]="${!var}"
done

echo "🔹 Ellenőrizzük a Facebook/Instagram tokeneket..."
for KEY in "${!FB_PAGES[@]}"; do
    TOKEN="${FB_PAGES[$KEY]}"
    PAGE_NAME="${KEY#FB_PAGE_TOKEN_}"
    RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" "https://graph.facebook.com/v25.0/me?access_token=$TOKEN")
    if [ "$RESPONSE" -eq 200 ]; then
        echo "✅ Facebook/Instagram token OK: $PAGE_NAME"
    else
        echo "❌ Facebook/Instagram token HIBA: $PAGE_NAME"
    fi
done

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
echo ""

read -p "🎯 Teszt poszt küldése Facebook oldalra? (y/n): " TESTPOST
if [[ "$TESTPOST" =~ ^[Yy]$ ]]; then
    read -p "Add meg a Facebook oldal nevét: " PAGEVAR
    NORMAL_PAGEVAR=$(echo "$PAGEVAR" | tr '[:upper:]' '[:lower:]' | tr -d ' ')
    PAGE_TOKEN=""
    for KEY in "${!FB_PAGES[@]}"; do
        NORMAL_KEY=$(echo "${KEY#FB_PAGE_TOKEN_}" | tr '[:upper:]' '[:lower:]' | tr -d ' ')
        if [ "$NORMAL_KEY" == "$NORMAL_PAGEVAR" ]; then
            PAGE_TOKEN="${FB_PAGES[$KEY]}"
            break
        fi
    done
    if [ -z "$PAGE_TOKEN" ]; then
        echo "❌ Token nem található: $PAGEVAR"
        exit 1
    fi
    read -p "Add meg a teszt poszt üzenetét: " MESSAGE
    POST_RESPONSE=$(curl -s -X POST "https://graph.facebook.com/v25.0/me/feed" \
        -d "message=$MESSAGE" \
        -d "access_token=$PAGE_TOKEN")
    echo "📌 Válasz a Facebooktól: $POST_RESPONSE"
fi
echo "======================================"
echo "🎉 Ellenőrzés kész!"
EOF

# 4️⃣ Futtathatóvá tesszük
chmod +x "$CHECK_SCRIPT"

# 5️⃣ Alias hozzáadása
grep -qxF 'alias titanium_check="$HOME/titanium_money_run/social_auth_engine/titanium_check.sh"' ~/.bashrc || \
    echo 'alias titanium_check="$HOME/titanium_money_run/social_auth_engine/titanium_check.sh"' >> ~/.bashrc
source ~/.bashrc

# 6️⃣ PM2-be felvétele, hogy mindig fusson óránként
if ! command -v pm2 >/dev/null 2>&1; then
    echo "⚠️ PM2 nincs telepítve, telepítsd: npm install -g pm2"
else
    # Python scriptet is készítünk, ami óránként futtatja a check-et
    PYTHON_RUNNER="$INSTALL_DIR/social_auth_runner.py"
    cat > "$PYTHON_RUNNER" << 'PYEOF'
import os, time, subprocess
ENV_FILE = os.path.expanduser("~/.titanium_env")
CHECK_SCRIPT = os.path.expanduser("~/titanium_money_run/social_auth_engine/titanium_check.sh")

def run_check():
    subprocess.run([CHECK_SCRIPT], shell=True)

if __name__ == "__main__":
    while True:
        run_check()
        time.sleep(3600)  # óránként
PYEOF

    pm2 start "$PYTHON_RUNNER" --name social_auth_engine --interpreter python3
    pm2 save
fi

echo "✅ Telepítés és beállítás kész!"
echo "💡 Használd a 'titanium_check' parancsot a manuális ellenőrzéshez."
