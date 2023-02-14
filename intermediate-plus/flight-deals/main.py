# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.

from pprint import pprint

from data_manager import DataManager
from flight_search import FlightSearch
from prices import prices

data_manager = DataManager()
flight_search = FlightSearch()

# Will not work because of insufficient requests
# sheet_data = data_manager.get_sheet_data()

sheet_data = prices
# pprint(sheet_data)

for entry in sheet_data:
    if entry["iataCode"] == "":
        entry["iataCode"] = flight_search.get_iata_code(entry["city"])
        flight_data = flight_search.find_flight(entry["iataCode"])
        # print(f"Flight from {flight_data.origin_city} ({flight_data.origin_airport}) to "
        #       f"{flight_data.destination_city} ({flight_data.destination_airport})")
        # print(f"Departure: {flight_data.out_date}")
        # print(f"Return: {flight_data.return_date}")
        # print(f"Price: £{flight_data.price}")
        # print("---------------------")

# pprint(sheet_data)

# Will not work because of insufficient requests
# data_manager.update_sheet_data(sheet_data)
