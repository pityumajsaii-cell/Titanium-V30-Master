#!/bin/bash
echo "🧹 Titanium Rendszerkarbantartás indítása..."
# Logok rövidítése (csak az utolsó 100 sort tartja meg)
tail -n 100 ~/server.log > ~/server.log.tmp && mv ~/server.log.tmp ~/server.log
tail -n 100 ~/marketing.log > ~/marketing.log.tmp && mv ~/marketing.log.tmp ~/marketing.log
tail -n 100 ~/watchdog.log > ~/watchdog.log.tmp && mv ~/watchdog.log.tmp ~/watchdog.log
echo "✅ Logok optimalizálva. Rendszer tiszta."
