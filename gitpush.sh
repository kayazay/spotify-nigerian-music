#!/bin/bash

git pull origin main
git add .

# commit changes
git commit -m "weekly commit of spotify project"
git push -u origin main
