import requests
import constants as c
from collections import namedtuple
from user import User

class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    def __init__(self):
        self._auth = c.AUTH_HEADER
        self._url = c.SHEETY_URL
        self._users_url = c.USERS_SHEETY_URL
        self._users = self._get_users_info()
        
    def _get_users_info(self):
        """Get data about users of application, consist of names and emails
        """
        users_data = requests.get(url=self._users_url, headers=self._auth)
        users_data = users_data.json()
        users_list = [User(name=user['whatIsYourFirstName?'],
                           surname=user['whatIsYourLastName?'],
                           email=user['whatIsYourEmail?'])
                      for user in users_data['users']]
        return users_list

    def get_data(self) -> dict:
        """Get data from sheet.
        
        Returns:
            dict: json with all data.
        """
        sheet_data = requests.get(url=self._url, headers=self._auth)
        return sheet_data.json()
        
    def fill_iata_codes(self, city_id, iata_code):
        """fill iata code inside sheet

        Args:
            city_id (int): number of row inside spreadsheet in which iata code will be changed
            iata_code (str): iata_code
        """
        put_params = {
            "price":{
                "iataCode": iata_code,
            }         
        }
        try:
            response = requests.put(url=f"{self._url}/{city_id}", json=put_params, headers=self._auth)
        except response.status_code != 200:
            print('There was a problem with filling iata codes.')
            print(response.text)
    
    def fill_cheapest_info(self, city_id, info):
        """fill info about cheapest flight on specified destination

        Args:
            city_id (int): number of row inside spreadsheet in which iata code will be changed
            info (dict): info about cheapest flight, including dates, pricing, carrier
        """
        put_params = {
            "price":{
                "cheapest": info['price'],
                "departureDate": info['departureDate'],
                "arrivalDate": info['arrivalDate'],
                "departureCarrier": info['departureCarrier'],
                "arrivalCarrier": info['arrivalCarrier']
            }         
        }
        try:
            response = requests.put(url=f"{self._url}/{city_id}", json=put_params, headers=self._auth)
        except response.status_code != 200:
            print('There was a problem with filling info about flights.')
            print(response.text)
        else:
            print('Filling sheet succeded.')

    @property
    def users(self):
        return self._users
