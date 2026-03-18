#!/bin/bash
# --- TITANIUM AUTO-SUBMITTER & SALES FORCE ---
# OPERÁTOR: MAJSAI ISTVÁN (TITANIUM)

echo "📩 [20] PÁLYÁZATOK KITÖLTÉSE..."
# 1. Magyar Technológiai Startup Alap (15M HUF) - Adatok előkészítése
echo "Pályázó: Majsai István" > ~/Titanium-V30-Master/prophet/marketing/leads/grant_app_01.txt
echo "Projekt: Titanium AI-Audit v16.1" >> ~/Titanium-V30-Master/prophet/marketing/leads/grant_app_01.txt
echo "Fedezet: 100 milliárd Tolna Majsai Token" >> ~/Titanium-V30-Master/prophet/marketing/leads/grant_app_01.txt
echo "Státusz: Beküldésre kész (Draft Generated)"

echo "🤝 [SALES] ÜZLETI AJÁNLAT KIKÜLDÉSE (TechCorp)..."
# 2. TechCorp ajánlat véglegesítése és továbbítása a virtuális várólistára
cp ~/Titanium-V30-Master/prophet/marketing/leads/techcorp_offer_pro.md ~/Titanium-V30-Master/prophet/marketing/leads/sent_offers.log

echo "📊 [MONITOR] ÖSSZES MODUL PÁRHUZAMOS FUTTATÁSA..."
# Minden háttérfolyamat kényszerítése
nohup ./prophet/marketing/lead_finder.sh > /dev/null 2>&1 &
nohup ./prophet/marketing/viral_gen.sh > /dev/null 2>&1 &
nohup ./prophet/self_dev/evolution.sh > /dev/null 2>&1 &

echo "✅ RENDSZER 100% EXECUTING MÓDBAN."
