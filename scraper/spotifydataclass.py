from dataclasses import dataclass, field, asdict
import datetime as dt

@dataclass(init=False)
class SpotifyData:

    tid: str
    track: str
    track_url: str
    release_date: dt.date
    duration_ms: int
    explicit: bool
    track_popularity: int
    markets: int
    albid: str
    album: str
    album_type: str
    artid: str
    artist: str
    genres: list[str] = field(default_factory=list)
    artist_popularity: int
    danceability: float
    instrumentalness: float
    speechiness: float
    valence: float
    loudness: float
    lyrics: list[str] = field(default_factory=list)
    added_at: dt.date

    def __init__(self, added_at, detail, artist, audio):
        self.tid = detail['id']
        self.track = detail['name']
        self.track_url = detail['external_urls']['spotify']
        release_date = detail['album']['release_date']
        self.release_date = dt.datetime.strptime(release_date, r'%Y-%m-%d')
        self.duration_ms = detail['duration_ms']
        self.explicit = detail['explicit']
        self.track_popularity = detail['popularity']
        self.markets = len(detail['available_markets'])
        self.albid = detail['album']['id']
        self.album = detail['album']['name']
        self.album_type = detail['album']['album_type']
        self.artid = detail['artists'][0]['id']
        self.artist = detail['artists'][0]['name']
        self.genres = artist['genres']
        self.artist_popularity = artist['popularity']
        self.danceability = audio['danceability']
        self.instrumentalness = audio['instrumentalness']
        self.speechiness = audio['speechiness']
        self.valence = audio['valence']
        self.loudness = audio['loudness']
        self.lyrics = []
        self.added_at = added_at

    def todict(self):
        return asdict(self)
