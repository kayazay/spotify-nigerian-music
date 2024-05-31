#!/bin/bash

# Navigate to your project directory
cd ~/spotify/

git init
git add .
git commit -m "Initial commit of spotify project"

# Add the remote repository
git remote add origin git@github.com:kayazay/spotify-nigerian-music.git
# git remote add origin https://github.com/USERNAME/REPO.git

# Verify the remote URL
git remote -v
git push -u origin master

