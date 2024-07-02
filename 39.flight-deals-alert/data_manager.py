import requests
import constants as c

class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    def __init__(self):
        self.auth = c.AUTH_HEADER
        self.url = c.SHEETY_URL
        
    def fill_sheet(self, city_id, iata_code):
        """fill iata code inside sheet

        Args:
            city_id (int): number of row inside spreadsheet in which iata code will be changed
            iata_code (string): iata_code
        """
        put_params = {
            "price":{
                "iataCode": iata_code,
            }         
        }
        try:
            response = requests.put(url=f"{self.url}/{city_id}", json=put_params, headers=self.auth)
        except response.status_code != 200:
            print('There was a problem with retrieving data.')
            print(response.text)
    
    def get_data(self) -> dict:
        """Get data from sheet.
        
        Returns:
            dict: json with all data.
        """
        sheet_data = requests.get(url=self.url, headers=self.auth)
        return sheet_data.json()
        
