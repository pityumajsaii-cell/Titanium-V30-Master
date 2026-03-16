#!/data/data/com.termux/files/usr/bin/bash
export PYTHONPATH="$HOME/titanium_v11"

while true; do
    echo "🚀 Ellenőrzés és indítás: Titanium V11"
    python3 <<PY
from ai_router import launch_full_system
launch_full_system(
    modules=["Education","AI_Tools","AI_Marketing","Payment","Dashboard"],
    mobile_friendly=True,
    push_notifications=True,
    realtime_graphs=True,
    analytics=True,
    self_learning=True,
    auto_archive=True
)
PY
    sleep 60  # 1 percenként ellenőriz
done
