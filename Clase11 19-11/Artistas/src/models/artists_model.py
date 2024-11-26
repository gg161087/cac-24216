from src.data.artists_db import artists

def get_all_artists():
    return artists

def get_artist(artist_id):
    return artists.get(artist_id)

def add_artist(artist_data):
    if not artists:
        id_new = 1
    else:
        id_new = int(max(artists, key=lambda x:x['id'])['id']) + 1
    artists[id_new] = artist_data

def update_artist( artist_id, artist_data):
    if artist_id in artists:
        artists[artist_id] = artist_data
        return True
    return False

def delete_artist(artist_id):
    if artist_id in artists:
        del artists[artist_id]
        return True
    return False
