from dotenv import load_dotenv
from os import environ

# get properties constants
DEF_URL = "https://gethome.pl/mieszkania/do-wynajecia/"
BASE_URL = "https://gethome.pl"

# params price and location to find
MAX_PRICE = 3000
LOCATION = "Krakow"

load_dotenv()

GOOGLE_FORM_LINK = environ['forms_link']
