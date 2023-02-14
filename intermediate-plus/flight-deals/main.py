# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.

from pprint import pprint

from data_manager import DataManager
from flight_search import FlightSearch
from prices import prices

data_manager = DataManager()
flight_search = FlightSearch()

# Uncomment when sheety requests are restored
# sheet_data = data_manager.get_sheet_data()

sheet_data = prices
pprint(sheet_data)

for entry in sheet_data:
    if entry["iataCode"] == "":
        entry["iataCode"] = flight_search.get_iata_code(entry["city"])

pprint(sheet_data)

# data_manager.update_sheet_data(sheet_data)
