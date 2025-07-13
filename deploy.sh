#!/bin/bash

cd /path/to/generator-app || exit

echo "[$(date)] Starting deployment..." >> deploy.log

echo "Pulling latest from GitHub..."
git pull origin main >> deploy.log 2>&1

echo "Restarting Python app..."
# Kill any existing Python app (adjust as needed)
pkill -f app.py

# Restart in background
nohup python3 app.py >> app_output.log 2>&1 &

echo "[$(date)] Deployment complete." >> deploy.log
