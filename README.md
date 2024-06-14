# SPOTIFY NIGERIAN MUSIC

This repository contains scripts for scraping tracks from a Spotify playlist and managing datasets using Docker containers. The project consists of two main components: the scraper and the dataset manager.

## Repository Structure
+ **dataset/:** Contains dataset files, metadata, kaggle credentials, and Dockerfile
+ **scraper/:** Contains scraping script, python requirements, credentials and Dockerfile
+ **compose.yaml:** Docker compose configuration for the both containers

## Usage
This project is automated by Linux Crontab to run every week on a specific day. Here is the script that handles the building and running of all docker containers, uploading new datasets to Kaggle, as well as pushing any changes to Github.

```bash
cd ~/init/spotify-nigerian-music
git status
docker compose up
git add .
git commit -m "weekly commit of spotify project"
git push -u origin main
```

## Licensing
This project is licensed under the [Apache License](https://www.apache.org/licenses/LICENSE-2.0).
