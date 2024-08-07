import requests
import constants as c
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import base64

# with spotipy create its composition in own class
class SpotifyManager:
    """Correspond with Spotify API
    """
    def __init__(self):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=c.SPOTIFY_CLIENT_ID,
                client_secret=c.SPOTIFY_CLIENT_SECRET,
                redirect_uri="https://example.org/callback",
                scope="playlist-modify-private ugc-image-upload",
                cache_path="token.txt",
                show_dialog=True,
            )
        )
        self.user_id = self.sp.current_user()["id"]
    
    def search_for_song(self, song_name, song_author, year):
        # I withdrew searching by arist due to the plenty of unsuccessful searches
        searching_result = self.sp.search(q=f"track:{song_name} year:{year}", type="track")
        try:
            uri = searching_result["tracks"]["items"][0]["uri"]
        except IndexError:
            print(f"'{song_name}' by '{song_author}' doesn't exist on Spotify. It will be skipped in further process.")
            return None
        else:
            return uri
    
    def create_playlist(self, date, is_public=False):
        year, month, day = date.split("-")
        chic_date = f"{day}.{month}.{year}"
        playlist_name = f"{chic_date} Billboard Hot 100™"
        description = f"Auto-generated playlist containing all blockbusters from the Billboard chart dated {chic_date}"
        new_playlist = self.sp.user_playlist_create(user=self.user_id,
                                     name=playlist_name,
                                     public=is_public,
                                     description=description
                                     )
        # get playlist id to instance variable
        try:
            self.playlist_id = new_playlist["id"]
            self.playlist_url = new_playlist["external_urls"]["spotify"]
        except IndexError:
            raise Exception("Playlist was not created. See details in json response")
            print(new_playlist)
        
    def upload_playlist_cover_image(self, cover_image_path: str):
        def jpg_to_base64_format(image_path):
            # encode image from jpg to base64 stream format
                with open(image_path, 'rb') as image_file:
                    image_data = image_file.read()
                    base64_encoded_data = base64.b64encode(image_data)
                    base64_string = base64_encoded_data.decode('utf-8')
                    return base64_string
        
        cover_image_encoded = jpg_to_base64_format(cover_image_path)
        self.sp.playlist_upload_cover_image(playlist_id=self.playlist_id,
                                            image_b64=cover_image_encoded)
    
    def add_tracks(self, tracks_uri: list):  
        self.sp.user_playlist_add_tracks(user=self.user_id, 
                                         playlist_id=self.playlist_id, 
                                         tracks=tracks_uri, 
                                         )
