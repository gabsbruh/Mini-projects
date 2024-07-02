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
    data_manager = DataManager()
    sheet_data = data_manager.get_data()

    # look for empty iatacode and send them to FlightSearch class in order to fill it
    flight_search = FlightSearch()
    for elem in sheet_data["prices"]:
        if (len(elem["iataCode"]) == 0) or (elem["iataCode"] == "Not Found."):
            city = elem["city"]
            id = elem["id"]
            iata_code = flight_search.get_iata_code(city_name=city)
            data_manager.fill_sheet(city_id=id, iata_code=iata_code)


if __name__ == "__main__":
    main()


### XXX:
""" Aktualnie apka znajduje najtanszy lot w podanym przedziale dat, na podstawie wyszukiwania
dla jednego destination (flight_data i tam jest instancja dla PAR i   price 2000)

Rate limit wciaz nie jest dobrany, srednio raz na 10 calli wyskakuje proglem (mimo ze jest ustawiony ponizej
wymaganego na amadeus api, moze trzeba zmniejszyc period do 100ms i 1 call)

kolejny krok to zautomatyzowanie wyszukiwania najtanszych lotow
"""