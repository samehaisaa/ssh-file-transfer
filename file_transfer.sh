#!/bin/bash

# Variables
SOURCE_DIR=~/wsl_project/source
REMOTE_USER=testuser
REMOTE_HOST=localhost
REMOTE_DIR=/home/testuser/remote_backup
SSH_KEY=~/.ssh/id_ed25519

# Transfer files using scp
scp -i $SSH_KEY -r $SOURCE_DIR $REMOTE_USER@$REMOTE_HOST:$REMOTE_DIR

# Check for errors
if [ $? -eq 0 ]; then
  echo "Transfer successful!"
else
  echo "Error in transfer!"
fi
