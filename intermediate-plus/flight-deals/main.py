# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.

from pprint import pprint

from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_sheet_data()

for entry in sheet_data:
    if entry["iataCode"] == "":
        entry["iataCode"] = flight_search.get_iata_code()

data_manager.update_sheet_data(sheet_data)