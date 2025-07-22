#!/bin/bash

# === CONFIGURATION ===
REMOTE_USER=root
REMOTE_HOST=68.183.128.48
REMOTE_PATH=/home/root/generator-app

# === UPLOAD FILES ===
echo "Uploading files to Digital Ocean..."
scp -r ./generator-app/* $REMOTE_USER@$REMOTE_HOST:$REMOTE_PATH/

# === RUN DEPLOY SCRIPT REMOTELY ===
echo "Running remote deployment script..."
ssh $REMOTE_USER@$REMOTE_HOST "cd $REMOTE_PATH && bash deploy.sh"
