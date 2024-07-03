import constants as c
import requests
from ratelimit import limits, sleep_and_retry

class FlightSearch:
    """This class is responsible for talking to the Flight Search API.
    """
    def __init__(self):
        self.api_key = c.AMADEUS_API_KEY
        self.api_secret = c.AMADEUS_API_SECRET
        self.url_iata = c.AMADEUS_URL_IATA_CODE
        self.url_token = c.AMADEUS_URL_NEW_TOKEN
        self.url_flights = c.AMADEUS_URL_FLIGHTS
        self.api_header = self._get_new_token()
    
    @sleep_and_retry
    @limits(calls=c.RATE, period=c.PERIOD)
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
        except response.status_code != 200:
            print(response.status_code)
            print(response.text)
        response = response.json()
        token = "Bearer " + response["access_token"]
        updated_header = {"Authorization": token}
        return updated_header
    
    @sleep_and_retry
    @limits(calls=c.RATE, period=c.PERIOD)
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
    
    @sleep_and_retry
    @limits(calls=c.RATE, period=c.PERIOD)
    def check_flight(self, olc: str, dlc: str, dep_date: str, 
                     ret_date: str, adults: int, max_price: float, 
                     nonStop: bool=True, currency: str='PLN', 
                     travel_class: str = 'ECONOMY') -> dict:
        """Function send api call to the amadeus api in order to look for flights in specified data.

        Args:
            olc (str): city/airport IATA code from which the traveler will depart 
            dlc (str): city/airport IATA code to which the traveler is going
            dep_date (str): the date YYYY-MM-DD on which the traveler will depart from the origin to go to the destination.  
            ret_date (str): the date YYYY-MM-DD on which the traveler will depart from the destination to return to the origin. 
            adults (int): the number of adult travelers 
            max_price (float): maximum price per traveler.
            nonStop (bool, optional): The search will find only flights going from the origin to the destination with no stop in between. Defaults to True.
            currency (str, optional): The preferred currency for the flight offers. Default to 'PLN'.
        Returns:
            dict: json with data about flights
        """
        call_params = {
            'originLocationCode': olc,
            'destinationLocationCode': dlc,
            'departureDate': dep_date,
            'returnDate': ret_date,
            'adults': adults,
            'travelClass': travel_class,
            'nonStop': str(nonStop).lower(), # there was problems with bool titlecase
            'currencyCode': currency,
            'maxPrice': max_price,
            'max': 5
        }
        json_ = requests.get(url=self.url_flights, params=call_params, headers=self.api_header)
        if json_.status_code == 200:
            return json_.json()
        else:
            print('Fligths response code: ', json_.status_code)
            
            print(json_.text)
            
            print("""\nThere was a problem with search. 
                  For further information, please visit: 
                  https://developers.amadeus.com/self-service/apis-docs/guides/developer-guides/common-errors/""")
            return None
