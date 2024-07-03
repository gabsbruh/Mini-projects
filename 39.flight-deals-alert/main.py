import os
import requests
import json
import constants as c
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch

def main():
    # get data from sheet
    data_manager = DataManager()
    sheet_data = data_manager.get_data()

    # look for empty iatacode and send them to FlightSearch class in order to fill it
    flight_search = FlightSearch()
    for elem in sheet_data["prices"]:
        if (len(elem["iataCode"]) == 0) or (elem["iataCode"] == "Not Found."):
            city = elem["city"]
            id = elem["id"]
            iata_code = flight_search.get_iata_code(city_name=city)
            data_manager.fill_iata_codes(city_id=id, iata_code=iata_code)

    # get refreshed data from sheet
    sheet_data = data_manager.get_data()

    # pass info from sheet data to the flight_data to look for cheapest flights
    for destination in sheet_data["prices"]:
        
        flight_data = FlightData(max_price=destination['maxPrice'], 
                                 destination_code=destination['iataCode'])
        info_cheapest = flight_data.get_cheapest_flight(min_days=destination['minimumDays'],
                                        max_days=destination['maximumDays'])
        data_manager.fill_cheapest_info(city_id=destination['id'], info=info_cheapest)
    
if __name__ == "__main__":
    main()