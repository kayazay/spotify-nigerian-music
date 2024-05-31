import configparser
import os
import base64
import requests
import spotipy

cfg = configparser.ConfigParser()
cfg.read('env.cfg')

# AUTHENTICATE TO SPOTIPY APP
def spotipyAuthenticator():
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
playlist = cfg['spotipy.client']['uri']

# AUTHENTICATE TO LYRICS OVH APP
def ovh(artist, track):
    response = requests.get(
        url = f'https://api.lyrics.ovh/v1/{artist}/{track}',
        headers = {'Content-Type': 'application/json'}
    )
    content = response.content
    decoded = str(content, encoding="utf-8")
    lyrics = decoded.split('"')[-2].split(r'\r\n')[-1]
    whtspc = lyrics.replace(r'\n\n',r'\n')
    tokenized = whtspc.split(r'\n')
    return tokenized
