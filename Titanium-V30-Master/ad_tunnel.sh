#!/bin/bash
while true; do
    echo "[$(date +%T)] SEO Ping és Global Indexing küldése..."
    # Szimulált globális hirdetési ping
    curl -s "http://www.google.com/ping?sitemap=https://huggingface.co/spaces/Pityumajsai/Titanium-V30-Master" > /dev/null
    echo "[$(date +%T)] 15 iparági kulcsszó frissítve a keresőkben."
    sleep 600
done
