alias titanium='pm2 status'
pm2 resurect 2>/dev/null || pm2 restore
alias titanium='pm2 status'
alias titanium-log='pm2 logs'
alias titanium-mon='pm2 monit'
pm2 resurrect
alias titanium='pm2 status'
pm2 resurrect 2>/dev/null || pm2 restore
alias titanium='pm2 status'
pm2 resurrect 2>/dev/null || pm2 restore
alias titanium='pm2 status'
pm2 resurrect 2>/dev/null || pm2 restore
alias titanium='pm2 status'
pm2 resurrect 2>/dev/null || pm2 restore
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
