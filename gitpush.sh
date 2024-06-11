#!/bin/bash
cd ~/spotify-nigerian-music

# git init OR git clone *.git

git pull origin main
git add .

# commit changes
git commit -m "Initial commit of spotify project"
git push -u origin master
