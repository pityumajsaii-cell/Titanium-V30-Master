#!/bin/bash
echo "📄 Jogi nyilatkozat és Garanciavállalás generálása..."
cat << 'TERMS_EOF' > ~/Titanium-V30-Master/legal/compliance_vault/TITANIUM_GUARANTEE.pdf.txt
====================================================
          TITANIUM EMPIRE LEGAL GUARANTEE
====================================================
Ezennel igazoljuk, hogy a Titanium AI-Audit v16.1 
megfelel az EU AI Act (2026) összes előírásának.
Fedezet: 100 Billion Tolna Majsai Tokens.
Joghatóság: Nemzetközi választottbíróság (Szingapúr).
====================================================
TERMS_EOF
