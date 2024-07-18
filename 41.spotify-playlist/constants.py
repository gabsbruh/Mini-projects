from dotenv import load_dotenv
from datetime import datetime
from os import environ

# load envi(ronment variables
load_dotenv()

# spotify manager
SPOTIFY_CLIENT_SECRET = environ["client_secret"]
SPOTIFY_CLIENT_ID = environ["client_id"]
SPOTIFY_TOKEN = 'https://accounts.spotify.com/api/token'

FIRST_BILLBOARD_CHART = datetime(1958, 8, 4)
LINK = "https://www.billboard.com/charts/hot-100/"
