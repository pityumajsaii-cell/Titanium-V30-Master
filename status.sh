#!/bin/bash
echo "🛰️ Titanium Apex Felhő Ellenőrzés..."
curl -I https://huggingface.co/spaces/Pityutolna/titanium-apex-enterprise
echo "-----------------------------------"
echo "✅ Ha 'HTTP/2 200' látható, a birodalom ONLINE!"
