import appsAuth as aA
from datetime import datetime as dt
import time
import pandas
date_scraped = None
sp = aA.spotipyAuthenticator()

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
            # get details from track variable
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
        # obtain next paginated results after scraping
        if playlistJson.get('next'):
            playlistJson = sp.next(playlistJson)
        else:
            playlistJson = None
    deduplTracks = tuple(set(finalTracks))
    return deduplTracks

# COMBINE ALL TRACKS GOTTEN AND GET DETAILS
def detailsFromTracks(allTracks, counter=1, listx=[]):
    print(allTracks)
    print('collecting details from each track, be patient')
    #sp2 = aA.spotipyAuthenticator()
    for track_id in allTracks:
        dictx = {}
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
        listx.append(dictx)
        if counter%10 == 0:
            time.sleep(15) 
            print(f'...track {counter} scraped with all details')
        counter += 1
    return listx

# PROVIDE NAME OF FILE TO DUMP
def fileNameGiver():
    year = date_scraped.year
    month = dt.strftime(date_scraped, r'%b').lower()
    week = date_scraped.isocalendar().week
    return f'./datasets/{year}week{week}{month}.csv'

if __name__=='__main__':
    #T4rmP = tracksFromPlaylist()
    D4rmT = detailsFromTracks(allTracks=
        ('2RcjfRvmKaVk2wlNVtzSaC', '7u0z6FcJDqkZwdpqAqUzmO', '59OGomfNJnA70zq7pQxkff', '1CBbhcNJe9yfmOJdBSqUpK', '1pt9MqNMJQUHtdTwaswwwR', '5ZWPSeh28gBYptDMZNAUAO', '5h8SBLMSZ9ycvLfNXH0vk9', '0C8RxBixBaXYc5enAXIm28', '7oWzMhT4jmC2cOV2m0OCCk', '2KGhXTEvSQ2SlW1sH9nb2h', '3owcb1QXJOHsj7u5Ayynzg', '5aYcdAo0OCkV9lxQFFWaVg', '2LP8KwtvzUx1onvXKQCoKR', '1Cek6PV24GtEk4GDWqFbCk', '0gRgQfUVHFAvWSCfr1OYf3', '4WYbYaibpIWj1FLbMUH2Yb', '4psOOvBSTGC5NE1uxvwkbz', '0OTos4FqtEgdOClbTFDg6D', '6UYzGWOLMjLd8jCae6gOgZ', '6CTWathupIiDs7U4InHnDA', '7scINjDU13FTbCakH7bf2E', '5Ime1ULtZ3BbKkTcU8spgd', '2Ydj7wgn4ZrFFQsfFBTTYJ', '1NKVlhpgU8dTgnb9uwyNYJ', '4cpxSBb2TRx8WJhQM1Jdpk', '3Cz8GII0boo08sdtHbCSNC', '3FUDYeiIvhEatAPP3AWRkS', '0vvUCHIXM3YXt0mJpNTOVY', '2k6OU00K9obF3R1eqA2mJP', '5c1rWQAa8GX8LgCC9h3d1N', '1MT5w1g81k0RyiWnXjJjIq', '6vpC9vAX6UsuxTAlclCFDd', '7nr3wqDwJkiSDbcbct67Um', '6ZYRpkPOtwG2pKDiHGJs9u', '111tsoAygUPLvjdlZF30dy', '3sKBph3ElueH1dVLmkHWZZ', '06B0pbiRWZJAfxJXu6R4wY', '2S13p9NH2CX3DDvTqazVYm', '0lYs23NNkgF1bhfWmjojO3', '5jLBhr4USswMtmsItEAFqf', '6d7Y7oakb02D3Ijq8Emgeu', '1deimiQlzca70jziGDtTsm', '4Qpa0WH8hUHtOJKSNPrGV7', '36tVdsRWDbPBekxVYEWhph', '7M3WKySNnVWCUCi85cmLAd', '0TqCqA8R4gDZ8Gup4PiFqg', '2EFZWENUR9obAK0n2BX19S', '2Gk6fi0dqt91NKvlzGsmm7', '68PdGy1jVVmzAMNSgib32M', '5E6bsNA69z9SMXM6hOWqdU', '20lVfwgZvlxYBwiPjJ19Ab', '1E9OXQIN9zhGpaVNATJTyS', '3rRKu7N2zRgb0pF9DLrrBI', '2K0ULBaljOe2NCOqtuqyxB', '6hVwoGjU2l2tHk9Cm1kEiZ', '4evzUQNNDpgP8mnlV2OVkf', '1vBqDhQhSlwr8rgIWTpCWT', '3S9FC9B3GExBXy2eIFq1tT', '21HcaFI07UjZp94DIA1PcS', '6xb2ynu4MU8TzfTKK8gL9g', '3x11dxRSmvNxq46e5IhNCO', '6DX3c5LFsm0sJE8eZezUWu', '0yTZcUtKHBc7aKrU52nyBK', '12Mel6t7zZlfn1CpmwL96L', '4uwZuF0mLw2e8wBoHC9yw2', '5kamq6BDkGnzj3HyO6KHfJ', '45xciFHk9uzfRYyAFrCQOT', '4jO4khnnFIW5PUTsSaHYmQ', '73y9Vj3ST8UfRj17wtCckA', '11JFN4b5BsGmZrCC0U7kTD', '597LY7HnUeb9n6EUFUF8uc', '6JP04ZuKnshngkHsj3LSmP', '4c3a3UMA78HUlSypLa2dJo', '1kW728xFsRBvunN1yiTsNf', '3PTKJqdK3OfK16kS56HuPb', '6fYefaw0KturTfuRNTKFbX', '5dGsXbKccVRe0HvXAv3836', '2zoZOVdfrwY359yrP8dhkD', '3sgFQajQAvJTYny1e8pJS4', '5tM3Fo4qBqDAwWJ9ZY5AtX', '4XxQgDIuVeU4drTCmrxqqd', '6bBQmflDHD8a35PeZjw44J', '0UdBaetogSoEIO7fSD1334', '2SHcPk6yW3WbS1tJGH2h8v', '3LuSjVLN13xR6WO01Mv5ta', '20QXAsEYAudrTly1EXWk1J', '4g52MWu8RhJYIkM9NdLvUN', '1kM5fFSFcsYPshdMpjp8EM', '2iblHxNHocQk2LeZqSp9P6', '0xt77zfzH4nanVb7setzY8', '4R7e4eQiLR8bYFElkWTxA1', '7nomKLY56JGEOE0N3V1yGs', '3GAu2fSg9deV207noxMKl0', '3HGnpIF3BYxqwKQ5gWdha7', '29e2gdZN35wxeGgDtkXjIa', '0Zf1H3gTJqVDG2SYvCsO9g', '2XuLnQELesgnkCGZbSJHO0', '5HM5trJxTouv3eUVcbW8sh', '14nSbMQqRo1BxshIjprVDO', '1xdaZj6LvQOCi7Cw802Gfp', '4G5IYu1QYKo7DeSecKtNXA', '5GX1wsJfvSXUobjDJgrVBD', '4YtDyhhToTqdN6HmSrLncM', '10mHj5Bo8All1K2i0TtJT3', '6m94NnMDxM5KM5Ut5vgfhR', '1YiEyKVVQK3wMlA6Tx580R', '2T5GZC1hlOr9DahCK2WnFy', '2qa0YHx8WA4wkV0qR1Su6U', '4HuciJ6VfCUkwoX4YFYj3f', '6VcPmIg0qnqtIBQoBkS2xd', '7JPweWVt1wDEu7EFwvupCo', '2YydIFWvhLpfZi4q85Gbq2', '2JyILhFSK1yopuDDxWVMFM', '652eb66Jp9rLJ3erEwaCio', '1FvYnYoGgA4VSCCQYoyYLB', '5YaLRBAkLirNXr9cOy1ojD', '5mF4ZRXmvDD33kDKIxQ6DM', '7GQWq2bKlhGTEEkXMQkloe', '3Y8PRiBMczgHn3edpbCkfb', '5mjxSIPHAMNk40q0nON5Cb', '0UJMgRVNBrnMmAeZ8p1iMc', '4GYqaST2JIrJrZwzEXYjnV', '45deBBy7lInAwEixnK3gwX', '6XBIOtdSL47qn201KKNCA0', '6PczP7McR5UyseBwf3QMBd', '3W3y3pGDnfhUQHeCoUwFLe', '1ylQVenjROC5GX2dj6X3A1', '7mE7qAkm5kvgalbtZhTQ0v', '7cGLORAFEGv5YPJsqNUz9C', '7CkDjDtJjCZA7AW7RBvrvC', '6FZlSfQrD9aoB4SSnoAzWk', '2qdwZPTNCHb8DXfQin53WK', '7AgJbXzhNAd9OZwDAb1UpU', '6U9jxxdQ6TNzjshIpwWMTf', '2YZIP6kROKip5s5C52L6u8', '5mhM7bfzv52bzfCzlq8vH1', '3ES1fBQACydIODlZmQS359', '3eWpfsYgd5OL2QdwcVcF6Q', '0UYyNBBFrseB1Nb690QKHM', '1rljbQ1Otc6S30kmrCCRRr', '5KV5UXd1uNZZafWTudrVft', '3TtLqP9g4oJc3OhaRIsxcp', '11Q7avc3GINHS2pSxso0vF', '0RPXUuLjVHolWYkaXCndXD', '4hbadZZrbM08KZIQZomWaI', '1V3I7dfERrC8ZdpasMdzfD', '1136eJrkWsDvReASbjLTaU', '2gcOLxQioot3aJEzyVQZUr', '6fUU7DGpNxZeTDgHHP2DqX', '0KV4dkrZR5EVsYD4GeAHCo', '0cnxJjQ8T4GSz87TaIkwDY', '5L845uQOeyOSSAhGPFEmLc', '5FzsdlFgAFN1aSe9YwoN6s', '1cSitFlpZlhS0KAnoH6a69', '6HTjqv0AsiZ34fOMcGCbSX', '0iZxD850qinyHVVWA25LPQ', '4KZMoDuxwSYP63bhbnMqe3', '6qS9yoAUIXNfno5t4YLQdn', '4oQ9SXKfTmAubnM06JMP5Z', '0BMOwfaleAhCJf1qABUCtd', '15NL7qizXvZEe34zPbuWL7', '4yF6ykrqb0iDtMjPtQMG8O', '0zCLxldZNgkpdmJgOpabaE', '6S2nSU6FmY2xCJFkh1lHER', '41OAbUwS3yasOZU7CGAPy7', '6akx8GkfWirUJVSiof4FYP', '6VX4hVDmDMfClxp6EwDNQP', '7wnNCOQnx3DbCE6xle3M7U', '5ksKJ5a1iawwfoCxWtImP9', '4vJI6P9T4yYb2wmsQAwOdh', '27oS8KzSVfMbsKzQrUEhEu', '3dWsXUC1wvR66VwBQx3xCd', '4Tgt15dD8P2m68HYxA8DCG', '08qxBKy7yKE4LOxZVdkfXY', '2pIQ4AKOtPukeUltnNsTWZ', '3lvs7B8Drx1i8wymacHMIF', '5q5gik45O6Zs7neeZKiStj', '2z13PLFl2jTiV2JLvQZtwI', '0ydoqpTVhaDzjDg7WVcg4m', '0RHdQDaqgDwsXQujji1TSn', '2koM4vqlpUzeRbNkjsDBwF', '35APZC4TisJJihjSDtgn3C', '4bE2eWDiGBzRgfTl5IPBW4', '21njdkZ0kJUSnY9fab1QuD', '6lrAyxpomr1dkHltiUqWSw', '5O5iEfPDhM3XKYDLMqkg6Z', '5TbF873wsjQ7sxmlsLXbBy', '2sVJp3hYRASeLQYgMxmyJd', '5IQUPSzuNlYmSzHK8fO0yH', '1rHPk2p3MQTh2wloo3P9zE', '4qm0rzVQA3kqQ0yA7LkuFK', '2q7BfsGmjmUbxn5VkI6QKN', '5F4OfeowSReF93KcH2eUcG', '0ax6l6vI9gXDmMk3ysOdbW', '6mHwUPpljnYwbzuua5jY3N', '664mVcYRMDsVnOg95R71Ti', '4wvnXoQqjIOoEis5eyTbCl', '0F98hOl7tUOTXphPzFfFX3', '6l7opVclJEHReImCPkMc5o', '3qH7uGwlgr7tmoL4ksRhPi', '6TC67clDSVsNb0dBPN6JeC', '64t5AXI4zUzkiAcDImxNx9', '2pe1Pd1IFztomzFGWK1LWr', '1RnRPPu3XPtftOhs1qF1hY', '1qxKva4IzWde7m2jLpZvDU', '78OD9RZjAyQcfsAigmRuGs', '5ZtK8XAVnoaGdBXZWCEVCY', '6kq3Twa8T9Rf9nxpf111hx', '1hNCm9UBn42kza39flUmKU', '3XmvXK6pJRewCn6mAfmsdS', '4OzS0O0i88cGeu8YklCHrT', '67KA6E6erqyx2lL3ib0mxZ', '1VQo0tmPiBdeZ2sZ8iFEmP', '6phfOLRF89L8DlEofGXVHN', '7izQcsYsMD8Z0wxyLC9SHH', '2T1jlkITIlqJETEzttebar', '35MU2MEhQMw0NhXZztAP9m', '0Y2gj3rSBjtB13CsfOnSDF', '6gHUiXF4BiJ9d7biTNmdKR', '2GpvODlXvV2dCuiaRXMbzn', '06mtMKkZiwzA1BHCTb1IBy', '6UTXf9k0H3JDus2ZZDwGpC', '1tKsfYB65Kz74yk0HMCdcH', '7IFoyt4ZL7raIETupyDCYM', '0AC5awNiTGPSP3Cbbdp5rD', '2UNdr8gnOQrVkSmLDeC59w', '5Xl9ZfRljGKcHD2Tn3UhQ4', '487d7D0DF6hPsXQmW5g8pn', '3xY9AUbeibAeVDyPkHm8Kj', '25k1dcqUAmq4uYKUFj7u3o', '3vXFxsPqMgw4SYP7fkWicM', '1IMRi5UVOV77PsAgdWDvzh', '2yIUb32c5s0cjMFuQJKTy7', '4vrMMlOtY8YKG9yLEQoumL', '3UnV8C3DyIns9oEQRt0UnZ', '6qk3jI8bKCgURI3h0d8zBZ', '4vHy2IHzf3EabEa7oMpUZB', '0ww0GM0f5USzNZidkcoCVX', '0yxmn9m8srZL6Ood6LVXfl', '2GG6ETOQ8jiXcKYrwhNi0M', '2mwNqgMNrguu5Xlns3kqeg', '3c4rB3w9UeCoZ2y5Ea954I', '0YeUYYOh25Cn57DKTC8uS4', '4EoYs4KY7oHQpJPTuxD7mU', '1edi2KPh2oghMy8ExJiFBN', '6Vn8psRFJ0V0nAddTWxJt0', '6MG8MRq1odNsWCasM9IehW', '1ow7Ba2FNoV1JNG5kQkWN2', '4tgQql47OrdwY4q2jEY2Zg', '3iiVEW0NpaDXK7svF0l4hH', '2FG5oQXJdQC5taNJxTvFKb', '3nT2nrfb3FMLg03W4mPaBl', '657Zw93nd2TAfM7umYI1P0', '731NDNG7VQOA2KBnS43jqr', '2gZ8kkkiycGErViJ5bu5PO', '4Xik88j0lef96PqxYFR66a', '6PdAiqbKP3Zmr3YHRdgT1y', '1s2FsIDYlX6nhQ6UXF4V2w', '4kxs4dsvMpeOPohBOvJzwr', '156RL4iswD6wyO7mznamFL', '2JtrWZrpNkbSEzG5m9phAV', '3IvE1iyRbBProcJDsHBsnH', '3js04Z5R4L1ZvtLPopSG8l', '1w8XryfrrR7rXSo5GscZ5f', '77q3rIpcqFsTo7qNvKNiOh', '1DZDwhLAc9Jh6YvZ5pNINv', '13VXuHw3O8Yt7VwRIDqSo4', '1I08zQMc1sHy2xwd8itedV', '75c5cm8y5Fzb6aTZM3MOpN', '0ohCXfOYVw5om6ZK26LGXd', '0vzmD1DurX0MZLERNZUqNu', '0WeU5EfNFu1wmlmCdMNDEJ', '0s3NyWRBLiqsj1tfTidSpU', '74CA9T8IpFzrLNFV6EoY3a', '7fA7mrYaXVDVVGCAV65NRN', '3rGBlf0cp7M3jbpsghlOH3', '3MldGIMtPcupNBI4Dnxolr', '3ovSaVUTDOtxfDw5xh9qJ4', '7papu4e31nzof4krM4DEnr', '5gL8d9dzG8wU4BYgJOGy0B', '1GLx5tpDdwEFiA7KaikvX2', '3zBoEiwCaAVnQDE9JvoHm5', '0dEFhHjGparc3MPlejuJ0e', '67LfIhq2SHRtaUqp4ue368', '1kxu6GYmdIdEATyPLBDAc0', '2lM7orFD058wiAiBixzffm', '3jEm22vZwLH6CelxDOtl5s', '2H0w7oYDjUvgsFlNQ5swIg', '0QH5o3AbDV3TGdXErrOpX1', '2QPwDdwmilPQTkPwSOUnqT', '60qIa2znv2BICoDyJS8rNv', '6ZBXya9ewPZa6zXDRfPhog', '5gGB277HfBuamx9TbdaNjL', '2ePVcmvh7t6ILzeXeGImNd', '5i16HfVleOCQPwDnvUlnyl', '3Aq8OvogNStehUPJcNDEZT', '4wd0CdhrJE1cA3Amvt7MeA', '4mVTl23YCrsMInBZ5exZWa', '6UYfRpkG97EjHTg0Oh0EqQ', '5psM7zuqtSaMnLr9WzI4s5', '1Qb4AOYjKD8w7BGSxVYuO7', '5O7fTE396BVFRTkQv5ENSo', '0BlBcMUDVI68fwwNGulSGM', '2isb6crrhgFJ3zxBFa5fXG', '5Ms6phtE3zdTYgNo5hlqzQ', '6vPTMGATXneg9Z1FswpDMI', '2rFPUq8a7gvO0IuaN9LpV7', '36AXjKaxwnDbBYaguLOiXA', '4GXW3Ne1jzdORKHvHjK31V', '0UIRtIY9v5b8BRZIFsvwxm', '67lhHtSEruyrHxlk3QJunD', '5dVJTSZhL2n81ZkT4PZu0x', '0GTiXml7vaGrdBubjKN79y', '4i1wik8DtU7eqSEWRsTHuP', '1YgIvHDTvi1vosins1jyAC', '1Lyo0G6hpTjWfWi8zjd9Wz', '1Z15FtYvtEXSD6P5l1GhSH', '1SiBHQQkkySXWZfARVr6Pz', '7jvvjljkMmfMEpRWQ7MxE2', '2YqYDFulNfjuE3ouXEvxAl', '7dcr2Uhxl9UvFpc1LgMVdt', '5mNEct44dKpHjEyCGVQNsF', '5POf2ZCMOY1BmGF65js1xy', '2khv04F26pnJr4989Maowi', '5JL5FbKStegRpZc7OCeRnc', '2d0ZOLvaDMTpWilxsvDKer', '5Hg17oihKUTh0BTajN4dKL', '2FCaYrweDiATqvZYDmHqlr', '16artMqVuD2b0ZGfgsHsOY', '4jcrO2T6XJ1B7hXsAEJ3ve', '6XVbwNk8cGGUrFPsYSPrYp', '3qVdyHNyr5EYAV8tYiPbT8', '7jrsxCoWlItakMhsyggv2c', '2iIfZ6XTP9lq026FaUKIQd', '409pX3u1zVMQr5GG8LUmJ3', '0Cw5y3wboBz8VTWkMkmIDo', '7g8MgU8WgI0QR0RN4Rqem3', '3qSk5TP4A8gQIsb8iNVwnx', '03Si7qWUAT675brKYfJ648', '780BUxpCmW9vOVYZsqdLLE', '4aVsQKeYOwOjHmEAYd8Kez', '31jkD22MNUrpebszwU7ZFz', '1AwhPCb0PmBTWReUSPzGwS', '46FW3Liu7MUD6yrmhPXc5C', '3GLF4uV3uS1ImSEPyhLZLp', '741bGvXuyaHaiFZrVEtLza', '3Czzw1naZtpz9cFxKtpRne', '0eeX8L0DWvGth1F6xVkvv7', '0GTFxFHRHkaihUjvrPweYa', '2hGr8Qdf5tN34XcLAb6Hu2', '6il9HYxvOPCckBBZO1EFo1', '2RMegWpDexon9pgIceLZ7O', '12jJRu9yInIX7oTxoXtM0S', '4wG7xubJwUdjvdVJvAV1d9', '4cxyQw1AKCVqa9JVSN7njk', '71prXuK7e8ke8sP1iB6iHW', '7FB5261Iv3MRbSz13HYP5l', '7o79e7ADyL2qdPUHMsosBi', '6O2hrfRRPBJ59PwKhSKFHz', '0YgAGCU3kDEMTvndL9u3Tw', '4Du46OHDaAefX56QR0S3na', '1Jj1sgeQ71UoGgetecz7mT', '0ectw8g5yRkC7GNsh6gP4h', '6w2MK8oMNDXP6iXcFf1kSm', '1OGKAJq0EG7d48X2FeNQzk', '5YEVBJnnt2qMM67NGCjEdV', '4PDy9AboUPU6yToQ9VxuhU', '0TTOsyDKykWhCh3qDd9wMY', '6odb5eJQY869V6DurgeDw9', '49NvGBWwEs9u6ILQd2snYd', '1jloWdvMh9nwHUu3mag8CL', '4JhgxVGrabIDvgqIbJjXX0', '24RnCHp1JaRJAANJXAZCPu', '1WsIk6g7dD8LZouywnzGUb', '4Ddq2ZrV5GaLs4wu9dbd76', '7wMYtt3SEquaep8sWCdQqp', '4zqRu31aWCiHeYMw9GptOO', '1bDaEMD1EmC3xQoSq0Hfce', '1kyYCsP2NRZEKkBg9wcF2c', '1zUxNj07FZ7wJOLQax3aU3', '7sFukIJffFFLwnazXIbqP5', '2yskKhqtDAHJ73obmJh8tf', '3yEPVODnT2tXcc3NN6ymIN', '5vqLQ8nrejrMf591htfM5u', '4lU9my0De9qwdzOyuWQFJH', '3sKWRWuDKm0NODw7kB8xUD', '4JDB6Rqf7lkWNx9wzs4kVb', '0AyRhLx663qekqQDLf78ta', '1FEh2VLXCzHr4DhMLufrs5', '3mVPT2RTkWxFRWjkEw8Y4y', '4L4lSdJzHNkJWjZKgHbnZr', '0GRvuyB4XNRnKjUYswt3Y8', '5apolZDeJTAfWk7cxnPnRP', '6TBpPOmLOa1mInpq3PIz6N', '1x9iAQOjMEHWZX7UeqiyWV', '6cyXHTix4NQ069gKJEYv41', '2Z5dUCDAmotABDmBl9rNk2', '3bXR4wt7A3T7OL6Wkgrzz7', '0ODCrGAuV8iSgnI8aJLznB', '3kkuduvNylAGQklZkrqZJT', '7fz52tAQ79hRZ5q5GTQ8aC', '0eqmxkeJHQs3mdOEFluYXB', '0HNQq6OQvAC7cm4vkVDox7', '2WHM3orrvvqziSkG0xp8sy', '1hVU0YUYyYvTh6cUJv9LHo', '30CGXw8n3VZlSIyQqhOtQD'))
    file = fileNameGiver()
    pandas.DataFrame(D4rmT).to_csv(file, index=False)
    print(f"thanks!\ndumped data to csv successfully\nbye now!!")
