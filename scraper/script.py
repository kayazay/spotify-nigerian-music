from appsAuth import SpotifyOperation, SpotifyPlaylistJobs
sptfyOp = SpotifyOperation()
sptfyjob = SpotifyPlaylistJobs()


from datetime import datetime as dt
import time
import pandas
date_scraped = None

# SCRAPE TRACKS FROM PLAYLIST
def tracksFromPlaylist(counter=1, finalTracks=[]):
    print('first entry into playlist, getting items now')
    playlistJson = sptfyjob.playlist_tracks()
    global date_scraped
    while playlistJson:
        # iterate over each item in the playlist
        for item in playlistJson.get('items')[:1]:
            added_at = item.get('added_at').split('T')[0]
            date_scraped = dt.strptime(added_at, r'%Y-%m-%d')
            track = item.get('track')
            # get details from track variable
            deetTracks = [track.get('id')]
            artist_json = track.get('artists')
            artist_ids = [artist.get('id') for artist in artist_json]
            # get recommended tracks from seed parameters
            for recommended in sptfyjob.recommendations(
                GENRES=['afrobeats','nigerian pop'], 
                ARTISTS=artist_ids[:2],
                TRACKS=deetTracks,
                LIMIT=5
            ).get('tracks'):
                deetTracks.append(recommended.get('id'))
            if counter % 10 == 0:
                time.sleep(15)
                print(f'...track {counter} scraped with {len(deetTracks)} total')
            counter += 1
            finalTracks += deetTracks
        # obtain next paginated results after scraping
        if playlistJson.get('next'):
            playlistJson = sptfyjob.next(playlistJson)
        else:
            playlistJson = None
    deduplTracks = tuple(set(finalTracks))
    return deduplTracks

# COMBINE ALL TRACKS GOTTEN AND GET DETAILS
def detailsFromTracks(allTracks, counter=1, listx=[]):
    print('collecting details from each track, be patient')
    for track_id in allTracks:
        sptfyOp.gettrackid(track_id)
        sptfyOp.track() 
        sptfyOp.artist()
        sptfyOp.audio()
        sptfyOp.api4ovh()
        # merge all three dictionary together
        finaldict = sptfyOp.finaldict
        finaldict['added_at'] = date_scraped
        print(f"{finaldict['track']} scraped with details and progress is {counter}")
        if counter % 25 == 0:
            print('...sleeping for 10 seconds now')
            time.sleep(10)
        listx.append(finaldict)
        counter += 1
    return listx

# PROVIDE NAME OF FILE TO DUMP
def fileNameGiver():
    year = date_scraped.year
    month = dt.strftime(date_scraped, r'%b').lower()
    week = date_scraped.isocalendar().week
    return f'./datasets/{year}week{week}{month}.csv'


if __name__=='__main__':
    T4rmP = tracksFromPlaylist()
    D4rmT = detailsFromTracks(T4rmP)
    file = fileNameGiver()
    pandas.DataFrame(D4rmT).to_csv(file, index=False)
    print(f"thanks!\ndumped data to {file} successfully\nbye now!!")

# end