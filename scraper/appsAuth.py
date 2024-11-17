import json, re, requests, os, dotenv
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import Spotify
dotenv.load_dotenv()

class CustomSpotify(Spotify):

    def __init__(self):
        _clientid = os.getenv('spotipy.client.id')
        _clientsecret = os.getenv('spotipy.client.secret')
        _auth_manager = SpotifyClientCredentials(_clientid, _clientsecret)
        super().__init__(client_credentials_manager=_auth_manager, retries=3, requests_timeout=30)
        self.artistobj = self.audioobj = None

    def playlist_tracks(self):
        _playlist = os.getenv('spotipy.uri')
        playlistjson = super().playlist_tracks(_playlist, limit=100)
        return playlistjson.get('items')

    def track(self, track_id):
        trackobj = super().track(track_id)
        artist_id = trackobj['artists'][0]['id']
        artistobj = super().artist(artist_id)
        audioobj =  super().audio_features([track_id])[0]
        return trackobj, artistobj, audioobj

    def recommendations(self, gettrack, getartist):
        tracks = [gettrack]
        genres = ['afrobeats','nigerian pop']
        artists = [artist.get('id') for artist in getartist]
        recommendeds = super().recommendations(
            seed_genres=genres, seed_artists=artists[:2], seed_tracks=tracks,limit=5
        )
        return recommendeds.get('tracks')

    def lyrics(self):
        names = (self.artist, self.track)
        '''print('waiting for lyrics')
        response = requests.get(
            url = f'https://api.lyrics.ovh/v1/{names[0]}/{names[1]}',
            headers = {'Content-Type': 'application/json'}, timeout=90,
        )
        print('lyrics gotten')
        tklyrics = None
        if response.status_code==200:
            jsonlyrics = json.loads(response.content)
            tklyrics = re.split("[\n|\r]+", jsonlyrics['lyrics'])
            tklyrics = tklyrics[1:]
        self.lyrics = None'''

