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
        pass        self.sp = spotipy.Spotify(
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
    
