#!/bin/bash

echo "=====SIT TIGHT... I'M MAKING SURE YOU'RE PROTECTED====="
echo "Configuring firewall using '/vagrant/configure_firewall.sh'..."

# Implicily deny all incoming connections
sudo ufw default deny incoming
# Implicity allow all outgoing connections
sudo ufw default allow outgoing
# Allow SSH
sudo ufw allow ssh
# [CHANGE TO YOUR VAGRANT ASSIGNED CUSTOM PORT NUMBER] Allow SSH custom port number
sudo ufw allow 2201/tcp
# Allow WWW for web traffic
sudo ufw allow www
# Enable firewall
sudo ufw enable

echo "=====ALRIGHT... I'M DONE====="
