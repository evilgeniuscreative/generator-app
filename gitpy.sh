#!/bin/bash

cd /root/generator-app || exit

echo "[$(date)] Starting deployment..." >> deploy.log

echo "Pulling latest from GitHub..."
git pull origin main >> deploy.log 2>&1

echo "Activating venv..."
source venv/bin/activate

echo "Restarting Python app..."
pkill -f app.py

nohup venv/bin/python app.py >> app_output.log 2>&1 &

echo "[$(date)] Deployment complete." >> deploy.log
