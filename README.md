# NIGERIAN SPOTIFY MUSIC ELT PROJECT

Here I try to

"resources": [{
  "name": "2024week21may.csv",
  "description": "This file contains weekly data dump from spotify playlist and further recommendations on each track; as well as details about each subsequent track.",
  "schema": {
    "fields": [
      {
        "name": "tid",
        "description": "unique key of track",
        "type": "string"
      },
      {
        "name": "track",
        "description": "full name of track",
        "type": "string"
      },
      {
        "name": "track_url",
        "description": "link to track",
        "type": "string"
      },
      {
        "name": "release_date",
        "description": "date track was released",
        "type": "date"
      },
      {
        "name": "duration_ms",
        "description": "duration of track in milliseconds",
        "type": "integer"
      },
      {
        "name": "explicit",
        "description": "whether track contains explicit lyrics or not",
        "type": "boolean"
      },
      {
        "name": "track_popularity",
        "description": "popularity rating of track from 0-100",
        "type": "integer"
      },
      {
        "name": "markets",
        "description": "number of countries track is available in",
        "type": "integer"
      },
      {
        "name": "albid",
        "description": "unique album id of track",
        "type": "string"
      },
      {
        "name": "album",
        "description": "full name of album",
        "type": "string"
      },
      {
        "name": "album_type",
        "description": "type of album (single, album)",
        "type": "string"
      },
      {
        "name": "artid",
        "description": "unique artist id",
        "type": "string"
      },
      {
        "name": "artist",
        "description": "full name of artist",
        "type": "string"
      },
      {
        "name": "genres",
        "description": "list of genres associated with artist",
        "type": "list"
      },
      {
        "name": "artist_popularity",
        "description": "popularity rating of artist from 0-100",
        "type": "integer"
      },
      {
        "name": "danceability",
        "description": "danceaility of track ()",
        "type": "integer"
      },
      {
        "name": "instrumentalness",
        "description": "instrumentalness of track ()",
        "type": "integer"
      },
      {
        "name": "speechiness",
        "description": "speechiness of track ()",
        "type": "integer"
      },
      {
        "name": "valence",
        "description": "valence of track ()",
        "type": "integer"
      },
      {
        "name": "loudness",
        "description": "loudness of track ()",
        "type": "integer"
      },
      {
        "name": "added_at",
        "description": "date playlist was last updated",
        "type": "date"
      },
      {
        "name": "lyrivs",
        "description": "tokenized list of lyrics of song, line by line",
        "type": "list"
      }
  ]}
}],