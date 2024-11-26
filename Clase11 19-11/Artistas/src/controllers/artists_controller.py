from src.models.artists_model import get_all_artists, get_artist, add_artist, update_artist, delete_artist
from src.view.artists_view import show_artists, show_artist, artist_added, artist_updated, artist_deleted, prompt_artist_id, show_artist, prompt_artist_data, artist_not_found

def show_all_artists():
    artists = get_all_artists()
    show_artists(artists)

def show_artist_by_id():
    artist_id = prompt_artist_id()
    artist = get_artist(artist_id)
    show_artist(artist)

def create_artist():        
    artist_data = prompt_artist_data()
    add_artist(artist_data)
    artist_added()

def update_artist():
    artist_id = prompt_artist_id()
    artist_data = prompt_artist_data()
    if update_artist(artist_id, artist_data):
        artist_updated()
    else:
        artist_not_found()

def delete_artist():
    artist_id = prompt_artist_id()
    if delete_artist(artist_id):
        artist_deleted()
    else:
        artist_not_found()
