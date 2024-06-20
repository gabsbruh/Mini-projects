import constants as c
import requests

class FlightSearch:
    """This class is responsible for talking to the Flight Search API.
    """
    def __init__(self):
        self.api_key = c.AMADEUS_API_KEY
        self.api_secret = c.AMADEUS_API_SECRET
        self.url_iata = c.AMADEUS_URL_IATA_CODE
        self.url_token = c.AMADEUS_URL_NEW_TOKEN
        self.api_header = self._get_new_token()
    
    def _get_new_token(self):
        head ={
            "content-type": 'application/x-www-form-urlencoded',
        }
        params = {
            "grant_type": "client_credentials",
            "client_id": c.AMADEUS_API_KEY,
            "client_secret": c.AMADEUS_API_SECRET,
        }
        try:
            response = requests.post(url=self.url_token, data=params, headers=head)
        except:
            raise Exception("You have reached the allowed number of API calls for today.")
        print(response.text)
        response = response.json()
        token = "Bearer " + response["access_token"]
        updated_header = {"Authorization": token}
        return updated_header
    
    def get_iata_code(self, city_name):
        params ={
            "keyword": city_name,
            "max": 1,
            "include": "AIRPORTS",
        }
        response = requests.get(url=self.url_iata, params=params, headers=self.api_header)
        try:
            code = response.json()["data"][0]['iataCode']
        except (KeyError, IndexError):
            return "Not Found."
        
        return code
    