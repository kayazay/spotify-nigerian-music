import appsAuth as aA
from datetime import datetime as dt
import time
import pandas
sp = aA.spotipyAuthenticator()
date_scraped = None

# SCRAPE TRACKS FROM PLAYLIST
def tracksFromPlaylist(counter=1, finalTracks=[]):
    print('first entry into playlist, getting items now')
    playlistJson = sp.playlist_tracks(aA.playlist)
    global date_scraped
    while playlistJson:
        # iterate over each item in the playlist
        for item in playlistJson.get('items'):
            added_at = item.get('added_at').split('T')[0]
            date_scraped = dt.strptime(added_at, r'%Y-%m-%d')
            track = item.get('track')
            # get details from track variabe
            deetTracks = [track.get('id')]
            artist_json = track.get('artists')
            artist_ids = [artist.get('id') for artist in artist_json]
            # get recommended tracks from seed parameters
            for recommended in sp.recommendations(
                seed_artists=artist_ids[:2],
                seed_tracks=deetTracks,
                seed_genres=['afrobeats','nigerian pop'],
                limit=5
            ).get('tracks'):
                deetTracks.append(recommended.get('id'))
            if counter%10 == 0: 
                time.sleep(15)
                print(f'...track {counter} scraped with {len(deetTracks)} total')
            counter += 1
            finalTracks += deetTracks
            break
        # obtain next paginated results after scraping
        if playlistJson.get('next'):
            playlistJson = sp.next(playlistJson)
        else:
            playlistJson = None
    deduplTracks = tuple(set(finalTracks))
    return deduplTracks

# COMBINE ALL TRACKS GOTTEN AND GET DETAILS
def detailsFromPlaylist(allTracks, counter=1, dictx={}, listx=[]):
    print('collecting details from each track, be patient')
    for track_id in allTracks:
        # get regular details of track
        detail = sp.track(track_id)
        dictx['tid'] = detail['id']
        dictx['track'] = detail['name']
        dictx['track_url'] = detail['external_urls']['spotify']
        dictx['release_date'] = detail['album']['release_date']
        dictx['duration_ms'] = detail['duration_ms']
        dictx['explicit'] = detail['explicit']
        dictx['track_popularity'] = detail['popularity']
        dictx['markets'] = len(detail['available_markets'])
        dictx['albid'] = detail['album']['id']
        dictx['album'] = detail['album']['name']
        dictx['album_type'] = detail['album']['album_type']
        # get genre and other info from artist
        dictx['artid'] = detail['artists'][0]['id']
        artist_f = sp.artist(dictx['artid'])
        dictx['artist'] = artist_f['name']
        dictx['genres'] = artist_f['genres']
        dictx['artist_popularity'] = artist_f['popularity']
        # get audio features of track
        audio_f = sp.audio_features(tracks=[track_id])[0]
        dictx['danceability'] = audio_f['danceability']
        dictx['instrumentalness'] = audio_f['instrumentalness']
        dictx['speechiness'] = audio_f['speechiness']
        dictx['valence'] = audio_f['valence']
        dictx['loudness'] = audio_f['loudness']
        # get time playlist was updated
        dictx['added_at'] = date_scraped
        dictx['lyrics'] = aA.ovh(dictx['artist'] , dictx['track'])
        if counter%10 == 0:
            time.sleep(15) 
            print(f'...track {counter} scraped with all details')
        counter += 1
        listx.append(dictx)
    return listx

# PROVIDE NAME OF FILE TO DUMP
def fileNameGiver():
    year = date_scraped.year
    month = dt.strftime(date_scraped, r'%b').lower()
    week = date_scraped.isocalendar().week
    fileStr = f'./datasets/{year}week{week}{month}.PARQUET'
    return fileStr

if __name__=='__main__':
    T4rmP = tracksFromPlaylist()
    D4rmT = detailsFromPlaylist(allTracks=T4rmP)
    file = fileNameGiver()
    df = pandas.DataFrame(D4rmT)
    df.to_parquet(file, engine='pyarrow', index=False)
    print(f"thanks!\ndumped data to parquet successfully\nbye now!!")
