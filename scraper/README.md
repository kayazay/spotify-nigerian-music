# Spotify Playlist Scraper

The scraper unit of this project does the following:

+ collects tracks from a Spotify playlist
+ gets preliminary data from each track: `track`, `artists`, and `date_scraped`
+ retrieves recommendations on each track
+ gets further details on all tracks collected
+ outputs information to csv in `./datasets`

## Requirements
+ Python 3.x
+ Libraries contained in `requirements.txt`
+ Credentials contained in `env.cfg`
```ini
[spotipy.client]
id = your_spotipy_client_id
secret = your_spotipy_client_secret
uri = your_spotify_playlist_url
```

## Functions
+ **appsAuth.py**
    + `spotipyAuthenticator:` Authenticates to the Spotify API
    + `ovh:` Retrieves lyrics for a given artist and track
+ **mainrunner.py**
    + `tracksFromPlaylist:` Scrapes tracks from the playlist and retrieves recommendations
    + `detailsFromTracks:` Collects detailed information from each track
    + `fileNameGiver:` Generates a file name for the CSV based on the scrape date

## Licensing
This project is licensed under the **[Apache License](https://www.apache.org/licenses/LICENSE-2.0)**.

---

<p>&copy; 2024 Kingsley Izima</p>
