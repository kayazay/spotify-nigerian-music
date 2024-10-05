import json, re, requests, configparser
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import Spotify

cfg = configparser.ConfigParser()
cfg.read('env.cfg')

class SpotifyOperation:
    
    playlist = cfg['spotipy.client']['uri']
    
    def __init__(self):
        CLIENT_ID = cfg['spotipy.client']['id']
        CLIENT_SECRET = cfg['spotipy.client']['secret']
        AUTH = SpotifyClientCredentials(client_id= CLIENT_ID, client_secret= CLIENT_SECRET)
        self.sptfy = Spotify(auth_manager=AUTH, retries=3,requests_timeout=30)
        self.track_id = None
        self.finaldict = {}
        
    def gettrackid(self, track_id):
        self.track_id = track_id

    def track(self, dict = {}):
        detail = self.sptfy.track(self.track_id)
        dict['tid'] = detail['id']
        dict['track'] = detail['name']
        dict['track_url'] = detail['external_urls']['spotify']
        dict['release_date'] = detail['album']['release_date']
        dict['duration_ms'] = detail['duration_ms']
        dict['explicit'] = detail['explicit']
        dict['track_popularity'] = detail['popularity']
        dict['markets'] = len(detail['available_markets'])
        dict['albid'] = detail['album']['id']
        dict['album'] = detail['album']['name']
        dict['album_type'] = detail['album']['album_type']
        dict['artid'] = detail['artists'][0]['id']
        dict['artist'] = detail['artists'][0]['name']
        # features of spotify track
        self.finaldict = {**self.finaldict, **dict}
    
    def artist(self, dict={}):
        print('waiting for artist')
        artid = self.finaldict['artid']
        print('artist gotten')
        artist = self.sptfy.artist(artid)
        dict['artist'] = artist['name']
        dict['genres'] = artist['genres']
        dict['artist_popularity'] = artist['popularity']
        # features of spotify artist
        self.finaldict = {**self.finaldict, **dict}
    
    def audio(self, dict={}):
        audio = self.sptfy.audio_features(tracks=[self.track_id])[0]
        dict['danceability'] = audio['danceability']
        dict['instrumentalness'] = audio['instrumentalness']
        dict['speechiness'] = audio['speechiness']
        dict['valence'] = audio['valence']
        dict['loudness'] = audio['loudness']
        # audio features of spotify track
        self.finaldict = {**self.finaldict, **dict}
    
    def api4ovh(self):
        names = (self.finaldict['artist'], self.finaldict['track'])
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
            tklyrics = tklyrics[1:]'''
        self.finaldict['lyrics'] = None


class SpotifyPlaylistJobs:

    playlist = cfg['spotipy.client']['uri']
    
    def __init__(self):
        CLIENT_ID = cfg['spotipy.client']['id']
        CLIENT_SECRET = cfg['spotipy.client']['secret']
        AUTH = SpotifyClientCredentials(client_id= CLIENT_ID, client_secret= CLIENT_SECRET)
        self.sptfy = Spotify(auth_manager=AUTH, retries=3,requests_timeout=30)
        self.track_id = None
        self.finaldict = {}    

    def playlist_tracks(self):
        return self.sptfy.playlist_tracks(SpotifyOperation.playlist)

    def recommendations(self, ARTISTS, TRACKS, GENRES, LIMIT):
        return self.sptfy.recommendations(
            seed_genres=GENRES,
            seed_artists=ARTISTS,
            seed_tracks=TRACKS,
            limit=LIMIT
        )

    def next(self, playlistJson):
        return self.sptfy.next(playlistJson)
