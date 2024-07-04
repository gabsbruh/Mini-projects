import os

# connect with spreadsheet
AUTH_TOKEN = os.environ.get('SHEETY_BEARER_TOKEN')
SHEETY_URL = os.environ.get('SHEETY_URL_2')
USERS_SHEETY_URL = SHEETY_URL.replace('prices', 'users')
AUTH_HEADER = {'Authorization': AUTH_TOKEN}

# connect with amadeus api to search for flights
AMADEUS_API_KEY = os.environ.get("AMADEUS_API_KEY")
AMADEUS_API_SECRET = os.environ.get("AMADEUS_API_SECRET")
AMADEUS_URL_IATA_CODE = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
AMADEUS_URL_NEW_TOKEN = "https://test.api.amadeus.com/v1/security/oauth2/token"
AMADEUS_URL_FLIGHTS = "https://test.api.amadeus.com/v2/shopping/flight-offers"

# specifications for flights
ADULTS = 1
MAX_PERIOD_MONTHS = 3
CURRENCY = 'PLN'
DEFAULT_ORIGIN_CODE = 'KRK'

# API LIMITS
PERIOD = 0.5 # time in seconds
RATE = 1 # rate per period

# my email
MY_EMAIL = os.environ.get('MY_EMAIL')
PASS = os.environ.get('EMAIL_SECRET')
