# Batch CSV Dump of Spotify Data

Each time the scraper runs, a dataframe containing all the retrieved tracks is dumped in this directory and then uploaded to the Kaggle dataset. The files are named in a way that makes it easy to determine the date of the dump at a glance.

For example:

+ 2024week1feb.csv indicates that the data was scraped in February, during the 6th week of the year 2024.

## Data Dictionary

| **Column Name** | **Descrption** | **Data Type** |
|------------|-----------|--------------|
| `tid` | unique key of track | *string* |
| `track` | full name of track | *string* |
| `track_url` | link to track | *string* |
| `release_date` | date track was released | *date* |
| `duration_ms` | duration of track in milliseconds | *integer* |
| `explicit` | whether track contains explicit lyrics or not | *boolean* |
| `track_popularity` | popularity rating of track from 0-100 | *integer* |
| `markets` | number of countries track is available in | *integer* |
| `albid` | unique album id of album | *string* |
| `album` | full name of album | *string* |
| `album_type` | type of album (single, album) | *string* |
| `artid` | unique artist id | *stringca* |
| `artist` | full name of artist | *string* |
| `genres` | list of genres associated with artist | *list* |
| `artist_popularity` | popularity rating of artist from 0-100 | *integer* |
| `danceability` | danceaility of track () | *integer* |
| `instrumentalness` | instrumentalness of track () | *integer* |
| `speechiness` | speechiness of track () | *integer* |
| `valence` | valence of track () | *integer* |
| `loudness` | loudness of track () | *integer* |
| `added_at` | date playlist was last updated | *date* |
| `lyrics` | tokenized lyrics; each line = item in list | *list* |

## Usage

All CSV files are standardized to have the same structure and file names, allowing them to be ingested into a semi-relational database, upon which models can be built.

## Licensing

These datasets were gotten from the Spotify Web API and therefore are licensed under the [Spotify Developer Terms](https://developer.spotify.com/terms).

---

<p>&copy; 2022 Kingsley Izima</p>
