alias titanium_check="$HOME/titanium_money_run/social_auth_engine/titanium_check.sh"
alias titanium_check="$HOME/titanium_money_run/social_auth_engine/titanium_check.sh"
alias titanium_check='/data/data/com.termux/files/home/titanium_money_run/social_auth_engine/titanium_check.sh'
alias titanium_check='/data/data/com.termux/files/home/titanium_system/titanium_check.sh'
alias titanium_check='/data/data/com.termux/files/home/titanium_system/video_factory/main.py'
# TITANIUM AUTO-START
if ! pgrep -f "titanium_v30_final.py" > /dev/null; then
    echo "🚀 Titanium V30 automatikus indítása..."
    ./titanium_master_control.sh
fi
alias titanium-restore='cp ~/TITANIUM_BACKUP_LOCAL/.env_backup ~/.env && echo 💎 Rendszer beállítások visszaállítva'

# Titanium V30 Gyorsindító és Ellenőrző
alias titanium_start='cd ~ && ./titanium_shield.sh'
