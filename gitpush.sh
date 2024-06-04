#!/bin/bash
# cd ~/spotify/

# Add the remote repository
# git remote add origin git@github.com:kayazay/spotify-nigerian-music.git && git remote -v

# git init OR git clone *.git
git pull origin main && git status
git add . && git status

# commit changes
git commit -m "Initial commit of spotify project"
git push -u origin master
