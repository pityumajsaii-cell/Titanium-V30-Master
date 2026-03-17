#!/bin/bash
read -p "Google Szerver IP: " CLOUD_IP
read -p "Google Felhasználónév: " CLOUD_USER
echo "🚀 Átvitel indul..."
scp -i $HOME/.ssh/titanium_key master_controller.sh $CLOUD_USER@$CLOUD_IP:~/
ssh -i $HOME/.ssh/titanium_key $CLOUD_USER@$CLOUD_IP "chmod +x master_controller.sh && ./master_controller.sh"
