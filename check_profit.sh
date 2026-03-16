#!/bin/bash
echo "📊 TITANIUM REAL-TIME MONITOR"
echo "----------------------------"
echo "Szerver IP: $(curl -s ifconfig.me)"
pgrep -fl python3
echo "----------------------------"
tail -n 5 ~/marketing.log
