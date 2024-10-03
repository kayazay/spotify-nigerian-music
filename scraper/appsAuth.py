import json, re, requests, configparser
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import Spotify

cfg = configparser.ConfigParser()
cfg.read('env.cfg')

class SpotifyOperation:
    
    PLAYLIST = cfg['spotipy.client']['uri']
    
    def __init__(self):
        CLIENT_ID = cfg['spotipy.client']['id']
        CLIENT_SECRET = cfg['spotipy.client']['secret']
        AUTH = SpotifyClientCredentials(client_id= CLIENT_ID, client_secret= CLIENT_SECRET)
        self.sptfy = Spotify(auth_manager=AUTH, retries=3,requests_timeout=30)
    
    def track(self, track_id, dict = {}):
        detail = self.sptfy.track(track_id)
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
        # features of spotify track
        return dict
    
    def audio(self, track_id, dict={}):
        audio = self.sptfy.audio_features(tracks=[track_id])[0]
        dict['danceability'] = audio['danceability']
        dict['instrumentalness'] = audio['instrumentalness']
        dict['speechiness'] = audio['speechiness']
        dict['valence'] = audio['valence']
        dict['loudness'] = audio['loudness']
        # audio features of spotify track
        return dict
    
    def artist(self, ddict, dict={}):
        artist_id = ddict['artid']
        artist = self.sptfy.artist(artist_id)
        dict['artist'] = artist['name']
        dict['genres'] = artist['genres']
        dict['artist_popularity'] = artist['popularity']
        # features of spotify artist
        return dict

    def api4ovh(ddict):
        artist_name = ddict['artist']
        track_name = ddict['track']        
        response = requests.get(
            url = f'https://api.lyrics.ovh/v1/{artist_name}/{track_name}',
            headers = {'Content-Type': 'application/json'}, timeout=90,
        )
        if response.status_code==200:
            jsonlyrics = json.loads(response.content)
            tklyrics = re.split("[\n|\r]+", jsonlyrics['lyrics'])
            return tklyrics[1:]
        else:
            return None


'''
import base64, requests
# AUTHENTICATE TO SPOTIPY APP
def spotipyAuthenticator2():
    # Base64 encode the client ID and client secret
    client_credentials = f"{cfg['spotipy.client']['id']}:{cfg['spotipy.client']['secret']}"
    client_credentials_base64 = base64.b64encode(client_credentials.encode())
    # Make a POST call to the Spotify API authenticating with client credentials 
    response = requests.post(
        url='https://accounts.spotify.com/api/token', 
        data={ 'grant_type': 'client_credentials' }, 
        headers={ 'Authorization': f'Basic {client_credentials_base64.decode()}' }
    )
    # Request the access token
    if response.status_code == 200:
        access_token = response.json()['access_token']
        print("Access token obtained successfully")
    else:
        print(response.status_code)
        print("Error obtaining access token.")
        exit()
    return spotipy.Spotify(auth=access_token)

from spotipy.oauth2 import SpotifyClientCredentials
def spotipyAuthenticator():
    auth_manager = SpotifyClientCredentials(
        client_id = cfg['spotipy.client']['id'], 
        client_secret = cfg['spotipy.client']['secret']
    )
    sp = spotipy.Spotify(
        auth_manager=auth_manager, 
        retries=3, 
        requests_timeout=30
    )
    return sp
# AUTHENTICATE TO LYRICS OVH APP
def ovh(artist, track):
    response = requests.get(
        url = f'https://api.lyrics.ovh/v1/{artist}/{track}',
        headers = {'Content-Type': 'application/json'},
        timeout=90,
    )
    if response.status_code==200:
        content = response.content
        jsonLyrics = json.loads(content)
        lyrics = jsonLyrics['lyrics']
        #whtspaced_lyrics = decoded.split(':')[-1]
        tokenized_lyrics = re.split("[\n|\r]+", lyrics)
        return tokenized_lyrics[1:]
    else:
        return None

'''
