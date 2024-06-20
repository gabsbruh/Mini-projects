import os
import requests
import json
import constants as c
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

def main():
    # get data from sheet
    sheet_data = requests.get(url=c.SHEETY_URL, headers=c.AUTH_HEADER)
    sheet_data = sheet_data.json()

    # look for empty iatacode and send them to FlightSearch class in order to fill it
    flight_search = FlightSearch()
    data_manager = DataManager()
    for elem in sheet_data["prices"]:
        if (len(elem["iataCode"]) == 0) or (elem["iataCode"] == "Not Found."):
            city = elem["city"]
            id = elem["id"]
            iata_code = flight_search.get_iata_code(city_name=city)
            data_manager.fill_sheet(city_id=id, iata_code=iata_code)


if __name__ == "__main__":
    main()
