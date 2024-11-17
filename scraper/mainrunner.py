from appsAuth import CustomSpotify
from dc import SpotifyData
from datetime import datetime as dt
import time, pandas

# SCRAPE TRACKS FROM PLAYLIST
print('first entry into playlist, getting items now')
tracks_pl_rcm, cs = set(), CustomSpotify()
plItems = cs.playlist_tracks()
for item in plItems:
    gettrack = item.get('track').get('id')
    getartist = item.get('track').get('artists')
    for recommended in cs.recommendations(gettrack, getartist):
        tracks_pl_rcm.add(recommended.get('id'))
        tracks_pl_rcm.add(gettrack)
    time.sleep(5.0)
    break

# COMBINE ALL TRACKS GOTTEN AND GET DETAILS
final_spotify_data, added_at, cs = [], dt.now().date(), CustomSpotify()
print('collecting details from each track, be patient')
for count, tid in enumerate(tracks_pl_rcm):
    track, artist, audio = cs.track(tid)
    rowdata = SpotifyData(added_at, track, artist, audio)
    final_spotify_data.append(rowdata.todict())
    time.sleep(5.0)
    if count % 50 == 0: print(f"progress: {count} tracks")

# PROVIDE NAME OF FILE TO DUMP
f = f"./datasets/{added_at.year}week{added_at.isocalendar().week}{added_at.strftime('%b')}.csv"
df = pandas.DataFrame(final_spotify_data)
df.to_csv(f.lower(), index=False)
print(f"dumped {len(final_spotify_data)} tracks to {f} successfully\nbye now!!")
